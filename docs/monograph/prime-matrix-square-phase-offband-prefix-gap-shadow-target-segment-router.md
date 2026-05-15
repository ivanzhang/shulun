# Prime Matrix square-phase off-band prefix gap shadow target segment router

**状态：** `target_overlap_cell_reduced_to_selected_target_segment_open`

本步把 target-overlap cell 继续压成单个 target atom segment：选中 cell 与目标 union 区间取交，再选出最短的实际非空 target segment。有限前沿 11 个包全部成功，选中 segment 长度为 2..5 个奇候选；全局仍需证明这些显式 target segment 含素数，或排斥 segment-void PDEC。

```text
packet_count=11
selector_success_count=11
selector_failure_count=0
selected_segment_candidate_count_range=2..5
selected_segment_target_prime_count_range=1..2
row_column_unconditional_closed=false
```

## 1. target segment 选择

把 selected cell 与每个 target union interval 取交；若某个交段含素数，则 target-union void 直接失败。有限前沿选择最短的非空 target segment。

## 2. 选择前沿

| P | side | selected segment | candidates | target primes | parent interval |
| ---: | --- | --- | ---: | --- | --- |
| 733 | `plus` | `681-687` | 4 | `[683]` | `681-687` |
| 523 | `plus` | `493-501` | 5 | `[499]` | `493-501` |
| 691 | `minus` | `649-653` | 3 | `[653]` | `649-653` |
| 683 | `plus` | `649-657` | 5 | `[653]` | `649-657` |
| 733 | `plus` | `697-705` | 5 | `[701]` | `697-705` |
| 673 | `minus` | `619-623` | 3 | `[619]` | `619-623` |
| 733 | `plus` | `681-687` | 4 | `[683]` | `681-687` |
| 313 | `plus` | `281-283` | 2 | `[281, 283]` | `281-283` |
| 1129 | `plus` | `1065-1071` | 4 | `[1069]` | `1065-1071` |
| 691 | `minus` | `649-653` | 3 | `[653]` | `649-653` |
| 673 | `minus` | `619-623` | 3 | `[619]` | `619-623` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `target_cell_to_target_segments` | `closed` | The selected target-overlap cell splits into intersections with explicit target-union intervals. |
| `single_target_segment_prime_supply_excludes_union_void` | `closed` | If one selected target segment contains a prime, the target-union void assumption is contradicted. |
| `finite_target_segment_selector` | `finite_evidence` | Every finite packet has a selected non-void target segment of length at most five odd candidates. |
| `global_selected_target_segment_prime_supply` | `open` | A global proof still needs a prime in the selected target atom segment, or exclusion of segment-void PDEC. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TargetSegmentReductionClosed` | `true` | `true` | target-overlap cell 已压到显式 target interval 交段。 | closed |
| `SingleTargetSegmentCriterionClosed` | `true` | `true` | 单个 target segment 含素数即可否定 union void。 | closed |
| `FiniteTargetSegmentSelectorSucceeds` | `true` | `false` | 有限前沿每个包都有非空 target segment。 | finite evidence only |
| `GlobalSelectedTargetSegmentSupplyClosed` | `false` | `false` | 仍需全局证明选中 segment 含素数，或排斥 segment-void PDEC。 | SelectedTargetAtomSegmentPrimeSupplyOrSegmentVoidPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 target segment 压缩，不关闭全局行/列命题。 | SelectedTargetAtomSegmentPrimeSupplyOrSegmentVoidPDEC |

## 5. 下一步

- 主攻：`SelectedTargetAtomSegmentPrimeSupplyOrSegmentVoidPDEC`。
- 对长度 2..5 的 selected target segments 建立统一素数供给，或证明其同时为空会触发列相位/平方锚矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_target_segment_router.py` | `6c2d51cb006b9dc0be706938dd6eeea687d7e5cb03544a1bc32996408f643287` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_escape_cell_selector_router.py` | `a8ae64c4db5d51dce05a2f74677d920eefaaffd43fd474385c050818a307bb1f` |
| `data/square-phase-offband-prefix-gap-shadow-escape-cell-selector-ledger.json` | `63031ec8fd4346d5b136d044f99ba2346e6695ab5da5912b81d6668c018ac568` |
| `data/square-phase-offband-prefix-gap-shadow-target-segment-ledger.json` | `946982cb153409640b672ccaf4a073e56d5161aa2e7eea87d57295c5588a1372` |
