# Prime Matrix concrete Rankin batch manifest 数据路由器

**状态：** `concrete_rankin_manifest_emitter_closed_per_color_rankin_open`

ConcreteRankinBatchManifestDataLedger 的发射流程已闭合：给定 concrete color set 后，可逐颜色生成 Rankin 证书并组装 manifest。当前 color set 已回收，新的最窄点是 `PerColorRankinCertificateFileLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
concrete_rankin_batch_manifest_emitter_closed=true
concrete_rankin_batch_manifest_data_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
ConcreteRankinBatchManifestDataLedger => ConcreteRankinBatchManifestEmitterClosed AND ConcreteColorSetEnumerationLedger AND PerColorRankinCertificateFileLedger.
```

## 2. 生成步骤

| step | output | meaning |
| --- | --- | --- |
| enumerate_color_set | ConcreteColorSetEnumerationLedger | 从 concrete coloring coverage 证书取完整 color_id 集合与每色 intervals。 |
| generate_per_color_rankin | PerColorRankinCertificateFileLedger | 对每个 color_id 运行单颜色 Rankin 审计，写出证书路径和 hash。 |
| classify_each_row | pass/lowmod_core_crtdefect/constant_gap | 按 allowed_budget 纪律判定 pass 或失败回流类型。 |
| attach_failed_returns | FailedRankinReturnPacketLedger | 失败行必须有 PDEC/SAE 回流包或 constant-gap refinement 包。 |
| emit_manifest | ConcreteRankinBatchManifestDataLedger | 写出 batch manifest，并声明 color_set_exact 与 all_rows_pass_or_return。 |

## 3. 当前扫描

- color-set-like JSON: `1`
- Rankin-certificate-like JSON: `1`
- return-packet-like JSON: `0`

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ConcreteRankinManifestDataGateActive | `true` | `false` | 上一层已把最窄点推进到 concrete Rankin batch manifest 数据。 | ConcreteRankinBatchManifestDataLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条内的数据生成，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| ManifestEmitterInputsReady | `true` | `true` | manifest schema、coloring schema、budget discipline 与单证书执行格式均已固定。 | 无发射规则剩余。 |
| ConcreteRankinBatchManifestEmitterClosed | `true` | `true` | concrete manifest 的生成流程已固定为颜色枚举、逐色证书、逐行分类、失败回流、manifest 发射。 | ConcreteRankinBatchManifestEmitterClosed |
| ConcreteColorSetEnumerationAvailable | `true` | `false` | 已发现 concrete color set 枚举闭合证书，可定义 manifest 全集行。 | ConcreteColorSetEnumerationLedger |
| PerColorRankinCertificateFilesAvailable | `true` | `false` | 仓库只发现样本/局部 Rankin 证书，尚非逐颜色全集。 | PerColorRankinCertificateFileLedger |
| FailedRankinReturnPacketsAvailable | `false` | `false` | 若 manifest 存在失败行，仍需正式回流包；当前未发现。 | FailedRankinReturnPacketLedger |
| ConcreteRankinBatchManifestDataLedger | `false` | `false` | Concrete manifest 数据不能由发射规则关闭；仍需逐颜色 Rankin 证书和 manifest。 | PerColorRankinCertificateFileLedger |

## 5. 下一步

当前唯一最窄点更新为 `PerColorRankinCertificateFileLedger`。

审稿边界：本步回收 concrete color set 并保持全量 Rankin manifest 打开；不关闭行列无条件定理。
