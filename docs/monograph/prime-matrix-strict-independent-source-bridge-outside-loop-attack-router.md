# Prime Matrix strict 独立 actual-source 桥外环直攻证书

**状态：** `independent_source_bridge_outside_loop_reduced_to_source_identity_or_strengthened_antiatom_open`

本轮直接攻 IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop。canonical 分支已闭合但只是 scoped case；generic WFD 自足模板已被 moving-delta 反证；ExactUV/pair-energy/joint 下钻又会回到宏循环。因此严格自足外环桥只能是 ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab 或 FullSNonAPStrengthenedSourceAntiAtomForActualSource。当前二者均未证明；外部 completed KLS 只能作为条件线。

```text
macrocycle_imported=true
canonical_branch_only_scoped=true
generic_wfd_template_refuted=true
source_identity_proved=false
strengthened_actual_source_antiatom_proved=false
independent_actual_source_bridge_outside_pair_energy_loop_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
external_completed_kls_accepted_as_strict_proof=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
rate_preservation_ledger_proved=false
dstructure_independent_gate_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 外环桥拆分

| from | to |
| --- | --- |
| IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab | actual full-S non-AP source equals canonical RIW/Buchstab decision-tree source before dispersion |
| FullSNonAPStrengthenedSourceAntiAtomForActualSource | actual noncanonical final capacity measure has no moving same-(u,v) atom |
| conditional external lane | ModulusDependentCompletedFullSKLSInput |

## 2. 必要字段

| field | meaning |
| --- | --- |
| `actual_source_identity` | 在 Cauchy/dispersion/payment 前证明实际 full-S non-AP 源就是 canonical RIW/Buchstab 决策树源。 |
| `strengthened_actual_antiatom` | 直接证明实际 noncanonical final capacity measure 满足 moving same-(u,v) 大原子反界。 |
| `no_generic_wfd_substitution` | 不得用已被 moving-delta 反证的 generic WFD/Type/Fourier/K4K6 模板替代 actual-source 定理。 |
| `no_exactuv_pair_energy_loop` | 不得把 ExactUV/pair-energy/joint constructor 回环作为 independent bridge 的证明。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MacrocycleImported` | `true` | `true` | 上一轮已证明 TERMINAL->SOURCE->PAIR->JOINT->TERMINAL 是宏循环；独立桥必须避开该回环。 | IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop |
| `CanonicalBranchOnlyScoped` | `true` | `true` | canonical RIW/Buchstab 分支已经闭合为 scoped case，但不能自动覆盖 unrestricted noncanonical 补集。 | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab |
| `SourceIdentityOptionStillOpen` | `true` | `false` | 若要用 source identity 破环，必须证明实际 full-S non-AP 源等于 canonical 决策树源；当前没有该证明。 | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab |
| `GenericWFDSelfContainedTemplateRefuted` | `true` | `true` | unrestricted generic WFD/Type/Fourier 自足模板已被 moving-delta 模型反证。 | 不能作为自足桥。 |
| `StrengthenedAntiAtomContractPinned` | `true` | `true` | noncanonical 补集的 actual-source 侧只剩实际源强化反原子，而不是形式筛法推论。 | FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| `EntropyShortcutFirewallImported` | `true` | `true` | fixed projection、formal WFD、K4/K6、早期零行几何和 pair-mass 等价命名都不能证明 actual entropy。 | FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| `NoExistingStrengthenedAntiAtomProof` | `true` | `false` | 当前材料没有实际 noncanonical full-S 源强化反原子的证明。 | FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| `ExternalCompletedKLSOnlyConditional` | `true` | `false` | completed/modulus-dependent full-S KLS 可作为条件外部线，但不能写成 strict 自足证明。 | ModulusDependentCompletedFullSKLSInput |
| `NewJointFormulaParallelStillOpen` | `true` | `false` | 新显式 joint alpha/delta 公式仍是并行破环输入；当前语料没有该工件。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `IndependentSourceBridgeOutsideLoopCurrentCorpusProved` | `false` | `false` | 外环桥已经压成 source identity 或 strengthened anti-atom；两者当前均未证明。 | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只压缩独立桥，不关闭 ExactUV、RatePreservation、DStructure/Rankin 和最终行/列命题。 | (NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 当前严格活动基

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件外部线：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource OR ModulusDependentCompletedFullSKLSInput) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只压缩外环 actual-source 桥；没有证明 source identity、强化反原子、ExactUV、RatePreservation 或 DStructure/Rankin。
