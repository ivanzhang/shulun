# Prime Matrix strict primitive summand 来源恒等式路由器

**状态：** `primitive_summand_origin_identity_reduced_to_row_level_origin_generation_table_open`

本步把 signed coefficient 来源恒等式继续压到逐行 clean-core 原始生成表。如果该表存在，来源恒等式、exact signed weight、constructor row 输出和推前前求和恒等式同时得到；但当前材料仍只给 formal-unit/source-tuple 容器和 unsigned skeleton，没有 signed coefficient 的逐行来源表。

```text
primitive_summand_origin_identity_router_closed=true
row_level_clean_core_origin_generation_table_proved=false
primitive_summand_signed_coefficient_origin_identity_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward 等价于提交 `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands`：在同一 formal unit 内列出 actual noncanonical primitive summand 的逐行原始生成表。已有 unsigned skeleton 只能给几何行，不能给 signed coefficient。

## 2. 逐行原始生成表字段

| field | meaning |
| --- | --- |
| `formal_unit_id` | 锁定同一反例 witness 的 formal unit。 |
| `source_tuple_hash` | 锁定 pre-Cauchy source tuple 与 anchor 参数。 |
| `primitive_row_index` | 给出 alpha/delta primitive summand 的有限行索引。 |
| `signed_coefficient` | 逐行 signed coefficient 的正向公式。 |
| `sign_local_factor` | 符号与 local factor 非零证明，失败则命名回流。 |
| `uv_branch_key` | 同步输出 exact `(u,v)` 与 branch key。 |
| `prepushforward_sum_identity` | 这些行在 Phi/payment 推前前求和等于 actual alpha/delta 系数。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OriginIdentityTargetActive` | `true` | `false` | 上一层已把 primitive summand signed expression 压成 signed coefficient 来源恒等式。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |
| `OriginIdentityIsRowLevelOriginGeneration` | `true` | `true` | 若存在 clean-core 原始生成账本，其逐行限制即可给出来源恒等式。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `PrepushforwardEmitterAlreadyPointsToOriginLedger` | `true` | `true` | pre-pushforward emitter origin ledger 已把同一缺口指向原始生成账本。 | 但未给逐行表。 |
| `SourceLoopSelfProofCut` | `true` | `true` | origin ledger、formula、emitter、payment 之间的循环来源证明已被切断。 | 不能由来源环自证逐行生成表。 |
| `FormalUnitAndSourceTupleContainersReady` | `true` | `true` | formal unit/source tuple/anchor 参数容器可用。 | 容器不产生 signed coefficient。 |
| `UnsignedSkeletonReadyButNotSignedOrigin` | `true` | `false` | carry-shell、P列锚和 layered-wheel 已给 unsigned row skeleton。 | 仍需 signed coefficient 来源表。 |
| `ExternalAndReverseRoutesRejected` | `true` | `true` | 外部谱、payment 反推和早期零行覆盖都不能生成逐行 signed origin。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `CleanCoreOriginalGenerationLedgerCurrentCorpusProved` | `false` | `false` | 当前 clean-core 原始生成账本仍未证明。 | CleanCoreOriginalCoefficientGenerationLedgerAndReturn。 |
| `RowLevelOriginTableCurrentCorpusProved` | `false` | `false` | 当前材料没有逐 actual noncanonical primitive summand 的原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `PrimitiveSummandOriginIdentityCurrentCorpusProved` | `false` | `false` | 没有逐行原始生成表，signed coefficient 来源恒等式仍未证明。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |

## 4. 下一真正单点

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```
