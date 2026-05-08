# Prime Matrix Noncanonical 最终压窄路由器

**状态：** `noncanonical_final_narrowed_to_exact_source_entropy_or_full_s_kls_input`

Noncanonical 补集已从三歧继续压成两项真实输入：内部新增 exact source entropy/强化反原子，或外部/新证 FullSNonAPWFDKLSTheoremInput。APSourceLift 与 generic 反原子路线不再可用；当前材料仍未闭合 self-contained noncanonical 包。

## 1. 压窄律

noncanonical full-S 补集的可行路线继续压窄：APSourceLift 被拒绝，generic 自足反原子被 moving-delta 反证，canonical 分支已经移出。当前只剩两个真实输入：证明 exact/actual source entropy 或强化实际源反原子；或者接受/证明 FullSNonAPWFDKLSTheoremInput。

```text
noncanonical_narrowing_boundary_closed=true
ap_source_lift_rejected=true
generic_self_contained_antiatom_refuted=true
exact_source_entropy_closed=false
external_full_s_contract_closed_if_accepted=true
self_contained_noncanonical_closed=false
row_column_unconditional_closed=false
```

## 2. 审查表

| gate | closed | verdict | evidence | consequence | remaining |
| --- | --- | --- | --- | --- | --- |
| `CanonicalBranchRemoved` | `true` | `closed_for_canonical_only` | actual-source global reconciliation | canonical RIW/Buchstab 分支已闭合，不能再当作 noncanonical 缺口。 | noncanonical complement only |
| `APSourceLiftRejected` | `true` | `route_rejected` | AP-source lift no-go router | non-AP generic WFD 补集不能无损回提为 BFI prime-AP discrepancy。 | NewFullSTheoremInput or strengthened source theorem |
| `GenericSelfContainedAntiAtomRefuted` | `true` | `generic_statement_false` | moving-delta anti-atom no-go router | 形式 WFD/Type/Fourier 假设下的 generic 反原子命题为假。 | strengthen actual source, restrict source, or accept external theorem |
| `SourceAntiAtomReductionPinned` | `true` | `reduced_open` | full-S source anti-atom router | 支撑+容量兼容已等价压成最终 source capacity measure 无 moving atom。 | prove strengthened source anti-atom or external dispersion match |
| `ExactWFDSourceEntropyNotForced` | `true` | `sufficient_but_unproved` | source block entropy router | ExactWFDSourceEntropy 一旦成立可推出 NC-BLK，但不由当前形式输入强制。 | prove exact entropy for actual coefficients |
| `FullSNonAPWFDKLSInputPinned` | `true` | `single_external_or_new_deep_theorem_atom` | new full-S theorem input router | 外部/新深定理路线已压成一个未中心化、无投影、full-S non-AP WFD KLS 输入。 | prove or accept FullSNonAPWFDKLSTheoremInput |
| `ExternalContractReadyIfAccepted` | `true` | `conditional_external_closed` | FullS-KLS-ext specialization router | 接受 FullS-KLS-ext 时对象/尺度/无投影兼容已经写入合同。 | explicit external acceptance or new proof |
| `TrilemmaBoundaryStillHonest` | `true` | `boundary_closed_not_theorem` | noncanonical complement trilemma router | 三歧边界闭合，但自足 noncanonical 补集没有由当前材料证明。 | two real choices remain |

## 3. 剩余真实选择

- `InternalNewTheorem: prove ExactWFDSourceEntropy / FullSNonAPStrengthenedSourceAntiAtom for the actual source`
- `ExternalDeepInput: accept or prove FullSNonAPWFDKLSTheoremInput`

## 4. 判定

noncanonical 最窄点已经不是 APSourceLift，也不是 generic WFD 反原子。当前内部路线必须证明 actual/exact source entropy；外部路线必须接受或证明 full-S non-AP WFD KLS 输入。
