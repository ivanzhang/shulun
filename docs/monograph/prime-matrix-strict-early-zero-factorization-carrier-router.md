# Prime Matrix strict 早期零行因式分解载体路由器

## 结论

`EarlyZeroRowFactorizationCarrierLedger` 可以在假设反例链内闭合：早期零行保证每列 `N_c` 有某个 `q<=P` 素因子，取最小这样的 `q_c`，并定义 `m_c=N_c/q_c`，即可得到同 formal unit、无选择的逐列因式/商载体。但这个载体还不是单一 `h0`；仍需证明 carrier 产生的 `h0` 与所有 cold prefix 的 `H_U=h0/D(U)` 商化兼容，并排除后验扩大 `h0`。

```text
status=early_zero_factorization_carrier_closed_h0_quotient_compat_open
hardpoint_before=EarlyZeroRowFactorizationCarrierLedger
hardpoint_after=H0CarrierQuotientCompatibilityWithColdPrefixes AND H0NoPostHocEnvelopeDiscipline
next_direct_attack_target=H0CarrierQuotientCompatibilityWithColdPrefixes
early_zero_row_factorization_carrier_ledger_present=true
row_column_unconditional_closed=false
```

## 载体字段

| 字段 | 定义 | 状态 |
|---|---|---|
| `witness_id` | H(P,row_index,r/source_tuple_hash) | `closed_schema` |
| `column` | 1<=c<P within the assumed early zero row | `closed_schema` |
| `N_c` | row value, e.g. xP+c under the fixed row convention | `closed_schema` |
| `q_c` | least prime q<=P dividing N_c | `closed_by_early_zero_assumption` |
| `m_c` | N_c/q_c | `closed_by_divisibility` |
| `carrier_row_hash` | H(witness_id,column,N_c,q_c,m_c) | `closed_schema` |

## 证明步骤

| 步骤 | 论证 | 状态 |
|---|---|---|
| `existence` | 早期零行假设说明每个列值 N_c 都被某个 P 以内素数覆盖。 | `closed_under_counterexample_assumption` |
| `canonical_selector` | 取满足 q\|N_c 且 q<=P 的最小素数，消除多因子选择歧义。 | `closed` |
| `quotient_row` | 定义 m_c=N_c/q_c；这是整数且由同一列唯一确定。 | `closed` |
| `hash_stability` | carrier_row_hash 继承 source_tuple_hash/formal_unit hash，不后验读取 Rankin 或 cold 产品块。 | `closed` |
| `h0_not_yet_defined` | 载体 C(w) 是逐列因式/商表；单一 h0=F(C(w)) 仍需额外公式。 | `open_next` |

## 边界

| 边界 | 含义 | 剩余 |
|---|---|---|
| `carrier_not_h0` | C(w) 是逐列 q_c,m_c 表，不是单一产品除数域 h0。 | `H0CarrierQuotientCompatibilityWithColdPrefixes` |
| `least_factor_not_cold_product` | q_c 是覆盖素标签；cold 产品 d 可能是多步前缀乘子，需证明 d\|F(C(w))。 | `H0CarrierQuotientCompatibilityWithColdPrefixes` |
| `no_posthoc_h0` | 不能把所有下游失败 d 再并入 h0；失败必须回流。 | `H0NoPostHocEnvelopeDiscipline` |

## 判定表

| Gate | Closed | Proved | Meaning | Remaining |
|---|---:|---:|---|---|
| `CarrierTargetImported` | `true` | `true` | 上一层已把 h0 源恒等式首缺口压成早期零行因式分解载体账本。 | `EarlyZeroRowFactorizationCarrierLedger` |
| `EarlyZeroAssumptionGivesPerColumnSmallPrime` | `true` | `true` | 在假设反例链内，每列 N_c 都有 P 以内素因子。 | `counterexample assumption` |
| `LeastSmallPrimeSelectorCanonical` | `true` | `true` | 选择最小 q_c 消除多覆盖素因子歧义。 | `selector closed` |
| `CarrierRowHashSchemaClosed` | `true` | `true` | carrier row 继承 formal unit/source tuple hash。 | `hash closed` |
| `EarlyZeroRowFactorizationCarrierLedgerPresent` | `true` | `true` | 逐列 (N_c,q_c,m_c) 载体账本可由假设早期零行 witness 规范生成。 | `EarlyZeroRowFactorizationCarrierLedger` |
| `H0CarrierQuotientCompatibilityWithColdPrefixesProved` | `false` | `false` | 尚未证明该载体产生的单一 h0 与所有 cold prefix 商化兼容。 | `H0CarrierQuotientCompatibilityWithColdPrefixes` |
| `H0NoPostHocEnvelopeDisciplineClosed` | `false` | `false` | 尚未证明后验扩大 h0 的所有情形都回流。 | `H0NoPostHocEnvelopeDiscipline` |
| `CanonicalH0FromEarlyZeroRowFactorizationIdentityProved` | `false` | `false` | 载体账本闭合，但 h0 公式、商兼容和无后验选择未闭合。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |
| `ActualProductDivisorDomainH0EmitterForFormalUnitProved` | `false` | `false` | 规范 h0 恒等式未闭合，h0 发射器仍未闭合。 | `ActualProductDivisorDomainH0EmitterForFormalUnit` |
| `ActualColdProductBlockParameterLedgerPresent` | `false` | `false` | h0 发射器未闭合，实际产品块参数账本仍不存在。 | `ActualColdProductBlockParameterLedgerForP018Table` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到反例链与真实结构链的终端矛盾。 | `H0CarrierQuotientCompatibilityWithColdPrefixes AND H0NoPostHocEnvelopeDiscipline AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 依赖哈希

| 文件 | SHA256 |
|---|---|
| `experiments/prime_matrix_strict_early_zero_factorization_carrier_router.py` | `bd5b287a6264625e5bb729e557162a12bc182d28e3037d67b3010ffb1c7a1dff` |
| `docs/monograph/prime-matrix-strict-canonical-h0-factorization-identity-router.json` | `8e717bb4bf1923093e3ab8485360bcaeb8265a6367f24842e410127bdcbc1e85` |
| `docs/monograph/prime-matrix-formal-unit-source-record-router.json` | `fe51a3ea8f7d8a71e3f667b43fda4229c11324772afb8c321a06c4d5fab36a2f` |
| `docs/monograph/prime-matrix-canonical-formal-unit-hash-stability-router.json` | `359c78f1c0629e514eb584acdb81ed489d36a0ba111a37a5c40eee03e59e3af6` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
