# Prime Matrix strict 同 formal-unit 核恒等式攻坚路由器

**状态：** `same_formal_unit_kernel_identity_reduced_to_pointwise_primitive_kernel_table_open`

本步直接攻核恒等式本身。已有 formal unit 抽取、finite key、source record 和 no-loss 账本，可以保证任意假设 witness 的对象被同一账本命名且不丢失；但这些账本不含 alpha/delta 的逐点 signed coefficient value。几何 Phi、解积分和 exact-UV 分散都需要同一张 primitive 核表来对齐。因此真正最窄破坏输入继续压缩为逐点同 formal-unit primitive alpha/delta 核表，而当前仍未闭合。

```text
kernel_identity_attack_router_closed=true
bridge_fields_closed=true
formal_unit_no_loss_available=true
source_tuple_container_available=true
reverse_source_recovery_blocked=true
zero_row_unsigned_recovery_blocked=true
pointwise_primitive_kernel_table_proved=false
same_formal_unit_kernel_identity_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 压缩等价

SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion 不能由 formal-unit 记录守恒、几何 Phi 基底或 signed 解积分形式自动推出；它等价于先提交 `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate`：逐 primitive row 给出 source tuple、signed weight、exact `(u,v)`、Phi atom、local factor 非零、rank/multiplicity 证书和命名回流。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `KernelIdentityTargetActive` | `true` | `false` | 上一层已把非递归破环包压成同 formal-unit pre-Cauchy alpha/delta 核恒等式。 | SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion |
| `FormalUnitExtractionAndNoLossAvailable` | `true` | `true` | 任意假设 witness 可被分割成有限 formal units，且义务不丢失。 | 这只保证记录守恒，不给 signed coefficient value。 |
| `SourceTupleContainerAvailableButNotCoefficient` | `true` | `true` | source tuple/anchor 参数字段和哈希纪律可用。 | 容器字段不能替代 primitive row 发射公式或 signed 权重公式。 |
| `PrimitiveRuleStillNeedsEmissionAndWeight` | `true` | `false` | alpha 侧 primitive rule 已拆成定义域、发射映射、权重公式、输出字段和回流。 | 缺少逐 primitive row 的显式发射和系数权重。 |
| `EmissionMapOpenAtAnchorPhaseFormula` | `true` | `false` | 确定性发射映射已排除 downstream/payment 反选。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| `WeightLawOpenAtIndependentArithmeticIdentity` | `true` | `false` | signed 权重律已排除零行几何和 payment 反推。 | IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger |
| `DisintegrationFormalButNeedsPointwiseTable` | `true` | `false` | 给定 signed source 后，逐纤维解积分只是形式闭合。 | 必须先有逐 primitive row 核表，才能做 Phi 推前求和。 |
| `PhiGeometryDoesNotCreateEquality` | `true` | `false` | 几何 Phi/payment base 和预算形状已知。 | Phi_*nu 等于 payment-side 系数仍需要逐点核表求和证明。 |
| `ExactUVDispersionStillNeedsSameTableRank` | `true` | `false` | ExactUV fiber 分散已压到 primitive emitter multiplicity。 | 没有同一 primitive key 表，就无法把 rank/multiplicity 证书与 signed source 对齐。 |
| `ReverseSourceAndZeroRowRecoveryBlocked` | `true` | `true` | 不能从 downstream payment skeleton 或早期零行 unsigned cover 反推 source。 | 核表必须正向提交，不能后验恢复。 |
| `KernelIdentityCurrentCorpusProved` | `false` | `false` | 当前材料没有逐 primitive row 的同 formal-unit alpha/delta 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |

## 3. 逐点核表字段

| field | requirement |
| --- | --- |
| `formal_unit_id` | 锁定同一 witness/formal unit，不允许 source、Phi、fiber 分别换口径。 |
| `primitive_row_id` | alpha/delta primitive row 的规范索引和排序，发射前确定。 |
| `source_tuple_hash` | 连接 source tuple、anchor 参数、branch path 和 local factor。 |
| `signed_weight` | 由 pre-Cauchy 算术恒等式给出，不由零行覆盖或 payment 反推。 |
| `uv_map` | 逐行输出 exact `(u,v)`，并与后续 fiber 分散同口径。 |
| `phi_atom` | 逐行给出 Phi/payment atom，含端点、重数、符号口径。 |
| `local_factor_nonzero` | 证明 local factor 非零；失败必须命名回流。 |
| `rank_or_multiplicity_certificate` | 对同一 `(u,v)`/fiber 给出 rank、bounded multiplicity 或分散证书。 |
| `return_tag` | 字段缺失、超预算、Phi 不等、rank 坍缩、canonical 泄漏均登记命名出口。 |

## 4. 下一真正最窄点

```text
PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
```
