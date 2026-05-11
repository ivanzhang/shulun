# Prime Matrix strict acyclic seed primitive coefficient law 路由器

**状态：** `acyclic_seed_primitive_coefficient_law_reduced_to_basis_weight_source_open`

本步把 acyclic seed primitive row signed coefficient law 压到最前置字段：seed 内部 pre-Cauchy basis weight 来源公式。unsigned skeleton、branch key、ExactUV、解积分和 payment 原像选择都只能在系数给定后验证，不能生成该来源公式。当前材料没有这条 basis weight source formula，所以仍未得到无条件终端矛盾。

```text
acyclic_seed_primitive_coefficient_law_router_closed=true
acyclic_seed_precauchy_basis_weight_source_formula_proved=false
acyclic_seed_primitive_row_signed_coefficient_law_proved=false
acyclic_seed_signed_row_emitter_rule_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward 的首个不可替代字段是 `AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows`。没有 basis weight source，sign/local factor、变差收费和推前前求和恒等式都不能成为数学陈述。

## 2. coefficient law 拆分

| component | role | status |
| --- | --- | --- |
| `basis_weight_source` | 给出 seed 内部的 pre-Cauchy 算术基函数/筛权来源。 | first open component |
| `sign_rule` | 由 basis weight 与 branch key 决定每行符号。 | depends on basis_weight_source |
| `local_factor_rule` | 给出 local factor 闭式公式、非零条件和失败回流。 | depends on basis_weight_source |
| `truncation_phase_charge` | 登记截断、相位过滤和 signed branch 变差收费。 | depends on row coefficient value |
| `alpha_delta_prepushforward_sum_identity` | 证明 primitive rows 在推前前求和等于 actual alpha/delta 系数。 | depends on all previous components |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrimitiveCoefficientLawTargetActive` | `true` | `false` | 上一层已把合法 seed 分支内的 signed row emitter 压到 primitive row signed coefficient law。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| `CoefficientLawDecomposed` | `true` | `true` | signed coefficient law 可拆为 basis weight source、sign/local factor、收费和推前前求和恒等式。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `BasisWeightSourceIsFirstOpenComponent` | `true` | `true` | 没有 seed 内部 pre-Cauchy basis weight 来源，后续符号、local factor 和求和恒等式无从定义。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `AlphaSignedWeightLawStillOpen` | `true` | `false` | alpha signed weight law 仍缺 exact formula 与独立 pre-Cauchy 算术恒等式。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `AlphaPrimitiveCoefficientFormulaStillOpen` | `true` | `false` | alpha primitive rule 仍缺 primitive coefficient weight formula。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `PointwisePrimitiveExpressionStillOpen` | `true` | `false` | 逐行 signed weight 公式仍缺 primitive summand 推前前表达式。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `SignedValueTableStillOpen` | `true` | `false` | signed lift 仍缺逐 skeleton row signed value table。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `UnsignedSkeletonCannotSupplyBasisWeight` | `true` | `true` | unsigned skeleton 只给几何 row 位置和相位字母表，不含 basis weight 来源。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `KeyAndDisintegrationAreAfterCoefficient` | `true` | `false` | branch key、ExactUV 和解积分只能在 signed coefficient 已登记后验证。 | 不能反向生成 basis weight source。 |
| `ReverseRecoveryBlocked` | `true` | `true` | 不能从早期零行覆盖或 payment 原像选择反推 basis weight source。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `AcyclicSeedPreCauchyBasisWeightSourceFormulaCurrentCorpusProved` | `false` | `false` | 当前材料没有给出 seed 内部的 pre-Cauchy basis weight 来源公式。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| `AcyclicSeedPrimitiveRowSignedCoefficientLawCurrentCorpusProved` | `false` | `false` | 没有 basis weight 来源公式，primitive row signed coefficient law 仍未证明。 | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |

## 4. 下一真正单点

```text
AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
