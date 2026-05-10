# Prime Matrix strict acyclic T1 mismatch 强制出口路由器

**状态：** `acyclic_t1_mismatch_no_silent_exit_closed_signed_source_or_defect_open`

`AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect` 的无静默出口 schema 已闭合：canonical T1 mismatch 只能进入 actual signed source 包、registered terminal/named return，或 clean DLS。这推进了反例链与真实结构链的统一矛盾场，但尚未排斥全部出口；当前最窄活动点是 `AlphaSignedLiftFailureNamedReturnLedger`，因为没有失败命名回流纪律，signed source 包和命名缺陷都不能完成扣账。

```text
mismatch_forcing_schema_closed=true
mismatch_partition_exhaustive_by_t1_law=true
actual_signed_source_package_proved=false
named_return_exclusion_proved=false
acyclic_windowed_kloosterman_dls_internal_estimate_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. mismatch 分割

| cell | test | forced_exit |
| --- | --- | --- |
| `NoIndependentT1Row` | seed 字段只在 T3/T4 payment 或 terminal certificate 后出现。 | source-missing named return。 |
| `TerminalDependentKey` | branch key、sign、local factor 或权重依赖 PDEC/SAE/ColumnCRT 结果。 | registered phase defect / terminal named return。 |
| `IndependentNoncanonicalT1Row` | 存在 T1 算术恒等式，但右端不是 canonical RIW/Buchstab 系数。 | actual signed source + Phi pushforward + source entropy lane。 |
| `CleanDiffuseNoLowDefect` | 低维 terminal defect 已被剥离，但仍不是 canonical T1 row。 | acyclic windowed DLS / CleanKLS lane。 |

## 2. 攻击后剩余

```text
(ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger) OR NamedReturnExclusion OR AcyclicWindowedKloostermanDLSInternalEstimate
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MismatchForcingTargetImported` | `true` | `false` | 上一层已把 canonical equality 失败态压成 mismatch forcing。 | AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect |
| `MismatchPartitionExhaustiveByT1Law` | `true` | `true` | T1 mismatch 只能是无独立 T1 行、terminal-dependent key、独立 noncanonical T1 行或 clean diffuse residual 四类。 | 无静默第五出口。 |
| `UnsignedZeroRowFallsInNoT1RowUnlessLifted` | `true` | `true` | 早期零行 unsigned cover 若不额外给 signed lift，就属于 NoIndependentT1Row，必须命名回流。 | AlphaSignedLiftFailureNamedReturnLedger |
| `TerminalDependentKeyForcedReturn` | `true` | `true` | branch key 若从下游 payment/PDEC 读取，则违反 T1 时间线，只能登记 terminal defect。 | registered terminal defect。 |
| `NamedDefectAlphabetAvailableButNotExcluded` | `true` | `false` | 已有命名回流字母表和压缩纪律，但尚未证明所有命名回流被排斥或预算反超。 | NamedReturn exclusion / unified budget。 |
| `IndependentNoncanonicalT1RequiresSignedLift` | `true` | `false` | 独立 noncanonical T1 行不是坏事，但必须提交 actual signed source、权重律、Phi 推前、变差预算和失败回流。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger |
| `ActualSourceEntropyStillOpen` | `true` | `false` | 即便 signed source 完成，后续 ExactUV/source entropy 主线仍未闭合。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `CleanDiffuseResidualRoutedButOpen` | `true` | `false` | clean diffuse residual 可路由到 windowed DLS/CleanKLS，但该解析原子仍未证明。 | AcyclicWindowedKloostermanDLSInternalEstimate |
| `CounterexampleTrueStructurePressureImported` | `true` | `true` | 统一矛盾场能把反例链压到短复现/缺陷/signed lift 候选，但还没给出终端矛盾。 | StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR signed lift。 |
| `MismatchForcingSchemaClosed` | `true` | `true` | mismatch 已无静默出口：必须进入 signed source、registered defect 或 clean DLS。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger OR AlphaSignedLiftFailureNamedReturnLedger OR AcyclicWindowedKloostermanDLSInternalEstimate |
| `AllMismatchExitsClosedCurrentCorpus` | `false` | `false` | 当前语料未证明 signed source 包、命名回流排斥和 clean DLS 任一完整闭合组合。 | (ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger) OR NamedReturnExclusion OR AcyclicWindowedKloostermanDLSInternalEstimate |

## 4. 下一主攻点

```text
AlphaSignedLiftFailureNamedReturnLedger
```

失败命名回流纪律必须证明：signed lift 缺失、Phi 不兼容、变差超预算、branch-key 爆炸或 terminal-dependent key 都被登记进同一 formal unit 的命名出口，不能成为无名损失。
