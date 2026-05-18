# Prime Matrix strict pair-energy 对角剥离终端归约证书

**状态：** `direct_pair_energy_diagonal_peeling_reduces_to_ncblk_or_pdec_model_open`

本步直接拆解 `SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed`。任何 exact-pair L2/max-atom 大筛都必须先处理对角重原子；否则单个 exact pair 的 delta 模型立即破坏 log-power no-heavy 目标。对角失败已经是既有 `RateBearingLargePairAtomPacketExclusion`，并回到 PDEC/clean terminal 三路；对角剥离后的 off-diagonal 估计正是 clean Kuznetsov/DLS，而该原子已进一步压到 `AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom`。同时 PDEC/CleanKLS+模型余量分支拆成同集 PDEC 作用域与高段模型余量。因此 direct pair-energy 不再是独立第三分支；最新严格剩余为 NCBLK/source anti-atom，或 PDEC 同集作用域加高段模型余量。行/列命题仍未无条件闭合。

```text
direct_pair_energy_atom_active=true
diagonal_delta_obstruction_closed=true
offdiagonal_clean_pair_large_sieve_reduced_to_kuznetsov_dls=true
kuznetsov_dls_reduced_to_ncblk=true
model_gap_reduced_to_high_segment=true
direct_pair_energy_disjunct_still_independent=false
row_column_unconditional_closed=false
```

## 1. 对角剥离图

| from | to | meaning |
| --- | --- | --- |
| `SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed` | `SameFormalUnitExactPairDiagonalNoHeavyAtomLedger AND CleanOffDiagonalExactPairDualLargeSieveLedger` | 任何 exact-pair L2/max-atom 大筛都必须先控制对角单 pair 质量，再处理 off-diagonal 相关和。 |
| `NOT SameFormalUnitExactPairDiagonalNoHeavyAtomLedger` | `RateBearingLargePairAtomPacketExclusion` | 对角无重原子失败就是同 formal unit 的 rate-bearing 大 exact-pair 原子包。 |
| `RateBearingLargePairAtomPacketExclusion` | `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks` | rate-bearing 大 pair packet 的持久签名进入 PDEC 作用域；clean 漂移进入 Kuznetsov/DLS。 |
| `CleanOffDiagonalExactPairDualLargeSieveLedger` | `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks` | 剥离对角与低维回流后，off-diagonal exact-pair 双线性型就是 clean Kloosterman/DLS 大筛对象。 |
| `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks` | `AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom` | 既有 KZ-A--KZ-E 同步把自足 Kuznetsov/DLS 的剩余压到 acyclic NC-BLK/source anti-atom。 |
| `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger` | `(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks) AND HighSegmentModelGapAlpha043C3AnalyticLedger` | PDEC/CleanKLS 终端拆成同集 PDEC 作用域或 KZ/DLS；模型余量有限段已闭合，高段余量仍开放。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DirectPairEnergyAtomActive` | `true` | `false` | 上一轮把下一直接主攻钉为 direct exact-pair energy 大筛。 | SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed |
| `DiagonalDeltaObstructionClosed` | `true` | `true` | 没有同 formal unit 的对角无重原子输入时，单 exact-pair delta 模型直接违反 L2/max-atom 目标。 | SameFormalUnitExactPairDiagonalNoHeavyAtomLedger |
| `PairEnergyMustPeelDiagonal` | `true` | `true` | direct pair-energy 大筛必须拆成对角 no-heavy 账本与 off-diagonal clean 双线性大筛。 | SameFormalUnitExactPairDiagonalNoHeavyAtomLedger AND CleanOffDiagonalExactPairDualLargeSieveLedger |
| `DiagonalFailureReturnsToRatePacket` | `true` | `true` | 对角 no-heavy 失败已经由既有 packetization 精确登记为 rate-bearing 大 pair packet，并进入终端三路。 | RateBearingLargePairAtomPacketExclusion |
| `SourcePacketStillOpenForDiagonalNoHeavy` | `true` | `false` | 若要正向证明对角 no-heavy，需要 pre-Cauchy actual source declaration packet；当前语料未给出。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| `OffDiagonalPartEqualsCleanKuznetsovDLS` | `true` | `false` | 剥离对角、PDEC 和 sparse/ColumnCRT 后，off-diagonal 估计正是 clean Kloosterman/Kuznetsov-DLS 大筛。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `KuznetsovDLSReducedToNCBLK` | `true` | `false` | KZ-A--KZ-D 已闭合，KZ-E 的 log-saving 剩余压到 acyclic NC-BLK/source anti-atom。 | AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |
| `PDECCleanKLSAndModelGapSplitImported` | `true` | `false` | PDEC/CleanKLS 已拆成同集 PDEC 作用域或 KZ/DLS；模型余量有限段闭合，高段解析余量仍开放。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |
| `DirectPairEnergyDisjunctSubsumed` | `true` | `true` | direct pair-energy 分支剥离后只回到 KZ/NCBLK 或 PDEC 作用域；它不再是独立于终端两路的第三分支。 | AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只删除 direct pair-energy 伪独立分支；NCBLK/source anti-atom、PDEC 作用域、高段模型余量、Rate 与 DStructure 仍未证明。 | (AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger)) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 对角 delta 阻断样例

| k | log y | threshold | single mass | L2 energy | violates |
| ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 3.72057e-14 | 1.0 | 1.0 | `True` |
| 4 | 9.21034 | 3.72897e-16 | 1.0 | 1.0 | `True` |
| 5 | 11.5129 | 1.04961e-17 | 1.0 | 1.0 | `True` |
| 6 | 13.8155 | 5.67713e-19 | 1.0 | 1.0 | `True` |
| 7 | 16.1181 | 4.81926e-20 | 1.0 | 1.0 | `True` |
| 8 | 18.4207 | 5.68996e-21 | 1.0 | 1.0 | `True` |
| 9 | 20.7233 | 8.64309e-22 | 1.0 | 1.0 | `True` |

## 4. 最新剩余

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger)
```

