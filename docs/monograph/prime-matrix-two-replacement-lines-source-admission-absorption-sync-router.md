# Prime Matrix 两条替代线 A1 source-admission 吸收同步证书

**状态：** `two_replacement_lines_a1_source_admission_absorbed_to_outside_cycle_break_open`

## 1. 结论

`A1CleanBranchCanonicalSourceAdmission` 在 strict source-admission branch absorption 与 post-source-admission macrocycle 证书中已经被识别为 scoped 分支边界，而不是全局排斥原子。因此两条替代线最新内部基应删除 A1 活动 OR，改写为循环外 seed cycle-cut、same-set PDEC、new joint/payload 工件，另乘 rate-bearing PDEC、RatePreservation 与 DStructure/Rankin。外部引理版仍是条件闭合；内部自足版仍未闭合。

```text
a1_source_admission_active_after_sync=false
source_root_active_after_sync=false
external_lemma_version_closed_conditionally=true
external_no_blackbox_version_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreviousSourceRootNoCycleImported | `true` | `true` | 上一层已把 source-root 活动原子替换为 A1 source-admission、same-set PDEC 或 new-joint 证书。 | 继续同步 A1 source-admission 后续证书。 |
| A1BranchStatementCoverageImported | `true` | `true` | A1 canonical source admission 是分支陈述：canonical RIW/Buchstab 子分支可内部处理，generic/noncanonical 分支必须外部化或回流。 | A1CanonicalSourceBranchStatementAndCoverage |
| A1AdmissionAbsorbedFromActiveOR | `true` | `true` | 把 A1 准入作为独立 OR 终端会把 scoped 分支边界误当全局排斥；因此它应从两条替代线活动 OR 中吸收掉。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion |
| PostAdmissionMacrocycleImported | `true` | `true` | 继续沿 A1/PDEC/new-joint/KZ/KZ-E 下钻会回到宏循环；非循环推进必须提交循环外输入。 | AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY |
| SeedCycleCutStillOpen | `true` | `false` | 循环外首选输入 seed cycle-cut primitive basis/coefficient source 当前尚未证明。 | AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput |
| PDECScopeStillOpen | `true` | `false` | same-set PDEC scope 仍需同 formal unit、坏窗集合、U_CRT/L_PDEC 与质量推前同口径证书。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| PayloadOutsideSignedLaneStillOpen | `true` | `false` | new primitive/joint payload 若要破环，必须在 signed-lane/source-entropy 自证环之外给出 pre-Cauchy 工件。 | NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| RateBearingPDECAndRateCarried | `true` | `false` | A1 吸收只删除分支伪终端；它不支付 rate-bearing PDEC/CleanKLS 或 moving-atom 速率保持。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet |
| DStructureReplacementStillOpen | `true` | `false` | DStructure/Rankin 独立接受或完整自足替代包仍是最终晋级门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage |
| A1RemovedFromTwoReplacementLines | `true` | `true` | 两条替代线最新内部基不应再把 A1 source-admission 列为活动证明原子。 | (AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层只吸收 A1 分支陈述伪出口；循环外输入、rate 与 DStructure 均未闭合。 | not closed |

## 3. 内部自足版

```text
((AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND HighSegmentModelGapAlpha043C3AnalyticLedger) AND (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR NoFurtherCanonicalSourceTerminalPromotionGap) AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

## 4. 条件外部 KZ 支路

```text
(AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY) AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 外部两线

外部引理版：

```text
AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 直接主攻原子

- `AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput`
- `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`
- `NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle`
- `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`
- `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet`
- `RatePreservationLedger_FOR_moving_atom_packet`
- `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage`

## 7. 状态快照

| field | value |
| --- | --- |
| `previous` | `two_replacement_lines_source_root_nocycle_reduced_to_a1_pdec_rate_dstructure_open` |
| `a1_absorb` | `strict_source_admission_absorbed_as_branch_statement_moving_atom_open` |
| `a1_macro` | `phi_lpf_latest_constructor_post_source_admission_macrocycle_rebased_open` |
| `a1_branch` | `canonical_branch_admission_reduced_to_branch_statement_and_coverage` |
| `dstructure` | `dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open` |

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json` | `76b64234307bf057c865b20478520022f755d4232dd99462a57e4bcc2d9421d2` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.json` | `65f8fff5d92d4fbb8f4268c23a434ba7663c1250d046fe549933e5ff05b4e7d8` |
| `docs/monograph/prime-matrix-strict-source-admission-branch-absorption-router.json` | `ff738635e2f712ebb777170a718e8775362847a92b7e29c4933da438fd7d64d6` |
| `docs/monograph/prime-matrix-triad-a1-canonical-branch-admission-router.json` | `80d6a38882ba2326054e52702f82ae67bee05fc0aed3e94fb58b53287c7debff` |
| `docs/monograph/prime-matrix-two-replacement-lines-source-root-nocycle-sync-router.json` | `c7de8b3f9019f9fcb84844867d9bb245abba296b3dec63f9020b66d56e34f405` |
| `experiments/prime_matrix_two_replacement_lines_source_admission_absorption_sync_router.py` | `5c038c7f2c6993e5844314cdc539e0e6e06d2bc9cd701907d4a0bd61c181f10e` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `099e536e52168ced1bbb30c042cd7f8f55fee2c704040c06952db36d441acfcd` |
