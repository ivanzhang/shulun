# Prime Matrix square-phase off-band prefix gap shadow selector label lower bound router

**状态：** `selector_label_lower_bound_open_global`

本步审计 cover-word 标签模数下界：在 162 个相位兼容覆盖词中，排除结构低轮冲突后剩余 49 个 non-structural 词；当前没有任何 non-structural 词满足 M<=W，也没有 actual mod-15 残基命中窗口。最小行级余量 M-W 为 45。这关闭当前前沿的标签下界审计；全局仍需证明 formal-unit 族无小模数 non-structural 词，或将其登记为 PDEC/ColumnCRT。

```text
phase_compatible_cover_word_count=162
nonstructural_cover_word_count=49
small_modulus_nonstructural_count=0
actual_residue_overlap_count=0
min_nonstructural_margin_M_minus_W=45
row_column_unconditional_closed=false
```

## 1. 行级标签下界

| idx | P | W | compatible | nonstruct | min M | min labels | min M-W | small M count | overlap count |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| 0 | 733 | 8 | 4 | 3 | 561 | `[3, 11, 17, 3]` | 553 | 0 | 0 |
| 1 | 523 | 96 | 6 | 1 | 4389 | `[19, 11, 3, 7]` | 4293 | 0 | 0 |
| 2 | 691 | 117 | 35 | 11 | 231 | `[7, 3, 11]` | 114 | 0 | 0 |
| 3 | 683 | 172 | 31 | 1 | 7293 | `[11, 17, 3, 13]` | 7121 | 0 | 0 |
| 4 | 733 | 100 | 5 | 2 | 7293 | `[3, 11, 17, 3, 13]` | 7193 | 0 | 0 |
| 5 | 673 | 28 | 6 | 2 | 273 | `[7, 3, 13]` | 245 | 0 | 0 |
| 6 | 733 | 8 | 4 | 3 | 561 | `[3, 11, 17, 3]` | 553 | 0 | 0 |
| 7 | 313 | 32 | 10 | 4 | 77 | `[7, 11]` | 45 | 0 | 0 |
| 8 | 1129 | 72 | 20 | 9 | 231 | `[3, 7, 11, 3]` | 159 | 0 | 0 |
| 9 | 691 | 117 | 35 | 11 | 231 | `[7, 3, 11]` | 114 | 0 | 0 |
| 10 | 673 | 28 | 6 | 2 | 273 | `[7, 3, 13]` | 245 | 0 | 0 |

## 2. 长度类下界

| L | records | min M | max W | minM-maxW | small M count | overlap count | closed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 1 | 77 | 32 | 45 | 0 | 0 | `true` |
| 3 | 4 | 231 | 117 | 114 | 0 | 0 | `true` |
| 4 | 5 | 231 | 172 | 59 | 0 | 0 | `true` |
| 5 | 1 | 7293 | 100 | 7193 | 0 | 0 | `true` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_nonstructural_label_floor` | `closed_on_current_frontier` | Every current non-structural compatible cover word has modulus larger than its phase width. |
| `small_modulus_overlap_absent` | `closed_on_current_frontier` | No current non-structural cover word has M<=W or an actual mod-15 hit inside the phase window. |
| `global_label_floor` | `open` | A global proof must exclude non-structural cover words with small label modulus in the formal-unit family. |
| `small_modulus_overlap_pdec` | `open` | Any global small-modulus survivor must be routed to a PDEC/ColumnCRT certificate. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteLabelFloorClosed` | `true` | `true` | 当前 non-structural 覆盖词全部满足 M>W。 | closed on current finite frontier |
| `FiniteActualResidueOverlapAbsent` | `true` | `true` | 当前没有 actual mod-15 残基命中窗口。 | closed on current finite frontier |
| `GlobalLabelFloorProved` | `false` | `false` | 尚未证明 formal-unit 族中不存在小模数 non-structural 覆盖词。 | NonStructuralLabelModulusFloorOrSmallModulusOverlapPDEC |
| `SmallModulusOverlapPDECExcluded` | `false` | `false` | 若小模数词存在，仍需 PDEC/ColumnCRT 排斥。 | NonStructuralLabelModulusFloorOrSmallModulusOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭当前标签下界审计，不关闭全局行/列命题。 | NonStructuralLabelModulusFloorOrSmallModulusOverlapPDEC |

## 5. 下一步

- 主攻：`NonStructuralLabelModulusFloorOrSmallModulusOverlapPDEC`。
- 直接证明目标：全局排斥 small-modulus non-structural cover words。
- 若存在 small-modulus survivor，则登记为 small-modulus overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_label_lower_bound_router.py` | `985e10cf4ebcdd80951a956b2f82db1f1723fa2980f369ad0271d16733b64abb` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_phase_width_envelope_router.py` | `d22471303dad825b366acf9418178abfbff3257f5d385771331d1666f65589bb` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
| `data/square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-ledger.json` | `d2315a905edf1d24de2158140c650b774dfacccf77d11555d20e4d8d37fbd6af` |
| `data/square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-ledger.json` | `5ab54c5084e14c07df5a99ff57dea510f27ec0ff0a2088782da4a807bdb4985c` |
