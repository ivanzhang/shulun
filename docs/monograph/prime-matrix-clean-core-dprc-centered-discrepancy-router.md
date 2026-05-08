# Prime Matrix clean-core DPRC 中心化偏差攻关路由器

**状态：** `dprc_centered_discrepancy_reduced_to_modelgap_and_bes_dls`

DPRC 的中心化偏差锁不再是原始 T_Y<S_Y。RSM 恒等式把它拆成显式模型余量/有限证书与 D_+ 平方根界；BES 又把 D_+ 平方根界拆成六个 beta 桶的高 L1 与高 L2 不能同步。若同步失败不能直接排斥，DLS 路线要求它显化为 PointLoad、ShortWindow 或 LowPhase，分别回流 ColumnCRT、SAE 或 PDEC/new-layer PDEC。

```text
dprc_centered_discrepancy_boundary_closed=true
rsm_identity_closed=true
bes_compression_closed=true
dprc_centered_discrepancy_input_proved=false
row_column_unconditional_closed=false
```

## 1. 新压缩律

```text
DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn
  => ExplicitModelGapAndFiniteDPRCLedger
     AND BESDangerIntersectionExclusionOrDLSNamedReturn。
```

`ExplicitModelGapAndFiniteDPRCLedger` 支付 `P<2003` 的有限段和 `P>=2003` 的 `S(1-H)>3sqrt(S)` 模型余量。`BESDangerIntersectionExclusionOrDLSNamedReturn` 支付 `D_+<=3sqrt(S)`；若高正和和高能量同步不能排斥，必须回流 `PointLoad/ColumnCRT`、`ShortWindow/SAE` 或 `LowPhase/PDEC`。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreviousDPRCInputPinned | `true` | `true` | 上一层已把几何预算的解析锁命名为 DPRC alpha=0.43 中心化偏差或层叠回流。 | 把 DPRC 输入继续原子化。 |
| RSMIdentityClosed | `true` | `true` | DPRC 容量闭合已等价降到模型余量 S(1-H) 与正偏差 D_+ 的比较。 | 提交显式 ModelGap/finite 证书与 D_+ 平方根界。 |
| FiniteCapacityAuditMaterialized | `true` | `false` | P<2003 和全扫到 P<=100000 的容量失败为零，有限证书数据已物化。 | 把 P<2003 固化为正式有限验收表。 |
| HighSegmentC3AuditMaterialized | `true` | `false` | 审计显示 P>=2003 时 C=3 同时支付模型余量和正偏差。 | 证明 ExplicitModelGapAndFiniteDPRCLedger，而不是只引用实验。 |
| BESCompressionClosed | `true` | `true` | D_+<=3sqrt(S) 被压成六个 beta 桶的高 L1 与高 L2 不能同步。 | 证明 BES 危险交集不存在或命名回流。 |
| BESDangerAuditClear | `true` | `false` | P<=100000 审计中两个 BES 危险交集均为零。 | 需要解析排斥，不可作为无条件证明。 |
| DLSNamedReturnGrammarClosed | `true` | `false` | 若 BES 危险交集发生，当前路线把失败拆成 PointLoad/ShortWindow/LowPhase 三出口。 | 证明三出口必然性，且分别吸收到 ColumnCRT/SAE/PDEC。 |
| NewLayerDispersionEvidenceAvailable | `true` | `false` | 新增层 Fourier 能量强但高 BES 压力处峰值分散，支持 LowPhase=>new-layer PDEC 或 DLS 吸收。 | 证明相位维数下界或低维集中必给 new-layer PDEC。 |
| DPRCAlpha043CenteredDiscrepancyInputProved | `false` | `false` | DPRC 输入未闭合；已压成 ModelGap/finite 账本与 BES/DLS 命名回流。 | ExplicitModelGapAndFiniteDPRCLedger AND BESDangerIntersectionExclusionOrDLSNamedReturn。 |
| DStructureRankinStillIndependent | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | DPRC 与 signed 源锁完成后仍需独立验收。 |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND BESDangerIntersectionExclusionOrDLSNamedReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND BESDangerIntersectionExclusionOrDLSNamedReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 当前结论

本步关闭的是 DPRC 的接口层：原始容量不等式已归约到模型余量/有限账本与 BES-DLS 危险交集。当前材料仍未给出这些输入的无条件证明，也未闭合行/列命题。
