# Prime Matrix square-phase off-band prefix gap shadow short-b cell factor cover router

**状态：** `selected_cell_void_reduced_to_short_b_small_factor_cover_open`

本步把 selected non-survivor small-k cell 的 void 进一步改写为短 b 单元小因子覆盖：因为每个 q=P-2b 都小于 P，若 q 合数则有素因子 ell<=sqrt(P)，等价于 CRT 残基 P≡2b (mod ell)。有限前沿每个 cell 都至少有一个未被小因子覆盖的位置，即实际素数；但全局仍需排斥完整短覆盖字，或把它提升为固定相位 PDEC/ColumnCRT 矛盾。

```text
record_count=11
complete_small_factor_cover_actual_count=0
uncovered_candidate_count_range=1..2
max_cell_length=5
max_parent_atom_k=2
max_distinct_least_small_factor_label_count=3
row_column_unconditional_closed=false
```

## 1. 等价压缩

对 selected cell 中的每个候选：

```text
q = P - 2b < P
q composite  <=>  exists prime ell <= sqrt(P) with ell | q
ell | q      <=>  P ≡ 2b (mod ell)
```

因此 selected-cell void 等价于短 b 区间被这些小素因子残基完全覆盖。

## 2. 覆盖前沿

| P | side | b cell | q cell | covered | uncovered q | least labels |
| ---: | --- | --- | --- | ---: | --- | --- |
| 733 | `plus` | `23-26` | `681-687` | `3/4` | `[683]` | `[3, 5]` |
| 523 | `plus` | `12-15` | `493-499` | `3/4` | `[499]` | `[3, 7, 17]` |
| 691 | `minus` | `19-21` | `649-653` | `2/3` | `[653]` | `[3, 11]` |
| 683 | `plus` | `14-17` | `649-655` | `3/4` | `[653]` | `[3, 5, 11]` |
| 733 | `plus` | `14-18` | `697-705` | `4/5` | `[701]` | `[3, 17, 19]` |
| 673 | `minus` | `25-27` | `619-623` | `2/3` | `[619]` | `[3, 7]` |
| 733 | `plus` | `23-26` | `681-687` | `3/4` | `[683]` | `[3, 5]` |
| 313 | `plus` | `15-16` | `281-283` | `0/2` | `[281, 283]` | `[]` |
| 1129 | `plus` | `29-32` | `1065-1071` | `3/4` | `[1069]` | `[3, 11]` |
| 691 | `minus` | `19-21` | `649-653` | `2/3` | `[653]` | `[3, 11]` |
| 673 | `minus` | `25-27` | `619-623` | `2/3` | `[619]` | `[3, 7]` |

## 3. 标签复用刚性

若同一奇素数 `ell` 同时覆盖 `b_i,b_j`，则 `ell | b_i-b_j`。在长度至多 5 的 cell 中，`ell>=5` 至多覆盖一个位置，只有 `ell=3` 可能隔 3 个 b 复用一次。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `cell_void_to_small_factor_cover` | `closed` | Since every selected q is below P, q-composite is equivalent to the existence of a prime divisor ell<=sqrt(P). |
| `small_factor_cover_to_crt_residue_word` | `closed` | For q=P-2b, a small factor ell gives the residue constraint P≡2b mod ell. |
| `short_cell_label_reuse_bound` | `closed` | In a b-cell of length at most five, an odd label ell>=5 hits at most one b; ell=3 can hit at most two. |
| `finite_incomplete_cover_frontier` | `finite_evidence` | The finite frontier has at least one uncovered candidate in every selected cell. |
| `global_complete_cover_exclusion` | `open` | A global proof still needs to exclude complete short residue-cover words under the fixed small-k phase constraints. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CellVoidSmallFactorCoverEquivalenceClosed` | `true` | `true` | selected-cell void 已等价写成短 b 区间的小素因子覆盖。 | closed |
| `CRTResidueWordFormClosed` | `true` | `true` | 每个覆盖标签都是 `P ≡ 2b (mod ell)` 的 CRT 残基约束。 | closed |
| `FiniteNoCompleteCover` | `true` | `false` | 有限前沿每个 selected cell 都至少有一个未被小因子覆盖的位置。 | finite evidence only |
| `GlobalCompleteCoverExcluded` | `false` | `false` | 仍需排斥固定 small-k 相位下的完整短覆盖字，或证明其回流到 PDEC/ColumnCRT。 | ShortBCellCompleteSmallFactorCoverPDECExclusionOrPhaseLift |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把终端 void 改写为残基覆盖系统，不关闭全局命题。 | ShortBCellCompleteSmallFactorCoverPDECExclusionOrPhaseLift |

## 6. 下一步

- 主攻：`ShortBCellCompleteSmallFactorCoverPDECExclusionOrPhaseLift`。
- 直接目标是排斥完整短覆盖字：所有 `b` 都被 `P≡2b (mod ell)` 小素标签覆盖。
- 这正好对接 CRT/逆元最小对齐解思路，但目前还没有推出全局矛盾。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_short_b_cell_factor_cover_router.py` | `aad8309144697dc6edffb53438c817b09e31f0c57717303564464afb416df073` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_contradiction_field_router.py` | `3d686ebffdabdfe06cafdb0429abbe7d80c4eb3e5aef150028448a35f2e95b4f` |
| `data/square-phase-offband-prefix-gap-shadow-contradiction-field-ledger.json` | `c8a0b0b7bc1eb7dfa022ee4d596d6a0807ded0e4fb507ba541fe66ef3b34ad38` |
| `data/square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-ledger.json` | `582dd7af864d3af9a0448caac174bdb014afd638bbe5f5d16042f47b080dc15f` |
