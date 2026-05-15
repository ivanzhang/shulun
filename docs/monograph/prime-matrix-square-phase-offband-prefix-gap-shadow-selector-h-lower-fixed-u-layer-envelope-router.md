# Prime Matrix square-phase off-band prefix gap shadow selector H lower fixed-u layer envelope router

**状态：** `loaded_b_breakpoint_reduced_to_fixed_u_short_goldbach_layer_envelope_open`

本步没有转换命题，而是把上一层 loaded-b 断点继续下钻到固定 `u` 层。固定 `u` 后，候选槽满足 `q=P-2b`、`m=P+2(b+u)`，所以 `q+m=2(P+u)`；同时半列窗口给出关于 `b` 的单调二次区间。因此，若断点被达到，破坏输入必须表现为某些短 Goldbach 层在受限 `b` 区间内过密，或 loaded-u 层数本身过密。当前 `P>=2001` 重放中断点达到数为 0，fixed-u 单层最大实载为 4，最小断点缺口为 1 层；这些仍是有限证据，严格自足闭合还需要全局 fixed-u 包络或短 Goldbach 层 PDEC 排斥。

```text
max_p=10000
p0=2001
target_h_coeff=0.43
fixed_u_grouping_failure_count=0
short_goldbach_sum_failure_count=0
fixed_u_interval_empty_failure_count=0
breakpoint_reached_count_at_p0=0
min_breakpoint_shortage_to_failure_at_p0=1
max_loaded_u_layers_at_p0=32
max_u_layer_load_at_p0=4
row_column_unconditional_closed=false
```

## 1. 固定 u 层公式

令 `H2=(P-1)/2`。固定 `u` 后，半列窗口 `1<=s<=H2` 等价于：

```text
plus:  uP-H2 <= 2b(b+u) <= uP-1
minus: uP+1 <= 2b(b+u) <= uP+H2
```

候选素对同时满足：

```text
q=P-2b, m=P+2(b+u), q+m=2(P+u)
```

所以 fixed-u 层不是抽象容量项，而是受二次 b 区间截断的短 Goldbach 表示层。

## 2. 断点的鸽巢路由

设 `Bcrit=LowSurvivors-ceil(0.43P/logP)+1`。若 loaded-b 层达到 `Bcrit`，则对任意候选上界 `K`：

```text
max_u_layer_load > K  OR  loaded_u_layers >= ceil(Bcrit/K).
```

因此下一步可以只攻两个原子：固定 u 层单层过载，或 loaded-u 层数过密。

## 3. P 区间账本

| P range | hits | min shortage | max loaded-u | max u-load | max u-window b-len | max density | p at min shortage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3..2000 | 150 | -1 | 10 | 3 | 21 | 1.0 | `[157, 173]` |
| 2001..5000 | 194 | 1 | 19 | 4 | 35 | 1.0 | `[2467]` |
| 5001..10000 | 268 | 13 | 32 | 4 | 49 | 1.0 | `[5297]` |

## 4. 最紧样本

| shortage | template | p | side | rho | H | R(P) | Low | Good | Bcrit | loaded b | loaded u | max u-load | max window | threshold | needed u |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 | 2467 | minus | 7 | 136 | 136 | 142 | 6 | 7 | 6 | 6 | 1 | 8 | 2 | 7 |
| 13 | 4 | 2243 | plus | 2 | 138 | 126 | 147 | 9 | 22 | 9 | 8 | 2 | 9 | 3 | 11 |
| 13 | 2 | 2347 | plus | 7 | 143 | 131 | 148 | 5 | 18 | 5 | 5 | 1 | 10 | 4 | 18 |
| 13 | 3 | 2347 | plus | 7 | 143 | 131 | 148 | 5 | 18 | 5 | 5 | 1 | 10 | 4 | 18 |
| 13 | 4 | 3767 | plus | 2 | 209 | 197 | 225 | 16 | 29 | 16 | 15 | 2 | 6 | 2 | 15 |
| 13 | 0 | 5297 | minus | 2 | 278 | 266 | 299 | 21 | 34 | 21 | 20 | 2 | 36 | 2 | 17 |
| 13 | 5 | 5297 | minus | 2 | 278 | 266 | 299 | 21 | 34 | 21 | 20 | 2 | 36 | 2 | 17 |
| 14 | 5 | 2027 | minus | 2 | 128 | 115 | 133 | 5 | 19 | 5 | 5 | 1 | 4 | 4 | 19 |
| 14 | 4 | 2063 | plus | 2 | 130 | 117 | 138 | 8 | 22 | 8 | 8 | 1 | 9 | 3 | 22 |
| 14 | 0 | 2927 | minus | 2 | 171 | 158 | 182 | 11 | 25 | 11 | 10 | 2 | 27 | 3 | 13 |
| 14 | 5 | 2927 | minus | 2 | 171 | 158 | 182 | 11 | 25 | 11 | 10 | 2 | 27 | 3 | 13 |
| 15 | 5 | 2267 | minus | 2 | 141 | 127 | 146 | 5 | 20 | 5 | 5 | 1 | 23 | 5 | 20 |

## 5. 单层最大实载样本

