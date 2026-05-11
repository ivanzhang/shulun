# Prime Matrix strict acyclic seed source tuple word constructor 路由器

**状态：** `source_tuple_word_constructor_reduced_to_basis_word_formula_open`

本步把 source tuple -> primitive basis word constructor 继续压到 basis_word_formula。现有账本已经锁定输入参数，但没有把 A、D0/K/Omega、phase_rule 等参数变成 primitive basis word 的算术公式；下游 unsigned skeleton、alpha/delta rule 和 payment/零行反推都不能补这个公式。

```text
source_tuple_word_constructor_router_closed=true
input_source_tuple_closed=true
basis_word_formula_from_source_tuple_parameters_proved=false
source_tuple_to_primitive_basis_word_constructor_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility` 的输入 source tuple 已有字段和哈希纪律；真正首缺口是 `AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility`。也就是说，需要一条只读取 source tuple 参数、发生在 Cauchy/payment 前、能输出 primitive basis word 坐标的公式。

## 2. basis_word_formula 字段

| field | meaning |
| --- | --- |
| `parameter_domain` | 公式允许读取的 source tuple 字段：A、D0、K、Omega、phase_rule、窗口端点和 formal_unit_id。 |
| `word_coordinate_formula` | 把 source tuple 参数变成 primitive basis word 坐标的闭式公式或确定性递推。 |
| `arithmetic_weight_slot` | word 中承载 signed local factor、筛权来源和截断层的槽位。 |
| `no_post_payment_input` | 公式不得读取 Cauchy、dispersion、payment、零行覆盖或 terminal extraction 后的数据。 |
| `formula_failure_return` | 公式未定义、多值、读到后验数据或跨作用域时的命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SourceTupleWordConstructorTargetActive` | `true` | `false` | 上一层已把 primitive basis word 生成规则压到 source tuple 到 word constructor。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `InputSourceTupleClosed` | `true` | `true` | formal unit/source tuple 的输入字段、锚集合、D0/K/Omega、phase_rule 与 hash 已锁定。 | 输入对象不是当前首缺口。 |
| `BasisWordFormulaIsFirstOpenField` | `true` | `true` | constructor 的真正首字段是 basis_word_formula；没有公式，pre-Cauchy 顺序证书和唯一性都无对象。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `SchemaParametersAreNotFormula` | `true` | `false` | A、D0、K、Omega、phase_rule 是参数，不是从参数到 primitive basis word 的算术映射。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `SourceLawSpecificationNotFormula` | `true` | `false` | pre-Cauchy source law 规定必须有来源公式和回流纪律，但不提供 word_coordinate_formula。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `ActualNoncanonicalConstructorFormulaStillMissing` | `true` | `false` | actual noncanonical primitive constructor formula/admission 尚未证明，不能推出 basis word formula。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `DownstreamRowAndAlphaDeltaRulesCannotDefineFormula` | `true` | `false` | unsigned row skeleton 与 alpha/delta rule 都在 word 或 primitive row 已生成后使用，不能倒置成 formula。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `PostPaymentAndZeroRowInputsRejected` | `true` | `true` | basis_word_formula 不能读 payment 原像、推前后投影或早期零行覆盖，否则是后验选择循环。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `BasisWordFormulaFromSourceTupleParametersCurrentCorpusProved` | `false` | `false` | 当前材料没有提交从 source tuple 参数到 primitive basis word 坐标的闭式公式或确定性递推。 | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| `SourceTupleToPrimitiveBasisWordConstructorCurrentCorpusProved` | `false` | `false` | 没有 basis_word_formula，constructor 的顺序证书、非后验唯一性和失败回流仍未合取闭合。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |

## 4. 下一真正单点

```text
AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility
```

并行依赖：

```text
AcyclicSeedPreCauchyOrderCertificateForBasisWordFormula
AcyclicSeedNonposthocWordConstructorUniquenessLedger
AcyclicSeedWordConstructorFailureReturnLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
