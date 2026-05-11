# Prime Matrix strict acyclic seed basis word origin identity 路由器

**状态：** `basis_word_origin_identity_reduced_to_row_level_generation_table_open`

本步把 basis word signed coefficient 来源恒等式接回统一原始生成表。几何 word 和 source tuple 已经命名，但 signed coefficient 的来源必须由逐行 clean-core 原始生成表给出；当前材料仍没有该表。

```text
basis_word_origin_identity_router_closed=true
basis_word_origin_equals_row_level_generation=true
row_level_clean_core_origin_generation_table_proved=false
basis_word_signed_coefficient_origin_identity_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 原始生成表字段

| field | meaning |
| --- | --- |
| `basis_word_id` | 由已闭合几何坐标产生的 primitive basis word 编号。 |
| `origin_source_tuple` | 同 formal-unit pre-Cauchy 来源 tuple。 |
| `signed_coefficient` | 该 basis word/primitive summand 的 signed coefficient 正向公式。 |
| `branch_key_uv_sign_local_factor` | branch key、u/v map、sign、local factor 和非零条件。 |
| `prepushforward_sum_identity` | 推前前求和等于目标 alpha/delta 系数贡献。 |
| `return_tag` | 缺来源、零因子、超预算、后验依赖或作用域冲突时的回流。 |

## 2. 前沿压缩

`AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward` 与既有 primitive summand 来源恒等式会合；真正共同剩余是 `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands`。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BasisWordOriginIdentityTargetActive` | `true` | `false` | 上一层已把 basis word value map 压到 signed coefficient 来源恒等式。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `ContainersAndGeometricWordsAvailable` | `true` | `true` | formal-unit/source-tuple 和几何 basis word 输入已闭合。 | 但它们不产生 signed coefficient。 |
| `BasisWordOriginEqualsRowLevelGeneration` | `true` | `true` | basis word 来源恒等式与 primitive summand 来源恒等式是同一需求：逐行原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowLevelGenerationTableStillOpen` | `true` | `false` | 当前材料没有逐 basis word/primitive summand 的 signed coefficient 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `AcyclicSignedEmitterStillOpen` | `true` | `false` | 无环 seed signed row emitter 仍缺 primitive row signed coefficient law。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SourceLoopAndReverseRecoveryBlocked` | `true` | `true` | 不能用来源循环、payment 反推或早期零行 unsigned cover 生成来源恒等式。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowLevelCleanCoreOriginalCoefficientGenerationTableCurrentCorpusProved` | `false` | `false` | 当前材料尚未提交 actual noncanonical primitive summands 的逐行原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `BasisWordSignedCoefficientOriginIdentityCurrentCorpusProved` | `false` | `false` | 没有逐行原始生成表，basis word signed coefficient 来源恒等式仍未证明。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |

## 4. 下一真正单点

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

并行依赖：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
