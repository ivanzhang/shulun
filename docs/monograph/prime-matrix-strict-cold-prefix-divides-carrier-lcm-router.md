# Prime Matrix strict cold prefix 整除 carrier-lcm-h0 路由器

## 结论

`ColdPrefixProductDividesCarrierLCMH0Ledger` 已压到精确 valuation 判据：`D(U)|h0^car` 当且仅当每个素数 p 上，prefix steps 的累计指数 `sum_g v_p(g)` 不超过载体商中的最大指数 `max_c v_p(m_c)`。这关闭了整除判定的代数部分，但没有证明所有 cold prefix 满足该预算；若超载，必须进入共同核/固定历史/PDEC/SAE/ColumnCRT 回流。最新最窄点为 `PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn`。

```text
status=carrier_lcm_divisibility_criterion_closed_prefix_valuation_budget_open
hardpoint_before=ColdPrefixProductDividesCarrierLCMH0Ledger
hardpoint_after=PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn AND CarrierLCMValuationOverflowNamedReturnLedger
next_direct_attack_target=PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn
carrier_lcm_valuation_criterion_closed=true
cold_prefix_product_divides_carrier_lcm_h0_ledger_proved=false
row_column_unconditional_closed=false
```

## Valuation 判据

| 名称 | 公式 | 状态 |
|---|---|---|
| `carrier_lcm_valuation` | v_p(h0^car)=max_c v_p(m_c) | `closed` |
| `prefix_product_valuation` | v_p(D(U))=sum_{step g in U} v_p(g) | `closed` |
| `divisibility_criterion` | D(U)\|h0^car iff for all p, sum_g v_p(g)<=max_c v_p(m_c) | `closed` |
| `overflow_interpretation` | if inequality fails for some p, U cannot stay in carrier-lcm primitive branch | `closed_as_return_condition` |

## 剩余阻断

| 阻断 | 含义 | 下一步 |
|---|---|---|
| `step_origin_not_registered` | 每个 prefix step g 必须指向 carrier rows；否则无法比较其 p-adic 用量。 | `ColdPrefixStepQuotientOriginMapToCarrierRows` |
| `repeated_prime_power_overflow` | 即使每个 g 单独除某个 m_c，多个步骤的同素数指数和仍可能超过 lcm 最大指数。 | `PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn` |
| `overflow_return_not_closed` | 若指数超预算，必须登记共同核、固定历史、PDEC/SAE 或 ColumnCRT 回流。 | `CarrierLCMValuationOverflowNamedReturnLedger` |

## 判定表

| Gate | Closed | Proved | Meaning | Remaining |
|---|---:|---:|---|---|
| `ColdPrefixDivisibilityTargetImported` | `true` | `true` | 上一层已把最窄点压成 cold prefix 产品是否除 carrier-lcm h0。 | `ColdPrefixProductDividesCarrierLCMH0Ledger` |
| `CarrierLCMValuationCriterionClosed` | `true` | `true` | D(U)\|h0^car 等价于逐素数 valuation 预算不超载。 | `criterion closed` |
| `ColdPrefixStepQuotientOriginMapToCarrierRowsProved` | `false` | `false` | 尚未为每个 prefix step g 登记其来自哪些 carrier quotient rows。 | `ColdPrefixStepQuotientOriginMapToCarrierRows` |
| `PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturnProved` | `false` | `false` | 尚未证明所有 cold prefix 满足 valuation 预算，或超载必回流。 | `PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn` |
| `CarrierLCMValuationOverflowNamedReturnLedgerClosed` | `false` | `false` | 指数超载后的共同核/固定历史/PDEC/SAE/ColumnCRT 回流包未闭合。 | `CarrierLCMValuationOverflowNamedReturnLedger` |
| `ColdPrefixProductDividesCarrierLCMH0LedgerProved` | `false` | `false` | 整除判据已闭合，但 step origin、valuation 预算和溢出回流未证。 | `ColdPrefixStepQuotientOriginMapToCarrierRows AND PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn AND CarrierLCMValuationOverflowNamedReturnLedger` |
| `PrefixResidualFrequencyEqualsCarrierLCMQuotientProved` | `false` | `false` | 整除未证，因此不能声明 H_U=h0^car/D(U) 是实际整数残频。 | `PrefixResidualFrequencyEqualsCarrierLCMQuotient` |
| `H0CarrierQuotientCompatibilityWithColdPrefixesProved` | `false` | `false` | cold prefix 整除未证，h0 商兼容仍未闭合。 | `H0CarrierQuotientCompatibilityWithColdPrefixes` |
| `CanonicalH0FromEarlyZeroRowFactorizationIdentityProved` | `false` | `false` | h0 商兼容未闭合，规范 h0 恒等式仍未闭合。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |
| `ActualProductDivisorDomainH0EmitterForFormalUnitProved` | `false` | `false` | 规范 h0 恒等式未闭合，h0 发射器仍未闭合。 | `ActualProductDivisorDomainH0EmitterForFormalUnit` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 依赖哈希

| 文件 | SHA256 |
|---|---|
| `experiments/prime_matrix_strict_cold_prefix_divides_carrier_lcm_router.py` | `c03755e351db898ba054ef2af3b02a21777974f588dc80733c55bed852faab15` |
| `docs/monograph/prime-matrix-strict-h0-carrier-quotient-compat-router.json` | `26b2488927106156a4b3faae60929abb7fd184e8cc8dba5644df7c62f7b9892a` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-product-fiber-multiplicity-router.json` | `207253ea5e911247addc82f0e59edfdf1d034a6591d762a9928b493792500d4a` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
