# Prime Matrix B=3 psi_0 fixed-T 零点缩进路由器

**状态：** `psi0_fixed_t_indentation_reduced_to_backlund_self_open_external_ready`

`Psi0FixedHeightZeroProximityIndentationCostLedger` 不是新的独立剩余。在固定 T 合同下，它与经典 Backlund 近零缩进成本属于同一 formal unit：都要处理水平/矩形边界贴近零点时的局部极点主部、小弧缩进和 jump budget。因此严格自足路线回流到 `ClassicalBacklundZeroIndentationCostInternalProofLedger`；若接受外部 `ClassicalBacklundZeroIndentationCostExternalAccepted`，fixed-T 缩进成本可条件关闭，但完整 `psi_0` 轮廓移线还必须继续证明水平边 away-from-zero 的显式 log-derivative 上界。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
psi0_fixed_t_indentation_reduced_to_backlund=true
psi0_fixed_t_indentation_self_contained_closed=false
psi0_fixed_t_indentation_external_closed=true
zeta_logder_contour_shift_closed=false
row_column_unconditional_closed=false
naive_fixed_t_jump_coefficient=50.265482457437
```

## 1. 原子替换

严格自足 fixed-T 路线：

```text
Psi0FixedHeightZeroProximityIndentationCostLedger
  =>
ClassicalBacklundZeroIndentationCostInternalProofLedger
```

外部 Backlund 条件路线：

```text
Psi0FixedHeightZeroProximityIndentationCostLedger
  =>
ClassicalBacklundZeroIndentationCostExternalAccepted
```

## 2. 局部等价

| psi0 object | Backlund object | common formal unit |
| --- | --- | --- |
| 水平边 integral of -zeta'/zeta(s) x^s/s at Im(s)=T | 固定高度附近 arg zeta / log-derivative 的避零缩进 | 若 rho=beta+i gamma 且 gamma 接近 T，则 -zeta'/zeta(s) 含 m/(s-rho) 主部。 |
| 固定 T 不允许改成 T* 时，水平边可能穿过或贴近零点。 | Backlund 矩形边界也必须处理边界零点和近边界零点。 | 端点极限只给定义，不给 uniform jump budget。 |
| 绕开 rho 的小凹口积分成本进入 finite-T Perron 余项。 | 绕开 rho 的小凹口/branch jump 成本进入 S(T) 或 RVM 常数。 | 未配对正成本都归入同一近零缩进账本。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Psi0FixedTIndentGateActive | `true` | `true` | 上一层轮廓移线已把 fixed-T 缺口定位为水平边贴近零点的缩进成本。 | Psi0FixedHeightZeroProximityIndentationCostLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席或数值实验替代证明。 | 保持 row_column_unconditional_closed=false。 |
| FixedTSingularityObstructionRecorded | `true` | `true` | 若零点高度等于或任意贴近 T，水平边上的 -zeta'/zeta 有极点主部；端点避零 convention 不能给统一成本。 | ClassicalBacklundZeroIndentationCostInternalProofLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |
| FormalUnitMatchesBacklundIndentation | `true` | `true` | psi_0 fixed-T 凹口与 Backlund 边界凹口使用同一局部 Laurent 主部、同一避零小弧和同一 jump budget。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| NaivePerZeroJumpBudgetRejected | `true` | `true` | 按 C_N=16 个零点逐个付 pi 级跳变会产生约 50.265 的系数，不能作为本项目小余量闭合。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| ExternalBacklundIndentTransfersConditionally | `true` | `false` | 若接受经典 Backlund 零点缩进外部引理，fixed-T 缩进成本本身可在条件路线中关闭。 | ClassicalBacklundZeroIndentationCostExternalAccepted |
| SelfContainedBacklundIndentStillOpen | `true` | `true` | 严格自足路线没有新逃逸口：该 fixed-T 缺口回流到经典 Backlund 缩进内部证明。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| Psi0FixedHeightZeroProximityIndentationCostLedger | `false` | `false` | 作者侧严格自足版未闭合；本步只完成原子等价和条件外部转接。 | ClassicalBacklundZeroIndentationCostInternalProofLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |
| Psi0ContourShiftStillNeedsHorizontalBound | `false` | `false` | 即使外部缩进成本被接受，完整 zeta 对数导数轮廓移线仍需水平边 away-from-zero 显式上界。 | Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger |

## 4. 最新输入基

fixed-T 严格自足输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ContourResidueAndLeftEdgeClosed AND Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (ClassicalBacklundZeroIndentationCostInternalProofLedger OR Psi0GoodHeightTStarAveragingContourShiftLedger)) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

接受外部 Backlund 缩进后的 fixed-T 条件输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ContourResidueAndLeftEdgeClosed AND Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger AND (ClassicalBacklundZeroIndentationCostExternalAccepted OR Psi0GoodHeightTStarAveragingContourShiftLedger)) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

严格自足路线继续攻 `ClassicalBacklundZeroIndentationCostInternalProofLedger`；若接受外部 Backlund 缩进，则下一步攻 `Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger`。
