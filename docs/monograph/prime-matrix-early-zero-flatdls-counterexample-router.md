# Prime Matrix 早期零行反例 flat-DLS 最后逃逸路由器

**状态：** `early_zero_flatdls_reduced_to_l2flat_kls_spectral_escape`

本步把 DLSFlatHighModLargeSieveAbsorption 放回早期零行反例分支中解释：反例若仍靠高模平坦残余支付零行，任何短窗、低模、列频率或 Bohr-cap 集中都会回流 SAE/PDEC/ColumnCRT；真正剩下的唯一逃逸是 L2-flat KLS 谱逃逸。因此下一步不是证明真实分布本身，而是排斥这个反例专属的 L2-flat 谱逃逸。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
early_zero_flatdls_last_escape_boundary_closed=true
dls_flat_highmod_large_sieve_absorption_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=DLSFlatHighModLargeSieveAbsorption
terminal_gap_after_router=EarlyZeroL2FlatKLSCounterexampleSpectralExclusion_OR_CDependentResidueWeightSpectralCancellationInput
```

## 1. 反例链条

```text
Assume EarlyZeroRowWithinP
named low-dimensional exits removed
flat-DLS residual must pay remaining zero-row budget
SN3-A/B low projection peak => SAE/PDEC/ColumnCRT
SN3-C multiband sync => ShellOverlap/LowModSync/KLS-Multishell
SN3-D KLS-Multishell => HighFrequencyColumn or L2FlatKLS
SN3-E HighFrequencyColumn => Bohr-cap PDEC/ColumnCRT/SAE or L2-flat CleanKLS
only last escape: L2-flat KLS spectral/NC-BLK input
```

这条链条的前提始终是 `Assume EarlyZeroRowWithinP`。真实样本中没有早期零行只作定位，不作为证明。

## 2. 替换律

```text
DLSFlatHighModLargeSieveAbsorption
  =>
EarlyZeroL2FlatKLSCounterexampleSpectralExclusion
```

在条件/外部版中，完成型谱输入仍可由 `CDependentResidueWeightSpectralCancellationInput` 承担。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EarlyZeroCounterexampleAssumptionPinned` | `true` | `true` | 本路由只在假设存在 P 行以内早期零行的反例分支中工作。 | `不使用真实样本未见零行作为证明。` |
| `FlatDLSGateActiveInCounterexampleBasis` | `true` | `true` | 上一层已把 new-layer 无集中 residual 准入到 DLSFlatHighModLargeSieveAbsorption。 | `现在必须把它解释为反例最后支付压力，而不是普通真实分布估计。` |
| `EmpiricalShortcutExplicitlyBlocked` | `true` | `true` | 早期零行矛盾矩阵已声明：真实样本中未见早期零行不能替代假设分支证明。 | `所有结论必须从反例支付压力推出。` |
| `SN3LowProjectionPeelingInherited` | `true` | `true` | 若 flat-DLS 支付出现短窗、q 低模或 d 低模峰，则 SN3-A/B 直接回流 SAE/PDEC/ColumnCRT。 | `剩余才是 TrueDistributedDLS。` |
| `SN3MultibandSyncSplitInherited` | `true` | `true` | 同行多真分散带若有 ShellOverlap 或 LowModSync，分别回流 SAE 或 PDEC/ColumnCRT。 | `剩余才是 KLS-Multishell。` |
| `SN3ColumnFrequencyDichotomyInherited` | `true` | `true` | KLS-Multishell 的有限列 Fourier 二分给出 HighFrequencyColumn 或 L2FlatKLS。 | `非零列频率不是无名 flat-DLS 质量。` |
| `HighFrequencyBohrCapNoCycleInherited` | `true` | `true` | HighFrequencyColumn 必须成为 Bohr-cap，并回流 PDEC/ColumnCRT/SAE，或退化为 L2-flat CleanKLS。 | `高频出口不能形成无名循环。` |
| `CleanKLSAdmissionAndExternalInterfaceRegistered` | `true` | `false` | L2-flat CleanKLS 只有在 K1--K9 准入通过后才能调用；外部 KLS 输入已登记。 | `自足版仍需实际谱/dispersion 估计。` |
| `CDependentSpectralReductionKnownButOpen` | `true` | `false` | 完成型 c-dependent residue 谱输入已接到 BWFD/BSC/KFLS/NC-BLK 核心链。 | `NCBLKActualBlockNonConcentrationOrExternalDIBFI 仍未证明或接受。` |
| `EarlyZeroFlatDLSLastEscapeBoundaryClosed` | `true` | `true` | 早期零行反例的 flat-DLS 最后逃逸已被压成唯一 L2-flat KLS 谱逃逸或命名 Bohr/PDEC/SAE/ColumnCRT 回流。 | `它不再是直接真实分布证明口。` |
| `EarlyZeroL2FlatKLSCounterexampleSpectralExclusion` | `false` | `false` | 尚未证明早期零行反例所需的 L2-flat 高频残余谱吸收或实际 NC-BLK 排斥。 | `下一步最窄目标。` |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND EarlyZeroL2FlatKLSCounterexampleSpectralExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND EarlyZeroL2FlatKLSCounterexampleSpectralExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

最窄目标更新为 `EarlyZeroL2FlatKLSCounterexampleSpectralExclusion`：在假设早期零行存在的反例分支中，证明 L2-flat 高频 KLS 残余不能继续支付零行余量；若证明失败，必须输出同 formal unit 的高频 Bohr/PDEC/SAE/ColumnCRT 证书，或明确接受/匹配 `CDependentResidueWeightSpectralCancellationInput`。
