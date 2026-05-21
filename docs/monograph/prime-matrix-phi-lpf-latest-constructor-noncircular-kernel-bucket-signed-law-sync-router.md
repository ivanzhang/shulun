# Prime Matrix Phi-LPF latest constructor noncircular kernel bucket signed-law sync 证书

**状态：** `phi_lpf_latest_constructor_noncircular_kernel_cut_to_bucket_signed_law_open`

本步把 latest constructor 的非循环 signed emission kernel 接入 Phi-LPF 支撑剥离证书。strict kernel 纪律要求 Cauchy 前声明且不得读取 downstream payment/Phi、row table 或零行覆盖；LPF/Phi 层已经用最小素因子 owner 与 Phi 递推支付 `(p,m)` support key、候选行容量和大素数零质量。因此 constructor 主攻不再是找行、数行或支撑容量，而是对每个 Phi-LPF bucket 正向给出 `PhiLPFBucketSignedCoefficientLawBeforePushforward`。该 signed law、signed survival、row-mass、PDEC scope、ExactUV/key、harmonic/skeleton、Rate 与 DStructure 仍未证明；行/列命题仍未无条件闭合。

```text
latest_constructor_noncircular_kernel_target_imported=true
strict_kernel_first_field_imported=true
phi_lpf_support_stripping_imported=true
phi_lpf_support_and_capacity_closed=true
unsigned_phi_lpf_bucket_cannot_emit_signed_coefficient=true
noncircular_kernel_coarse_target_removed=true
noncircular_signed_coefficient_emission_kernel_proved=false
phi_lpf_bucket_signed_coefficient_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFBucketSignedCoefficientLawBeforePushforward
```

## 1. 同步链

```text
NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter
PhiLPFPrimitiveRowSupportAndCapacityLedger AND PhiLPFBucketSignedCoefficientLawBeforePushforward
LPF/Phi support and capacity stripped off
PhiLPFBucketSignedCoefficientLawBeforePushforward
```

## 2. 支撑样本读数

| N | pi(N) | composites | support keys | bijection |
| ---: | ---: | ---: | ---: | --- |
| 30 | 10 | 19 | 19 | `true` |
| 100 | 25 | 74 | 74 | `true` |
| 997 | 168 | 828 | 828 | `true` |
| 5003 | 670 | 4332 | 4332 | `true` |
| 10000 | 1229 | 8770 | 8770 | `true` |

## 3. bucket signed law 合同

| field | meaning |
| --- | --- |
| `bucket_key` | LPF/Phi 已闭合的 `(p,m)` primitive row support key。 |
| `signed_coefficient_value` | 对该 key 的 Cauchy 前 signed coefficient 正向赋值。 |
| `sign_local_factor` | sign、local factor、非零条件与失败回流标签。 |
| `alpha_delta_side_and_branch_key` | 该 key 属于 alpha/delta 哪侧、哪个 branch key、哪个 `(u,v)` 输出。 |
| `prepushforward_sum_identity` | 对全部 Phi-LPF keys 的 signed 求和在推前前等于 actual alpha/delta 贡献。 |
| `no_downstream_recovery` | 赋值律不读取 payment skeleton、零行覆盖、来源恒等式或终端反推。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestConstructorNoncircularKernelTargetImported` | `true` | `false` | 上一层 row-level fixed-point cut 已把 latest constructor 主攻压到非循环 signed emission kernel。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| `StrictKernelFirstFieldImported` | `true` | `false` | strict kernel 路由把合法 kernel 的首字段钉到 Cauchy 前 actual noncanonical emitter declaration line。 | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter |
| `PhiLPFSupportStrippingImported` | `true` | `false` | 既有 support-stripped 证书把 noncircular kernel 拆成已闭合 LPF/Phi 支撑容量与未闭合 bucket signed law。 | PhiLPFPrimitiveRowSupportAndCapacityLedger AND PhiLPFBucketSignedCoefficientLawBeforePushforward |
| `PhiLPFSupportAndCapacityClosed` | `true` | `true` | LPF 唯一 owner、Phi 递推、candidate row map 与 p>sqrt(N) 零质量已经支付无符号支撑/容量。 | PhiLPFPrimitiveRowSupportAndCapacityLedger |
| `UnsignedPhiLPFBucketCannotEmitSignedCoefficient` | `true` | `true` | LPF/Phi 桶只给 `(p,m)` support key 与容量，不给 sign、local factor、branch key 或推前前 signed 求和。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| `NoncircularKernelCoarseTargetRemoved` | `true` | `false` | constructor 前沿不再停在 noncircular kernel 口；其找行/容量部分剥离后剩 bucket signed coefficient law。 | PhiLPFBucketSignedCoefficientLawBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| `PhiLPFBucketSignedCoefficientLawCurrentCorpusProved` | `false` | `false` | 当前材料没有对每个 LPF/Phi support key 正向赋 signed coefficient、非零 local factor 和 prepushforward identity。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| `SignedSurvivalAndRowMassStillParallel` | `true` | `false` | bucket signed law 仍不自动给非零 signed survival，也不自动支付 same-formal-unit row-mass/no-heavy-row。 | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| `PDECScopeAndTerminalExitsStillParallel` | `true` | `false` | 同集 PDEC scope、canonical lock、independent bridge、terminal WFD、direct pointwise table 与外部谱输入仍作为并行出口保留。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExternalDIBFIKuznetsovDispersionTheoremMatch |
| `TailAndConstructorSiblingFieldsStillParallel` | `true` | `false` | 本层不证明 harmonic/skeleton、ExactUV/source entropy、complete/fixed key、joint rows、Rate 或 DStructure。 | HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把 noncircular kernel 的无符号部分剥离到 LPF/Phi 桶，不证明 signed law 或无条件全局矛盾。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR (PhiLPFBucketSignedCoefficientLawBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger)) AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance AND RatePreservationLedger_FOR_moving_atom_packet AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |

## 5. 最新保留基

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR (PhiLPFBucketSignedCoefficientLawBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger)) AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance AND RatePreservationLedger_FOR_moving_atom_packet AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

下一内部主攻：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
```

条件性 scope/外部输入仍保留：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch
```

并行仍需：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
HarmonicWindowAlpha043PGe3001Upper0850Ledger
DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
RatePreservationLedger_FOR_moving_atom_packet
JointEmitterPrimitiveSummandRowsFormulaBeforePushforward
JointEmitterPrepushforwardWordCoefficientIdentityLedger
JointEmitterNoDownstreamRecoveryAndNamedReturnLedger
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_constructor_noncircular_kernel_bucket_signed_law_sync_router.py` | `09d97653ab262dc22b1e8c2f4cdd11996c924feb94725220466d53bbf42ecf5a` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json` | `7f2888e974e74673edf61a93e53296526b0a4edbf52d59cebb9f114fc3252e3a` |
| `docs/monograph/prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json` | `96d6dadbc5add815f8623295aae5ae519c0b5e44db556d85d657259db97a9773` |
| `docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json` | `c19cac4502bc4a62202e18d136493e2820c11590c92a20ba40f590c7aa7216b4` |
| `docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json` | `d916331b1d8bea632d161cbe99fe4500813feb8333bf0463e4de5767bbf3a81c` |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
