# Prime Matrix square-phase off-band prefix gap shadow selector H lower effective-capacity correlation router

**状态：** `h_lower_reduced_to_low_survivor_goodshell_correlated_surplus_open`

本步把平方窗下界 `H>=0.43P/logP` 改写成有效容量恒等式 `H=LowSurvivors-GoodShell` 后的相关余量门。当前 selector 重放中恒等式失败数为 0，`P>=2001` 的最小 H 系数为 0.4305890165577595。但独立系数门失败：`min LowSurvivor coeff - max GoodShell coeff` 只有 0.40862823778238117，低于 0.43；所以真正剩余不是两个独立估计，而是行级相关余量，或其失败时的近满有效半素数铺砖 PDEC。

```text
max_p=10000
p0=2001
target_h_coeff=0.43
prime_rho_hit_count=612
identity_failure_count=0
H_lower_failure_count_at_p0=0
min_H_scaled_coeff_at_p0=0.4305890165577595
min_low_survivor_scaled_coeff_at_p0=0.44958559081766064
max_good_shell_scaled_coeff_at_p0=0.040957353035279497
independent_gate_beats_target_after_p0=false
tail_upper_external_closed=true
row_column_unconditional_closed=false
```

## 1. 精确分解

对 `alpha=floor(4P/5)` 的低轮幸存集合，既有有效容量恒等式给出：

```text
LowSurvivors = Prime + GoodShell
H = Prime
therefore H = LowSurvivors - GoodShell.
```

这里 `GoodShell` 是真正命中低幸存列的有效高尾近方半素数槽。因而 `H>=0.43P/logP` 等价于：

```text
LowSurvivors - GoodShell >= 0.43 P/logP.
```

## 2. P 区间账本

| P range | hits | min H coeff | min Low coeff | max Good coeff | minLow-maxGood | independent beats 0.43 | min margin coeff | min integer slack | p at min H | p at max Good |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 3..2000 | 150 | 0.38646464754254584 | 0.43094723437910587 | 0.09661616188563646 | 0.3343310724934694 | `false` | -0.04353535245745416 | -1.43543386511001 | `[157]` | `[157]` |
| 2001..5000 | 194 | 0.4305890165577595 | 0.44958559081766064 | 0.040957353035279497 | 0.40862823778238117 | `false` | 0.000589016557759503 | 0.1860387719493417 | `[2467]` | `[4057]` |
| 5001..10000 | 268 | 0.45003229386999777 | 0.4840275390903933 | 0.039932105870291154 | 0.44409543322010214 | `true` | 0.020032293869997775 | 12.374617936792106 | `[5297]` | `[5867]` |

## 3. 最紧样本

| margin coeff | integer slack | template | p | side | rho | W | H | Low | Good | T | H coeff | Low coeff | Good coeff |
| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.000589016557759503 | 0.1860387719493417 | 6 | 2467 | minus | 7 | 2 | 136 | 142 | 6 | 66 | 0.4305890165577595 | 0.44958559081766064 | 0.01899657425990115 |
| 0.020032293869997775 | 12.374617936792106 | 0 | 5297 | minus | 2 | 2 | 278 | 299 | 21 | 121 | 0.45003229386999777 | 0.4840275390903933 | 0.033995245220395515 |
| 0.020032293869997775 | 12.374617936792106 | 5 | 5297 | minus | 2 | 2 | 278 | 299 | 21 | 121 | 0.45003229386999777 | 0.4840275390903933 | 0.033995245220395515 |
| 0.024651120984511388 | 15.50688049839971 | 6 | 5407 | minus | 7 | 2 | 286 | 307 | 21 | 122 | 0.4546511209845114 | 0.48803459490295453 | 0.033383473918443145 |
| 0.026839168942828895 | 12.278689504737343 | 4 | 3767 | plus | 2 | 1 | 209 | 225 | 16 | 91 | 0.4568391689428289 | 0.4918125024504139 | 0.03497333350758499 |
| 0.029124108094015833 | 26.26170252957735 | 0 | 8117 | minus | 2 | 2 | 414 | 438 | 24 | 178 | 0.4591241080940158 | 0.4857399984183066 | 0.02661589032429077 |
| 0.029124108094015833 | 26.26170252957735 | 5 | 8117 | minus | 2 | 2 | 414 | 438 | 24 | 178 | 0.4591241080940158 | 0.4857399984183066 | 0.02661589032429077 |
| 0.03127719581700239 | 16.95141018276712 | 6 | 4567 | minus | 7 | 2 | 250 | 270 | 20 | 108 | 0.4612771958170024 | 0.4981793714823626 | 0.03690217566536019 |
| 0.03168279976837046 | 15.303286914503417 | 5 | 4007 | minus | 2 | 2 | 223 | 238 | 15 | 99 | 0.46168279976837046 | 0.49273769661377653 | 0.031054896845406084 |
| 0.03259467552714762 | 27.550075271817093 | 0 | 7547 | minus | 2 | 2 | 391 | 410 | 19 | 169 | 0.4625946755271476 | 0.48507370068064076 | 0.022479025153493107 |
| 0.03259467552714762 | 27.550075271817093 | 5 | 7547 | minus | 2 | 2 | 391 | 410 | 19 | 169 | 0.4625946755271476 | 0.48507370068064076 | 0.022479025153493107 |
| 0.034429158491650735 | 30.023543815389473 | 0 | 7817 | minus | 2 | 2 | 405 | 429 | 24 | 175 | 0.46442915849165073 | 0.49195088640226703 | 0.02752172791061634 |

