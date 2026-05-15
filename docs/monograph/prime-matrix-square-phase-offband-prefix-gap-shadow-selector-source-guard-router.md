# Prime Matrix square-phase off-band prefix gap shadow selector source guard router

**状态：** `selector_full_shape_source_decomposed_to_pressure_or_ordered_shape_guard_open_global`

本步把 full-shape selector 来源拆成两个可攻原子：`W_required>0` 等价于 `2T-H>=0` 的见证压力门；通过后还必须匹配 ordered prefix shape。当前 15 个 matching 代表中，14 个已在见证压力门失败，1 个在 ordered prefix shape 门失败，因此没有 full-shape overlap PDEC 实例。全局剩余是把这两个门控失败提升为 formal-unit 族的符号排斥。

```text
record_count=15
required_formula_failure_count=0
witness_pressure_gate_failure_count=14
ordered_prefix_shape_gate_failure_count=1
full_shape_overlap_count=0
signed_tail_deficit_range=-20..0
row_column_unconditional_closed=false
```

## 1. Guard Records

| replay P | side | H | T | 2T-H | W formula | target atoms | replay atoms | failure gate |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| 647 | `minus` | 50 | 20 | -10 | 0 | `['both_offband_middle:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'plus_only_noslot:k1', 'plus_only_noslot:k2']` | `WitnessPressureGate` |
| 677 | `minus` | 45 | 22 | -1 | 0 | `['both_offband_middle:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'both_offband_middle:k0', 'plus_only_noslot:k1']` | `WitnessPressureGate` |
| 727 | `minus` | 54 | 22 | -10 | 0 | `['both_offband_middle:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'both_offband_middle:k0', 'plus_only_noslot:k1']` | `WitnessPressureGate` |
| 757 | `minus` | 66 | 23 | -20 | 0 | `['both_offband_middle:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'plus_only_noslot:k1', 'both_offband_middle:k1']` | `WitnessPressureGate` |
| 727 | `plus` | 54 | 22 | -10 | 0 | `['both_offband_middle:k0', 'minus_only_noslot:k0', 'both_offband_middle:k1']` | `['both_offband_middle:k0', 'minus_only_noslot:k0', 'minus_only_noslot:k1']` | `WitnessPressureGate` |
| 757 | `plus` | 52 | 23 | -6 | 0 | `['both_offband_middle:k0', 'minus_only_noslot:k0', 'both_offband_middle:k1']` | `['minus_only_noslot:k0', 'both_offband_middle:k1', 'minus_only_noslot:k1']` | `WitnessPressureGate` |
| 727 | `plus` | 54 | 22 | -10 | 0 | `['both_offband_middle:k0', 'minus_only_noslot:k0', 'both_offband_middle:k1']` | `['both_offband_middle:k0', 'minus_only_noslot:k0', 'minus_only_noslot:k1']` | `WitnessPressureGate` |
| 757 | `plus` | 52 | 23 | -6 | 0 | `['both_offband_middle:k0', 'minus_only_noslot:k0', 'both_offband_middle:k1']` | `['minus_only_noslot:k0', 'both_offband_middle:k1', 'minus_only_noslot:k1']` | `WitnessPressureGate` |
| 293 | `plus` | 20 | 10 | 0 | 1 | `['minus_only_noslot:k0', 'minus_only_noslot:k1', 'minus_only_noslot:k2']` | `['minus_only_noslot:k0', 'both_offband_middle:k1', 'minus_only_noslot:k1']` | `OrderedPrefixShapeGate` |
| 311 | `plus` | 31 | 10 | -11 | 0 | `['minus_only_noslot:k0', 'minus_only_noslot:k1', 'minus_only_noslot:k2']` | `['minus_only_noslot:k0', 'minus_only_noslot:k1', 'minus_only_noslot:k2']` | `WitnessPressureGate` |
| 317 | `plus` | 27 | 11 | -5 | 0 | `['minus_only_noslot:k0', 'minus_only_noslot:k1', 'minus_only_noslot:k2']` | `['minus_only_noslot:k0', 'minus_only_noslot:k1', 'minus_only_noslot:k2']` | `WitnessPressureGate` |
| 647 | `minus` | 50 | 20 | -10 | 0 | `['plus_only_noslot:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'plus_only_noslot:k1', 'plus_only_noslot:k2']` | `WitnessPressureGate` |
| 677 | `minus` | 45 | 22 | -1 | 0 | `['plus_only_noslot:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'both_offband_middle:k0', 'plus_only_noslot:k1']` | `WitnessPressureGate` |
| 727 | `minus` | 54 | 22 | -10 | 0 | `['plus_only_noslot:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'both_offband_middle:k0', 'plus_only_noslot:k1']` | `WitnessPressureGate` |
| 757 | `minus` | 66 | 23 | -20 | 0 | `['plus_only_noslot:k0', 'plus_only_noslot:k1']` | `['plus_only_noslot:k0', 'plus_only_noslot:k1', 'both_offband_middle:k1']` | `WitnessPressureGate` |

## 2. 命题行

| name | status | statement |
| --- | --- | --- |
| `witness_pressure_formula` | `closed` | The replay gate satisfies W_required=max(0,floor((2T-H)/2)+1), so W_required>0 iff 2T-H>=0. |
| `current_matching_representatives_guard_decomposition` | `closed_on_current_frontier` | Every current matching representative fails either the witness pressure gate or the ordered prefix shape gate. |
| `symbolic_pressure_and_shape_exclusion` | `open` | A global proof must show template residues force one of these two gates to fail in the formal-unit family, or route overlaps to PDEC. |

## 3. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `WitnessPressureFormulaClosed` | `true` | `true` | `W_required` 已由 `2T-H` 精确控制。 | closed |
| `CurrentRepresentativesFailSourceGuards` | `true` | `true` | 当前 matching 代表全部死于见证压力门或 ordered shape 门。 | closed on current finite frontier |
| `GlobalTemplateResidueGuardExclusionProved` | `false` | `false` | 仍需证明模板 residue 在 formal-unit 族中必触发同样门控失败。 | SymbolicWitnessPressureAndOrderedPrefixShapeExclusionForTemplateResidues |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把来源定理拆成两个原子门，不关闭全局行/列命题。 | SymbolicWitnessPressureAndOrderedPrefixShapeExclusionForTemplateResidues |

## 4. 下一步

- 主攻：`SymbolicWitnessPressureAndOrderedPrefixShapeExclusionForTemplateResidues`。
- 先证明 small-modulus template residue 若匹配局部父 atom，则在 formal-unit selector 中必有 `2T-H<0`；
- 剩余正阈值例外再证明 ordered prefix shape 必改变，或登记 full-shape overlap PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_source_guard_router.py` | `5383c437edb961ee7bfaf1fca30900ff45821eff1844dc568d3f5fae209b56a1` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_full_shape_provenance_router.py` | `8c10be38d91e42a7ccc507a57cab829d1709b0e68afc4f03aa88c98f1ef063c9` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `data/square-phase-offband-prefix-gap-shadow-selector-full-shape-provenance-ledger.json` | `9c108614b8a2df80ae8819e9a9928e5b1d06ec3db40528313d6d42f12e1de68a` |
| `data/square-phase-offband-prefix-gap-shadow-selector-source-guard-ledger.json` | `c9fd1423390a995a82e7c56960c8263e38f3c1679d688265ace182844a9482e5` |
