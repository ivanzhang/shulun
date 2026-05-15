# Prime Matrix square-phase off-band prefix gap shadow selector small modulus template router

**状态：** `selector_small_modulus_templates_conflict_open_global`

本步把 7 个 small-modulus 候选归并为 5 个低轮 residue 模板；所有模板都满足 cover-word residue 与 actual P 在 gcd(M,15) 下不相等，因此当前前沿无需 PDEC。全局剩余是证明这些模板冲突在 formal-unit 族中稳定，或对 residue 匹配模板提交 PDEC/ColumnCRT。

```text
candidate_count=7
template_count=5
conflicting_template_count=5
pdec_template_count=0
row_column_unconditional_closed=false
```

## 1. Residue 模板

| template | instances | labels | gcd | rho | actual | moduli | P values | conflict |
| --- | ---: | --- | ---: | ---: | ---: | --- | --- | ---: |
| `band=minus_only_noslot\|k=0\|L=4\|labels=3,5,7\|g=15\|rho=7\|actual=8` | 1 | `[3, 5, 7]` | 15 | 7 | 8 | `[105]` | `[683]` | `true` |
| `band=minus_only_noslot\|k=0\|L=4\|labels=3,5,11\|g=15\|rho=7\|actual=8` | 1 | `[3, 5, 11]` | 15 | 7 | 8 | `[165]` | `[683]` | `true` |
| `band=minus_only_noslot\|k=1\|L=2\|labels=3,7\|g=3\|rho=2\|actual=1` | 1 | `[3, 7]` | 3 | 2 | 1 | `[21]` | `[313]` | `true` |
| `band=plus_only_noslot\|k=1\|L=3\|labels=3,5,7\|g=15\|rho=2\|actual=1` | 2 | `[3, 5, 7]` | 15 | 2 | 1 | `[105]` | `[691]` | `true` |
| `band=plus_only_noslot\|k=1\|L=3\|labels=3,5,7\|g=15\|rho=7\|actual=1` | 2 | `[3, 5, 7]` | 15 | 7 | 1 | `[105]` | `[691]` | `true` |

## 2. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_small_modulus_templates_registered` | `closed_on_current_frontier` | Current small-modulus candidates are reduced to finitely many lowwheel residue templates. |
| `finite_templates_all_conflicting` | `closed_on_current_frontier` | Every current small-modulus template has cover-word residue different from actual P modulo gcd(M,15). |
| `global_template_conflict` | `open` | A global proof must show the same residue-template conflict persists in the formal-unit family. |
| `template_overlap_pdec` | `open` | Any template with matching residues must be routed to PDEC/ColumnCRT. |

## 3. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteTemplateRegistrationClosed` | `true` | `true` | 当前 small-modulus 候选已归并为 residue 模板。 | closed on current finite frontier |
| `FiniteTemplatesAllConflict` | `true` | `true` | 当前模板全部低轮冲突，无需 PDEC。 | closed on current finite frontier |
| `GlobalTemplateConflictProved` | `false` | `false` | 尚未证明 formal-unit 族中同类模板必然冲突。 | SmallModulusLowwheelResidueTemplateGlobalizationOrOverlapPDEC |
| `TemplateOverlapPDECExcluded` | `false` | `false` | 若出现 residue 匹配模板，仍需 PDEC/ColumnCRT 排斥。 | SmallModulusLowwheelResidueTemplateGlobalizationOrOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭当前模板归并层，不关闭全局行/列命题。 | SmallModulusLowwheelResidueTemplateGlobalizationOrOverlapPDEC |

## 4. 下一步

- 主攻：`SmallModulusLowwheelResidueTemplateGlobalizationOrOverlapPDEC`。
- 直接证明目标：证明这些 residue 模板的冲突在 formal-unit 族中稳定。
- 若出现 `rho=actual` 的模板，则登记为 template overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_template_router.py` | `6e65429a972b2d9fd63bb7ef682b3357adff3ca7e7142826c6934a793adff474` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_candidate_router.py` | `ecc1f8375277523c8cff1010e9e2ad9b380fd79d953a312ec1980a4409198d25` |
| `data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json` | `e3b34a34f5ca89d882cb98a8473f5820568ffbd60c1e48b1bbe56fd9418eb509` |
| `data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-ledger.json` | `6d93ca61a5a6632b2a1c5e8c6488b41c9598906b6380a4e1528e240494de71a3` |