| p | side | rho | loaded b | loaded u | max u-load | top loaded u layers |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 7727 | `minus` | 2 | 27 | 24 | 4 | `u=1:load=4,window=14; u=12:load=1,window=4; u=15:load=1,window=4; u=16:load=1,window=4; u=25:load=1,window=3` |
| 9377 | `minus` | 2 | 27 | 24 | 4 | `u=0:load=4,window=48; u=3:load=1,window=9; u=5:load=1,window=8; u=9:load=1,window=6; u=13:load=1,window=5` |
| 9377 | `minus` | 2 | 27 | 24 | 4 | `u=0:load=4,window=48; u=3:load=1,window=9; u=5:load=1,window=8; u=9:load=1,window=6; u=13:load=1,window=5` |
| 4457 | `minus` | 2 | 19 | 16 | 4 | `u=0:load=4,window=33; u=1:load=1,window=11; u=4:load=1,window=6; u=11:load=1,window=3; u=12:load=1,window=4` |
| 4457 | `minus` | 2 | 19 | 16 | 4 | `u=0:load=4,window=33; u=1:load=1,window=11; u=4:load=1,window=6; u=11:load=1,window=3; u=12:load=1,window=4` |
| 8677 | `minus` | 7 | 35 | 32 | 3 | `u=0:load=3,window=46; u=128:load=2,window=2; u=1:load=1,window=15; u=6:load=1,window=6; u=8:load=1,window=6` |
| 9467 | `plus` | 2 | 29 | 27 | 3 | `u=4:load=3,window=9; u=1:load=1,window=20; u=2:load=1,window=13; u=8:load=1,window=6; u=19:load=1,window=4` |
| 8819 | `plus` | 2 | 29 | 26 | 3 | `u=1:load=3,window=19; u=22:load=2,window=3; u=2:load=1,window=12; u=5:load=1,window=8; u=6:load=1,window=7` |

## 6. 结构判断

- 当前最紧断点仍是 `P=2467, minus, rho=7`：`Bcrit=7`、loaded b 为 `6`、还差一层。
- 有限重放中 fixed-u 单层最大实载为 `4`；这指向短 Goldbach 层过密，而不是固定 b 层容量问题。
- 由于 fixed-u 层自带 `q+m=2(P+u)`，后续若出现断点反例，可以登记为同一偶数层内多素对聚集的相位证书。
- 当前仍未证明全局行/列无条件闭合。

## 7. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_u_quadratic_window_representation` | `closed` | For fixed u, the half-column condition is a monotone quadratic interval in b: plus has uP-H2 <= 2b(b+u) <= uP-1, minus has uP+1 <= 2b(b+u) <= uP+H2. |
| `fixed_u_short_goldbach_layer_identity` | `closed` | Every fixed-u candidate has q=P-2b, m=P+2(b+u), hence q+m=2(P+u); layer load is a truncated Goldbach representation count. |
| `breakpoint_pigeonhole_route` | `closed` | If loaded-b reaches Bcrit, then for any proposed fixed-u load cap K either some fixed-u layer has load>K or the number of loaded u layers is at least ceil(Bcrit/K). |
| `global_fixed_u_envelope_or_short_goldbach_pdec` | `open` | A global proof must bound these truncated short-Goldbach layer loads and loaded-u layer counts below Bcrit, or register persistent over-density as PDEC/SAE. |

## 8. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedUQuadraticWindowRepresentationClosed` | `true` | `true` | 固定 u 层可由单调二次 b 区间精确表示。 | closed |
| `FixedUShortGoldbachIdentityClosed` | `true` | `true` | 固定 u 层实载等于受 b 区间截断的 q+m=2(P+u) 素对计数。 | closed |
| `CurrentFixedULoadBelowBreakpoint` | `true` | `false` | 有限重放中 fixed-u 分层未触发断点；这只是证据，不是全局证明。 | finite evidence only |
| `GlobalFixedULayerEnvelopeProved` | `false` | `false` | 仍需全局控制 fixed-u 层负载与 loaded-u 层数，或排斥短 Goldbach 层过密 PDEC。 | SelectorGoodShellFixedULayerEnvelopeOrShortGoldbachLayerPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把断点层容量再压成 fixed-u 短 Goldbach 层包络。 | SelectorGoodShellFixedULayerEnvelopeOrShortGoldbachLayerPDEC |

## 9. 下一步

- 主攻：`SelectorGoodShellFixedULayerEnvelopeOrShortGoldbachLayerPDEC`。
- 具体目标：证明 fixed-u 短 Goldbach 层负载与 loaded-u 层数不能共同达到 `Bcrit`，或把达到断点的同偶数层素对过密登记并排斥为 PDEC/SAE。

## 10. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_u_layer_envelope_router.py` | `3873b35f45a49cb567ec763d8a640f988529a5fa94890281dc3097d61bbba4db` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py` | `2b436d80485f8facf51dffb6411bff8c73d56ab36ed99bc0229b1a45911df80e` |
| `experiments/prime_matrix_square_phase_even_layer_interval_router.py` | `9e243ffa1743280677931b841a5227047791d4eaecbcfe3c64e6457394475e90` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-ledger.json` | `f1258ae0679f9520292acf751412fa30399cfe854d993e64aee38d16df155cdb` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-ledger.json` | `ec479a8c592f01c52ac1b53fc2bafb22d7e94b6b35c9808d4440d0d4e488e338` |
