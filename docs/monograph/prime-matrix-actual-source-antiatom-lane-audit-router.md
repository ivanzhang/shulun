# Prime Matrix actual-source 反原子 lane 审计路由器

**状态：** `actual_source_antiatom_lane_requires_new_axiom_or_spectral_input`

actual-source 反原子 lane 已被进一步压窄：canonical source 分支已经闭合；generic self-contained 反原子为假；因此若不新增强化实际源反原子定理/公理，当前数学硬攻应转向 c-dependent 完成型谱抵消。

```text
actual_source_antiatom_lane_boundary_closed=true
actual_source_antiatom_proved=false
generic_self_contained_antiatom_refuted=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
ActualFullSNonAPSourceCapacityAntiAtomForActualSource => canonical branch already closed; generic branch refuted; global route needs AddStrengthenedActualSourceAntiAtomTheorem or CDependentResidueWeightSpectralCancellationInput.
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ActualSourceAntiAtomLaneActive | `true` | `false` | noncanonical 二选一路由把自足优先点设为 actual-source 反原子。 | ActualFullSNonAPSourceCapacityAntiAtomForActualSource |
| CanonicalActualSourceBranchClosed | `true` | `true` | canonical RIW/Buchstab source 分支的 actual-source provenance 与 bridge 已闭合。 | 不覆盖 noncanonical/generic 补集。 |
| GlobalUnrestrictedStillOpen | `true` | `false` | actual-source bridge 明确不关闭 global unrestricted/noncanonical 补集。 | noncanonical complement remains. |
| GenericSelfContainedAntiAtomRefuted | `true` | `true` | generic full-S 自足反原子被 moving-delta capacity model 反证。 | 不能由 formal WFD/Type/Fourier/K4K6 推出。 |
| StrengthenedSourceContractPinned | `true` | `true` | 剩余 source lane 已精确成为最终容量测度的无 moving same-(u,v) atom 定理。 | AddStrengthenedActualSourceAntiAtomTheorem |
| NoExistingProofOfActualSourceAntiAtom | `true` | `false` | 现有材料只能给 canonical 分支闭合和 generic 反例；不能推出 global actual-source 反原子。 | AddStrengthenedActualSourceAntiAtomTheorem OR CDependentResidueWeightSpectralCancellationInput |

## 3. 下一步

若坚持完全自足，需要新增并证明 `AddStrengthenedActualSourceAntiAtomTheorem`。
若不新增源公理，当前数学最窄点转为 `CDependentResidueWeightSpectralCancellationInput`。
