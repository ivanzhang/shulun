# Prime Matrix LowMod 有限弧 cap 归约路由器

**状态：** `lowmod_finite_arc_cap_reduced_to_lowphase_three_micro_inputs`

本步把 LowMod 有限弧 cap 质量界从独立新原子移除：固定轮弧、新增层弧和高模平坦弧分别就是既有 LowPhase 三微输入。因此下一步不应另造 LowMod 第四终端，而应直接证明 LowPhase 三微输入，或从具体 LowModDualCap 中抽取 SAE/ColumnCRT/refined PDEC 回流证书。

```text
lowmod_finite_arc_independent_input_removed=true
lowmod_finite_arc_cap_mass_bounds_closed=false
lowphase_three_micro_inputs_proved=false
row_column_unconditional_closed=false
terminal_gap_before_router=FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas
terminal_gap_after_router=LowPhaseThreeMicroInputsOrExplicitLowModDualCapReturn
```

## 1. 归约映射

| LowMod finite arc case | existing target |
| --- | --- |
| `fixed_wheel_arc` | `DLSFixedWheelUnitPeakDilutionOrPDECReturn` |
| `new_layer_arc` | `DLSNewLayerFourierConcentrationPDECReturn` |
| `high_mod_flat_arc` | `DLSFlatHighModLargeSieveAbsorption` |
| `sparse_or_displacement` | `SAE finite packet or ColumnCRT-as-PDEC` |

LowMod 弧帽不是一个新的平行终端。固定轮单位类峰、升层新增 Fourier 峰、
以及剥离后的高模平坦残余，已经分别落入 LowPhase 的三微输入。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LowModFiniteArcInputPinned` | `true` | `true` | 上一层已把 LowMod PDEC 容量失败压成未来 primitive schema 的有限弧 cap 质量界。 | `判断该有限弧 cap 是否独立于既有 LowPhase/DLS 体系。` |
| `FiniteArcIsRankOneLowPhaseSlice` | `true` | `true` | 有限循环弧 cap 是有限签名空间中的非平凡字符秩一薄片。 | `LowMod 弧帽可按 LowPhase/横向结构二分处理。` |
| `LayeredWheelClampAvailable` | `true` | `true` | 层叠轮夹击场已经给出固定轮单位类峰的命名回流口。 | `若固定轮峰持续同步，必须给 W-unit PDEC/SAE/ColumnCRT；若稀释则转新增层或平坦 DLS。` |
| `FourierInheritanceClassifiesNewLayer` | `true` | `true` | 强 Fourier 频率可区分为继承层与新增素因子层。 | `新增层集中必须给 new-layer PDEC；否则不能作为固定低模峰。` |
| `NewLayerEnergyDispersionAvailable` | `true` | `true` | 新增层能量已经与单峰集中区分开。 | `若新增层高维分散，则剩余弧帽只能进入 flat DLS/KLS 吸收。` |
| `NewLayerTowerNoUnnamedEscape` | `true` | `true` | 无限升层不能作为无名逃逸；熵发散给 PDEC，熵可求和给 CleanKLS/DLS。 | `仍需对应终端估计，而不是新增 LowMod 出口。` |
| `SparseColumnNamedReturnsPreserved` | `true` | `true` | 低支撑、孤窗和列位移弧帽不形成第四出口。 | `回流 SAE finite packet 或 ColumnCRT-as-PDEC。` |
| `LowPhaseSharedMicroInputsImported` | `true` | `false` | LowMod 有限弧 cap 的三种未闭合场景正是 LowPhase 已命名的三微输入。 | `DLSFixedWheelUnitPeakDilutionOrPDECReturn AND DLSNewLayerFourierConcentrationPDECReturn AND DLSFlatHighModLargeSieveAbsorption。` |
| `LowModFiniteArcCapMassBoundsClosed` | `false` | `false` | 上述三微输入尚未证明，因此 LowMod 有限弧 cap 质量界仍未闭合。 | `证明 LowPhase 三微输入，或提交显式 LowModDualCap 回流证书。` |

## 3. 新的最窄剩余

```text
FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas
  -> DLSFixedWheelUnitPeakDilutionOrPDECReturn
     AND DLSNewLayerFourierConcentrationPDECReturn
     AND DLSFlatHighModLargeSieveAbsorption
  or explicit LowModDualCap return to SAE/ColumnCRT/refined PDEC.
```

这一步仍不是终端证明；它关闭的是输入分类边界，说明 LowMod 有限弧 cap 不再额外增加
一个独立开放原子。真正要硬攻的是 LowPhase 三微输入或具体 DualCap 回流证书。
