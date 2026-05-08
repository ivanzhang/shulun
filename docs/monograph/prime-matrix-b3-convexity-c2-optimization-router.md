# Prime Matrix B=3 临界带凸性 C=2 常数优化闭合证书

**状态：** `critical_strip_convexity_c2_closed`

临界带凸性 C=2 常数优化已闭合。关键是不用上一层 C_left=4 的粗合并，而在优化层重新使用尖锐 chi、pole 和右边界 zeta 预算；单变量余量在 T>=2 上保持正值。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
critical_strip_convexity_c2_closed=true
C_convexity=2.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
CriticalStripConvexityC2ConstantOptimizationLedger
  =>
CriticalStripConvexityClosedC2
```

## 2. 核心不等式

```text
L=log(T+3), eta=1/L, T>=2: log|chi(-eta+it)|<=0.5L, log|s-1|<=log(T+2), log|zeta(1+eta-it)|<=log(1+L), and 0.5L+log(T+2)+log(1+L)<2L.
```

单变量余量审计：

```text
T_minimizer=4.141261010285
margin_at_minimizer=0.046627017338
derivative_at_minimizer=0.000000000000
margin_at_T2=0.068727668610
margin_at_T20=0.192592029025
```

## 3. 预算表

| T | L | chi sharp 0.5L | pole log(T+2) | zeta log(1+L) | left total | 2L | margin |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | `1.609437912434` | `0.804718956217` | `1.386294361120` | `0.959134838921` | `3.150148156258` | `3.218875824868` | `0.068727668610` |
| 4.14145 | `1.965915416883` | `0.982957708441` | `1.815060382146` | `1.087185725738` | `3.885203816325` | `3.931830833766` | `0.046627017441` |
| 10 | `2.564949357462` | `1.282474678731` | `2.484906649788` | `1.271149848285` | `5.038531176803` | `5.129898714923` | `0.091367538120` |
| 100 | `4.634728988230` | `2.317364494115` | `4.624972813284` | `1.728949051966` | `8.671286359365` | `9.269457976459` | `0.598171617094` |
| 10000 | `9.210640326985` | `4.605320163493` | `9.210540351979` | `2.323430345879` | `16.139290861351` | `18.421280653970` | `2.281989792619` |
| 1e+06 | `13.815513557960` | `6.907756778980` | `13.815512557962` | `2.695674845154` | `23.418944182096` | `27.631027115920` | `4.212082933824` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ConvexityC2OptimizationGateActive | `true` | `false` | 上一层唯一内部最窄点是临界带凸性 C=2 常数优化。 | CriticalStripConvexityC2ConstantOptimizationLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ThreeLinesAndBoundaryInputsAvailable | `true` | `true` | 三线原理、右边界 Euler 预算和左边界函数方程预算均已可用。 | 无形式输入剩余。 |
| SharpChiEnvelopeClosed | `true` | `true` | 优化层使用更尖锐的 chi 包络：log\|chi(-eta+it)\|<=0.5L，而不是沿用粗 C_left=4 拆分。 | SharpChiEnvelopeClosedC05 |
| PoleAndRightZetaSharpEnvelopeClosed | `true` | `true` | 使用 log\|s-1\|<=log(T+2) 与 log\|zeta(1+eta-it)\|<=log(1+L)。 | PoleRightZetaSharpEnvelopeClosed |
| ScalarMarginPositiveClosed | `true` | `true` | 单变量余量 2L-(0.5L+log(T+2)+log(1+L)) 在 T>=2 上最小值仍为正。 | min_margin=0.046627017338 |
| CriticalStripConvexityC2ConstantOptimizationLedger | `true` | `true` | C=2 凸性优化闭合：左右边界均可支付在 2L 内，三线定理给临界带内部同一 C=2 上界。 | CriticalStripConvexityClosedC2 |
| HorizontalAggregationStillNext | `false` | `false` | 下一步需要把 C=2 凸性上界与去极点/缩进项合并成水平边常数。 | HorizontalVariationConstantAggregationLedger |
| BacklundAggregationStillDownstream | `false` | `false` | 之后仍需 Backlund 总常数聚合。 | BacklundArgumentConstantAggregationLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantAggregationLedger) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND BacklundArgumentConstantAggregationLedger) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

唯一内部最窄点更新为 `HorizontalVariationConstantAggregationLedger`；随后是 `BacklundArgumentConstantAggregationLedger`。
