# Prime Matrix B=3 psi_0 Perron 截断核常数路由器

**状态：** `perron_kernel_truncation_reduced_to_four_microledgers_open`

Perron 截断核常数层已压成四个微账本；高度选择与边界避零可由既有口径关闭，真正剩余是右边 Perron 核近似常数和 -zeta'/zeta 轮廓移线常数。当前不能声明 R_T 常数闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
perron_kernel_truncation_reduced=true
perron_kernel_truncation_constant_closed=false
row_column_unconditional_closed=false
```

## 1. 替换

```text
PerronKernelTruncationConstantForPsi0Ledger
  =>
(Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationConstantLedger AND Psi0ZetaLogDerivativeContourShiftBoundLedger AND Psi0ZeroBoundaryAvoidanceLimitLedger)
```

## 2. 候选常数合同

```text
|R_T(x)| <= C_Perron*x*log^2(xT)/T + C_edge*log x
```

| item | value |
| --- | ---: |
| C_Perron | `256.000000000000` |
| C_edge | `8.000000000000` |
| anchor x | `20000.000000000000` |
| anchor T | `14.000000000000` |
| x log^2(xT)/T at anchor | `224736.331601117039` |
| candidate bound at anchor | `57532580.117786385119` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PerronKernelGateActive | `true` | `false` | 上一层已闭合无截断 psi_0 精确公式，当前最窄点是 finite-T 截断核常数。 | PerronKernelTruncationConstantForPsi0Ledger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ExactPsi0FormulaAvailable | `true` | `true` | 无截断 psi_0 显式公式已闭合，可作为 finite-T 截断的起点。 | InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost |
| HeightSelectionLedgerClosed | `true` | `true` | 取避开零点高度的 T_epsilon 并最终令 epsilon->0；高度选择只改变端点极限，不产生主预算。 | Psi0PerronFiniteRectangleHeightSelectionLedger |
| BoundaryAvoidanceLimitClosed | `true` | `true` | 端点半权与避零极限已登记，边界落零按重数进入极限。 | Psi0ZeroBoundaryAvoidanceLimitLedger |
| RightEdgeKernelApproximationConstantMissing | `false` | `false` | 还缺直接从截断 Perron 核估计 psi_0 与右边竖线积分差的显式常数。 | Psi0RightEdgePerronKernelApproximationConstantLedger |
| ZetaLogDerivativeContourShiftBoundMissing | `false` | `false` | 还缺把右边竖线移到零点留数公式时，水平边和左边界的显式 -zeta'/zeta 常数。 | Psi0ZetaLogDerivativeContourShiftBoundLedger |
| PerronKernelReducedToFourMicroLedgers | `true` | `false` | 截断核常数原子已压成高度选择、右边 Perron 核近似、zeta 对数导数轮廓界、边界避零极限四项。 | (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationConstantLedger AND Psi0ZetaLogDerivativeContourShiftBoundLedger AND Psi0ZeroBoundaryAvoidanceLimitLedger) |
| PerronKernelTruncationConstantForPsi0Ledger | `false` | `false` | 只有右边 Perron 核常数和 zeta 对数导数轮廓界都完成后，才能关闭 R_T 常数。 | (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationConstantLedger AND Psi0ZetaLogDerivativeContourShiftBoundLedger AND Psi0ZeroBoundaryAvoidanceLimitLedger) |
| ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger | `false` | `false` | 截断核之后还要把零点自由带代入零点和数值预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |
| PerronTruncationTrivialZeroPrimePowerTailBudgetLedger | `false` | `false` | 平凡零点和素数幂尾项仍需同口径预算。 | PerronTruncationTrivialZeroPrimePowerTailBudgetLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationConstantLedger AND Psi0ZetaLogDerivativeContourShiftBoundLedger AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

当前最窄点更新为 `Psi0RightEdgePerronKernelApproximationConstantLedger`；之后是 `Psi0ZetaLogDerivativeContourShiftBoundLedger`。
