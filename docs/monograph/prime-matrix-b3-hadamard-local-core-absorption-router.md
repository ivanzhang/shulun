# Prime Matrix B=3 Hadamard 局部零点核心吸收路由器

**状态：** `hadamard_local_core_absorption_closed_by_sign_discard`

Hadamard 局部零点核心吸收闭合：目标零点已单独进入主负项；其余近壳零点在 Re(-zeta'/zeta) 中仍是非正贡献，可丢弃。因此局部核心正预算为 0，C_N=16 只保留为有限性和 multiplicity 安全网。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
local_core_absorption_closed=true
local_core_positive_budget=0.0
row_column_unconditional_closed=false
```

## 1. 替换

```text
HadamardLocalZeroCoreAbsorptionByCN16Ledger
  =>
HadamardLocalZeroCoreAbsorptionClosedBySignDiscard
```

## 2. 局部核心账本

| class | rule | effect |
| --- | --- | --- |
| target_zero | rho=rho0, including multiplicity at the selected zero | charged only to the main negative DVP term |
| same_window_non_target | rho!=rho0 and \|Im rho-gamma0\|<1 | zero kernel is nonnegative, hence contribution to Re(-zeta'/zeta) is nonpositive |
| same_height_or_multiple_neighbor | rho shares ordinate or is arbitrarily close but is not the selected target copy | also nonpositive; no positive C_log budget is charged |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LocalCoreAbsorptionGateActive | `true` | `false` | 上一层最窄点是目标附近 \|Im rho-gamma0\|<1 的非目标零点核心是否消耗正预算。 | HadamardLocalZeroCoreAbsorptionByCN16Ledger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| PairingAndShellConventionReady | `true` | `true` | 目标零点已单独分离，1/rho 项已按符号丢弃，局部核心只剩非目标零点核。 | HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic |
| LocalNonTargetZeroSignDiscardClosed | `true` | `true` | sigma>1 时局部非目标零点核实部非负，在 Re(-zeta'/zeta) 中带负号，DVP 非负组合后仍非正，可丢弃。 | HadamardLocalZeroCoreAbsorptionClosedBySignDiscard |
| CN16NotNeededForPositiveBudget | `true` | `true` | C_N=16 只作为 multiplicity/有限性安全网；局部核心正预算为 0，不需要按个数付费。 | positive local-core budget = 0 |
| HadamardLocalZeroCoreAbsorptionByCN16Ledger | `true` | `true` | 局部零点核心吸收闭合。 | HadamardLocalZeroCoreAbsorptionClosedBySignDiscard |
| RangeConventionStillNext | `false` | `false` | Hadamard 余项最后还需统一 sigma、低高度、kernel 和 C_log 聚合口径。 | HadamardRemainderRangeAndKernelConventionLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND JensenZeroCountingLocalNumericalLedger AND (HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed AND ((HadamardFarZeroQuadraticDecayShapeClosed AND HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros AND HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic) AND HadamardCN16UnitIntervalToDyadicShellCountClosed AND HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel) AND HadamardLocalZeroCoreAbsorptionClosedBySignDiscard AND HadamardRemainderRangeAndKernelConventionLedger) AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

当前最窄点更新为 `HadamardRemainderRangeAndKernelConventionLedger`。
