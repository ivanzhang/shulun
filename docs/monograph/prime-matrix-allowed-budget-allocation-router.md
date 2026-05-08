# Prime Matrix allowed_budget 分配纪律路由器

**状态：** `allowed_budget_allocation_discipline_closed_batch_rankin_open`

AllowedBudgetAllocationLedger 已闭合为预算纪律：每个颜色类预算必须预登记，总预算受主链允许预算约束；Rankin 通过才闭合，失败必须显式登记为 low-mod core CRTDefect/PDEC-SAE 或 constant-gap。新的最窄点是提交全量批量 Rankin 证书：`BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
allowed_budget_allocation_discipline_closed=true
formal_colored_corridor_inventory_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
AllowedBudgetAllocationLedger => AllowedBudgetAllocationDisciplineClosed AND BatchRankinCertificatesAllPassOrReturnToPDECSAE.
```

## 2. 预算纪律

| rule | meaning |
| --- | --- |
| predeclared_budget | 每个 color_id 的 B_allow 必须随 source tuple/inventory 一起登记，先于 Rankin 审计。 |
| sum_budget_guard | 多颜色预算必须满足 sum_c B_c 不超过该 source tuple 的主链允许预算。 |
| single_color_acceptance | 若存在 s 使 R_s(C_c;K)<=B_c，则该颜色类核心计数被 RLA-1 验收。 |
| failed_with_spike_return | Rankin 不通过且 residue spike 超阈值时，登记 low-mod core CRTDefect 并回流 PDEC/SAE。 |
| failed_without_spike_constant_gap | Rankin 不通过且无 spike 时，只能登记 constant-gap，继续细分或调参，不能标为通过。 |
| no_posthoc_reallocation | 看到 Rankin ledger 后不得把其他颜色类未用预算后验转给失败类，除非重新提交全局预算证书。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AllowedBudgetGateActive | `true` | `false` | 上一层已把最窄点推进到 allowed_budget 分配纪律。 | AllowedBudgetAllocationLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条内的预算证书，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| ColoringCoverageImported | `true` | `true` | 同色不相交走廊对象已由上一层固定。 | 预算只能分配给这些固定颜色类。 |
| FormalBudgetFieldsPinned | `true` | `true` | 正式 inventory 已要求 allowed_budget 与 failure_return。 | 字段格式无剩余。 |
| RankinAcceptanceTheoremImported | `true` | `true` | RLA-1/RLA-2 给出单颜色和多颜色预算验收不等式。 | 无预算验收逻辑剩余。 |
| FailureRoutingImported | `true` | `true` | 预算失败只能进入 low-mod core CRTDefect/PDEC-SAE 或 constant-gap，不可口头吸收。 | PDECOrSAEUnifiedExclusionLedger or constant-gap |
| AllowedBudgetAllocationDisciplineClosed | `true` | `true` | allowed_budget 分配纪律已闭合：预算预登记、总预算守卫、失败回流三者固定。 | AllowedBudgetAllocationDisciplineClosed |
| AllowedBudgetAllocationLedger | `true` | `true` | 预算分配层闭合为验收纪律；下一步必须提交全量 Rankin 批量证书或失败回流。 | BatchRankinCertificatesAllPassOrReturnToPDECSAE |
| BatchRankinStillDownstream | `false` | `false` | 每个正式颜色类的 concrete Rankin 证书和失败回流列表尚未全集提交。 | BatchRankinCertificatesAllPassOrReturnToPDECSAE |

## 4. 下一步

当前唯一最窄点更新为 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

审稿边界：本步不提交全量 Rankin 证书，不关闭 PDEC/SAE，也不关闭行列无条件定理。
