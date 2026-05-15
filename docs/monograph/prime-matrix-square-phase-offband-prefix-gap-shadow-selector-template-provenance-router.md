# Prime Matrix square-phase off-band prefix gap shadow selector template provenance router

**状态：** `selector_template_provenance_required_open`

本步审计 small-modulus 模板冲突能否由 phase+素性自动全球化。结果是否定的：5 个模板的 residue 在当前 phase 窗口中都有素数代表，匹配素数代表总数为 11。因此当前 actual P 避开模板 residue 是 formal-unit selector 来源问题，而不是局部 phase/primality 问题；下一步必须证明 actual selector 的 residue 来源，或对 matching template 提交 PDEC/ColumnCRT。

```text
candidate_count=7
template_count=5
template_with_matching_prime_count=5
total_matching_prime_representative_count=11
row_column_unconditional_closed=false
```

## 1. Template Provenance

| template | rho | actual | matching primes | selector provenance required |
| --- | ---: | ---: | --- | ---: |
| `band=minus_only_noslot\|k=0\|L=4\|labels=3,5,11\|g=15\|rho=7\|actual=8` | 7 | 8 | `[727, 757]` | `true` |
| `band=minus_only_noslot\|k=0\|L=4\|labels=3,5,7\|g=15\|rho=7\|actual=8` | 7 | 8 | `[727, 757]` | `true` |
| `band=minus_only_noslot\|k=1\|L=2\|labels=3,7\|g=3\|rho=2\|actual=1` | 2 | 1 | `[293, 311, 317]` | `true` |
| `band=plus_only_noslot\|k=1\|L=3\|labels=3,5,7\|g=15\|rho=2\|actual=1` | 2 | 1 | `[647, 677]` | `true` |
| `band=plus_only_noslot\|k=1\|L=3\|labels=3,5,7\|g=15\|rho=7\|actual=1` | 7 | 1 | `[727, 757]` | `true` |

## 2. 命题行

| name | status | statement |
| --- | --- | --- |
| `phase_primality_globalization_rejected` | `closed` | The small-modulus template conflict cannot be globalized using only the phase window and primality, because matching prime representatives exist. |
| `actual_selector_provenance_required` | `open` | A global proof must use the actual formal-unit selector to force actual P into the nonmatching residue class. |
| `template_overlap_pdec` | `open` | If the selector can land in the template residue, the matching template must be routed to PDEC/ColumnCRT. |

## 3. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PhasePrimalityAloneExcludesTemplates` | `false` | `false` | 模板 residue 在当前 phase 窗口中有素数代表，不能靠 phase+素性排除。 | rejected |
| `ActualSelectorProvenanceNeeded` | `true` | `true` | 必须证明 actual formal-unit selector 为什么避开这些 residue。 | ActualFormalUnitResidueSelectorProvenanceOrTemplateOverlapPDEC |
| `GlobalActualSelectorResidueProved` | `false` | `false` | 尚未证明 formal-unit selector 的 residue 来源定理。 | ActualFormalUnitResidueSelectorProvenanceOrTemplateOverlapPDEC |
| `TemplateOverlapPDECExcluded` | `false` | `false` | 若 selector 可命中模板 residue，仍需 PDEC/ColumnCRT 排斥。 | ActualFormalUnitResidueSelectorProvenanceOrTemplateOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭错误的 phase-primality 全球化路线，不关闭全局行/列命题。 | ActualFormalUnitResidueSelectorProvenanceOrTemplateOverlapPDEC |

## 4. 下一步

- 主攻：`ActualFormalUnitResidueSelectorProvenanceOrTemplateOverlapPDEC`。
- 直接证明目标：解释 actual formal-unit selector 的 residue 来源，证明它不能落入模板 rho。
- 若 selector 可落入 rho，则登记 matching template overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_template_provenance_router.py` | `3e29bf7e46148084bf4f1a8ef57acb8d8aa8aa9a3d6ce62c03ec43b7bfe4aa71` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_small_modulus_template_router.py` | `6e65429a972b2d9fd63bb7ef682b3357adff3ca7e7142826c6934a793adff474` |
| `data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-candidate-ledger.json` | `e3b34a34f5ca89d882cb98a8473f5820568ffbd60c1e48b1bbe56fd9418eb509` |
| `data/square-phase-offband-prefix-gap-shadow-selector-small-modulus-template-ledger.json` | `6d93ca61a5a6632b2a1c5e8c6488b41c9598906b6380a4e1528e240494de71a3` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
