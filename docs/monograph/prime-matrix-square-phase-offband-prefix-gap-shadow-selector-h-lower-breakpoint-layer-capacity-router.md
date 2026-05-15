# Prime Matrix square-phase off-band prefix gap shadow selector H lower breakpoint layer capacity router

**状态：** `h_lower_breakpoint_reduced_to_loaded_b_layer_upper_bound_open`

本步把 H 下界失败写成整数断点：失败当且仅当 GoodShell 的 loaded b 层数达到 `LowSurvivors-ceil(0.43P/logP)+1`。由于 `alpha=4/5` 时固定 b 层的 u 区间长度 <1，每层至多一个 GoodShell 槽，所以 GoodShell 计数就是 distinct loaded-b 层数。当前 `P>=2001` 重放没有达到断点，最小缺口为 1 层；全局剩余是证明 loaded-b 素对层数永远低于该断点，或把达到断点的持久层素对过密抽成 PDEC/SAE。

```text
max_p=10000
p0=2001
target_h_coeff=0.43
prime_rho_hit_count=612
unit_b_layer_capacity_failure_count=0
breakpoint_reached_count_at_p0=0
min_breakpoint_shortage_to_failure_at_p0=1
shortage_le_1_count_at_p0=1
max_b_layer_load_at_p0=1
row_column_unconditional_closed=false
```

## 1. 整数断点

令

```text
R(P)=ceil(0.43P/logP)
Bcrit(P,side)=LowSurvivors(P,side)-R(P)+1.
```

因为 `H=LowSurvivors-GoodShell` 且 `H` 为整数，所以

```text
H>=0.43P/logP fails  <=>  GoodShell >= Bcrit.
```

再由固定 b 层单位容量，`GoodShell` 等于 loaded b 层数。

## 2. 单位容量证书

- For alpha=4/5, q=P-2b>4P/5 and the half-grid interval has length at most (P-1)/(2q)<5/8.
- 在 `P=2001` 处的通用上界样本：`0.624687656171914`。

## 3. P 区间账本

| P range | hits | min shortage | <=1 | <=2 | <=5 | <=10 | max loaded coeff | max breakpoint coeff | max b-load | max u-load | p at min shortage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3..2000 | 150 | -1 | 17 | 26 | 58 | 90 | 0.09661616188563646 | 0.23898458226790323 | 1 | 3 | `[157, 173]` |
| 2001..5000 | 194 | 1 | 1 | 1 | 1 | 1 | 0.040957353035279497 | 0.15305503352891223 | 1 | 4 | `[2467]` |
| 5001..10000 | 268 | 13 | 0 | 0 | 0 | 0 | 0.039932105870291154 | 0.13578544966001457 | 1 | 4 | `[5297]` |

## 4. 最紧样本

| shortage | template | p | side | rho | W | H | R(P) | Low | Good | Bcrit | loaded b | max b-load | max u-load | loaded coeff | breakpoint coeff |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 | 2467 | minus | 7 | 2 | 136 | 136 | 142 | 6 | 7 | 6 | 1 | 1 | 0.01899657425990115 | 0.022162669969884675 |
| 13 | 4 | 2243 | plus | 2 | 1 | 138 | 126 | 147 | 9 | 22 | 9 | 1 | 2 | 0.030958593763121656 | 0.07567656253207516 |
| 13 | 2 | 2347 | plus | 7 | 1 | 143 | 131 | 148 | 5 | 18 | 5 | 1 | 1 | 0.01653364549606098 | 0.05952112378581953 |
| 13 | 3 | 2347 | plus | 7 | 1 | 143 | 131 | 148 | 5 | 18 | 5 | 1 | 1 | 0.01653364549606098 | 0.05952112378581953 |
| 13 | 4 | 3767 | plus | 2 | 1 | 209 | 197 | 225 | 16 | 29 | 16 | 1 | 2 | 0.03497333350758499 | 0.06338916698249779 |
| 13 | 0 | 5297 | minus | 2 | 2 | 278 | 266 | 299 | 21 | 34 | 21 | 1 | 2 | 0.033995245220395515 | 0.05503992083302131 |
| 13 | 5 | 5297 | minus | 2 | 2 | 278 | 266 | 299 | 21 | 34 | 21 | 1 | 2 | 0.033995245220395515 | 0.05503992083302131 |
| 14 | 5 | 2027 | minus | 2 | 2 | 128 | 115 | 133 | 5 | 19 | 5 | 1 | 1 | 0.018782220390853477 | 0.07137243748524322 |
| 14 | 4 | 2063 | plus | 2 | 1 | 130 | 117 | 138 | 8 | 22 | 8 | 1 | 1 | 0.029595410617823566 | 0.0813873791990148 |
| 14 | 0 | 2927 | minus | 2 | 2 | 171 | 158 | 182 | 11 | 25 | 11 | 1 | 2 | 0.02999626448705526 | 0.06817332837967104 |
| 14 | 5 | 2927 | minus | 2 | 2 | 171 | 158 | 182 | 11 | 25 | 11 | 1 | 2 | 0.02999626448705526 | 0.06817332837967104 |
| 15 | 5 | 2267 | minus | 2 | 2 | 141 | 127 | 146 | 5 | 20 | 5 | 1 | 1 | 0.017040610168741793 | 0.06816244067496717 |

