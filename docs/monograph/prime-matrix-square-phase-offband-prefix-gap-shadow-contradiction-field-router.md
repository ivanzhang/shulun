# Prime Matrix square-phase off-band prefix gap shadow contradiction field router

**状态：** `terminal_contradiction_field_reduced_to_selected_nonsurvivor_cell_supply_open`

本步把 atom-piece void 与 support-collapse 合并成终端矛盾场：所有 selected atom piece 都与 wheel-17 survivor 集合不相交，因此其中任一素数都会成为 escape prime 并否定支撑塌缩。有限前沿每包确有 selected escape prime；但现有结构还没有全局强制该非幸存 small-k cell 含素数。最新剩余压成 selected non-survivor small-k cell 的素数供给，或排斥 punctured cell void PDEC。

```text
record_count=11
all_selected_pieces_disjoint_from_survivors=true
max_wheel17_survivor_intersection_count=0
min_actual_selected_escape_prime_count=1
actual_support_collapse_count=0
max_selected_candidate_count=5
max_parent_atom_k=2
row_column_unconditional_closed=false
```

## 1. 终端矛盾场

合并后的逻辑是：

```text
support collapse: Prime(hull) subset wheel17 survivors
selected atom piece: selected cell subset hull and selected cell cap wheel17 survivors = empty
therefore: any prime in selected cell is an escape prime and contradicts support collapse
remaining: prove selected cell contains a prime, or exclude selected-cell void as PDEC
```

## 2. 合并前沿

| P | side | selected cell | survivors | intersection | selected escape primes |
| ---: | --- | --- | --- | --- | --- |
| 733 | `plus` | `681-687` | `[677]` | `[]` | `[683]` |
| 523 | `plus` | `493-499` | `[487, 491]` | `[]` | `[499]` |
| 691 | `minus` | `649-653` | `[659, 661]` | `[]` | `[653]` |
| 683 | `plus` | `649-655` | `[641, 643, 647]` | `[]` | `[653]` |
| 733 | `plus` | `697-705` | `[677, 683, 691]` | `[]` | `[701]` |
| 673 | `minus` | `619-623` | `[]` | `[]` | `[619]` |
| 733 | `plus` | `681-687` | `[691]` | `[]` | `[683]` |
| 313 | `plus` | `281-283` | `[277]` | `[]` | `[281, 283]` |
| 1129 | `plus` | `1065-1071` | `[1061, 1063, 1073, 1081]` | `[]` | `[1069]` |
| 691 | `minus` | `649-653` | `[659, 661]` | `[]` | `[653]` |
| 673 | `minus` | `619-623` | `[631, 641, 643, 647]` | `[]` | `[619]` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `selected_piece_survivor_disjointness` | `closed` | Every selected atom-piece in the frontier is disjoint from the wheel-17 survivor set. |
| `selected_prime_implies_support_collapse_escape` | `closed` | A prime in the selected atom-piece is automatically an escape prime outside the support-collapse survivor set. |
| `finite_selected_escape_prime_present` | `finite_evidence` | The finite frontier has at least one selected escape prime in every merged field packet. |
| `direct_structural_contradiction_from_existing_constraints` | `open` | The existing constraints alone do not yet force a prime in the selected non-survivor cell. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SelectedPieceDisjointFromSurvivorsClosed` | `true` | `true` | selected atom-piece 是 wheel-17 支撑塌缩幸存集之外的逃逸单元。 | closed |
| `PrimeInSelectedPieceBreaksSupportCollapse` | `true` | `true` | 该单元一旦含素数，就直接给出 escape prime，反例链崩溃。 | closed |
| `FiniteSelectedEscapePrimePresent` | `true` | `false` | 有限前沿每包都有 selected escape prime；仍不能当全局证明。 | finite evidence only |
| `ExistingConstraintsForceSelectedPrime` | `false` | `false` | 现有支撑塌缩、列相位和 q=P-2b 正规形尚未强制该小单元含素数。 | SelectedNonSurvivorSmallKCellPrimeSupplyOrPuncturedCellVoidPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步把终端矛盾场压到非幸存 small-k cell 素数供给，不关闭全局命题。 | SelectedNonSurvivorSmallKCellPrimeSupplyOrPuncturedCellVoidPDEC |

## 5. 下一步

- 主攻：`SelectedNonSurvivorSmallKCellPrimeSupplyOrPuncturedCellVoidPDEC`。
- 需要证明 selected non-survivor small-k cell 含素数，或把该 cell void 解释成固定相位 PDEC 并排斥。
- 这一步没有把目标换成普通短素数间隙；仍保持同一 off-band prefix 反例链。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_contradiction_field_router.py` | `3d686ebffdabdfe06cafdb0429abbe7d80c4eb3e5aef150028448a35f2e95b4f` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_atom_piece_void_boundary_router.py` | `ea4b9848cf09c980a865a80713c9fc160c74d7501912336dc90748e2096b4ff4` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_support_collapse_router.py` | `69b61f3820afc3daa860fd3ac612bb78d8a3635e89aea87a2b8dafaf2bc5e273` |
| `data/square-phase-offband-prefix-gap-shadow-atom-piece-void-boundary-ledger.json` | `f5bdd68cc74988ed2cb2a115825b20cbcd8a3a172d555381d08b193137500488` |
| `data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json` | `221c23d9062defd07903b63b15e284ddd4f86693640f512aa6818c6abda95594` |
| `data/square-phase-offband-prefix-gap-shadow-contradiction-field-ledger.json` | `c8a0b0b7bc1eb7dfa022ee4d596d6a0807ded0e4fb507ba541fe66ef3b34ad38` |
