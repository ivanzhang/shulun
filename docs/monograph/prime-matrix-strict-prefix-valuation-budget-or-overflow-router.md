# Prime Matrix strict prefix valuation 预算或溢出回流路由器

**状态：** `prefix_valuation_pass_or_overflow_return_closed_overflow_exclusion_open`

`PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn` 已闭合为严格 pass-or-return：对每个已登记 cold prefix，计算 `E_p(U)=sum_g v_p(g)` 与 `B_p=max_c v_p(m_c)`。若所有 `E_p(U)<=B_p`，则 `D(U)|h0^car`；若某个素数超载，立即输出 `CarrierLCMValuationOverflowNamedReturn`，并接入素数幂级联、共同核、固定历史/PDEC、SAE 或热核心出口。因此 valuation 超载不再是无名第四出口；但这些命名出口尚未被排斥，所以不能声明所有 cold prefix 都整除 `h0^car`，行/列命题仍未无条件闭合。

```text
pass_or_overflow_classifier_executable_closed=true
overflow_named_exit_map_closed=true
prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved=true
carrier_lcm_valuation_overflow_named_return_ledger_closed=true
cold_prefix_product_divides_carrier_lcm_h0_ledger_proved=false
row_column_unconditional_closed=false
```

## 1. 路由规则

| step | rule | effect |
| --- | --- | --- |
| compute_carrier_budget | B_p=max_c v_p(m_c)=v_p(h0^car) | 给出 carrier-lcm 对每个素数 p 的最大可用指数。 |
| compute_prefix_usage | E_p(U)=sum_{g in U} v_p(g)=v_p(D(U)) | 把前缀消耗压成逐素数 token 用量。 |
| budget_pass | if E_p(U)<=B_p for every p, then D(U)\|h0^car | 该 prefix 可以继续留在 carrier-lcm 商分支。 |
| overflow_return | if some E_p(U)>B_p, emit CarrierLCMValuationOverflowNamedReturn | 该 prefix 不能留在 primitive carrier-lcm 分支，必须进入命名回流。 |
| named_exit_map | overflow is prime-power cascade / low common-kernel / fixed-history-PDEC / SAE / hot-core | 溢出不是第四类无名逃逸；最终排斥仍依赖命名出口验收。 |

## 2. 样本账本

- path: `data/prefix-valuation-budget-or-overflow-sample-ledger.json`
- sha256: `8fa1cf0441f0675618bad08dc74595cf829583ac816b8ac8a9f3122fe281d91b`

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrefixValuationBudgetTargetImported` | `true` | `true` | 上一层已把 cold prefix 整除问题压成 valuation 预算或溢出回流。 | PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn |
| `CarrierLCMValuationCriterionImported` | `true` | `true` | 已导入 D(U)\|h0^car 等价于逐素数预算不超载。 | criterion imported |
| `PassOrOverflowClassifierExecutableClosed` | `true` | `true` | 给定 carrier quotients 与 prefix steps，分类器必输出预算通过或 valuation 溢出包。 | CarrierLCMValuationOverflowNamedReturnLedger |
| `OverflowNamedExitMapClosed` | `true` | `true` | valuation 溢出已映射到素数幂级联、共同核、固定历史/PDEC、SAE 或热核心。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturnProved` | `true` | `true` | 每个已登记 prefix 产品要么满足 carrier-lcm 预算，要么被命名为 valuation overflow return。 | CarrierLCMValuationOverflowReturnExclusionOrAbsorption |
| `CarrierLCMValuationOverflowNamedReturnLedgerClosed` | `true` | `true` | 溢出包的命名、payload 与既有回流出口对接闭合；但未排斥这些出口。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ColdPrefixProductDividesCarrierLCMH0LedgerProved` | `false` | `false` | 存在 overflow return 分支尚未排斥，不能声明所有 cold prefix 都整除 h0^car。 | CarrierLCMValuationOverflowReturnExclusionOrAbsorption |
| `PrefixResidualFrequencyEqualsCarrierLCMQuotientProved` | `false` | `false` | 只有预算通过的 prefix 可立刻得到 h0^car/D(U) 整数残频；溢出分支仍需排斥或吸收。 | ColdPrefixProductDividesCarrierLCMH0Ledger OR CarrierLCMValuationOverflowReturnExclusionOrAbsorption |
| `H0CarrierQuotientCompatibilityWithColdPrefixesProved` | `false` | `false` | pass-or-return 已闭合，但命名 overflow 分支未全局排斥。 | CarrierLCMValuationOverflowReturnExclusionOrAbsorption AND PrefixResidualFrequencyEqualsCarrierLCMQuotient |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | CarrierLCMValuationOverflowReturnExclusionOrAbsorption AND UnifiedTerminalBudgetStrictInequality AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`CarrierLCMValuationOverflowReturnExclusionOrAbsorption`。
- 具体任务：排斥或吸收 valuation overflow return；否则只能得到条件分支闭合。
- 并行守门：`NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion`、`UnifiedTerminalBudgetStrictInequality`、`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prefix-valuation-budget-or-overflow-sample-ledger.json` | `8fa1cf0441f0675618bad08dc74595cf829583ac816b8ac8a9f3122fe281d91b` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.json` | `03ac0c2625c0b49599ca004afb2d9df95656ffb4494505278ae7ec7b7212b8fc` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json` | `4c85ccfac092bb1ef772079cbf6adaa4c1f64f7b485b8d3ed2a71e2ea67422f9` |
| `experiments/prime_matrix_strict_prefix_valuation_budget_or_overflow_router.py` | `dbc7f6ef0036dd3346da0d50868819b33b4b69d9b82c966c790263e1b329774c` |
