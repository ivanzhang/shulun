# Prime Matrix strict alpha signed lift 失败命名回流路由器

**状态：** `alpha_signed_lift_failure_named_return_ledger_closed_exclusion_open`

`AlphaSignedLiftFailureNamedReturnLedger` 已闭合为登记纪律：signed lift 缺失、权重律失败、Phi 不兼容、变差/branch-key 超预算、canonical 泄漏、terminal-dependent key 和 clean diffuse residual 都必须进入同一 formal unit 的命名出口。该步不排斥这些出口；排斥仍需 actual signed source 包、NamedReturnExclusion 或 acyclic windowed DLS。下一最窄点回到 `AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger`。

```text
alpha_signed_lift_failure_named_return_ledger_closed=true
universal_formal_unit_records_imported=true
no_loss_return_accounting_imported=true
failure_return_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 失败类型与命名出口

| failure | trigger | named_return |
| --- | --- | --- |
| `MissingSignedSourceRow` | 早期零行只给 unsigned cover，未给 T1 signed alpha source row。 | SourceMissingReturn / PDEC-SAE-ColumnCRTNamedReturn |
| `WeightLawMissingOrZero` | pre-Cauchy 算术权重律缺失、权重为零、符号或 local factor 不同步。 | AlphaWeightLawFailureNamedReturn |
| `PhiPushforwardMismatch` | alpha rows 沿 Phi 推前后不等于 payment-side alpha 系数。 | PhiCompatibilityReturn / PDEC or SAE endpoint return |
| `VariationOrSupportOverBudget` | signed 总变差、绝对支撑或 branch-key 数超过几何账本预算。 | SparseHistorySAE / HotCore / FixedHistory return |
| `CanonicalLeakOrTerminalDependentKey` | noncanonical 规则偷用 canonical scoped 模板，或 branch key 依赖 terminal payment/PDEC。 | RegisteredPhaseDefect / TerminalNamedReturn |
| `CleanDiffuseResidual` | 低维缺陷已剥离但仍无法生成 signed lift。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |

## 2. 攻击后剩余

```text
(ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger) OR NamedReturnExclusion OR AcyclicWindowedKloostermanDLSInternalEstimate
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FailureReturnTargetImported` | `true` | `false` | 上一层把 mismatch forcing 的最窄活动点压成 signed lift 失败命名回流。 | AlphaSignedLiftFailureNamedReturnLedger |
| `UniversalFormalUnitRecordsImported` | `true` | `true` | 任意早期零行 witness 已可抽取有限、无漏、可哈希的 formal unit records。 | 所有失败都必须留在同一 formal unit 账本内。 |
| `NoLossReturnAccountingImported` | `true` | `true` | no-loss 账本给出 O(w)=SourceRecords disjoint_union NamedReturnRecords，Lost(O)=empty。 | 失败对象不能消失。 |
| `AlphaPrimitiveFailureAlphabetImported` | `true` | `true` | alpha primitive rule 已列出 canonical 泄漏、未登记、超预算、thin/rejected/cancelling 等失败回流需求。 | AlphaPrimitiveRuleFailureNamedReturnLedger remains open as exclusion, not as naming schema. |
| `AlphaWeightFailureAlphabetImported` | `true` | `true` | 权重律失败类型已被识别为恒等式缺失、权重为零、符号冲突或 local factor 缺失。 | AlphaWeightLawFailureNamedReturnLedger remains open as downstream exclusion. |
| `TerminalDependentSelectionForcedReturn` | `true` | `true` | 从 payment skeleton 或 terminal certificate 反推 source 被拒绝；这种失败只能命名回流。 | Registered terminal defect. |
| `TerminalDefectAlphabetImported` | `true` | `true` | 终端缺陷无自由出口：低模、dyadic、共同核、固定历史、SAE、冷核心预算均已命名。 | NamedReturnExclusion |
| `NamedReturnCompressionImported` | `true` | `true` | 命名出口压成持久全局终端包或非持久统一预算；失败不再是无名损失。 | Persistent terminal family OR unified budget. |
| `AlphaSignedLiftFailureNamedReturnLedgerProved` | `true` | `true` | signed lift 的所有失败类型都有同 formal unit 的命名出口；本步只证明登记纪律，不证明出口不发生。 | NamedReturnExclusion |
| `FailureReturnExclusionNotProved` | `false` | `false` | 命名出口登记后，仍需后续证明命名回流排斥、actual signed source 包或 clean DLS。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger OR NamedReturnExclusion OR AcyclicWindowedKloostermanDLSInternalEstimate |

## 4. 下一主攻点

```text
AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger
```
