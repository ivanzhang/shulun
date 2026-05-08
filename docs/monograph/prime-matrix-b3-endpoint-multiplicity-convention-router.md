# Prime Matrix B=3 端点避零与重数 convention 闭合证书

**状态：** `endpoint_zero_avoidance_multiplicity_convention_closed_by_limit`

端点避零与重数 convention 已闭合：所有边界落零先用 epsilon 避开，在避零边界上应用 argument principle，再取极限并按解析重数计入。这只解决定义一致性，不证明新的零点分布，也不关闭行列无条件命题。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
endpoint_multiplicity_convention_closed=true
row_column_unconditional_closed=false
```

## 1. 自足与外部替换

自足输入基：

```text
EndpointZeroAvoidanceMultiplicityConventionLedger
  =>
EndpointZeroAvoidanceMultiplicityConventionClosedByLimit
```

外部 Backlund 输入基：

```text
EndpointZeroAvoidanceMultiplicityConventionLedger
  =>
EndpointZeroAvoidanceMultiplicityConventionClosedByLimit
```

## 2. 极限 convention

```text
N_closed([A,B]) = lim_{epsilon->0+} N_avoiding((A-epsilon, B+epsilon)), with boundary zeros counted by analytic multiplicity.
```

| step | content |
| --- | --- |
| finite_multiplicity | xi 是整函数；紧矩形内零点离散且每个零点重数有限。 |
| avoidance_sequence | 对给定端点高度 T，取 epsilon_j -> 0，使 T±epsilon_j 不等于任何零点虚部。 |
| argument_principle_first | 先在避开零点的边界上应用 argument principle 或 Littlewood 矩形恒等式。 |
| multiplicity_limit | 令 epsilon_j -> 0，边界零点以解析重数完整计入闭区间零点计数。 |
| no_constant_charge | 端点 convention 只改变计数定义，不额外支付 pi 跳变、C_S 常数或 C_N 常数。 |

关键点是：端点落零不产生新的分析估计。先绕开、后取极限；跳变由零点重数账本吸收，近零点绕行成本仍归属 Backlund 凹口账本，不能在这里重复扣费或伪造余量。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EndpointConventionGateActive | `true` | `false` | 外部 Backlund 分支当前最窄点是端点避零与重数 convention；自足输入基中也含同一 atom。 | EndpointZeroAvoidanceMultiplicityConventionLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条内的解析记账，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| XiFiniteMultiplicityAvailable | `true` | `true` | xi 已作为整函数进入输入基，因此紧区域内零点离散且重数有限。 | XiEntireOrderOneGrowthClosed |
| ArgumentPrincipleCompatible | `true` | `true` | 已有 xi 矩形 argument principle；端点落零时可先扰动边界再取极限。 | ArgumentPrincipleXiRectangleCountingClosed |
| AvoidingSequenceAndLimitClosed | `true` | `true` | 选择避开零点虚部的 epsilon 序列，在避零边界上计数，再令 epsilon->0，边界零点按重数进入闭区间。 | EndpointZeroAvoidanceMultiplicityConventionClosedByLimit |
| NoBudgetDoubleCounting | `true` | `true` | 端点 convention 不重复扣减凹口成本，也不新增 C_S 或 C_N 常数；所有近零点绕行成本仍属于既有 Backlund 凹口账本。 | 无新常数。 |
| ExternalBacklundInputsPreserved | `true` | `false` | 外部 Backlund 常数链已到 C_S=8 紧等号；本步只补端点定义，不改变该预算。 | BacklundCS8SlackAfterBridgeClosedTightHalf |
| EndpointZeroAvoidanceMultiplicityConventionLedger | `true` | `true` | 端点避零与重数 convention 已由极限定义闭合。 | EndpointZeroAvoidanceMultiplicityConventionClosedByLimit |
| RVMToCN16Next | `false` | `false` | 端点 convention 关闭后，外部 Backlund 分支下一硬点转到 RVM 到 C_N=16 的局部计数合并。 | RVMToCN16LocalInequalityLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationOrCNRelaxationLedger)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionClosedByLimit AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional/external Backlund 输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND ClassicalFirstZetaZeroHeightGT14ExternalAccepted AND BacklundXiNoNontrivialZeroBelow14ExternalClosed) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationNotNeededC16ClosedR4)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationClosedEta1Over16 AND BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16) AND BacklundVariationWindowScaleClosedH1Over512C192) AND ClassicalBacklundZeroIndentationCostExternalAccepted)) AND BacklundCS8SlackAfterBridgeClosedTightHalf)) AND EndpointZeroAvoidanceMultiplicityConventionClosedByLimit AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

完全自足路线仍先攻 `CriticalLineNoZeroOn0To14FiniteLedger`；外部 Backlund 分支下一步转为 `RVMToCN16LocalInequalityLedger`。
