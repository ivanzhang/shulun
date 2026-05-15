# Prime Matrix square-phase off-band prefix gap shadow selector small modulus candidate router

**状态：** `selector_small_modulus_candidates_lowwheel_conflict_open_global`

本步把 small-modulus 缺口具体化：当前前沿存在 7 个 M<=W 的相位兼容覆盖词，但它们全部满足 residue mod gcd(M,15) 与 actual P 不同，因此已经被低轮结构冲突排除；需要 PDEC 的非冲突候选数为 0。全局剩余变成证明 formal-unit 族中所有 small-modulus 兼容词都必然低轮冲突，或对非冲突 survivor 提交 PDEC/ColumnCRT。

```text
small_modulus_candidate_count=7
structural_conflict_candidate_count=7
overlap_pdec_candidate_count=0
candidate_rows_count=4
row_column_unconditional_closed=false
```

## 1. 小模数候选

| idx | P | W | candidates | structural conflicts | PDEC candidates |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 733 | 8 | 0 | 0 | 0 |
| 1 | 523 | 96 | 0 | 0 | 0 |
| 2 | 691 | 117 | 2 | 2 | 0 |
| 3 | 683 | 172 | 2 | 2 | 0 |
| 4 | 733 | 100 | 0 | 0 | 0 |
| 5 | 673 | 28 | 0 | 0 | 0 |
| 6 | 733 | 8 | 0 | 0 | 0 |
| 7 | 313 | 32 | 1 | 1 | 0 |
| 8 | 1129 | 72 | 0 | 0 | 0 |
| 9 | 691 | 117 | 2 | 2 | 0 |
| 10 | 673 | 28 | 0 | 0 | 0 |

## 2. 候选明细

| P | labels | M | W | gcd(M,15) | residue mod gcd | P mod gcd | window values | structural conflict |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 691 | `[3, 7, 5]` | 105 | 117 | 15 | 2 | 1 | `[677]` | `true` |
| 691 | `[7, 3, 5]` | 105 | 117 | 15 | 7 | 1 | `[682]` | `true` |
| 683 | `[3, 7, 5, 3]` | 105 | 172 | 15 | 7 | 8 | `[667, 772]` | `true` |
| 683 | `[3, 11, 5, 3]` | 165 | 172 | 15 | 7 | 8 | `[712]` | `true` |
| 313 | `[7, 3]` | 21 | 32 | 3 | 2 | 1 | `[296, 317]` | `true` |
| 691 | `[3, 7, 5]` | 105 | 117 | 15 | 2 | 1 | `[677]` | `true` |
| 691 | `[7, 3, 5]` | 105 | 117 | 15 | 7 | 1 | `[682]` | `true` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_small_modulus_candidates_exhausted` | `closed_on_current_frontier` | All current compatible cover words with M<=W are explicitly enumerated. |
| `finite_small_modulus_lowwheel_conflict` | `closed_on_current_frontier` | Every current small-modulus compatible word is structurally conflicting modulo gcd(M,15). |
| `global_small_modulus_lowwheel_conflict` | `open` | A global proof must show every small-modulus compatible word in the formal-unit family is a lowwheel conflict. |
| `small_modulus_overlap_pdec` | `open` | Any non-conflicting small-modulus survivor must be routed to PDEC/ColumnCRT. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteSmallModulusEnumerationClosed` | `true` | `true` | 当前 M<=W 的相位兼容覆盖词已全部枚举。 | closed on current finite frontier |
| `FiniteSmallModulusAllLowwheelConflict` | `true` | `true` | 当前小模数候选全部由 gcd(M,15) 结构冲突排除。 | closed on current finite frontier |
| `GlobalSmallModulusLowwheelConflictProved` | `false` | `false` | 尚未证明 formal-unit 族中小模数候选必然结构冲突。 | SmallModulusCompatibleWordsLowwheelConflictOrOverlapPDEC |
| `SmallModulusOverlapPDECExcluded` | `false` | `false` | 若出现非冲突 small-modulus survivor，仍需 PDEC/ColumnCRT 排斥。 | SmallModulusCompatibleWordsLowwheelConflictOrOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭当前小模数候选筛，不关闭全局行/列命题。 | SmallModulusCompatibleWordsLowwheelConflictOrOverlapPDEC |

## 5. 下一步

- 主攻：`SmallModulusCompatibleWordsLowwheelConflictOrOverlapPDEC`。
- 直接证明目标：证明 formal-unit 族中 `M<=W` 的兼容词必然满足低轮结构冲突。
- 若存在非冲突 small-modulus survivor，则登记为 overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_candidate_router.py` | `ecc1f8375277523c8cff1010e9e2ad9b380fd79d953a312ec1980a4409198d25` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_label_lower_bound_router.py` | `985e10cf4ebcdd80951a956b2f82db1f1723fa2980f369ad0271d16733b64abb` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
| `data/square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-ledger.json` | `5ab54c5084e14c07df5a99ff57dea510f27ec0ff0a2088782da4a807bdb4985c` |
| `data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json` | `e3b34a34f5ca89d882cb98a8473f5820568ffbd60c1e48b1bbe56fd9418eb509` |
