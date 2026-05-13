# Prime Matrix strict 共同核回流循环下降/PDEC 路由器

**状态：** `common_kernel_free_return_cycle_excluded_named_exits_open`

`CommonKernelReturnCycleDescentOrPDECLedger` 可以关闭为“无免费回流循环”。若共同核分支落在固定商型，已有 `h -> h/(bc)` 且 `bc>=2` 的严格高度下降；若不固定但有限历史/商型/重叠键反复出现，则由持久阈值登记为固定历史、ColumnCRT 或 PDEC；若所有键都不持久，则每次回流都消耗有限字母表 SAE/冷供给预算；兄弟整族超收费则转入热核心或固定历史。因此低乘子共同核不能形成不下降、不收费、也不命名的循环。但这只关闭免费循环，不排斥 PDEC/SAE/热核心/固定历史出口，也不证明统一终端预算严格余量，所以行/列命题仍未无条件闭合。

```text
return_cycle_target_imported=true
fixed_quotient_height_descent_closed=true
persistent_finite_type_pdec_route_closed=true
nonpersistent_finite_debit_closed=true
sibling_hot_fixed_return_registered=true
free_common_kernel_return_cycle_excluded=true
common_kernel_return_cycle_descent_or_pdec_proved=true
unified_terminal_budget_strict_inequality_proved=false
named_return_exclusion_proved=false
low_multiplier_common_kernel_excluded=false
row_column_unconditional_closed=false
```

## 1. 回流出口

| exit | trigger | effect |
| --- | --- | --- |
| fixed quotient descent | persistent pair quotient (b,c) with bc>=2 | frequency height h is replaced by h/(bc), so a same-level cycle is impossible |
| persistent finite type | same history word, quotient type, sibling overlap key, or kernel key repeats above threshold | the branch is registered as FixedHistory/ColumnCRT/PDEC |
| nonpersistent finite debit | no finite type reaches its persistence threshold | each return consumes a bounded SAE/history-token allowance already present in the nonpersistent budget |
| hot family return | sibling family charge exceeds the cold support envelope | the branch is no longer cold; it routes to hot core, fixed history, PDEC, or SAE |

## 2. 有限 token 样本

| alphabet size | threshold | max nonpersistent returns | first forced persistent return | pigeonhole ok |
| --- | --- | --- | --- | --- |
| `6` | `3` | `12` | `13` | `true` |
| `10` | `4` | `30` | `31` | `true` |
| `14` | `5` | `56` | `57` | `true` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ReturnCycleTargetImported` | `true` | `true` | 上一层已把低乘子共同核的真正剩余压成回流下降/PDEC 账本。 | CommonKernelReturnCycleDescentOrPDECLedger |
| `FixedQuotientHeightDescentClosed` | `true` | `true` | 固定商型分支已有 h -> h/(bc), bc>=2 的严格高度下降。 | FixedQuotientTypePDECColumnCertificateExclusion |
| `PersistentFiniteTypePDECRouteClosed` | `true` | `false` | 同一有限历史/商型/重叠键持久复现时已登记为 PDEC/ColumnCRT，但排斥未完成。 | FixedTypeHistoryPDECExclusion OR FixedQuotientTypePDECColumnCertificateExclusion |
| `NonpersistentFiniteDebitClosed` | `true` | `true` | 若没有持久复现，则回流次数由有限字母表乘持久阈值控制，并进入 SAE/冷供给预算。 | BoundedQuotientTypeSAEAbsorption AND SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `SiblingHotFixedReturnRegistered` | `true` | `true` | 兄弟整族超冷预算或重复收费不能继续留在冷分支。 | TerminalCoreHotDivisorWindowPDECorSAE OR FixedTypeHistoryPDECExclusion |
| `FreeCommonKernelReturnCycleExcluded` | `true` | `true` | 共同核回流不能无限免费循环；必为高度下降、有限预算扣减、热回流或 PDEC。 | UnifiedTerminalBudgetStrictInequality OR NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `CommonKernelReturnCycleDescentOrPDECProved` | `true` | `true` | 目标账本闭合为无免费循环；但命名出口和预算严格余量仍开。 | UnifiedTerminalBudgetStrictInequality AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `LowMultiplierCommonKernelExcluded` | `false` | `false` | 共同核免费循环已排除，但 PDEC/SAE/热核心/固定历史出口尚未全部排斥。 | UnifiedTerminalBudgetStrictInequality AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND FixedQuotientTypePDECColumnCertificateExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | UnifiedTerminalBudgetStrictInequality AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`UnifiedTerminalBudgetStrictInequality`。
- 含义：免费循环已经排除，剩余必须在同参数终端预算中证明需求严格大于非持久供给与命名回流扣除。
- 并行：固定商型 PDEC、固定历史、热核心和 DStructure/Rankin 仍是独立验收门。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-density-transfer-router.json` | `f2b0c000ddb05b2504eb547a318d94a219fd70ac27ff34089b01524caa1688f7` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-type-columncrt-router.json` | `2604e2de93bc17bbe7678dddccf958b8a747714286d2c1ab8d5734246be78733` |
| `docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json` | `10d6c849cdb719344db932e7cfbf6f7f94ba66f26b28f0f3bb5f73d5d5df778d` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json` | `973a1c986598cb27dd132354715b336eae7938103c89d09da451123f2ade08de` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json` | `4ec39bb552f9cc5f120b20ae937e8569370f7aa75322dda2d4ee669b2897985b` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-history-router.json` | `6cbb750d3888d20ef1c7267231ddfb8490b1efc92b0edda308ec96f1d40905b2` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-history-sae-budget-router.json` | `8f077e91bd0f02d25e6598256b5ebe958579e779abe1ecc41dd6861207e09523` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.json` | `17ebb6fdd134cb1ec15518763ec426a0509da1f7432254a4fa16e02dbefb1dc0` |
| `experiments/prime_matrix_strict_common_kernel_return_cycle_descent_router.py` | `1dc77715550bac629d735adbb7e5fa967d12cad3e1631430285dac3be675c063` |
