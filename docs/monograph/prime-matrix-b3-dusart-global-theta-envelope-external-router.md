# Prime Matrix B=3 Dusart 全局 theta 包络外部路由器

**状态：** `dusart_global_theta_envelope_external_closed_self_contained_open`

外部条件路线下，Dusart Proposition 5.1 的全局 theta 界 `vartheta(x)-x < x/36260 (x>0)` 同时关闭 `x>=20000` 的 theta 包络目标和阈值以下有限桥。这一步是外部定理旁路：不等于仓库内已经证明了零点自由区到非平滑 psi/theta 的轮廓常数，也不关闭严格自足路线或最终 DStructure/Rankin 守门项。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
explicit_psi_theta_contour_envelope_external_closed=true
finite_theta_bridge_external_closed=true
explicit_psi_theta_contour_envelope_self_contained_closed=false
finite_theta_bridge_self_contained_closed=false
row_column_unconditional_closed=false
```

## 1. 外部条件替换

| old | new |
| --- | --- |
| `ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion` | `DusartThetaEnvelopeXGe20000ExternalClosedOneOver36260` |
| `FiniteThetaEnvelopeBridgeBelowAnalyticThreshold` | `DusartThetaEnvelopeFiniteBridgeExternalClosedAllXPositive` |

## 2. 外部引理内容

接受的外部引理为 Dusart Proposition 5.1：`vartheta(x)-x < x/36260` 对所有 `x>0` 成立。

来源：Pierre Dusart, Estimates of some functions over primes without R.H., arXiv:1002.0442, Proposition 5.1。公共入口：https://arxiv.org/abs/1002.0442。

## 3. 目标常数

| item | value |
| --- | ---: |
| anchor x | `20000` |
| denominator | `36260` |
| relative error | `0.000027578599007` |
| Chebyshev multiplier | `1.000027578599` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExplicitContourEnvelopeGateActive | `true` | `true` | 低高度核验之后，外部主链当前最窄点是 x>=20000 的显式 psi/theta 包络。 | ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只补假设反例链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| LowHeightAlreadyClosedExternally | `true` | `false` | 上一层已用首零点/Turing 完备性关闭 T<=14 低高度核验。 | FiniteLowHeightZeroCheckExternalClosedFirstZeroGT14TuringComplete |
| DusartGlobalThetaEnvelopeAvailable | `true` | `false` | Dusart Proposition 5.1 的 theta 界对所有 x>0 成立，因此强于 x>=20000 的目标区间。 | DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260 |
| ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion | `true` | `false` | 外部条件路线可用 Dusart 全局 theta 界旁路关闭该 x>=20000 包络；这不是内部 contour 常数证明。 | DusartThetaEnvelopeXGe20000ExternalClosedOneOver36260 |
| FiniteThetaEnvelopeBridgeBelowAnalyticThreshold | `true` | `false` | 同一 Dusart 界对所有 x>0 成立，因此有限桥在外部路线中成为冗余并可关闭。 | DusartThetaEnvelopeFiniteBridgeExternalClosedAllXPositive |
| SelfContainedContourStillOpen | `false` | `false` | 严格自足路线仍需从零点自由区推导非平滑 psi/theta 轮廓常数。 | InternalZeroFreeRegionToThetaContourEnvelopeLedger |
| SelfContainedFiniteBridgeStillOpen | `false` | `false` | 严格自足路线仍需阈值以下 theta 包络有限核验和可复现 hash。 | InternalFiniteThetaEnvelopeBridgeHashLedger |
| SelfContainedBasisUnchanged | `true` | `true` | 本路由只替换外部输入基；自足输入基仍保留 contour 与 finite bridge 原子。 | ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold |
| DStructureRankinGateStillSeparate | `false` | `false` | theta 包络外部闭合不触动最终行列命题的 DStructure/Rankin 独立验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 最新输入基

外部 Titchmarsh+CN16 路线输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ZetaLogDerivativeContourShiftExternalClosedC12000) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536 AND PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000) AND DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260) AND FiniteLowHeightZeroCheckExternalClosedFirstZeroGT14TuringComplete) AND DusartThetaEnvelopeXGe20000ExternalClosedOneOver36260 AND DusartThetaEnvelopeFiniteBridgeExternalClosedAllXPositive) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

下一步攻 `SelfContainedMeisselMertensConstantIntervalLedgerAt20000`。自足路线仍保留 `InternalZeroFreeRegionToThetaContourEnvelopeLedger, InternalFiniteThetaEnvelopeBridgeHashLedger`。
