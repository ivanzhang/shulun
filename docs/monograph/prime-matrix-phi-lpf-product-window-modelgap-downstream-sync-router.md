# Prime Matrix Phi-LPF product-window modelgap downstream sync 证书

**状态：** `product_window_modelgap_downstream_synced_signed_payload_and_terminal_gates_open`
**核验日期：** `2026-05-26`

本步把 product-window terminal/modelgap frontier 留下的 `ExplicitModelGapAndFiniteDPRCLedger` 接入既有下游证书链：低段有限 DPRC、高段模型余量因子化、Dusart 调和窗口、动态粗骨架有限桥、P>=100000 lower-sieve 尾段、B3/Mertens 最新同步。结论是模型缺口不再应作为 product-window 当前第一硬点。但这不是三命题无条件闭合：product-window signed payload、pre-Cauchy identity、same-unit rank/ExactUV、RatePreservation、DStructure/Rankin 以及 admissible trace/Type-II 通道仍未证明。

```text
product_window_modelgap_gate_active_before_sync=true
explicit_model_gap_finite_split_imported=true
high_segment_factorization_imported=true
harmonic_window_dusart_closed=true
dynamic_skeleton_lower_factorization_imported=true
strict_mertens_tail_closed_by_latest_rate_sync=true
product_window_modelgap_downstream_removed_from_active_basis=true
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
row_column_unconditional_closed=false
```

## 1. 下游同步链

| from | to | meaning |
| --- | --- | --- |
| `ExplicitModelGapAndFiniteDPRCLedger` | `HighSegmentModelGapAlpha043C3AnalyticLedger` | 低段有限 DPRC 证书已闭合，模型缺口混合账本先压成高段模型余量。 |
| `HighSegmentModelGapAlpha043C3AnalyticLedger` | `HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger` | 高段模型余量被拆成调和窗口上界与动态粗骨架下界，桥接段 2003<=P<3001 已闭合。 |
| `HarmonicWindowAlpha043PGe3001Upper0850Ledger` | `DusartPrimeReciprocalWindowAlpha043Upper0850Closed` | 调和窗口由有限枚举加 Dusart 素数倒数和显式估计关闭。 |
| `DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger` | `LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger` | 动态粗骨架有限段 3001<=P<100000 已闭合，尾段压成一维 lower-sieve。 |
| `LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger` | `LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger` | P=100000 处 10% 模型主项已超过 401，尾段义务压成显式 10% 主项包。 |
| `B3/Mertens tail package` | `closed for current strict rate-bearing tail sync` | 后续 rate-bearing Mertens 同步已把自足 Mertens 尾段移出活动剩余；但 Rate、PDEC 与 DStructure 门仍开放。 |
| `product-window modelgap side` | `ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync` | 模型缺口不再是 product-window 当前第一主攻；第一硬点转回 signed payload、Rate 与 DStructure。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ProductWindowModelGapGateActiveBeforeSync | `true` | `false` | 上一 product-window 证书的第一硬点确为 ExplicitModelGapAndFiniteDPRCLedger。 | ExplicitModelGapAndFiniteDPRCLedger |
| ExplicitModelGapFiniteSplitImported | `true` | `false` | P<2003 有限 DPRC 已闭合，混合模型缺口账本被拆成高段模型余量。 | HighSegmentModelGapAlpha043C3AnalyticLedger |
| HighSegmentFactorizationImported | `true` | `false` | 2003<=P<3001 桥接段已闭合；P>=3001 只剩调和窗口与动态骨架两输入。 | HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger |
| HarmonicWindowDusartClosed | `true` | `true` | 调和窗口上界已由有限段与 Dusart 素数倒数和显式估计关闭。 | closed; keep DynamicRoughSkeleton side only |
| DynamicSkeletonLowerFactorizationImported | `true` | `false` | 动态粗骨架有限段已闭合，尾段改写为 P>=100000 的一维 lower-sieve 账本。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| LinearTailTenPercentMarginCompressed | `true` | `false` | 尾段 lower-sieve 输入已压成 10% 模型主项显式余量包。 | LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger |
| B3TailBridgeImportedWithStrictGuard | `true` | `false` | B3 粗筛接口、lower weights 支配和 10% 容量代数已对齐；该桥本身仍保留严格自足守卫。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 before latest Mertens sync |
| StrictMertensTailClosedByLatestRateSync | `true` | `true` | 后续 rate-bearing Mertens 最新同步已关闭旧自足 Mertens 尾段原子；本证书只导入该尾段事实。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance still open in the rate-bearing branch |
| ProductWindowModelGapDownstreamRemovedFromActiveBasis | `true` | `false` | 模型缺口下游链已足够同步，不能再把 ExplicitModelGap 作为 product-window 第一主攻。 | ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync |
| ProductWindowSignedPayloadStillOpen | `false` | `false` | 真正破奇偶性仍需要推前前 signed payload、pre-Cauchy identity、same-unit rank/ExactUV 与 internal transition。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| RateAndDStructureStillOpen | `false` | `false` | RatePreservation 与 DStructure/Rankin 独立验收没有被模型缺口下游同步关闭。 | RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本证书是下游前沿同步，不是三命题无条件闭合证明。 | row_column_unconditional_closed=false |

## 3. 最新保留基

终端侧：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

product-window 总保留基：

```text
((PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND NoFurtherCanonicalSourceTerminalPromotionGap AND ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients OR PointwiseSqrtPrimeInputCOne OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND RatePreservationLedger_FOR_moving_atom_packet
```

仍开放的实际负载摘要：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

并行仍需：

```text
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients
PointwiseSqrtPrimeInputCOne
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
```

严格含义：本证书只同步模型缺口下游链，不证明 signed payload、Rate、DStructure 或行/列命题。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-dynamic-skeleton-lower-factorization-router.json` | `2c46448ba6bd4969f962984ad095d47199a787ef4906d5d2297ac5c252fefa8d` |
| `docs/monograph/prime-matrix-explicit-model-gap-finite-ledger-router.json` | `c7a64bd09aae24e52f1a6a6d8048506342358f959952c7678bf91c82dcf20e1a` |
| `docs/monograph/prime-matrix-harmonic-window-dusart-ledger-router.json` | `19070e055ced7cecb38b8a23661193fad075069c796ad66df630ebbfbc084b6f` |
| `docs/monograph/prime-matrix-high-segment-model-gap-factorization-router.json` | `32115b117e03e8e0c5f98db427c294ae85cd58eebdd323446e1fc79be30e3e43` |
| `docs/monograph/prime-matrix-linear-lower-sieve-tail-margin-router.json` | `de5e6e1f6f2ff1a6bf3bee4b10c45a8380b84d630e24697fec6f8eefee3dd7b5` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-terminal-modelgap-frontier-router.json` | `de92042ea621475895f0fac5f9f28d153de3c84b1e69d6ea9f1482772ac48ef8` |
| `docs/monograph/prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json` | `dad9b5f3f5f1d66df613a270f14e4608e99b511c22efa597075061bfc528f55e` |
| `docs/monograph/prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json` | `41ecd4cfd58beb65c2ec5e1b5fdf2119ec46954e790ed0f036f92b66bfc282d4` |
| `experiments/prime_matrix_phi_lpf_product_window_modelgap_downstream_sync_router.py` | `671bf346bc7e554325fa0d389d204e275f3df7fca90ea042feb5b0dc29a1a7d6` |
