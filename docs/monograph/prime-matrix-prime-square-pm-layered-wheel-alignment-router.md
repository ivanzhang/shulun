# Prime Matrix P^2±r 两行平方锚层叠轮筛路由器

**状态：** `p_square_pm_layered_wheel_alignment_closed_survivor_lower_bound_open`

你的 P^2 锚提示可以严格化：`P^2+r` 与 `P^2-r` 分别是相邻两行 `x=P` 与 `x=P-1` 的同一平方锚前后侧；对每个 `q<P`，合数标记只取 `r≡-P^2 mod q` 与 `r≡P^2 mod q` 两个镜像禁类。因为 `P` 是所有这些小模的单位，`P^2` 落在层叠轮筛的平方类中，所以每一层 `30,210,2310,...` 都确实给出刚性相位信息。但有限轮层只说明已加入小素数能判定哪些 r 已合成；最终 `q<P` 层仍需证明存在未覆盖 r，这正是平方根长度短区间素数硬点。新的最窄自足目标是：若最终层全覆盖，则终端杀光必须显化为 SquarePhase-PDEC/SAE/ColumnCRT；否则给出 two-sided square-phase 幸存下界。

```text
max_p=5000
finite_prime_count=668
plus_failure_count=0
minus_failure_count=0
all_final_equivalences_hold=true
plus_global_survivor_lower_bound_proved=false
terminal_full_cover_pdec_return_proved=false
row_column_unconditional_closed=false
```

## 1. 确定性结构

| name | status | statement |
| --- | --- | --- |
| `two_row_square_anchor_identity` | `closed` | P^2+r 是第 x=P 行第 r 列；P^2-r 是第 x=P-1 行第 P-r 列。 |
| `plus_minus_canonical_residue` | `closed` | q<P 覆盖 P^2+r iff r≡-P^2 mod q；覆盖 P^2-r iff r≡P^2 mod q。 |
| `quadratic_mirror_lock` | `closed` | P 是每个 q<P 的单位，所以 P^2 是平方类；奇 q 下正负禁类互为相反数且不重合。 |
| `inverse_alignment_specialization` | `closed` | plus 侧是逆元对齐系统的 x=P 特化；minus 侧是 x=P-1 反向列特化。 |
| `finite_layered_wheel_exactness` | `closed` | 任意有限轮层只给出已加入小素数的精确合数标记；最终 q<P 层未覆盖点等价于对应平方锚素数。 |
| `global_survivor_lower_bound` | `open` | 证明最终 q<P 层 plus 或 minus 存在幸存列，仍等价于平方根长度短区间素数输入或 PDEC 排斥。 |

## 2. 样本最终层

| P | plus survivors | least plus | minus survivors | least minus | both-side survivors |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 3 | 173 | 3 | 167 | 1 |
| 17 | 1 | 293 | 3 | 283 | 0 |
| 19 | 3 | 367 | 4 | 359 | 1 |
| 23 | 2 | 541 | 3 | 523 | 0 |
| 29 | 4 | 853 | 5 | 839 | 2 |
| 31 | 5 | 967 | 4 | 953 | 0 |
| 101 | 11 | 10211 | 12 | 10193 | 1 |
| 499 | 40 | 249017 | 44 | 248987 | 4 |
| 1009 | 72 | 1018091 | 70 | 1018057 | 3 |
| 2003 | 125 | 4012013 | 139 | 4011991 | 11 |
| 4999 | 300 | 24990037 | 289 | 24989971 | 18 |

## 3. 最紧样本

- plus 侧最少幸存：`P=3`，幸存 `1`，最小素数 `11`。
- minus 侧最少幸存：`P=3`，幸存 `1`，最小素数 `7`。
- 两侧同 r 同时幸存最少样本：`P=5`，数量 `0`。该双侧素对不是当前必需目标。

## 4. 样本层叠轮筛

