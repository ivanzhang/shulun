# Prime Matrix B=3 平凡零点/素数幂/尾项预算路由器

**状态：** `trivial_tail_prime_power_budget_closed_theta_open`

`PerronTruncationTrivialZeroPrimePowerTailBudgetLedger` 已按初等口径关闭：psi_0 精确公式给出 -log(2pi) 和平凡零点项，端点半权 convention 防止端点重复计费，素数幂转移由 PC1 低阶账本承担。该闭合只处理尾项归属和可界性，不推出 theta@20000 小误差。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
trivial_tail_prime_power_budget_closed=true
row_column_unconditional_closed=false
```

## 1. 替换

```text
PerronTruncationTrivialZeroPrimePowerTailBudgetLedger
  =>
PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000
```

## 2. 锚点压力诊断

| item | value |
| --- | ---: |
| log(2pi) | `1.837877066409` |
| trivial zero log term | `0.000000001250` |
| static relative to x=20000 | `0.000091893853` |
| static beats theta target | `false` |
| exact prime-power Chebyshev weight at 20000 | `171.201064434665` |
| prime-power relative to x=20000 | `0.008560053222` |

该表说明尾项可归账，但不能自动替代 `ThetaEnvelopeTargetAt20000NumericalBudgetLedger`。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TrivialTailPrimePowerGateActive | `true` | `true` | 零点和预算之后，当前最窄点是同一 psi_0/Perron 口径下的平凡零点、素数幂和尾项账本。 | PerronTruncationTrivialZeroPrimePowerTailBudgetLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| Psi0ExactFormulaAvailable | `true` | `true` | 内部 psi_0 精确公式已经给出常数项 -log(2pi) 与平凡零点项 -1/2 log(1-x^-2)。 | InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost |
| EndpointHalfWeightConventionAvailable | `true` | `true` | Chebyshev psi_0 端点半权 convention 已闭合，避免端点重复计费。 | ChebyshevPsi0EndpointHalfWeightConventionClosed |
| PrimePowerTransferAvailable | `true` | `true` | 素数幂到 theta/素数 Chebyshev 权的转移已在 PC1 账本中登记，可作为初等低阶项。 | PrimePowerThetaPsiTransferLedgerClosed |
| NontrivialZeroBudgetAlreadySeparated | `true` | `false` | 非平凡零点和预算已经由上一层外部条件账本关闭，本步不再重复支付。 | ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536 |
| PerronTruncationTrivialZeroPrimePowerTailBudgetLedger | `true` | `true` | 平凡零点、公式常数、端点半权和素数幂转移闭合为初等尾项账本。 | PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000 |
| ThetaTargetStillSeparate | `false` | `false` | 这些尾项有界不等于 theta@20000 小误差目标；theta 目标仍需外部 Dusart 或独立有限桥。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger |
| FiniteLowHeightStillSeparate | `false` | `false` | 低高度零点核验仍与本初等尾项账本无关。 | FiniteLowHeightZeroCheckLedger |

## 4. 最新输入基

外部 Titchmarsh+CN16 路线输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ZetaLogDerivativeContourShiftExternalClosedC12000) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536 AND PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

下一步攻 `ThetaEnvelopeTargetAt20000NumericalBudgetLedger`；低高度核验 `FiniteLowHeightZeroCheckLedger` 仍独立开放。
