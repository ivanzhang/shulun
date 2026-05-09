# Prime Matrix B=3 零点自由区到 PNT 轮廓常数路由器

**状态：** `pnt_contour_constant_reduced_to_microledgers_open`

PNT 轮廓常数层已被压到三个更窄微账本：非平滑 Chebyshev/Perron 常数账本、C=1280,T0=14 的零点和轮廓数值预算、以及平凡零点/素数幂/截断尾同口径预算。当前材料不能直接关闭该层，更不能自动推出 x=20000 的 1/36260 级 theta 目标。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
pnt_contour_constant_reduced=true
pnt_contour_constant_closed=false
row_column_unconditional_closed=false
```

## 1. 微账本替换

```text
ZeroFreeRegionToExplicitPNTContourConstantLedger
  =>
(UnsmoothedChebyshevPerronExplicitFormulaConstantLedger AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger)
```

## 2. 来源审查

| item | value |
| --- | --- |
| smooth_explicit_formula_available | `true` |
| unsmoothed_perron_formula_constantized | `false` |
| dusart_theta_target_registered | `true` |
| explicit_zero_sum_truncation_budget_present | `false` |

## 3. x=20000 压力诊断

| item | value |
| --- | ---: |
| anchor x | `20000` |
| log(anchor x) | `9.903487552536` |
| target relative error | `0.000027578599007` |
| zero-free c | `0.000781250000000` |
| diagnostic exponent sqrt(c)/4 | `0.006987712429687` |
| diagnostic factor at 20000 | `0.978249825587` |
| log x needed for target if K=1 | `2.257262e+06` |

该表只用于说明常数压力：普通零点自由区型 PNT 误差远不足以在 `x=20000` 直接达到 Dusart 级目标。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PNTContourGateActive | `true` | `false` | 上一层已把 C_log 与零点排斥参数闭合，当前最窄点转为 PNT 轮廓常数。 | ZeroFreeRegionToExplicitPNTContourConstantLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ZeroRepulsionC1280T14Ready | `true` | `true` | 已取得高高度零点自由带 beta<=1-1/(1280 log(\|gamma\|+3)), \|gamma\|>=14。 | 低高度仍由独立有限账本处理。 |
| SmoothExplicitFormulaAvailable | `true` | `true` | 仓库已有平滑 Chebyshev 显式公式和素数幂低阶吸收接口。 | SmoothChebyshevExplicitFormulaAppendixClosed |
| UnsmoothedPerronConstantLedgerMissing | `false` | `false` | 还没有把非平滑 psi/theta 的 Perron 截断、端点误差和常数写成可复核账本。 | UnsmoothedChebyshevPerronExplicitFormulaConstantLedger |
| ZeroSumContourNumericalBudgetMissing | `false` | `false` | 还没有把 C=1280,T0=14 零点自由带代入零点和、截断高度、平凡零点尾项的数值预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |
| TrivialTailAndPrimePowerBudgetStillNeeded | `false` | `false` | 平凡零点、素数幂和截断尾必须与非平滑 Perron 同口径登记，不能由平滑公式自动替代。 | PerronTruncationTrivialZeroPrimePowerTailBudgetLedger |
| PNTContourConstantReducedToMicroLedgers | `true` | `false` | 旧 PNT 轮廓常数原子已压成非平滑 Perron 常数、零点和预算、平凡/截断尾预算三个微账本。 | (UnsmoothedChebyshevPerronExplicitFormulaConstantLedger AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) |
| ZeroFreeRegionToExplicitPNTContourConstantLedger | `false` | `false` | 只有三个微账本全部完成后，才能说零点自由区到显式 PNT 轮廓常数闭合。 | (UnsmoothedChebyshevPerronExplicitFormulaConstantLedger AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) |
| ThetaTargetAt20000StillSeparate | `false` | `false` | 即使 PNT 轮廓常数完成，x=20000 的 1/36260 级目标仍需单独预算或外部 Dusart/有限桥。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger |
| FiniteLowHeightStillSeparate | `false` | `false` | T0 以下零点排除仍是独立有限证书，不能并入高高度轮廓预算。 | FiniteLowHeightZeroCheckLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (UnsmoothedChebyshevPerronExplicitFormulaConstantLedger AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

当前最窄点更新为 `UnsmoothedChebyshevPerronExplicitFormulaConstantLedger`；随后是 `ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger` 与 `PerronTruncationTrivialZeroPrimePowerTailBudgetLedger`。`ThetaEnvelopeTargetAt20000NumericalBudgetLedger` 和 `FiniteLowHeightZeroCheckLedger` 保持独立。
