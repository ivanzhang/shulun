# Prime Matrix B=3 Backlund Littlewood 矩形转移闭合证书

**状态：** `backlund_littlewood_rectangle_argument_closed`

Backlund 的 Littlewood 矩形转移层已自足闭合。这只是形式恒等式：它把 arg zeta 的水平变化交给左右竖边 log|zeta|、零点权重和初等去极点项；真正的数值压力仍在右边 Euler product、水平边、左边函数方程和 C_S 聚合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_littlewood_rectangle_argument_closed=true
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundLittlewoodRectangleArgumentLedger
  =>
BacklundLittlewoodRectangleArgumentClosed
```

## 2. 文内证明

取 `F(s)=(s-1)zeta(s)`。这样 `s=1` 的极点被去掉，额外产生的 `log|s-1|` 与 `arg(s-1)` 是初等项。

对矩形 `R=[a,b] x [T0,T1]`，边界避开 `F` 的零点时，Littlewood 矩形引理给出：

```text
For F(s)=(s-1)zeta(s), a<b, T0<T1, and a boundary avoiding zeros, int_a^b(arg F(sigma+iT1)-arg F(sigma+iT0)) d sigma = 2*pi*sum_{rho in R}(Re rho-a) + int_T0^T1 log|F(b+it)| dt - int_T0^T1 log|F(a+it)| dt.
```

证明可由 argument principle 应用于 `(s-a)F'(s)/F(s)` 得到。右端零点权重按重数计，边界碰零时先作 `epsilon` 扰动或小凹口再取极限。

因此本层只完成 `arg` 到边界积分的结构转移。它没有证明 `|S(T)|<=C_S log(T+3)`，也没有使用真实零行不存在。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BacklundLittlewoodRectangleGateActive | `true` | `false` | 上一层唯一内部最窄点是 Backlund 的 Littlewood 矩形转移。 | BacklundLittlewoodRectangleArgumentLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ZetaContinuationAvailable | `true` | `true` | zeta 的解析延拓和函数方程输入已在上游闭合，可定义 F(s)=(s-1)zeta(s)。 | 无解析延拓剩余。 |
| PoleRemovalFactorClosed | `true` | `true` | 用 F(s)=(s-1)zeta(s) 去掉 s=1 的极点；新增的 log\|s-1\| 和 arg(s-1) 是初等边界项。 | 初等项交给后续边界预算吸收。 |
| LittlewoodRectangleIdentityClosed | `true` | `true` | Littlewood 矩形引理把上下边 arg 差精确转成左右边 log\|F\| 积分和矩形内零点横向权重。 | BacklundLittlewoodRectangleArgumentClosed |
| BoundaryIndentationConventionClosed | `true` | `true` | 若边界碰到零点，先作 epsilon 平移或小凹口，最后取极限并按重数记账。 | 全局端点统一仍留给 EndpointZeroAvoidanceMultiplicityConventionLedger。 |
| BacklundLittlewoodRectangleArgumentLedger | `true` | `true` | 待证 atom 已闭合为 Littlewood 矩形转移恒等式；它不提供数值上界。 | BacklundLittlewoodRectangleArgumentClosed |
| RightEdgeEulerProductStillNext | `false` | `false` | 下一步需要在右边界用 Euler product 给 log\|zeta\| 和 arg 预算。 | ZetaRightEdgeEulerProductArgumentNumericalLedger |
| HorizontalAndLeftEdgesStillDownstream | `false` | `false` | 水平边、左边函数方程和 C_S 聚合仍未闭合。 | CriticalStripHorizontalVariationNumericalLedger AND FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentNumericalLedger AND CriticalStripHorizontalVariationNumericalLedger AND FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `ZetaRightEdgeEulerProductArgumentNumericalLedger`；随后是 `CriticalStripHorizontalVariationNumericalLedger`、`FunctionalEquationLeftEdgeArgumentLedger`、`BacklundArgumentConstantAggregationLedger`。
