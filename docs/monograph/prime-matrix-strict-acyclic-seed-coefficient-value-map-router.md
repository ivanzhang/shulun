# Prime Matrix strict acyclic seed coefficient value map 路由器

**状态：** `coefficient_value_map_reduced_to_basis_word_origin_identity_open`

本步把 basis word -> signed coefficient value map 压到来源恒等式。换言之，必须正向说明每个 basis word 的 signed coefficient 从哪个同 formal-unit pre-Cauchy source tuple 生成，并在推前之前等于 alpha/delta 贡献；当前材料没有这条恒等式。

```text
coefficient_value_map_router_closed=true
value_map_must_be_origin_identity=true
basis_word_signed_coefficient_origin_identity_proved=false
basis_word_to_signed_coefficient_value_map_formula_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 来源恒等式字段

| field | meaning |
| --- | --- |
| `origin_source_tuple` | 产生该 basis word/signed coefficient 的同 formal-unit pre-Cauchy source tuple。 |
| `signed_coefficient_expression` | signed coefficient 的正向表达式，含筛权、符号、branch/local factor。 |
| `origin_to_basis_word_identity` | 证明来源表达式生成的对象正是该 primitive basis word。 |
| `prepushforward_equality` | 证明在 Phi/payment/Cauchy 推前之前已等于目标 alpha/delta 贡献。 |
| `return_tag` | 来源缺失、零因子、符号冲突或后验依赖时的命名回流。 |

## 2. 前沿压缩

`AcyclicSeedBasisWordToSignedCoefficientValueMapFormula` 继续压到 `AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward`：signed coefficient 的 value map 必须是 pre-Cauchy 来源恒等式，而不是后验赋值表。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CoefficientValueMapTargetActive` | `true` | `false` | 上一层已把 coefficient assignment 压到 basis word -> signed coefficient value map formula。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `ValueMapMustBeOriginIdentity` | `true` | `true` | value map 不能只是赋值符号；必须说明 signed coefficient 从哪个 pre-Cauchy 来源恒等式生成。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `PrimitiveSummandOriginRouteStillOpen` | `true` | `false` | primitive summand signed expression 已被压到来源恒等式，但来源恒等式仍未证明。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `RowLevelOriginGenerationTableStillOpen` | `true` | `false` | 逐行原始生成表仍未证明，不能给出 value map 的来源行。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `PointwiseSignedWeightRoutesStillOpen` | `true` | `false` | 逐点 signed value table 和 signed weight expression 仍未证明。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `BasisSourceStillOpen` | `true` | `false` | basis weight source formula 仍未证明；value map 缺其算术来源。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `ReverseOriginRecoveryBlocked` | `true` | `true` | 不能从 payment、推前后投影或早期零行覆盖反推 signed coefficient 来源。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `BasisWordSignedCoefficientOriginIdentityCurrentCorpusProved` | `false` | `false` | 当前材料没有给出每个 basis word 的 signed coefficient pre-Cauchy 来源恒等式。 | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `BasisWordToSignedCoefficientValueMapFormulaCurrentCorpusProved` | `false` | `false` | 没有来源恒等式，value map formula 仍未证明。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |

## 4. 下一真正单点

```text
AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward
```

并行依赖：

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows
PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
