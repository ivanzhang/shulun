# Prime Matrix square-phase off-band prefix gap shadow segment normal form router

**状态：** `selected_target_atom_piece_normal_form_registered_open`

本步把 selected target segment 继续切回原始 fixed band/k atom pieces，并选出最短的非空 atom piece。有限前沿 11 个包全部选择成功，选中 atom piece 长度为 2..5，父 atom 的最大 k 为 2；全局仍需证明这些 selected small-k atom pieces 含素数，或排斥正规形 atom-piece-void PDEC。

```text
record_count=11
atom_piece_selector_failure_count=0
selected_segment_candidate_count_range=2..5
selected_atom_piece_candidate_count_range=2..5
b_length_range=2..5
max_parent_atom_k=2
row_column_unconditional_closed=false
```

## 1. 正规形

每个 selected target segment 先按原始 atom 切分，再选出一个显式非空 atom piece：

```text
q=P-2b, b_lo<=b<=b_hi, selected atom piece <= parent atom = band:k:qlo-qhi
```

## 2. 正规形前沿

| P | side | q atom piece | b interval | parent atom | primes |
| ---: | --- | --- | --- | --- | --- |
| 733 | `plus` | `681-687` | `23-26` | `minus_only_noslot:k1:681-687` | `[683]` |
| 523 | `plus` | `493-499` | `12-15` | `minus_only_noslot:k0:493-499` | `[499]` |
| 691 | `minus` | `649-653` | `19-21` | `plus_only_noslot:k1:649-653` | `[653]` |
| 683 | `plus` | `649-655` | `14-17` | `minus_only_noslot:k0:649-655` | `[653]` |
| 733 | `plus` | `697-705` | `14-18` | `minus_only_noslot:k0:697-705` | `[701]` |
| 673 | `minus` | `619-623` | `25-27` | `plus_only_noslot:k2:619-623` | `[619]` |
| 733 | `plus` | `681-687` | `23-26` | `minus_only_noslot:k1:681-687` | `[683]` |
| 313 | `plus` | `281-283` | `15-16` | `minus_only_noslot:k1:281-283` | `[281, 283]` |
| 1129 | `plus` | `1065-1071` | `29-32` | `minus_only_noslot:k1:1065-1071` | `[1069]` |
| 691 | `minus` | `649-653` | `19-21` | `plus_only_noslot:k1:649-653` | `[653]` |
| 673 | `minus` | `619-623` | `25-27` | `plus_only_noslot:k2:619-623` | `[619]` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `selected_segment_atom_piece_selector` | `closed` | Every selected target segment contains a selected non-void atom piece from the original fixed band/k atoms. |
| `selected_atom_piece_q_equals_p_minus_2b_normal_form` | `closed` | Each selected atom piece has explicit q=P-2b and b-interval endpoints. |
| `finite_small_k_segment_frontier` | `finite_evidence` | The finite frontier only uses parent atoms with k<=2 and selected atom-piece length at most five. |
| `global_selected_small_k_segment_supply` | `open` | A global proof still needs prime supply in these selected small-k atom pieces, or exclusion of atom-piece-void PDEC. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `AtomPieceSelectorClosed` | `true` | `true` | 每个 selected segment 都已选出一个非空原始 band/k atom piece。 | closed |
| `QEqualsPMinus2BNormalFormClosed` | `true` | `true` | 每个 selected atom piece 已写成 q=P-2b 的 b 区间。 | closed |
| `FiniteSmallKSegmentFrontier` | `true` | `false` | 有限前沿全部为 k<=2 的短 target atom piece。 | finite evidence only |
| `GlobalSmallKSegmentSupplyClosed` | `false` | `false` | 仍需全局证明 selected small-k atom piece 含素数，或排斥 atom-piece void。 | SelectedSmallKAtomPiecePrimeSupplyOrAtomPieceVoidPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 atom-piece 正规形，不关闭全局行/列命题。 | SelectedSmallKAtomPiecePrimeSupplyOrAtomPieceVoidPDEC |

## 5. 下一步

- 主攻：`SelectedSmallKAtomPiecePrimeSupplyOrAtomPieceVoidPDEC`。
- 继续攻击这些 k<=2、长度 2..5 的 q=P-2b atom pieces 素数供给，或把 atom-piece void 接入列相位/平方锚矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_segment_normal_form_router.py` | `ae2b76a0341113f4b98ac2c46598615e597e5bc25aaf23c13b77a1cdeb5ad5ab` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_target_segment_router.py` | `6c2d51cb006b9dc0be706938dd6eeea687d7e5cb03544a1bc32996408f643287` |
| `data/square-phase-offband-prefix-gap-shadow-target-segment-ledger.json` | `946982cb153409640b672ccaf4a073e56d5161aa2e7eea87d57295c5588a1372` |
| `data/square-phase-offband-prefix-gap-shadow-support-collapse-ledger.json` | `221c23d9062defd07903b63b15e284ddd4f86693640f512aa6818c6abda95594` |
| `data/square-phase-offband-prefix-gap-shadow-segment-normal-form-ledger.json` | `41a1178e194c4ade02b18399ec2c5d42f55bea38a44ab9dade7106b1bbb1bc73` |
