# Prime Matrix strict 自足 Mertens 尾段当前前沿路由器

**状态：** `self_contained_mertens_tail_frontier_compressed_to_unsmoothed_perron_internal_zerosum_theta_bridge_b1_open`

自足 Mertens 尾段已经压到显式 PNT 机器的当前真实前沿：有限素数倒数跳点、分部求和接口、DVP 符号排斥、C=1280/T0=14 参数和初等尾项均可复用；剩余不再是零行几何，而是非平滑 Perron 常数、内部零点和预算、theta@20000/有限桥、以及 Meissel-Mertens B1 常数区间。外部 Dusart/Mertens 路线可条件推进到 DStructure/Rankin，但严格自足线仍未闭合。

```text
finite_prime_steps_to_20000_closed=true
partial_summation_interface_closed=true
dvp_symbolic_repulsion_closed=true
zero_repulsion_c1280_t14_registered=true
trivial_tail_prime_power_closed=true
external_mertens_theta_route_closed_to_dstructure=true
unsmoothed_perron_constant_proved=false
internal_zero_sum_budget_proved=false
theta_target_self_contained_proved=false
finite_theta_bridge_proved=false
meissel_mertens_b1_interval_proved=false
self_contained_mertens_tail_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿表

| name | status | meaning | remaining |
| --- | --- | --- | --- |
| `finite_prime_steps_to_20000` | `closed` | 286<=x<10372 与 10372<=x<20000 的素数倒数跳点作为精确 Stieltjes 原子保留。 | 无。 |
| `partial_summation_interface` | `closed` | 一旦有 theta/psi 包络和 B1 常数区间，素数倒数尾段由分部求和接口推出。 | 等待 theta/B1 输入。 |
| `dvp_symbolic_and_numeric_region` | `partly_closed` | DVP 符号零点排斥与 C=64 参数优化给出 beta<=1-1/(1280 log(\|gamma\|+3)), \|gamma\|>=14。 | FiniteLowHeightZeroCheckLedger AND UnsmoothedChebyshevPerronExplicitFormulaConstantLedger AND InternalZeroSumDyadicContourBudgetLedger |
| `trivial_tail_prime_power` | `closed` | 平凡零点、端点半权、素数幂和截断尾项已有初等归账。 | 不能替代 theta@20000 小误差。 |
| `theta_20000_and_finite_bridge` | `open_self_contained` | 普通 C=1280 零点自由区常数不能自动达到 Dusart 级 theta@20000 目标。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold |
| `meissel_mertens_b1_interval` | `open_self_contained` | B1 常数区间与 x=20000 基点核验仍需自足算术账本。 | SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `external_route` | `conditional_external_closed_to_dstructure` | 接受 Dusart theta/reciprocal-prime Mertens 外部定理后，B3 解析链推进到 DStructure/Rankin 守门项。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 该解析前沿只作为早期零行反例链的 B3/TV 输入，不使用真实缺席样本。 | 保持 row_column_unconditional_closed=false。 |
| `MertensTailFiniteAndFormalLayersClosed` | `true` | `true` | 有限跳点、分部求和接口、DVP 符号链、C=1280/T0=14 参数和初等尾项均已登记。 | UnsmoothedChebyshevPerronExplicitFormulaConstantLedger AND InternalZeroSumDyadicContourBudgetLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `UnsmoothedPerronStillOpen` | `false` | `false` | 平滑显式公式不能自动替代非平滑 Chebyshev/Perron 常数账本。 | UnsmoothedChebyshevPerronExplicitFormulaConstantLedger |
| `InternalZeroSumStillOpen` | `false` | `false` | 外部零点和预算可条件关闭；自足线仍需文内 dyadic 零点和预算。 | InternalZeroSumDyadicContourBudgetLedger |
| `ThetaAndBridgeStillOpen` | `false` | `false` | x=20000 的小 theta 误差和有限桥不能由普通零点自由区粗常数自动推出。 | ThetaEnvelopeTargetAt20000NumericalBudgetLedger AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold |
| `B1IntervalStillOpen` | `false` | `false` | Meissel-Mertens 常数区间自足算术仍未完成。 | SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `SelfContainedMertensTailProved` | `false` | `false` | 自足 reciprocal-prime Mertens 尾段仍未闭合。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |

## 3. 下一最窄点

```text
UnsmoothedChebyshevPerronExplicitFormulaConstantLedger
```

并行保留：

```text
InternalZeroSumDyadicContourBudgetLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger AND FiniteLowHeightZeroCheckLedger AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000
```

审稿边界：本步不证明自足 Mertens 尾段；只把其当前真实前沿压缩为可逐项攻击的解析账本。
