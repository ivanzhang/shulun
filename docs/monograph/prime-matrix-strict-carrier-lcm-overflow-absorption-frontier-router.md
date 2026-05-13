# Prime Matrix strict carrier-lcm overflow 吸收前沿路由器

**状态：** `carrier_lcm_overflow_reduced_to_origin_budget_persistent_terminal_open`

`CarrierLCMValuationOverflowReturnExclusionOrAbsorption` 已被压缩：overflow 原子只有两种非循环形态。若单个 step 的 p-adic 指数已超过 `h0^car` 预算，那是 `ColdPrefixStepQuotientOriginMapToCarrierRows` 来源域缺陷；若每步局部可容纳但多步累计超载，那是重复 p-token，必须进入已命名的素数幂级联/共同核/固定历史/PDEC/SAE/热核心出口。因此 carrier-lcm overflow 不再是独立无名硬点。真正剩余为：step 来源域映射、非持久稀疏历史预算反超，以及持久终端族排斥。

```text
overflow_atom_split_closed=true
carrier_lcm_overflow_independent_hardpoint_removed=true
carrier_lcm_valuation_overflow_return_exclusion_or_absorption_proved=false
cold_prefix_step_quotient_origin_map_to_carrier_rows_proved=false
sparse_history_demand_exceeds_nonpersistent_supply_budget_proved=false
persistent_terminal_family_excluded=false
row_column_unconditional_closed=false
```

## 1. Overflow 原子拆分

| atom | trigger | route | meaning |
| --- | --- | --- | --- |
| single_step_domain_overflow | some step g has v_p(g)>B_p | ColdPrefixStepQuotientOriginMapToCarrierRows | 该 step 本身不属于 carrier-lcm 商域，必须证明来源映射或登记来源域缺陷。 |
| repeated_token_overflow | each step fits locally, but sum_step v_p(g)>B_p | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion | 多步重复消耗同一 p-token；进入素数幂级联/共同核/固定历史/PDEC/SAE/热核心。 |
| nonpersistent_named_overflow | overflow key does not persist beyond finite threshold | UnifiedTerminalBudgetStrictInequality | 非持久回流不是独立出口，必须由同参数 U_cold/稀疏历史预算吸收。 |
| persistent_named_overflow | same overflow key persists beyond threshold | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore | 持久复现进入固定历史、PDEC/CleanKLS 或 moving-atom 终端族。 |

## 2. 样本账本

- path: `data/carrier-lcm-overflow-atom-sample-ledger.json`
- sha256: `30a6e3c15e01a97428441f57e61f0f84a5da15c6064443c818ef43a8989e63da`

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CarrierLCMOverflowTargetImported` | `true` | `true` | 上一层已把剩余压成 valuation overflow return 的排斥或吸收。 | CarrierLCMValuationOverflowReturnExclusionOrAbsorption |
| `OverflowAtomSplitClosed` | `true` | `true` | overflow 原子只能是单步来源域缺陷或多步重复 token 命名回流。 | ColdPrefixStepQuotientOriginMapToCarrierRows OR NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `NamedReturnAlphabetCompressionImported` | `true` | `true` | 命名回流字母表已压成非持久预算吸收与持久终端族排斥。 | UnifiedTerminalBudgetStrictInequality AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `CarrierLCMOverflowIndependentHardpointRemoved` | `true` | `true` | carrier-lcm overflow 不再是独立未命名硬点；它归入来源域、统一预算或持久终端族。 | ColdPrefixStepQuotientOriginMapToCarrierRows AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `CarrierLCMValuationOverflowReturnExclusionOrAbsorptionProved` | `false` | `false` | 虽然独立硬点已压缩，但 step 来源域、非持久预算反超和持久终端族排斥仍未完成。 | ColdPrefixStepQuotientOriginMapToCarrierRows AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `ColdPrefixProductDividesCarrierLCMH0LedgerProved` | `false` | `false` | overflow 分支尚未全部排斥或吸收，仍不能声明所有 prefix product 整除 carrier-lcm h0。 | CarrierLCMValuationOverflowReturnExclusionOrAbsorption |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | ColdPrefixStepQuotientOriginMapToCarrierRows AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`ColdPrefixStepQuotientOriginMapToCarrierRows`。
- 同步硬点：`SparseHistoryDemandExceedsNonpersistentSupplyBudget` 与 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。
- 边界：本步删除 overflow 独立黑箱，不排斥所有 overflow 分支。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/carrier-lcm-overflow-atom-sample-ledger.json` | `30a6e3c15e01a97428441f57e61f0f84a5da15c6064443c818ef43a8989e63da` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json` | `5f08b5eed000355b69e5a8cc52eb4e0c2de4a8589c7f60b696f780a6101f9325` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.json` | `17ebb6fdd134cb1ec15518763ec426a0509da1f7432254a4fa16e02dbefb1dc0` |
| `experiments/prime_matrix_strict_carrier_lcm_overflow_absorption_frontier_router.py` | `f9537d5afc6ccd894e3ff103988097403278d3572b720d0b7f18f750e0871198` |
