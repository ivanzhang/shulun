# Prime Matrix LowMod-new-layer 桥接路由器

**状态：** `lowmod_newlayer_atom_bridged_to_schema_and_flat_admission`

本步把 LowMod 有限弧路径中的新增层子口接入既有 new-layer 投影切片链：DLSNewLayerFourierConcentrationPDECReturn 不再作为整块终端保留，而被替换为合法 new-layer PDEC schema 准入与无集中 flat admission 两项。

```text
lowmod_newlayer_bridge_closed=true
newlayer_schema_proved=false
newlayer_flat_admission_proved=false
row_column_unconditional_closed=false
terminal_gap_before_router=DLSNewLayerFourierConcentrationPDECReturn
terminal_gap_after_router=RegisteredNewLayerPDECFormalUnitAndCapStableSchema_AND_NewLayerNoConcentrationImpliesFlatAdmission
```

## 1. 替换律

```text
DLSNewLayerFourierConcentrationPDECReturn
  =>
RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission.
```

含义是：强新增层 Fourier 集中若存在，必须通过确定性切片形成同 formal unit 的 PDEC cap；
若不存在可登记的低维集中，则剩余对象必须满足 flat-DLS/KLS 准入，而不能停在“无集中”这句话上。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LowModFiniteArcReducedToLowPhase` | `true` | `true` | 上一层已把 LowMod 有限弧 cap 并入 LowPhase 三微输入。 | `接入已存在的 new-layer 子口压缩结果。` |
| `LowPhaseNewLayerAtomPinned` | `true` | `true` | LowPhase 路由中新增层子口仍以 DLSNewLayerFourierConcentrationPDECReturn 出现。 | `用 new-layer 外部匹配/投影切片链替换它。` |
| `ExternalLemmaDirectShortcutRejected` | `true` | `true` | 外部 KLS/FullS 引理不能直接替代新增层子口。 | `必须先给投影/PDEC 准入或无集中 flat admission。` |
| `ProjectionSlicerClosedToSchema` | `true` | `true` | 投影单调与 Fourier-to-cap 确定性切片已闭合。 | `剩余为合法 new-layer PDEC schema 准入。` |
| `NewLayerAtomBridgeClosed` | `true` | `true` | DLSNewLayerFourierConcentrationPDECReturn 已被替换为两个更原子的输入。 | `RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission。` |
| `NewLayerSchemaAndFlatAdmissionStillOpen` | `false` | `false` | new-layer PDEC schema 准入和无集中 flat admission 尚未证明。 | `先攻 RegisteredNewLayerPDECFormalUnitAndCapStableSchema；随后攻 NewLayerNoConcentrationImpliesFlatAdmission。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

最窄优先目标为 `RegisteredNewLayerPDECFormalUnitAndCapStableSchema`。这一步仍不闭合行/列无条件命题；它只关闭 LowMod 有限弧路径与 new-layer 子口之间的接线缺口。
