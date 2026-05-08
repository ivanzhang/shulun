# Prime Matrix DLS fixed-wheel 单位峰命名回流 schema 路由器

**状态：** `dls_fixedwheel_return_schema_closed_terminal_exclusion_open`

本步闭合的是 DLS fixed-wheel 单位峰的专属命名回流 schema：固定轮峰若持久，必须登记为 W-unit PDEC；若升层后继续集中，进入 new-layer PDEC/flat admission；若固定轮和新增层缺陷都被剥离，则 flat/L2-flat 逃逸已在早期零行反例分支回到终端包。因此 fixed-wheel 专属 gap 被删除；但 W-unit PDEC、终端包和 signed 几何账本仍未无条件排斥。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
dls_fixedwheel_return_schema_closed=true
dls_fixedwheel_specific_gap_removed=true
fixedwheel_numeric_dilution_proved=false
wunit_pdec_terminal_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=DLSFixedWheelUnitPeakDilutionOrPDECReturn
terminal_gap_after_router=NoDLSFixedWheelSpecificGap_AfterWUnitPDECOrLayeredDilutionReturn
```

## 1. 替换律

```text
DLSFixedWheelUnitPeakDilutionOrPDECReturn
  =>
NoDLSFixedWheelSpecificGap_AfterWUnitPDECOrLayeredDilutionReturn
```

这一步仍处于反例分支/终端证书口径，不使用真实样本缺席。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DLSFixedWheelGateActive` | `true` | `true` | 当前输入基仍含 DLSFixedWheelUnitPeakDilutionOrPDECReturn。 | `本步只攻击 fixed-wheel 专属无名出口。` |
| `FixedWheelAtomPinned` | `true` | `true` | LowPhase 已把固定轮单位类峰定位为 W-unit PDEC 或稀释回流。 | `不能继续作为未定义低模规律。` |
| `FiniteWheelFormalUnit` | `true` | `true` | 固定 W 的单位类 U_W 与中心化偏差 E_a(W) 是有限 formal unit 对象。 | `持久峰可登记为 W-unit PDEC。` |
| `FixedWheelNotTerminalLaw` | `true` | `true` | W=30 单位峰真实存在但没有固定单位类长期主导，不能作为终局规律停留。 | `样本只定位结构，不作证明。` |
| `LayeredWheelDilutionOrPDEC` | `true` | `true` | 升层后若峰继续同步则给 PDEC；若不同步，单类峰被稀释并进入新增层/flat 分支。 | `数值稀释本身不是无条件证明。` |
| `PersistentWUnitPeakAdmitsPDEC` | `true` | `true` | 固定单位峰若在同 formal unit 上持久复现，必须作为显式 W-unit PDEC schema 准入。 | `PDEC family 无条件排斥仍开放。` |
| `LayerEscapeUsesNewLayerReturn` | `true` | `true` | 固定轮峰若升层为新增因子 Fourier 集中，已有 new-layer PDEC/flat admission 接线。 | `new-layer 终端证书仍按既有边界处理。` |
| `FlatEscapeAlreadyCounterexampleRouted` | `true` | `true` | 固定轮与新增层均被剥离后的 flat/L2-flat 逃逸已在早期零行反例分支回到终端包。 | `终端包本身仍未无条件排斥。` |
| `NoDLSFixedWheelSpecificFourthExit` | `true` | `true` | fixed-wheel 只有持久 W-unit PDEC、升层 new-layer/flat 回流或稀释不足三类归宿。 | `NoDLSFixedWheelSpecificGap_AfterWUnitPDECOrLayeredDilutionReturn` |
| `DLSFixedWheelUnitPeakDilutionOrPDECReturn` | `true` | `true` | 该硬点作为 fixed-wheel 命名回流 schema 已闭合。 | `不等于 W-unit PDEC 或终端包已排斥。` |
| `SignedGeometricLedgerVariationBranchLiftAndReturn` | `false` | `false` | DLS 微输入删除后，下一步回到 signed 几何账本变差/分支提升锁。 | `SignedGeometricLedgerVariationBranchLiftAndReturn` |
| `GlobalPDECorSparseTerminalExclusion` | `false` | `false` | 若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。 | `FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

fixed-wheel 专属 gap 已删除。下一步最窄目标转到 `SignedGeometricLedgerVariationBranchLiftAndReturn`：证明 actual signed source 的总变差和 branch key 复杂度确由几何账本支配，或把超预算质量回流 PDEC/SAE/ColumnCRT/CleanKLS。
