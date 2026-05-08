# Prime Matrix actual signed/Phi 兼容预算到 pre-pushforward emitter 压缩路由器

**状态：** `actual_signed_phi_budget_reduced_to_prepushforward_emitter_open`

本步不证明 actual signed/Phi 兼容预算；它把该复合黑箱压成更原子的 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。假设早期零行反例若要保留 clean-core 支付链，就必须在 Cauchy/dispersion 前给出同 formal unit 的 primitive signed preimage summand、branch key、u/v、sign/local factor 与推前系数恒等式；否则该对象不能留在假设链条中，必须按未登记来源、口径冲突、thin block、PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入回流。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
actual_signed_phi_budget_reduction_closed=true
actual_signed_source_phi_compatibility_budget_proved=false
registered_primitive_prepushforward_fiber_emitter_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn
terminal_gap_after_router=RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
```

## 1. 替换律

```text
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn
  =>
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
```

这里分清两条链：假设链条强制反例必须提供该 emitter；真实链条不能从 payment 图或样本缺席反推出 emitter。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ActualSignedPhiBudgetGateActive` | `true` | `true` | 当前输入基仍含 ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。 | `本步判断它的真正原子字段。` |
| `HypotheticalCounterexampleChainGuard` | `true` | `true` | 本路由只在假设早期零行反例所需的证书链中工作，不用真实样本缺席。 | `保持假设链条与真实链条分离。` |
| `DisintegrationFormalPartClosed` | `true` | `true` | 给定 signed source 与 Phi 后，逐纤维解积分形式闭合；真实门是 pushforward identity 与预算。 | `需要 pre-pushforward signed source。` |
| `AlphaDeltaDictionaryFieldsPinned` | `true` | `true` | 字典字段已经固定为 signed source、pushforward、variation/support 和 sign refinement。 | `字段尚未填。` |
| `PaymentSkeletonAlreadyClosed` | `true` | `true` | completion-hole 域、first-cover map 和 payment count identity 已闭合。 | `剩余不是 payment 图，而是 signed primitive lift。` |
| `ReversePushforwardNoGoImported` | `true` | `true` | 不能从 Gamma 反推唯一 primitive source；必须额外提交 pre-pushforward fiber emitter。 | `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn` |
| `PreCauchyLedgerFieldsImported` | `true` | `true` | pre-Cauchy 来源律要求 primitive path key、同 formal unit、非零/符号细分和命名回流。 | `这些正是 emitter 字段。` |
| `CompatibilityBudgetReducedToFiberEmitter` | `true` | `true` | 兼容预算包的未闭合内容等价压成同 formal unit 的 pre-pushforward fiber emitter。 | `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn` |
| `ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn` | `true` | `true` | 该硬点作为复合黑箱已压缩到 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。 | `压缩不证明 emitter 存在。` |
| `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn` | `false` | `false` | 当前材料尚未给出 actual noncanonical primitive pre-pushforward fiber emitter。 | `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn` |
| `ExplicitModelGapAndFiniteDPRCLedger` | `true` | `false` | 模型余量/有限 DPRC 账本仍在输入基中，未由本步处理。 | `ExplicitModelGapAndFiniteDPRCLedger` |
| `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | `false` | `false` | 源侧 emitter 与模型余量完成后仍需 DStructure/Tail-log4/finite Rankin 独立验收。 | `DStructureRankinPromotionPackage。` |

## 3. 最新输入基

条件输入基：

```text
((RegisteredPrimitivePrePushforwardFiberEmitterAndReturn AND ExplicitModelGapAndFiniteDPRCLedger) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

下一步最窄目标为 `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn`：在推前前逐纤维列出 primitive summand、系数恒等式、branch key、u/v map、符号和 local factor；无法登记或超预算者必须命名回流。
