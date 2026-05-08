# Prime Matrix 批量 Rankin pass-or-return 路由器

**状态：** `batch_rankin_schema_closed_manifest_missing`

BatchRankinCertificatesAllPassOrReturnToPDECSAE 的验收 schema 已闭合：每个正式颜色类必须在 batch manifest 中有一行，且该行要么 Rankin pass，要么提供 low-mod core CRTDefect/PDEC-SAE 回流 packet，或显式 constant-gap。仓库当前只发现单个样本/局部 Rankin 证书，未发现全量 manifest，因此新的最窄点是 `FormalRankinBatchManifestLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
batch_rankin_verifier_schema_closed=true
batch_rankin_pass_or_return_closed=false
formal_rankin_batch_manifest_found=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
BatchRankinCertificatesAllPassOrReturnToPDECSAE => BatchRankinVerifierSchemaClosed AND FormalRankinBatchManifestLedger; failed rows require FailedRankinReturnPacketLedger or RankinConstantGapRefinementLedger.
```

## 2. Manifest 字段

| field | meaning |
| --- | --- |
| batch_id | 批量证书稳定编号。 |
| source_tuple_hash | 锁定同一 coloring/budget source tuple。 |
| color_set_hash | 锁定所有 color_id 的全集，防止漏色。 |
| color_id | 每行对应一个正式颜色类。 |
| rankin_certificate_path | 该颜色类单证书路径。 |
| rankin_certificate_hash | 单证书 sha256。 |
| rankin_budget_pass | 单证书 Rankin 预算验收结果。 |
| exact_budget_pass | 精确计数是否也进入预算；用于审计交叉核验。 |
| failure_kind | pass、lowmod_core_crtdefect 或 constant_gap。 |
| return_packet_id | 失败时指向 PDEC/SAE 回流 packet 或常数缺口 packet。 |
| coverage_equation_ref | 指向 coloring coverage 证书，说明没有遗漏颜色类。 |

## 3. 当前扫描

- Rankin-like JSON: `1`
- batch manifest: `0`
- failed return packets: `0`

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BatchRankinGateActive | `true` | `false` | 上一层已把最窄点推进到批量 Rankin pass-or-return。 | BatchRankinCertificatesAllPassOrReturnToPDECSAE |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条内的批量证书，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| AllowedBudgetDisciplineImported | `true` | `true` | allowed_budget 已要求预登记、总预算守卫和失败回流。 | 无预算纪律剩余。 |
| RankinAcceptanceAndReturnImported | `true` | `true` | RLA 处理 pass，LMC/FXA 处理 low-mod spike 回流，no-spike 保留 constant-gap。 | PDECOrSAEUnifiedExclusionLedger or RankinConstantGapRefinementLedger |
| ExecutableRankinSamplePasses | `true` | `true` | 现有样本证书通过 exact 与 Rankin 预算，说明单证书格式可执行。 | 样本不是批量全集。 |
| BatchRankinVerifierSchemaClosed | `true` | `true` | 批量验收 schema 已闭合：逐 color_id 要么 pass，要么给失败回流 packet。 | BatchRankinVerifierSchemaClosed |
| FormalRankinBatchManifestAvailable | `false` | `false` | 仓库尚未发现覆盖全部正式颜色类的 Rankin batch manifest。 | FormalRankinBatchManifestLedger |
| FailedRankinReturnPacketsAvailable | `false` | `false` | 仓库尚未发现正式 failed-Rankin 回流 packet；若全 pass 可为空，但必须由 manifest 说明。 | FailedRankinReturnPacketLedger |
| BatchRankinCertificatesAllPassOrReturnToPDECSAE | `false` | `false` | 批量门不能由 schema 和样本关闭；必须有全量 manifest 且每行 pass 或合法回流。 | FormalRankinBatchManifestLedger AND (FailedRankinReturnPacketLedger OR all-pass manifest) |

## 5. 下一步

当前唯一最窄点更新为 `FormalRankinBatchManifestLedger`；若 manifest 中存在失败行，则还需要 `FailedRankinReturnPacketLedger`。

审稿边界：本步不关闭批量 Rankin 门，不关闭 PDEC/SAE，也不关闭行列无条件定理。
