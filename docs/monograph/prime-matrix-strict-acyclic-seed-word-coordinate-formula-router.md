# Prime Matrix strict acyclic seed word coordinate formula 路由器

**状态：** `word_coordinate_formula_anchor_closed_reduced_to_signed_weight_coordinate_slot_open`

本步同步 word_coordinate_formula 前沿：anchor input rule 已由锚区间和多重度账本闭合，因此不再是当前缺口；完整坐标公式的真正剩余是 signed weight coordinate slot。该槽位仍缺 signed weight/local factor 赋值公式，所以 word_coordinate_formula 仍未证明。

```text
word_coordinate_formula_router_closed=true
anchor_input_rule_proved=true
coordinate_domain_closed_after_anchor_input=true
signed_weight_coordinate_slot_proved=false
word_coordinate_formula_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters` 的旧前沿 `AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates` 已闭合；当前第一剩余坐标门是 `AcyclicSeedSignedWeightCoordinateSlotLedger`。

## 2. 当前坐标剩余字段

| field | meaning |
| --- | --- |
| `anchor_input_rule` | 已由 anchor input rule 路由器闭合：逐锚枚举、端点耦合、相位前置过滤和复杂度收费。 |
| `dyadic_phase_coordinate_domain` | anchor rule 闭合后，D0/K/Omega 与 phase_rule 的输入域可登记。 |
| `signed_weight_coordinate_slot` | 仍缺承载 signed weight、sign、local factor 和 return_tag 的坐标槽证明。 |
| `slot_value_formula_dependency` | signed 槽位继续依赖 primitive basis word 上的 signed weight/local factor 赋值公式。 |
| `coordinate_nonposthoc_certificate` | 坐标公式仍不得读取 payment、零行覆盖、推前后投影或 terminal extraction 后数据。 |
| `coordinate_failure_return` | signed 槽位或赋值公式缺失时回流命名终端家族。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WordCoordinateFormulaTargetActive` | `true` | `false` | 上一层已把 basis_word_formula 压到 word_coordinate_formula。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| `AnchorSetAndInputRuleClosed` | `true` | `true` | A、D0/K/Omega、phase_rule 可复算，且 anchor input rule 已由逐锚枚举、端点耦合和相位前置过滤闭合。 | anchor 坐标门不再是当前前沿。 |
| `CoordinateDomainAvailableAfterAnchorInput` | `true` | `true` | anchor rule 闭合后，primitive word 的 anchor/dyadic/phase 输入域已可登记。 | 仍需 signed weight coordinate slot。 |
| `SignedWeightCoordinateSlotIsFirstRemainingGate` | `true` | `true` | 完整 word coordinate formula 还必须给 signed weight、sign、local factor 和 return_tag 槽位。 | AcyclicSeedSignedWeightCoordinateSlotLedger |
| `SignedSlotValueFormulaStillOpen` | `true` | `false` | signed 槽位继续依赖 primitive basis word 上的 signed weight/local factor 赋值公式。 | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| `ReverseCoordinateRecoveryBlocked` | `true` | `true` | 不能从 payment、推前后投影或早期零行覆盖反推出 signed coordinate slot 或 signed value formula。 | AcyclicSeedSignedWeightCoordinateSlotLedger |
| `WordCoordinateFormulaCurrentCorpusProved` | `false` | `false` | anchor/dyadic/phase 坐标门已同步闭合；因 signed weight coordinate slot 未证明，完整 word coordinate formula 仍未证明。 | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |

## 4. 下一真正单点

```text
AcyclicSeedSignedWeightCoordinateSlotLedger
```

并行依赖：

```text
AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords
AcyclicSeedCoordinateNonposthocCertificateLedger
AcyclicSeedCoordinateFailureReturnLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
