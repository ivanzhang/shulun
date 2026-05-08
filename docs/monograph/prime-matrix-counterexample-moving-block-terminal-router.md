# Prime Matrix 反例分支 moving-block 到早期零行终端包路由器

**状态：** `counterexample_moving_block_reduced_to_early_zero_terminal_package_open`

本步只在假设早期零行反例分支内工作。actual same-(u,v) moving block 若有登记低维签名，它已经是 PDEC/SAE/ColumnCRT 型终端；若完全无登记签名，则它就是纯 L2-flat/NC-BLK 逃逸，而早期零行 L2-flat 路由已把该逃逸排除为 EarlyZeroTerminalExclusionPackage。因此 moving-block hardpoint 不再是独立无名 clean-core 出口，剩余回到早期零行终端包及模型/DPRC 口径兼容。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
moving_block_to_terminal_reduction_closed=true
actual_moving_block_spread_proved=false
early_zero_terminal_package_fully_proved=false
exact_model_gap_dprc_compatibility_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
terminal_gap_after_router=EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock
```

## 1. 反例二分

```text
Assume EarlyZeroRowWithinP
actual moving same-(u,v) atom
  -> registered finite/low-dimensional signature
       -> PDEC / SAE / ColumnCRT / EarlyZeroTerminalExclusionPackage
  -> no registered signature
       -> pure L2-flat / NC-BLK escape
       -> EarlyZeroTerminalExclusionPackage
```

该二分不使用真实样本缺席；它只比较反例分支内已登记的早期零行缺陷合同与 flat/KLS 准入合同。

## 2. 替换律

```text
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
  =>
EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleMovingBlockGateActive` | `true` | `false` | 最新最窄点是早期零行反例分支中的 actual same-(u,v) moving block 集中。 | `判断它是否仍可作为无名 clean-core 终端。` |
| `SourceEntropyImplicationImported` | `true` | `true` | SourceBlockEntropy 一旦证明可推出 NC-BLK；形式 WFD/Type/Fourier 不能免费推出它。 | `不能用 generic 模板闭合，只能用反例分支结构继续压缩。` |
| `SharpMovingAtomPinned` | `true` | `true` | clean-core sharp 输入已固定为最终容量测度无 moving same-(u,v) 大原子。 | `若有大原子，必须通过所有回流测试。` |
| `RegisteredOrPureFlatDichotomy` | `true` | `true` | 反例分支中的 moving block 若有登记低维签名则进 PDEC/SAE/ColumnCRT；若没有则是纯 L2-flat/NC-BLK 逃逸。 | `两支都不再是无名终端。` |
| `PureL2FlatEscapeAlreadyRemovedInEarlyZeroBranch` | `true` | `true` | 早期零行反例分支已排除纯 L2-flat KLS 作为最后无名逃逸。 | `纯 flat 支路回到 EarlyZeroTerminalExclusionPackage。` |
| `EarlyZeroTerminalPackageAlreadyReduced` | `true` | `true` | EarlyZeroTerminalExclusionPackage 已压成 anchor-collar、复合 cofactor 下降和 early-band SAE 三项。 | `终端包仍未被排斥。` |
| `CounterexampleMovingBlockReducedToTerminalPackage` | `true` | `true` | 在假设早期零行分支内，moving-block 集中不能继续作为独立 clean-core 无名出口。 | `EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock` |
| `EarlyZeroTerminalExclusionPackage` | `false` | `false` | 还没有排斥准入后的 primitive PDEC 容量、SAE/LocalSurvivor 或稳定复现位移缺陷。 | `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion。` |
| `ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock` | `false` | `false` | ExplicitModelGapAndFiniteDPRCLedger 仍需与本次 moving-block 到终端包的替换口径一致化。 | `检查模型余量/有限 DPRC 账本是否已覆盖该替换后的终端包。` |
| `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | `DStructureRankinPromotionPackage。` |

## 4. 最新输入基

条件输入基：

```text
((EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock AND ExplicitModelGapAndFiniteDPRCLedger) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

下一步最窄目标回到 `EarlyZeroTerminalExclusionPackage`：排斥 primitive PDEC 容量、SAE/LocalSurvivor packet 或稳定复现位移缺陷；同时核对模型余量/DPRC 账本是否与该替换口径兼容。
