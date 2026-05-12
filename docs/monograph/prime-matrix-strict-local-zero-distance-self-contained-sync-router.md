# Prime Matrix strict 局部零点倒距离自足同步路由器

**状态：** `psi0_local_zero_distance_self_contained_closed_weighted_budget_open`

`Psi0HorizontalLocalZeroDistanceSumConstantLedger` 已可从外部条件版同步为 strict 自足版：共同包络提供 fixed-T 缩进纪律，RVM-CN16 同步提供 C_N=16，Hadamard/Gamma/余项提供内部 log-derivative 展开；因此 eta=1/16 给出 C_N/eta=256，再加结构余项 32，得到 C=288。该步不关闭加权水平积分预算，也不关闭行/列无条件命题。

```text
psi0_horizontal_local_zero_distance_self_contained_closed=true
psi0_horizontal_weighted_integral_budget_self_contained_closed=false
unsmoothed_perron_strict_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
C_total_logder=288.000000000000
```

## 1. 自足替换

```text
Psi0HorizontalLocalZeroDistanceSumConstantLedger
  => Psi0HorizontalLocalZeroDistanceSumSelfContainedClosedC288Eta1Over16
```

## 2. 常数表

| item | value | formula | meaning |
| --- | ---: | --- | --- |
| eta | `0.062500000000` | 1/16 | 共同缩进纪律之后，剩余水平段离目标零点的登记最小距离。 |
| C_N | `16.000000000000` | RVMToCN16LocalInequalitySelfContainedClosedWithRawArgCS8CommonEnvelope | 自足同步后的单位高度局部零点数常数。 |
| local distance coefficient | `256.000000000000` | C_N/eta | 近零点倒距离总贡献的粗上界系数。 |
| structural remainder reserve | `32.000000000000` | HadamardGammaRemainder reserve | log-derivative 展开中非局部主部的结构余项预留。 |
| total pointwise coefficient | `288.000000000000` | 256 + 32 | 水平边点态界的最终系数。 |

## 3. 样例上界

| T | log(T+3) | pointwise bound |
| ---: | ---: | ---: |
| 14.000000000000 | 2.833213344056 | 815.965443088190 |
| 45.000000000000 | 3.871201010908 | 1114.905891141473 |
| 100.000000000000 | 4.634728988230 | 1334.801948610135 |
| 1000.000000000000 | 6.910750787962 | 1990.296226933038 |
| 20000.000000000000 | 9.903637541287 | 2852.247611890729 |
| 1000000.000000000000 | 13.815513557960 | 3978.867904692415 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理早期零行假设链条中的解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `LocalZeroDistanceAtomActive` | `true` | `true` | log-derivative 展开闭合后，strict Perron 的下一原子正是局部倒距离和。 | Psi0HorizontalLocalZeroDistanceSumConstantLedger |
| `FixedTIndentDisciplineSelfContained` | `true` | `true` | 共同高高度包络已把 fixed-T 缩进原子调和为作者侧可用的内部闭合输入。 | ClassicalBacklundZeroIndentationCostInternalProofClosedByHighPowerCommonEnvelope |
| `RVMCN16SelfContainedAvailable` | `true` | `true` | RVM 原始 arg 归一化、CS8 边界桥和低高度 xi 子包已同步为 C_N=16。 | RVMToCN16LocalInequalitySelfContainedClosedWithRawArgCS8CommonEnvelope |
| `LogDerivativeExpansionSelfContainedAvailable` | `true` | `true` | Hadamard 对数导数、Gamma/digamma 和余项账本已给出内部结构展开。 | ClassicalZetaLogDerivativeAwayFromZerosInternalExpansionClosedByHadamardGammaRemainder |
| `ExternalFormulaReusedOnlyAsArithmeticCheck` | `true` | `true` | 旧外部证书只复用 eta=1/16、C_N/eta+32=288 的算术模板，不复用外部假设。 | Psi0HorizontalLocalZeroDistanceSumClosedC288Eta1Over16 |
| `EtaOneOver16C288BudgetClosed` | `true` | `true` | 在缩进后的水平段，每个近零点贡献至多 1/eta；16/(1/16)+32=288。 | Psi0HorizontalLocalZeroDistanceSumSelfContainedClosedC288Eta1Over16 |
| `Psi0LocalZeroDistanceSelfContainedClosed` | `true` | `true` | 三项内部输入全部到位后，局部零点倒距离和从外部条件版升级为 strict 自足版。 | Psi0HorizontalLocalZeroDistanceSumSelfContainedClosedC288Eta1Over16 |
| `UnsmoothedPerronStrictSelfContainedClosed` | `false` | `false` | 本步只关闭点态倒距离常数；水平加权积分预算仍未 strict 自足同步。 | Psi0HorizontalWeightedIntegralBudgetLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只是解析输入自足化，不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
Psi0HorizontalWeightedIntegralBudgetLedger
```

也就是把点态 C=288 水平边界乘上 Perron 权重并压入 C=12000 的加权预算。
