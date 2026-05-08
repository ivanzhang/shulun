# Prime Matrix per-color Rankin certificate file 路由器

**状态：** `per_color_rankin_certificate_files_closed_manifest_open`

PerColorRankinCertificateFileLedger 已闭合：每个 color_id 的 Rankin 单证书文件、预算 verdict、hash 与失败回流要求均可复算。下一步回收 `ConcreteRankinBatchManifestDataLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
per_color_rankin_certificate_file_ledger_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
PerColorRankinCertificateFileLedger => ColorSetEnumeration AND AllowedBudgetDiscipline AND RankinVerifier AND FailureReturnRequirement.
```

## 2. 证书记录族

| record_type | coverage | rule |
| --- | --- | --- |
| color_certificate_header | 每个 color_id 一条。 | 记录 source_tuple_hash、color_set_id、color_id、intervals_hash、K、phase_rule、allowed_budget。 |
| rankin_input_row | 每个同色不交 interval 或压缩段一条。 | 输入必须来自 coverage equation 后的同色不交 partition。 |
| rankin_parameter_row | 每个 color_id 一条。 | 记录 s/weights/cutoff 与 RLA 验收所需常数，禁止看结果后调参。 |
| rankin_budget_verdict | 每个 color_id 一条。 | rankin_budget_pass=true iff R_s(C_c;K)<=allowed_budget。 |
| exact_budget_crosscheck | 可执行样本或有限段必须写 exact_budget_pass。 | exact 计数用于审计，不替代 Rankin 验收定理。 |
| failure_return_requirement | 每个 rankin_budget_pass=false 的 color_id 一条。 | 必须标记 lowmod_core_crtdefect 或 constant_gap，并交给 manifest 连接 return packet。 |

## 3. 验收纪律

| law | formula | meaning |
| --- | --- | --- |
| one_file_per_color | color_id in ColorSet -> exactly one rankin certificate file. | 不能漏掉颜色类，也不能重复审计同一颜色类。 |
| same_source_tuple_lock | certificate.source_tuple_hash == color_set.source_tuple_hash. | Rankin 文件不能跨 source tuple 拼接 intervals 或预算。 |
| budget_predeclared | allowed_budget is inherited from inventory before the Rankin run. | 禁止后验调预算。 |
| rankin_pass_definition | pass iff R_s(C_c;K)<=B_c for the recorded parameters. | pass 判定只由 RLA 验收式给出。 |
| failure_is_not_erasure | not pass -> failure_kind in {lowmod_core_crtdefect, constant_gap}. | 失败颜色类必须进入后续 return，不允许静默删除。 |
| certificate_hash | rankin_certificate_hash=H(header,input_rows,parameters,verdict). | 单证书路径和 hash 可由 manifest 复核。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PerColorRankinFileGateActive | `true` | `false` | 上一层已把最窄点推进到 per-color Rankin certificate file。 | PerColorRankinCertificateFileLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ColorSetImported | `true` | `true` | color_id 全集和每色同色不交 intervals 已由 coverage/color-set 账本固定。 | 不能漏色或重选 intervals。 |
| AllowedBudgetImported | `true` | `true` | 每个 color_id 的 allowed_budget 必须预登记，失败路由已固定。 | 不能后验调预算。 |
| RankinVerifierImported | `true` | `true` | RLA 验收式和可执行样本均已固定，单证书格式可复核。 | 样本不等于全局 pass。 |
| CanonicalCertificateHashImported | `true` | `true` | rankin_certificate_hash 继承 source_tuple_hash 与 color_id。 | 证书身份稳定。 |
| FailureRowsRemainNamed | `true` | `false` | 本步允许某些 color_id 的 Rankin 不通过，但失败必须进入 lowmod_core_crtdefect 或 constant_gap。 | FailedRankinReturnPacketLedger or RankinConstantGapRefinementLedger |
| PerColorRankinCertificateFileLedger | `true` | `true` | 逐色 Rankin 证书文件账本闭合：每个 color_id 都有可复算文件、verdict 和失败回流要求。 | ConcreteRankinBatchManifestDataLedger |

## 5. 下一步

当前回收目标为 `ConcreteRankinBatchManifestDataLedger`。

审稿边界：本步只关闭逐色 Rankin 文件生成与验收字段；不宣称所有颜色类 pass，不关闭 PDEC/SAE 或行列无条件定理。
