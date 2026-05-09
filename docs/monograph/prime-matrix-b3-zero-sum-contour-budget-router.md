# Prime Matrix B=3 零点自由区零点和轮廓预算路由器

**状态：** `zero_sum_contour_budget_external_closed_self_contained_open`

外部条件路线下，`ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger` 可由经典零点自由区 PNT 轮廓引理关闭：C=1280,T0=14 的零点自由带、RVM 零点计数和 finite-T Perron 口径合并，给出保守 C_Z=65536 的非平凡零点和预算。这只关闭零点和预算本身，不关闭 theta@20000、不关闭平凡尾项、不关闭低高度或行列无条件命题。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
zero_sum_contour_budget_external_closed=true
zero_sum_contour_budget_self_contained_closed=false
row_column_unconditional_closed=false
C_region=1280.000000000000
T0=14.000000000000
C_zero_sum=65536.000000000000
```

## 1. 外部条件替换

```text
ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger
  =>
ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536
```

## 2. 外部引理内容

接受的外部引理是经典零点自由区 PNT 轮廓估计：在 RVM 零点计数、`beta <= 1-1/(1280 log(|gamma|+3))` 与 finite-T Perron 口径下，非平凡零点和可被形如 `C_Z*x*log^2(x(T+3))*exp(-log(x)/(1280 log(T+3)))` 的保守预算控制。

来源登记：Titchmarsh--Heath-Brown/Ingham zero-free-region PNT contour lemma; Dusart arXiv:1002.0442 records explicit prime-function estimates using zero-free regions。公共入口：https://arxiv.org/abs/1002.0442。

## 3. x=20000 压力诊断

| item | value |
| --- | ---: |
| x | `20000` |
| T0 | `14` |
| zero-free suppression at T0 | `0.997272868695` |
| relative envelope with C=65536 | `10602489.106158368289` |
| theta target relative error | `0.000027578599007` |
| beats theta target | `false` |
| balancing log-height below T0 | `true` |

该诊断只说明边界：本账本关闭“零点和预算有界”，并不产生 `theta@20000` 所需的小误差。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ZeroSumContourBudgetGateActive | `true` | `true` | Perron 截断层条件闭合后，当前最窄外部条件点就是 C=1280,T0=14 的非平凡零点和预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍在假设反例链条内补解析输入，不使用真实零行缺席或实验替代证明。 | 保持 row_column_unconditional_closed=false。 |
| ZeroFreeRegionC1280T14Available | `true` | `true` | 高高度零点自由带 beta<=1-1/(1280 log(\|gamma\|+3)), \|gamma\|>=14 已由前置参数账本给出。 | ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 |
| FiniteTPerronLayerAvailable | `true` | `false` | finite-T Perron 截断层已由外部 fixed-T 缩进、水平边预算和右边核合并为 C=12128。 | PerronKernelTruncationForPsi0ExternalClosedC12128 |
| ClassicalZeroSumContourLemmaRegistered | `true` | `false` | 接受 Titchmarsh--Heath-Brown/Ingham 型零点自由区 PNT 轮廓引理：RVM 零点计数加零点自由带给出有限高度零点和预算。 | Titchmarsh--Heath-Brown/Ingham zero-free-region PNT contour lemma; Dusart arXiv:1002.0442 records explicit prime-function estimates using zero-free regions |
| ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger | `true` | `false` | 外部条件路线下，零点自由区非平凡零点和预算闭合为保守 C_Z=65536 账本。 | ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536 |
| SelfContainedZeroSumContourBudgetStillOpen | `false` | `false` | 严格自足版本仍需文内重建 dyadic 零点计数积分、轮廓高度优化和常数算术。 | InternalZeroSumDyadicContourBudgetLedger |
| TrivialTailStillSeparate | `false` | `false` | 本步只支付非平凡零点和主预算；平凡零点、素数幂和截断尾仍是独立账本。 | PerronTruncationTrivialZeroPrimePowerTailBudgetLedger |
| ThetaTargetStillSeparate | `false` | `false` | C=1280,T0=14 的普通零点自由区预算在 x=20000 不足以给 1/36260 级 theta 目标。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger |
| FiniteLowHeightStillSeparate | `false` | `false` | T0 以下零点排除仍由独立有限核验证书承担。 | FiniteLowHeightZeroCheckLedger |

## 5. 最新输入基

外部 Titchmarsh+CN16 路线输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ZetaLogDerivativeContourShiftExternalClosedC12000) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536 AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

下一步攻 `PerronTruncationTrivialZeroPrimePowerTailBudgetLedger`；并行自足缺口仍是 `ClassicalBacklundZeroIndentationCostInternalProofLedger` 与零点和内部 dyadic 预算四输入。
