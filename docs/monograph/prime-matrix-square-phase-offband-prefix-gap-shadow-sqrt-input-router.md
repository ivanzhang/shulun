# Prime Matrix square-phase off-band prefix gap shadow sqrt-input router

**状态：** `fixed_shape_gap_shadow_reduced_to_union_prime_supply_or_sqrt_gap_input_open`

本步把固定小 k 形状 PDEC 的最后数学输入边界写清：每个强制 prime-void 模板，只要其固定 q 区间并集含一个素数就被排除。若模板覆盖整个奇 q hull，则这正是 P 下方长度 depth 的后向素数间隙输入；若存在覆盖缺口，则是更精细的穿孔固定形状并集素数供给输入。有限账本中所有模板并集实际都含素数，但全局仍未证明。

```text
template_count=27
shape_count=15
actual_template_void_count=0
max_depth_from_p=78
max_depth_over_sqrt_p=2.321387
row_column_unconditional_closed=false
```

## 1. 输入边界

每个 failure 模板是一组固定前缀 atom 区间。若这些区间并集中存在一个素数 `q`，则该模板不可能全空，gap shadow 被排除。

若这些 atom 覆盖其 hull 内全部奇 `q`，则所需输入就是

```text
there is a prime in [P-depth, P) with the correct odd parity
```

也就是 `P` 下方 sqrt 尺度的后向素数间隙界。否则，它是穿孔形状并集的素数供给问题。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| template records | 27 |
| shape count | 15 |
| input types | `{'BackwardSqrtPrimeGap': 5, 'PuncturedShapeUnionPrimeSupply': 22}` |
| actual template void count | 0 |
| max depth from P | 78 |
| max depth/sqrt(P) | 2.321387 |
| max coverage defect candidates | 12 |

## 3. 最深模板边界

| P | side | type | load | q hull | depth | depth/sqrt(P) | coverage defect | atoms |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | --- |
| 1129 | `plus` | `PuncturedShapeUnionPrimeSupply` | 5 | `1051-1095` | 78 | 2.321387 | 9 | `minus_only_noslot:k0:1083-1095,minus_only_noslot:k1:1065-1071,minus_only_noslot:k2:1051-1055` |
| 313 | `plus` | `PuncturedShapeUnionPrimeSupply` | 3 | `273-295` | 40 | 2.260934 | 4 | `minus_only_noslot:k0:289-295,minus_only_noslot:k1:281-283,minus_only_noslot:k2:273-275` |
| 733 | `plus` | `PuncturedShapeUnionPrimeSupply` | 1 | `675-705` | 58 | 2.142279 | 10 | `minus_only_noslot:k0:697-705,both_offband_middle:k2:675-675` |
| 733 | `plus` | `PuncturedShapeUnionPrimeSupply` | 1 | `675-687` | 58 | 2.142279 | 2 | `minus_only_noslot:k1:681-687,both_offband_middle:k2:675-675` |
| 673 | `minus` | `PuncturedShapeUnionPrimeSupply` | 2 | `619-637` | 54 | 2.081547 | 3 | `plus_only_noslot:k1:631-637,plus_only_noslot:k2:619-623` |
| 673 | `minus` | `PuncturedShapeUnionPrimeSupply` | 4 | `619-671` | 54 | 2.081547 | 12 | `plus_only_noslot:k0:649-671,plus_only_noslot:k2:619-623` |
| 733 | `plus` | `PuncturedShapeUnionPrimeSupply` | 2 | `681-705` | 52 | 1.920664 | 4 | `minus_only_noslot:k0:697-705,minus_only_noslot:k1:681-687` |
| 487 | `plus` | `PuncturedShapeUnionPrimeSupply` | 4 | `445-465` | 42 | 1.903202 | 3 | `both_offband_middle:k0:465-465,minus_only_noslot:k0:457-463,minus_only_noslot:k1:445-449` |
| 293 | `plus` | `PuncturedShapeUnionPrimeSupply` | 2 | `261-275` | 32 | 1.869460 | 2 | `minus_only_noslot:k0:271-275,both_offband_middle:k1:265-265,minus_only_noslot:k1:261-263` |
| 113 | `plus` | `PuncturedShapeUnionPrimeSupply` | 2 | `95-103` | 18 | 1.693298 | 1 | `both_offband_middle:k0:103-103,minus_only_noslot:k0:99-101,minus_only_noslot:k1:95-95` |
| 683 | `plus` | `PuncturedShapeUnionPrimeSupply` | 1 | `639-657` | 44 | 1.683613 | 4 | `both_offband_middle:k0:657-657,minus_only_noslot:k0:649-655,both_offband_middle:k1:639-639` |
| 523 | `plus` | `PuncturedShapeUnionPrimeSupply` | 1 | `485-501` | 38 | 1.661624 | 3 | `both_offband_middle:k0:501-501,minus_only_noslot:k0:493-499,both_offband_middle:k1:485-485` |
| 421 | `plus` | `PuncturedShapeUnionPrimeSupply` | 2 | `387-401` | 34 | 1.657059 | 2 | `both_offband_middle:k0:401-401,minus_only_noslot:k0:393-399,both_offband_middle:k1:387-387` |
| 73 | `plus` | `PuncturedShapeUnionPrimeSupply` | 1 | `59-65` | 14 | 1.638576 | 1 | `both_offband_middle:k0:65-65,minus_only_noslot:k0:63-63,minus_only_noslot:k1:59-59` |
| 673 | `minus` | `PuncturedShapeUnionPrimeSupply` | 4 | `631-671` | 42 | 1.618981 | 5 | `plus_only_noslot:k0:649-671,plus_only_noslot:k1:631-637` |
| 691 | `minus` | `PuncturedShapeUnionPrimeSupply` | 1 | `649-665` | 42 | 1.597755 | 5 | `both_offband_middle:k0:665-665,plus_only_noslot:k1:649-653` |
| 691 | `minus` | `PuncturedShapeUnionPrimeSupply` | 4 | `649-689` | 42 | 1.597755 | 6 | `plus_only_noslot:k0:667-689,plus_only_noslot:k1:649-653` |
| 271 | `minus` | `PuncturedShapeUnionPrimeSupply` | 3 | `245-269` | 26 | 1.579388 | 3 | `plus_only_noslot:k0:257-269,both_offband_middle:k0:255-255,plus_only_noslot:k1:245-247` |
| 419 | `minus` | `PuncturedShapeUnionPrimeSupply` | 3 | `387-417` | 32 | 1.563302 | 3 | `plus_only_noslot:k0:401-417,both_offband_middle:k0:399-399,plus_only_noslot:k1:387-391` |
| 199 | `minus` | `PuncturedShapeUnionPrimeSupply` | 4 | `177-197` | 22 | 1.559539 | 2 | `plus_only_noslot:k0:187-197,both_offband_middle:k0:185-185,plus_only_noslot:k1:177-179` |
| 157 | `minus` | `PuncturedShapeUnionPrimeSupply` | 3 | `139-155` | 18 | 1.436556 | 2 | `plus_only_noslot:k0:147-155,both_offband_middle:k0:145-145,plus_only_noslot:k1:139-139` |
| 73 | `minus` | `PuncturedShapeUnionPrimeSupply` | 3 | `61-71` | 12 | 1.404494 | 1 | `plus_only_noslot:k0:67-71,both_offband_middle:k0:65-65,plus_only_noslot:k1:61-61` |
| 691 | `minus` | `BackwardSqrtPrimeGap` | 3 | `665-689` | 26 | 0.989087 | 0 | `plus_only_noslot:k0:667-689,both_offband_middle:k0:665-665` |
| 37 | `minus` | `BackwardSqrtPrimeGap` | 1 | `31-35` | 6 | 0.986394 | 0 | `plus_only_noslot:k0:33-35,both_offband_middle:k0:31-31` |

