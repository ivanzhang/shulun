# Prime Matrix 批量 Rankin pass-or-return 路由器

**状态：** `batch_rankin_pass_return_closed_pdec_sae_or_constant_gap_open`

BatchRankinCertificatesAllPassOrReturnToPDECSAE 已闭合为 pass-or-return 门：schema、concrete manifest/data、逐色证书生成律和 failed-return packet 纪律均已回收。这一步只说明 Rankin 批量行不会漏账；新的最窄点转为 `PDECOrSAEUnifiedExclusionLedger`，并保留 `RankinConstantGapRefinementLedger` 与 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`，不关闭行列无条件定理。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
batch_rankin_verifier_schema_closed=true
batch_rankin_pass_or_return_closed=true
concrete_rankin_batch_manifest_data_closed=true
failed_rankin_return_packet_ledger_closed=true
formal_rankin_batch_manifest_found=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
BatchRankinCertificatesAllPassOrReturnToPDECSAE => BatchRankinVerifierSchemaClosed AND ConcreteRankinBatchManifestDataLedger AND FailedRankinReturnPacketLedger; failures still route to PDECOrSAEUnifiedExclusionLedger or RankinConstantGapRefinementLedger.
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
- batch manifest: `1`
- failed return packets: `1`

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BatchRankinGateActive | `true` | `false` | 上一层已把最窄点推进到批量 Rankin pass-or-return。 | BatchRankinCertificatesAllPassOrReturnToPDECSAE |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设反例链条内的批量证书，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| AllowedBudgetDisciplineImported | `true` | `true` | allowed_budget 已要求预登记、总预算守卫和失败回流。 | 无预算纪律剩余。 |
| RankinAcceptanceAndReturnImported | `true` | `true` | RLA 处理 pass，LMC/FXA 处理 low-mod spike 回流，no-spike 保留 constant-gap。 | PDECOrSAEUnifiedExclusionLedger or RankinConstantGapRefinementLedger |
| ExecutableRankinSamplePasses | `true` | `true` | 现有样本证书通过 exact 与 Rankin 预算，说明单证书格式可执行。 | 样本不是批量全集。 |
| BatchRankinVerifierSchemaClosed | `true` | `true` | 批量验收 schema 已闭合：逐 color_id 要么 pass，要么给失败回流 packet。 | BatchRankinVerifierSchemaClosed |
| ConcreteRankinManifestDataImported | `true` | `true` | 已回收 concrete Rankin manifest 数据：颜色全集、逐色证书与逐行分类生成律均固定。 | manifest/data 已可生成；不再作为 BatchRankin 剩余。 |
| FailedRankinReturnPacketsAvailable | `true` | `true` | 已回收 failed-Rankin 回流 packet 纪律：失败行要么命名回流，要么全 pass 空声明。 | 失败回流不漏账；PDEC/SAE 与 constant-gap 仍在下游。 |
| BatchRankinCertificatesAllPassOrReturnToPDECSAE | `true` | `true` | 批量 Rankin 门已闭合为 pass-or-return：全量 manifest/data 存在，且每行 pass 或进入合法回流。 | PDECOrSAEUnifiedExclusionLedger OR RankinConstantGapRefinementLedger |

## 5. 下一步

当前唯一最窄点更新为 `PDECOrSAEUnifiedExclusionLedger`；`RankinConstantGapRefinementLedger` 与 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 仍是独立剩余。

审稿边界：本步只关闭批量 Rankin pass-or-return 门，不关闭 PDEC/SAE、constant-gap、DStructure/Rankin 独立验收，也不关闭行列无条件定理。
