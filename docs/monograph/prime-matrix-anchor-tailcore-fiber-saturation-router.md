# Prime Matrix anchor tail-core 到纤维饱和路由器

**状态：** `anchor_tailcore_reduced_to_fiber_saturation`

本步删除 anchor tail-core 的独立性：高模 tail 若非 fiber saturation，则已经落入全局 DLS PointLoad/ShortWindow/LowPhase 或 Bohr-cap 命名出口。anchor 专属剩余只剩 canonical q-fiber 近饱和是否必回流 PDEC/SAE。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
anchor_tailcore_independent_input_removed=true
anchor_fiber_saturation_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=AnchorEndpointTailCorePDECOrFiberSaturation
terminal_gap_after_router=AnchorFiberSaturationPDECOrSAEReturn
```

## 1. 替换律

```text
AnchorEndpointTailCorePDECOrFiberSaturation
  =>
AnchorFiberSaturationPDECOrSAEReturn
```

这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AnchorTailCoreGateActive` | `true` | `true` | 上一层 anchor 专属最窄目标是 AnchorEndpointTailCorePDECOrFiberSaturation。 | `本步只处理高模 tail-core。` |
| `BESDLSNamedAlphabetImported` | `true` | `true` | 高模 tail-core 若承担强负缺陷，必须显化为 PointLoad、ShortWindow 或 LowPhase。 | `这些不是 anchor 新出口。` |
| `HighFrequencyNoCycleImported` | `true` | `true` | 非零列频率/Bohr-cap 不能形成无名循环，只能回流 PDEC/SAE/ColumnCRT 或 L2-flat。 | `L2-flat 已在早期零行反例分支中关闭为终端包。` |
| `AnchorFiberGeometryPinned` | `true` | `true` | anchor 专属剩余只能是 canonical q-fiber 短素数窗口的近饱和支付。 | `即 AnchorFiberSaturation。` |
| `ExistingGlobalInputsCoverNonFiberTail` | `true` | `false` | PointLoad、ShortWindow、FixedWheel 已在全局输入基中保留。 | `它们尚未证明，但不再是 anchor 专属新增项。` |
| `AnchorTailCoreIndependentInputRemoved` | `true` | `true` | AnchorEndpointTailCorePDECOrFiberSaturation 被压成已有 DLS 命名出口或真正 anchor-fiber 饱和。 | `AnchorFiberSaturationPDECOrSAEReturn` |
| `AnchorFiberSaturationPDECOrSAEReturn` | `false` | `false` | 尚未证明 canonical q-fiber 近饱和必然给出 PDEC/SAE，或不能持续支付早期零行。 | `下一步最窄目标。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND AnchorFiberSaturationPDECOrSAEReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND AnchorFiberSaturationPDECOrSAEReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

最窄目标更新为 `AnchorFiberSaturationPDECOrSAEReturn`：证明 canonical q-fiber 近饱和不能持续支付早期零行，或从近饱和中抽取同 formal unit 的 PDEC/SAE 证书。
