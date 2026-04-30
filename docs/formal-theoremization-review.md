# 行列命题最终定理化审稿稿

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

## 待证数学输入 A（Column-Closure 归约）

对任意奇素数 `P` 与列 `c<P`，若第 `c` 列无素数，则由该列合数解释诱导的锚覆盖族满足 Structured-EHPD 坏配置假设。

**必须证明的要点。**

- 每个合数 `kP+c` 的素因子解释可唯一分配到小因子锁定、粗因子锚、双粗尾部三类之一。
- 同一短窗口中大于 `sqrt(P)` 的素因子不能被两个距离小于 `sqrt(P)` 的粗合数共享。
- CRT 列均衡保证非零同余类交集的列分布不能把所有缺口集中到单列。
- 第 `P` 列排除后，所有相关模数与列坐标互素，避免平凡全合数列。

## 待证数学输入 B（Row-Closure 归约）

对任意奇素数 `P` 与行 `k`，若第 `k` 行无素数，则该行合数解释诱导的锚覆盖族满足同一 Structured-EHPD 坏配置假设。

**必须证明的要点。**

- 相邻数的合数解释必须来自不同素因子；同余商相邻时保持互质。
- `P+1` 与 `P-1` 诱导的正反 45 度斜线锁定只覆盖小因子锁定层，剩余双粗点仍受大因子短窗不可复用约束。
- 尾部 `m` 侧计数把 `q≈P` 的危险覆盖转为 Tail-log4 误差，而不泄漏主体容量。
- 行全覆盖若跨 CRT 周期复现，必须与 CRT 非零同余类均衡一致；该一致性正是 EHPD 坏配置的周期刚性假设。

## 待证数学输入 C（Tail-log4 定理）

行/列归约中的尾部覆盖贡献满足

`T_tail <= C_tail V_D P/log^4 P`。

本输入已在 `docs/tail-log4-theoremization.md` 中拆成三条独立定理：

1. `TL4-L`：低谱倒数窗口大筛。剩余外部输入是 BG/coherent reciprocal Kloosterman 的任意固定对数节省版本。
2. `TL4-S`：平滑与端点余项。该项已由 Vaaler 截断和 Selberg 权能量给出直接证明。
3. `TL4-M`：中谱平均二元上筛。剩余外部输入是二维 Selberg 上筛与平均大模数二元上筛。

因此 Tail-log4 已不再作为单一黑箱；它只剩两个标准解析输入需要引用或附录证明。

## 待证数学输入 D（OMR/CGTP/LSMP 结构定理）

若坏配置在 Tail-log4 削尾后仍存在，则 OMR 生成树、CGTP 投影增量和 LSMP 小质量 packing 给出 `Λ^2` 级矛盾，并可使用保守常数

`16,16,16,16,16; 8,8,8,8; epsilon_OMR_power=64`。

**必须证明的要点。**

- OMR 层逼近和投影抽取只产生 `C_OMR_layer=16`、`C_OMR_projection=16` 的常数损失。
- CGTP 的 martingale 能量增量与 variance-to-density 转换不损失超过 `C_CGTP=16`、`A_CGTP_log=8`。
- LSMP 的方向筛选、离散 coarea 与 DPI 只产生对数损失，不退化回 `Λ^{-2}` 损失。
- frequency-collision terminal 可接入 Tree-WFE，并由 `C_collision_span=16`、`A_collision_span_log=8` 控制。

## 审稿结论

当前仓库已经具备定理 1--3 的机械闭合与证书闭合；但要达到顶级数学期刊“完整无条件证明”，必须把待证输入 A--D 逐项升级为完整证明或明确引用的外部定理。任何最终摘要都应使用“在 A--D 已证前提下闭合”的严谨表述，直到这些输入被逐行证明。
