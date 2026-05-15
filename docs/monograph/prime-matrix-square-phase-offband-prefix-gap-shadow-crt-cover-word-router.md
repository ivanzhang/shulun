# Prime Matrix square-phase off-band prefix gap shadow CRT cover word router

**状态：** `complete_small_factor_cover_reduced_to_crt_cover_word_open`

本步把完整短覆盖进一步正规化为 CRT 覆盖词。若 selected cell 从 b=B 开始、长度为 L，完整 void 需要标签 ell_t 使 q_start=P-2B 满足 q_start≡2t (mod ell_t)。长度至多 5 时，覆盖词至少需要 L 个不同标签（L<=3）或 L-1 个不同标签（L>=4），对应最小模数下界在当前前沿为 15..1155。CRT 兼容本身不矛盾；最新剩余是排斥这些兼容覆盖词与固定 small-k 相位/列相位同时持久对齐。

```text
record_count=11
complete_crt_cover_word_actual_count=0
missing_new_label_count_lower_bound_range=1..2
complete_word_crt_modulus_lower_bound_range=15..1155
max_cell_length=5
row_column_unconditional_closed=false
```

## 1. CRT 覆盖词

令 selected cell 的起点为 `B=b_lo`，长度为 `L`，并写 `q_start=P-2B`。完整覆盖词是：

```text
for t=0..L-1, choose odd prime ell_t <= sqrt(P)
q_start - 2t ≡ 0 (mod ell_t)
equivalently q_start ≡ 2t (mod ell_t)
```

同一标签复用时必须满足 `ell | (t_i-t_j)`；在 `L<=5` 内只有 `ell=3` 可隔 3 复用一次。

## 2. 前沿词

| P | side | b cell | q cell | missing labels >= | min full modulus | partial labels |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 733 | `plus` | `23-26` | `681-687` | `1` | `105` | `[3, 5]` |
| 523 | `plus` | `12-15` | `493-499` | `1` | `105` | `[3, 7, 17]` |
| 691 | `minus` | `19-21` | `649-653` | `1` | `105` | `[3, 11]` |
| 683 | `plus` | `14-17` | `649-655` | `1` | `105` | `[3, 5, 11]` |
| 733 | `plus` | `14-18` | `697-705` | `1` | `1155` | `[3, 17, 19]` |
| 673 | `minus` | `25-27` | `619-623` | `1` | `105` | `[3, 7]` |
| 733 | `plus` | `23-26` | `681-687` | `1` | `105` | `[3, 5]` |
| 313 | `plus` | `15-16` | `281-283` | `2` | `15` | `[]` |
| 1129 | `plus` | `29-32` | `1065-1071` | `1` | `105` | `[3, 11]` |
| 691 | `minus` | `19-21` | `649-653` | `1` | `105` | `[3, 11]` |
| 673 | `minus` | `25-27` | `619-623` | `1` | `105` | `[3, 7]` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `same_label_reuse_rule` | `closed` | A repeated odd label ell in a consecutive b-cell is possible only across b-distance divisible by ell. |
| `short_cell_min_distinct_label_bound` | `closed` | For cell length L<=5, a complete cover word needs at least L labels for L<=3 and L-1 labels for L>=4. |
| `complete_cover_word_crt_progression` | `closed` | Every complete label word defines a compatible CRT progression for q_start=P-2B. |
| `finite_partial_words_not_complete` | `finite_evidence` | The finite frontier only has partial cover words; every selected cell has missing labels/uncovered q-values. |
| `global_compatible_word_exclusion` | `open` | A global proof still needs to exclude compatible CRT cover words inside the fixed small-k phase cell. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CRTCoverWordNormalFormClosed` | `true` | `true` | 完整小因子覆盖已提升为 `q_start=P-2B` 的 CRT 覆盖词。 | closed |
| `ShortCellLabelMultiplicityBoundClosed` | `true` | `true` | 长度至多 5 的覆盖词有明确的最少不同标签数和模数下界。 | closed |
| `FiniteNoCompleteWord` | `true` | `false` | 有限前沿只有 partial word，没有完整覆盖词；仍只是有限证据。 | finite evidence only |
| `GlobalCompatibleWordExcluded` | `false` | `false` | CRT 兼容本身不矛盾，仍需接固定 small-k 相位与列相位排斥。 | CompatibleCRTCoverWordPDECExclusionOrColumnPhaseLift |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 CRT 覆盖词正规形，不关闭全局命题。 | CompatibleCRTCoverWordPDECExclusionOrColumnPhaseLift |

## 5. 下一步

- 主攻：`CompatibleCRTCoverWordPDECExclusionOrColumnPhaseLift`。
- 需要证明兼容 CRT 覆盖词不能同时落入固定 small-k atom phase，或把它提升为 ColumnCRT/PDEC 证书。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_crt_cover_word_router.py` | `b1b979d3f114422ed43c68277ffed63431a65fa81d83943d39f9ca0ed571938d` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_short_b_cell_factor_cover_router.py` | `aad8309144697dc6edffb53438c817b09e31f0c57717303564464afb416df073` |
| `data/square-phase-offband-prefix-gap-shadow-short-b-cell-factor-cover-ledger.json` | `582dd7af864d3af9a0448caac174bdb014afd638bbe5f5d16042f47b080dc15f` |
| `data/square-phase-offband-prefix-gap-shadow-crt-cover-word-ledger.json` | `a8d3b86e09fde5f3e5ea2a7b960299762daf0707cb2374d0db37ee5e84e54839` |
