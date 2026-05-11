# Prime Matrix strict acyclic seed signed weight coordinate slot 路由器

**状态：** `signed_weight_coordinate_slot_reduced_to_slot_value_formula_open`

本步把 signed weight coordinate slot 压到 slot_value_formula。锚、dyadic、phase 输入已闭合，所以几何坐标不再阻塞；剩余是纯 signed 算术：必须正向给出每个 primitive basis word 的 signed weight/local factor，且与 basis source 和 coefficient assignment 兼容。

```text
signed_weight_coordinate_slot_router_closed=true
coordinate_domain_closed=true
slot_schema_available=true
signed_weight_slot_value_formula_proved=false
signed_weight_coordinate_slot_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. slot 字段

| field | meaning |
| --- | --- |
| `slot_schema` | 在 primitive basis word 中声明 signed_weight、sign、local_factor、return_tag 槽位。 |
| `slot_value_formula` | 对每个 primitive basis word 给出 signed weight/local factor 的实际赋值公式。 |
| `nonzero_and_sign_rule` | 证明 local factor 非零、符号口径确定；失败时命名回流。 |
| `basis_assignment_compatibility` | 证明该槽位赋值与 seed coefficient assignment/basis source 是同一公式。 |
| `prepushforward_sum_compatibility` | 证明槽位赋值参与推前前 alpha/delta 求和恒等式。 |

## 2. 前沿压缩

`AcyclicSeedSignedWeightCoordinateSlotLedger` 的输入域和槽位 schema 可由已闭合坐标账本声明；真正首缺口是 `AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords`，即每个 primitive basis word 的 signed weight/local factor 赋值公式。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SignedWeightCoordinateSlotTargetActive` | `true` | `false` | 上一层已关闭 anchor input rule，并把 word coordinate formula 的剩余压到 signed weight coordinate slot。 | AcyclicSeedSignedWeightCoordinateSlotLedger |
| `CoordinateDomainClosed` | `true` | `true` | primitive word 的 anchor/dyadic/phase 输入域已由锚区间和多重度账本闭合。 | slot_schema 可声明。 |
| `SlotSchemaAvailableButValueMissing` | `true` | `false` | 可声明 signed_weight/sign/local_factor 槽位，但还没有每个 word 的实际赋值公式。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `SlotValueFormulaIsFirstOpenField` | `true` | `true` | 没有 slot_value_formula，非零符号、coefficient assignment 和推前前求和都无从验证。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `PointwiseSignedValueTableStillOpen` | `true` | `false` | 逐 skeleton row signed value table 与非递归 signed weight formula 仍未证明。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `BasisSourceAndAssignmentStillOpen` | `true` | `false` | seed basis source、basis alphabet 和 coefficient assignment 尚未闭合，不能给 signed slot 赋值。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `UnsignedCoordinateCannotFillSignedSlot` | `true` | `true` | anchor/dyadic/phase 坐标只给 unsigned 输入域，不能自动产生 signed weight/local factor。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `ReverseSignedSlotRecoveryBlocked` | `true` | `true` | 不能从 payment、推前后投影或早期零行覆盖反推 signed slot value。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `SignedWeightSlotValueFormulaCurrentCorpusProved` | `false` | `false` | 当前材料没有提交 primitive basis word 上的 signed weight/local factor 赋值公式。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `SignedWeightCoordinateSlotCurrentCorpusProved` | `false` | `false` | slot schema 可命名，但缺 value formula、非零符号规则和 assignment 兼容，故坐标槽未闭合。 | AcyclicSeedSignedWeightCoordinateSlotLedger |

## 4. 下一真正单点

```text
AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords
```

并行依赖：

```text
AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger
AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows
PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
