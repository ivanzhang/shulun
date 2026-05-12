# Prime Matrix strict Dusart 解析核与阈值拼接路由器

**状态：** `dusart_analytic_kernel_threshold_arithmetic_splice_closed_inputs_open`

Dusart P5.1 的解析核与阈值已经被压成严格拼接结构：高尾 `x>=e^28` 只需 `eps_psi(28)<=0.00002224`；中间带 `8e11<=x<=e^28` 由 `0.00002841-0.9999e^-14<1/36260` 接上；而 `x<8e11` 需要 theta 有限表。本步关闭拼接算术，但不关闭 psi 误差表、psi-theta 下界、8e11 有限表和低高度证书。

```text
dusart_analytic_kernel_threshold_arithmetic_splice_closed=true
analytic_kernel_and_threshold_closed=false
direct_internal_dusart_theta_pnt_envelope_closed=false
middle_range_finite_verification_closed=false
finite_low_height_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 外部边界

- 外部来源：`arXiv:1002.0442`
- 链接：https://arxiv.org/abs/1002.0442
- 角色：source boundary for the Dusart Proposition 5.1 proof structure only

## 2. 拼接算术

| check | formula | value | margin |
| --- | --- | ---: | ---: |
| target relative error | `1/36260` | `2.757859900717043574e-5` | `baseline` |
| high tail x>=e^28 | `0.00002224 < 1/36260` | `2.224000000000000000e-5` | `5.338599007170435742e-6` |
| middle strip 8e11<=x<=e^28 | `0.00002841 - 0.9999 e^-14 < 1/36260` | `2.757855443376834247e-5` | `4.457340209326913989e-11` |
| threshold ordering | `8e11 < e^28` | `8.000000000000000000e+11 < 1.446257064291475174e+12` | `6.462570642914751737e+11` |
| current finite bridge reach | `20000 < 8e11` | `2.000000000000000000e+4 < 8.000000000000000000e+11` | `7.999999800000000000e+11` |

## 3. 自足替换

```text
DusartThetaAnalyticKernelAndThresholdLedger
  =>
DusartP51ArithmeticSpliceClosed AND PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger AND PsiMinusThetaLowerGap09999SqrtSelfContainedLedger AND ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger

DusartThetaMiddleRangeFiniteVerificationLedger
  =>
ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger AND PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger AND PsiMinusThetaLowerGap09999SqrtSelfContainedLedger

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只压缩假设反例链所需解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `DusartAnalyticKernelGateActive` | `true` | `true` | 上一证书把下一最窄点设为 Dusart theta/PNT 的解析核与阈值。 | DusartThetaAnalyticKernelAndThresholdLedger |
| `DusartP51ArithmeticSpliceClosed` | `true` | `true` | Dusart P5.1 的高尾和中间带数值拼接余量为正；中间带余量很薄但严格为正。 | 只关闭拼接算术，不关闭输入表和外部定理证明。 |
| `HighTailThresholdArithmeticClosed` | `true` | `true` | 若有 psi 相对误差 eps_28<=0.00002224，则 x>=e^28 自动给 theta(x)-x<x/36260。 | PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger |
| `MiddleStripArithmeticClosed` | `true` | `true` | 若有 psi 上界 0.00002841 与 psi-theta>0.9999 sqrt(x)，则 8e11<=x<=e^28 接上。 | PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger AND PsiMinusThetaLowerGap09999SqrtSelfContainedLedger |
| `ExistingFiniteThetaBridgeTooShortForDusartP51` | `true` | `true` | 仓库已自足关闭 x<=20000 的 theta 桥，但 Dusart P5.1 的有限表接口要求 theta(x)<x 到 8e11。 | ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `PsiContourCoarseComponentsReadyButNotSharpEnough` | `true` | `true` | Perron 常数、高高度零点和、平凡尾项已自足化；它们还没有给出 Dusart 表级 psi 误差。 | PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger |
| `DusartThetaAnalyticKernelAndThresholdLedger` | `false` | `false` | 解析核与阈值尚未闭合：关键 psi 误差表、psi-theta 下界、8e11 有限 theta 表仍需作者侧证明或可复现证书。 | PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger AND PsiMinusThetaLowerGap09999SqrtSelfContainedLedger AND ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `MiddleRangeFiniteVerificationStillOpen` | `false` | `false` | 原来的 20000<x<X_A 中段现在被精确压成 20000<x<8e11 的 theta 有限表和 8e11<=x<=e^28 的解析拼接。 | ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger AND PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger AND PsiMinusThetaLowerGap09999SqrtSelfContainedLedger |
| `LowHeightAuditStillOpen` | `false` | `false` | psi 误差表若走零点路线，仍要低高度 Turing/无零证书支撑。 | CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger |
| `DirectInternalDusartThetaPNTEnvelopeClosed` | `false` | `false` | 本步闭合的是拼接结构，不是完整内部 Dusart 定理。 | DusartThetaAnalyticKernelAndThresholdLedger AND DusartThetaMiddleRangeFiniteVerificationLedger AND CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 解析拼接压缩不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger
```
