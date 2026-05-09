# Prime Matrix B=3 psi_0 水平边加权积分预算路由器

**状态：** `psi0_horizontal_weighted_budget_external_closed_c12000`

`Psi0HorizontalWeightedIntegralBudgetLedger` 在外部 Titchmarsh+CN16+Backlund 条件路线下闭合。使用 pointwise `|-zeta'/zeta| <= 288 log(T+3)`，水平直段和凹口弧段统一吸收到 `12000*x*log^2(xT)/T`。这关闭水平边包，但仍只是一个很粗的 Perron 余项形状；后续还要聚合完整 `Psi0ZetaLogDerivativeContourShiftBoundLedger`，并进入零点和/PNT 数值预算。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
psi0_horizontal_weighted_integral_budget_external_closed=true
psi0_horizontal_logder_external_package_closed=true
psi0_horizontal_weighted_integral_budget_self_contained_closed=false
zeta_logder_contour_shift_closed=false
row_column_unconditional_closed=false
C_weighted_budget=12000.000000000000
```

## 1. 外部条件替换

```text
Psi0HorizontalWeightedIntegralBudgetLedger
  =>
Psi0HorizontalWeightedIntegralBudgetClosedC12000

Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger
  =>
Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosClosedByTitchmarshCN16C12000
```

## 2. 预算分解

| component | coefficient | formula | meaning |
| --- | ---: | --- | --- |
| straight horizontal segments | `1565.730333192410` | 2*e*C_logder | 两条水平直段，使用 integral x^sigma d sigma <= e*x/log x，并粗吸收到 x*log^2(xT)/T。 |
| indentation arcs | `9837.773824519947` | 4*pi*e*C_logder | 上下两侧凹口弧长用 2*pi*eta*N(T,1) 和 C_N log(T+3) 粗付。 |
| rounded reserve | `12000.000000000000` | ceil reserve above straight+arcs | 给端点、半权和 log(T+3)<=log(xT) 的口径转换留余量。 |

## 3. 压力诊断

| x | T | log(xT) | budget bound | relative to x |
| ---: | ---: | ---: | ---: | ---: |
| 20000.000000000000 | 14.000000000000 | 12.542544882151 | 2696835979.213404655457 | 134841.798960670247 |
| 20000.000000000000 | 45.000000000000 | 13.710150042306 | 1002497142.306962728500 | 50124.857115348139 |
| 20000.000000000000 | 1000.000000000000 | 16.811242831518 | 67828292.529665812850 | 3391.414626483291 |
| 20000.000000000000 | 20000.000000000000 | 19.806975105072 | 4707795.153755425476 | 235.389757687771 |
| 20000.000000000000 | 1000000.000000000000 | 23.718998110500 | 135021.809127821180 | 6.751090456391 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Psi0HorizontalWeightedBudgetGateActive | `true` | `true` | 上一层已给出 pointwise C=288 log(T+3)，当前任务是把 x^s/s 权重积分纳入 Perron 余项。 | Psi0HorizontalWeightedIntegralBudgetLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席或数值实验替代证明。 | 保持 row_column_unconditional_closed=false。 |
| LocalZeroDistanceC288Available | `true` | `false` | 外部 Backlund/RVM 条件路线已给出水平边 pointwise log-derivative 系数 C=288。 | Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16 |
| StraightHorizontalWeightedBoundClosed | `true` | `true` | 两条水平直段由 \|s\|>=T、x^(1+1/log x)<=e*x 和 integral x^sigma d sigma 控制。 | 2*e*C_logder |
| IndentArcWeightedBoundClosed | `true` | `true` | 凹口弧段由 eta=1/16、局部零点计数和弧长 2*pi*eta*N 控制，统一吸收到 x log^2(xT)/T。 | 4*pi*e*C_logder |
| WeightedBudgetC12000MarginClosed | `true` | `true` | 直段与弧段总系数低于 12000，端点和口径转换留在余量内。 | Psi0HorizontalWeightedIntegralBudgetClosedC12000 |
| Psi0HorizontalWeightedIntegralBudgetLedger | `true` | `false` | 外部 Titchmarsh+CN16+Backlund 条件路线下，水平边加权积分预算闭合为 C=12000。 | Psi0HorizontalWeightedIntegralBudgetClosedC12000 |
| HorizontalLogDerivativeExternalPackageClosed | `true` | `false` | 局部零点倒距离和与加权预算都关闭后，水平边 log-derivative 包可在该条件路线下关闭。 | Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosClosedByTitchmarshCN16C12000 |
| SelfContainedWeightedBudgetStillOpen | `false` | `false` | 严格自足路线仍缺自足 Backlund 缩进和自足 C_N=16，因此不能同步关闭。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| ContourShiftAggregationNext | `false` | `false` | 下一步需要把留数左边界、fixed-T 缩进和水平边包合并，关闭外部条件轮廓移线。 | Psi0ZetaLogDerivativeContourShiftExternalAggregationLedger |

## 5. 最新输入基

外部 Titchmarsh+CN16 路线输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ContourResidueAndLeftEdgeClosed AND (Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosClosedByTitchmarshCN16C12000) AND (ClassicalBacklundZeroIndentationCostExternalAccepted OR Psi0GoodHeightTStarAveragingContourShiftLedger)) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

下一步攻 `Psi0ZetaLogDerivativeContourShiftExternalAggregationLedger`，随后进入 `ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger`。
