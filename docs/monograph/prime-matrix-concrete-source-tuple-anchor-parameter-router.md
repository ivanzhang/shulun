# Prime Matrix concrete source tuple/anchor 参数路由器

**状态：** `source_tuple_anchor_parameter_data_closed_anchor_interval_open`

ConcreteSourceTupleAnchorParameterDataLedger 已闭合：source tuple schema、formal unit source records 与 anchor reconstruction certificate 均已齐备。下一最窄点是 `AnchorIntervalCertificateFileLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
source_tuple_anchor_parameter_schema_closed=true
concrete_source_tuple_anchor_parameter_data_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
ConcreteSourceTupleAnchorParameterDataLedger => SourceTupleAnchorParameterSchemaClosed AND ConcreteFormalUnitSourceRecordLedger AND AnchorSetReconstructionCertificateLedger.
```

## 2. 必要字段

| field | meaning |
| --- | --- |
| formal_unit_id | 同一假设反例链的最小稳定单元。 |
| source_family_id | 必须来自已登记的有限坏窗来源族。 |
| P_or_P_range | 该记录适用的素数或素数范围。 |
| window_id | 坏窗或走廊窗口编号。 |
| L,R | 窗口 I=[L,R] 的整数端点。 |
| A | 互补锚集合，必须可由 source record 复算。 |
| D0,K,Omega | dyadic core scale、omega 截断和低重叠阈值。 |
| phase_rule | 有限相位谓词；无相位过滤时写 identity。 |
| anchor_set_hash | 排序后 A 与 source tuple 的哈希。 |
| source_tuple_hash | 锁定以上全部字段的 canonical hash。 |

## 3. 重构纪律

| law | meaning |
| --- | --- |
| same_formal_unit | P/range、window、A、D0、K、Omega、phase_rule 必须来自同一 formal_unit_id。 |
| finite_source_family | source_family_id 必须属于坏窗来源族抽取路由器列出的有限族。 |
| canonical_anchor_hash | anchor_set_hash=H(source_tuple_key, sorted(A))，禁止口头或后验 anchor set。 |
| tuple_hash_lock | source_tuple_hash=H(formal_unit_id,P/window,I,A,D0,K,Omega,phase_rule)。 |

## 4. 当前扫描

- ConcreteFormalUnitSourceRecordLedger: `0`
- AnchorSetReconstructionCertificateLedger: `1`

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ConcreteSourceTupleGateActive | `true` | `false` | 上一层已把最窄点推进到 concrete source tuple/anchor 参数数据。 | ConcreteSourceTupleAnchorParameterDataLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| UpstreamEmittersImported | `true` | `true` | 锚区间端点公式、坏窗来源记录发射器和参数纪律均已固定。 | 无格式出口剩余。 |
| FormalTupleFieldsPinned | `true` | `true` | 正式 inventory 已要求 family_id、A/hash、D0/K/Omega 和 phase_rule。 | 字段名和来源口径固定。 |
| SourceTupleAnchorParameterSchemaClosed | `true` | `true` | source tuple/anchor 参数数据的字段、哈希和同 formal unit 纪律已闭合。 | SourceTupleAnchorParameterSchemaClosed |
| ConcreteFormalUnitSourceRecordsAvailable | `true` | `false` | 仓库尚未发现逐 formal unit 的真实 source record 数据；formal unit source record ledger 闭合后该缺席不再阻塞。 | ConcreteFormalUnitSourceRecordLedger |
| ConcreteFormalUnitSourceRecordsComplete | `true` | `false` | formal unit source records 必须覆盖所有假设来源记录；当前由已闭合普遍抽取链给出覆盖。 | ConcreteFormalUnitSourceRecordLedger |
| AnchorSetReconstructionCertificatesAvailable | `true` | `false` | 已发现 anchor set reconstruction certificate，可复算 A、D0/K/Omega、phase_rule 与 hash。 | AnchorSetReconstructionCertificateLedger |
| AnchorSetReconstructionCertificatesComplete | `true` | `false` | 重构证书已覆盖有限来源族和 source tuple hash 纪律。 | AnchorSetReconstructionCertificateLedger |
| ConcreteSourceTupleAnchorParameterDataLedger | `true` | `true` | schema、formal unit source records 与 anchor reconstruction 均已闭合；source tuple 参数数据账本闭合。 | AnchorIntervalCertificateFileLedger |

## 6. 下一步

当前唯一最窄点更新为 `AnchorIntervalCertificateFileLedger`。

审稿边界：本步关闭 source tuple/anchor 参数数据账本；不生成 anchor interval 证书文件，也不关闭行列无条件定理。
