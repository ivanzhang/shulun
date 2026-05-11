# Prime Matrix strict acyclic seed signed slot value formula 路由器

**状态：** `signed_slot_value_formula_reduced_to_coefficient_assignment_open`

本步把 signed slot value formula 压到 coefficient assignment。几何 primitive word 域已经可用，但该域没有 signed 赋值；现有 basis source、basis alphabet、逐点 signed value table 都仍未闭合，且 payment/零行反推被阻断。

```text
signed_slot_value_formula_router_closed=true
coefficient_assignment_is_first_open_field=true
acyclic_seed_coefficient_assignment_on_basis_alphabet_proved=false
signed_weight_slot_value_formula_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. value formula 组成

| component | role |
| --- | --- |
| `coefficient_assignment` | 每个 basis word 到 signed coefficient 的赋值公式，是第一开口。 |
| `sign_local_factor_rule` | 由 coefficient assignment 诱导符号、local factor 和非零条件。 |
| `return_rule` | 零值、符号冲突、local factor 缺失或超预算的命名回流。 |
| `prepushforward_sum_identity` | 证明赋值后的 primitive words 在推前前给出目标 alpha/delta 系数。 |

## 2. 前沿压缩

`AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords` 的第一不可替代字段是 `AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger`：必须先给出每个 basis word 到 signed coefficient 的赋值，才能定义 sign/local factor 和推前前求和。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SignedSlotValueFormulaTargetActive` | `true` | `false` | 上一层已把 signed weight coordinate slot 压到 primitive basis word 上的 slot value formula。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `PrimitiveWordDomainAvailableButUnsigned` | `true` | `true` | primitive word 的几何输入域已闭合，但该域仍是 unsigned 坐标域。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `CoefficientAssignmentIsFirstOpenField` | `true` | `true` | slot value formula 的第一字段是 basis word 到 signed coefficient 的赋值；没有它，符号和 local factor 都无定义。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `AlphabetAndAssignmentStillOpen` | `true` | `false` | noncanonical basis alphabet 与 coefficient assignment 尚未共同闭合。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `BasisSourceAndCoefficientLawStillOpen` | `true` | `false` | basis weight source formula 与 primitive row signed coefficient law 仍未证明。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `PointwiseSignedValueFormulaStillOpen` | `true` | `false` | 逐点 signed alpha 值表、非递归 signed weight 公式和 primitive summand signed expression 仍未证明。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `ReverseCoefficientRecoveryBlocked` | `true` | `true` | 不能从 payment、推前后投影或早期零行覆盖反推 coefficient assignment。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `CoefficientAssignmentOnBasisAlphabetCurrentCorpusProved` | `false` | `false` | 当前材料没有提交从 actual noncanonical basis word 到 signed coefficient 的赋值公式。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `SignedSlotValueFormulaCurrentCorpusProved` | `false` | `false` | 没有 coefficient assignment，slot value formula 仍未证明。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |

## 4. 下一真正单点

```text
AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger
```

并行依赖：

```text
AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows
AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger
PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
