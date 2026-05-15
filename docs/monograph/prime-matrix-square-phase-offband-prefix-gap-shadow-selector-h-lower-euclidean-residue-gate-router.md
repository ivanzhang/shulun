# Prime Matrix square-phase off-band prefix gap shadow selector H lower Euclidean residue gate router

**状态：** `fixed_u_short_goldbach_layer_reduced_to_euclidean_residue_cap_gate_open`

本步把 fixed-u 短 Goldbach 层再压成 fixed-b 欧几里得余数门。令 `q=P-2b` 且 `2b^2=u0*q+v`，则 minus 候选恰为 `1<=v<=H2`、`u=u0`，plus 候选恰为 `1<=q-v<=H2`、`u=u0+1`。因此 GoodShell 的破坏输入已变成高素数 `q`、余数 cap、伴随素数 `m` 三者的同步事件。当前 `P>=2001` 重放中候选恒等失败数为 0，断点达到数为 0，最小断点缺口为 1；全局仍需证明余数 cap 素对同步不能达到断点，或将其登记并排斥为 PDEC/SAE。

```text
max_p=10000
p0=2001
candidate_identity_failure_count=0
residue_s_formula_failure_count=0
breakpoint_reached_count_at_p0=0
min_breakpoint_shortage_to_failure_at_p0=1
max_residue_gate_candidate_count_at_p0=35
max_both_side_prime_pair_layers_at_p0=3
row_column_unconditional_closed=false
```

## 1. 欧几里得余数门

```text
H2=(P-1)/2
q=P-2b
2b^2 = u0*q + v, 0<=v<q
minus: 1<=v<=H2, u=u0, s=v, m=P+2(b+u0)
plus:  1<=q-v<=H2, u=u0+1, s=q-v, m=P+2(b+u0+1)
```

这个公式把半列窗口、fixed-u 选择、左右侧符号统一成一个余数 cap 判据。

## 2. P 区间账本

| P range | hits | unique P | min shortage | max residue candidates | max both-side cap | max both-side prime-pair | p at min shortage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3..2000 | 150 | 85 | -1 | 10 | 9 | 1 | `[157, 173]` |
| 2001..5000 | 194 | 110 | 1 | 20 | 25 | 3 | `[2467]` |
| 5001..10000 | 268 | 166 | 13 | 35 | 33 | 3 | `[5297]` |

## 3. 最紧样本

| shortage | template | p | side | rho | H | R(P) | Low | Good | Bcrit | loaded b | residue candidates | cap s range | sample slots |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | 6 | 2467 | minus | 7 | 136 | 136 | 142 | 6 | 7 | 6 | 6 | 159..634 | `b=37,u=1,q=2393,m=2543,v=345; b=60,u=3,q=2347,m=2593,v=159; b=78,u=5,q=2311,m=2633,v=613` |
| 13 | 4 | 2243 | plus | 2 | 138 | 126 | 147 | 9 | 22 | 9 | 9 | 2..1037 | `b=32,u=1,q=2179,m=2309,v=2048; b=65,u=4,q=2113,m=2381,v=2111; b=78,u=6,q=2087,m=2411,v=1733` |
| 13 | 2 | 2347 | plus | 7 | 143 | 131 | 148 | 5 | 18 | 5 | 5 | 9..1047 | `b=25,u=1,q=2297,m=2399,v=1250; b=139,u=19,q=2069,m=2663,v=1400; b=142,u=20,q=2063,m=2671,v=1131` |
| 13 | 3 | 2347 | plus | 7 | 143 | 131 | 148 | 5 | 18 | 5 | 5 | 9..1047 | `b=25,u=1,q=2297,m=2399,v=1250; b=139,u=19,q=2069,m=2663,v=1400; b=142,u=20,q=2063,m=2671,v=1131` |
| 13 | 4 | 3767 | plus | 2 | 209 | 197 | 225 | 16 | 29 | 16 | 16 | 44..1784 | `b=72,u=3,q=3623,m=3917,v=3122; b=110,u=7,q=3547,m=4001,v=2918; b=149,u=13,q=3469,m=4091,v=2774` |
| 13 | 0 | 5297 | minus | 2 | 278 | 266 | 299 | 21 | 34 | 21 | 21 | 138..2296 | `b=18,u=0,q=5261,m=5333,v=648; b=54,u=1,q=5189,m=5407,v=643; b=59,u=1,q=5179,m=5417,v=1783` |
| 13 | 5 | 5297 | minus | 2 | 278 | 266 | 299 | 21 | 34 | 21 | 21 | 138..2296 | `b=18,u=0,q=5261,m=5333,v=648; b=54,u=1,q=5189,m=5407,v=643; b=59,u=1,q=5179,m=5417,v=1783` |
| 14 | 5 | 2027 | minus | 2 | 128 | 115 | 133 | 5 | 19 | 5 | 5 | 324..898 | `b=63,u=4,q=1901,m=2161,v=334; b=83,u=7,q=1861,m=2207,v=751; b=98,u=10,q=1831,m=2243,v=898` |
| 14 | 4 | 2063 | plus | 2 | 130 | 117 | 138 | 8 | 22 | 8 | 8 | 32..959 | `b=23,u=1,q=2017,m=2111,v=1058; b=81,u=7,q=1901,m=2239,v=1716; b=95,u=10,q=1873,m=2273,v=1193` |
| 14 | 0 | 2927 | minus | 2 | 171 | 158 | 182 | 11 | 25 | 11 | 11 | 70..1345 | `b=15,u=0,q=2897,m=2957,v=450; b=45,u=1,q=2837,m=3019,v=1213; b=98,u=7,q=2731,m=3137,v=91` |

