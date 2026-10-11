# input_2 的统一采集与验证

`input_2` 是全部 395 个经典 Defects4J 案例的重新采集版。原 `input` 保留。
六个项目分别为 Chart 26、Closure 133、Lang 65、Math 106、Mockito 38、Time 27。
这里的“统一”指候选生成算法、证据提取方式、验收条件和文件结构一致；历史项目所需的依赖、JDK 和平台兼容处理按案例记录。

## 每个案例执行的步骤

1. 从 Defects4J 官方仓库包导出指定固定版本，并应用官方 fixed-to-buggy 源码补丁。必要的历史目录及编译兼容处理见下文。
2. 用同一个 tree-sitter Java 提取器枚举生产源码中声明的方法、构造器和字段，并提取测试方法及继承关系。
3. 编译生产源码与每个官方触发测试所需的测试类。候选选择不读取修复位置或参考答案。
4. 单独运行每个触发测试：先无覆盖插桩复现失败，再通过同一个 ASM 方法入口 agent 采集执行记录。
5. 要求两次运行均执行指定测试、恰好失败一次且没有忽略测试，并核对存档失败类型、错误信息和应用栈位置。随机值与时间值的特例使用明确的语义条件；原始结果完整保留。
6. 将运行条目映射至声明的方法，取所有触发测试的并集。包括显式构造器、setup/teardown 和类初始化过程中调用的普通方法；不把隐式构造器、合成/桥接方法、类初始化块加入候选。
7. 生成统一的十个输入文件，按与标签无关的确定性顺序排列候选。每个案例最多预测五个候选，与失败测试数量无关。

JUnit 结束后运行器正常退出 JVM，由 agent 的 shutdown hook 写出覆盖记录，避免后台线程空闲等待改变采集边界。完整失败报告来自 Defects4J 存档；本次新执行的堆栈与覆盖证据另存，均经过复现校验。

## 文件位置

| 位置 | 内容 |
|---|---|
| `../input_2/cases/<项目_编号>/` | 定位 agent 使用的十个输入文件 |
| `../input_2/manifest.json` | 395 个案例的候选数、失败测试数与文件哈希 |
| `coverage_evidence/`、`coverage_audit/` | 每个触发测试的原始命中、无插桩/插桩日志及校验结果 |
| `source_audit/`、`source_provenance.json` | 源码版本、源补丁和提取审计 |
| `collection_protocol.json` | 统一流程、工具哈希、兼容处理与随机测试验收规则 |
| `ground_truth.json`、`reference_audit/` | 官方补丁到方法的统一参考映射及未映射修改 |
| `build_summary.json`、`VALIDATION.json` | 构建统计与发布校验结果 |
| `original_input_integrity.json` | 原 input 的完整性核对 |

`ground_truth_patch.json` 与本版主参考使用相同的官方补丁映射，保留此文件名用于兼容原评估脚本。映射先在完整源码方法集合上完成，再与实际覆盖候选取交集，避免把未覆盖的内层方法标签转移给外层方法。没有候选内参考方法的案例仍保留在 395 个案例及评估分母内。

不要把本 `evaluation_2` 文件夹或构建缓存提供给故障定位 agent。候选编号、输入哈希与原版本可能变化；旧预测文件不能直接复用。

## 历史环境兼容

兼容处理不是另一套候选筛选策略，均不根据参考答案选方法。

- Lang_2、Time_21 使用 Java 7 运行；Lang_15 用 Java 7 编译测试，以保留旧泛型推断行为。
- 早期 Lang 的 `enum` 包和同名局部变量使用编译副本改名；Lang_44 至 Lang_47 的旧 BigDecimal 调用增加与旧接口运行时转换等价的显式类型转换。输入保留原声明，编译副本及哈希另记。
- Lang_48 在源补丁之前应用 Defects4J 官方 `test-44-48.diff` checkout 修正；Time_22 至 Time_27 按官方钩子去掉 `JodaTime/` 外层目录。
- Chart_19 仓库中的 `itext-2.0.6.jar` 实际为 HTML 错误页，使用官方 Chart_10 快照内同版本完好文件。JUnit 依赖版本按历史断言行为选择。
- Closure_26 的内存 JavaScript 模块路径需要 POSIX 分隔符；无插桩和插桩两次运行均使用同一适配运行器，保留 Windows 原生磁盘路径处理。生产源码未为此改写。
- Mockito_5 延续新增 42 个案例采用的测试类加载辅助代码路径分隔符修正。

少数随机/时钟测试不可能要求每次错误中的数字完全相同。本版只对明确列出的测试接受受限语义匹配，并继续要求相同失败类型与应用栈位置；规则见 `collection_protocol.json` 和 `tools/collect_method_coverage.py`。未对任意错误或任意数字放宽匹配。

## 复用本机缓存重建

源码与大型构建缓存位于 `D:/codex_uniform395`；JDK 和 Defects4J 根路径在各案例审计中记录。

```powershell
python evaluation_2/tools/prepare_uniform_sources.py --cache D:/codex_uniform395/cache --d4j ${USER_HOME}/Desktop/defects4j-master/defects4j-master --repos D:/codex_uniform395/repos --jdk ${USER_HOME}/Desktop/codex_data/evaluation/coverage_runtime/jdk8u504-b01 --svnkit D:/codex_uniform395/svnkit --workers 4
python evaluation_2/tools/collect_uniform.py --cache D:/codex_uniform395/cache --d4j ${USER_HOME}/Desktop/defects4j-master/defects4j-master --jdk ${USER_HOME}/Desktop/codex_data/evaluation/coverage_runtime/jdk8u504-b01 --jdk7 D:/codex_method_coverage/runtime/zulu7.56.0.11-ca-jdk7.0.352-win_x64 --runtime D:/codex_uniform395/runtime_final --runs D:/codex_uniform395/runs --workers 4 --force
python evaluation_2/tools/assemble_uniform.py --cache D:/codex_uniform395/cache --d4j ${USER_HOME}/Desktop/defects4j-master/defects4j-master --coverage D:/codex_uniform395/runs
python evaluation_2/tools/validate_release.py
```

本次仅构建并校验定位输入和参考，没有运行 Codex 故障定位实验。
