# Prime Matrix B=3 psi_0 水平边 log-derivative 上界路由器

**状态：** `psi0_horizontal_logder_structural_reduction_open`

`Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger` 已完成结构性压缩，但未闭合。Titchmarsh 公式给出附近零点主部加 O(log T) 的结构，Leong/Trudgian 给出接近 1 线的显式外部候选；然而项目需要覆盖整个 Perron 水平边的显式常数，并把避零距离后的局部零点和 `x^s/s` 加权积分纳入 PNT 常数预算。因此外部路线的下一步不是再谈 fixed-T 缩进，而是严格匹配 `ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted`，并完成 `Psi0HorizontalWeightedIntegralBudgetLedger`；严格自足路线还需内部证明局部零点距离和。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
psi0_horizontal_logder_structural_reduction=true
psi0_horizontal_logder_self_contained_closed=false
psi0_horizontal_logder_external_strict_match_closed=false
psi0_horizontal_weighted_integral_budget_closed=false
zeta_logder_contour_shift_closed=false
row_column_unconditional_closed=false
```

## 1. 原子替换

结构性分解：

```text
Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger
  =>
(TitchmarshLocalZeroExpansionExternalRegistered AND ExplicitNearOneZetaLogDerivativeExternalRegistered AND Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger)
```

严格自足路线：

```text
Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger
  =>
(ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger AND Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger)
```

外部严格匹配路线：

```text
Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger
  =>
(ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted AND Psi0HorizontalWeightedIntegralBudgetLedger)
```

## 2. 外部来源

| source | url | used for |
| --- | --- | --- |
| Titchmarsh, The Theory of the Riemann Zeta-function, Theorem 9.6(A) | https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf | 结构性来源：zeta'/zeta 可写成附近零点主部和 O(log t) 余项；该来源不是项目级显式常数闭合。 |
| Nicol Leong, arXiv:2405.04869 | https://arxiv.org/abs/2405.04869 | 显式外部候选：给出接近 1 线的 log-derivative 显式估计；仍需检查是否覆盖本项目 whole-strip Perron 水平边。 |
| Tim Trudgian, explicit logarithmic derivative bounds | https://doi.org/10.7169/facm/2015.52.2.5 | 显式外部候选：接近 1 线时有 \|zeta'/zeta\| <= 87 log t 类型界；但原条件 t>=45 且 sigma 接近 1，不能单独覆盖全水平边。 |

## 3. 加权压力诊断

| x | T | C_away | log(xT) | diagnostic two-horizontal bound | relative to x |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 20000.000000000000 | 14.000000000000 | 87.000000000000 | 12.542544882151 | 106296023.431140109897 | 5314.801171557006 |
| 20000.000000000000 | 45.000000000000 | 87.000000000000 | 13.710150042306 | 39513511.592719502747 | 1975.675579635975 |
| 20000.000000000000 | 1000.000000000000 | 87.000000000000 | 16.811242831518 | 2673458.018062526826 | 133.672900903126 |
| 20000.000000000000 | 20000.000000000000 | 87.000000000000 | 19.806975105072 | 185558.153269133414 | 9.277907663457 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Psi0HorizontalLogDerivativeGateActive | `true` | `true` | 上一层 fixed-T 缩进归并后，条件路线下一点是水平边 away-from-zero 的 -zeta'/zeta 上界。 | Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席或数值实验替代证明。 | 保持 row_column_unconditional_closed=false。 |
| FixedTIndentExternalAvailable | `true` | `false` | 接受外部 Backlund 缩进后，近零穿越成本可条件支付；这只解决极近零点，不给 away-from-zero 全边界常数。 | ClassicalBacklundZeroIndentationCostExternalAccepted |
| FixedTIndentSelfContainedStillOpen | `true` | `true` | 严格自足路线仍同时保留 Backlund 缩进内部证明义务。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| TitchmarshLocalZeroExpansionRegistered | `true` | `false` | 经典结构公式可把 zeta'/zeta 分成附近零点主部和 O(log T) 余项。 | TitchmarshLocalZeroExpansionExternalRegistered |
| NearOneExplicitExternalRegistered | `true` | `false` | Leong/Trudgian 类型显式结果可作为右端接近 1 线的外部候选。 | ExplicitNearOneZetaLogDerivativeExternalRegistered |
| WholeStripExplicitExternalMatchMissing | `false` | `false` | 项目水平边从左边界到右边界，需 whole-strip、避零距离、端点 convention 同时匹配的显式常数；当前外部候选尚未严格覆盖。 | ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted |
| LocalZeroDistanceSumConstantMissing | `false` | `false` | Titchmarsh 结构仍需把 sum 1/\|s-rho\| 在凹口后用局部零点计数和最小距离显式化。 | Psi0HorizontalLocalZeroDistanceSumConstantLedger |
| HorizontalWeightedIntegralBudgetMissing | `false` | `false` | 即使有 pointwise log-derivative 上界，还需把 x^sigma/\|s\| 权重积分压进 Perron/PNT 常数预算。 | Psi0HorizontalWeightedIntegralBudgetLedger |
| HorizontalLogDerivativeStructuralReduction | `true` | `false` | 本步完成结构分解：外部结构公式和右端显式候选已定位，但项目级 whole-strip 常数和加权预算仍开放。 | (TitchmarshLocalZeroExpansionExternalRegistered AND ExplicitNearOneZetaLogDerivativeExternalRegistered AND Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger) |
| Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger | `false` | `false` | 自足路线和外部严格匹配路线都尚未完全关闭该水平边原子。 | self: (ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger AND Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger) ; external: (ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted AND Psi0HorizontalWeightedIntegralBudgetLedger) |
| Psi0ZetaLogDerivativeContourShiftStillOpen | `false` | `false` | fixed-T 缩进已归并，但水平边上界未闭合，所以完整轮廓移线仍未闭合。 | Psi0ZetaLogDerivativeContourShiftBoundLedger |

## 5. 最新输入基

严格自足输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ContourResidueAndLeftEdgeClosed AND (ClassicalZetaLogDerivativeAwayFromZerosInternalProofLedger AND Psi0HorizontalLocalZeroDistanceSumConstantLedger AND Psi0HorizontalWeightedIntegralBudgetLedger) AND (ClassicalBacklundZeroIndentationCostInternalProofLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger)) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

接受外部 Backlund 缩进后的输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ContourResidueAndLeftEdgeClosed AND (ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted AND Psi0HorizontalWeightedIntegralBudgetLedger) AND (ClassicalBacklundZeroIndentationCostExternalAccepted OR Psi0GoodHeightTStarAveragingContourShiftLedger)) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

内部路线先攻 `Psi0HorizontalLocalZeroDistanceSumConstantLedger`，并行保留 `ClassicalBacklundZeroIndentationCostInternalProofLedger`；外部路线先匹配 `ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted`，随后攻 `Psi0HorizontalWeightedIntegralBudgetLedger`。
