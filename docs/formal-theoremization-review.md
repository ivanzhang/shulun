# 行列命题最终定理化审稿稿

统一索引见 `docs/final-interface-index.md`；若主文档历史段与该索引冲突，以索引和本文件为准。

本稿把主证明拆成“可机械验证部分”和“必须逐行证明的数学输入”。这是顶级数学期刊审稿所需的最小清晰结构。

## 定理 1（有限验证段）

对所有奇素数 `P<=floor(exp(5))=148`，`Prime-Square-Closure(P)` 成立。

**证明。** 脚本 `experiments/verify_small_prime_square.py` 对每个奇素数 `P<=148` 构造 `P×P` 方阵，逐行和逐列计数素数。证书 `docs/finite-verify-exp5.json` 记录 `odd_prime_count=33`、`ok=true`、`failures=[]`，且 `worst_min_row_prime_count=1`、`worst_min_col_prime_count=1`。因此每个被验证奇素数的每行与除第 `P` 列外每列均含素数。证毕。

## 定理 2（机械阈值抽取）

假设 `docs/explicit-p0-constants.structured-conservative.json` 中的每个常数均由相应数学输入证明，则理论段覆盖所有 `P>exp(3.5)`。

**证明。** 抽取器 `experiments/extract_p0.py` 检查以下有限不等式：

1. 所有正性与结构开关相容；
2. `tail_error_power=4>A_star=2`；
3. OMR/CGTP/LSMP 对数损失 `32<K_sieve_log_saving=128`；
4. C 区直接证书在 `logP<=5` 时可用；
5. 主体常数账本满足严格余量。

运行

`python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conservative.json --max-log 100 --step 0.1`

产生证书 `docs/explicit-p0-structured-conservative-result.json`，其中 `log_P0_upper=3.5`。故在所有数学输入已证时，理论段覆盖 `P>exp(3.5)`。证毕。

## 定理 3（两段覆盖闭合）

若理论段的所有数学输入无条件成立，则 `Prime-Square-Closure(P)` 对全部奇素数成立。

**证明。** 若 `P<=exp(5)`，由定理 1。若 `P>exp(3.5)`，由定理 2。由于 `exp(3.5)<exp(5)`，任意奇素数落在两段并集中。证毕。

## 待证数学输入 A/B（行列归约）

`Column-Closure` 与 `Row-Closure` 的反例归约已在 `docs/row-column-reduction-theoremization.md` 中短定理化：

- Theorem A：列反例归约为 Structured-EHPD 坏配置；
- Theorem B：行反例归约为 Structured-EHPD 坏配置。

当前剩余主要是符号和分层核对：小因子锁定、双粗主体、尾部锚三层是否完全覆盖且不误计；Tail-log4 是否同时适配行列尾部；45 度斜线锁定是否只作为小因子锁定层处理。

## 待证数学输入 C（Tail-log4 定理）

行/列归约中的尾部覆盖贡献满足

`T_tail <= C_tail V_D P/log^4 P`。

本输入已在 `docs/tail-log4-theoremization.md` 中拆成三条独立定理：

1. `TL4-L`：低谱倒数窗口大筛。剩余外部输入是 BG/coherent reciprocal Kloosterman 的任意固定对数节省版本。
2. `TL4-S`：平滑与端点余项。该项已由 Vaaler 截断和 Selberg 权能量给出直接证明。
3. `TL4-M`：中谱平均二元上筛。其大模数层已在 `docs/tail-log4-theoremization.md` 第 6 节拆成二维 Selberg 上筛模板、平均奇异级数账本和平均大模数命题。

因此 Tail-log4 已不再作为单一黑箱；TL4-L 已在 `docs/tail-log4-theoremization.md` 第 7 节拆成 RKS-log 引用模式、Vaughan Type I/II 核验和低体积吸收。剩余核心主要是把 RKS-log 与具体 Bourgain--Garaev/多线性倒数 Kloosterman 定理逐项匹配。

## 待证数学输入 D（OMR/CGTP/LSMP 结构定理）

若坏配置在 Tail-log4 削尾后仍存在，则 OMR 生成树、CGTP 投影增量和 LSMP 小质量 packing 给出 `Λ^2` 级矛盾，并可使用保守常数

`16,16,16,16,16; 8,8,8,8; epsilon_OMR_power=64`。

本输入已在 `docs/omr-cgtp-lsmp-theoremization.md` 拆成 OMR-1/2/3、CGTP、LSMP-1/2、FCT 等独立接口。已组合化的部分包括层蛋糕匹配、一维圆周模型、离散 coarea 和 martingale 能量账本。剩余深层输入缩小为：

- NRC：已在 `docs/nrc-theoremization.md` 定理化为完成法 + Weil/Kloosterman 界；
- FCT/Tree-WFE：已在 `docs/fct-tree-wfe-theoremization.md` 定理化为短深度 span 计数、频率闭包终端与树状容量账本。

## 审稿结论

当前仓库已经具备定理 1--3 的机械闭合与证书闭合；但要达到顶级数学期刊“完整无条件证明”，必须把待证输入 A--D 逐项升级为完整证明或明确引用的外部定理。任何最终摘要都应使用“在 A--D 已证前提下闭合”的严谨表述，直到这些输入被逐行证明。
