# Prime Matrix strict acyclic seed primitive basis word generation 路由器

**状态：** `primitive_basis_word_generation_reduced_to_source_tuple_word_constructor_open`

本步把最新真正单点再压到 source tuple -> primitive basis word constructor。现有 formal-unit/source-tuple 只能登记参数，unsigned skeleton 只能在 word 已有时给几何锚，零行/payment/推前后反选已被 no-go 阻断；因此 constructor 仍是未闭合的自足输入。

```text
primitive_basis_word_generation_router_closed=true
source_tuple_to_primitive_basis_word_constructor_proved=false
primitive_basis_word_set_generation_rule_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment` 的第一可检验字段是 `AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility`：必须先有 source tuple 到 primitive basis word 的 pre-Cauchy 正向构造，再谈准入谓词、row anchor、复杂度收费和 coefficient assignment。

## 2. constructor 字段

| field | meaning |
| --- | --- |
| `input_source_tuple` | 同一 formal unit 下的 actual noncanonical seed/source tuple。 |
| `basis_word_formula` | 由 source tuple 参数正向产生 primitive basis word 的闭式公式或递推规则。 |
| `pre_cauchy_order_certificate` | 证明该构造发生在 Cauchy、dispersion、payment 和 terminal extraction 之前。 |
| `nonposthoc_uniqueness` | 排除从零行覆盖、payment 原像或推前后投影反选 word。 |
| `constructor_failure_return` | source tuple 无法生成 word、生成多值或作用域冲突时的命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrimitiveBasisWordGenerationTargetActive` | `true` | `false` | 上一层已把 basis alphabet 账本压到 primitive basis word set generation rule。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `WordConstructorPrecedesPredicateAndAnchor` | `true` | `true` | admissible predicate、row anchor、复杂度收费和缺字母回流都以已生成的 word 为定义域。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `SourceTupleAvailableButNoConstructor` | `true` | `false` | source tuple 可登记参数，但当前没有从这些参数到 primitive basis word 的正向公式。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `PreCauchySourceLawIsSpecificationNotConstructor` | `true` | `false` | pre-Cauchy source law 说明需要哪些字段，但没有给出 basis_word_formula。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `ActualPrimitiveConstructorStillMissing` | `true` | `false` | actual noncanonical primitive constructor/admission 未证明，因此不能自动产生 word constructor。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `UnsignedSkeletonOnlyAnchorsAfterWord` | `true` | `false` | unsigned skeleton 可在 word 已有时提供几何锚；不能构造带算术权重的 word。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `RowOriginTableMissing` | `true` | `false` | primitive summand 来源恒等式和逐行原始生成表仍未证明，不能作为 constructor 证据。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `PosthocReverseSelectionBlocked` | `true` | `true` | 从 payment、推前后投影或早期零行覆盖反选 word 已被既有 no-go 与 reverse firewall 阻断。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `SourceTupleToPrimitiveBasisWordConstructorCurrentCorpusProved` | `false` | `false` | 当前材料没有提交 source tuple 到 primitive basis word 的 pre-Cauchy 正向构造。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `PrimitiveBasisWordSetGenerationRuleCurrentCorpusProved` | `false` | `false` | 没有 word constructor，generation rule 的其余字段都只能悬空。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |

## 4. 下一真正单点

```text
AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility
```

并行依赖：

```text
AcyclicSeedBasisWordAdmissibilityPredicateLedger
AcyclicSeedWordToRowAnchorCompatibilityLedger
AcyclicSeedBasisWordComplexityAndMissingReturnLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
