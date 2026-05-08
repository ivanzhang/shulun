# Prime Matrix formal unit 源记录路由器

**状态：** `formal_unit_source_record_schema_closed_universal_extractor_open`

ConcreteFormalUnitSourceRecordLedger 的 schema 层已闭合，但反证路线不能依赖真实反例数据。因此剩余被改写成普遍抽取输入：必须证明任意早期零行 witness 都能产生有限、无漏、同 formal unit 的 source records。新的最窄点是 `UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
formal_unit_source_record_schema_closed=true
concrete_formal_unit_source_record_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
ConcreteFormalUnitSourceRecordLedger => FormalUnitSourceRecordSchemaClosed AND UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger.
```

## 2. 普遍抽取定理子句

| clause | meaning |
| --- | --- |
| witness_input | 输入任意假设早期零行 witness，例如 (P,n,row_signature)，而不是使用真实零行缺席。 |
| finite_partition | 把 witness 诱导的窗口、端点、尾锚、核心与走廊分成有限 formal units。 |
| source_family_assignment | 每个 formal unit 必须落入已闭合 taxonomy 的有限 source_family_id。 |
| coverage_no_loss | 所有坏窗/走廊义务要么被某个 formal unit 覆盖，要么显式回流 PDEC/SAE/Rankin。 |
| same_unit_hash | 每条记录输出 canonical formal_unit_id 和 source_hash，供下游 A、D0、phase 重构。 |

## 3. 当前扫描

- formal-unit-record-like JSON: `0`

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ConcreteFormalUnitSourceRecordGateActive | `true` | `false` | 上一层已把最窄点推进到 concrete formal unit 源记录。 | ConcreteFormalUnitSourceRecordLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行分支内工作，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| UpstreamSourceSchemasImported | `true` | `true` | source tuple schema、来源族 taxonomy 和记录发射器均已闭合。 | 无来源类型剩余。 |
| FormalUnitSourceRecordSchemaClosed | `true` | `true` | formal unit source record 的输入、输出字段和 coverage/no-loss 义务已固定。 | FormalUnitSourceRecordSchemaClosed |
| ConcreteFormalUnitSourceRecordDataAvailable | `false` | `false` | 仓库尚未发现逐 formal unit 的 concrete source record 数据。 | ConcreteFormalUnitSourceRecordLedger |
| ConcreteFormalUnitSourceRecordDataComplete | `false` | `false` | 固定数据若存在，必须覆盖全部假设反例链诱导的 formal units。 | ConcreteFormalUnitSourceRecordLedger |
| UniversalExtractorTheoremAvailable | `false` | `false` | 反证路线真正需要的是任意早期零行 witness 到 formal unit records 的普遍抽取定理。 | UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger |
| ConcreteFormalUnitSourceRecordLedger | `false` | `false` | 没有实际反例数据时，ledger 只能由 universal extractor theorem 关闭；该定理尚未提交。 | UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger |

## 5. 下一步

当前唯一最窄点更新为 `UniversalEarlyZeroRowFormalUnitExtractorTheoremLedger`；其内部第一子门是 `FormalUnitPartitionCoverageLemma`。

审稿边界：本步没有证明普遍抽取定理，也没有关闭 PDEC/SAE、Rankin 或行列无条件定理。
