# Prime Matrix B=3 Gamma 主项局部差分闭合证书

**状态：** `gamma_main_local_difference_closed_cmain4`

Gamma 主项局部差分已用保守 C_main=4 闭合。RVM 局部计数现在真正剩余的是 Backlund/arg zeta 显式上界、端点 convention 与 CN16 合并。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
gamma_main_local_difference_closed=true
C_main=4.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
GammaMainTermLocalDifferenceNumericalLedger
  =>
GammaMainTermLocalDifferenceNumericalClosedCmain4
```

## 2. 文内证明

RVM 主项中的 Gamma 辐角可写成

```text
Theta(T)=arg Gamma(1/4+iT/2) - (T/2)log pi.
Theta'(T)=1/2 Re psi(1/4+iT/2) - 1/2 log pi.
```

由上一 Gamma/digamma 账本，`|Theta'(T)|<=2 log(T+3)`。所以长度 2 的局部差满足

```text
|Theta(T+1)-Theta(T-1)| <= 4 log(T+3).
```

因此取 `C_main=4` 支付 Gamma 主项局部差分。

## 3. 主项尺度审计

| T | log(T+3) | main scale | C_main bound | slack |
| ---: | ---: | ---: | ---: | ---: |
| 0 | `1.098612288668` | `0.000000000000` | `4.394449154672` | `4.394449154672` |
| 1 | `1.386294361120` | `0.000000000000` | `5.545177444480` | `5.545177444480` |
| 2 | `1.609437912434` | `0.000000000000` | `6.437751649736` | `6.437751649736` |
| 10 | `2.564949357462` | `0.147921159051` | `10.259797429846` | `10.111876270795` |
| 100 | `4.634728988230` | `0.880856757930` | `18.538915952919` | `17.658059194988` |
| 10000 | `9.210640326985` | `2.346727955689` | `36.842561307941` | `34.495833352252` |
| 1e+06 | `13.815513557960` | `3.812599153448` | `55.262054231839` | `51.449455078391` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| GammaMainLocalDifferenceGateActive | `true` | `false` | 上一层唯一内部最窄点是 RVM Gamma 主项在 [T-1,T+1] 上的数值差分界。 | GammaMainTermLocalDifferenceNumericalLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ArgumentPrincipleAvailable | `true` | `true` | xi 矩形 argument principle 计数层已闭合。 | 无形式计数剩余。 |
| DigammaBoundAvailable | `true` | `true` | Gamma/digamma 的统一 log 界已由 C_gamma=24 账本给出。 | 无 Gamma/digamma 基础剩余。 |
| GammaThetaDerivativeBoundClosed | `true` | `true` | 由 Theta'(T)=1/2 Re psi(1/4+iT/2)-1/2 log pi 与 digamma 界，\|Theta'(T)\|<=2 log(T+3)。 | 无剩余。 |
| GammaMainLocalDifferenceBoundClosed | `true` | `true` | 在长度 2 区间积分，Gamma 主项局部差由 C_main log(T+3) 支付，C_main=4。 | GammaMainTermLocalDifferenceNumericalClosedCmain4 |
| GammaMainTermLocalDifferenceNumericalLedger | `true` | `true` | 待证 atom 已闭合为 C_main=4 的 Gamma 主项局部差分账本。 | GammaMainTermLocalDifferenceNumericalClosedCmain4 |
| BacklundZetaArgumentStillNext | `false` | `false` | 下一步需要 Backlund/arg zeta 显式上界；这是 RVM 局部计数的真正硬项。 | BacklundZetaArgumentBoundNumericalLedger |
| EndpointAndCN16StillDownstream | `false` | `false` | 端点 convention 与 CN16 合并仍未闭合。 | EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND BacklundZetaArgumentBoundNumericalLedger AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

唯一内部最窄点更新为 `BacklundZetaArgumentBoundNumericalLedger`；随后是 `EndpointZeroAvoidanceMultiplicityConventionLedger` 与 `RVMToCN16LocalInequalityLedger`。
