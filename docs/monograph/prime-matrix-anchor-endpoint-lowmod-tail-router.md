# Prime Matrix anchor 端点 PDEC 低模/尾项二分路由器

**状态：** `anchor_endpoint_pdec_reduced_to_lowmod_tail_dichotomy`

本步把 anchor-collar 端点 PDEC 从一个整体强负误差拆成低模有限 CRT 相位坏集与高模 tail-core/纤维饱和两项。它不排斥端点缺陷，只删除整体黑箱形态，让下一步可直接攻固定低模相位坏集。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
anchor_endpoint_pdec_dichotomy_closed=true
anchor_endpoint_pdec_exclusion_fully_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=AnchorCollarEndpointDefectPDECExclusion
terminal_gap_after_router=(AnchorEndpointLowModPDECFinitePhaseExclusion AND AnchorEndpointTailCorePDECOrFiberSaturation)
```

## 1. 二分公式

```text
If E_x<=-G_x, then for any D and theta either E_{x,<=D}<=-theta G_x or E_{x,>D}<=-(1-theta)G_x.
```

这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。

## 2. 替换律

```text
AnchorCollarEndpointDefectPDECExclusion
  =>
(AnchorEndpointLowModPDECFinitePhaseExclusion AND AnchorEndpointTailCorePDECOrFiberSaturation)
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AnchorEndpointDefectGateActive` | `true` | `true` | 上一层最新最窄目标是 AnchorCollarEndpointDefectPDECExclusion。 | `本步只处理该端点缺陷。` |
| `EndpointBridgeImported` | `true` | `true` | 早期零行若触发 anchor 主项间隙，则 E_x<=-G_x。 | `需要排斥该强负端点缺陷。` |
| `DLS13LowTailTemplateImported` | `true` | `true` | DLS13 已有同型低模/尾项精确二分，可逐字迁移到 E_x。 | `不新增概率假设。` |
| `AnchorEndpointLowTailDichotomy` | `true` | `true` | 对任意 D 与 0<theta<1，E_x<=-G_x 强制 E_{x,<=D}<=-theta G_x 或 E_{x,>D}<=-(1-theta)G_x。 | `端点缺陷不能作为整体黑箱保留。` |
| `LowModFinitePhasePDECRoute` | `true` | `false` | 低模项是有限 CRT 相位函数；若承担强负缺陷，则给 fixed-wheel/lowphase PDEC 坏相位。 | `仍需排斥该有限相位坏集。` |
| `TailCoreNamedReturnRoute` | `true` | `false` | 尾项若承担强负缺陷，必须显化为 PointLoad、ShortWindow、LowPhase 或 anchor-fiber 饱和。 | `仍需排斥尾项 core 或回流 PDEC/SAE。` |
| `AnchorEndpointPDECDichotomyClosed` | `true` | `true` | AnchorCollarEndpointDefectPDECExclusion 已压成低模有限相位排斥与高模尾项 core/纤维饱和排斥。 | `(AnchorEndpointLowModPDECFinitePhaseExclusion AND AnchorEndpointTailCorePDECOrFiberSaturation)` |
| `AnchorEndpointLowModPDECFinitePhaseExclusion` | `false` | `false` | 尚未证明固定 D 低模坏相位不能持续命中早期零行反例族。 | `下一步最窄目标。` |
| `AnchorEndpointTailCorePDECOrFiberSaturation` | `false` | `false` | 尚未证明高模尾项强负只能回流已可排斥 PDEC/SAE 或短纤维饱和。 | `第二剩余。` |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND ((AnchorEndpointLowModPDECFinitePhaseExclusion AND AnchorEndpointTailCorePDECOrFiberSaturation) OR AnchorFiberSaturationPDECOrSAEReturn) AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND ((AnchorEndpointLowModPDECFinitePhaseExclusion AND AnchorEndpointTailCorePDECOrFiberSaturation) OR AnchorFiberSaturationPDECOrSAEReturn) AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

最窄目标更新为 `AnchorEndpointLowModPDECFinitePhaseExclusion`：固定 `D` 后，低模项是有限 CRT 相位函数；若它能持续承担 `-theta G_x` 级负缺陷，就必须形成 fixed-wheel/lowphase PDEC 坏相位。下一步要排斥这个坏相位，或把它登记为可处理 PDEC 证书。
