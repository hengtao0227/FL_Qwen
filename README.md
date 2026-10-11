# Qwen3.8-Max 方法级故障定位实验

这是一个可独立上传到 GitHub 的纯净实验目录，用 Qwen Code 在 395 个 Defects4J
案例上执行方法级故障定位，并在预测冻结后独立计算 Top-1、MRR@5、Top-3、Top-5
及资源消耗。

当前仓库是**未开始状态**：`experiment_runs/qwen/` 不包含模型输出、预测、失败记录或
历史评估结果。本目录只涉及 Qwen，不包含 GPT、DeepSeek 或跨模型对比脚本。

为便于公开发布，复制过程中仅将原采集机器的个人主目录路径前缀替换为
`${USER_HOME}`；数据内容、参考答案和代码未因此改变。具体文件及替换次数记录在
`SANITIZATION_REPORT.json`。

## 固定实验条件

- Harness：Qwen Code `0.25.0`
- Provider：Alibaba Model Studio，OpenAI-compatible 接口
- 模型：`qwen3.8-max`
- 推理强度：`xhigh`
- 案例：`input_2/all395.txt` 中的 395 个唯一案例
- 重复次数：每例 1 次
- 执行方式：默认串行
- 重试：每例最多 3 次尝试（首次 + 2 次外层重试）
- 定位阶段：只读取当前案例的 `input_2` 证据，不读取 `evaluation_2`
- 评估阶段：仅在预测冻结后读取 `evaluation_2`

## 目录结构

```text
FL_Qwen_Localization_GitHub/
├─ input_2/                       # 完整的 395 例输入证据与输入清单
├─ evaluation_2/                  # 完整参考答案、覆盖证据、评分器与审计文件
├─ experiment_runner/
│  └─ qwen/
│     ├─ run_qwen_batch.py        # 定位与资源统计运行器
│     ├─ _runner_base.py          # Qwen 运行器内部公共函数
│     ├─ input_validation.py      # 输入、哈希、候选和预测格式校验
│     ├─ evaluate_results.py      # 预测冻结后的图文评估报告
│     ├─ watch_progress.ps1       # 只读实时进度条
│     ├─ prompt.txt               # 定位提示词
│     ├─ prediction.schema.json   # 结构化预测格式
│     ├─ settings.example.json    # 不含密钥的 Qwen Code 配置示例
│     ├─ config.qwen_full395.localize_only.json
│     ├─ config.qwen_pilot01.localize_only.json
│     └─ tests/                   # 不调用模型的本地测试
└─ experiment_runs/
   └─ qwen/                       # 初始为空；正式运行输出写入这里
```

`evaluation_2` 含参考答案。为了防止标签泄露，不能把它作为定位子进程的工作目录，
也不要在运行过程中用它选择案例、修改排序或重跑特定案例。运行器的计划和输入校验只依赖
`input_2`。Qwen Code 的 `--bare`/plan 模式不是操作系统级沙箱，因此严格读取隔离仍标记
为 `not_verified`。

## 环境准备

建议使用 Windows 10/11、PowerShell、Python 3.10+ 和 Qwen Code 0.25.0。

```powershell
Set-Location "$HOME\Desktop\FL_Qwen_Localization_GitHub"

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt

qwen --version
```

将 `experiment_runner/qwen/settings.example.json` 中的模型配置合并到你自己的
`$HOME/.qwen/settings.json`，并通过 Qwen Code/本机安全配置保存
`DASHSCOPE_API_KEY`。不要把真实 API Key 写入本仓库或提交到 Git。

运行器会在真正调用模型前验证：认证类型为 `openai`、模型注册为 `qwen3.8-max`、
默认推理强度为 `xhigh`，且基础地址是配置中的 Model Studio 地址。

## 1. 本地测试（不调用模型）

```powershell
python -m unittest discover -s .\experiment_runner\qwen\tests -v
python .\tools\verify_clean_repository.py
python .\tools\verify_checksums.py
```

测试覆盖 395 例清单、无答案读取、工具白名单、Token/费用口径、结构化输出、认证和
欠费停止分类，以及离线假 Harness。测试不需要 API Key。

## 2. 冻结并检查全量计划（不调用模型）

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only
```

正常输出应显示 `395 runs`、最多 `1185 attempts` 和 `No model calls made`。此步骤会
创建冻结的 `plan.json`，但不会创建 `runs/` 或调用模型。请先检查计划再执行下一步。

## 3. 启动正式实验

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only `
  --execute
```

同一输出目录有文件锁，不能同时启动两个运行器。认证失效、欠费、额度耗尽或系统性配置
错误会保存进度并停止；不要通过反复调用规避额度限制。恢复前应先解决对应账户问题。

## 4. 查看实时进度

在另一个 PowerShell 窗口执行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\experiment_runner\qwen\watch_progress.ps1
```

进度监视器以允许原子替换的共享模式读取 JSON，不会占用运行锁或触发模型调用。
按 `Ctrl+C` 只关闭进度条，不会停止实验。

## 5. 断点恢复与仅汇总

确认没有其他运行器占用目录，并解决认证/计费问题后恢复：

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only `
  --resume
```

只重建资源汇总、不调用模型：

```powershell
python .\experiment_runner\qwen\run_qwen_batch.py `
  --config .\experiment_runner\qwen\config.qwen_full395.localize_only.json `
  --out .\experiment_runs\qwen\full395_qwen3_8_max_xhigh_r1_localize_only `
  --summarize
```

成功且预测有效的案例不会重复调用。失败、无效或中断案例的恢复记录会保留在新的
attempt 中，不覆盖原始事件和 stderr。

## 6. 独立评估

只有在 `summary.json` 显示 395/395 个有效预测后才执行：

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

评估报告的主要指标是 Top-1 和 MRR@5，辅助指标是 Top-3、Top-5；同时报告时间、
Token、工具调用、重试和估算费用。费用是按冻结价格表计算的 CNY 估算，不是账单。
缓存 Token 不会重复加入总 Token；Qwen Code 未提供的推理 Token 和内部重试保持
`null`，不会填成零。

## 输出与审计

每次尝试保存原始事件、stderr、输入副本、模型/强度、输入哈希、预测、有效性、时间、
Token、工具调用、重试和失败类型。定位汇总不会产生基于参考答案的指标；只有上述独立
评估命令才读取 `evaluation_2`。

## 上传 GitHub

本目录约 823 MB，最大单文件约 15 MB；虽然没有触及 GitHub 的单文件 100 MB 限制，
首次提交和克隆仍会较慢。建议使用 Git 命令行而不是网页批量上传：

```powershell
git init
git add .
git commit -m "Add clean Qwen fault-localization experiment"
git branch -M main
git remote add origin https://github.com/OWNER/REPOSITORY.git
git push -u origin main
```

上传前请阅读 `DATA_NOTICE.md`，确认数据集及第三方源码/补丁的再分发许可。仓库没有附带
通用 LICENSE，避免错误地替第三方数据授予许可。
