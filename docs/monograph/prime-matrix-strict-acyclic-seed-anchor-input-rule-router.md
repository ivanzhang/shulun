# Prime Matrix strict acyclic seed anchor input rule 路由器

**状态：** `anchor_input_rule_closed_word_coordinate_reduced_to_signed_weight_slot_open`

本步利用已有锚区间与多重度证书关闭 anchor input rule：选择函数是 sorted(A) 逐锚全枚举，端点由 J_a 公式固定，phase_rule 前置过滤，空锚集/空区间/高重叠都有记录或回流。因此真正剩余不再是 anchor 输入，而是 primitive basis word 中 signed weight/local factor 的坐标槽。

```text
anchor_input_rule_router_closed=true
anchor_input_rule_proved=true
signed_weight_coordinate_slot_proved=false
word_coordinate_formula_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 已闭合输入律

| law | meaning |
| --- | --- |
| `anchor_selection_function` | 选择函数不是单点后验选择，而是 `sorted(A)` 的逐锚全枚举；A=empty 显式登记。 |
| `window_endpoint_coupling` | 每个锚 a 的输入区间为 J_a=[max(D0,ceil(L/a)), min(2D0,floor(R/a)+1))。 |
| `phase_filter_pullback` | phase_rule 在锚区间证书与 sweep-line 多重度表中前置过滤，不能在下游重选。 |
| `empty_and_failure_return` | A=empty、J_a=empty、缺字段、m(d)>Omega 均有显式记录或命名回流。 |
| `complexity_charge` | 多重度表用 m(d)<=Omega / m(d)>Omega 给出低重叠收费和高重叠回流。 |

## 2. 前沿压缩

`AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates` 可由锚区间证书、锚区间枚举和低重叠多重度表闭合；word coordinate formula 的下一真正缺口转为 `AcyclicSeedSignedWeightCoordinateSlotLedger`。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AnchorInputRuleTargetActive` | `true` | `false` | 上一层已把 word coordinate formula 压到 anchor input rule。 | AcyclicSeedAnchorInputRuleForPrimitiveWordCoordinates |
| `AnchorSelectionFunctionClosedBySortedEnumeration` | `true` | `true` | 锚输入选择由 `sorted(A)` 逐锚全枚举给出；空锚集显式记录，不靠后验挑选。 | anchor_selection_function closed。 |
| `WindowEndpointCouplingClosed` | `true` | `true` | J_a 端点由窗口 [L,R]、D0 与 anchor a 的 ceil/floor 公式唯一确定。 | window_endpoint_coupling closed。 |
| `PhaseFilterPullbackClosed` | `true` | `true` | phase_rule 已在锚区间/多重度表中前置过滤；不能在下游重新选择。 | phase_filter_pullback closed。 |
| `AnchorInputComplexityChargeClosed` | `true` | `true` | low-overlap multiplicity table 给出 m(d)<=Omega 的收费与 m(d)>Omega 的 high-overlap return。 | anchor_input_complexity_charge closed。 |
| `AnchorInputNonposthocAndFailureReturnClosed` | `true` | `true` | source_tuple_hash、endpoint hash、empty flags 与 high-overlap return 排除后验输入选择。 | anchor_input_failure_return closed。 |
| `AnchorInputRuleCurrentCorpusProved` | `true` | `true` | anchor input rule 的选择、端点、相位、空例、复杂度和回流均由既有锚区间/多重度账本闭合。 | 可进入 word coordinate formula 的下一坐标槽。 |
| `DyadicAndPhaseCoordinatesAvailableAfterAnchorInput` | `true` | `true` | d in [D0,2D0)、J_a 端点和 phase_filtered segments 已给出 dyadic/phase 坐标数据。 | AcyclicSeedSignedWeightCoordinateSlotLedger |
| `SignedWeightCoordinateSlotCurrentCorpusProved` | `false` | `false` | 当前材料仍未给出 primitive basis word 中承载 signed weight/local factor 的坐标槽。 | AcyclicSeedSignedWeightCoordinateSlotLedger |
| `WordCoordinateFormulaCurrentCorpusProved` | `false` | `false` | anchor/dyadic/phase 输入已闭合，但缺 signed weight coordinate slot，完整 word coordinate formula 仍未闭合。 | AcyclicSeedSignedWeightCoordinateSlotLedger |
| `SignedSlotOpenMatchesCoefficientLawGap` | `true` | `false` | signed slot 与后续 coefficient assignment/basis weight source 是同一缺口，不能从 unsigned 输入自动推出。 | AcyclicSeedSignedWeightCoordinateSlotLedger |

## 4. 下一真正单点

```text
AcyclicSeedSignedWeightCoordinateSlotLedger
```

并行依赖：

```text
AcyclicSeedCoordinateNonposthocCertificateLedger
AcyclicSeedCoordinateFailureReturnLedger
AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
