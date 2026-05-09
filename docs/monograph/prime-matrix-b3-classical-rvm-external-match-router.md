# Prime Matrix B=3 经典 Riemann-von Mangoldt 外部公式匹配路由器

**状态：** `classical_rvm_external_candidate_registered_strict_match_open`

外部 Riemann-von Mangoldt 显式公式候选已经定位，但它按高阈值 log x>=40、较大 T 下界和 T*∈[T,2T] 截断点工作，且以 psi(x) 而非 psi_0 半权端点叙述。因此它可以作为高阈值参考，不能严格关闭本项目 x>=20000,T>=14 的自足合同；下一步仍需内部 all-x Perron 证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
classical_rvm_external_match_reduced=true
classical_rvm_external_strict_match_closed=false
row_column_unconditional_closed=false
```

## 1. 替换

```text
ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger
  =>
(CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger)
```

## 2. 外部候选合同

| item | value |
| --- | --- |
| external_source | `Cully-Hugill and Johnston, On the error term in the explicit formula of Riemann-von Mangoldt II` |
| external_url | `https://arxiv.org/abs/2402.04272` |
| external_shape | `psi(x)=x-sum_{\|gamma\|<=T*}x^rho/rho+O*(M*x*(log x)^(1-omega)/T)` |
| external_min_log_x | `40.0` |
| external_uses_T_star_in_T_2T | `True` |
| contract_anchor_x | `20000.0` |
| contract_log_anchor_x | `9.903487552536127` |
| contract_min_T | `14.0` |
| external_min_T_at_anchor_if_applicable | `98.07906570323802` |
| threshold_match | `False` |
| t_lower_bound_match | `False` |
| fixed_T_match | `False` |
| psi0_half_weight_match | `False` |
| strict_match_closed | `False` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ClassicalRvMGateActive | `true` | `false` | 上一层最窄点要求接受经典 von Mangoldt 显式公式或给出内联证明。 | ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只审查假设链条解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ExternalRvMHighThresholdCandidateRegistered | `true` | `false` | Cully-Hugill/Johnston 给出显式截断 Riemann-von Mangoldt 公式候选。 | CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered |
| ExternalThresholdDoesNotMatchX20000 | `false` | `false` | 该外部定理按 log x>=40 等高阈值使用，不能直接覆盖 x=20000。 | 需要有限桥或内部 all-x Perron 证明。 |
| ExternalTWindowDoesNotMatchT14 | `false` | `false` | 外部定理需要较大 T 下界且使用某个 T* in [T,2T]，不能直接替代固定 T>=14 合同。 | 需要重新参数化或内部截断核账本。 |
| Psi0HalfWeightNotMatchedByExternalPsiStatement | `false` | `false` | 外部候选以 psi(x) 叙述；本项目合同需要 psi_0 半权端点和端点误差口径。 | InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger |
| ExternalStrictMatchClosed | `false` | `false` | 只有阈值、T 窗口、固定截断点和 psi_0 端点全部匹配后才能接受为本原子闭合。 | InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger |
| ClassicalRvMExternalMatchReduced | `true` | `false` | 外部候选已登记但不能直接关闭；本原子被压成高阈值外部候选或内部 all-x Perron 证明。 | (CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger) |
| ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger | `false` | `false` | 当前外部候选不满足严格对接，因此作者侧自足路线仍需内部 all-x 证明。 | (CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger) |
| PerronKernelTruncationConstantForPsi0Ledger | `false` | `false` | 内部 all-x 证明的核心仍是 Perron 截断核常数账本。 | PerronKernelTruncationConstantForPsi0Ledger |
| ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger | `false` | `false` | 经典公式或内联证明之后，仍需零点和轮廓数值预算。 | ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionClosed) AND CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch) AND ZeroRepulsionParameterNumericalOptimizationClosedC64A1Over256C1Over1280T14 AND (((CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered OR InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger) AND PerronKernelTruncationConstantForPsi0Ledger AND ChebyshevPsi0EndpointHalfWeightConventionClosed) AND ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger AND PerronTruncationTrivialZeroPrimePowerTailBudgetLedger) AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

当前最窄点更新为 `InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger`；其核心计算账本是 `PerronKernelTruncationConstantForPsi0Ledger`，随后再进入 `ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger`。
