# Prime Matrix DLS point-load/ColumnCRT 命名回流 schema 路由器

**状态：** `dls_pointload_columncrt_return_schema_closed_terminal_exclusion_open`

本步闭合的是 DLS point-load/ColumnCRT 的专属命名回流 schema：单点高负载若平衡则不能支付缺陷预算；若持久则给出有限列位移或尾锚签名并进入 PDEC/ColumnCRT；若孤立则进入 SAE/LocalSurvivor packet。因此 point-load 专属无名出口被删除；但 PDEC/ColumnCRT/SAE 终端排斥和 fixed-wheel 微输入仍未证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
dls_pointload_return_schema_closed=true
dls_pointload_specific_gap_removed=true
columncrt_independent_terminal_removed=true
pdec_columncrt_sae_terminal_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=DLSPointLoadColumnCRTBoundOrNamedReturn
terminal_gap_after_router=NoDLSPointLoadColumnCRTSpecificGap_AfterDisplacementPDECOrSAEReturn
```

## 1. 替换律

```text
DLSPointLoadColumnCRTBoundOrNamedReturn
  =>
NoDLSPointLoadColumnCRTSpecificGap_AfterDisplacementPDECOrSAEReturn
```

这一步仍处于反例分支/终端证书口径，不使用真实样本缺席。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DLSPointLoadGateActive` | `true` | `true` | 当前输入基仍含 DLSPointLoadColumnCRTBoundOrNamedReturn，且它来自 BES/DLS 三出口字母表。 | `本步只攻击 point-load 专属无名出口。` |
| `PointLoadAlphabetPinned` | `true` | `true` | DLS 点负载只能回流 ColumnCRT、tail-anchor 或 displacement PDEC。 | `不能作为 BES 同步失败黑箱。` |
| `ColumnCRTIndependentExitAbsorbed` | `true` | `true` | ColumnCRT 不是独立终端；持久非零位移是 displacement PDEC，孤立位移是 SAE/endpoint。 | `位移 PDEC/SAE 终端排斥仍未证明。` |
| `FiniteDisplacementSignature` | `true` | `true` | 点负载若持续，给出有限列位移签名 sigma_col=(ell,d mod ell) 或其细化。 | `同签名持久进入 PDEC。` |
| `BalancedPointLoadCannotPayDefectBudget` | `true` | `true` | 若所有非零位移余类均不超载，则 ColumnCRT/point-load 不能承担命名缺陷预算。 | `这是 BoundOrNamedReturn 中的 bound 侧。` |
| `TailAnchorPointLoadAbsorbed` | `true` | `true` | 若 point-load 实为尾锚/互补因子锚，持久进 PDEC/ColumnCRT，孤立进 SAE。 | `尾锚排斥仍归终端证书。` |
| `PersistentPointLoadAdmitsPDEC` | `true` | `true` | 同一 point-load/位移/尾锚签名持久复现，必须作为显式 PDEC schema 准入。 | `PDEC family 无条件排斥仍开放。` |
| `SparsePointLoadAdmitsSAE` | `true` | `true` | 若 point-load 只孤立出现，必须物化为有限 SAE/LocalSurvivor packet schema。 | `不是全局 sparse family 无条件排斥。` |
| `NoDLSPointLoadSpecificFourthExit` | `true` | `true` | point-load 只有平衡不足、持久 PDEC/ColumnCRT、孤立 SAE 或 tail-anchor 回流，没有专属第四出口。 | `NoDLSPointLoadColumnCRTSpecificGap_AfterDisplacementPDECOrSAEReturn` |
| `DLSPointLoadColumnCRTBoundOrNamedReturn` | `true` | `true` | 该硬点作为 point-load 命名回流 schema 已闭合。 | `不等于全局 PDEC/ColumnCRT/SAE 排斥已证明。` |
| `DLSFixedWheelUnitPeakDilutionOrPDECReturn` | `false` | `false` | Fixed-wheel 单位类峰稀释或 PDEC 回流仍是最新最窄微输入。 | `DLSFixedWheelUnitPeakDilutionOrPDECReturn` |
| `GlobalPDECorSparseTerminalExclusion` | `false` | `false` | 若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。 | `FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

point-load 专属 gap 已删除。下一步最窄目标转到 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`：证明固定轮单位类峰被层叠轮稀释，或把持久单位峰登记为 PDEC。
