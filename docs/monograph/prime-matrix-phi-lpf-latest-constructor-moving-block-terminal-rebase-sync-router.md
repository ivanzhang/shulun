# Prime Matrix Phi-LPF latest constructor moving-block terminal rebase sync 证书

**状态：** `phi_lpf_latest_constructor_moving_block_terminal_rebased_open`

本步把最新 rebase 后的 `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn` 接入 strict moving-block 终端路由。该输入不能作为新的无名黑箱；全局拆分把它压到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`，同时 `ExplicitModelGapAndFiniteDPRCLedger` 仍独立保留。

```text
latest_rebased_fresh_joint_moving_block_input_imported=true
existing_constructor_moving_block_terminal_reusable=true
strict_actual_moving_block_router_imported=true
global_pdec_sparse_split_imported=true
precauchy_alpha_terminal_sync_agrees=true
constructor_moving_block_unnamed_exit_removed=true
actual_noncanonical_moving_block_spread_ncb_lk_proved=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

## 1. 同步链

```text
FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestRebasedFreshJointMovingBlockInputImported` | `true` | `false` | 上一层 rebase 已把 constructor fresh joint declaration 压到 actual moving-block/NC-BLK。 | ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn |
| `ExistingConstructorMovingBlockTerminalReusable` | `true` | `false` | 旧 constructor moving-block terminal 同步输入相同，可在新 rebase 前沿复用。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `StrictActualMovingBlockRouterImported` | `true` | `true` | strict moving-block 路由已说明该输入不能作为无名终端停留。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本层只在反例链内部同步，不用真实零行缺席或有限数值现象作全局证明。 | 命名终端、模型账本或并行开放字段。 |
| `GlobalPDECSparseSplitImported` | `true` | `true` | moving-block 的 global PDEC/sparse terminal 已经由全局拆分回到 PDEC/CleanKLS 容量门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `CurrentMaterializedTerminalFrontierExhausted` | `true` | `true` | 当前已物化 PDEC/sparse 前沿清零；这只是当前材料边界，不是未来 family 的不存在性证明。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `PreCauchyAlphaTerminalSyncAgrees` | `true` | `true` | latest pre-Cauchy alpha productive 分支也把 moving-block 回接到同一 PDEC/CleanKLS 与模型账本。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `ConstructorMovingBlockUnnamedExitRemoved` | `true` | `true` | constructor fresh-joint 路线不能把 moving-block/NC-BLK 作为新的独立黑箱。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `ModelGapLedgerRetained` | `true` | `false` | moving-block 专属 DPRC 兼容门可删除，但显式模型余量与有限 DPRC 账本仍需证明。 | ExplicitModelGapAndFiniteDPRCLedger |
| `ConstructorJointRowsIdentityReturnStillParallel` | `true` | `false` | 本层只替换 moving-block 原子；joint rows、word/coefficient identity 与 no-downstream return ledger 仍未证明。 | JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger |
| `SourceExactUVAndSignedMassStillParallel` | `true` | `false` | source entropy/ExactUV、signed survival、row-mass、complete/fixed key 仍不是 moving-block 路由的结论。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| `RateDStructureStillParallel` | `true` | `false` | Rate preservation 与 DStructure/Tail-log4/finite Rankin 独立验收门继续保留。 | RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只做 rebase 同步；未证明三命题无条件闭合。 | ((AlphaRowAnchorPhaseEmissionFormulaLedger AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger) OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger) OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

并行仍需：

```text
ExplicitModelGapAndFiniteDPRCLedger
JointEmitterPrimitiveSummandRowsFormulaBeforePushforward
JointEmitterPrepushforwardWordCoefficientIdentityLedger
JointEmitterNoDownstreamRecoveryAndNamedReturnLedger
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_constructor_moving_block_terminal_rebase_sync_router.py` | `9a01e66e019cbec420d4ad68c195416c41ca83c5f8cda9888e8af267c5cc5605` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-rebase-sync-router.json` | `96c0ddb0422ebe7c7094628dafdf6c37776db5bbbc4528b8d9837d3f0e966f74` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-router.json` | `3f3ac9568f2d039437ca3a2bd7581658d1418a7caf3335891e78c09f71077613` |
| `docs/monograph/prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json` | `d042d5ccfeec63bcfba1c16571e404052d7a66cefce94527ce843051b64a2f6e` |
| `docs/monograph/prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json` | `e30d4f506435633e7614c16ee4f1faa1b65bf739dd93fd731050f5972155c078` |
| `docs/monograph/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json` | `b29335cbb7c029994260284c3e3c6c07e896329a51ca8446ec60b832ca6b8357` |
