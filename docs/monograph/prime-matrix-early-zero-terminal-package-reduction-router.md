# Prime Matrix 早期零行终端排斥包压缩路由器

**状态：** `early_zero_terminal_package_reduced_to_anchor_collar_depth_sae`

本步把抽象 EarlyZeroTerminalExclusionPackage 压成已有早期零行几何硬核：大行段是真双素 canonical anchor-collar 短纤维容量，早期段是复合 cofactor 递归下降或 LocalSurvivor/SAE 排斥。该压缩不完成终端排斥，但删除了抽象终端包的无名性。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
early_zero_terminal_package_reduced=true
early_zero_terminal_package_fully_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=EarlyZeroTerminalExclusionPackage
terminal_gap_after_router=AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion
```

## 1. 结构链

```text
EarlyZeroTerminalExclusionPackage
=> registered stable recurrence or boundary phase defect
=> exact carry-shell primitive support
=> cofactor depth split
=> x>=sqrt(P): canonical anchor collar short prime fibers
=> x<sqrt(P): composite cofactor descent or SAE/PDEC return
```

这仍然是在 `Assume EarlyZeroRowWithinP` 下工作；真实样本缺席不参与证明。

## 2. 替换律

```text
EarlyZeroTerminalExclusionPackage
  =>
AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EarlyZeroTerminalPackageActive` | `true` | `true` | 上一层已把 pure L2-flat 逃逸替换为 EarlyZeroTerminalExclusionPackage。 | `现在压缩终端包本身。` |
| `PhaseDefectNoFourthExit` | `true` | `true` | 早期零行相位缺陷已经准入 PDEC/SAE/ColumnCRT 命名家族。 | `还没有排斥这些命名家族。` |
| `StableRecurrenceDisplacementAbsorbed` | `true` | `true` | 稳定短复现若存在，按 displacement PDEC、ColumnCRT 或 SAE/endpoint 吸收。 | `不再作为独立第四项。` |
| `CarryShellPrimitiveSupportClosed` | `true` | `true` | primitive PDEC 支撑已被 exact carry-shell 恒等式重写。 | `容量不等式仍未证明。` |
| `CofactorDepthSplitClosed` | `true` | `true` | x>=sqrt(P) 时 cofactor 必为素数；x<sqrt(P) 的复合 cofactor 只能递归或命名回流。 | `复合递归容量/孤窗排斥仍未完成。` |
| `AnchorCollarPrimePairReductionClosed` | `true` | `true` | 真双素分支的最小高素锚落在 x<q<sqrt((x+1)P)，固定 q 后是长度 <sqrt(P) 的短素数纤维。 | `短纤维总容量仍未证明不足。` |
| `ContradictionMatrixFrontierCompatible` | `true` | `true` | 早期零行矛盾矩阵也把当前最强前沿定位到 anchor-collar 纤维容量或命名回流。 | `说明压缩结果与既有总图一致。` |
| `EarlyZeroTerminalPackageReduced` | `true` | `true` | 抽象 EarlyZeroTerminalExclusionPackage 被压成 anchor-collar、cofactor descent、early-band SAE 三项。 | `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion` |
| `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn` | `false` | `false` | 尚未证明所有 canonical collar q-fiber 的短素数容量不能覆盖 R_x。 | `下一步最窄目标。` |
| `CompositeCofactorDepthDescentOrNamedReturn` | `false` | `false` | 尚未证明 x<sqrt(P) 的复合 cofactor 递归壳必下降到底或命名排斥。 | `第二剩余。` |
| `EarlyBandLocalSurvivorOrSAEExclusion` | `false` | `false` | 孤立早期窗口和递归失败时的 LocalSurvivor/SAE packet 尚未全局排斥。 | `第三剩余。` |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

最窄目标更新为 `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn`：证明 canonical anchor collar 中长度 `<sqrt(P)` 的短素数纤维总容量不能覆盖 `R_x`，或证明任何过载都会产生 PDEC/SAE/ColumnCRT 命名证书。
