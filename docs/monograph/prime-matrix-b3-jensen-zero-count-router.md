# Prime Matrix B=3 Jensen 局部零点计数账本路由器

**状态：** `jensen_zero_count_rvm_route_external_closed_self_contained_open`

Jensen 局部零点计数的主攻路线改为 RVM 直接计数：边界上界和圆心下界只属于 Jensen 圆盘替代证明，不再作为 RVM 路线的额外必需项。接受外部 Backlund/低高度输入时，本局部计数已条件闭合；严格自足路线仍卡在 Backlund 近零凹口成本内部化与 14 以下零点有限核验。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
jensen_zero_count_reduced=true
jensen_zero_count_external_closed=true
jensen_zero_count_self_contained_proved=false
C_N_candidate=16.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
JensenZeroCountingLocalNumericalLedger
  =>
(RiemannVonMangoldtExplicitLocalCountingLedger OR (XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger))
```

外部 Backlund/低高度输入下的条件替换：

```text
JensenZeroCountingLocalNumericalLedger
  =>
RVMToCN16LocalInequalityClosedWithRawArgCS8
```

## 2. 候选预算

| t | log(|t|+3) | C_N log bound | local RVM scale | budget ratio |
| ---: | ---: | ---: | ---: | ---: |
| 0 | `1.098612288668` | `17.577796618690` | `0.349699152566` | `50.265482457437` |
| 1 | `1.386294361120` | `22.180709777918` | `0.441271200305` | `50.265482457437` |
| 10 | `2.564949357462` | `41.039189719385` | `0.816448738041` | `50.265482457437` |
| 100 | `4.634728988230` | `74.155663811674` | `1.475280056736` | `50.265482457437` |
| 10000 | `9.210640326985` | `147.370245231763` | `2.931837874162` | `50.265482457437` |
| 1e+06 | `13.815513557960` | `221.048216927356` | `4.397614548205` | `50.265482457437` |

候选 `C_N=16` 明显大于 RVM 局部主尺度；当前选择 RVM 直接计数路线，Jensen 圆盘边界/圆心下界保留为替代路线而非额外必要条件。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| JensenZeroCountingGateActive | `true` | `false` | 上一层唯一内部最窄点是局部零点计数 N(t+1)-N(t-1)<=C_N log(\|t\|+3)。 | JensenZeroCountingLocalNumericalLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| GammaComponentAvailable | `true` | `true` | Gamma/digamma 分量已由 C_gamma=24 支付。 | 无 Gamma 项剩余。 |
| RiemannVonMangoldtDirectRouteReduced | `true` | `false` | 局部零点计数可走 RVM 直接路线；该路线已被拆成 argument principle、Gamma 主项、Backlund、端点、CN16 合并。 | RiemannVonMangoldtExplicitLocalCountingLedger |
| ExternalRVMToCN16RouteClosed | `true` | `false` | 接受外部 Backlund 缩进/低高度输入时，RVM 已合并为 C_N=16 局部计数。 | RVMToCN16LocalInequalityClosedWithRawArgCS8 |
| JensenDiskAlternativeNotRequiredForRVMRoute | `true` | `true` | 边界上界和圆心下界只属于 Jensen 圆盘替代证明；当前主攻 RVM 直接路线时不作为额外必需项。 | XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger |
| JensenZeroCountingExternalClosed | `true` | `false` | 在外部 Backlund/低高度输入下，旧 Jensen 局部计数原子可由 RVM-C_N=16 直接关闭。 | RVMToCN16LocalInequalityClosedWithRawArgCS8 |
| JensenZeroCountingSelfContainedStillOpen | `false` | `false` | 严格自足路线仍缺 Backlund 近零凹口成本内部化与 0<t<=14 的有限零点核验。 | BacklundZeroProximityIndentationCostLedger AND CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger |
| JensenZeroCountingReducedToRVMOrDiskRoute | `true` | `false` | 旧 Jensen 局部计数原子已压成 RVM 直接计数路线，或 Jensen 圆盘边界/圆心替代路线。 | (RiemannVonMangoldtExplicitLocalCountingLedger OR (XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger)) |
| HadamardPartialFractionRemainderStillNext | `false` | `false` | 局部零点计数完成后，才可处理 Hadamard 远零点与 1/rho 余项。 | HadamardPartialFractionRemainderNumericalLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND (RiemannVonMangoldtExplicitLocalCountingLedger OR (XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger)) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

严格自足路线的最窄点更新为 `BacklundZeroProximityIndentationCostLedger`；并行低高度核验为 `CriticalLineNoZeroOn0To14FiniteLedger`、`CriticalStripNoOffLineZeroBelow14TuringLedger`。若改走 Jensen 圆盘替代路线，则需 `XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger`。
