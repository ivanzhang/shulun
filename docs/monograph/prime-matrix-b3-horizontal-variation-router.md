# Prime Matrix B=3 临界带水平边变化路由器

**状态：** `critical_strip_horizontal_variation_reduced_open`

临界带水平边账本尚未自足闭合。本步已闭合避零缩进 convention 与去极点初等预算，并把真正硬点压成：临界带 log|zeta| 显式凸性上界，以及把该上界聚合进水平边常数。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
critical_strip_horizontal_variation_reduced=true
critical_strip_horizontal_variation_self_contained_proved=false
C_convexity_candidate=2.000000000000
C_horizontal_candidate=8.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
CriticalStripHorizontalVariationNumericalLedger
  =>
(HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND CriticalStripConvexityLogZetaBoundNumericalLedger AND HorizontalVariationConstantAggregationLedger)
```

## 2. 候选预算

下面只审计若能证明 `log|zeta(s)|<=2 log(T+3)` 型临界带凸性上界时，水平边常数的量级是否还有余量；该表不是凸性定理证明。

| T | L | eta | strip width | convexity integral | pole integral | total candidate | 8L budget |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | `1.609437912434` | `0.621334934560` | `2.242669869119` | `7.218875824868` | `3.609437912434` | `10.828313737302` | `12.875503299473` |
| 10 | `2.564949357462` | `0.389871245251` | `1.779742490503` | `9.129898714923` | `4.564949357462` | `13.694848072385` | `20.519594859692` |
| 100 | `4.634728988230` | `0.215762346092` | `1.431524692184` | `13.269457976459` | `6.634728988230` | `19.904186964689` | `37.077831905837` |
| 10000 | `9.210640326985` | `0.108570084652` | `1.217140169304` | `22.421280653970` | `11.210640326985` | `33.631920980956` | `73.685122615881` |
| 1e+06 | `13.815513557960` | `0.072382397933` | `1.144764795866` | `31.631027115920` | `15.815513557960` | `47.446540673879` | `110.524108463678` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CriticalStripHorizontalGateActive | `true` | `false` | 上一层唯一内部最窄点是临界带水平边变化预算。 | CriticalStripHorizontalVariationNumericalLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| RectangleAndRightEdgeAvailable | `true` | `true` | Littlewood 矩形转移和右边界 Euler product 预算已闭合。 | 无右边界形式剩余。 |
| HorizontalZeroIndentationConventionClosed | `true` | `true` | 水平边若穿过零点，采用 epsilon 平移或小凹口；缩进贡献按重数进入端点/零点 convention。 | HorizontalZeroIndentationConventionClosed |
| HorizontalPoleRemovalBudgetClosed | `true` | `true` | F=(s-1)zeta(s) 的去极点因子在宽度 1+2/L 的水平边上贡献至多初等 O(L)。 | HorizontalPoleRemovalBudgetClosed |
| CriticalStripConvexityLogZetaBoundMissing | `false` | `false` | 仍需自足证明临界带内 log\|zeta(s)\| 的显式凸性/三线型 O(log(T+3)) 上界。 | CriticalStripConvexityLogZetaBoundNumericalLedger |
| HorizontalVariationConstantAggregationMissing | `false` | `false` | 仍需把凸性上界、去极点项、上下两条水平边和缩进成本聚合为指定水平边常数。 | HorizontalVariationConstantAggregationLedger |
| CriticalStripHorizontalVariationReduced | `true` | `false` | 旧水平边原子已压成两个闭合 convention 和两个真正数值剩余。 | (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND CriticalStripConvexityLogZetaBoundNumericalLedger AND HorizontalVariationConstantAggregationLedger) |
| LeftAndBacklundAggregationStillDownstream | `false` | `false` | 水平边之后还需左边函数方程与 Backlund 总常数聚合。 | FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND CriticalStripConvexityLogZetaBoundNumericalLedger AND HorizontalVariationConstantAggregationLedger) AND FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `CriticalStripConvexityLogZetaBoundNumericalLedger`；随后是 `HorizontalVariationConstantAggregationLedger`、`FunctionalEquationLeftEdgeArgumentLedger`、`BacklundArgumentConstantAggregationLedger`。
