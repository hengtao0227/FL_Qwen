import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("qwen_runner", HERE / "run_qwen_batch.py")
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


class QwenRunnerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = HERE / "config.qwen_full395.localize_only.json"
        cls.cfg, cls.available = q.read_config(cls.config)

    def test_full_plan_is_exact_and_answer_free(self):
        plan = q.build_plan(self.cfg, self.available)
        self.assertEqual(395, len(plan["jobs"]))
        self.assertEqual(395, len({row["case_id"] for row in plan["jobs"]}))
        self.assertFalse(plan["evaluation_performed"])
        self.assertFalse(plan["answer_files_accessed"])
        self.assertNotIn("evaluation_2", json.dumps(plan["file_hashes"]))
        self.assertEqual("Qwen Code", plan["harness"])
        self.assertEqual("qwen3.8-max", plan["config"]["conditions"][0]["model"])
        self.assertEqual("xhigh", plan["config"]["conditions"][0]["reasoning_effort"])

    def test_command_is_bare_read_only_and_contains_no_secret(self):
        command = q.command_for(["qwen"], self.cfg)
        text = json.dumps(command)
        for flag in ("--bare", "--no-telemetry", "--no-chat-recording", "--auth-type",
                     "--json-schema", "--output-format", "--max-wall-time"):
            self.assertIn(flag, command)
        self.assertIn("edit", command)
        self.assertIn("run_shell_command", command)
        self.assertIn("get_goal", command)
        self.assertIn("update_goal", command)
        self.assertNotIn("DASHSCOPE_API_KEY", text)

    def test_prompt_requires_structured_output_tool(self):
        prompt = Path(self.cfg["prompt_file"]).read_text(encoding="utf-8")
        self.assertIn("structured_output", prompt)
        self.assertIn("不要用普通文本回答", prompt)

    def test_event_usage_and_cost_are_not_double_counted(self):
        condition = self.cfg["conditions"][0]
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            events = root / "events.jsonl"
            rows = [
                {"type": "system", "subtype": "init", "session_id": "s", "cwd": str(root),
                 "tools": ["read_file", "structured_output"], "model": condition["model"]},
                {"type": "assistant", "parent_tool_use_id": None, "message": {
                    "content": [], "usage": {"input_tokens": 100, "cache_read_input_tokens": 40,
                                               "output_tokens": 20}}},
                {"type": "assistant", "parent_tool_use_id": None, "message": {
                    "content": [{"type": "text", "text": "presentation fragment"}],
                    "usage": {"input_tokens": 0, "cache_read_input_tokens": 0,
                              "output_tokens": 0}}},
                {"type": "result", "parent_tool_use_id": None, "is_error": False,
                 "structured_result": {}, "result": "{}",
                 "usage": {"input_tokens": 100, "cache_read_input_tokens": 40,
                           "output_tokens": 20}}
            ]
            events.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
            parsed = q.parse_qwen_events(events, condition, root)
            self.assertTrue(parsed["usage_complete"])
            self.assertEqual(1, len(parsed["usage_samples"]))
            self.assertEqual(100, parsed["usage"]["input_tokens"])
            self.assertEqual(60, parsed["usage"]["uncached_input_tokens"])
            self.assertEqual(40, parsed["usage"]["cached_input_tokens"])
            price, status, tiers = q.estimate_cost(parsed["usage_samples"], self.cfg["pricing"], True)
            self.assertAlmostEqual((60 * 12 + 40 * 1.5 + 20 * 36) / 1_000_000, price)
            self.assertEqual("estimated_from_qwen_per_request_usage", status)
            self.assertEqual(1, tiers["1000000"])

    def test_error_classification_stops_for_auth_and_quota(self):
        self.assertEqual("auth_error", q.classify_error("401 invalid api key"))
        self.assertEqual("quota_error", q.classify_error("billing_error insufficient balance"))
        self.assertEqual("quota_error", q.classify_error(
            "400 Access denied; account is not in good standing; overdue-payment"))
        self.assertIn("auth_error", q.STOP_BATCH)
        self.assertIn("quota_error", q.STOP_BATCH)

    def test_end_to_end_with_offline_fake(self):
        input_io = q.base.module_from(HERE / "input_validation.py", "fake_qwen_input_validation")
        job = {"condition_id": "qwen3_8_max_xhigh", "repeat_id": 1,
               "case_id": self.cfg["cases"][0]}
        with tempfile.TemporaryDirectory() as td:
            result = q.run_attempt([sys.executable, str(HERE / "tests/fake_qwen.py")], self.cfg,
                                   self.cfg["conditions"][0], job, Path(td) / "attempt_01",
                                   self.available, input_io, "test", os.environ.copy())
            self.assertEqual("completed", result["status"])
            self.assertTrue(result["prediction_valid"])
            self.assertEqual(2200, result["usage"]["input_tokens"])
            self.assertEqual(300, result["usage"]["output_tokens"])
            self.assertIsNone(result["usage"]["reasoning_output_tokens"])
            self.assertEqual(1, result["tool_calls"])
            self.assertAlmostEqual(.0267, result["estimated_cost_cny"])

    def test_plan_only_needs_no_key_or_cli(self):
        with tempfile.TemporaryDirectory() as td:
            result = subprocess.run(
                [sys.executable, str(HERE / "run_qwen_batch.py"), "--config", str(self.config),
                 "--out", str(Path(td) / "out")], capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("No model calls made", result.stdout)
            self.assertFalse((Path(td) / "out" / "runs").exists())


if __name__ == "__main__":
    unittest.main()
