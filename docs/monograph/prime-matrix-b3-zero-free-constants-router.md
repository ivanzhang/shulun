# Prime Matrix B=3 零点自由区常数账本路由器

**状态：** `zero_free_constants_reduced_to_named_zeta_package_open`

本步把唯一内部原子压成了可审稿的 zeta 解析包：函数方程/Hadamard、Euler product 对数导数正性、de la Vallee Poussin 三角核、零点排斥不等式、显式常数和低高度零点核验。当前只闭合了三角核纯代数层；真正的自足零点自由区常数证明仍未闭合，不能升级为行命题无条件证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
zero_free_constants_reduced=true
zero_free_constants_self_contained_proved=false
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger
  =>
(CompletedZetaXiFunctionalEquationAndHadamardProductLedger AND EulerProductLogDerivativePositiveRealPartLedger AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityLedger AND ExplicitZeroFreeRegionConstantNumericalLedger AND FiniteLowHeightZeroCheckLedger)
```

这说明当前硬点已经不是方阵覆盖几何本身，而是把显式 PNT 的解析机器完全内联。

## 2. x=20000 常数压力

| item | value |
| --- | ---: |
| anchor_x | `20000` |
| log(anchor_x) | `9.903487552536` |
| sqrt(log(anchor_x)) | `3.146980704189` |
| target relative theta error | `0.000027578599007` |
| required a for C exp(-a sqrt(log x)) at C=1 | `3.336045394347` |
| required a for C exp(-a sqrt(log x)) at C=10 | `4.067726109748` |
| x needed if a=1,C=1 | `7.362379e+47` |
| x needed if a=2,C=1 | `9.263061e+11` |

结论：`x=20000` 对普通 `C exp(-a sqrt(log x))` 型 PNT 误差极苛刻；若不引用 Dusart/Rosser-Schoenfeld，就必须给出显式零点自由区常数加低高度零点核验，或把解析阈值推高后再用有限桥下推。

## 3. 来源审查

| item | value |
| --- | --- |
| smooth_explicit_formula_present | `true` |
| xi_functional_equation_hadamard_present | `false` |
| euler_product_log_derivative_positive_kernel_present | `false` |
| de_la_vallee_poussin_zero_free_argument_present | `false` |
| explicit_zero_free_constant_ledger_present | `false` |
| finite_low_height_zero_check_present | `false` |
| external_dusart_mertens_route_registered | `true` |

## 4. 三角核审查

```text
3+4*cos(t)+cos(2t)=2*(1+cos(t))^2>=0
sample_count=2048
max_sample_error=8.882e-16
min_sample_value=0.000e+00
```

三角核非负性只关闭 de la Vallee Poussin 方法的代数核，不关闭零点自由区定理本身。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ZeroFreeConstantsGateActive | `true` | `false` | 上一层唯一内部最窄点是自足 de la Vallee Poussin 零点自由区常数账本。 | SelfContainedDeLaValleePoussinZeroFreeRegionConstantsLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条中补解析输入，不用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| SmoothExplicitFormulaStillOnlyStartingPoint | `true` | `true` | 平滑显式公式提供 -zeta'/zeta 的入口，但不包含零点自由区常数。 | 不能替代零点自由区证明。 |
| XiFunctionalEquationHadamardMissing | `false` | `false` | 仓库内没有完整 zeta 延拓、函数方程、xi Hadamard 乘积的常数化账本。 | CompletedZetaXiFunctionalEquationAndHadamardProductLedger |
| EulerProductLogDerivativePositiveKernelMissing | `false` | `false` | 需要把 sigma>1 的 Euler product 对数导数正性接入零点排斥不等式。 | EulerProductLogDerivativePositiveRealPartLedger |
| TrigonometricKernelIdentityClosed | `true` | `true` | de la Vallee Poussin 核 3+4cos(t)+cos(2t)=2(1+cos(t))^2>=0 是纯代数闭合。 | DeLaValleePoussinTrigonometricKernelIdentityClosed |
| ZeroRepulsionInequalityMissing | `false` | `false` | 还缺从三角核、Euler product 正性和 Hadamard/函数方程推出零点排斥的完整不等式。 | DeLaValleePoussinZeroRepulsionInequalityLedger |
| ExplicitZeroFreeConstantNumericalLedgerMissing | `false` | `false` | 还缺把排斥不等式常数化为可用于 x>=20000 theta 包络的显式常数账本。 | ExplicitZeroFreeRegionConstantNumericalLedger |
| FiniteLowHeightZeroCheckMissing | `false` | `false` | 任何低阈值显式界都需要低高度零点排除或有限验证证书；仓库尚无 hash 账本。 | FiniteLowHeightZeroCheckLedger |
| ZeroFreeConstantsReducedToNamedZetaPackage | `true` | `false` | 旧零点自由区常数原子被拆成 zeta 基础、Euler 正性、三角核、排斥不等式、显式常数、低高度核验。 | (CompletedZetaXiFunctionalEquationAndHadamardProductLedger AND EulerProductLogDerivativePositiveRealPartLedger AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityLedger AND ExplicitZeroFreeRegionConstantNumericalLedger AND FiniteLowHeightZeroCheckLedger) |
| ContourThetaEnvelopeStillDownstream | `false` | `false` | 即便零点自由区常数账本完成，还必须把它经 Perron/显式公式轮廓积分转成 theta/psi 包络。 | ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion |
| FiniteThetaBridgeStillDownstream | `false` | `false` | 轮廓积分阈值通常高于 20000 时，需要有限桥把阈值下推到 B3 锚点。 | FiniteThetaEnvelopeBridgeBelowAnalyticThreshold |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | 外部 Dusart/Mertens 版虽然已越过 B3 主系数包，但最终仍需 DStructure/Rankin 独立验收。 | DStructureRankinPromotionPackage。 |

## 6. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND (CompletedZetaXiFunctionalEquationAndHadamardProductLedger AND EulerProductLogDerivativePositiveRealPartLedger AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityLedger AND ExplicitZeroFreeRegionConstantNumericalLedger AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 下一步

唯一内部最窄点更新为 `CompletedZetaXiFunctionalEquationAndHadamardProductLedger`；随后是 `EulerProductLogDerivativePositiveRealPartLedger`、`DeLaValleePoussinZeroRepulsionInequalityLedger`、`ExplicitZeroFreeRegionConstantNumericalLedger` 与 `FiniteLowHeightZeroCheckLedger`。
这些全部完成后，才进入下游 `ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion`、`FiniteThetaEnvelopeBridgeBelowAnalyticThreshold` 和 `SelfContainedMeisselMertensConstantIntervalLedgerAt20000`。
