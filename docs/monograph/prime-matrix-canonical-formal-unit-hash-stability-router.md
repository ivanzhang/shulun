# Prime Matrix canonical formal unit hash stability 路由器

**状态：** `canonical_formal_unit_hash_stability_closed_universal_extractor_ready`

CanonicalFormalUnitHashStabilityLemma 已闭合：分层 canonical hash 消除自引用，source/return 记录继承同一 formal_unit_id。下一步可回收 `UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
canonical_formal_unit_hash_stability_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
CanonicalFormalUnitHashStabilityLemma => FiniteCanonicalKey AND SourceTupleHashSchema AND AssignmentNoLoss AND ReturnQuotientInheritance AND LayeredHashDiscipline.
```

## 2. 分层哈希纪律

| layer | formula | meaning |
| --- | --- | --- |
| nucleus_key | H0(witness_id, source_family_id, branch_type, P/window, D0,K,Omega,phase_key, parent_return_key) | 先哈希不含 formal_unit_id 的规范核，避免自引用。 |
| formal_unit_id | H1('formal_unit', witness_id, nucleus_key_hash) | formal_unit_id 只由 witness 与规范核决定，分割或回流不后验改名。 |
| source_tuple_hash | H2('source_tuple', formal_unit_id, source_family_id, P/window, A,D0,K,Omega,phase_rule) | source tuple 锁定同一 formal unit 下的参数与锚集合。 |
| source_record_hash | H3('source_record', source_tuple_hash, branch_type, canonical_payload_hash) | 普通来源记录只追加 payload，不改变 formal_unit_id。 |
| return_record_hash | H4('return_record', formal_unit_id, return_type, parent_key_hash, canonical_payload_hash) | PDEC/SAE/ColumnCRT/Rankin 等回流记录继承父 formal unit。 |
| source_tuple_hash_stability | same canonical fields => same hash; any changed field => new key or named return. | 哈希稳定性来自 canonical 字段总函数与 no-loss return，不来自具体反例样本。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CanonicalHashGateActive | `true` | `false` | 上一层已把最窄点推进到 canonical formal unit hash stability。 | CanonicalFormalUnitHashStabilityLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步只给任意假设早期零行 witness 的记录哈希纪律，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| FiniteCanonicalKeyImported | `true` | `true` | 每个 obligation 已有 canonical finite key，字段来源固定。 | 可生成 nucleus_key。 |
| SourceTupleHashSchemaImported | `true` | `true` | source tuple 与 formal unit source record 已规定 formal_unit_id/source_hash/source_tuple_hash 字段。 | 哈希字段口径固定。 |
| AssignmentAndNoLossImported | `true` | `true` | 每个 obligation 要么进入 source record，要么进入 named return record，不能消失。 | 哈希对象全集固定。 |
| ReturnAndQuotientInheritanceImported | `true` | `true` | 重复、边界与 quotient/reuse return 已保留在父 formal unit 账本中。 | return 不改写父 formal_unit_id。 |
| SelfReferenceBrokenByLayeredHash | `true` | `true` | 先定义不含 formal_unit_id 的 nucleus_key，再定义 formal_unit_id 与 source_tuple_hash。 | 消除 formal_unit_id/source_tuple_hash 循环定义。 |
| CanonicalFormalUnitHashStabilityLemma | `true` | `true` | canonical 字段、分层哈希和 no-loss return 共同保证 formal_unit_id 与 source hashes 在分割/回流下稳定。 | UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger |

## 4. 下一步

当前回收目标为 `UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger`。

审稿边界：本步只证明 formal unit 与 source/return 哈希稳定；不证明具体终端排斥，也不关闭行列无条件定理。
