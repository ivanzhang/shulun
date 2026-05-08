# Prime Matrix B=3 RVM 到 C_N=16 局部计数合并证书

**状态：** `rvm_to_cn16_external_closed_raw_arg_normalization`

RVM 到 C_N=16 的外部分支合并闭合，但依赖一个明确归一化：前序 C_S=8 必须是原始 arg zeta 常数，进入 RVM 的 S(T) 时除以 pi。该解释下总系数约 10.426<16；若把 C_S=8 当成已规范化的 S(T) 常数则失败。完全自足路线仍未闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
rvm_to_cn16_external_closed=true
rvm_to_cn16_self_contained_closed=false
C_main=4.000000000000
C_arg_raw=8.000000000000
C_N_target=16.000000000000
raw_arg_rvm_coefficient=10.426597697578
raw_arg_slack=5.573402302422
normalized_S_rvm_coefficient=24.189752114287
normalized_S_slack=-8.189752114287
row_column_unconditional_closed=false
```

## 1. 外部条件链替换

```text
RVMToCN16LocalInequalityLedger
  =>
RVMToCN16LocalInequalityClosedWithRawArgCS8
```

自足输入基不替换该 atom，因为自足零点排除与自足 Backlund C_S=8 仍开。

## 2. 核心不等式

```text
N(T+1)-N(T-1) <= C_main*L + (2*C_arg/pi)*L_endpoint <= (4 + 16/pi*log(4)/log(3))*L < 16*L, L=log(T+3).
```

`log(T+4)/log(T+3)` 在 `T>=0` 上由 `log(4)/log(3)` 控制。低高度零点由外部 14 以下无零点输入兜底；端点落零由上一步极限 convention 处理。

## 3. 归一化分叉预算

| case | formula | coefficient | target | slack |
| --- | --- | ---: | ---: | ---: |
| raw_arg_backlund | `C_main + (2*C_arg/pi)*log(4)/log(3)` | `10.426597697578` | `16.000000000000` | `5.573402302422` |
| normalized_S_backlund_rejected | `C_main + 2*C_S*log(4)/log(3)` | `24.189752114287` | `16.000000000000` | `-8.189752114287` |

## 4. 高度样本审计

| T | log(T+3) | endpoint ratio | raw-arg coefficient | CN16 slack |
| ---: | ---: | ---: | ---: | ---: |
| 0 | `1.098612288668` | `1.261859507143` | `10.426597697578` | `5.573402302422` |
| 1 | `1.386294361120` | `1.160964047444` | `9.912741340884` | `6.087258659116` |
| 2 | `1.609437912434` | `1.113282752559` | `9.669902500121` | `6.330097499879` |
| 10 | `2.564949357462` | `1.028892567387` | `9.240106816323` | `6.759893183677` |
| 100 | `4.634728988230` | `1.002084676566` | `9.103575349508` | `6.896424650492` |
| 10000 | `9.210640326985` | `1.000010853210` | `9.093013453885` | `6.906986546115` |
| 1e+06 | `13.815513557960` | `1.000000072382` | `9.092958547580` | `6.907041452420` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RVMToCN16GateActive | `true` | `false` | 端点 convention 关闭后，外部 Backlund 分支当前最窄点是把 RVM 局部计数合并到 C_N=16。 | RVMToCN16LocalInequalityLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FormalRVMInputsAvailable | `true` | `true` | argument principle、Gamma 主项 C_main=4、端点重数极限 convention 均已在外部输入基中可用。 | ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND EndpointZeroAvoidanceMultiplicityConventionClosedByLimit |
| ExternalBacklundCS8Available | `true` | `false` | 外部 Backlund 分支已经验收点态原始 arg zeta 常数 C_arg=8。 | BacklundCS8SlackAfterBridgeClosedTightHalf |
| LowHeightExternalZeroInputAvailable | `true` | `false` | 低高度区间由外部首零点/14 以下无非平凡零点输入兜底；自足路线仍未关闭该输入。 | ClassicalFirstZetaZeroHeightGT14ExternalAccepted OR BacklundXiNoNontrivialZeroBelow14ExternalClosed |
| RawArgNormalizationPassesCN16 | `true` | `true` | RVM 中 S(T)=arg zeta/pi；端点两次 arg 贡献为 2*C_arg/pi，再乘 log(T+4)/log(T+3)<=log4/log3。 | coefficient=10.426597697578<16 |
| NormalizedSInterpretationRejected | `true` | `true` | 若把 C_S=8 解释成已经除以 pi 的 S(T) 常数，则系数超过 16；本证书明确不走该解释。 | coefficient=24.189752114287>16 |
| RVMToCN16LocalInequalityLedger | `true` | `true` | 在原始 arg zeta 归一化下，RVM 局部计数合并为 N(T+1)-N(T-1)<=16 log(T+3) 的外部分支输入。 | RVMToCN16LocalInequalityClosedWithRawArgCS8 |
| SelfContainedRVMToCN16StillOpen | `false` | `false` | 完全自足路线仍缺 14 以下零点排除与自足 Backlund C_S=8，因此不能同步替换自足输入基。 | CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger |
| DStructureRankinPromotionNext | `false` | `false` | 外部解析链再往后仍需独立 DStructure/Rankin 验收门，且行列无条件命题未闭合。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationOrCNRelaxationLedger)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionClosedByLimit AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional/external Backlund 输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND ClassicalFirstZetaZeroHeightGT14ExternalAccepted AND BacklundXiNoNontrivialZeroBelow14ExternalClosed) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationNotNeededC16ClosedR4)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationClosedEta1Over16 AND BacklundZeroDistanceSumConstantAggregationClosedC192Eta1Over16) AND BacklundVariationWindowScaleClosedH1Over512C192) AND ClassicalBacklundZeroIndentationCostExternalAccepted)) AND BacklundCS8SlackAfterBridgeClosedTightHalf)) AND EndpointZeroAvoidanceMultiplicityConventionClosedByLimit AND RVMToCN16LocalInequalityClosedWithRawArgCS8) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 下一步

完全自足路线仍先攻 `CriticalLineNoZeroOn0To14FiniteLedger`；外部分支下一验收门为 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
