# Prime Matrix clean-core DLS LowPhase PDEC/flat DLS 攻关路由器

**状态：** `dls_lowphase_reduced_to_fixedwheel_newlayer_flatdls`

LowPhase 不是单个固定模规律。固定轮单位类峰若持续同步，给 W-unit PDEC；升层后若新增 Fourier 频率低维集中，给 new-layer PDEC；若固定轮和新增层均被稀释，剩余只能是高模平坦分散能量，必须由 flat DLS/KLS 大筛吸收。因此 LowPhase 输入被拆成固定轮峰稀释/回流、新增层集中/回流、flat DLS 吸收三项。

```text
dls_lowphase_boundary_closed=true
lowphase_input_proved=false
row_column_unconditional_closed=false
```

## 1. 审计摘要

| metric | value |
| --- | --- |
| W=30 max peak | `1.076781` |
| W=30 high-L1 max peak | `0.902430` |
| W=30 max L1 when peak>=0.8 | `2.442672` |
| W=30 max L2 when peak>=0.8 | `1.177635` |
| layered danger count | `0` |
| layered cauchy danger count | `0` |
| Fourier representative danger count | `0` |

层叠轮最大单位峰：

| W | max peak | high-L1 max peak |
| ---: | ---: | ---: |
| `30` | `1.076781` | `0.902430` |
| `210` | `0.617936` | `0.331095` |
| `2310` | `0.293727` | `0.175276` |

Fourier 继承代表样本：

| W | class_histogram | new_factor_histogram | max Fourier/sqrt | max centered peak/sqrt |
| ---: | --- | --- | ---: | ---: |
| `30` | `{'base': 8}` | `{}` | `1.833925` | `1.021564` |
| `210` | `{'inherited': 2, 'new-layer': 6}` | `{'7': 6}` | `2.168333` | `0.611625` |
| `2310` | `{'new-layer': 8}` | `{'11': 8}` | `2.252895` | `0.292146` |

这些读数只用于定位结构，不是证明。

## 2. 三个 LowPhase 微输入

| micro_input | route | closed | evidence | meaning |
| --- | --- | --- | --- | --- |
| `DLSFixedWheelUnitPeakDilutionOrPDECReturn` | fixed W-unit PDEC or dilution | `false` | W=30 max peak=1.076781, high-L1 max peak=0.902430 | 固定轮单位类峰若与 BES 危险同步，必须给出 W-unit PDEC；若不同步，固定轮不能支付 LowPhase 危险质量。 |
| `DLSNewLayerFourierConcentrationPDECReturn` | new-layer PDEC or phase-dimension lower bound | `false` | Fourier 继承分类显示 W=2310 的代表强频率全部进入新增因子 11 层。 | 新增层强频率若低维集中，则给 new-layer PDEC；若高维分散，则不能形成单位相位尖峰。 |
| `DLSFlatHighModLargeSieveAbsorption` | flat high-mod DLS/KLS absorption | `false` | 新增层能量强但高 BES 压力处 centered peak 明显下降。 | 若固定轮与新增层均不集中，剩余 LowPhase 必须由真正高模平坦大筛吸收。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreviousLowPhaseInputPinned | `true` | `true` | 上一层已把 BES-DLS 最窄优先级定位为 LowPhase 的 PDEC/new-layer/flat DLS 二分。 | 单独攻击 LowPhase 输入。 |
| WheelUnitPhaseBalanceRouteAvailable | `true` | `false` | 固定轮和层叠轮单位类相位账本已建立。 | 证明固定轮峰同步必给 PDEC，或证明峰随层提升不能支付 BES 危险交集。 |
| CurrentAuditDangerSyncClear | `true` | `false` | P<=100000 的层叠轮审计中 BES 危险交集为零。 | 审计不是全局证明。 |
| FourierInheritanceNewLayerRouteAvailable | `true` | `false` | 代表样本的强 Fourier 频率可分为继承层与新增层，新增层偏斜可命名为 new-layer PDEC。 | 证明新增层低维集中必给 PDEC，或证明集中不能与 BES 危险同步。 |
| NewLayerEnergyDispersionRouteAvailable | `true` | `false` | 新增层能量恒等式已把强能量与单峰集中区分开。 | 证明 phase-dimension 下界推出 flat DLS 吸收。 |
| NewLayerPDECTowerNoUnnamedEscape | `true` | `false` | 若不断升层出现新增层偏斜，已有塔熵合同要求它进入 profinite/new-layer PDEC 或 CleanKLS。 | 仍需实际 PDEC/flat DLS 终端证明。 |
| FlatDLSAbsorptionInterfaceAvailable | `true` | `false` | 低维峰剥离后的平坦分散残余已有 SN3/DLS 接口。 | 证明 DLSFlatHighModLargeSieveAbsorption。 |
| LowPhasePDECFlatInputProved | `false` | `false` | LowPhase 输入未闭合；它被拆成固定轮峰、新增层集中和平坦高模吸收三项。 | DLSFixedWheelUnitPeakDilutionOrPDECReturn AND DLSNewLayerFourierConcentrationPDECReturn AND DLSFlatHighModLargeSieveAbsorption |
| DStructureRankinStillIndependent | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | LowPhase、其余 DLS 微输入、signed 源锁和模型余量完成后仍需独立验收。 |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND DLSNewLayerFourierConcentrationPDECReturn AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND DLSNewLayerFourierConcentrationPDECReturn AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 当前结论

本步关闭的是 LowPhase 的路线边界：它不能再作为一个整体黑箱。下一步应直接攻 fixed-wheel 峰稀释/new-layer PDEC/flat DLS 三个微输入，其中最贴近现有结构材料的是 `DLSNewLayerFourierConcentrationPDECReturn`。
