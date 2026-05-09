# Prime Matrix B=3 psi_0 右边 Perron 核近似常数路由器

**状态：** `right_edge_perron_kernel_closed_c128_contour_shift_open`

右边 Perron 核近似常数闭合为 C_right=128：它只支付 psi_0 与右边截断竖线积分之间的核误差。整个 R_T 常数尚未闭合，因为仍需 -zeta'/zeta 轮廓移线常数。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
right_edge_perron_kernel_closed=true
perron_kernel_truncation_constant_closed=false
row_column_unconditional_closed=false
```

## 1. 替换

```text
Psi0RightEdgePerronKernelApproximationConstantLedger
  =>
Psi0RightEdgePerronKernelApproximationClosedC128
```

## 2. 常数

| item | value |
| --- | ---: |
| C_right | `128.000000000000` |
| C_edge | `4.000000000000` |
| anchor x | `20000.000000000000` |
| anchor T | `14.000000000000` |
| right edge bound at anchor | `28766290.058893192559` |

## 3. 证明组件

| component | closed | claim |
| --- | --- | --- |
| truncated_kernel_pointwise_bound | `true` | Perron 核误差由 min(1,1/(T\|log(x/n)\|)) 控制，端点取 psi_0 半权。 |
| near_shell_bound | `true` | \|n-x\|<=x/T 的近壳总 Lambda 质量由 log x 与壳长给出 O(x log x/T+log x)。 |
| far_shell_dyadic_bound | `true` | 远壳按 \|log(n/x)\| dyadic 求和，使用 -zeta'/zeta(1+1/log x)<=2 log x 的保守界。 |
| constant_aggregation | `true` | 近壳、远壳和端点统一吸收到 C_right=128, C_edge=4。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RightEdgePerronKernelGateActive | `true` | `false` | Perron 截断核四包中的当前最窄点是右边竖线核近似常数。 | Psi0RightEdgePerronKernelApproximationConstantLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ExactPsi0AndEndpointReady | `true` | `true` | psi_0 精确公式和半权端点规范已闭合，可使用标准截断 Perron 核。 | 无端点剩余。 |
| KernelPointwiseAndShellBoundsClosed | `true` | `true` | 截断核点态误差、近壳质量、远壳 dyadic 求和和常数聚合给出 C_right=128。 | Psi0RightEdgePerronKernelApproximationClosedC128 |
| Psi0RightEdgePerronKernelApproximationConstantLedger | `true` | `true` | 右边 Perron 核近似常数闭合；它只控制 psi_0 与右边竖线积分的差。 | Psi0RightEdgePerronKernelApproximationClosedC128 |
| Psi0ZetaLogDerivativeContourShiftBoundLedger | `false` | `false` | 仍需把右边竖线积分移线为零点留数，并支付 -zeta'/zeta 轮廓边界。 | Psi0ZetaLogDerivativeContourShiftBoundLedger |
| ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger | `false` | `false` | 轮廓移线后还需零点自由带下的零点和预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND Psi0ZetaLogDerivativeContourShiftBoundLedger AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

当前最窄点更新为 `Psi0ZetaLogDerivativeContourShiftBoundLedger`；随后是 `ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger`。
