# Prime Matrix strict 水平边加权积分预算自足同步路由器

**状态：** `psi0_horizontal_weighted_budget_self_contained_closed_perron_sync_open`

`Psi0HorizontalWeightedIntegralBudgetLedger` 已可从外部条件版同步为 strict 自足版：输入点态界已由 strict 局部倒距离证书给出 C=288，直段 `2eC` 与凹口 `4*pi*eC` 的总成本低于 12000。该步关闭水平边 log-derivative 包，但仍需单独同步 Perron 压缩账本；行/列无条件命题保持未闭合。

```text
psi0_horizontal_weighted_integral_budget_self_contained_closed=true
psi0_horizontal_logder_self_contained_package_closed=true
unsmoothed_perron_strict_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
C_weighted_budget=12000.000000000000
```

## 1. 自足替换

```text
Psi0HorizontalWeightedIntegralBudgetLedger
  => Psi0HorizontalWeightedIntegralBudgetSelfContainedClosedC12000

Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosLedger
  => Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosSelfContainedClosedC12000

```

## 2. 预算分解

| component | coefficient | formula | meaning |
| --- | ---: | --- | --- |
| straight horizontal segments | `1565.730333192410` | 2*e*C_logder | 两条水平直段由 \|s\|>=T、x^(1+1/log x)<=e*x 和积分长度控制。 |
| indentation arcs | `9837.773824519947` | 4*pi*e*C_logder | 凹口弧段由 eta=1/16、局部零点数和弧长预算控制。 |
| rounded reserve | `12000.000000000000` | ceil reserve above straight+arcs | 为端点、半权和 log(T+3)<=log(xT) 转换保留余量。 |

## 3. 压力诊断

| x | T | log(xT) | budget bound | relative to x |
| ---: | ---: | ---: | ---: | ---: |
| 20000.000000000000 | 14.000000000000 | 12.542544882151 | 2696835979.213404655457 | 134841.798960670247 |
| 20000.000000000000 | 45.000000000000 | 13.710150042306 | 1002497142.306962728500 | 50124.857115348139 |
| 20000.000000000000 | 1000.000000000000 | 16.811242831518 | 67828292.529665812850 | 3391.414626483291 |
| 20000.000000000000 | 20000.000000000000 | 19.806975105072 | 4707795.153755425476 | 235.389757687771 |
| 20000.000000000000 | 1000000.000000000000 | 23.718998110500 | 135021.809127821180 | 6.751090456391 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步继续只在假设反例链解析输入内同步，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `WeightedBudgetAtomActive` | `true` | `true` | strict 局部倒距离关闭后，Perron 自足压缩链唯一剩余解析原子就是水平加权预算。 | Psi0HorizontalWeightedIntegralBudgetLedger |
| `PointwiseC288SelfContainedAvailable` | `true` | `true` | 局部零点倒距离已自足给出 \|zeta'/zeta\| 的 C=288 log(T+3) 点态包。 | Psi0HorizontalLocalZeroDistanceSumSelfContainedClosedC288Eta1Over16 |
| `ExternalWeightedArithmeticTemplateChecked` | `true` | `true` | 旧外部证书只作为直段/凹口常数算术模板，不复用外部 Backlund/RVM 假设。 | Psi0HorizontalWeightedIntegralBudgetClosedC12000 |
| `StraightHorizontalWeightedBoundClosed` | `true` | `true` | 两条水平直段成本为 2e*C_logder，已包含于 C=12000 预算。 | 2*e*C_logder |
| `IndentArcWeightedBoundClosed` | `true` | `true` | 凹口弧段成本为 4*pi*e*C_logder，和直段合计低于 12000。 | 4*pi*e*C_logder |
| `WeightedBudgetC12000SelfContainedClosed` | `true` | `true` | 点态 C=288 与权重积分估计合成后，水平边加权积分预算自足关闭。 | Psi0HorizontalWeightedIntegralBudgetSelfContainedClosedC12000 |
| `HorizontalLogDerivativeSelfContainedPackageClosed` | `true` | `true` | 局部倒距离和加权预算都自足关闭后，水平边 log-derivative 包自足关闭。 | Psi0HorizontalZetaLogDerivativeBoundAwayFromZerosSelfContainedClosedC12000 |
| `UnsmoothedPerronStrictSelfContainedClosed` | `false` | `false` | 本步关闭最后的水平预算原子；仍需单独同步 Perron 压缩账本，避免隐式越级。 | UnsmoothedChebyshevPerronExplicitFormulaConstantLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只是解析输入自足化，不产生全局反例矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
UnsmoothedPerronStrictSelfContainedFinalSync
```
