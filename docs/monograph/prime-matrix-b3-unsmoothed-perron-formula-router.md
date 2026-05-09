# Prime Matrix B=3 非平滑 Chebyshev/Perron 显式公式路由器

**状态：** `unsmoothed_perron_formula_reduced_to_classical_formula_and_kernel_open`

非平滑 Chebyshev/Perron 子账本已经压到最小可审查合同：要么接受经典 von Mangoldt 显式公式并登记适用常数，要么在文内证明 psi_0(x) 的 Perron 截断公式及 R_T 常数。当前材料只有平滑公式、非正式 psi(x)-x 说明和其他对象的 Perron 模板，尚未关闭本原子。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
unsmoothed_perron_formula_reduced=true
unsmoothed_perron_formula_closed=false
row_column_unconditional_closed=false
```

## 1. 替换

```text
UnsmoothedChebyshevPerronExplicitFormulaConstantLedger
  =>
(ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger AND PerronKernelTruncationConstantForPsi0Ledger AND ChebyshevPsi0EndpointHalfWeightConventionClosed)
```

## 2. 目标公式合同

| item | value |
| --- | --- |
| psi0_definition | `psi_0(x)=sum_{n<x} Lambda(n)+1/2 Lambda(x) if x is an integer` |
| target_formula | `psi_0(x)=x-sum_{\|gamma\|<=T} x^rho/rho-log(2*pi)-1/2 log(1-x^-2)+R_T(x)` |
| target_remainder_shape | `\|R_T(x)\| <= C_Perron*x*log^2(xT)/T + C_edge*log x` |
| validity_needed | `x>=20000, T>=14, endpoint convention fixed` |

## 3. 来源审查

| item | value |
| --- | --- |
| smooth_formula_closed | `true` |
| informal_von_mangoldt_formula_present | `true` |
| generic_perron_template_present | `true` |
| psi0_constantized_formula_present | `false` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| UnsmoothedPerronGateActive | `true` | `false` | 上一层已把 PNT 轮廓常数压到非平滑 Perron 公式、零点和预算、尾项预算。 | UnsmoothedChebyshevPerronExplicitFormulaConstantLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| UpstreamPNTMicroReductionAvailable | `true` | `true` | PNT 轮廓层已经完成微账本拆分，因此本步可以专攻非平滑 Perron 子账本。 | 无上游拆分剩余。 |
| SmoothFormulaDoesNotSufficeButIsAvailable | `true` | `true` | 平滑 Mellin 显式公式已闭合，但只能作为推导背景，不能直接替代 psi/theta 的非平滑常数公式。 | 需要非平滑 Perron 内联或外部接受。 |
| InformalVonMangoldtFormulaPresent | `true` | `false` | 文稿已有 psi(x)-x=-sum x^rho/rho+低阶项的非正式说明。 | 尚未给常数化截断余项。 |
| GenericPerronTemplatePresent | `true` | `false` | 主稿有其他对象的 Perron 截断模板，可复用思路但不能自动覆盖 zeta von Mangoldt 公式。 | 需写成 psi_0 专用账本。 |
| EndpointHalfWeightConventionClosed | `true` | `true` | 采用 psi_0 半权端点定义后，整数跳点误差被固定为 O(log x) 口径。 | ChebyshevPsi0EndpointHalfWeightConventionClosed |
| Psi0PerronConstantizedFormulaMissing | `false` | `false` | 还没有目标公式中 R_T(x) 的显式常数 C_Perron、C_edge 与适用区间证书。 | ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger AND PerronKernelTruncationConstantForPsi0Ledger |
| UnsmoothedPerronFormulaReducedToClassicalFormulaAndKernel | `true` | `false` | 旧非平滑 Perron 原子已压成经典公式接受/内联证明、Perron 截断核常数、端点半权口径。 | (ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger AND PerronKernelTruncationConstantForPsi0Ledger AND ChebyshevPsi0EndpointHalfWeightConventionClosed) |
| UnsmoothedChebyshevPerronExplicitFormulaConstantLedger | `false` | `false` | 只有 psi_0 目标公式和 R_T 常数账本完成后，才能关闭非平滑 Perron 子账本。 | (ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger AND PerronKernelTruncationConstantForPsi0Ledger AND ChebyshevPsi0EndpointHalfWeightConventionClosed) |
| ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger | `false` | `false` | 非平滑公式闭合后，还要把 C=1280,T0=14 代入零点和轮廓预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |
| PerronTruncationTrivialZeroPrimePowerTailBudgetLedger | `false` | `false` | 平凡零点、素数幂与截断尾仍需同一公式口径下登记。 | PerronTruncationTrivialZeroPrimePowerTailBudgetLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND ((ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger AND PerronKernelTruncationConstantForPsi0Ledger AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

当前最窄点更新为 `ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger`；若选择文内自足证明，核心就是 `PerronKernelTruncationConstantForPsi0Ledger`。之后才进入 `ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger`。
