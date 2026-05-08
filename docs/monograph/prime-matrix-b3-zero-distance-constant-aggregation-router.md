# Prime Matrix B=3 零点倒距离常数聚合路由器

**状态：** `zero_distance_constant_aggregation_external_closed_c192`

零点倒距离常数聚合在外部 Backlund/Jensen 分支中闭合为 C_distance=192。这是 eta=1/16 近零截断与 Jensen C16 计数的直接聚合；旧 C64 不能继续使用，后续窗口尺度必须按 C192 重新选择。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
zero_distance_constant_aggregation_external_closed=true
zero_distance_constant_aggregation_self_contained_closed=false
eta=0.062500000000
zero_count_constant=16.000000000000
shell_count=5
distance_constant=192.000000000000
old_distance_target_rejected=64.000000000000
row_column_unconditional_closed=false
```

## 1. 外部条件链替换

```text
BacklundZeroDistanceSumConstantAggregationLedger
  =>
BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16
```

## 2. 常数表

| quantity | value | formula | meaning |
| --- | ---: | --- | --- |
| near-zero cutoff eta | `0.062500000000` | 1/16 | eta 内零点已转入凹口成本。 |
| dyadic shell count | `5.000000000000` | ceil(log2(1/eta))+1 | 沿用旧倒距离路由器的有限层公式。 |
| zero count coefficient | `16.000000000000` | C_N | 外部 Jensen C16 局部零点计数。 |
| distance constant | `192.000000000000` | C_N*(2*shells+2) | eta 截断后的倒距离和常数。 |
| old placeholder target | `64.000000000000` | C_distance_target | 旧 64 只是 eta=1 级占位，不能继续使用。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ZeroDistanceConstantAggregationGateActive | `true` | `false` | 外部 Backlund/Jensen 分支当前最窄点是倒距离和常数聚合。 | BacklundZeroDistanceSumConstantAggregationLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条内的解析记账，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| DyadicAndNearZeroInputsAvailable | `true` | `true` | dyadic 求和形式已闭合，eta=1/16 的近零分离也已闭合。 | BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationClosedEta1Over16 |
| ExternalJensenC16CountAvailable | `true` | `false` | 每个固定局部盘的零点数由外部 Jensen C16 聚合给出。 | BacklundIndependentJensenZeroCountC16AggregationExternalClosed |
| DistanceConstantC192Computed | `true` | `true` | 按旧 dyadic 公式，eta=1/16 给出 C_distance=16*(2*5+2)=192。 | BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16 |
| OldC64PlaceholderRejected | `true` | `true` | 旧 C_distance=64 只对应无近零截断的占位；当前链条必须携带 C192 进入窗口尺度验收。 | BacklundVariationWindowScaleLedger |
| ZeroDistanceConstantAggregationClosed | `true` | `true` | 倒距离和常数已显式聚合为 C192；后续只需选择窗口尺度吸收该常数。 | BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16 |
| VariationWindowScaleNext | `false` | `false` | 下一步必须用 C192 选择短窗口尺度，不能回退到 C64。 | BacklundVariationWindowScaleLedger |
| IndentCostStillDownstream | `false` | `false` | 近零点凹口成本仍未支付。 | BacklundZeroProximityIndentationCostLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationOrCNRelaxationLedger)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional/external Backlund 输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND ClassicalFirstZetaZeroHeightGT14ExternalAccepted AND BacklundXiNoNontrivialZeroBelow14ExternalClosed) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationNotNeededC16ClosedR4)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationClosedEta1Over16 AND BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

完全自足路线仍先攻 `CriticalLineNoZeroOn0To14FiniteLedger`；外部 Backlund/Jensen 分支下一步转为 `BacklundVariationWindowScaleLedger`。
