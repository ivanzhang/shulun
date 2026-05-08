# Prime Matrix B=3 Jensen 局部零点计数账本路由器

**状态：** `jensen_zero_count_reduced_to_four_micro_ledgers_open`

Jensen 局部零点计数尚未闭合；它已压成 Riemann-von Mangoldt/边界上界/圆心下界/C_N convention 四个微账本。候选 C_N=16 很保守，但必须由这些账本逐项支撑后才能使用。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
jensen_zero_count_reduced=true
jensen_zero_count_self_contained_proved=false
C_N_candidate=16.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
JensenZeroCountingLocalNumericalLedger
  =>
(RiemannVonMangoldtExplicitLocalCountingLedger AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger)
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

候选 `C_N=16` 明显大于 RVM 局部主尺度，但仍不能代替显式 argument principle 或 Jensen 证明。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| JensenZeroCountingGateActive | `true` | `false` | 上一层唯一内部最窄点是局部零点计数 N(t+1)-N(t-1)<=C_N log(\|t\|+3)。 | JensenZeroCountingLocalNumericalLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| GammaComponentAvailable | `true` | `true` | Gamma/digamma 分量已由 C_gamma=24 支付。 | 无 Gamma 项剩余。 |
| RiemannVonMangoldtLocalCountingMissing | `false` | `false` | 还需 argument principle/Riemann-von Mangoldt 显式版本给出局部零点主尺度。 | RiemannVonMangoldtExplicitLocalCountingLedger |
| XiBoundaryMajorantMissing | `false` | `false` | 若走 Jensen 圆盘法，还需 xi 在圆盘边界上的显式 log majorant。 | XiBoundaryLogMajorantNumericalLedger |
| JensenLowerAnchorMissing | `false` | `false` | Jensen 法还需圆心处 xi 不过小的显式下界，避免只给上界无法计数。 | JensenDiskLowerAnchorNumericalLedger |
| LocalCNConventionMissing | `false` | `false` | 还需把低高度分界、重零点计数 convention 和 C_N=16 聚合成统一账本。 | LocalZeroCountCNConventionLedger |
| JensenZeroCountingReducedToFourMicroLedgers | `true` | `false` | 旧 Jensen 局部计数原子已压成 RVM/边界上界/圆心下界/C_N convention 四包。 | (RiemannVonMangoldtExplicitLocalCountingLedger AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) |
| HadamardPartialFractionRemainderStillNext | `false` | `false` | 局部零点计数完成后，才可处理 Hadamard 远零点与 1/rho 余项。 | HadamardPartialFractionRemainderNumericalLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND (RiemannVonMangoldtExplicitLocalCountingLedger AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `RiemannVonMangoldtExplicitLocalCountingLedger`；随后是 `XiBoundaryLogMajorantNumericalLedger`、`JensenDiskLowerAnchorNumericalLedger`、`LocalZeroCountCNConventionLedger`。
