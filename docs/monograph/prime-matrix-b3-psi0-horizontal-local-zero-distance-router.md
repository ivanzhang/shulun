# Prime Matrix B=3 psi_0 水平边局部零点倒距离和路由器

**状态：** `psi0_horizontal_local_zero_distance_external_closed_self_open`

`Psi0HorizontalLocalZeroDistanceSumConstantLedger` 在外部 Backlund/RVM 条件路线下闭合：固定 eta=1/16 后，凹口外剩余水平段到近零点距离至少 eta，C_N=16 给出倒距离和不超过 256 log(T+3)，再给 Titchmarsh 结构余项预留 32 log(T+3)，得到 pointwise 系数 C=288。该步不关闭严格自足路线，也不关闭加权水平积分预算。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
psi0_horizontal_local_zero_distance_external_closed=true
psi0_horizontal_local_zero_distance_self_contained_closed=false
psi0_horizontal_weighted_integral_budget_closed=false
zeta_logder_contour_shift_closed=false
row_column_unconditional_closed=false
C_total_logder=288.000000000000
```

## 1. 外部条件替换

```text
Psi0HorizontalLocalZeroDistanceSumConstantLedger
  =>
Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16
```

## 2. 常数表

| item | value | formula | meaning |
| --- | ---: | --- | --- |
| eta | `0.062500000000` | 1/16 | 凹口后的剩余水平边到近零点的登记最小距离。 |
| C_N | `16.000000000000` | RVMToCN16LocalInequalityClosedWithRawArgCS8 | 外部 Backlund/RVM 分支给出的单位高度局部零点计数常数。 |
| local distance coefficient | `256.000000000000` | C_N/eta | 粗界 sum 1/\|s-rho\| <= C_N log(T+3)/eta。 |
| structural remainder reserve | `32.000000000000` | Titchmarsh O(log T) reserve | 给局部零点主部之外的结构余项预留。 |
| total log-derivative coefficient | `288.000000000000` | C_N/eta + 32 | 供下一层加权水平积分预算使用的 pointwise 系数。 |

## 3. 样例上界

| T | log(T+3) | pointwise bound |
| ---: | ---: | ---: |
| 14.000000000000 | 2.833213344056 | 815.965443088190 |
| 45.000000000000 | 3.871201010908 | 1114.905891141473 |
| 100.000000000000 | 4.634728988230 | 1334.801948610135 |
| 1000.000000000000 | 6.910750787962 | 1990.296226933038 |
| 20000.000000000000 | 9.903637541287 | 2852.247611890729 |
| 1000000.000000000000 | 13.815513557960 | 3978.867904692415 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Psi0LocalZeroDistanceGateActive | `true` | `true` | 上一层把水平边 log-derivative 压到局部零点倒距离和与加权积分预算。 | Psi0HorizontalLocalZeroDistanceSumConstantLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席或数值实验替代证明。 | 保持 row_column_unconditional_closed=false。 |
| ExternalCN16LocalCountAvailable | `true` | `false` | 接受外部 Backlund/RVM 分支时，单位高度零点数有 C_N=16 上界。 | RVMToCN16LocalInequalityClosedWithRawArgCS8 |
| SelfContainedCN16StillOpen | `true` | `true` | 严格自足路线仍缺自足 Backlund 和低高度零点核验，不能自足调用 C_N=16。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| FixedIndentDisciplineAvailableExternally | `true` | `false` | 外部 fixed-T 缩进允许把 eta 内近零点转入凹口成本，剩余水平段距离至少 eta。 | ClassicalBacklundZeroIndentationCostExternalAccepted |
| EtaOneOver16DistanceBoundComputed | `true` | `true` | 在剩余水平段上，每个近零点贡献至多 1/eta；C_N=16 给出 256 log(T+3)，结构余项预留 32 log(T+3)。 | Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16 |
| Psi0LocalZeroDistanceExternalClosed | `true` | `false` | 外部条件路线下，局部零点倒距离和闭合为 pointwise 系数 C=288。 | Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16 |
| Psi0LocalZeroDistanceSelfContainedClosed | `false` | `false` | 自足路线只有在自足 C_N=16 和自足 fixed-T 缩进都关闭后才能同步闭合。 | ClassicalBacklundZeroIndentationCostInternalProofLedger AND RVMToCN16 self-contained |
| Psi0HorizontalLocalZeroDistanceSumConstantLedger | `true` | `false` | 本原子在外部 Backlund/RVM 条件路线下关闭；严格自足版仍未关闭。 | Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16 |
| HorizontalWeightedIntegralBudgetNext | `false` | `false` | pointwise C=288 log(T+3) 仍需乘上 x^sigma/\|s\| 并进入 Perron/PNT 常数预算。 | Psi0HorizontalWeightedIntegralBudgetLedger |
| WholeStripExternalMatchStillIndependent | `false` | `false` | 若不采用内部 Titchmarsh+CN16 展开，也可继续寻找 whole-strip 外部显式引理。 | ExplicitWholeStripZetaLogDerivativeAwayFromZerosExternalAccepted |

## 5. 最新输入基

接受外部 Backlund/RVM 后的输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ContourResidueAndLeftEdgeClosed AND (TitchmarshLocalZeroExpansionExternalRegistered AND Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16 AND Psi0HorizontalWeightedIntegralBudgetLedger) AND (ClassicalBacklundZeroIndentationCostExternalAccepted OR Psi0GoodHeightTStarAveragingContourShiftLedger)) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

下一步集中攻 `Psi0HorizontalWeightedIntegralBudgetLedger`；严格自足路线并行保留 `ClassicalBacklundZeroIndentationCostInternalProofLedger`。
