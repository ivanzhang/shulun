# Prime Matrix clean-core new-layer 外部引理匹配路由器

**状态：** `newlayer_external_match_reduced_to_projection_morphism_and_flat_admission`

外部闭合引理是一台只吃“已准入平坦谱块”的机器；当前 new-layer 硬点还在把新增轮层 Fourier 低维集中转成 PDEC 证书、或把删除后的残余转成 flat-KLS 准入块。所以本轮没有宣称行/列命题闭合，而是把 new-layer 子口压成两个精确微输入。

```text
direct_external_lemma_closes_newlayer=false
self_contained_newlayer_closed=false
row_column_unconditional_closed=false
```

## 1. 结构律

External KLS/FullS lemmas close only a prepared flat spectral block. The current new-layer atom sits one level earlier: it must first prove that low-dimensional concentration on the added wheel fiber is an actual PDEC certificate, or that after deleting all such fibers the residual satisfies the clean flat-admission hypotheses. Therefore external closure can attach only after an exact new-layer projection/admission morphism, not directly at DLSNewLayerFourierConcentrationPDECReturn.

因此当前子口更新为：

```text
DLSNewLayerFourierConcentrationPDECReturn
  => ExactNewLayerFiberPDECProjectionMorphism
     AND NewLayerNoConcentrationImpliesFlatAdmission.
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CurrentNewLayerAtomPinned` | `true` | `false` | LowPhase 已把最贴近结构材料的子口命名为新增轮层 Fourier 集中/PDEC 回流。 | 核对外部闭合引理能否替代该子口。 |
| `ExternalFullSKLSContractClosedIfAccepted` | `true` | `false` | FullS-KLS-ext 外部合同版可闭合完成后的 non-AP WFD full-S 块。 | 这只是外部定理版，不是完全自足版。 |
| `CleanKLSAdmissionTemplateRegistered` | `true` | `false` | K1--K9 已说明失败项如何回流，全部通过时才可调用 KLS/DLS。 | new-layer 分支必须证明自己满足这些准入条件或返回 PDEC。 |
| `NewLayerEnergyIdentityAvailable` | `true` | `false` | 新增层能量已由继承频率和 r 不整除 h 的新频率精确拆分。 | 能量恒等式还不是低维集中推出 PDEC 的证明。 |
| `FourierInheritanceClampAvailable` | `true` | `false` | 强频率可判定为旧层继承或新增素因子层。 | 需证明新增层强频率的持久集中给出合法 new-layer PDEC 证书。 |
| `ExternalKLSPhaseTemplateAvailable` | `true` | `false` | 外部 KLS 模板能处理 CRT 后标准逆元相位。 | 需证明 new-layer 低模频率删除后可变成该模板的平坦输入。 |
| `PrimarySourceSelfContainedNoGoRetained` | `true` | `true` | 现有 DI/BFI 主来源不能直接给出本文所需 full-S non-AP KLS-ext。 | 自足版仍需内部证明，或另立新外部定理输入。 |
| `DirectExternalLemmaClosesNewLayer` | `false` | `false` | 外部闭合引理不能直接替代 DLSNewLayerFourierConcentrationPDECReturn。 | ExactNewLayerFiberPDECProjectionMorphism AND NewLayerNoConcentrationImpliesFlatAdmission。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是完整晋级的独立验收门。 | new-layer/flat DLS/signed 源锁完成后仍需独立验收。 |

## 3. 参数匹配表

| item | external closed lemma side | current new-layer side | match | closed by external | remaining | reason |
| --- | --- | --- | --- | --- | --- | --- |
| `proof_stage` | post_completion_flat_kloosterman_or_nonap_wfd_block | pre_flat_admission_unit_fiber_fourier_concentration | `stage_mismatch` | `false` | `ExactNewLayerFiberPDECProjectionMorphism` | 外部 KLS/FullS 引理从已完成、已给定系数、已通过 clean admission 的块开始；当前 new-layer 原子还要证明新增素因子 fiber 上的低维集中必给 PDEC。 |
| `frequency_support` | Kloosterman frequency h and inverse variable after CRT | new-layer additive frequencies r not dividing h on W=rW0 | `partial_after_projection` | `false` | `NewLayerFrequencyToKLSVariableMap` | KLS 模板能处理 CRT 后的逆元相位；但 r∤h 的新增层频率先要被证明能投影到同一 formal unit，否则它只是低模 fiber 偏斜而不是 KLS 输入。 |
| `coefficient_flatness` | open_at_kuznetsov_ls_atom_sc9 | unit-class conditioned residue weights before deleting PDEC spikes | `requires_deletion_ledger` | `false` | `NewLayerNoConcentrationImpliesFlatAdmission` | 外部引理只吸收 L2-flat/diffuse 系数；新增层如果有低维尖峰，必须先登记为 new-layer PDEC，删除后才能声称剩余满足 flat admission。 |
| `projection_and_centering` | FullS-KLS-ext absorbs uncentered non-projected non-AP WFD object | new-layer low-mod unit projection with BES danger thresholds | `not_the_same_no_projection_statement` | `false` | `NewLayerFormalUnitIdentity` | FullS 合同的 no-projection 是对 non-AP WFD 完成块说的；new-layer 仍需证明低模单位 fiber、BES 桶和 payment formal unit 是同一对象。 |
| `danger_thresholds` | mean-square or log-saving bound after admission | BES high-L1 and high-L2 simultaneous positive pressure | `requires_return_compatibility` | `false` | `BESDangerToPDECReturnOrFlatAdmission` | 外部谱平均不给出 BES 危险交集的命名回流；内部命题要求危险同步失败必须回到 PDEC/SAE/ColumnCRT/DLS。 |
| `primary_source_derivation` | NewFullSTheoremInputOrAPSourceLift | fully self-contained no-black-box route | `not_closed_self_contained` | `false` | `SC9OrInternalNewLayerFlatDLSProof` | 现有 DI/BFI 主来源不能直接推出 full-S non-AP KLS-ext；即使外部合同版可用，完全自足版仍需内部谱大筛或等价新层分散证明。 |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND ExactNewLayerFiberPDECProjectionMorphism AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND ExactNewLayerFiberPDECProjectionMorphism AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 当前结论

外部闭合引理与当前子口的参数比较给出一个硬边界：
只要还没有 `ExactNewLayerFiberPDECProjectionMorphism`，就不能把新增轮层低维集中直接送入外部 KLS；
只要还没有 `NewLayerNoConcentrationImpliesFlatAdmission`，就不能把“无集中”直接等同于 flat-DLS 可吸收。
因此下一步最窄自足目标不是再找新的外部引用，而是证明这两个投影/准入微输入，之后 flat 分支才可与 KLS/DLS 终端对接。
