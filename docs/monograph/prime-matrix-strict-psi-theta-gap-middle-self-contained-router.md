# Prime Matrix strict P5.1 中段 psi-theta 下界自足证书

**状态：** `psi_theta_gap_09999_sqrt_closed_on_p51_middle_by_two_layer_finite_audit`

P5.1 中段所需的 `psi(x)-theta(x)>0.9999sqrt(x)` 已自足闭合。核心压缩是令 `y=sqrt(x)`，只用平方层和立方层即可：`psi(x)-theta(x)>=theta(y)+theta(y^(2/3))`。有限审计覆盖 `sqrt(8e11)<=y<=e^14` 的全部跳点，最坏 surplus 约为 8173，远大于 1000 的舍入保护。P5.1 当前剩余收窄为 `theta(x)<x` 到 `8e11` 的有限表/证书。

```text
psi_minus_theta_lower_gap_09999_sqrt_self_contained_closed=true
dusart_p51_full_theta_statement_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 有限审计

| field | value |
| --- | ---: |
| `x_lo` | `800000000000.0` |
| `x_hi` | `1446257064291.475` |
| `y_lo` | `894427.1909999158` |
| `y_hi` | `1202604.2841647768` |
| `prime_limit` | `1202615` |
| `prime_count` | `93118` |
| `breakpoint_count` | `22453` |
| `checked_intervals` | `22452` |
| `worst_surplus` | `8173.164500438841` |
| `worst_y_right` | `904482.9999999999` |
| `next_breakpoint` | `904483.0` |
| `theta_y` | `903321.2385184902` |
| `theta_y_2_over_3` | `9244.47768194844` |
| `required_0_9999_y` | `904392.5516999998` |
| `rounding_guard` | `1000.0` |
| `audit_hash` | `c74f50421cf92c134eb28ce80a7d8f257b6788967458b57d904ced1e764e9daf` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只补 P5.1 中段解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `PsiThetaGapGateActive` | `true` | `true` | 上一证书已把下一最窄点设为 P5.1 中段 psi-theta 下界。 | PsiMinusThetaLowerGap09999SqrtSelfContainedLedger |
| `TwoLayerPrimePowerLowerBoundIdentity` | `true` | `true` | 令 y=sqrt(x)，则 psi(x)-theta(x)>=theta(y)+theta(y^(2/3))。 | uses only prime-square and prime-cube layers |
| `MiddleYIntervalFiniteReduction` | `true` | `true` | P5.1 中段 8e11<=x<=e^28 等价于 y in [sqrt(8e11), e^14]，只需有限覆盖。 | finite breakpoint audit |
| `FiniteBreakpointAuditClosed` | `true` | `true` | 在 theta(y) 与 theta(y^(2/3)) 的所有跳点前检查最坏点，最小 surplus 仍大于 1000。 | c74f50421cf92c134eb28ce80a7d8f257b6788967458b57d904ced1e764e9daf |
| `PsiMinusThetaLowerGap09999SqrtSelfContainedLedger` | `true` | `true` | 对 P5.1 中段全体 x，psi(x)-theta(x)>0.9999sqrt(x) 已由两层素数幂有限审计自足闭合。 | closed on 8e11<=x<=e^28 |
| `P51PsiInputsRemainClosed` | `true` | `true` | 高尾 b=28 与中段 psi 上界输入保持闭合。 | psi input pair closed |
| `P51StillNeedsThetaFiniteTable` | `false` | `false` | P5.1 全段 theta 结论剩余主要非 psi 输入为 theta(x)<x 到 8e11 的有限表/证书。 | ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭的是 P5.1 中段 psi-theta 输入，不直接产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最窄点

```text
ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger
```

