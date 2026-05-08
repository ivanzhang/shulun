# Prime Matrix 正式 Rankin batch manifest 路由器

**状态：** `formal_rankin_batch_manifest_schema_closed_data_missing`

FormalRankinBatchManifestLedger 的 schema 层已闭合：正式 manifest 必须精确覆盖 coloring 证书中的 color_id 全集，禁止重复，所有 hash 必须对齐，并且每行必须 pass 或合法回流。仓库当前未发现 concrete manifest，因此新的最窄点是 `ConcreteRankinBatchManifestDataLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
formal_rankin_batch_manifest_schema_closed=true
formal_rankin_batch_manifest_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
FormalRankinBatchManifestLedger => FormalRankinBatchManifestSchemaClosed AND ConcreteRankinBatchManifestDataLedger.
```

## 2. 完整性规则

| rule | meaning |
| --- | --- |
| color_set_exact | manifest 的 color_id 集合必须等于 coloring coverage 证书中的颜色全集。 |
| no_duplicate_color | 每个 color_id 只能出现一次；重复行必须合并或报错。 |
| source_tuple_hash_match | 每行 source_tuple_hash 必须与 coloring/budget 源一致。 |
| certificate_hash_match | 每行 rankin_certificate_hash 必须等于单证书文件实际 sha256。 |
| pass_or_return_total | 每行只能是 pass、lowmod_core_crtdefect return 或 constant_gap return。 |
| all_pass_empty_return_allowed | 若所有行 pass，return packet 可为空，但 manifest 必须显式声明 all_pass。 |

## 3. 当前扫描

- manifest-like JSON: `0`

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FormalRankinManifestGateActive | `true` | `false` | 上一层已把最窄点推进到正式 Rankin batch manifest。 | FormalRankinBatchManifestLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条内的 manifest，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| UpstreamSchemasImported | `true` | `true` | batch schema、coloring coverage、allowed_budget 与 formal inventory schema 均已固定。 | 无 manifest 格式上游剩余。 |
| FormalRankinBatchManifestSchemaClosed | `true` | `true` | manifest 完整性规则已固定为无漏色、无重复、hash 对齐和 pass/return 全覆盖。 | FormalRankinBatchManifestSchemaClosed |
| ConcreteManifestAvailable | `false` | `false` | 仓库尚未发现正式 batch manifest 数据文件。 | ConcreteRankinBatchManifestDataLedger |
| ConcreteManifestComplete | `false` | `false` | manifest 必须声明覆盖全部 color_id。 | ConcreteRankinBatchManifestDataLedger |
| ConcreteManifestRowsPassOrReturn | `false` | `false` | manifest 每行必须 pass 或引用合法回流 packet。 | ConcreteRankinBatchManifestDataLedger OR FailedRankinReturnPacketLedger |
| FormalRankinBatchManifestLedger | `false` | `false` | FormalRankinBatchManifestLedger 不能由 schema 关闭；仍需提交 concrete manifest 数据。 | ConcreteRankinBatchManifestDataLedger |

## 5. 下一步

当前唯一最窄点更新为 `ConcreteRankinBatchManifestDataLedger`。若存在失败行，还需要 `FailedRankinReturnPacketLedger`。

审稿边界：本步只关闭 manifest schema，不提交 concrete manifest，不关闭批量 Rankin 门。