## 4. 结构判断

- 独立估计 `LowSurvivors` 与 `GoodShell` 不够尖：当前最小低幸存系数减最大 GoodShell 系数低于 `0.43`。
- 因此必须证明行级相关余量：GoodShell 槽不能集中贴满低幸存集合的临界部分。
- 若该余量失败，反例会形成 near-full effective tiling：有效半素数槽覆盖低幸存集合到只剩少于 `0.43P/logP` 个平方锚素数。
- 当前仍未完成全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `selector_square_window_effective_capacity_identity` | `closed_on_replay_and_symbolic_source` | On each selector row, H equals LowSurvivors minus GoodShell effective slots. |
| `independent_low_good_coefficient_split` | `rejected_as_current_narrow_route` | The observed min LowSurvivor coefficient and max GoodShell coefficient do not independently imply H>=0.43P/logP. |
| `correlated_low_good_surplus` | `open` | The exact remaining H gate is LowSurvivors-GoodShell>=0.43P/logP on selector rho hits. |
| `near_full_effective_tiling_pdec` | `open_return` | If the correlated surplus fails, GoodShell must tile all but 0.43P/logP of the low survivors, giving a near-full effective tiling defect. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `EffectiveCapacityIdentityClosed` | `true` | `true` | `H=LowSurvivors-GoodShell` 在 selector 命中行上已对齐。 | closed |
| `CurrentFiniteHLowerGateHolds` | `true` | `false` | 有限重放支持 H 下系数，但不能当作全局证明。 | finite evidence only |
| `IndependentCoefficientSplitSufficient` | `false` | `false` | 独立下界/上界门太粗；必须证明行级相关余量。 | SelectorLowSurvivorGoodShellCorrelatedSurplusOrNearFullEffectiveTilingPDEC |
| `CorrelatedLowGoodSurplusProved` | `false` | `false` | 仍需全局证明 `LowSurvivors-GoodShell>=0.43P/logP`。 | SelectorLowSurvivorGoodShellCorrelatedSurplusOrNearFullEffectiveTilingPDEC |
| `TailUpperStrictSelfContainedClosed` | `false` | `false` | 旁路自足缺口仍是 pi 双侧区间界内化；外部路线可先继续攻 H。 | SelfContainedDusartPiTwoSidedIntervalLedger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 H 下界门压成更具体的相关余量/近满铺砖缺陷。 | SelectorLowSurvivorGoodShellCorrelatedSurplusOrNearFullEffectiveTilingPDEC |

## 7. 下一步

- 主攻：`SelectorLowSurvivorGoodShellCorrelatedSurplusOrNearFullEffectiveTilingPDEC`。
- 具体下钻方向：把 near-full effective tiling 写成低幸存列与 GoodShell 槽的二部匹配/容量缺陷，寻找固定相位 PDEC 或 SAE 回流。
- 外部路线中尾项门已可关闭；严格自足路线仍需补 `SelfContainedDusartPiTwoSidedIntervalLedger`。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_effective_capacity_correlation_router.py` | `66fb6ad9be48f082d4337eff0e5c384ee0df65ef0704efdf167e41290e55f5c1` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py` | `5f53bd13fef7ac641fb9bf25f0d67d25e79d4e2d8977b667785fd6c93ded5529` |
| `experiments/prime_matrix_square_phase_primevoid_effective_tiling_router.py` | `571adc584832e2902c55bd88a85ca9927be237066bed9b156b2c37a575b6ba66` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_tail_upper_pi_input_router.py` | `f3edbf2be92f4f18bac9908c635ef0866b92c1be3a65d932f788f138fdfc7f1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-ledger.json` | `d2736d775a1d60c5e18fa8fd4598921c9030bfb03d9bc464cafcf0c7a3a6c460` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-ledger.json` | `c17df6178bf657ee63128b7366721bc61b9fa7c19731df3385e92c5593aca892` |
