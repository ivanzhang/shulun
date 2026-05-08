# Prime Matrix DLS short-window SAE 命名回流 schema 路由器

**状态：** `dls_shortwindow_sae_return_schema_closed_numeric_bound_open`

本步闭合的是 DLS short-window SAE 的专属命名回流 schema：固定短窗是有限局部覆盖对象，孤立时必须提交 LocalSurvivor/SAE packet，持久时必须提交 PDEC schema，层级逃逸时必须进入 CleanKLS/DLS 或下降回流。因此 short-window 专属无名出口被删除；但数值 short-window bound、PDEC/sparse 终端排斥和其他 DLS 微输入仍未证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
dls_shortwindow_return_schema_closed=true
dls_shortwindow_specific_gap_removed=true
dls_shortwindow_numeric_bound_proved=false
pdec_or_sae_terminal_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=DLSShortWindowSAEBoundOrNamedReturn
terminal_gap_after_router=NoDLSShortWindowSpecificSAEGap_AfterLocalPacketOrPDECReturn
```

## 1. 替换律

```text
DLSShortWindowSAEBoundOrNamedReturn
  =>
NoDLSShortWindowSpecificSAEGap_AfterLocalPacketOrPDECReturn
```

这一步仍处于反例分支/终端证书口径，不使用真实样本缺席。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DLSShortWindowGateActive` | `true` | `true` | 当前输入基仍含 DLSShortWindowSAEBoundOrNamedReturn，且它来自 BES/DLS 三出口字母表。 | `本步只攻击 short-window 专属无名出口。` |
| `ShortWindowAlphabetPinned` | `true` | `true` | DLS 危险交集若落入 short-window，只允许 SAE/LocalSurvivor 或 persistent sparse PDEC。 | `不能再作为 BES 同步失败黑箱。` |
| `FiniteLocalWindowObject` | `true` | `true` | 固定孤窗 I 有有限候选集 C(I) 与 blocker 投影，可形成 LocalSurvivorCert。 | `证书未填时仍需 packet/schema。` |
| `SAELocalDescentWellFounded` | `true` | `true` | 固定孤窗内局部势函数有限下降；沿无限反例族复现则由鸽巢转为 PDEC。 | `PDEC 排斥仍未证明。` |
| `PacketGenerationDichotomy` | `true` | `true` | 不可立即核验的孤窗只剩 finite packet、持久签名 PDEC、层级逃逸 CleanKLS/DLS 或下降回流。 | `未来 packet 必须显式提交。` |
| `FutureSparsePacketBoundaryImported` | `true` | `true` | 当前 sparse/LocalSurvivor 前沿清零；未来新增 sparse route 必须提交 extractor schema。 | `不是全局 sparse family 无条件排斥。` |
| `PersistentShortWindowAdmitsPDEC` | `true` | `true` | short-window 若在同 formal unit 上持久复现，必须作为显式 PDEC schema 准入。 | `PDEC family 无条件排斥仍开放。` |
| `NoDLSShortWindowSpecificFourthExit` | `true` | `true` | short-window 只有有限 packet、持久 PDEC、CleanKLS/DLS 或下降回流，没有专属第四出口。 | `NoDLSShortWindowSpecificSAEGap_AfterLocalPacketOrPDECReturn` |
| `DLSShortWindowSAEBoundOrNamedReturn` | `true` | `true` | 该硬点作为 short-window 命名回流 schema 已闭合。 | `不等于数值 short-window bound 已证明。` |
| `DLSPointLoadColumnCRTBoundOrNamedReturn` | `false` | `false` | PointLoad/ColumnCRT 微输入仍在最新输入基中，下一步优先攻击。 | `DLSPointLoadColumnCRTBoundOrNamedReturn` |
| `DLSFixedWheelUnitPeakDilutionOrPDECReturn` | `false` | `false` | Fixed-wheel 单位类峰稀释或 PDEC 回流仍是独立全局微输入。 | `DLSFixedWheelUnitPeakDilutionOrPDECReturn` |
| `GlobalPDECorSparseTerminalExclusion` | `false` | `false` | 若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。 | `FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

short-window 专属 gap 已删除。下一步最窄目标转到 `DLSPointLoadColumnCRTBoundOrNamedReturn`：证明 point-load 不能持续支付 DLS/BES 危险交集，或把它物化为 ColumnCRT/displacement PDEC / sparse packet 回流。