## 4. 结构判断

- 余数门把候选槽改写为 `2b^2 mod (P-2b)` 落入左右 cap，并要求伴随 `m` 为素数。
- 这与用户提出的 CRT/逆元最小对齐思路同形：零行或反例链若存在，必须在这些余数 cap 中形成同步对齐。
- 当前最紧样本仍只差一层；尚未从余数 cap 同步中推出全局矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_b_euclidean_residue_gate` | `closed` | Writing q=P-2b and 2b^2=u0*q+v, the minus side is exactly 1<=v<=H2 with u=u0, and the plus side is exactly 1<=q-v<=H2 with u=u0+1. |
| `residue_gate_candidate_identity` | `closed` | The Euclidean residue gate generates exactly the same GoodShell candidate slots as the fixed-b interval formula. |
| `crt_ready_residue_cap_form` | `closed` | GoodShell is now a high-prime q layer plus a residue cap condition on 2b^2 mod q and a companion primality condition for m. |
| `global_residue_cap_prime_pair_envelope` | `open` | A global proof must control how often the residue cap and companion prime condition can jointly reach Bcrit, or register that persistence as PDEC/SAE. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `EuclideanResidueGateClosed` | `true` | `true` | fixed-b/fixed-u 候选槽精确等价于欧几里得余数 cap 门。 | closed |
| `CurrentResidueGateBelowBreakpoint` | `true` | `false` | 有限重放中余数门候选未触发断点；这不是全局证明。 | finite evidence only |
| `GlobalResidueCapEnvelopeProved` | `false` | `false` | 仍需全局证明高素数 q 层、余数 cap 与 companion prime 不能共同达到断点。 | SelectorGoodShellEuclideanResidueCapEnvelopeOrResiduePrimePairPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 fixed-u 短 Goldbach 层压成 CRT-ready 余数门。 | SelectorGoodShellEuclideanResidueCapEnvelopeOrResiduePrimePairPDEC |

## 7. 下一步

- 主攻：`SelectorGoodShellEuclideanResidueCapEnvelopeOrResiduePrimePairPDEC`。
- 具体目标：控制 `q=P-2b` 为素数、`2b^2 mod q` 落入 cap、`m` 为素数三条件的同步密度；若不能直接上界，则登记为 residue-prime-pair PDEC/SAE。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_euclidean_residue_gate_router.py` | `ed3f1dcdbe3a4015685a74c81cffdcead86b20d2752095190ff36437b6119956` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py` | `2b436d80485f8facf51dffb6411bff8c73d56ab36ed99bc0229b1a45911df80e` |
| `experiments/prime_matrix_square_phase_even_layer_interval_router.py` | `9e243ffa1743280677931b841a5227047791d4eaecbcfe3c64e6457394475e90` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-ledger.json` | `ec479a8c592f01c52ac1b53fc2bafb22d7e94b6b35c9808d4440d0d4e488e338` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-ledger.json` | `c6d719de684899e3cbe7e153c1c5a063a07cdad9d3d9f1527e3de45e8ae579cc` |
