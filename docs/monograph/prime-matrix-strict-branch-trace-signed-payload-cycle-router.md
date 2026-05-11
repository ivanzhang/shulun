# Prime Matrix strict branch trace signed payload 回流路由器

**状态：** `branch_trace_formula_split_visible_coordinate_closed_signed_payload_loops_open`

本步继续攻击 `ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn`。结论很窄：完整 branch trace 若作为外部/新输入给出，确实能生成取向律；但按当前内部材料继续展开，它分成可见坐标 trace 和 signed payload trace。可见坐标 trace 已被 anchor、D0/K/Omega、phase、word-coordinate 链条压到 signed weight coordinate slot；而 signed payload 槽位继续经 slot value、coefficient assignment、value map、origin identity 回到 row-level clean-core 原始生成表。也就是说，branch trace 线在当前语料中仍是 signed-source 固定点的一种重命名，不能当作独立证明。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
active_previous_target=ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
visible_coordinate_trace_reduced_to_word_coordinate_chain=true
signed_payload_trace_returns_to_row_level_origin_table=true
branch_trace_route_counts_as_independent_proof=false
new_external_or_primitive_trace_input_provided=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. trace 分裂

完整 trace 必须同时含有两类字段：

| part | fields | current status |
| --- | --- | --- |
| visible coordinate trace | anchor, D0/K/Omega, phase, dyadic/truncation, basis word coordinates | 已压到 word-coordinate 线；首个不可替代槽位是 signed weight coordinate slot |
| signed payload trace | orientation parity, signed coefficient, local factor, exact `(u,v)`, return tag | 回到 signed coefficient assignment / row-level origin table |

因此“完整 trace”不是一个单字段魔法输入。它的 signed payload 部分正是我们上一轮想证明的取向/local-factor 来源。

## 2. 当前内部展开链

```text
ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
  -> AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment
  -> AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility
  -> AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility
  -> AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters
  -> AcyclicSeedSignedWeightCoordinateSlotLedger
  -> AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords
  -> AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger
  -> AcyclicSeedBasisWordToSignedCoefficientValueMapFormula
  -> AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward
  -> RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

这条链条的前半段给出坐标容器，后半段要求 signed coefficient 值。后半段不是可见坐标的推论。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BranchTraceTargetActive` | `true` | `false` | 上一轮把取向律压到 exact actual noncanonical branch trace。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| `TraceSplitsIntoCoordinateAndPayload` | `true` | `true` | 完整 trace 由可见坐标字段和 signed payload 字段共同组成。 | 两者都必须正向给出 |
| `VisibleCoordinateChainLocated` | `true` | `true` | anchor/D0/K/Omega/phase 到 basis word 坐标的链条已定位。 | signed weight coordinate slot |
| `CoordinateTraceDoesNotEmitSignedPayload` | `true` | `true` | 可见坐标只给 word/row 形状，不产生 orientation parity 或 signed coefficient。 | signed payload trace |
| `SignedPayloadReturnsToRowLevel` | `true` | `true` | signed slot/value-map/origin identity 回到 row-level 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `BranchTraceRouteIsFixedPointInCurrentCorpus` | `true` | `true` | 当前内部展开没有提供新的非循环生成器，只把缺口重命名为 trace payload。 | 不可当作证明 |
| `NewPrimitiveTraceInputProvided` | `false` | `false` | 当前材料没有额外提交 primitive trace constructor formula。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn as new input |
| `BranchTraceCurrentCorpusProved` | `false` | `false` | trace 的 signed payload 部分未证明。 | signed payload source or terminal descent |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 本步只排除了 trace 线自证，未产生终端矛盾。 | noncircular descent/external + DStructure |

## 4. 剩余选择

若允许新增真正 primitive trace 输入，下一单点仍可写成：

```text
ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
```

但它必须作为新证明包提交，不能由当前 word-coordinate / assignment 环自证。

若不新增该输入，内部 strict 线的非循环方向只剩：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
```

外部条件方向为：

```text
AcceptFullSKLSExtExternalContract
```

最终晋级仍需：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 结论

branch trace 线给出了取向律的正确格式，但没有在当前内部材料中生成 signed payload。当前最窄实质缺口没有消失：要么提交一个真正新的 noncanonical primitive trace constructor formula；要么停止用 source/trace/assignment 环自证，转攻终端回流的 well-founded 严格下降证书。
