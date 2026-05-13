# Prime Matrix strict cold prefix step 来源图路由器

**状态：** `cold_prefix_step_token_origin_map_closed_global_source_defect_open`

`ColdPrefixStepQuotientOriginMapToCarrierRows` 的正确最弱形式不是要求每个 step `g` 整体除某个 `m_c`，而是要求 `g` 的每个素数幂 token `p^e` 都能映射到某个满足 `v_p(m_c)>=e` 的 carrier row。本步关闭了这个 token 来源图判据，并把单步超出 carrier-lcm 本地域的情形登记为 source-defect return。因此 step 来源图本身不再是代数障碍；剩余是把 source-defect return 与累计 valuation pass 同步，形成 no-return 分支上的 `D(U)|h0^car`，并最终排斥或吸收所有回流。

```text
strong_single_carrier_row_requirement_rejected=true
canonical_token_origin_map_criterion_closed=true
cold_prefix_step_quotient_origin_map_to_carrier_rows_proved_for_local_steps=true
cold_prefix_step_quotient_origin_map_to_carrier_rows_global_proved=false
step_local_carrier_domain_defect_return_closed=true
no_return_cold_prefix_product_divides_carrier_lcm_h0_proved=false
row_column_unconditional_closed=false
```

## 1. 来源图命题

| name | statement | status |
| --- | --- | --- |
| token_origin_not_single_row_origin | g\|h0^car only requires each p^e\|\|g to be supported by some carrier row; g need not divide one m_c. | closed |
| canonical_token_selector | For p^e in g, choose the least column c with v_p(m_c)>=e. | closed |
| local_domain_equivalence | A token origin map exists iff v_p(g)<=max_c v_p(m_c) for every p\|g. | closed |
| source_defect_return | If no token origin map exists, g is outside the carrier-lcm local domain and must return. | closed_as_return_condition |

## 2. 样本账本

- path: `data/cold-prefix-step-origin-map-sample-ledger.json`
- sha256: `f838112f8687acbea59236f934d367b09674a9f05bd1eb9b01e943116876111f`

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StepOriginTargetImported` | `true` | `true` | 上一层已把单步来源域缺陷压到 cold prefix step 来源图。 | ColdPrefixStepQuotientOriginMapToCarrierRows |
| `StrongSingleCarrierRowRequirementRejected` | `true` | `true` | step g 不必整体除某个 m_c；逐素数 token 来源图才是正确最弱对象。 | single-row shortcut rejected |
| `CanonicalTokenOriginMapCriterionClosed` | `true` | `true` | 局部可容纳 step 的每个 p^e token 都有确定性 carrier row 来源。 | token map closed |
| `StepLocalCarrierDomainDefectReturnClosed` | `true` | `true` | 若某个 p^e 无 carrier row 支撑，则该 step 不能留在 carrier-lcm 分支，必须回流。 | ColdPrefixStepLocalCarrierDomainGuardOrSourceDefectReturn |
| `ColdPrefixStepQuotientOriginMapToCarrierRowsProvedForLocalSteps` | `true` | `true` | 对所有局部 carrier-admissible step，来源图已闭合。 | ColdPrefixStepQuotientOriginMapToCarrierRows |
| `ColdPrefixStepQuotientOriginMapToCarrierRowsGlobalProved` | `false` | `false` | 全局仍需证明实际 cold prefix 不触发 source-defect，或该 defect 被预算/终端族吸收。 | ColdPrefixStepLocalCarrierDomainGuardOrSourceDefectReturn AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `NoReturnColdPrefixProductDividesCarrierLCMH0Proved` | `false` | `false` | 还需把 step local guard 与累计 valuation pass 同步成完整 no-return 分支定理。 | NoReturnColdPrefixProductDividesCarrierLCMH0 |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | ColdPrefixStepLocalCarrierDomainGuardOrSourceDefectReturn AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`NoReturnColdPrefixProductDividesCarrierLCMH0`。
- 并行守门：`ColdPrefixStepLocalCarrierDomainGuardOrSourceDefectReturn`、`SparseHistoryDemandExceedsNonpersistentSupplyBudget`、`IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。
- 边界：本步闭合 token 来源图判据，不声明全部实际 prefix 已整除 carrier-lcm h0。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/cold-prefix-step-origin-map-sample-ledger.json` | `f838112f8687acbea59236f934d367b09674a9f05bd1eb9b01e943116876111f` |
| `docs/monograph/prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json` | `b387c085456d139d10212a0bb3e70744205f8f6084853cccf1cc7e176bea9a13` |
| `docs/monograph/prime-matrix-strict-early-zero-factorization-carrier-router.json` | `a55db8bd6be9a6a2582addf4c7f32cd8c6281e0d3da8f6f1d1593601733220a4` |
| `docs/monograph/prime-matrix-strict-h0-carrier-quotient-compat-router.json` | `26b2488927106156a4b3faae60929abb7fd184e8cc8dba5644df7c62f7b9892a` |
| `docs/monograph/prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json` | `5f08b5eed000355b69e5a8cc52eb4e0c2de4a8589c7f60b696f780a6101f9325` |
| `experiments/prime_matrix_strict_cold_prefix_step_origin_map_router.py` | `8b3d10e364ece889f073c37fad3da06c0a441742f0e8fc89f31052d918620027` |
