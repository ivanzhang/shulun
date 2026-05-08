# Prime Matrix Noncanonical 补集三歧边界路由器

**状态：** `noncanonical_complement_trilemma_boundary_closed_inputs_still_conditional`

第二包三歧边界已闭合：扣除 canonical 分支后，generic 自足反原子被 moving-delta 反例排除；外部路线压成 `FullS-KLS-ext`/`FullSNonAPWFDKLSTheoremInput`；自足路线只能新增实际源恒等或强化实际源反原子。当前材料仍未自足证明 noncanonical 补集本身。

## 1. 三歧律

扣除 canonical RIW/Buchstab 分支后，noncanonical full-S 补集只有三种合法闭合模式。generic 自足 WFD 反原子路线已被 moving-delta capacity model 反证，所以不能由 formal WFD、Type/Fourier、K4/K6 或朴素 incidence 修复。必须证明实际源恒等、证明强化实际源反原子，或接受/证明直接作用于当前未中心化无投影 non-AP WFD 对象的精确 FullS-KLS-ext 定理。

```text
trilemma_boundary_closed=true
self_contained_noncanonical_package_closed=false
external_contract_package_closed_if_fulls_kls_ext_accepted=true
row_column_unconditional_closed=false
```

## 2. 审查表

| gate | closed | verdict | evidence | consequence | remaining |
| --- | --- | --- | --- | --- | --- |
| `CanonicalBranchSubtracted` | `true` | `closed_for_canonical_branch` | actual-source bridge + canonical-source final theorem | canonical RIW/Buchstab 分支已移出 noncanonical 补集。 | none inside canonical branch |
| `NoncanonicalContractPinned` | `true` | `contract_closed` | noncanonical complement input contract | 第二包不是 generic WFD 自足引理，而是实际源/强化反原子/外部定理三歧。 | choose one legal closure mode |
| `SourceAntiAtomReduction` | `true` | `reduced_not_proved` | full-S source anti-atom router | 支撑与容量兼容已等价压成最终 source capacity measure 的强化反原子。 | prove strengthened source anti-atom or take external route |
| `GenericSelfContainedAntiAtomNoGo` | `true` | `refuted` | self-contained anti-atom no-go router | 当前 generic full-S 自足反原子在 moving-delta 模型下为假。 | must strengthen source, restrict to canonical, or accept external FullS-KLS-ext |
| `FullSNonAPWFDKLSInputPinned` | `true` | `single_external_atom` | new full-S theorem input router | 外部/新深定理路线已压成一个 full-S non-AP WFD KLS 定理输入。 | prove or cite exact FullS-KLS-ext |
| `ExternalContractClosedIfAccepted` | `true` | `conditional_external_closed` | FullS-KLS-ext specialization router | 接受 FullS-KLS-ext 时，scale/object/no-projection 合同已经闭合。 | primary-source derivation or explicit external acceptance |

## 3. 合法闭合模式

- 实际源恒等：证明 actual full-S non-AP source 等于 canonical RIW/Buchstab
- 强化实际源反原子：证明最终 source capacity measure 没有 moving same-(u,v) atom
- 外部/新深定理：接受或证明 FullS-KLS-ext / FullSNonAPWFDKLSTheoremInput

## 4. 仍需输入

- `ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource`
- `DIBFIPrimarySourceSpecializationProof OR explicit acceptance of FullS-KLS-ext as external theorem`
- `DStructureTailLog4FiniteRankinIndependentAcceptance for final theorem promotion`

## 5. 判定

这一步闭合的是第二包的“边界形状”，不是把第二包无条件证明完。完全自足 generic full-S 反原子路线已经被反例排除；若不接受外部 `FullS-KLS-ext`，就必须新增并证明实际源恒等或强化实际源反原子。即便第二包用外部定理版闭合，完整行/列定理仍需第三包 `DStructure/Rankin` 晋级输入。
