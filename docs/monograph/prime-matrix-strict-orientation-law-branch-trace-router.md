# Prime Matrix strict 取向律到完整 branch trace 路由器

**状态：** `orientation_local_factor_law_reduced_to_complete_branch_trace_formula_or_return_open`

本步继续攻击 `PrimitiveOrientationLocalFactorProductLawBeforePushforward`。新的压缩结论是：signed 取向律不能作为孤立的 Möbius/奇偶公式补入；它必须由 actual noncanonical primitive emitter 的完整 branch trace 正向生成。若完整 trace 存在，则 orientation bit、sign、local factor、truncation weight、branch key、exact `(u,v)` 和 return tag 都是同一条 Cauchy 前路径的字段，同路径无抵消可由非零 local factor 乘积推出。当前材料只在 canonical 分支有 RIW/Buchstab 决策树影子；noncanonical clean-core 仍未提交自己的 exact branch-trace constructor formula。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
active_previous_target=PrimitiveOrientationLocalFactorProductLawBeforePushforward
complete_branch_trace_would_imply_orientation_law=true
canonical_branch_trace_scoped_only=true
generic_wfd_not_a_branch_trace=true
actual_noncanonical_complete_branch_trace_formula_proved=false
primitive_orientation_local_factor_product_law_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 压缩定理

若存在

```text
ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
```

也就是对每个 actual noncanonical source tuple，在 Cauchy/dispersion/Phi/payment 之前给出有限条 primitive branch traces，且每条 trace 同时登记

```text
ordered branch operations,
alpha/delta side,
orientation parity,
dyadic/truncation state,
local factor product,
signed coefficient,
exact (u,v),
branch key,
return tag
```

则 `PrimitiveOrientationLocalFactorProductLawBeforePushforward` 条件闭合：取向位和 local factor 乘积不再需要额外猜测，而是 trace 字段的函数。

## 2. 为什么不能只用 Möbius/parity 影子

Möbius/parity 公式能描述某些低模端点或 squarefree 支撑上的奇偶影子，但它缺少四个 actual emitter 必需字段：

| missing field | why it matters |
| --- | --- |
| `actual_source_tuple_scope` | 必须证明该奇偶来自当前 noncanonical clean-core source，而不是 canonical 或 generic WFD 模板 |
| `ordered_branch_trace` | 同一个 Möbius 符号可能对应多条不同 branch 路径，local factor 和 key 不同 |
| `exact_uv_output` | payment/Phi 前就要输出 exact `(u,v)`，不能从下游纤维反推 |
| `failure_return_tags` | 零 local factor、超预算、thin/rejected/cancelling 必须命名回流 |

因此 Möbius/parity 是候选局部影子，不是 strict 内部线可用的 signed coefficient 生成律。

## 3. 完整 trace 条件闭合链

| step | conditional result |
| --- | --- |
| complete trace lists ordered branch operations | primitive row 的来源不再后验选择 |
| trace records orientation parity | `orientation(row)` 由路径奇偶确定 |
| trace records nonzero local factors | `local_factor_product(row)` 非零或命名回流 |
| trace records dyadic/truncation state | `truncation_weight(row)` 与同一 formal unit 同步 |
| trace records exact `(u,v)` and branch key | Phi/payment 前字段完整，不需下游恢复 |
| trace partition is disjoint | 同一 primitive contribution 不被多路径重复计数 |
| same-trace coefficient is nonzero product | 同路径无抵消，符号 refinement 可登记 |

所以完整 trace 是取向律的更小生成原子。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OrientationLawTargetActive` | `true` | `false` | 上一轮最窄点是 primitive orientation/local-factor 乘积律。 | PrimitiveOrientationLocalFactorProductLawBeforePushforward |
| `OrientationLawGeneratedByTrace` | `true` | `true` | 若完整 branch trace 存在，取向、符号、local factor 和 signed coefficient 都是 trace 字段。 | prove trace formula |
| `MobiusParityShadowInsufficient` | `true` | `true` | Möbius/parity 只给局部奇偶影子，不给 actual source tuple、exact `(u,v)`、branch key 和回流。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| `CanonicalDecisionTreeScopedOnly` | `true` | `true` | canonical RIW/Buchstab 决策树只服务 canonical-source 分支，不能跨导入 noncanonical clean-core。 | noncanonical trace needed |
| `GenericWFDNotBranchTrace` | `true` | `true` | generic WFD 是形式分解约束，不是 primitive branch trace emitter。 | actual branch trace formula |
| `CompleteTraceImpliesNoCancellationConditionally` | `true` | `true` | 完整 trace 下，路径互斥且 local factor 乘积非零，同路径无抵消。 | trace existence/budget/return still open |
| `TraceBudgetStillOpen` | `true` | `false` | 完整 trace 数必须满足 polylog/K6 预算，超预算须回流。 | CompleteActualNoncanonicalTraceBudgetLedger |
| `TraceReturnDisciplineStillOpen` | `true` | `false` | 非唯一、零因子、抵消、thin/rejected、超预算必须进入命名回流。 | CompleteBranchTraceFailureNamedReturnLedger |
| `ActualNoncanonicalTraceFormulaCurrentCorpusProved` | `false` | `false` | 当前材料没有 exact actual noncanonical primitive branch-trace constructor formula。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| `OrientationLocalFactorLawCurrentCorpusProved` | `false` | `false` | 取向律被压到完整 trace 公式，但尚未证明。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 本步不产生终端矛盾，不声明行/列命题无条件闭合。 | trace formula 或 terminal descent / 外部合同 + DStructure 验收 |

## 5. 下一真正单点

```text
ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
```

展开为：

```text
ActualNoncanonicalPrimitiveBranchAlphabetLedger
AND CompleteOrderedBranchTraceConstructorFormula
AND OrientationParityAndLocalFactorProductFromTrace
AND ExactUVAndBranchKeyOutputFromTrace
AND CompleteActualNoncanonicalTraceBudgetLedger
AND CompleteBranchTraceFailureNamedReturnLedger
AND NoCanonicalGenericWFDOrDownstreamRecovery
```

若该 exact trace 公式失败，不能再回到 row-level/signed-source 固定点自证；合法出口只剩：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR
AcceptFullSKLSExtExternalContract
```

最终仍需：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 结论

最新最窄点从“取向/local-factor 乘积律”进一步压成“actual noncanonical 完整 branch trace 公式或命名回流”。这是更深一层的同一命题下钻：完整 trace 若能写出，则 signed 取向、local factor 和无抵消同时得到；当前未闭合的是 noncanonical actual emitter 的精确 trace 构造，而不是几何骨架、Möbius 奇偶影子或 canonical 决策树模板。
