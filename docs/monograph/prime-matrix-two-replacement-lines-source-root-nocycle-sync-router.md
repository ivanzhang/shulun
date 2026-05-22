# Prime Matrix 两条替代线 source-root/no-cycle 同步证书

**状态：** `two_replacement_lines_source_root_nocycle_reduced_to_a1_pdec_rate_dstructure_open`

## 1. 结论

rate-bearing Mertens 尾段闭合后留下的 source-root 活动原子已经可以用后续 strict source-root 终端环、direct PDEC scope 饱和、KZ no-cycle 与 KZ-E source-bridge 证书替换。当前两条替代线不应继续把 source-root 当作独立非循环出口；内部自足线压到 A1 clean branch canonical source admission、fresh same-set PDEC/new-joint 证书、rate-bearing PDEC、RatePreservation 与 DStructure 自足替代包。外部引理版仍只在 AcceptedFullSKLSExtExternalContract 与 DStructure 独立接受同时给定时条件闭合；无黑箱外部版仍需同对象 FullS theorem-match 或新 dispersion 证明。

```text
source_root_active_after_sync=false
external_lemma_version_closed_conditionally=true
external_no_blackbox_version_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RateTailPreviousImported | `true` | `true` | 上一层已经删除自足 PNT/Mertens 尾段旧硬点，并把内部线压到 source-root、PDEC/CleanKLS、Rate 与 DStructure。 | 同步 source-root 后续证书。 |
| SourceRootTerminalCycleImported | `true` | `true` | forward source-root 的内部路线已经回到 signed/source-rank/alpha 终端环；它不再是可作为证明的独立非循环出口。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse |
| DirectPDECScopeSaturatedButUnproved | `true` | `false` | direct same-set PDEC 作用域审计已导入；当前语料仍缺同 formal unit、坏窗集合、U_CRT/L_PDEC 与质量推前完全同口径的证书。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| KZNoCycleGateReducedToDirectKZE | `true` | `false` | 不允许复用 NCBLK/source-root 后，现有 KZ-E 路线只剩直接 well-factorable dispersion log-saving。 | AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection |
| KZEDirectReducedToA1SourceAdmission | `true` | `false` | KZ-E no-projection 自足路线若不接受外部 DI/BFI/Kuznetsov 证书，就必须在 Cauchy/dispersion 前证明 clean A1 分支准入 canonical RIW/Buchstab source。 | A1CleanBranchCanonicalSourceAdmission |
| ExternalNoProjectionStillConditional | `true` | `false` | 外部 no-projection DI/BFI/Kuznetsov 可作为条件输入；它不能冒充内部自足证明。 | ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY |
| SourceRootAtomRemovedFromTwoReplacementLines | `true` | `true` | 两条替代线的最新内部清单不应再把 source-root 当作活动原子；它应被替换为 A1 source admission、fresh same-set PDEC 或 new-joint 证书。 | A1CleanBranchCanonicalSourceAdmission OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| RateBearingPDECGateCarried | `true` | `false` | rate-bearing packet 的 PDEC/CleanKLS 承重门仍未由 source-root 同步自动支付。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet |
| RatePreservationStillOpen | `true` | `false` | moving-atom packet 的速率保持账本仍是独立承重门。 | RatePreservationLedger_FOR_moving_atom_packet |
| DStructureAuthorSideSplitImported | `true` | `false` | DStructure/Rankin 作者侧普通剩余已归零；剩余是独立接受事件，或提交完整文内自足替代包。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage |
| ExternalLemmaPackageConditionPinned | `true` | `false` | 外部引理版只有在 FullS-KLS 外部合同与 DStructure/Rankin 独立接受同时作为输入时闭合；这不是无条件证明。 | AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| NoBlackboxExternalLineStillOpen | `true` | `false` | 无黑箱外部线仍需同对象 FullS theorem-match、actual source capacity 新定理或新的自守/dispersion 证明。 | ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof |
| InternalSelfContainedCondensedToTwoFreshInputs | `true` | `false` | 内部自足线当前只剩 fresh source-admission/PDEC-new-joint 入口，再乘以 rate-bearing PDEC、Rate 与 DStructure 替代包。 | (A1CleanBranchCanonicalSourceAdmission OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage) |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层只替换旧 source-root 活动原子并压窄最新真剩余；外部引理版仍是条件闭合，内部自足版仍未闭合。 | not closed |

## 3. 外部引理版

```text
AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这只是条件闭合口径：FullS-KLS 外部合同和 DStructure/Rankin 独立接受必须同时作为输入。

## 4. 无黑箱外部版

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

泛称 FI/DI/BFI/Kuznetsov/Maynard 不足；必须匹配同一个 completed full-S non-AP WFD 对象、权重、窗口、模数范围、投影和误差预算。

## 5. 内部自足版

```text
((A1CleanBranchCanonicalSourceAdmission OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND HighSegmentModelGapAlpha043C3AnalyticLedger) AND (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR NoFurtherCanonicalSourceTerminalPromotionGap) AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

条件外部 KZ no-projection 支路仅可写为：

```text
(A1CleanBranchCanonicalSourceAdmission OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 直接主攻原子

- `A1CleanBranchCanonicalSourceAdmission`
- `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`
- `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`
- `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet`
- `RatePreservationLedger_FOR_moving_atom_packet`
- `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage`
- `ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof`

## 7. 状态快照

| field | value |
| --- | --- |
| `previous` | `two_replacement_lines_rate_tail_mertens_closed_terminal_gates_open` |
| `source_root` | `forward_source_root_internal_route_reduced_to_terminal_cycle_open` |
| `pdec` | `post_source_root_pdec_scope_saturated_internal_basis_reduced_open` |
| `kz` | `post_new_joint_kz_nocycle_gate_reduced_to_kze_direct_log_saving_open` |
| `kze` | `post_kze_direct_no_projection_reduced_to_actual_source_admission_open` |
| `dstructure` | `dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open` |

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json` | `76b64234307bf057c865b20478520022f755d4232dd99462a57e4bcc2d9421d2` |
| `docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json` | `223f7e68d259298177cb2eb4afd3bc6c0f8f7c696f37633ba1cca7407ac07395` |
| `docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json` | `cec3c0ff75b87992f6544ceee97015142de6d2545521e3197d6ee7a996ab62d4` |
| `docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json` | `daf08ea0d88fb2c0729398c4a59702b9a59e46efb38aae7fe9e2f369e99633d6` |
| `docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json` | `8ea074295bea6900bdb26efb22686da30430e22f94003d9362a25884788bf5d2` |
| `docs/monograph/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-router.json` | `231f7f2e185a924776df064586f93dc7952e2f20f911cec8fa89dcd1e4631879` |
| `experiments/prime_matrix_two_replacement_lines_source_root_nocycle_sync_router.py` | `0825b0378b00c69905a7f4b0df37ab6a8ed8017df0913ae12857aaeae4632002` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `1956bdad74505e81ad5c0ca5e1570a3be4c46951e7043ef46764891635bf2547` |
