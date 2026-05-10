# Prime Matrix strict acyclic seed canonical T1 equality 分支分类路由器

**状态：** `acyclic_seed_canonical_t1_equality_classified_canonical_case_absorbed_mismatch_open`

`AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock` 已被分支分类：若 acyclic seed 在 T1 逐点等于 canonical RIW/Buchstab 系数并锁住同一 branch key，则该 case 只被吸收到 canonical scoped promotion，不给完整行/列无条件矛盾；若不等，则必须证明 mismatch 强制落入 actual signed source/ExactUV/source entropy、registered terminal defect，或 acyclic windowed DLS。现有早期零行几何与真实结构压力不能直接证明该等式，也不能证明全部 mismatch 已被排斥。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
equality_branch_classifier_closed=true
canonical_equality_case_absorbed=true
acyclic_seed_to_canonical_t1_coefficient_equality_proved=false
all_mismatches_force_registered_defect_or_actual_source_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 分支公式

```text
AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock
  ->
AcyclicSeedEqualsCanonicalT1CaseAbsorbedByScopedCanonicalPromotion OR AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect
```

去掉 scoped canonical case 后，严格 noncanonical 活动剩余为：

```text
AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem OR AcyclicWindowedKloostermanDLSInternalEstimate
```

## 2. mismatch 出口表

| case | description | route |
| --- | --- | --- |
| `MissingT1SourceRow` | acyclic seed 没有独立 T1 系数行，只能从下游覆盖或 payment 读取。 | registered source-missing return / PDEC-SAE-ColumnCRT。 |
| `TerminalDependentBranchKey` | branch key、符号或权重依赖 terminal payment、PDEC/SAE 或后验投影。 | registered phase defect / named terminal return。 |
| `GenuineNoncanonicalT1Identity` | 存在独立 pre-Cauchy 算术恒等式，但不是 canonical RIW/Buchstab 系数。 | actual signed source / ExactUV / source entropy 主线。 |
| `CleanDiffuseResidual` | 低维缺陷已剥离，但 residual 仍为非 canonical clean diffuse object。 | acyclic windowed DLS / CleanKLS。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EqualityTargetImported` | `true` | `false` | 上一层已把 canonical pre-Cauchy 身份账本压到 acyclic seed 与 canonical T1 系数逐点等式。 | AcyclicSeedToCanonicalT1CoefficientEqualityAndBranchKeyLock |
| `ScopedCanonicalFormulaAvailable` | `true` | `true` | canonical RIW/Buchstab T1 公式在 canonical branch 内已闭合，可作为比较右端。 | 仍需证明 acyclic seed 等于该右端。 |
| `CanonicalEqualityCaseAbsorbed` | `true` | `true` | 若逐点等式、branch-key lock 和 no terminal dependence 全部成立，该 case 只进入 canonical scoped promotion。 | AcyclicSeedEqualsCanonicalT1CaseAbsorbedByScopedCanonicalPromotion |
| `CanonicalEqualityNotGlobalContradiction` | `true` | `true` | canonical scoped promotion 不是完整行/列无条件闭合；它只删除已证明 canonical 的 case。 | row_column_unconditional_closed=false。 |
| `UnsignedZeroRowCannotProveEquality` | `true` | `true` | 早期零行反例给 unsigned CRT/covering data，不能直接给 canonical signed T1 coefficient equality。 | AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect |
| `SignedLiftStillOpenForMismatch` | `true` | `false` | 若 mismatch 是 genuine noncanonical T1 identity，仍需 actual signed source、权重律、Phi 推前和 branch 预算。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger |
| `TerminalDependentSelectionRejected` | `true` | `true` | 若 equality 只能在 terminal extraction 之后识别，则不是 T1 branch-key lock，必须命名回流。 | registered terminal defect / named return。 |
| `CounterexamplePressureNotEnoughForEquality` | `true` | `true` | 反例链与真实结构链已有压力场，但目前只产生 unsigned rigidity 和候选矛盾，不产生 canonical T1 等式。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR signed lift。 |
| `ActualSourceLaneRemainsOpen` | `true` | `false` | 非 canonical T1 身份若存在，应进入 actual-source 熵/ExactUV 支撑；该主线仍未证明。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `CleanDLSLaneRemainsOpen` | `true` | `false` | clean diffuse residual 的解析出口仍未自足闭合。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `EqualityBranchClassifierClosed` | `true` | `true` | 等式目标已被分类为 canonical absorbed case 或 mismatch forcing case；不能再把 equality 当作无来源常数填充。 | AcyclicSeedEqualsCanonicalT1CaseAbsorbedByScopedCanonicalPromotion OR AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect |
| `AcyclicSeedToCanonicalT1EqualityCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 acyclic seed 逐点等于 canonical T1 系数，也没有证明全部 mismatch 都已触发已闭合终端缺陷。 | AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect |

## 4. 下一主攻点

```text
AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect
```

下一步必须证明所有 canonical T1 mismatch 都不能静默存在：它们要么给出 actual signed source/source entropy 输入，要么登记 terminal defect，要么落入 clean DLS。否则反例链仍有 noncanonical 出口。
