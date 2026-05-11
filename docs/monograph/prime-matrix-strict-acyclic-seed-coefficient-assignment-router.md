# Prime Matrix strict acyclic seed coefficient assignment 路由器

**状态：** `coefficient_assignment_reduced_to_basis_word_value_map_formula_open`

本步把 coefficient assignment 压到 value map formula。锚/相位/截断输入已经闭合，问题不再是找到 word，而是给每个 word 赋 signed coefficient；这个赋值不能由 payment、零行覆盖或下游解积分反推。

```text
coefficient_assignment_router_closed=true
geometric_basis_word_domain_closed=true
basis_word_to_signed_coefficient_value_map_formula_proved=false
acyclic_seed_coefficient_assignment_on_basis_alphabet_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. assignment 字段

| field | meaning |
| --- | --- |
| `assignment_domain` | 已生成的 actual noncanonical primitive basis words。 |
| `value_map_formula` | 每个 basis word 到 signed coefficient 的赋值公式。 |
| `sign_local_factor_projection` | 从赋值公式投影出 sign、local factor 和非零条件。 |
| `basis_source_compatibility` | 赋值公式与 seed pre-Cauchy basis weight source 是同一对象。 |
| `failure_return` | 无定义、零因子、符号冲突、超预算或作用域冲突时的回流。 |

## 2. 前沿压缩

`AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger` 的第一开口是 `AcyclicSeedBasisWordToSignedCoefficientValueMapFormula`。几何 basis word 域已可用，但 signed assignment 必须给出 word -> coefficient 的具体赋值公式。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CoefficientAssignmentTargetActive` | `true` | `false` | 上一层已把 signed slot value formula 压到 coefficient assignment。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `GeometricBasisWordDomainClosed` | `true` | `true` | anchor/dyadic/phase 输入域已经闭合；可作为 assignment 的 unsigned domain。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `BasisAlphabetDomainStillNeedsSignedValue` | `true` | `false` | noncanonical basis alphabet 的 signed/local-factor 层仍依赖 coefficient assignment 自身。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `ValueMapFormulaIsFirstOpenField` | `true` | `true` | assignment 的第一不可替代字段是 basis word 到 signed coefficient 的 value map formula。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `ExistingPointwiseValueRoutesStillOpen` | `true` | `false` | 逐点 signed value table、非递归 signed weight 公式和 basis coefficient assignment 均未证明。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `BasisSourceAndCoefficientLawStillOpen` | `true` | `false` | basis weight source 与 primitive row signed coefficient law 仍缺赋值公式支撑。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `ReverseAssignmentRecoveryBlocked` | `true` | `true` | 不能从 payment、推前后投影或早期零行覆盖反推出 value map formula。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `BasisWordToSignedCoefficientValueMapFormulaCurrentCorpusProved` | `false` | `false` | 当前材料没有给出 actual noncanonical basis word 到 signed coefficient 的赋值公式。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `CoefficientAssignmentOnBasisAlphabetCurrentCorpusProved` | `false` | `false` | 没有 value map formula，coefficient assignment 仍未证明。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |

## 4. 下一真正单点

```text
AcyclicSeedBasisWordToSignedCoefficientValueMapFormula
```

并行依赖：

```text
AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows
PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
