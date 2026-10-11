# Qwen Code 故障定位实验

本目录是可独立运行的 Qwen Code 实验实现，不依赖 GPT 或 DeepSeek 目录。
`_runner_base.py` 只提供本运行器需要的通用文件、哈希、锁和进程辅助函数。

正式条件固定为：

- Harness：Qwen Code 0.25.0
- Provider：Alibaba Model Studio（DashScope OpenAI-compatible）
- 模型：`qwen3.8-max`
- 推理强度：`xhigh`
- 案例：`input_2` 清单中的 395 个唯一案例
- 重复：每例 1 次；默认串行；每例最多 3 次尝试（首次 + 2 次外层重试）
- 模式：仅定位和资源统计；定位期间不读取 `evaluation_2`

每个案例只复制当前案例的 10 个输入证据文件到独立工作目录。Qwen Code 以
`--bare --approval-mode plan` 运行，且仅允许 `read_file` 与 `structured_output`；
禁用编辑、Shell、代理和目标管理工具。该限制不是 OS 级读取边界，因此严格读取隔离
标记为 `not_verified`，不宣称已验证。

## 正式运行

以下命令均从项目根目录执行。第一条仅校验并冻结计划，不调用模型：

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only
```

首次启动：

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only `
  --execute
```

断点恢复：

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only `
  --resume
```

仅重建资源汇总（不调用模型）：

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only `
  --summarize
```

成功且预测有效的案例在恢复时跳过；失败、无效或中断案例从下一次 attempt 继续。
认证失效、额度错误或系统性配置错误会保存现有进度并停止批次，不会把后续案例批量
记成失败，也不会尝试规避额度限制。

## 实时进度条

在另一个 PowerShell 窗口执行以下命令。监视器只读取落盘状态，不获取实验锁，也不
调用模型；按 `Ctrl+C` 只会关闭进度条，不会停止后台实验。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\experiment_runner\qwen\watch_progress.ps1
```

## 独立评估

仅在 395 例预测全部冻结后执行。此阶段会读取参考答案，但不会调用模型或修改预测：

```powershell
python .\evaluation_2\score.py `
  --truth .\evaluation_2\ground_truth.json `
  --predictions .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only\predictions\qwen3_8_max_xhigh\repeat_01 `
  --cases-file .\evaluation_2\all395.txt `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only\evaluation\scores395.json

python .\experiment_runner\qwen\evaluate_results.py `
  --scores .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only\evaluation\scores395.json `
  --results .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only\results.json `
  --summary .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only\summary.json `
  --runtime .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only\runtime.json `
  --truth .\evaluation_2\ground_truth.json `
  --score-script .\evaluation_2\score.py `
  --score-core .\evaluation_2\score_core.py `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only\evaluation
```

## 资源口径

输入 Token 已包含缓存命中输入；总 Token 只按输入 + 输出计算，缓存 Token 不重复相加。
Qwen Code 未单独提供推理 Token 和内部连接重试事件时均保留 `null`。费用按冻结的官方
中国内地（北京）价格及逐请求 Token 估算，币种为 CNY，不冒充账单费用。

## 本地测试

```powershell
python -m unittest discover -s .\experiment_runner\qwen\tests -v
```
