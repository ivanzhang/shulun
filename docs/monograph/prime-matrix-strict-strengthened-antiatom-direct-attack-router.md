# Prime Matrix strict actual-source 强化反原子直攻证书

**状态：** `strict_strengthened_antiatom_direct_attack_reduced_to_new_actual_source_axiom_or_external_spectral_input_open`

本轮直接攻 FullSNonAPStrengthenedSourceAntiAtomForActualSource。合同本身已钉住；generic WFD/Type/Fourier 版被 moving-delta 模型反证，不能继续当作自足引理。若把命题严格限为 actual-source，当前材料尚无正向源构造、source identity 或 exact entropy 证明来推出该反原子；因此 strict 自足线只能新增并证明 AddStrengthenedActualSourceAntiAtomTheorem，或条件接受 ExternalDIBFIKuznetsovDispersionTheoremMatch。行/列命题没有无条件闭合。

```text
strict_strengthened_antiatom_direct_attack_boundary_closed=true
generic_self_contained_antiatom_refuted=true
formal_wfd_type_fourier_shortcuts_blocked=true
moving_delta_countermodel_imported=true
strengthened_actual_source_antiatom_proved=false
new_actual_source_axiom_required=true
external_spectral_input_only_conditional=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 直攻判定

```text
generic formal anti-atom version: refuted by moving-delta;
actual-source strengthened version: open as a new actual-source theorem;
external spectral version: acceptable only as conditional input;
row/column unconditional theorem: not closed.
```

## 2. actual-source 定理必要字段

| field | meaning |
| --- | --- |
| `exact_actual_source_binding` | 证明 M_{u,v} 是实际 RIW/Buchstab、Type/Fourier、dispersion 产生的源容量，而不是任意形式 WFD 模板容量。 |
| `scale_uniform_moving_uv_antiatom` | 对随尺度移动的同一 `(u,v)` 标签给出 `max M_{u,v}/sum M_{u,v} <= log^{-2A}`。 |
| `nonrecursive_source_constructor` | 在 Cauchy、pair-energy、joint constructor 与 terminal extraction 之前给出正向源构造或等价恒等式。 |
| `no_generic_template_substitution` | 不得用 formal WFD、Type-I/II、Fourier smoothing、K4/K6、naive incidence 代替 actual-source 定理。 |
| `no_exactuv_pair_joint_loop` | 不得通过 ExactUV/pair-energy/joint 回环证明该反原子，否则回到已记录宏循环。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrengthenedAntiAtomContractPinned` | `true` | `true` | 最终 source 反原子合同已精确钉住为实际容量测度的 moving same-(u,v) log-power 反界。 | none at statement-boundary level |
| `HardpointActiveInStrictBasis` | `true` | `true` | 上一轮外环桥后，strict 活动基确实包含 actual-source 强化反原子硬点。 | FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| `MovingDeltaCountermodelImported` | `true` | `true` | moving-delta 模型通过形式模板但使 `max M/sum M=1`，反证 generic 形式反原子。 | 不能证明 generic WFD 版。 |
| `GenericSelfContainedAntiAtomRefuted` | `true` | `true` | unrestricted generic WFD/Type/Fourier 反原子不是未证，而是在当前形式假设下为假。 | 必须改为 actual-source 定理或外部谱输入。 |
| `FormalShortcutFirewallClosed` | `true` | `true` | formal WFD、固定投影、K4/K6、naive incidence、Fourier smoothing 均不能推出 moving `(u,v)` 反原子。 | FullSNonAPStrengthenedSourceAntiAtomForActualSource |
| `ActualSourceSpecificTheoremMissing` | `true` | `false` | 当前语料没有证明实际 noncanonical full-S 源满足该强化反原子；只能把它作为新增 actual-source 定理。 | AddStrengthenedActualSourceAntiAtomTheorem |
| `SourceIdentityParallelExitStillOpen` | `true` | `false` | 另一条自足出口是证明实际源等于 canonical RIW/Buchstab 源；当前只在 canonical 分支 scoped 闭合。 | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab |
| `MovingAtomExactEntropyStillOpen` | `true` | `false` | moving atom normal form 仍把问题压到 exact actual-source entropy，而不是给出熵定理本身。 | ExactWFDSourceEntropy / strengthened actual-source anti-atom |
| `ExternalSpectralInputOnlyConditional` | `true` | `false` | DI/BFI/Kuznetsov 或 completed full-S KLS 可以作为外部输入线，但不能冒充 strict 自足证明。 | ExternalDIBFIKuznetsovDispersionTheoremMatch OR ModulusDependentCompletedFullSKLSInput |
| `StrengthenedActualSourceAntiAtomProved` | `false` | `false` | 本轮直攻未从现有材料推出 actual-source 强化反原子。 | AddStrengthenedActualSourceAntiAtomTheorem OR ExternalDIBFIKuznetsovDispersionTheoremMatch |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 行/列命题仍需 source 破环输入、ExactUV、RatePreservation 与 DStructure/Rankin 全部闭合。 | (NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 当前严格活动基

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件关闭的是 strengthened anti-atom 直攻路线的边界分类；它没有证明 actual-source 强化反原子、ExactUV、RatePreservation 或 DStructure/Rankin。
