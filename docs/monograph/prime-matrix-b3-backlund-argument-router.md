# Prime Matrix B=3 Backlund/arg zeta 显式上界路由器

**状态：** `backlund_argument_reduced_to_five_micro_ledgers_open`

Backlund/arg zeta 显式上界尚未自足闭合。它已压成五个微账本；候选 C_S=8 只是预算目标，必须由 Littlewood 矩形和边界积分逐项支撑。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_argument_reduced=true
backlund_argument_self_contained_proved=false
C_S_candidate=8.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundZetaArgumentBoundNumericalLedger
  =>
(BacklundLittlewoodRectangleArgumentLedger AND ZetaRightEdgeEulerProductArgumentNumericalLedger AND CriticalStripHorizontalVariationNumericalLedger AND FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger)
```

## 2. 候选预算

| T | log(T+3) | C_S log bound | two-endpoint budget |
| ---: | ---: | ---: | ---: |
| 2 | `1.609437912434` | `12.875503299473` | `25.751006598946` |
| 10 | `2.564949357462` | `20.519594859692` | `41.039189719385` |
| 100 | `4.634728988230` | `37.077831905837` | `74.155663811674` |
| 10000 | `9.210640326985` | `73.685122615881` | `147.370245231763` |
| 1e+06 | `13.815513557960` | `110.524108463678` | `221.048216927356` |

候选 `C_S=8` 只用于预算排布；未完成前不能作为定理输入。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BacklundArgumentGateActive | `true` | `false` | 上一层唯一内部最窄点是 Backlund/arg zeta 显式上界。 | BacklundZetaArgumentBoundNumericalLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| GammaMainAvailable | `true` | `true` | Gamma 主项局部差分已由 C_main=4 闭合。 | 无 Gamma 主项剩余。 |
| BacklundLittlewoodRectangleMissing | `false` | `false` | 还需把 arg zeta 变化转成 Littlewood 矩形内 log\|zeta\| 边界积分。 | BacklundLittlewoodRectangleArgumentLedger |
| RightEdgeEulerProductArgumentMissing | `false` | `false` | 还需在 sigma=1+eta 右边界用 Euler product 控制 arg/log\|zeta\|。 | ZetaRightEdgeEulerProductArgumentNumericalLedger |
| HorizontalVariationMissing | `false` | `false` | 还需控制矩形上下水平边的 log\|zeta\| 变化和零点附近绕行成本。 | CriticalStripHorizontalVariationNumericalLedger |
| LeftEdgeFunctionalEquationMissing | `false` | `false` | 还需用函数方程把左边界归还给右边界与 Gamma 主项。 | FunctionalEquationLeftEdgeArgumentLedger |
| BacklundConstantAggregationMissing | `false` | `false` | 还需把各边贡献聚合为 \|S(T)\|<=C_S log(T+3)，候选 C_S=8。 | BacklundArgumentConstantAggregationLedger |
| BacklundArgumentReducedToFiveMicroLedgers | `true` | `false` | 旧 Backlund 原子已压成 Littlewood 矩形、右边 Euler、水平边、左边函数方程、常数聚合五包。 | (BacklundLittlewoodRectangleArgumentLedger AND ZetaRightEdgeEulerProductArgumentNumericalLedger AND CriticalStripHorizontalVariationNumericalLedger AND FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger) |
| EndpointAndCN16StillDownstream | `false` | `false` | Backlund 完成后还需端点 convention 与 CN16 合并。 | EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentLedger AND ZetaRightEdgeEulerProductArgumentNumericalLedger AND CriticalStripHorizontalVariationNumericalLedger AND FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `BacklundLittlewoodRectangleArgumentLedger`；随后是 `ZetaRightEdgeEulerProductArgumentNumericalLedger`、`CriticalStripHorizontalVariationNumericalLedger`、`FunctionalEquationLeftEdgeArgumentLedger`、`BacklundArgumentConstantAggregationLedger`。
