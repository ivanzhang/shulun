# Prime Matrix clean-core BES-DLS 命名回流攻关路由器

**状态：** `bes_dls_named_return_reduced_to_three_exit_microinputs`

BES-DLS 输入的作用是删除高 L1/高 L2 同步失败的无名出口。中心化核与危险交集代数已固定；若危险交集出现，二次能量只能通过 PointLoad、ShortWindow 或 LowPhase 三种可登记形态承担。PointLoad 回流 ColumnCRT/displacement PDEC，ShortWindow 回流 SAE/LocalSurvivor 或持久 PDEC，LowPhase 回流 W-unit/new-layer PDEC 或 flat DLS。因此最新剩余不是 BES 大口径，而是这三类出口的实际排斥或命名回流证明。

```text
bes_dls_named_return_boundary_closed=true
dls_kernel_and_danger_algebra_closed=true
bes_dls_named_return_input_proved=false
row_column_unconditional_closed=false
```

## 1. 近危险摘要

| metric | value |
| --- | ---: |
| record_count | `10` |
| max_l1_over_sqrt | `2.468627` |
| max_l2_over_sqrt | `1.233496` |
| max_effective_dimension | `5.938250` |
| max_point_load | `4` |
| max_short_window_positive_over_sqrt | `0.381667` |
| max_low_phase_positive_over_sqrt | `0.902430` |
| all_top_low_phase_residues_are_units | `true` |

这些数值只用于定位出口优先级，不作为无条件证明。

## 2. 三出口微输入

| exit | diagnostic | route | micro_input | closed | meaning |
| --- | --- | --- | --- | --- | --- |
| PointLoad | nearmiss max point load = 4 | ColumnCRT / tail-anchor / displacement PDEC | `DLSPointLoadColumnCRTBoundOrNamedReturn` | `false` | 若单点高素标签负载可持续超阈值，则固定列位移或尾锚签名必须回流 ColumnCRT/PDEC；否则不能支付 BES 危险交集。 |
| ShortWindow | nearmiss max short-window positive = 0.381667 sqrt(S) | SAE / LocalSurvivor / persistent sparse PDEC | `DLSShortWindowSAEBoundOrNamedReturn` | `false` | 若短 q 子窗承担固定比例正偏差，则必须生成有限 LocalSurvivor/SAE packet，或持久化为 PDEC。 |
| LowPhase | nearmiss max low-phase positive = 0.902430 sqrt(S); top residues unit=true | W-unit PDEC / new-layer PDEC / flat DLS | `DLSLowPhasePDECNewLayerOrFlatDLSBound` | `false` | 若分散正偏差在单位类或新增轮层 Fourier 方向同步，则给出 PDEC；若每层分散，则必须由高模 DLS 大筛吸收。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreviousBESDLSInputPinned | `true` | `true` | 上一层已把 DPRC 正偏差锁压到 BES 危险交集排斥或 DLS 命名回流。 | 单独攻击 BES-DLS 输入。 |
| DLSKernelAndDangerAlgebraClosed | `true` | `true` | 中心化核、危险交集、尖峰桶鸽巢和二次能量展开已经形式化。 | 把二次能量超额严格送入三出口。 |
| DLSPointShortLowAlphabetClosed | `true` | `false` | DLS 失败字母表已固定为 PointLoad、ShortWindow、LowPhase。 | 证明该三分覆盖所有 BES 危险失败，而非只是证明路线。 |
| NearmissThreeExitDiagnosticsMaterialized | `true` | `false` | 近危险审计显示 PointLoad 不爆炸，ShortWindow 不够强，最稳定信号是单位类内部 LowPhase。 | 审计不能替代全局排斥证明。 |
| ColumnCRTIndependentExitAbsorbed | `true` | `false` | PointLoad 若形成列位移持久过载，不是独立终端，而是 displacement PDEC 或 SAE。 | 仍需证明 DLSPointLoadColumnCRTBoundOrNamedReturn。 |
| SAEIndependentExitAbsorbed | `true` | `false` | ShortWindow 若形成孤窗逃逸，不是独立终端，而是 LocalSurvivor packet 或持久 PDEC。 | 仍需证明 DLSShortWindowSAEBoundOrNamedReturn。 |
| LowPhaseLayeredPDECRouteClosed | `true` | `false` | LowPhase 已接入 W-unit/new-layer PDEC 与 flat DLS 二分。 | 证明 DLSLowPhasePDECNewLayerOrFlatDLSBound。 |
| BESDLSNamedReturnInputProved | `false` | `false` | BES-DLS 输入未闭合；它被拆成三出口微输入。 | DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSLowPhasePDECNewLayerOrFlatDLSBound |
| DStructureRankinStillIndependent | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | BES-DLS、signed 源锁和模型余量完成后仍需独立验收。 |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSLowPhasePDECNewLayerOrFlatDLSBound AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSLowPhasePDECNewLayerOrFlatDLSBound AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 当前结论

本步关闭的是 BES-DLS 的命名边界：危险交集不能再作为无名同步失败保留。它必须进入 PointLoad、ShortWindow 或 LowPhase 三类微输入。当前材料没有证明三类微输入，也没有闭合无条件行/列命题；下一最窄优先级是 LowPhase 的 W-unit/new-layer PDEC 或 flat DLS 排斥。
