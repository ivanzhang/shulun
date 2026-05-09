# Prime Matrix B=3 显式零点自由区常数账本路由器

**状态：** `explicit_zero_free_constants_reduced_to_numerical_subledgers_open`

显式零点自由区常数尚未自足闭合。当前只能诚实地把它压成四个数值子账本：C_log、零点排斥参数优化、PNT 轮廓积分常数、x=20000 目标预算。外部 Dusart 版仍可用，但完全自足版继续开放。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
explicit_zero_free_constants_reduced=true
explicit_zero_free_constants_self_contained_proved=false
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
ExplicitZeroFreeRegionConstantNumericalLedger
  =>
(ExplicitCLogHadamardStirlingJensenNumericalLedger AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger)
```

## 2. x=20000 目标压力

| item | value |
| --- | ---: |
| anchor_x | `20000` |
| log(anchor_x) | `9.903487552536` |
| sqrt(log(anchor_x)) | `3.146980704189` |
| target relative error | `0.000027578599007` |
| required a in C=1 exp(-a sqrt(log x)) | `3.336045394347` |
| required a in C=10 exp(-a sqrt(log x)) | `4.067726109748` |

这说明低锚点要求极强：普通渐近零点自由区常数不能自动给出 `x=20000` 的 theta 误差，必须配合低高度核验和有限桥。

## 3. 来源审查

| item | value |
| --- | --- |
| external_dusart_theta_registered | `true` |
| explicit_C_log_numeric_ledger_present | `false` |
| zero_free_c_T0_numeric_ledger_present | `false` |
| pnt_contour_numeric_ledger_present | `false` |
| finite_low_height_hash_present | `false` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExplicitZeroFreeConstantsGateActive | `true` | `false` | 上一层唯一内部最窄点是把符号零点排斥常数数值化。 | ExplicitZeroFreeRegionConstantNumericalLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入边界，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| SymbolicZeroRepulsionAvailable | `true` | `true` | 上一层已闭合存在性形式 beta<=1-c/log(\|gamma\|+3)。 | 还不能用于 x>=20000 数值预算。 |
| ExternalDusartThetaRegistered | `true` | `false` | 外部 Dusart theta 界已登记，可走外部路线；它不是自足常数账本。 | 外部路线已在 B3 主系数包中使用。 |
| ExplicitCLogNumericalLedgerMissing | `false` | `false` | 还缺 Hadamard/Stirling/Jensen 剩余项的 C_log 可复算数值上界。 | ExplicitCLogHadamardStirlingJensenNumericalLedger |
| ZeroRepulsionNumericalOptimizationMissing | `false` | `false` | 还缺由 C_log 推出 c、T0 和零点自由带的数值优化账本。 | ZeroRepulsionParameterNumericalOptimizationLedger |
| PNTContourNumericalLedgerMissing | `false` | `false` | 还缺从零点自由带经 Perron/显式公式轮廓积分推出 theta/psi 误差的常数账本。 | ZeroFreeRegionToExplicitPNTContourConstantLedger |
| ThetaEnvelopeTargetAt20000BudgetMissing | `false` | `false` | x=20000 要达到 1/36260 级相对误差，必须单独核算解析阈值和有限桥。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger |
| ExplicitZeroFreeConstantsReducedToNumericalSubledgers | `true` | `false` | 旧显式零点自由常数原子已压成 C_log、参数优化、PNT 轮廓、x=20000 目标预算四包。 | (ExplicitCLogHadamardStirlingJensenNumericalLedger AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) |
| FiniteLowHeightZeroCheckStillSeparate | `false` | `false` | 低高度零点排除仍是独立有限证书，不能并入高高度常数优化。 | FiniteLowHeightZeroCheckLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductClosed AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND (ExplicitCLogHadamardStirlingJensenNumericalLedger AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

唯一内部最窄点更新为 `ExplicitCLogHadamardStirlingJensenNumericalLedger`；随后是 `ZeroRepulsionParameterNumericalOptimizationLedger`、`ZeroFreeRegionToExplicitPNTContourConstantLedger`、`ThetaEnvelopeTargetAt20000NumericalBudgetLedger`。
