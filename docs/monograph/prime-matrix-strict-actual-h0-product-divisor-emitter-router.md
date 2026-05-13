# Prime Matrix strict actual h0 产品除数域发射器路由器

## 结论

`ActualProductDivisorDomainH0EmitterForFormalUnit` 已被压到真正源头：必须新增并证明一个从早期零行 witness/同 formal unit 因式分解数据到单一整数 `h0` 的规范恒等式，同时证明所有 cold 产品支撑 `d` 都满足 `d|h0`，且不能后验扩大 `h0`。现有 source tuple 字段没有 `h0`，诊断样本和按候选反推 h0 都不能作为证明。下一最窄点为 `CanonicalH0FromEarlyZeroRowFactorizationIdentity`。

```text
status=h0_emitter_reduced_to_canonical_factorization_identity_coverage_nochoice
hardpoint_before=ActualProductDivisorDomainH0EmitterForFormalUnit
hardpoint_after=CanonicalH0FromEarlyZeroRowFactorizationIdentity AND H0DivisibilityCoverageNoChoiceLedger AND H0CanonicalHashAndNoPostHocChoiceDiscipline
next_direct_attack_target=CanonicalH0FromEarlyZeroRowFactorizationIdentity
actual_product_divisor_domain_h0_emitter_for_formal_unit_proved=false
row_column_unconditional_closed=false
```

## Source Tuple 字段审查

| 字段 | 是否已有 | h0 相关用途 | 缺口 |
|---|---:|---|---|
| `formal_unit_id/source_tuple_hash` | `yes` | row identity key | `does not define product divisor domain` |
| `P_or_P_range` | `yes` | budget scale | `does not determine divisors d\|h0` |
| `window_id,L,R` | `yes` | local window geometry | `window endpoints alone do not define multiplicative product carrier` |
| `A` | `yes` | anchor set | `no theorem says h0 is lcm/product of A or that every cold d divides it` |
| `D0,K,Omega` | `yes` | sieve/overlap parameters | `scale and overlap parameters are not a canonical integer h0` |
| `phase_rule` | `yes` | finite phase predicate | `phase predicate cannot be used as Euler product divisor domain` |
| `h0` | `no` | required product divisor domain | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |

## 禁止捷径

| 捷径 | 为什么无效 | 回到 |
|---|---|---|
| `diagnostic_h0_samples` | 样本中的 2310/4320/840 只验证投影和 Rankin 公式，未绑定任意 actual formal unit。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |
| `choose_h0_as_lcm_of_candidates` | 候选集合本身定义为 d\|h0；反过来用候选集合定义 h0 是循环。 | `H0CanonicalHashAndNoPostHocChoiceDiscipline` |
| `choose_h0_as_product_of_A` | 现有 source tuple 只给 anchor set A，没有证明所有 cold 产品 d 都来自 A 的除数格。 | `H0DivisibilityCoverageNoChoiceLedger` |
| `choose_h0_from_D0_K_Omega` | D0/K/Omega 是尺度和重叠参数，不是已证明的产品除数域。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |
| `posthoc_enlarge_h0_until_pass` | 会改变 Euler product 和 Rankin 预算，是后验选择，破坏同 formal unit 哈希纪律。 | `H0CanonicalHashAndNoPostHocChoiceDiscipline` |

## 发射器最小 schema

| 字段 | 定义 | 作用 |
|---|---|---|
| `input_witness` | early-zero witness / formal_unit source record | h0 必须来自假设反例链，而不是真实缺席或诊断样本。 |
| `factorization_identity` | canonical formula producing integer h0 from row factorization / quotient data | 给出产品除数域的非循环来源。 |
| `coverage_law` | every cold product support d in this formal unit satisfies d\|h0 | 让候选集合定义 `{d:d\|h0}` 合法。 |
| `minimality_or_no_choice_law` | same witness gives same h0; enlargements route to named return | 防止后验选择 h0 以调节 Rankin 权重。 |
| `h0_hash` | H(source_tuple_hash, factorization_identity_hash, h0) | 让下游 block 和 Rankin 表可复算。 |
| `failure_return` | if no such h0 exists, route to PDEC/SAE/ColumnCRT/fixed-history | h0 发射失败必须成为终端回流，而不是静默缺口。 |

