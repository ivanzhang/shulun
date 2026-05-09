# Prime Matrix B=3 psi_0 zeta 对数导数轮廓移线路由器

**状态：** `zeta_logder_contour_shift_reduced_fixed_t_gap_open`

轮廓移线已经压到真正缺口：留数和左边界不是问题，问题是 fixed-T 水平边可能贴近零点，必须证明固定高度缩进成本，或明确把合同改成 T* 好高度版本。当前 fixed-T 自足链未闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
zeta_logder_contour_shift_reduced=true
zeta_logder_contour_shift_closed=false
row_column_unconditional_closed=false
```

## 1. 替换

```text
Psi0ZetaLogDerivativeContourShiftBoundLedger
  =>
(Psi0ContourResidueAndLeftEdgeClosed AND Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (Psi0FixedHeightZeroProximityIndentationCostLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger))
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ContourShiftGateActive | `true` | `false` | 右边 Perron 核已闭合后，当前最窄点是把右边竖线积分移线成零点留数。 | Psi0ZetaLogDerivativeContourShiftBoundLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ResidueAndLeftEdgeClosed | `true` | `true` | 留数清单与左边界衰减已由内部 psi_0 精确公式吸收；这里不再重复付费。 | Psi0ContourResidueAndLeftEdgeClosed |
| HorizontalLogDerivativeBoundMissing | `false` | `false` | 还缺避开零点后的水平边 -zeta'/zeta 显式上界。 | Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger |
| FixedHeightZeroProximityCostMissing | `false` | `false` | 若坚持固定 T 截断，必须支付 T 附近零点贴近水平边的缩进/近零成本。 | Psi0FixedHeightZeroProximityIndentationCostLedger |
| GoodHeightTStarAlternativeOpen | `false` | `false` | 若允许改成 T* in [T,2T]，可走平均好高度路线，但这会改变当前 fixed-T 合同。 | Psi0GoodHeightTStarAveragingContourShiftLedger |
| ContourShiftReducedToFixedTOrGoodHeight | `true` | `false` | 轮廓移线原子已压成留数左边界、水平边 log-derivative、固定 T 缩进或好高度替代。 | (Psi0ContourResidueAndLeftEdgeClosed AND Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (Psi0FixedHeightZeroProximityIndentationCostLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger)) |
| Psi0ZetaLogDerivativeContourShiftBoundLedger | `false` | `false` | 当前 fixed-T 轮廓移线未闭合；缺口是水平边 log-derivative 和零点贴近成本。 | (Psi0ContourResidueAndLeftEdgeClosed AND Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (Psi0FixedHeightZeroProximityIndentationCostLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger)) |
| ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger | `false` | `false` | 轮廓移线闭合后，才进入零点自由区下的零点和数值预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |

## 3. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ContourResidueAndLeftEdgeClosed AND Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (Psi0FixedHeightZeroProximityIndentationCostLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger)) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

fixed-T 自足路线先攻 `Psi0FixedHeightZeroProximityIndentationCostLedger`；并行可攻 `Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger`。若改合同，则研究 `Psi0GoodHeightTStarAveragingContourShiftLedger`。