严格活动基：

```text
(AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger)) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
```

并行保留：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 诚实边界

- 本证书只删除 direct pair-energy 的伪独立地位，不证明 NCBLK/source anti-atom。
- PDEC 同集作用域、高段模型余量、RatePreservation 与 DStructure/Rankin 仍未闭合。
- 对角 delta 表是阻断黑箱大筛的确定性模型，不是行/列命题证明。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_pair_energy_diagonal_peeling_terminal_reduction_router.py` | `4b861b4985f24a5504381b045e5b1690db8bb082faaa0c4c057333c2e114fa40` |
| `docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json` | `e3a50b8cac8b76860ca77442c786e57e7420e7a8cb05182b570798f68c56174c` |
| `docs/monograph/prime-matrix-strict-independent-pair-energy-attack-router.json` | `b587d4d2665daeb0158f0c429f52b98ec6461e1e33d6d6a1b4b60af76dd88f74` |
| `docs/monograph/prime-matrix-strict-rate-bearing-large-pair-packet-router.json` | `2d8b4f875ebf4cbe7712e4d8f3ac6ad3cda374b0a381788a599587bc7e246872` |
| `docs/monograph/prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json` | `fb988aea08dcdf541574fa412e2e37254570b8ad688b010a6c0366c03c4e7270` |
| `docs/monograph/prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json` | `9c97ae816a9b8840e743496fabd791c8792c136a547c0990010f31ea0a80f19d` |
| `docs/monograph/prime-matrix-explicit-model-gap-finite-ledger-router.json` | `c7a64bd09aae24e52f1a6a6d8048506342358f959952c7678bf91c82dcf20e1a` |
| `docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json` | `d9e042ffccaaf050e72788abdb0a10a5776a3cb4d8a37fc949c9710a4a832f44` |
| `docs/monograph/prime-matrix-strict-exact-uv-support-attack-router.json` | `e9f89b9cc78c45934694a16a33c108347a20b70c1a9a814f34dd39c9f565a08b` |
| `docs/monograph/prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json` | `949d8afe0b5b1c450c23dd4cc72eecdca5368c247d63507ebd7eb9d3d42493d5` |
