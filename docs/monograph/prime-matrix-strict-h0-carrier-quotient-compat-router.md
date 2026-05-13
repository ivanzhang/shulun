# Prime Matrix strict h0 载体商兼容路由器

## 结论

`H0CarrierQuotientCompatibilityWithColdPrefixes` 已推进到一个非后验候选公式：令 `h0^car` 为早期零行载体中全部商 `m_c` 的 lcm。这个公式由 witness 先验确定，因此关闭了 h0 后验扩大纪律。但还没有证明每个 cold prefix 的产品 `D(U)` 都除 `h0^car`，也没有把符号 `H_U=h0/D(U)` 替换成实际整数 `h0^car/D(U)`。最新最窄点为 `ColdPrefixProductDividesCarrierLCMH0Ledger`。

```text
status=carrier_lcm_h0_formula_closed_cold_prefix_divisibility_open
hardpoint_before=H0CarrierQuotientCompatibilityWithColdPrefixes
hardpoint_after=ColdPrefixProductDividesCarrierLCMH0Ledger AND PrefixResidualFrequencyEqualsCarrierLCMQuotient
next_direct_attack_target=ColdPrefixProductDividesCarrierLCMH0Ledger
carrier_quotient_lcm_h0_formula_closed=true
h0_carrier_quotient_compatibility_with_cold_prefixes_proved=false
row_column_unconditional_closed=false
```

## 公式与纪律

| 名称 | 公式 | 状态 |
|---|---|---|
| `carrier_rows` | C(w)={(c,N_c,q_c,m_c): q_c=min prime<=P dividing N_c, m_c=N_c/q_c} | `imported_closed` |
| `carrier_lcm_h0` | h0^car(w)=lcm_c m_c | `closed_definition` |
| `h0_hash` | H(source_tuple_hash,'carrier_lcm_h0',sorted carrier row hashes) | `closed_definition` |
| `no_posthoc_rule` | h0 is computed before cold prefix enumeration; failures route, not enlarge h0 | `closed_discipline` |
| `cold_prefix_compatibility` | for every cold prefix U with product D(U), require D(U)\|h0^car | `open` |

## 剩余阻断

| 阻断 | 含义 | 下一步 |
|---|---|---|
| `prefix_product_not_yet_tied_to_quotients` | 载体给出每列 m_c；但 cold prefix product D(U) 是否由这些 m_c 的因子组成尚未证明。 | `ColdPrefixProductDividesCarrierLCMH0Ledger` |
| `prefix_tree_may_use_downstream_grouping` | 若 U 的定义读取 cold/Rankin 后验分组，就不能直接保证 D(U)\|h0^car。 | `ColdPrefixProductDividesCarrierLCMH0Ledger` |
| `symbolic_HU_needs_actual_substitution` | 已有 H_U=h0/D(U) 接口必须替换为 h0^car/D(U)，并证明整数性。 | `PrefixResidualFrequencyEqualsCarrierLCMQuotient` |

## 判定表

| Gate | Closed | Proved | Meaning | Remaining |
|---|---:|---:|---|---|
| `H0CarrierQuotientCompatibilityTargetImported` | `true` | `true` | 上一层已把最窄点压成 h0 载体与 cold prefix 商化兼容。 | `H0CarrierQuotientCompatibilityWithColdPrefixes` |
| `CarrierQuotientLCMH0FormulaClosed` | `true` | `true` | 用逐列商 m_c 的 lcm 定义非后验候选 h0^car。 | `CarrierQuotientLCMH0Formula` |
| `H0NoPostHocEnvelopeDisciplineClosed` | `true` | `true` | h0^car 在 cold prefix 枚举前由 carrier 固定；失败不能扩大 h0，只能回流。 | `H0NoPostHocEnvelopeDiscipline` |
| `ColdPrefixProductDividesCarrierLCMH0LedgerProved` | `false` | `false` | 尚未证明每个 cold prefix product D(U) 都除 h0^car。 | `ColdPrefixProductDividesCarrierLCMH0Ledger` |
| `PrefixResidualFrequencyEqualsCarrierLCMQuotientProved` | `false` | `false` | 尚未把下游符号 H_U=h0/D(U) 替换为实际整数 h0^car/D(U)。 | `PrefixResidualFrequencyEqualsCarrierLCMQuotient` |
| `H0CarrierQuotientCompatibilityWithColdPrefixesProved` | `false` | `false` | h0 公式和无后验纪律已推进，但 cold prefix 整除兼容未证。 | `ColdPrefixProductDividesCarrierLCMH0Ledger AND PrefixResidualFrequencyEqualsCarrierLCMQuotient` |
| `CanonicalH0FromEarlyZeroRowFactorizationIdentityProved` | `false` | `false` | 商兼容未闭合，规范 h0 恒等式仍未闭合。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |
| `ActualProductDivisorDomainH0EmitterForFormalUnitProved` | `false` | `false` | 规范 h0 恒等式未闭合，h0 发射器仍未闭合。 | `ActualProductDivisorDomainH0EmitterForFormalUnit` |
| `ActualColdProductBlockParameterLedgerPresent` | `false` | `false` | h0 发射器未闭合，实际产品块参数账本仍不存在。 | `ActualColdProductBlockParameterLedgerForP018Table` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `ColdPrefixProductDividesCarrierLCMH0Ledger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 依赖哈希

| 文件 | SHA256 |
|---|---|
| `experiments/prime_matrix_strict_h0_carrier_quotient_compat_router.py` | `c104dfc6ea39ca2439cbeda5511c41ece6fc8fb2f768aa30aa4b50b1ef47b990` |
| `docs/monograph/prime-matrix-strict-early-zero-factorization-carrier-router.json` | `a55db8bd6be9a6a2582addf4c7f32cd8c6281e0d3da8f6f1d1593601733220a4` |
| `docs/monograph/prime-matrix-strict-canonical-h0-factorization-identity-router.json` | `8e717bb4bf1923093e3ab8485360bcaeb8265a6367f24842e410127bdcbc1e85` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-product-fiber-multiplicity-router.json` | `207253ea5e911247addc82f0e59edfdf1d034a6591d762a9928b493792500d4a` |
| `docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.json` | `664b98a29a37db7ba354f28adf9d20842bfdac7505c8803fd5cd2d9038b06175` |
