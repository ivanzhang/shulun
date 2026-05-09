# Prime Matrix B=3 Hadamard 远/近壳分离 convention 路由器

**状态：** `hadamard_shell_separation_convention_closed_half_open_dyadic`

Hadamard 远/近壳分离 convention 已闭合：目标零点、近壳核心和远壳 dyadic tail 用半开区间唯一分配，避免 target、local core 与 far tail 重复扣费。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
shell_separation_convention_closed=true
row_column_unconditional_closed=false
```

## 1. 替换

```text
HadamardFarZeroShellSeparationConventionLedger
  =>
HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic
```

## 2. 分割表

| part | definition | charged_to |
| --- | --- | --- |
| target | `rho=rho0=beta0+i gamma0` | main negative zero term -4/(sigma-beta0) |
| local_core | `rho!=rho0 and \|Im rho-gamma0\|<1` | HadamardLocalZeroCoreAbsorptionByCN16Ledger |
| far_shell_j | `2^j <= \|Im rho-gamma0\| < 2^(j+1), j>=0` | HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel |
| boundary | `exact equality goes to the lower-index half-open shell` | no double counting |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ShellSeparationGateActive | `true` | `false` | 上一层最窄点是把目标零点、近壳核心和远壳 dyadic tail 分成互斥账本。 | HadamardFarZeroShellSeparationConventionLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| KernelShapeAndCoefficientReady | `true` | `true` | 二次衰减形状和远零点系数归一化均已闭合，可安全定义远壳账本。 | HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros |
| HalfOpenDyadicPartitionClosed | `true` | `true` | 零点按 target/local_core/far half-open dyadic shells 唯一归类，边界归低阶壳，避免重复扣费。 | HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic |
| TargetZeroSeparated | `true` | `true` | 目标零点只进入 de la Vallee Poussin 主负项，不再进入远壳或局部核心余项。 | no target double charge |
| HadamardFarZeroShellSeparationConventionLedger | `true` | `true` | 远/近壳分离 convention 已闭合。 | HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic |
| HadamardOtherMicroLedgersStillOpen | `false` | `false` | Hadamard 余项还需配对/1rho 抵消、局部核心吸收和范围 convention。 | HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger AND HadamardLocalZeroCoreAbsorptionByCN16Ledger AND HadamardRemainderRangeAndKernelConventionLedger |
| CLogAggregationStillDownstream | `false` | `false` | Hadamard 四账本全闭合后，才能进入 C_log 总常数聚合。 | CLogAggregationAndRangeConventionLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionByCN16Ledger AND HadamardRemainderRangeAndKernelConventionLedger) AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

当前最窄点更新为 `HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger`；随后是 `HadamardLocalZeroCoreAbsorptionByCN16Ledger`、`HadamardRemainderRangeAndKernelConventionLedger`。
