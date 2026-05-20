# Prime Matrix row-origin table to Phi-LPF bucket signed-law sync 证书

**状态：** `row_origin_table_reduced_to_phi_lpf_bucket_signed_law_open`

本步把最新的逐行 clean-core origin table 硬点接入 LPF/Phi 支撑剥离证书。Row-level 表不能从来源环自证；固定点切断后必须给 noncircular pre-Cauchy signed kernel。而 LPF/Phi 已经把该 kernel 的无符号支撑、owner layer 与容量全部剥离为 `(p,m)` 桶，所以最新真正硬点不再是找行或数行，而是 `PhiLPFBucketSignedCoefficientLawBeforePushforward`。该 signed law 仍未证明，行/列命题仍未无条件闭合。

```text
row_level_origin_table_imported=true
row_table_requires_seed_emitter=true
signed_source_fixed_point_cut_imported=true
noncircular_kernel_imported=true
phi_lpf_support_stripping_imported=true
phi_lpf_support_and_capacity_closed=true
row_origin_table_reduced_to_phi_lpf_bucket_signed_law=true
phi_lpf_bucket_signed_coefficient_law_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFBucketSignedCoefficientLawBeforePushforward
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` | `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity` | 逐行 clean-core 原始生成表必须由 Cauchy 前 seed signed-row emitter 正向产生。 |
| `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity` | `NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows` | signed-source 固定点切断后，emitter 不能从来源环恢复，必须给非循环 signed coefficient 发射核。 |
| `NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows` | `PhiLPFPrimitiveRowSupportAndCapacityLedger AND PhiLPFBucketSignedCoefficientLawBeforePushforward` | LPF/Phi 已剥离无符号支撑和容量，剩余是每个 `(p,m)` 桶上的 signed law。 |
| `PhiLPFPrimitiveRowSupportAndCapacityLedger` | `closed unsigned support/capacity` | 最小素因子桶和 Phi 递推支付 support key、owner layer、capacity 和 p>sqrt(N) 零质量。 |
| `PhiLPFBucketSignedCoefficientLawBeforePushforward` | `latest direct hardpoint` | 必须正向给 signed coefficient、sign/local factor、branch key 与推前前 alpha/delta 求和恒等式。 |

## 2. LPF/Phi 支撑快照

| N | pi(N) | composites | support keys | bijection |
| ---: | ---: | ---: | ---: | --- |
| 30 | 10 | 19 | 19 | `true` |
| 100 | 25 | 74 | 74 | `true` |
| 997 | 168 | 828 | 828 | `true` |
| 5003 | 670 | 4332 | 4332 | `true` |
| 10000 | 1229 | 8770 | 8770 | `true` |

## 3. 桶级 signed law 合同

| field | meaning |
| --- | --- |
| `bucket_key` | 已闭合 LPF/Phi support key `(p,m)`，其中 `p=LPF(pm)` 且 `m` 为 p-rough。 |
| `signed_coefficient_formula` | 不读取 payment/origin table 的 Cauchy 前 signed coefficient 正向公式。 |
| `sign_local_factor_nonzero` | 符号、local factor、非零条件和零因子命名回流。 |
| `alpha_delta_branch_key` | 同步输出 alpha/delta side、branch key 和 exact `(u,v)`。 |
| `prepushforward_sum_identity` | 全部桶级 signed rows 在 Phi/payment 推前前已经求和为 actual alpha/delta 贡献。 |
| `same_formal_unit_mass_check` | 与 row-mass/no-heavy-row 账本同口径登记，不能由桶容量自动推出。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RowOriginTableFrontierImported | `true` | `false` | 上一层已把 Phi-LPF signed-survival 的 signed expression 缺口同步到逐行 clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| RowTableRequiresSeedEmitterImported | `true` | `false` | strict row-level 证书说明 row table 必须由无环 pre-Cauchy seed signed-row emitter 产生。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| SignedSourceFixedPointCutImported | `true` | `true` | row-level 表、来源恒等式、basis word 和 signed assignment 构成固定点，不能自证 signed coefficient。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| NoncircularKernelImported | `true` | `false` | 固定点切断后，真正入口是 Cauchy 前 noncircular signed coefficient emission kernel。 | NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows |
| PhiLPFSupportStrippingImported | `true` | `false` | support-stripped 证书已把 noncircular kernel 拆成已闭合 support/capacity 与未闭合 signed law。 | PhiLPFPrimitiveRowSupportAndCapacityLedger AND PhiLPFBucketSignedCoefficientLawBeforePushforward |
| PhiLPFSupportAndCapacityClosed | `true` | `true` | LPF 唯一 ownership 与 Phi 递推已经支付 `(p,m)` support key、候选容量和 owner layer。 | PhiLPFPrimitiveRowSupportAndCapacityLedger |
| UnsignedBucketCannotEmitSignedLaw | `true` | `true` | LPF/Phi 桶只含无符号支撑和容量，不含 signed coefficient、local factor、orientation 或推前前恒等式。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| RowOriginTableReducedToPhiLPFBucketSignedLaw | `true` | `false` | 逐行 origin table 的找行/数行部分已被 Phi-LPF 剥离；剩余正是桶级 signed coefficient law。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| PhiLPFBucketSignedLawCurrentCorpusProved | `false` | `false` | 当前材料仍没有对每个 `(p,m)` support key 正向赋 signed coefficient 与 sign/local factor。 | PhiLPFBucketSignedCoefficientLawBeforePushforward |
| RowMassStillIndependent | `true` | `false` | 即使 signed law 提交，same-formal-unit row-mass/no-heavy-row 仍需同口径账本。 | SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只同步 hardpoint 并剥离 LPF/Phi 无符号部分；不证明 signed law、row mass、complete key、fixed-key multiplicity 或终端排斥。 | PhiLPFBucketSignedCoefficientLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |

## 5. 最新保留基

```text
(PhiLPFBucketSignedCoefficientLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate; parallel: CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_row_origin_table_phi_lpf_bucket_law_sync_router.py` | `d3e42d424bea5285fc9d1d0dca9a663a83141a7e228c7ae1ffa48c7f35e7e4a2` |
| `docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json` | `2a1b6082621d0c9d8ddd1acfa69d12f9c3f3a38cebe422ba3d14b196661b5a30` |
| `docs/monograph/prime-matrix-strict-row-level-origin-generation-table-router.json` | `a9ac8a47342465ed4499d5ca8540fc54b5072d82c4bfba2d53c17b5b2d7e4a78` |
| `docs/monograph/prime-matrix-strict-signed-source-fixed-point-breaker-router.json` | `a07743b021b11f13f19d791fc43d4268f551878c43f3340bd54664254311185f` |
| `docs/monograph/prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json` | `96d6dadbc5add815f8623295aae5ae519c0b5e44db556d85d657259db97a9773` |
| `docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json` | `c19cac4502bc4a62202e18d136493e2820c11590c92a20ba40f590c7aa7216b4` |
| `docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json` | `d916331b1d8bea632d161cbe99fe4500813feb8333bf0463e4de5767bbf3a81c` |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
