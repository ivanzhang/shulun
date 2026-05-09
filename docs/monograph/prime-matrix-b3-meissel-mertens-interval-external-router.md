# Prime Matrix B=3 Meissel-Mertens 常数区间外部路由器

**状态：** `meissel_mertens_interval_external_closed_self_contained_open`

外部条件路线下，`SelfContainedMeisselMertensConstantIntervalLedgerAt20000` 可由已有 Dusart 型素数倒数和显式 Mertens 证书聚合关闭：有限阶梯覆盖 `286<=x<10372`，尾段 `x>=10372` 由外部定理匹配，B1 口径采用 `0.2614972128476428`。该步不是自足 B1/尾段证明；它只把外部 B3 解析主链推进到最终 DStructure/Rankin 独立验收门。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
meissel_mertens_interval_external_closed=true
meissel_mertens_interval_self_contained_closed=false
row_column_unconditional_closed=false
```

## 1. 外部条件替换

```text
SelfContainedMeisselMertensConstantIntervalLedgerAt20000
  =>
DusartMeisselMertensConstantIntervalAt20000ExternalClosed
```

## 2. Mertens 外部证书数字

| item | value |
| --- | ---: |
| Meissel-Mertens B1 | `0.261497212848` |
| finite step range | `[286, 10372]` |
| tail start x | `10372` |
| Dusart tail error at start | `0.001506804667` |
| external atom | `DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MeisselMertensIntervalGateActive | `true` | `true` | Dusart theta 包络与有限桥之后，外部主链当前最窄点是 B1/Meissel-Mertens 常数区间输入。 | SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只补假设反例链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ThetaEnvelopeAlreadyClosedExternally | `true` | `false` | 上一层已经用 Dusart 全局 theta 界关闭 x>=20000 包络和有限桥。 | DusartThetaEnvelopeXGe20000ExternalClosedOneOver36260 AND DusartThetaEnvelopeFiniteBridgeExternalClosedAllXPositive |
| DusartReciprocalPrimeMertensExternalReady | `true` | `false` | 已有显式素数倒数 Mertens 外部证书给出有限阶梯、尾段 Dusart 匹配和 B1 常数口径。 | DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted |
| SelfContainedMeisselMertensConstantIntervalLedgerAt20000 | `true` | `false` | 接受 Dusart/Rosser-Schoenfeld 型素数倒数和外部定理后，B1 常数区间输入在外部路线中关闭。 | DusartMeisselMertensConstantIntervalAt20000ExternalClosed |
| B3LocalRosserAnchorAlreadyPresent | `true` | `true` | B3 Rosser 面字典和 alpha=0.43 锚点变差预算已经在当前输入基中登记。 | B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043 |
| SelfContainedMertensStillOpen | `false` | `false` | 严格自足路线仍需内联 B1 区间算术与 reciprocal-prime Mertens 尾段证明。 | SelfContainedMeisselMertensB1IntervalArithmeticLedger AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| SelfContainedBasisUnchanged | `true` | `true` | 本路由只替换外部输入基；自足输入基保留 Meissel-Mertens 常数区间原子。 | SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| DStructureRankinGateStillSeparate | `false` | `false` | B3 解析外部链闭合后，最终行列无条件命题仍需 DStructure/Rankin 独立验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最新输入基

外部 Titchmarsh+CN16 路线输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost) AND (Psi0PerronFiniteRectangleHeightSelectionLedger AND Psi0RightEdgePerronKernelApproximationClosedC128 AND (Psi0ZetaLogDerivativeContourShiftExternalClosedC12000) AND Psi0ZeroBoundaryAvoidanceLimitLedger) AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourBudgetExternalClosedC1280T14C65536 AND PerronTrivialZeroPrimePowerTailBudgetClosedElementaryXGe20000) AND DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260) AND FiniteLowHeightZeroCheckExternalClosedFirstZeroGT14TuringComplete) AND DusartThetaEnvelopeXGe20000ExternalClosedOneOver36260 AND DusartThetaEnvelopeFiniteBridgeExternalClosedAllXPositive) AND DusartMeisselMertensConstantIntervalAt20000ExternalClosed))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

外部 B3 解析主链下一步为 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；自足路线仍保留 `SelfContainedMeisselMertensB1IntervalArithmeticLedger, SelfContainedDusartReciprocalPrimeProofAppendixXGe10372`。