## 4. 形状输入摘要

| count | shape | input types | P range | max depth/sqrt(P) | min load | max defect |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 5 | `side=minus|W=1|N=3|V=3|plus_only_noslot:k0,both_offband_middle:k0,plus_only_noslot:k1` | `{'PuncturedShapeUnionPrimeSupply': 5}` | 73..419 | 1.579388 | 3 | 3 |
| 3 | `side=plus|W=1|N=3|V=3|both_offband_middle:k0,minus_only_noslot:k0,minus_only_noslot:k1` | `{'PuncturedShapeUnionPrimeSupply': 3}` | 73..487 | 1.903202 | 1 | 3 |
| 3 | `side=plus|W=1|N=3|V=3|both_offband_middle:k0,minus_only_noslot:k0,both_offband_middle:k1` | `{'PuncturedShapeUnionPrimeSupply': 3}` | 421..683 | 1.683613 | 1 | 4 |
| 3 | `side=minus|W=1|N=2|V=2|plus_only_noslot:k0,both_offband_middle:k0` | `{'BackwardSqrtPrimeGap': 3}` | 37..47 | 0.986394 | 1 | 0 |
| 2 | `side=plus|W=1|N=3|V=3|minus_only_noslot:k0,minus_only_noslot:k1,minus_only_noslot:k2` | `{'PuncturedShapeUnionPrimeSupply': 2}` | 313..1129 | 2.321387 | 3 | 9 |
| 2 | `side=minus|W=2|N=3|V=2|plus_only_noslot:k0,plus_only_noslot:k1` | `{'PuncturedShapeUnionPrimeSupply': 2}` | 673..691 | 1.618981 | 4 | 6 |
| 1 | `side=plus|W=2|N=3|V=2|minus_only_noslot:k0,both_offband_middle:k2` | `{'PuncturedShapeUnionPrimeSupply': 1}` | 733..733 | 2.142279 | 1 | 10 |
| 1 | `side=plus|W=2|N=3|V=2|minus_only_noslot:k1,both_offband_middle:k2` | `{'PuncturedShapeUnionPrimeSupply': 1}` | 733..733 | 2.142279 | 1 | 2 |
| 1 | `side=minus|W=2|N=3|V=2|plus_only_noslot:k0,plus_only_noslot:k2` | `{'PuncturedShapeUnionPrimeSupply': 1}` | 673..673 | 2.081547 | 4 | 12 |
| 1 | `side=minus|W=2|N=3|V=2|plus_only_noslot:k1,plus_only_noslot:k2` | `{'PuncturedShapeUnionPrimeSupply': 1}` | 673..673 | 2.081547 | 2 | 3 |
| 1 | `side=plus|W=2|N=3|V=2|minus_only_noslot:k0,minus_only_noslot:k1` | `{'PuncturedShapeUnionPrimeSupply': 1}` | 733..733 | 1.920664 | 2 | 4 |
| 1 | `side=plus|W=1|N=3|V=3|minus_only_noslot:k0,both_offband_middle:k1,minus_only_noslot:k1` | `{'PuncturedShapeUnionPrimeSupply': 1}` | 293..293 | 1.869460 | 2 | 2 |
| 1 | `side=minus|W=2|N=3|V=2|both_offband_middle:k0,plus_only_noslot:k1` | `{'PuncturedShapeUnionPrimeSupply': 1}` | 691..691 | 1.597755 | 1 | 5 |
| 1 | `side=minus|W=2|N=3|V=2|plus_only_noslot:k0,both_offband_middle:k0` | `{'BackwardSqrtPrimeGap': 1}` | 691..691 | 0.989087 | 3 | 0 |
| 1 | `side=plus|W=1|N=1|V=1|both_offband_middle:k0` | `{'BackwardSqrtPrimeGap': 1}` | 23..23 | 0.834058 | 1 | 0 |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `template_void_exclusion_by_union_prime_supply` | `closed` | A forced void template is excluded once its union of fixed q=P-2b atom intervals contains at least one prime q. |
| `contiguous_template_to_backward_sqrt_gap` | `closed` | If the template covers every odd q in its hull, its exclusion is a backward prime-gap bound below P with length equal to the hull depth. |
| `punctured_template_to_shape_union_supply` | `closed` | If the template does not cover the whole hull, its exclusion is a punctured fixed-shape union prime-supply input. |
| `finite_no_template_void` | `finite_evidence` | The finite audit finds that every listed template union actually contains at least one prime. |
| `global_fixed_shape_union_supply` | `open` | A global proof still needs the fixed-shape union prime-supply theorem, or an external sqrt-scale prime-gap input strong enough to imply it. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TemplateVoidExclusionByUnionPrimeSupplyClosed` | `true` | `true` | 每个强制空模板只要自身并集含素数即可排除。 | closed |
| `SqrtGapInputBoundaryClosed` | `true` | `true` | 连续 hull 模板已等价为 P 下方 sqrt 级后向素数间隙输入。 | closed |
| `FiniteNoTemplateVoid` | `true` | `false` | 有限样本中所有模板并集都含素数。 | finite evidence only |
| `GlobalFixedShapeUnionSupplyClosed` | `false` | `false` | 仍需全局证明固定形状并集素数供给，或引用同等强度短区间素数输入。 | FixedShapeUnionPrimeSupplyOrSqrtScaleGapInput |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只标定最终输入边界，不关闭全局行/列命题。 | FixedShapeUnionPrimeSupplyOrSqrtScaleGapInput |

## 7. 下一步

- 主攻：`FixedShapeUnionPrimeSupplyOrSqrtScaleGapInput`。
- 自足路线必须证明这些固定/穿孔 q 区间并集含素数。
- 外部路线需要 sqrt 尺度后向短区间素数输入；现有有限审计不能替代该全局输入。
- 当前仍未证明全局行/列无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_sqrt_input_router.py` | `4cb2f5e660a97927ab5cb90bb0df1cc3ec2857370a28d4c8bcb32eb309ead438` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_shape_router.py` | `d48eb4ffecbe7bd236bdb568f1db7b1443da0e4718165aafa02b2349911a9ba2` |
| `data/square-phase-offband-prefix-gap-shadow-ledger.json` | `f80e634e8dd67f202e02c0466af8df409217cc4b623b72d519612ee873fd3a74` |
| `data/square-phase-offband-prefix-gap-shadow-shape-ledger.json` | `dbe7b6ec327be0078b515b824004ffea5461a9e5285d85ea5539930ccea79e0d` |
| `data/square-phase-offband-prefix-gap-shadow-sqrt-input-ledger.json` | `819d391201c6719a8f93ab4786657e73e7d06f356971d002615aa8fdc10fd0e5` |