## 判定表

| Gate | Closed | Proved | Meaning | Remaining |
|---|---:|---:|---|---|
| `H0EmitterTargetImported` | `true` | `true` | 上一层已把 actual 参数账本首要缺口压成 h0 产品除数域发射器。 | `ActualProductDivisorDomainH0EmitterForFormalUnit` |
| `UpstreamFormalUnitContainerReady` | `true` | `true` | source tuple、formal unit source record、hash、cold candidate rule 与 projection 均可作为输入。 | `input ready` |
| `SourceTupleContainsH0Field` | `true` | `false` | source tuple 字段审查显示 h0 不在当前 schema 中。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |
| `CanonicalH0FromEarlyZeroRowFactorizationIdentityProved` | `false` | `false` | 尚未给出从早期零行 witness/行因式分解到单一 h0 的非循环恒等式。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity` |
| `H0DivisibilityCoverageNoChoiceLedgerProved` | `false` | `false` | 尚未证明所有 cold 产品支撑 d 均除同一 h0，且 h0 不能后验扩大。 | `H0DivisibilityCoverageNoChoiceLedger` |
| `H0CanonicalHashAndNoPostHocChoiceDisciplineClosed` | `false` | `false` | 尚未建立 h0_hash 与后验选择排斥纪律。 | `H0CanonicalHashAndNoPostHocChoiceDiscipline` |
| `ActualProductDivisorDomainH0EmitterForFormalUnitProved` | `false` | `false` | 需要 h0 恒等式、覆盖律和无选择哈希纪律三者同时成立。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity AND H0DivisibilityCoverageNoChoiceLedger AND H0CanonicalHashAndNoPostHocChoiceDiscipline` |
| `ActualColdProductBlockParameterLedgerPresent` | `false` | `false` | h0 发射器未闭合，实际 cold 产品块参数账本仍不存在。 | `ActualColdProductBlockParameterLedgerForP018Table` |
| `PrimitiveProductRankinP018InequalityTablePresent` | `false` | `false` | 缺 h0 与实际产品块，P^0.18 表仍不能生成。 | `PrimitiveProductRankinP018InequalityTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `CanonicalH0FromEarlyZeroRowFactorizationIdentity AND PrimitiveProductRankinFailureReturnPacketLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 依赖哈希

| 文件 | SHA256 |
|---|---|
| `experiments/prime_matrix_strict_actual_h0_product_divisor_emitter_router.py` | `02bbcc53994b8b6b4fd264c5a0a89571b4be4e278b77e3041edd475e16bee3d3` |
| `docs/monograph/prime-matrix-strict-actual-cold-product-block-parameter-router.json` | `2428d70c9536c4b33a959d5f3410fcdb151910226841e49e51f387080ebf769f` |
| `docs/monograph/prime-matrix-concrete-source-tuple-anchor-parameter-router.json` | `74670815e579c18d92061f1e4ea57f992810d9a43fbaed2b319ccfa02fd958bb` |
| `docs/monograph/prime-matrix-formal-unit-source-record-router.json` | `fe51a3ea8f7d8a71e3f667b43fda4229c11324772afb8c321a06c4d5fab36a2f` |
| `docs/monograph/prime-matrix-canonical-formal-unit-hash-stability-router.json` | `359c78f1c0629e514eb584acdb81ed489d36a0ba111a37a5c40eee03e59e3af6` |
| `docs/monograph/prime-matrix-strict-cold-product-block-inventory-router.json` | `a9630947c1df0d152a5f1e9f111863792c4022494f509f6ae966b0f7957d6b1b` |
| `docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json` | `4c85ccfac092bb1ef772079cbf6adaa4c1f64f7b485b8d3ed2a71e2ea67422f9` |
