# Prime Matrix 内外两线共同核心调和路由器

**状态：** `dual_lane_common_core_reconciled_external_or_new_source_antiatom_open`

两条线在自足版本中已经汇合：外部 c-dependent 谱抵消若不作为外部定理接受，会通过 BWFD/BSC/KFLS 回到 actual same-(u,v) 非集中，也就是内部强化源反原子核心。因此当前没有两个独立自足硬点；真正二选一是接受外部 FullS-KLS/c-dependent 谱定理，或证明实际源恒等/新 full-S 源反原子。DStructure/Rankin 晋级仍独立开放。

```text
common_core_reconciliation_closed=true
self_contained_common_core_proved=false
external_contract_accepted_as_final_input=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 调和判定表

| gate | closed | meaning | consequence |
| --- | --- | --- | --- |
| `DualLaneTerminalPinned` | `true` | 上一层已把外部线压成 c-dependent residue 谱抵消，内部线压成强化源反原子。 | 可以检查这两个终端是否独立。 |
| `CDependentResidueReturnsToNCBLK` | `true` | c-dependent residue 谱输入经有限 Fourier 接入 BWFD/BSC/KFLS 链。 | 自足证明时它不是新普通大筛原子，而是回到 actual same-(u,v) 非集中或外部定理。 |
| `NCBLKAlignsToExactSourceEntropy` | `true` | NC-BLK 自足路线必须证明 exact full-S non-AP source entropy，不能偷用 canonical 分支。 | 该目标与内部强化源反原子是同一 moving-block 核心的两种表述。 |
| `ExternalContractSeparatedFromSelfContainedCore` | `true` | 接受 FullS-KLS-ext 外部合同时外部版闭合；自足/主来源逐项版仍剩新源反原子输入。 | 外部定理可作为黑箱输入，但不能冒充自足证明。 |
| `SelfContainedTaxonomyCommonCorePinned` | `true` | 完全自足路线只剩实际源恒等或实际源强化反原子。 | unrestricted generic WFD 自足版已被 moving-delta 反证。 |
| `DStructurePromotionStillSeparate` | `true` | DStructure/Tail-log4/finite Rankin 仍是独立晋级门。 | 数学输入闭合后仍需独立验收才能升级为完整行/列无条件定理。 |

## 2. 上一层输入基

```text
(FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 调和后输入基

```text
((ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput) OR AcceptedFullSKLSExtOrCDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 完全自足版输入基

```text
ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 核心律

CDependentResidueWeightSpectralCancellationInput 若被接受，就是外部定理输入。若试图从当前材料内部证明它，有限 Fourier completion 会把它降回 BWFD/BSC/KFLS，再降回 actual same-(u,v) block non-concentration。这与内部线的 source-antiatom / moving-block 共同核心是同一个数学义务。

## 6. 当前结论

若不接受外部 FullS-KLS/c-dependent 谱定理，当前最窄自足目标就是证明实际源恒等或新 full-S 源反原子。
这一步没有证明该新源定理，也没有完成 DStructure/Rankin 独立验收。
