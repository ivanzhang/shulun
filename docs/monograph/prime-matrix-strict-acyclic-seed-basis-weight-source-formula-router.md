# Prime Matrix strict acyclic seed basis weight source formula 路由器

**状态：** `acyclic_seed_basis_weight_source_reduced_to_internal_arithmetic_basis_expansion_open`

本步把 basis weight source formula 继续压到 seed 内部 pre-Cauchy 算术基展开。这张展开必须给出 basis alphabet、coefficient assignment、截断/相位层规则、noncanonical 作用域证书、推前前恒等式和失败回流。当前材料没有该内部基展开，因此当前仍只是更精确地定位破坏输入，还没有形成无条件矛盾。

```text
acyclic_seed_basis_weight_source_formula_router_closed=true
acyclic_seed_internal_arithmetic_basis_expansion_proved=false
acyclic_seed_precauchy_basis_weight_source_formula_proved=false
acyclic_seed_primitive_row_signed_coefficient_law_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows 不能从 canonical、generic WFD、外部谱、零行覆盖、payment 原像或 source tuple 容器导出；它必须提交 `AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy`。

## 2. 内部算术基展开字段

| field | meaning |
| --- | --- |
| `basis_alphabet` | seed 内部允许的 pre-Cauchy 算术基函数/筛权字母表。 |
| `coefficient_assignment` | 每个 basis word 到 primitive row signed coefficient 的赋值公式。 |
| `truncation_layer_rule` | 截断层、相位层和 branch layer 的确定性规则。 |
| `noncanonical_scope_certificate` | 证明该展开属于 actual noncanonical seed，不偷用 canonical RIW/Buchstab。 |
| `pre_cauchy_identity` | 展开在 Cauchy/dispersion/Phi 前已经等于目标 alpha/delta 系数。 |
| `failure_return` | 缺字母、零赋值、作用域冲突或超预算时命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BasisWeightSourceTargetActive` | `true` | `false` | 上一层已把 primitive coefficient law 压到 seed 内部 basis weight source formula。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `BasisSourceRequiresInternalArithmeticExpansion` | `true` | `true` | basis weight source 不能只是 source tuple 字段名；必须给出 seed 内部 pre-Cauchy 算术基展开。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `CanonicalRIWNotImportable` | `true` | `true` | canonical RIW/Buchstab 只在 canonical-source 分支内有作用域，不能跨入 actual noncanonical seed。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `GenericWFDNotBasisSource` | `true` | `true` | generic WFD 或形式 well-factorable 条件不是 primitive row 的原始 basis weight source。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `ExternalSpectralDoesNotEmitBasis` | `true` | `true` | 外部谱估计处理给定系数后的平均，不生成 seed 内部 basis expansion。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `ZeroRowAndPaymentReverseBlocked` | `true` | `true` | 早期零行覆盖和 payment 原像都不能反向产生 basis expansion。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `FormalUnitSourceTupleContainersInsufficient` | `true` | `false` | formal-unit/source-tuple 容器只给参数与哈希，不给 basis alphabet 或 coefficient assignment。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `UnsignedSkeletonInsufficientForBasisExpansion` | `true` | `false` | unsigned row skeleton 可定位候选几何行，但不定义 seed 的算术基展开。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `AcyclicSeedInternalArithmeticBasisExpansionCurrentCorpusProved` | `false` | `false` | 当前材料没有提交 actual noncanonical seed 的内部 pre-Cauchy 算术基展开。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `BasisWeightSourceFormulaCurrentCorpusProved` | `false` | `false` | 没有内部算术基展开，basis weight source formula 仍未证明。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |

## 4. 下一真正单点

```text
AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
