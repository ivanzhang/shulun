# Prime Matrix B=3 Euler product 对数导数正性闭合证书

**状态：** `euler_product_log_derivative_positive_kernel_closed`

Euler product 对数导数正性已闭合。该层只给 sigma>1 处的正核不等式；它本身还不是零点自由区，下一步必须同 Hadamard 零点部分分式合并，证明 de la Vallee Poussin 零点排斥。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
euler_product_log_derivative_positive_real_part_closed=true
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
EulerProductLogDerivativePositiveRealPartLedger
  =>
EulerProductLogDerivativePositiveRealPartClosed
```

## 2. 文内证明

当 `sigma>1` 时，Euler product 绝对收敛，逐项取对数导数得到

```text
F(s)=-zeta'/zeta(s)=sum_{n>=1} Lambda(n)n^(-s), Re s>1
```

对任意实数 `u`，

```text
3+4*cos(u)+cos(2u)=2*(1+cos(u))^2>=0
```

令 `u=t log n`，逐项乘以非负权 `Lambda(n)n^{-sigma}` 并求和，得到

```text
3F(sigma)+4 Re F(sigma+i t)+Re F(sigma+2 i t)>=0, sigma>1
```

这正是 de la Vallee Poussin 零点排斥步骤需要的 Euler 正性输入。

## 3. 有限截断审计

| sigma | t | finite positive sum | min kernel seen |
| ---: | ---: | ---: | ---: |
| 1.2 | 0 | `2.514703149377e+01` | `8.000000000000e+00` |
| 1.2 | 0.1 | `2.371054207715e+01` | `6.372515161598e+00` |
| 1.2 | 0.7 | `7.155531722647e+00` | `2.109423746788e-14` |
| 1.2 | 1.3 | `8.201877780602e+00` | `1.751498780456e-07` |
| 1.2 | 2 | `8.221302623032e+00` | `4.048138363411e-07` |
| 1.2 | 3.5 | `8.272466699757e+00` | `1.313704700578e-11` |

有限截断样本最小正和：`7.155531722647e+00`。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EulerProductPositiveKernelGateActive | `true` | `false` | 上一层唯一内部最窄点是 Euler product 对数导数正性。 | EulerProductLogDerivativePositiveRealPartLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只补假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| HadamardInputAvailable | `true` | `true` | 上一层已给出 xi'/xi 的零点部分分式，供下一排斥层使用。 | HadamardFactorizationLogDerivativeClosed |
| TrigKernelIdentityAvailable | `true` | `true` | 三角核 3+4cos u+cos 2u=2(1+cos u)^2>=0 已在零点自由区常数路由中闭合。 | DeLaValleePoussinTrigonometricKernelIdentityClosed |
| EulerProductLogDerivativeSeriesClosed | `true` | `true` | 对 sigma>1，Euler product 给 -zeta'/zeta(s)=sum Lambda(n)n^{-s}，绝对收敛。 | 无剩余。 |
| PositiveRealPartKernelClosed | `true` | `true` | 逐项乘以正核并求和，得 3F(sigma)+4Re F(sigma+it)+Re F(sigma+2it)>=0。 | EulerProductLogDerivativePositiveRealPartClosed |
| EulerProductLogDerivativePositiveRealPartLedger | `true` | `true` | 待证 atom 已闭合为 Euler product 对数导数正性不等式。 | EulerProductLogDerivativePositiveRealPartClosed |
| ZeroRepulsionInequalityStillNext | `false` | `false` | 下一步要把 Hadamard 部分分式与 Euler 正性合并，推出 de la Vallee Poussin 零点排斥。 | DeLaValleePoussinZeroRepulsionInequalityLedger |
| ExplicitConstantsStillDownstream | `false` | `false` | 排斥不等式之后仍需显式常数账本与低高度零点核验。 | ExplicitZeroFreeRegionConstantNumericalLedger AND FiniteLowHeightZeroCheckLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityLedger AND ExplicitZeroFreeRegionConstantNumericalLedger AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

唯一内部最窄点更新为 `DeLaValleePoussinZeroRepulsionInequalityLedger`；随后是 `ExplicitZeroFreeRegionConstantNumericalLedger` 与 `FiniteLowHeightZeroCheckLedger`。
