# Prime Matrix Phi-LPF moving-atom source-bucket preimage sync 证书

**状态：** `phi_lpf_moving_atom_source_bucket_preimage_synced_signed_injection_open`

本步把最新 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` 接到 LPF/Phi 源桶前像。LPF ownership 与 Phi 递推已经严格删除无主 moving atom 和 prime-row/virtual-unit 源前像出口：若 clean-core moving atom 真实来自 composite source，它的推前前支撑必须分解为唯一 `(p,m)` 桶。这个结论仍是无符号支撑层，不能自动产生 signed coefficient、local factor、alpha/delta branch 或同 formal unit 的 no-heavy-row 质量注入。最新直接主攻因此收窄为 `LPFMovingAtomSignedPreimageMassInjectionLedger`，并行保留逐点 Phi-LPF signed 表、signed survival/row-mass、PDEC/CleanKLS 速率包、高段模型余量、Rate 和 DStructure。行/列命题仍未无条件闭合。

```text
latest_independent_moving_atom_frontier_imported=true
lpf_phi_composite_ownership_identity_imported=true
lpf_bucket_identity_sample_verified=true
moving_atom_unsigned_source_preimage_partition_closed=true
prime_row_leak_and_virtual_unit_preimage_blocked=true
signed_mass_injection_proved=false
rate_bearing_packet_exclusion_proved=false
independent_nonterminal_moving_atom_exclusion_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=LPFMovingAtomSignedPreimageMassInjectionLedger
```

## 1. LPF/Phi 桶恒等式读数

```text
Phi(x,p_k) = Phi(x,p_{k+1}) + Phi(floor(x/p_k),p_k)
C(N) = sum_{p<=sqrt(N)} (Phi(floor(N/p),p)-1)
pi(N) = N - 1 - C(N)
```

N=10000 的机器审计：`bucket_sum=8770`，`composite_actual=8770`，`pi_by_identity=1229`，`pi_actual=1229`。

| p | floor(N/p) | Phi(floor(N/p),p) | c(p) |
| ---: | ---: | ---: | ---: |
| 2 | 5000 | 5000 | 4999 |
| 3 | 3333 | 1667 | 1666 |
| 5 | 2000 | 667 | 666 |
| 7 | 1428 | 381 | 380 |
| 11 | 909 | 208 | 207 |
| 13 | 769 | 160 | 159 |
| 17 | 588 | 111 | 110 |
| 19 | 526 | 95 | 94 |
| 23 | 434 | 77 | 76 |
| 29 | 344 | 60 | 59 |

## 2. 同步链

| from | to | meaning |
| --- | --- | --- |
| `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` | `ActualNoncanonicalCleanCoreMovingAtomExclusion` | independent nonterminal 版本仍以排斥 actual clean-core moving atom 为目标。 |
| `ActualNoncanonicalCleanCoreMovingAtomExclusion` | `LPFMovingAtomSourceBucketPreimagePartitionLedger` | 若 moving atom 来自 actual composite source，则每个推前前源键有唯一 LPF owner bucket。 |
| `LPFMovingAtomSourceBucketPreimagePartitionLedger` | `LPFMovingAtomSignedPreimageMassInjectionLedger` | 无符号前像分桶已闭合；剩余是 signed 质量、local factor、branch 与 no-heavy-row 的同单位注入。 |
| `LPFMovingAtomSignedPreimageMassInjectionLedger` | `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND HighSegmentModelGapAlpha043C3AnalyticLedger)` | 若 signed 注入闭合，下一步必须由逐点 signed 表排斥，或落入速率型终端包/PDEC-CleanKLS 账本。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LatestIndependentMovingAtomFrontierImported | `true` | `false` | latest alpha terminal three-atoms 同步已把当前直接主攻钉在 independent nonterminal moving atom。 | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| LPFPhiCompositeOwnershipIdentityImported | `true` | `true` | LPF ownership 与 Phi 递推给出合数支撑的唯一 owner bucket 和精确容量；N=10000 样本恒等式通过。 | LPFMovingAtomSourceBucketPreimagePartitionLedger |
| MovingAtomUnsignedSourcePreimagePartitionClosed | `true` | `true` | clean-core moving atom 若来自 actual composite source，其推前前源支撑可按唯一 `(p,m)`、`p=LPF(pm)`、`m` p-rough 分桶；无主 moving atom 出口被删除。 | LPFMovingAtomSignedPreimageMassInjectionLedger |
| PrimeRowLeakAndVirtualUnitPreimageBlocked | `true` | `true` | Phi 公式中的 `m=1` 是 prime row 修正，不是 composite moving-atom source；真实最小源桶从 square-base `(p,p)` 开始。 | LPFMovingAtomSignedPreimageMassInjectionLedger |
| SignedMassInjectionNotGeneratedByUnsignedPhi | `true` | `false` | LPF/Phi 只给无符号支撑与容量；从 large same-(u,v) final atom 反推同 formal unit 的 signed preimage 质量仍需正向系数表与 no-heavy-row 账本。 | LPFMovingAtomSignedPreimageMassInjectionLedger AND PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| RateBearingPacketInterfaceImported | `true` | `false` | 已有 moving-block 同步消除了无名低维出口：低维签名进 PDEC/SAE/ColumnCRT，无签名进速率型终端包。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet |
| IndependentMovingAtomExclusionAfterLPFProved | `false` | `false` | 本层只删除无主/prime-row 源前像出口；仍未排斥 LPF-owned signed preimage 或速率型终端包。 | LPFMovingAtomSignedPreimageMassInjectionLedger OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet) |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层是前沿同步与源桶前像归约，不是三目标命题无条件闭合。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR LPFMovingAtomSignedPreimageMassInjectionLedger) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. strict 基

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR LPFMovingAtomSignedPreimageMassInjectionLedger) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 最新保留基

```text
((LPFMovingAtomSourceBucketPreimagePartitionLedger AND LPFMovingAtomSignedPreimageMassInjectionLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR ActualNoncanonicalCleanCoreMovingAtomExclusion) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
LPFMovingAtomSignedPreimageMassInjectionLedger
```

并行主攻：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
HighSegmentModelGapAlpha043C3AnalyticLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_moving_atom_source_bucket_preimage_sync_router.py` | `a8f9f7e115ba3a5b1c5a3b4d034fe7aa837e0235536799a8cd25303c8367380b` |
| `docs/monograph/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.json` | `41da3e8b643b76144bf63d8dcf6701f79831bd9a4113edd42b93807a8b4ef681` |
| `docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json` | `2857cbdeab08a400b1bce9099500290e8c59439ec11553ca0e5678335a5e6806` |
| `docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json` | `d916331b1d8bea632d161cbe99fe4500813feb8333bf0463e4de5767bbf3a81c` |
| `docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json` | `c19cac4502bc4a62202e18d136493e2820c11590c92a20ba40f590c7aa7216b4` |
| `docs/monograph/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json` | `65fb8bbd578b7dcc32c930fc86e8ea9b803d59b4d5773c589c44cfec90027e58` |
| `docs/monograph/prime-matrix-phi-lpf-source-entropy-signed-survival-router.json` | `073edf36be5e26306930db964a9a7920916efc6af78c1fb034a4a34f804189f7` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.json` | `ed0043e2cdc051382cb6a28f6383f79a397773ec5ee3e9ca1ba7f8df260f2fda` |
| `docs/monograph/prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json` | `f5135c99d7f964b3c5b29b81681512083ff8bcaca431ff71fda3f2606fa81b9a` |
