import json
from pathlib import Path
import sys


def emit(value):
    print(json.dumps(value, ensure_ascii=False), flush=True)


args = sys.argv[1:]
model = args[args.index("--model") + 1]
cwd = str(Path.cwd())
prediction = json.loads(Path("prediction_template.json").read_text(encoding="utf-8-sig"))
candidate = Path("candidate_index.tsv").read_text(encoding="utf-8-sig").splitlines()[1].split("\t")[0]
prediction["ranking"] = [{"rank": 1, "candidate_id": candidate, "reason": "offline fake"}]
session = "offline-qwen-session"
emit({"type": "system", "subtype": "init", "session_id": session, "cwd": cwd,
      "tools": ["read_file", "structured_output"], "model": model,
      "permission_mode": "plan", "qwen_code_version": "0.25.0-fake"})
emit({"type": "assistant", "session_id": session, "parent_tool_use_id": None,
      "message": {"model": model, "content": [
          {"type": "tool_use", "id": "read-1", "name": "read_file",
           "input": {"file_path": "TASK.md"}}],
          "usage": {"input_tokens": 1000, "cache_read_input_tokens": 200,
                    "output_tokens": 100, "total_tokens": 1100}}})
emit({"type": "user", "session_id": session, "parent_tool_use_id": None,
      "message": {"content": [{"type": "tool_result", "tool_use_id": "read-1",
                                "is_error": False, "content": "ok"}]}})
emit({"type": "assistant", "session_id": session, "parent_tool_use_id": None,
      "message": {"model": model, "content": [
          {"type": "tool_use", "id": "structured-1", "name": "structured_output",
           "input": prediction}],
          "usage": {"input_tokens": 1200, "cache_read_input_tokens": 800,
                    "output_tokens": 200, "total_tokens": 1400}}})
emit({"type": "result", "subtype": "success", "session_id": session,
      "parent_tool_use_id": None, "is_error": False, "duration_ms": 20,
      "duration_api_ms": 10, "num_turns": 2, "result": json.dumps(prediction),
      "structured_result": prediction,
      "usage": {"input_tokens": 2200, "cache_read_input_tokens": 1000,
                "output_tokens": 300, "total_tokens": 2500}, "permission_denials": []})

