# Prime Matrix strict acyclic seed word coordinate formula 路由器

**状态：** `word_coordinate_formula_reduced_to_anchor_input_rule_open`

本步把 word_coordinate_formula 再压到 anchor_input_rule。目前材料能重构 anchor 集和参数，但没有给出从这些对象选择 primitive word 输入的函数；后续 dyadic、phase、signed 槽位和复杂度收费都依赖这个选择函数。

```text
word_coordinate_formula_router_closed=true
anchor_input_rule_proved=false
word_coordinate_formula_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters` 的第一坐标门是 `AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates`：虽然 A 与参数可复算，但必须先说明 primitive basis word 从哪些 anchor/window/phase 输入产生。

## 2. anchor_input_rule 字段

| field | meaning |
| --- | --- |
| `anchor_selection_function` | 从重构出的 A 或 A=empty 情形中确定 primitive word 坐标输入的选择函数。 |
| `window_endpoint_coupling` | 说明所选 anchor 如何与窗口端点、P/range 和 formal_unit_id 同步。 |
| `phase_filter_pullback` | 把 phase_rule 拉回到 anchor input，而不是只作用于最终 row。 |
| `empty_anchor_case` | A=empty 或 null 参数族时的 canonical 输入规则和命名回流。 |
| `anchor_input_complexity_charge` | anchor 选择带来的分支数、相位数和截断数收费。 |
| `anchor_input_failure_return` | anchor 缺失、选择多值、跨 formal unit 或读后验数据时的回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WordCoordinateFormulaTargetActive` | `true` | `false` | 上一层已把 basis_word_formula 压到 word_coordinate_formula。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `AnchorSetReconstructedButNotSelected` | `true` | `false` | A、D0/K/Omega、phase_rule 可复算，但还没有从 A 选择 primitive word 输入的规则。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `AnchorInputRuleIsFirstCoordinateGate` | `true` | `true` | 没有 anchor input rule，dyadic/truncation coordinate、phase coordinate 和 signed slot 都没有共同输入。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `AnchorIntervalCertificateIsNotInputRule` | `true` | `false` | anchor interval 证书给可用区间或枚举边界，不给 primitive word 的 anchor selection function。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `UnsignedAnchorPhaseNotArithmeticInput` | `true` | `false` | unsigned anchor/phase 公式只服务几何 row 发射，不能替代 pre-Cauchy basis word 的输入选择。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `BranchBudgetChargesAfterSelection` | `true` | `false` | 分支预算可以收费已选择的输入，但不能定义 anchor selection function 本身。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `ReverseAnchorSelectionBlocked` | `true` | `true` | 不能从 payment、推前后投影或早期零行覆盖反选 anchor input。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `AnchorInputRuleCurrentCorpusProved` | `false` | `false` | 当前材料没有给出从重构 A/窗口/phase 到 primitive word 输入的选择函数。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `WordCoordinateFormulaCurrentCorpusProved` | `false` | `false` | 没有 anchor input rule，完整 word coordinate formula 仍未证明。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |

## 4. 下一真正单点

```text
AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates
```

并行依赖：

```text
AcyclicSeedDyadicTruncationCoordinateLedger
AcyclicSeedPhaseCoordinatePullbackLedger
AcyclicSeedAnchorInputComplexityChargeLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
