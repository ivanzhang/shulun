# Prime Matrix Phi-LPF small-to-large factor-peeling signed-state boundary 证书

**状态：** `small_to_large_factor_peeling_closes_unsigned_states_not_signed_payload`
**核验日期：** `2026-05-25`

本证书把“从小到大精细化分剥素因子”落成 LPF-owned composite bucket 账本。
结论是：剥离路径、Möbius、Liouville、depth parity 与 squarefree 状态都能闭合，
但它们仍只是无符号 factor-word label，不能生成 pre-Cauchy signed payload。

```text
small_to_large_factor_peeling_verified_all_samples=true
mobius_liouville_state_computable_from_factor_word_all_samples=true
prime_row_or_virtual_unit_leak_blocked_all_samples=true
peeling_generates_new_precauchy_signed_payload=false
orientation_local_factor_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
built_in_signed_pairing_proved=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 1. 样本读数

| N | composite keys | owner buckets | factor steps | max depth | squarefree | nonsquarefree | mu + / - / 0 | lambda + / - |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100 | 74 | 4 | 140 | 5 | 52 | 22 | 16/36/22 | 26/48 |
| 997 | 828 | 11 | 1869 | 8 | 597 | 231 | 231/366/231 | 339/489 |
| 5003 | 4332 | 19 | 10571 | 11 | 3152 | 1180 | 1293/1859/1180 | 1855/2477 |
| 10000 | 8770 | 25 | 21986 | 12 | 6406 | 2364 | 2687/3719/2364 | 3818/4952 |
| 30030 | 26781 | 40 | 69651 | 13 | 19673 | 7108 | 8367/11306/7108 | 11810/14971 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OrderedFactorWordImported` | `true` | `true` | 既有 ordered coherence 证书已关闭 p-rough cofactor 的非降 LPF 词唯一性。 | `PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward` |
| `SmallToLargePeelingVerifiedOnSamples` | `true` | `true` | 本证书重新枚举 composite LPF buckets，验证每个 cofactor 的从小到大剥离路径。 | `closed unsigned factor-word ledger` |
| `MobiusLiouvilleSquarefreeStateClosed` | `true` | `true` | Möbius、Liouville、depth parity、squarefree 都是 factor word 的机械函数。 | `post-factorization arithmetic state table` |
| `PrimeRowAndVirtualUnitLeakBlocked` | `true` | `true` | composite moving-source bucket 从 m>=p 开始；m=1 只是 prime-row 修正，不是 composite source。 | `prime-row leak blocked` |
| `PeelingStateIsUnsignedLabelOnly` | `true` | `true` | 剥离状态只依赖整数因子词；它没有 pre-Cauchy source key、orientation 或 ExactUV trace。 | `PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward` |
| `OrientationLocalFactorStillOpen` | `true` | `false` | orientation/local-factor product law 仍不是 LPF/Phi factor word 的推论。 | `PrimitiveOrientationLocalFactorProductLawBeforePushforward` |
| `LatestGlobalBasisStillNeedsBuiltInPairing` | `true` | `false` | 按最新全局 strict 基底，signed 路线最终仍需 atomic joint rows 的内置配对闭式。 | `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` |
| `ExactUVSourceEntropyStillOpen` | `true` | `false` | 剥离因子不会给 complete key、source entropy 或 fixed-key ExactUV multiplicity。 | `ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger` |
| `PointwiseSignedTableStillOpen` | `true` | `false` | 逐点 Phi-LPF signed table 若要闭合，首字段仍是 orientation/local-factor product law。 | `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭 small-to-large factor-peeling signed-state 边界；未证明三命题无条件闭合。 | `PrimitiveOrientationLocalFactorProductLawBeforePushforward OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` |

## 3. 最大样本细节

`N=30030` 的最大深度样本：

```text
n=16384, owner_p=2, cofactor=8192, factor_word=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
n=24576, owner_p=2, cofactor=12288, factor_word=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
```

最常见第一剥离因子：

```text
2:7507, 3:4171, 5:2069, 7:1346, 11:790, 13:644, 17:478, 19:424
```

## 4. 最新开放口

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

严格全局基底仍保留：

```text
(BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance) OR (PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger)
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_small_to_large_factor_peeling_signed_state_boundary_router.py` | `04baba0be9da0933d5e3faa6774783ff18dcbde50c45888048c5e3c89d20e784` |
| `docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json` | `f976e98574efb9522fb37341b9a8c62636a0903fd569f118e9059a361245acc4` |
| `docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json` | `c4346bdf5a7500f4d6c50f9abd0255bd916ff288dcae000cd2caa87434f38392` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json` | `7c76acab60f95b655941cb563439aca48116d80cd4dc1733a0210d96e4a45fb0` |
| `docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.json` | `78cda26ba38bcf8446f487c7c7f723e4b14766d2d66f4e8d788ba962c698441e` |
| `docs/monograph/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.json` | `d46484521bd8b12fd648f9b2278a36d86a84be4ac7bf56c1d35c1a761fe726fd` |

行/列命题仍未无条件闭合。
