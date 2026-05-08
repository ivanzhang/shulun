# Prime Matrix 区间图着色覆盖证书路由器

**状态：** `interval_graph_coloring_coverage_closed_budget_open`

IntervalGraphColoringCoverageCertificateLedger 已闭合为确定性证书：固定 source tuple 后，anchor intervals 的低重叠部分按整数区间图贪心着色，颜色数不超过 Omega；每个颜色类内 intervals 两两不交，coverage_equation 记录有色多重集等于低重叠走廊多重集。新的最窄点是 `AllowedBudgetAllocationLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
interval_graph_coloring_coverage_closed=true
formal_colored_corridor_inventory_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
IntervalGraphColoringCoverageCertificateLedger => IntervalGraphColoringCoverageCertificateClosed AND AllowedBudgetAllocationLedger.
```

## 2. 证书字段

| field | meaning |
| --- | --- |
| source_tuple_hash | 锁定 P/range、window_id、A、D0、K、Omega、phase_rule。 |
| anchor_intervals | 每个 anchor a 的 J_a=[ceil(L/a),floor(R/a)] 与 [D0,2D0) 的交。 |
| low_overlap_filter | 只保留 m(d)<=Omega 的走廊部分；m(d)>Omega 已回流 high-overlap defect。 |
| coloring_algorithm | 按左端点扫描的贪心 interval coloring；活动区间颜色复用。 |
| color_count_bound | 最大同时活动区间数 <= Omega，因此 color_id in {1,...,Omega}。 |
| per_color_disjointness | 每个颜色类内 intervals 两两不交。 |
| coverage_equation | 有色 interval 多重集精确等于低重叠 anchor interval 多重集。 |
| failure_return | 若重叠界或覆盖等式失败，回流 high-overlap defect 或 source tuple 错配。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| IntervalColoringGateActive | `true` | `false` | 上一层已把最窄点推进到区间图着色和覆盖等式证书。 | IntervalGraphColoringCoverageCertificateLedger |
| ParameterTupleImported | `true` | `true` | A、D0、K、Omega 与 phase_rule 已由上一层固定。 | 不能重选参数。 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条内的 formal corridor 证书，不用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| FormalCoverageFieldsPinned | `true` | `true` | 正式 inventory 已要求 color_id、intervals 与 coverage_equation。 | 字段格式无剩余。 |
| IntervalGraphPerfectColoringImported | `true` | `true` | DCS 已证明最大重叠度 <= Omega 的整数区间族可用 Omega 色贪心着色。 | 无着色存在性剩余。 |
| PerColorRankinObjectReady | `true` | `true` | CCB 的 Rankin 账本对象正是同色不相交走廊并集。 | AllowedBudgetAllocationLedger |
| IntervalGraphColoringCoverageCertificateClosed | `true` | `true` | 着色和覆盖等式可由 source tuple 确定性复算；无额外数学出口。 | IntervalGraphColoringCoverageCertificateClosed |
| IntervalGraphColoringCoverageCertificateLedger | `true` | `true` | 区间图着色覆盖证书闭合；下一步只剩 allowed budget 分配纪律。 | AllowedBudgetAllocationLedger |
| AllowedBudgetStillDownstream | `false` | `false` | 每个颜色类的 allowed_budget 分配和 Rankin 批量验收尚未提交。 | AllowedBudgetAllocationLedger AND BatchRankinCertificatesAllPassOrReturnToPDECSAE |

## 4. 下一步

当前唯一最窄点更新为 `AllowedBudgetAllocationLedger`；随后是 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

审稿边界：本步不分配预算，不执行全量 Rankin 批量验收，也不关闭行列无条件定理。