## 5. 结构判断

- 破坏输入已从 `GoodShell` 总量改写为 distinct `b` 层素对数量。
- 固定 `b` 层不能提供多重容量；若达到断点，只能是许多不同 `b` 层同时产生素对。
- 最紧样本 `P=2467, minus, rho=7` 只差一个 loaded b 层会触发 H 门失败，这是下一步应直接排斥的原子形态。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_b_unit_capacity` | `closed` | For alpha=4/5, each fixed b layer contains at most one admissible u, hence at most one GoodShell slot. |
| `h_lower_failure_breakpoint_equivalence` | `closed` | H>=0.43P/logP fails iff loaded GoodShell b-layers reach LowSurvivors-ceil(0.43P/logP)+1. |
| `current_breakpoint_not_reached` | `closed_on_current_sweep` | The current selector sweep never reaches the loaded-b breakpoint; the closest row misses it by one layer. |
| `global_loaded_b_layer_upper_bound` | `open` | A global proof must bound the number of loaded b layers below the breakpoint, or route persistent excess to LayerPrimePairPDEC/SAE. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedBUnitCapacityClosed` | `true` | `true` | 固定 b 层由长度 <1 的 u 区间控制，至多贡献一个 GoodShell 槽。 | closed |
| `BreakpointEquivalenceClosed` | `true` | `true` | H 下界失败等价于 loaded b 层数达到整数断点。 | closed |
| `CurrentBreakpointNotReached` | `true` | `false` | 有限重放中断点未被达到；最紧处只差一层。 | finite evidence only |
| `GlobalLoadedBLayerUpperBoundProved` | `false` | `false` | 仍需全局证明 loaded b 层数低于断点。 | SelectorGoodShellLoadedBLayerBreakpointUpperBoundOrLayerPrimePairPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把破坏输入压成 distinct-b 素对层数量上界。 | SelectorGoodShellLoadedBLayerBreakpointUpperBoundOrLayerPrimePairPDEC |

## 8. 下一步

- 主攻：`SelectorGoodShellLoadedBLayerBreakpointUpperBoundOrLayerPrimePairPDEC`。
- 具体目标：证明 distinct loaded-b prime-pair layers 低于 `Bcrit`，或把达到断点的层素对过密写成固定 b/u 相位 PDEC/SAE。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py` | `2b436d80485f8facf51dffb6411bff8c73d56ab36ed99bc0229b1a45911df80e` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_effective_capacity_correlation_router.py` | `66fb6ad9be48f082d4337eff0e5c384ee0df65ef0704efdf167e41290e55f5c1` |
| `experiments/prime_matrix_square_phase_even_layer_interval_router.py` | `9e243ffa1743280677931b841a5227047791d4eaecbcfe3c64e6457394475e90` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-ledger.json` | `c17df6178bf657ee63128b7366721bc61b9fa7c19731df3385e92c5593aca892` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-ledger.json` | `f1258ae0679f9520292acf751412fa30399cfe854d993e64aee38d16df155cdb` |
