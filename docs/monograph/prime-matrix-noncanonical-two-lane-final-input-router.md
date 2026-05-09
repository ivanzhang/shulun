# Prime Matrix noncanonical 二选一最终输入路由器

**状态：** `noncanonical_two_lane_pinned_source_or_spectral_open`

NoncanonicalTwoLaneMathInput 已拆成两条互斥可审稿 lane：自足路线必须证明实际源反原子或实际源恒等；外部路线必须证明/接受 c-dependent 完成型谱抵消。当前两条 lane 都未证明，所以行列无条件定理仍未闭合。

```text
noncanonical_two_lane_boundary_closed=true
noncanonical_two_lane_proved_or_accepted=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
NoncanonicalTwoLaneMathInput => (ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR CDependentResidueWeightSpectralCancellationInput); final theorem still requires DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.
```

## 2. Lane 表

| lane | active | boundary_closed | proved_or_accepted | role | required_input |
| --- | --- | --- | --- | --- | --- |
| ActiveNoncanonicalGateImported | `true` | `true` | `true` | 最终数学输入已缩为 noncanonical 二选一。 | ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR CDependentResidueWeightSpectralCancellationInput |
| ActualFullSNonAPSourceCapacityAntiAtomForActualSource | `true` | `true` | `false` | 自足 lane：证明实际源没有 moving same-(u,v) 原子，或进一步证明实际源等于 canonical RIW/Buchstab。 | For the final full-S non-AP WFD source capacity measure M_{u,v}, prove max_{u,v} M_{u,v}/sum_{u,v}M_{u,v} <= log^{-2A} for every A. |
| CDependentResidueWeightSpectralCancellationInput | `true` | `true` | `false` | 外部/新深定理 lane：对 c-dependent、未中心化、无投影 residue 权重取得谱平均抵消。 | handles c-dependent residue weights B_{c,x}; uses well-factorable lambda_c and smooth omega_h over c,h; goes beyond pointwise Weil and ordinary large sieve; keeps the uncentered no-projection non-AP WFD target; delivers NaturalWFDScale/log^A P for every A>0 |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `true` | `true` | `false` | 并行晋级验收 lane：即使 noncanonical 数学输入闭合，也仍需独立接受。 | independent promotion acceptance |

## 3. 下一步

优先自足硬攻：`ActualFullSNonAPSourceCapacityAntiAtomForActualSource`。
外部/新深定理备选：`CDependentResidueWeightSpectralCancellationInput`。
并行晋级验收：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
