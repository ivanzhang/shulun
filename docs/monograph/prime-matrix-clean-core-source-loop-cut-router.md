# Prime Matrix clean-core 来源环切断路由器

**状态：** `clean_core_source_loop_cut_to_acyclic_seed_open`

本步把 CleanCoreOriginalCoefficientGenerationLedgerAndReturn 的循环来源证明路径切断。现有路由只形成 origin ledger -> constructor admission -> actual noncanonical formula -> registered emitter -> origin ledger 的等价环；假设早期零行反例若要保留 clean-core 分支，必须提交不依赖 downstream payment skeleton 的无环 pre-Cauchy noncanonical primitive source seed。若提交不了，该分支不能作为 clean-core 终端，必须回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
source_loop_detected=true
circular_reverse_derivation_rejected=true
source_loop_cut_closed=true
acyclic_pre_cauchy_source_seed_proved=false
clean_core_original_generation_ledger_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=CleanCoreOriginalCoefficientGenerationLedgerAndReturn
terminal_gap_after_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
```

## 1. 来源环

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn
  -> CleanCorePrimitiveSourceConstructorAdmissionAndReturn
  -> ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn
  -> RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
  -> CleanCoreOriginalCoefficientGenerationLedgerAndReturn
```

这个环只说明若一个字段已经合法给出，其他字段可以互相展开或分组；它不能从 downstream payment skeleton 反向生成 primitive source。

## 2. 替换律

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn
  =>
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
```

该替换把“循环来源证明”改写为无环源种子义务。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OriginLedgerGateActive` | `true` | `false` | 最新假设链最窄点已回到 CleanCoreOriginalCoefficientGenerationLedgerAndReturn。 | `检查它是否能靠既有路由自我闭合。` |
| `OriginLedgerToConstructorAdmission` | `true` | `true` | 原始账本必须先给 pre-Cauchy primitive source constructor 准入。 | `该方向不生成构造器，只说明账本入口。` |
| `ConstructorAdmissionToActualNoncanonicalFormula` | `true` | `true` | 来源分类防火墙把 canonical/generic/unregistered/external 分流后，只剩 actual noncanonical 公式。 | `仍需 actual noncanonical primitive formula。` |
| `ActualFormulaToRegisteredEmitter` | `true` | `true` | 反向来源函子只给等价改写：actual formula 等价为 registered pre-pushforward emitter。 | `不能从 payment 图反推来源。` |
| `RegisteredEmitterBackToOriginLedger` | `true` | `true` | pre-pushforward emitter 已压回 actual alpha/delta 原始生成账本。 | `闭合成来源环，但没有生成源种子。` |
| `CleanCoreSourceLoopDetected` | `true` | `true` | 现有源侧路由形成 origin ledger -> constructor -> formula -> emitter -> origin ledger 的循环。 | `循环本身不是证明，必须切断。` |
| `CircularReverseDerivationRejected` | `true` | `true` | 假设反例链不能把自身 payment skeleton 或有限投影当作 primitive source 的来源证明。 | `需要无环 pre-Cauchy 源种子或命名回流。` |
| `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn` | `false` | `false` | 当前材料尚未提交不依赖 downstream payment 图的 actual noncanonical primitive source seed。 | `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn` |
| `ExplicitModelGapAndFiniteDPRCLedger` | `true` | `false` | 模型余量/有限 DPRC 账本仍在输入基中，未由来源环切断处理。 | `ExplicitModelGapAndFiniteDPRCLedger。` |
| `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | `DStructureRankinPromotionPackage。` |

## 4. 最新输入基

条件输入基：

```text
((AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ExplicitModelGapAndFiniteDPRCLedger) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

下一步最窄目标为 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn`：给出不依赖真实 payment 图、有限投影塔或样本缺席的 pre-Cauchy actual noncanonical primitive source seed；否则必须输出命名回流标签。
