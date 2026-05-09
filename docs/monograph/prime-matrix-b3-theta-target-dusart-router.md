# Prime Matrix B=3 theta@20000 外部 Dusart 目标路由器

**状态：** `theta_target_external_closed_self_contained_open`

外部条件路线下，`ThetaEnvelopeTargetAt20000NumericalBudgetLedger` 可由 Dusart Proposition 5.1 关闭：`vartheta(x)-x < x/36260` 对所有 `x>0` 成立，因此在锚点 `x=20000` 精确给出目标相对误差。该步不是自足证明，也不关闭低高度零点核验、后续有限桥、Mertens 区间账本、DStructure/Rankin 守门项或行列无条件命题。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
theta_target_external_closed=true
theta_target_self_contained_closed=false
row_column_unconditional_closed=false
```

## 1. 外部条件替换

```text
ThetaEnvelopeTargetAt20000NumericalBudgetLedger
  =>
DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260
```

## 2. 外部引理内容

接受的外部引理为 Dusart Proposition 5.1：`vartheta(x)-x < x/36260` 对所有 `x>0` 成立。

来源：Pierre Dusart, Estimates of some functions over primes without R.H., arXiv:1002.0442, Proposition 5.1。公共入口：https://arxiv.org/abs/1002.0442。

## 3. x=20000 目标预算

| item | value |
| --- | ---: |
| x | `20000` |
| target denominator | `36260` |
| relative error | `0.000027578599007` |
| absolute allowance | `0.551571980143` |
| Chebyshev multiplier | `1.000027578599` |
| valid for anchor | `true` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ThetaTargetGateActive | `true` | `true` | 平凡尾项账本之后，外部条件路线的当前最窄点正是 theta@20000 小误差输入。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步只补假设反例链条需要的解析输入，不使用真实零行缺席或统计替代证明。 | 保持 row_column_unconditional_closed=false。 |
| TrivialTailBudgetAlreadyClosed | `true` | `true` | 上一层已把 psi_0 平凡零点、端点半权、素数幂尾项归账，theta 目标可以作为独立 Chebyshev 显式界输入处理。 | PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000 |
| DusartProposition51Registered | `true` | `false` | 接受 Dusart Proposition 5.1：vartheta(x)-x < x/36260 对所有 x>0 成立。 | Pierre Dusart, Estimates of some functions over primes without R.H., arXiv:1002.0442, Proposition 5.1 |
| ThetaEnvelopeTargetAt20000NumericalBudgetLedger | `true` | `false` | 由于 20000>0，Dusart 全局显式界直接给出 theta@20000 目标所需的相对误差 1/36260。 | DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260 |
| SelfContainedThetaTargetStillOpen | `false` | `false` | 严格自足路线若不引用 Dusart，仍需在文内重建 theta 显式界或有限桥。 | InternalDusartThetaEnvelopeProofLedger |
| FiniteLowHeightStillSeparate | `false` | `false` | 低高度零点核验不是 theta 目标的一部分，仍需独立关闭。 | FiniteLowHeightZeroCheckLedger |
| DStructureRankinGateStillSeparate | `false` | `false` | 即使外部解析链继续推进，行列无条件命题仍需 DStructure/Rankin 独立验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| SelfContainedBasisUnchanged | `true` | `true` | 本路由只替换外部输入基；自足输入基保留 theta 原子，防止误报自足闭合。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger |

## 5. 最新输入基

外部 Titchmarsh+CN16 路线输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ZetaLogDerivativeContourShiftExternalClosedC12000) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536 AND PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000) AND DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

下一步攻 `FiniteLowHeightZeroCheckLedger`；随后连接 `ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion`、`FiniteThetaEnvelopeBridgeBelowAnalyticThreshold` 和 `SelfContainedMeisselMertensConstantIntervalLedgerAt20000`。严格自足线仍保留 `ClassicalBacklundZeroIndentationCostInternalProofLedger` 与内部 theta 证明账本。
