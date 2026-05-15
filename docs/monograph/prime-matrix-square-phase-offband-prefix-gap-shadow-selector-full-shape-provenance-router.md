# Prime Matrix square-phase off-band prefix gap shadow selector full-shape provenance router

**状态：** `selector_matching_templates_excluded_by_current_full_shape_replay_open_global`

本步把上一层 phase+素性无法排除的 matching prime representatives 代回完整上游 gap-shadow selector。结果：当前全部 matching 代表只匹配局部父 atom 相位，没有一个提升为同一 `W,N,V,ordered band/k` 完整 shape。因此当前有限前沿暂无 matching-template overlap PDEC 实例；真正剩余收窄为把这种 full-shape selector 来源写成 formal-unit 族的符号定理。

```text
candidate_instance_count=7
source_template_count=5
raw_candidate_matching_prime_check_count=15
unique_replay_prime_count=7
full_shape_compatible_check_count=0
full_shape_excluded_check_count=15
template_overlap_pdec_after_full_shape_count=0
row_column_unconditional_closed=false
```

## 1. Full-Shape Replay

| source P | replay P | side | labels | target parent | W replay | replay templates | full-shape compatible | reason |
| ---: | ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| 691 | 647 | `minus` | `[3, 7, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 691 | 677 | `minus` | `[3, 7, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 691 | 727 | `minus` | `[7, 3, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 691 | 757 | `minus` | `[7, 3, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 683 | 727 | `plus` | `[3, 7, 5, 3]` | `minus_only_noslot:k0` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 683 | 757 | `plus` | `[3, 7, 5, 3]` | `minus_only_noslot:k0` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 683 | 727 | `plus` | `[3, 11, 5, 3]` | `minus_only_noslot:k0` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 683 | 757 | `plus` | `[3, 11, 5, 3]` | `minus_only_noslot:k0` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 313 | 293 | `plus` | `[7, 3]` | `minus_only_noslot:k1` | 1 | 1 | `false` | `DifferentFullShapeKey` |
| 313 | 311 | `plus` | `[7, 3]` | `minus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 313 | 317 | `plus` | `[7, 3]` | `minus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 691 | 647 | `minus` | `[3, 7, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 691 | 677 | `minus` | `[3, 7, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 691 | 727 | `minus` | `[7, 3, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |
| 691 | 757 | `minus` | `[7, 3, 5]` | `plus_only_noslot:k1` | 0 | 0 | `false` | `OffbandWitnessRequirementZero` |

## 2. Template Summary

| template | replay primes | compatible | excluded | positive W replay | reasons |
| --- | --- | ---: | ---: | ---: | --- |
| `shape=side=minus\|W=2\|N=3\|V=2\|both_offband_middle:k0,plus_only_noslot:k1\|parent=plus_only_noslot:k1\|labels=3,5,7\|rho=2` | `[647, 677]` | 0 | 2 | 0 | `['OffbandWitnessRequirementZero']` |
| `shape=side=minus\|W=2\|N=3\|V=2\|both_offband_middle:k0,plus_only_noslot:k1\|parent=plus_only_noslot:k1\|labels=3,5,7\|rho=7` | `[727, 757]` | 0 | 2 | 0 | `['OffbandWitnessRequirementZero']` |
| `shape=side=minus\|W=2\|N=3\|V=2\|plus_only_noslot:k0,plus_only_noslot:k1\|parent=plus_only_noslot:k1\|labels=3,5,7\|rho=2` | `[647, 677]` | 0 | 2 | 0 | `['OffbandWitnessRequirementZero']` |
| `shape=side=minus\|W=2\|N=3\|V=2\|plus_only_noslot:k0,plus_only_noslot:k1\|parent=plus_only_noslot:k1\|labels=3,5,7\|rho=7` | `[727, 757]` | 0 | 2 | 0 | `['OffbandWitnessRequirementZero']` |
| `shape=side=plus\|W=1\|N=3\|V=3\|both_offband_middle:k0,minus_only_noslot:k0,both_offband_middle:k1\|parent=minus_only_noslot:k0\|labels=3,5,11\|rho=7` | `[727, 757]` | 0 | 2 | 0 | `['OffbandWitnessRequirementZero']` |
| `shape=side=plus\|W=1\|N=3\|V=3\|both_offband_middle:k0,minus_only_noslot:k0,both_offband_middle:k1\|parent=minus_only_noslot:k0\|labels=3,5,7\|rho=7` | `[727, 757]` | 0 | 2 | 0 | `['OffbandWitnessRequirementZero']` |
| `shape=side=plus\|W=1\|N=3\|V=3\|minus_only_noslot:k0,minus_only_noslot:k1,minus_only_noslot:k2\|parent=minus_only_noslot:k1\|labels=3,7\|rho=2` | `[293, 311, 317]` | 0 | 3 | 1 | `['DifferentFullShapeKey', 'OffbandWitnessRequirementZero']` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `matching_prime_replay_registered` | `closed_on_current_frontier` | Every matching prime representative from the template provenance ledger is replayed through the full upstream gap-shadow selector. |
| `parent_phase_not_full_shape` | `closed_on_current_frontier` | Matching a parent atom phase window is strictly weaker than matching the full W,N,V and ordered band/k shape. |
| `current_matching_templates_do_not_lift` | `closed_on_current_frontier` | No current matching prime representative lifts to the same full shape template. |
| `global_full_shape_selector_source` | `open` | A global proof still must derive the same full-shape selector provenance symbolically for the formal-unit family. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `MatchingRepresentativesReplayed` | `true` | `true` | 上一层 matching primes 已全部代回完整上游构造。 | closed on current finite frontier |
| `CurrentMatchingTemplatesLiftToFullShape` | `true` | `true` | 当前 matching primes 只匹配局部父 atom，不匹配完整 shape。 | closed on current finite frontier |
| `TemplateOverlapPDECNeededNow` | `true` | `true` | 当前有限前沿没有 full-shape overlap PDEC 实例。 | closed on current finite frontier |
| `GlobalFormalUnitSelectorSourceProved` | `false` | `false` | 仍需把 full-shape 回放提升为 formal-unit 族的符号来源定理。 | FullShapeFormalUnitSelectorSourceTheoremOrMatchingTemplateOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭当前 matching prime 代表的完整形状回放，不关闭全局行/列命题。 | FullShapeFormalUnitSelectorSourceTheoremOrMatchingTemplateOverlapPDEC |

## 5. 下一步

- 主攻：`FullShapeFormalUnitSelectorSourceTheoremOrMatchingTemplateOverlapPDEC`。
- 当前有限 matching 代表已经被完整 shape 回放排除。
- 仍需把回放中使用的 `W_required`、prefix atom 排序和 ordered band/k 约束写成 formal-unit 族的符号来源定理。
- 若符号来源定理失败，则必须登记 full-shape overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_full_shape_provenance_router.py` | `8c10be38d91e42a7ccc507a57cab829d1709b0e68afc4f03aa88c98f1ef063c9` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_template_provenance_router.py` | `3e29bf7e46148084bf4f1a8ef57acb8d8aa8aa9a3d6ce62c03ec43b7bfe4aa71` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-ledger.json` | `9c108614b8a2df80ae8819e9a9928e5b1d06ec3db40528313d6d42f12e1de68a` |
