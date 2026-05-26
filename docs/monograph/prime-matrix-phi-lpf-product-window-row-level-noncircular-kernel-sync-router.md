# Prime Matrix Phi-LPF product-window row-level noncircular-kernel sync 证书

**状态：** `product_window_row_level_fixed_point_cut_to_noncircular_signed_kernel_open`
**核验日期：** `2026-05-26`

本步把 product-window 最新第一硬点 `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` 接入 strict row-level、strict signed-source fixed-point 与 latest constructor row-level sync 证书。结论是：row-level 表若要成立，必须由无环 pre-Cauchy seed signed-row emitter 正向产生；但现有内部展开会回到同一 row-level 表。删除该固定点后，第一主攻同步为 `NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows`。

```text
row_table_to_seed_emitter_imported=true
signed_source_fixed_point_cut_imported=true
latest_constructor_row_level_sync_imported=true
reverse_payment_and_zero_row_recovery_blocked=true
product_window_row_level_coarse_target_removed=true
next_primary_attack_target=NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
row_column_unconditional_closed=false
```

## 1. 下游同步链

| from | to | meaning |
| --- | --- | --- |
| `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` | `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity` | 逐行原始生成表必须由无环 pre-Cauchy seed signed-row emitter 正向产生。 |
| `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity` | `signed source spine -> basis word -> assignment -> value map -> origin identity -> row table` | 现有内部展开回到同一 row-level 表，形成 signed-source 固定点。 |
| `fixed point rejected as proof` | `NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows` | 删除自证环后，必须提交不读取 row table/payment/来源恒等式的 pre-Cauchy signed kernel。 |
| `missing kernel or failed local factor` | `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily` | 若 kernel、非零局部因子或作用域失败，必须进入命名终端回流。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ProductWindowRowLevelTargetActiveBeforeSync` | `true` | `false` | 上一层 product-window 同步把第一硬点推进到 row-level clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `StrictRowLevelRouterImported` | `true` | `false` | strict row-level 证书说明该表必须由无环 pre-Cauchy seed signed-row emitter 产生。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SignedSourceFixedPointCutImported` | `true` | `true` | signed-source 内部展开回到同一 row-level 表；该固定点不能作为证明。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `LatestConstructorRowLevelSyncImported` | `true` | `false` | latest constructor 线已独立把 row-level 粗口删除并同步到 noncircular signed kernel。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `ReversePaymentAndZeroRowRecoveryBlocked` | `true` | `true` | payment 反推、来源环和早期零行 unsigned cover 均不能恢复 signed coefficient source。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `NoncircularSignedKernelStillOpen` | `true` | `false` | 当前材料没有不读取 row-level 表、来源恒等式、payment/Phi 下游或零行覆盖的 Cauchy 前 signed coefficient 发射核。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `SignedSurvivalAndRowMassStillParallel` | `true` | `false` | kernel 只解决 signed coefficient 来源；非零 signed survival 与 row-mass/no-heavy-row 仍需独立支付。 | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| `ProductWindowRowLevelCoarseTargetRemoved` | `true` | `false` | product-window 第一主攻不应停在 row-level 表名；删除固定点后必须提交 noncircular signed kernel。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本证书只同步 row-level fixed-point cut，不证明 kernel、signed survival、row-mass 或终端排斥。 | row_column_unconditional_closed=false |

## 3. 最新保留基

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR (NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger)) AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
```

失败回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```

并行仍需：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

严格含义：本证书只同步 row-level fixed-point cut，不证明行/列命题。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json` | `7f2888e974e74673edf61a93e53296526b0a4edbf52d59cebb9f114fc3252e3a` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-signed-expression-origin-table-sync-router.json` | `0f2ed8409a6d29b48a35799cf1323dcd60e6a0c47aa642bb7b48b31648ebbe8e` |
| `docs/monograph/prime-matrix-strict-row-level-origin-generation-table-router.json` | `a9ac8a47342465ed4499d5ca8540fc54b5072d82c4bfba2d53c17b5b2d7e4a78` |
| `docs/monograph/prime-matrix-strict-signed-source-fixed-point-breaker-router.json` | `a07743b021b11f13f19d791fc43d4268f551878c43f3340bd54664254311185f` |
| `experiments/prime_matrix_phi_lpf_product_window_row_level_noncircular_kernel_sync_router.py` | `8dd13ca12a599775c3245c173ad01375702af1417af61cd41db664df01e3927e` |