| P | cutoff | plus survivors | minus survivors | both-side survivors | mirror law |
| ---: | --- | ---: | ---: | ---: | --- |
| 13 | `5` | 3 | 4 | 1 | `true` |
| 13 | `7` | 3 | 3 | 1 | `true` |
| 13 | `11` | 3 | 3 | 1 | `true` |
| 13 | `13` | 3 | 3 | 1 | `true` |
| 13 | `17` | 3 | 3 | 1 | `true` |
| 13 | `19` | 3 | 3 | 1 | `true` |
| 13 | `23` | 3 | 3 | 1 | `true` |
| 13 | `29` | 3 | 3 | 1 | `true` |
| 13 | `31` | 3 | 3 | 1 | `true` |
| 13 | `q<P` | 3 | 3 | 1 | `true` |
| 17 | `5` | 3 | 4 | 1 | `true` |
| 17 | `7` | 2 | 3 | 0 | `true` |
| 17 | `11` | 2 | 3 | 0 | `true` |
| 17 | `13` | 1 | 3 | 0 | `true` |
| 17 | `17` | 1 | 3 | 0 | `true` |
| 17 | `19` | 1 | 3 | 0 | `true` |
| 17 | `23` | 1 | 3 | 0 | `true` |
| 17 | `29` | 1 | 3 | 0 | `true` |
| 17 | `31` | 1 | 3 | 0 | `true` |
| 17 | `q<P` | 1 | 3 | 0 | `true` |
| 19 | `5` | 5 | 5 | 2 | `true` |
| 19 | `7` | 4 | 4 | 1 | `true` |
| 19 | `11` | 4 | 4 | 1 | `true` |
| 19 | `13` | 3 | 4 | 1 | `true` |
| 19 | `17` | 3 | 4 | 1 | `true` |
| 19 | `19` | 3 | 4 | 1 | `true` |
| 19 | `23` | 3 | 4 | 1 | `true` |
| 19 | `29` | 3 | 4 | 1 | `true` |
| 19 | `31` | 3 | 4 | 1 | `true` |
| 19 | `q<P` | 3 | 4 | 1 | `true` |
| 23 | `5` | 5 | 6 | 2 | `true` |
| 23 | `7` | 4 | 5 | 1 | `true` |
| 23 | `11` | 4 | 4 | 0 | `true` |
| 23 | `13` | 3 | 4 | 0 | `true` |
| 23 | `17` | 3 | 3 | 0 | `true` |
| 23 | `19` | 2 | 3 | 0 | `true` |
| 23 | `23` | 2 | 3 | 0 | `true` |
| 23 | `29` | 2 | 3 | 0 | `true` |
| 23 | `31` | 2 | 3 | 0 | `true` |
| 23 | `q<P` | 2 | 3 | 0 | `true` |
| 29 | `5` | 7 | 7 | 2 | `true` |
| 29 | `7` | 6 | 6 | 2 | `true` |
| 29 | `11` | 5 | 6 | 2 | `true` |
| 29 | `13` | 5 | 6 | 2 | `true` |
| 29 | `17` | 5 | 6 | 2 | `true` |
| 29 | `19` | 5 | 5 | 2 | `true` |
| 29 | `23` | 4 | 5 | 2 | `true` |
| 29 | `29` | 4 | 5 | 2 | `true` |
| 29 | `31` | 4 | 5 | 2 | `true` |
| 29 | `q<P` | 4 | 5 | 2 | `true` |
| 31 | `5` | 8 | 8 | 3 | `true` |
| 31 | `7` | 7 | 6 | 1 | `true` |
| 31 | `11` | 6 | 6 | 0 | `true` |
| 31 | `13` | 6 | 5 | 0 | `true` |
| 31 | `17` | 6 | 5 | 0 | `true` |
| 31 | `19` | 6 | 5 | 0 | `true` |
| 31 | `23` | 5 | 4 | 0 | `true` |
| 31 | `29` | 5 | 4 | 0 | `true` |
| 31 | `31` | 5 | 4 | 0 | `true` |
| 31 | `q<P` | 5 | 4 | 0 | `true` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TwoRowSquareAnchorCRTClosed` | `true` | `true` | P^2±r 已精确接入相邻两行和逆元对齐模型。 | closed |
| `LayeredWheelFiniteExactnessClosed` | `true` | `true` | 每层轮筛给出的合数标记、最终幸存列与素数事实完全一致。 | closed for finite exactness |
| `FinitePlusMinusNoFullCoverChecked` | `true` | `false` | 有限扫描 P<=5000 中，前后两侧均未出现全覆盖。 | finite evidence only |
| `PlusGlobalSurvivorLowerBoundProved` | `false` | `false` | 证明 plus 最终层一定有幸存列就是 P^2 后长度 P 内有素数。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| `MinusGlobalSurvivorLowerBoundProved` | `false` | `false` | 证明 minus 最终层一定有幸存列就是 P^2 前长度 P 内有素数。 | PrimeInLastHalfBeforePrimeSquareForEveryPrimeP |
| `TerminalFullCoverRoutesToPDEC` | `false` | `false` | 若假设某侧全覆盖，仍需证明层叠轮筛终端杀光必形成 PDEC/SAE/ColumnCRT 回流。 | TerminalSquarePhasePDECSAEOrColumnCRTReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步是结构闭合和硬点压缩，不产生全局无条件矛盾。 | TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound OR TerminalSquarePhasePDECSAEOrColumnCRTReturn |

## 6. 下一步

- 主攻：`TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound`。
- 备选闭合口：`TerminalSquarePhasePDECSAEOrColumnCRTReturn`。
- 不再把任意固定轮 `W` 当作全局规律；证明目标应是层层提升后，全覆盖若持续则必产生终端相位缺陷。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-square-pm-layered-wheel-alignment-ledger.json` | `74c9565b1c4e2cb98413e26ecb2ddcc09a0a7975ab9e005f8721c63cec02c457` |
| `experiments/prime_matrix_prime_square_pm_layered_wheel_alignment_router.py` | `5a52d0c796addd70e170e48ad16ad1ac2bde08935b4442c5d9001ed057a967eb` |
