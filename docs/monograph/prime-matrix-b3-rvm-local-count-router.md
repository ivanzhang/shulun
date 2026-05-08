# Prime Matrix B=3 Riemann-von Mangoldt 局部计数路由器

**状态：** `rvm_local_count_reduced_to_five_micro_ledgers_open`

RVM 显式局部计数尚未自足闭合，但已压成五个可审稿微账本。核心新增硬点不是主项，而是 Backlund/arg zeta 显式上界与端点 convention。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
rvm_local_count_reduced=true
rvm_local_count_self_contained_proved=false
C_N_candidate=16.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
RiemannVonMangoldtExplicitLocalCountingLedger
  =>
(ArgumentPrincipleXiRectangleCountingLedger AND GammaMainTermLocalDifferenceNumericalLedger AND BacklundZetaArgumentBoundNumericalLedger AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger)
```

## 2. 主项尺度审计

| T | log(T+3) | local main scale | CN16 bound | slack |
| ---: | ---: | ---: | ---: | ---: |
| 2 | `1.609437912434` | `0.000000000000` | `25.751006598946` | `25.751006598946` |
| 10 | `2.564949357462` | `0.147921159051` | `41.039189719385` | `40.891268560334` |
| 100 | `4.634728988230` | `0.880856757930` | `74.155663811674` | `73.274807053744` |
| 10000 | `9.210640326985` | `2.346727955689` | `147.370245231763` | `145.023517276074` |
| 1e+06 | `13.815513557960` | `3.812599153448` | `221.048216927356` | `217.235617773908` |

主项远小于 `16 log(T+3)`；真正需核验的是 `arg zeta` 与端点/低高度 convention。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RVMLocalCountingGateActive | `true` | `false` | 上一层唯一内部最窄点是 Riemann-von Mangoldt 显式局部零点计数。 | RiemannVonMangoldtExplicitLocalCountingLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ZetaXiAnalyticBasisAvailable | `true` | `true` | theta-Mellin、xi 整函数与 Hadamard 层已闭合，可供 argument principle 使用。 | 无基础解析剩余。 |
| ArgumentPrincipleXiRectangleCountingMissing | `false` | `false` | 还需把 xi 零点计数写成矩形边界上 Delta arg xi 的形式，并固定避零边界。 | ArgumentPrincipleXiRectangleCountingLedger |
| GammaMainTermLocalDifferenceMissing | `false` | `false` | 还需数值核算 Gamma/主项差分在 [T-1,T+1] 上为 O(log(T+3))。 | GammaMainTermLocalDifferenceNumericalLedger |
| BacklundZetaArgumentBoundMissing | `false` | `false` | 还需 Backlund/arg zeta 显式上界，控制 S(T+1)-S(T-1)。 | BacklundZetaArgumentBoundNumericalLedger |
| EndpointMultiplicityConventionMissing | `false` | `false` | 还需端点落零、重零点和 T<2 低高度区间的计数 convention。 | EndpointZeroAvoidanceMultiplicityConventionLedger |
| RVMToCN16LocalInequalityMissing | `false` | `false` | 还需把主项、arg 项和端点项合并为 N(T+1)-N(T-1)<=16 log(T+3)。 | RVMToCN16LocalInequalityLedger |
| RVMExplicitLocalCountingReducedToFiveMicroLedgers | `true` | `false` | 旧 RVM 局部计数原子已压成 argument principle、Gamma 主项、Backlund 辐角、端点 convention、CN16 转移五包。 | (ArgumentPrincipleXiRectangleCountingLedger AND GammaMainTermLocalDifferenceNumericalLedger AND BacklundZetaArgumentBoundNumericalLedger AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) |
| JensenBoundaryAndAnchorStillDownstream | `false` | `false` | RVM 局部计数之外，Jensen 路线仍需 xi 边界上界、圆心下界和 CN convention。 | XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingLedger AND GammaMainTermLocalDifferenceNumericalLedger AND BacklundZetaArgumentBoundNumericalLedger AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `ArgumentPrincipleXiRectangleCountingLedger`；随后是 `GammaMainTermLocalDifferenceNumericalLedger`、`BacklundZetaArgumentBoundNumericalLedger`、`EndpointZeroAvoidanceMultiplicityConventionLedger`、`RVMToCN16LocalInequalityLedger`。
