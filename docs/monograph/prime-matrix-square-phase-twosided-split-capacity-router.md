# Prime Matrix square-phase two-sided split capacity

**状态：** `twosided_square_phase_split_capacity_reduced_to_alpha_four_fifths_lowhole_open`

`P^2±r` 的层叠轮筛可继续压成一个完全确定的容量判据：先筛到 `y=floor(alpha P)`，若某侧低轮幸存数 `H_y` 大于尾素数 `q in (y,P)` 的实际固定相位容量 `C_y`，则该侧必有平方锚素数。有限审计显示 `alpha=4/5` 在 `P<=5000` 范围内 plus/minus 两侧 margin 全为正，比 `2/3` 的样本边界更稳。但全局仍需证明 `H_floor(4P/5)` 的下界，或证明 margin 失败必产生尾相位 PDEC/SAE 回流。

```text
max_p=5000
finite_prime_count=668
alpha_4_5_plus_failure_count=0
alpha_4_5_minus_failure_count=0
alpha_4_5_combined_failure_count=0
alpha_four_fifths_global_lowhole_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `signed_split_capacity_criterion` | `closed` | For each sign, if H_y^sign(P)>C_y^sign(P), then P^2 sign r has a prime with 1<=r<P. |
| `exact_tail_capacity` | `closed` | C_y^sign(P) is the exact number of tail phase slots r in [1,P-1] hit by q in (y,P). |
| `twosided_combined_criterion` | `closed` | If H_y^+(P)+H_y^-(P)>C_y^+(P)+C_y^-(P), at least one side has a square-anchor prime. |
| `alpha_four_fifths_finite_margin` | `diagnostic_only` | The alpha=4/5 margin is positive for both signs in the scanned range, but this is not a global proof. |
| `remaining_lowhole_lower_bound` | `open` | A global proof needs a lower bound for H_floor(4P/5)^sign(P), or a proof that margin failure routes to PDEC/SAE. |

## 2. Alpha 扫描汇总

| alpha | plus fail | minus fail | combined fail | min plus | min minus | min combined |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.500000 | 653 | 653 | 655 | -102 | -109 | -188 |
| 0.600000 | 79 | 65 | 21 | -21 | -23 | -20 |
| 0.666667 | 4 | 2 | 0 | 0 | 0 | 1 |
| 0.700000 | 2 | 1 | 0 | 0 | 0 | 1 |
| 0.750000 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0.800000 | 0 | 0 | 0 | 1 | 1 | 2 |
| 0.850000 | 0 | 0 | 0 | 1 | 1 | 2 |
| 0.900000 | 0 | 0 | 0 | 1 | 1 | 2 |

## 3. Alpha=4/5 样本

| P | plus H | plus C | plus margin | minus H | minus C | minus margin |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 3 | 1 | 2 | 3 | 1 | 2 |
| 17 | 1 | 0 | 1 | 3 | 0 | 3 |
| 19 | 3 | 1 | 2 | 4 | 1 | 3 |
| 23 | 3 | 2 | 1 | 3 | 1 | 2 |
| 29 | 4 | 0 | 4 | 5 | 0 | 5 |
| 31 | 5 | 1 | 4 | 4 | 1 | 3 |
| 101 | 11 | 4 | 7 | 12 | 3 | 9 |
| 499 | 42 | 18 | 24 | 45 | 18 | 27 |
| 1009 | 79 | 32 | 47 | 77 | 34 | 43 |
| 2003 | 132 | 54 | 78 | 144 | 57 | 87 |
| 4999 | 317 | 134 | 183 | 303 | 128 | 175 |

## 4. 最紧样本

- plus 最小 margin：`P=3`，`H=1`，`C=0`，`margin=1`。
- minus 最小 margin：`P=3`，`H=1`，`C=0`，`margin=1`。
- combined 最小 margin：`P=3`，`H=2`，`C=0`，`margin=2`。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SplitCapacityCriterionClosed` | `true` | `true` | 低轮幸存数大于高尾容量时，该侧平方锚素数必存在。 | closed |
| `AlphaFourFifthsFiniteBothSignsPositive` | `true` | `false` | 有限扫描 P<=5000 下 alpha=4/5 两侧 margin 均为正。 | finite evidence only |
| `AlphaFourFifthsGlobalLowHoleLowerBound` | `false` | `false` | 需要把样本正余量升级为全局低洞下界与高尾容量上界。 | SquarePhaseAlphaFourFifthsLowHoleLowerBound |
| `TailCapacityFailureRoutesToPDEC` | `false` | `false` | 若 margin<=0 持久发生，必须登记为尾相位容量异常、端点 SAE 或 SquarePhase-PDEC。 | SquarePhaseTailCapacityPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭分割判据和有限证据，不关闭全局命题。 | SquarePhaseAlphaFourFifthsLowHoleLowerBound OR SquarePhaseTailCapacityPDECSAEReturn |

## 6. 下一步

- 主攻：`SquarePhaseAlphaFourFifthsLowHoleLowerBound`。
- 备选回流：`SquarePhaseTailCapacityPDECSAEReturn`。
- 关键是证明 alpha=4/5 低轮幸存数下界，而不是继续扩大有限扫描。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-twosided-split-capacity-ledger.json` | `1b6d6bba84ef370819ff3a11dcc0d382f9162dd37e0c7bb1ec0166e2b74a3f9d` |
| `experiments/prime_matrix_square_phase_twosided_split_capacity_router.py` | `5949ac34fe3772e6c6abb65d630ebc45a3eafbc5321e247320f7bccc5e20da03` |
