# Prime Matrix B=3 xi 矩形 argument principle 计数闭合证书

**状态：** `argument_principle_xi_rectangle_counting_closed`

xi 矩形 argument principle 计数恒等式已闭合。它只是形式计数层，不给任何数值上界；下一步仍要数值化 Gamma 主项、Backlund 辐角和端点 convention。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
argument_principle_xi_rectangle_counting_closed=true
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
ArgumentPrincipleXiRectangleCountingLedger
  =>
ArgumentPrincipleXiRectangleCountingClosed
```

## 2. 文内证明

对避开零点的矩形 `R`，argument principle 给出

```text
N(R)=1/(2*pi*i) int_{partial R} xi'(s)/xi(s) ds = Delta_{partial R} arg xi / (2*pi)
```

若边界穿过零点，先对边界作 `epsilon` 平移或凹口绕开，最后令 `epsilon->0`，以零点重数计入。这个 convention 的全局统一仍由后续端点账本处理。

该层不估计辐角大小，只把零点计数精确转成边界积分。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ArgumentPrincipleXiGateActive | `true` | `false` | 上一层唯一内部最窄点是 xi 矩形 argument principle 计数。 | ArgumentPrincipleXiRectangleCountingLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| XiEntireFunctionAvailable | `true` | `true` | xi 已闭合为整函数，argument principle 可直接应用。 | 无整函数性剩余。 |
| BoundaryPerturbationConventionClosed | `true` | `true` | 若矩形边界穿过零点，先取 epsilon 扰动并在极限中按重数计数。 | 端点统一记账仍留给 EndpointZeroAvoidanceMultiplicityConventionLedger。 |
| XiRectangleArgumentCountingClosed | `true` | `true` | 矩形内零点数等于 (1/2pi i) int_{partial R} xi'(s)/xi(s) ds，即边界辐角变化除以 2pi。 | ArgumentPrincipleXiRectangleCountingClosed |
| ArgumentPrincipleXiRectangleCountingLedger | `true` | `true` | 待证 atom 已闭合为 xi 矩形 argument principle 计数恒等式。 | ArgumentPrincipleXiRectangleCountingClosed |
| GammaMainTermStillNext | `false` | `false` | 下一步需要把边界辐角分解中的 Gamma/主项差数值化。 | GammaMainTermLocalDifferenceNumericalLedger |
| BacklundAndEndpointStillDownstream | `false` | `false` | arg zeta、端点 convention 与 CN16 合并仍未闭合。 | BacklundZetaArgumentBoundNumericalLedger AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalLedger AND BacklundZetaArgumentBoundNumericalLedger AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `GammaMainTermLocalDifferenceNumericalLedger`；随后是 `BacklundZetaArgumentBoundNumericalLedger`、`EndpointZeroAvoidanceMultiplicityConventionLedger`、`RVMToCN16LocalInequalityLedger`。
