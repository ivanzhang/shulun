# Prime Matrix early-band LocalSurvivor/SAE 命名回流 schema 路由器

**状态：** `early_band_local_survivor_schema_closed_global_shortwindow_open`

本步闭合的是 early-band LocalSurvivor/SAE 的专属无名出口：在早期零行反例分支中，孤立 early-band 窗口必须物化为有限 LocalSurvivor/SAE packet，持久同签名必须进入 PDEC，层级逃逸必须进入 CleanKLS/DLS。因此 early-band 专属 gap 被删除；但全局 DLSShortWindowSAEBoundOrNamedReturn 与 PDEC/sparse 终端排斥仍未证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
early_band_local_survivor_return_schema_closed=true
early_band_specific_gap_removed=true
pdec_or_sae_terminal_exclusion_proved=false
dls_shortwindow_global_input_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=EarlyBandLocalSurvivorOrSAEExclusion
terminal_gap_after_router=NoEarlyBandSpecificLocalSurvivorSAEGap_AfterNamedReturn
```

## 1. 替换律

```text
EarlyBandLocalSurvivorOrSAEExclusion
  =>
NoEarlyBandSpecificLocalSurvivorSAEGap_AfterNamedReturn
```

这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EarlyBandLocalSurvivorGateActive` | `true` | `true` | 当前输入基仍含 EarlyBandLocalSurvivorOrSAEExclusion，且它来自早期零行反例分支。 | `本步只攻击 early-band 专属无名出口。` |
| `EarlyZeroCounterexampleBranchGuard` | `true` | `true` | 沿用 Assume EarlyZeroRowWithinP；不使用真实样本缺席，也不宣布无条件闭合。 | `保持反例分支口径。` |
| `SAEIndependentTerminalAbsorbed` | `true` | `true` | SAE 已不是独立终端，只能成为 LocalSurvivor packet、持久 PDEC 或 CleanKLS/DLS 回流。 | `终端排斥本身仍未证明。` |
| `LocalSurvivorPacketGenerationDichotomy` | `true` | `true` | 孤窗若能抽取就是有限 packet；若同签名持久复现则进 PDEC；若层级逃逸则进 CleanKLS/DLS。 | `未来新增 packet 仍需提交 schema。` |
| `FutureSparsePacketBoundaryImported` | `true` | `true` | 当前 sparse/LocalSurvivor 前沿清零；未来新增 sparse 路线必须带 extractor schema。 | `不是全局 sparse family 无条件排斥。` |
| `PersistentEarlyBandSignatureAdmitsPDEC` | `true` | `true` | 若 early-band 局部签名在 formal 反例族中持久复现，必须提交同 formal unit PDEC schema。 | `PDEC 终端家族仍开放。` |
| `ShortWindowGlobalInputPreserved` | `true` | `true` | early-band 孤窗属于 short-window/SAE 字母表；全局 DLSShortWindow 微输入继续保留。 | `DLSShortWindowSAEBoundOrNamedReturn` |
| `NoEarlyBandSpecificFourthExit` | `true` | `true` | early-band LocalSurvivor/SAE 没有专属第四出口：孤立进 packet，持久进 PDEC，升层进 DLS。 | `NoEarlyBandSpecificLocalSurvivorSAEGap_AfterNamedReturn` |
| `EarlyBandLocalSurvivorOrSAEExclusion` | `true` | `true` | 该硬点作为 early-band 专属命名回流 schema 已闭合。 | `不等于全局 short-window/SAE 微输入已证明。` |
| `DLSShortWindowSAEBoundOrNamedReturn` | `false` | `false` | 全局 short-window SAE bound 或命名回流仍需证明；本步只是删掉 early-band 专属 gap。 | `DLSShortWindowSAEBoundOrNamedReturn` |
| `GlobalPDECorSparseTerminalExclusion` | `false` | `false` | 若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。 | `FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

early-band 专属 gap 已删除。下一步最窄目标转到全局 `DLSShortWindowSAEBoundOrNamedReturn`：证明 short-window SAE 不能持续支付 DLS/BES 危险交集，或把它物化为有限 packet / persistent PDEC schema。
