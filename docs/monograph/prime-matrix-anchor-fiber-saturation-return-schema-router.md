# Prime Matrix anchor fiber 饱和命名回流 schema 路由器

**状态：** `anchor_fiber_saturation_return_schema_closed_terminal_exclusion_open`

本步闭合的是 anchor fiber 饱和的命名回流 schema：固定 q 的短素数窗口是有限 formal unit；持久近饱和必须作为 primitive PDEC schema，孤立近饱和必须作为 LocalSurvivor/SAE packet。因此 anchor 专属 fiber gap 被删除，但 PDEC/SAE 终端排斥本身仍未证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
anchor_fiber_saturation_return_schema_closed=true
anchor_specific_fiber_gap_removed=true
pdec_or_sae_terminal_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=AnchorFiberSaturationPDECOrSAEReturn
terminal_gap_after_router=NoAnchorSpecificFiberSaturationGap_AfterNamedPDECOrSAEReturn
```

## 1. 替换律

```text
AnchorFiberSaturationPDECOrSAEReturn
  =>
NoAnchorSpecificFiberSaturationGap_AfterNamedPDECOrSAEReturn
```

这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AnchorFiberSaturationGateActive` | `true` | `true` | 上一层唯一 anchor 专属剩余是 AnchorFiberSaturationPDECOrSAEReturn。 | `本步只判断 fiber 饱和是否有未命名出口。` |
| `FiniteShortFiberFormalUnit` | `true` | `true` | 固定 q 后，m 位于长度 <sqrt(P) 的有限素数窗口；物理原子是 (x,q,m,c)。 | `fiber 饱和可登记为有限 formal unit packet。` |
| `PersistentFiberSaturationAdmitsPDEC` | `true` | `true` | 若同一 fiber 签名沿反例族持久近饱和，则必须提交同 formal unit primitive PDEC schema。 | `终端排斥仍依赖 PDEC family 证书，不在本步证明。` |
| `IsolatedFiberSaturationAdmitsSparseSAE` | `true` | `true` | 若 fiber 饱和只孤立出现，则必须提交有限 LocalSurvivor/SAE packet schema。 | `终端排斥仍依赖 sparse/SAE packet 证书，不在本步证明。` |
| `NoUnnamedFiberSaturationExit` | `true` | `true` | fiber 饱和要么持久进 PDEC，要么孤立进 SAE/LocalSurvivor；没有 anchor 专属第四出口。 | `NoAnchorSpecificFiberSaturationGap_AfterNamedPDECOrSAEReturn` |
| `AnchorFiberSaturationPDECOrSAEReturn` | `true` | `true` | 该硬点作为命名回流 schema 已闭合。 | `PDEC/SAE 终端家族本身仍未无条件排斥。` |
| `GlobalPDECorSparseTerminalExclusion` | `false` | `false` | 若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。 | `FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

anchor 专属 fiber gap 已删除。下一步最窄目标回到 `CompositeCofactorDepthDescentOrNamedReturn`；若未来实际物化新的 PDEC/SAE packet，则由 `FutureExplicitPrimitivePDECSchema_OR_FutureExplicitSparsePacketExtractorSchema_if_materialized` 接管。
