# Prime Matrix square-phase off-band prefix gap shadow escape cell selector router

**状态：** `target_overlap_escape_cell_selector_registered_open`

本步把 single gap-cell supply 再收窄到 target-overlap cell：只有落入目标 union 的素数才能直接否定原始 union void。有限前沿中每个包都可选出一个 target-overlap escape cell，且没有纯互补 cell 承担逃逸；全局仍需证明选中 target-overlap cell 必含 target prime，或排斥 target-cell void PDEC。

```text
packet_count=11
selector_success_count=11
selector_failure_count=0
pure_complement_nonvoid_packet_count=0
selected_cell_candidate_count_range=4..10
row_column_unconditional_closed=false
```

## 1. 选择规则

只选择与目标 union 相交且实际含 target prime 的 gap cell；若能全局证明该 cell 含素数，则原始 target-union void 直接矛盾。

## 2. 选择前沿

| P | side | selected cell | type | target primes | complement primes |
| ---: | --- | --- | --- | --- | --- |
| 733 | `plus` | `679-687` | `mixed_gap_cell` | `[683]` | `[]` |
| 523 | `plus` | `493-501` | `target_union_gap_cell` | `[499]` | `[]` |
| 691 | `minus` | `649-657` | `mixed_gap_cell` | `[653]` | `[]` |
| 683 | `plus` | `649-657` | `target_union_gap_cell` | `[653]` | `[]` |
| 733 | `plus` | `693-705` | `mixed_gap_cell` | `[701]` | `[]` |
| 673 | `minus` | `619-637` | `mixed_gap_cell` | `[619, 631]` | `[]` |
| 733 | `plus` | `681-689` | `mixed_gap_cell` | `[683]` | `[]` |
| 313 | `plus` | `279-295` | `mixed_gap_cell` | `[281, 283, 293]` | `[]` |
| 1129 | `plus` | `1065-1071` | `target_union_gap_cell` | `[1069]` | `[]` |
| 691 | `minus` | `649-657` | `mixed_gap_cell` | `[653]` | `[]` |
| 673 | `minus` | `619-629` | `mixed_gap_cell` | `[619]` | `[]` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `target_overlap_selector` | `closed` | If a target-overlap gap cell contains a target prime, the original target-union void assumption is false. |
| `finite_no_pure_complement_escape` | `finite_evidence` | In the finite frontier, every escaping prime lies in a target-overlap cell; pure complement cells do not supply escapes. |
| `finite_target_escape_selector` | `finite_evidence` | Every finite packet has a selected target-overlap cell with at least one target prime. |
| `global_target_overlap_prime_supply` | `open` | A global proof still needs a target prime in at least one selected target-overlap cell, or exclusion of target-cell void PDEC. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TargetOverlapSelectorClosed` | `true` | `true` | target-overlap cell 含 target prime 直接否定原始 union void。 | closed |
| `FiniteSelectorSucceeds` | `true` | `false` | 有限前沿每个包都有 target-overlap escape cell。 | finite evidence only |
| `FinitePureComplementEscapeAbsent` | `true` | `false` | 有限前沿纯互补 cell 未承担逃逸素数。 | finite evidence only |
| `GlobalTargetCellPrimeSupplyClosed` | `false` | `false` | 仍需全局证明选中 target-overlap cell 含 target prime。 | TargetOverlapGapCellPrimeSupplyOrTargetCellVoidPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 escape cell 选择，不关闭全局行/列命题。 | TargetOverlapGapCellPrimeSupplyOrTargetCellVoidPDEC |

## 5. 下一步

- 主攻：`TargetOverlapGapCellPrimeSupplyOrTargetCellVoidPDEC`。
- 对选中 target-overlap cells 建立统一素数供给，或证明同时为空会触发列相位/平方锚矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_escape_cell_selector_router.py` | `a8ae64c4db5d51dce05a2f74677d920eefaaffd43fd474385c050818a307bb1f` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_gap_cell_router.py` | `b563bc3b9c01bc7f2eb8034067e5b91c17ee775f48aa01c5f4fd666ce561c23b` |
| `data/square-phase-offband-prefix-gap-shadow-gap-cell-ledger.json` | `ac04a88489870922cb63f322e7515657d8762ec5fb4af58e7040c498512cedce` |
| `data/square-phase-offband-prefix-gap-shadow-escape-cell-selector-ledger.json` | `63031ec8fd4346d5b136d044f99ba2346e6695ab5da5912b81d6668c018ac568` |
