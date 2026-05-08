# Prime Matrix B=3 xi 整函数与一阶增长闭合证书

**状态：** `xi_entire_order_one_growth_closed`

xi 的整函数性与一阶以内增长已由 theta-Mellin 对称积分公式闭合。这让 zeta-xi 基础包只剩 Hadamard 分解和对数导数部分分式。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
xi_entire_order_one_growth_closed=true
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
XiEntireOrderOneGrowthLedger
  =>
XiEntireOrderOneGrowthClosed
```

## 2. 文内证明

由上一层对称公式

```text
Lambda(s)=1/(s(s-1))+1/2 int_1^infty theta_0(t)(t^(s/2-1)+t^((1-s)/2-1))dt.
```

定义

```text
xi(s)=1/2*s*(s-1)*Lambda(s).
```

`1/(s(s-1))` 的两个显式极点被 `s(s-1)` 消去；积分项因 `theta_0(t)` 在 `[1,infty)` 指数衰减而对 `s` 整。故 `xi` 是整函数。

若 `|s|<=r`，则积分被

```text
int_1^infty exp(-pi*t) * (t^(r/2)+t^((r+1)/2)) dt
```

控制。Gamma/Stirling 粗界给该量 `<=exp(C*r*log(r+3))`，乘上二次多项式因子不改变阶。因此

```text
max_{|s|<=r}|xi(s)| <= exp(C*r*log(r+3))
rho(xi)<=1
```

这足以进入一阶整函数的 Hadamard 分解层。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| XiEntireOrderGateActive | `true` | `false` | 上一层唯一内部最窄点是 xi 的整函数性与一阶增长账本。 | XiEntireOrderOneGrowthLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍是解析基础，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ThetaMellinFunctionalEquationAvailable | `true` | `true` | 上一层已闭合 Lambda(s) 的对称积分公式与函数方程。 | ThetaMellinZetaContinuationFunctionalEquationClosed |
| XiEntireCancellationClosed | `true` | `true` | xi(s)=1/2*s*(s-1)*Lambda(s) 消去 Lambda 在 s=0,1 的显式极点，积分项整。 | 无剩余。 |
| XiOrderAtMostOneGrowthClosed | `true` | `true` | 对 \|s\|=r，用 theta_0(t)<<exp(-pi t) 控制积分为 exp(O(r log(r+3)))，故 xi 阶至多一。 | 无剩余。 |
| XiEntireOrderOneGrowthLedger | `true` | `true` | 待证 atom 已闭合为 xi 整函数与一阶以内增长。 | XiEntireOrderOneGrowthClosed |
| HadamardFactorizationStillNext | `false` | `false` | 下一步用一阶整函数的 Hadamard 分解得到 xi'/xi 的零点部分分式。 | HadamardFactorizationLogDerivativeLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeLedger) AND EulerProductLogDerivativePositiveRealPartLedger AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityLedger AND ExplicitZeroFreeRegionConstantNumericalLedger AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `HadamardFactorizationLogDerivativeLedger`。
