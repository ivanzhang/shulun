# Prime Matrix failed Rankin return packet 路由器

**状态：** `failed_rankin_return_packet_closed_batch_rankin_ready`

FailedRankinReturnPacketLedger 已闭合：Rankin 失败行不会消失；要么 manifest 全 pass 并写空声明，要么每个失败 color_id 进入 PDEC/SAE 或 constant-gap packet。下一步回收 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
failed_rankin_return_packet_ledger_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
FailedRankinReturnPacketLedger => ManifestRows AND PerColorVerdicts AND AllPassEmptyDeclaration OR NamedFailurePackets.
```

## 2. 回流记录族

| record_type | coverage | rule |
| --- | --- | --- |
| all_pass_empty_return_declaration | 若 manifest 没有失败行，则必须显式写 all_pass=true。 | 空 packet 不是缺失；它是 manifest 全 pass 的可复核声明。 |
| failed_color_header | 每个 rankin_budget_pass=false 的 color_id 一条。 | 记录 color_id、rankin_certificate_hash、failure_kind 和 source_tuple_hash。 |
| lowmod_core_crtdefect_packet | failure_kind=lowmod_core_crtdefect 的失败行。 | 写 directed core、residue spike、low-mod witness，并转入 PDEC/SAE。 |
| constant_gap_packet | failure_kind=constant_gap 的失败行。 | 写 no-spike 证据和常数缺口账本引用，转入 constant-gap refinement。 |
| packet_hash_row | 每个 packet 一条。 | return_packet_id=H(source_tuple_hash,color_id,failure_kind,payload_hash)。 |

## 3. 回流纪律

| law | formula | meaning |
| --- | --- | --- |
| pass_rows_need_no_packet | rankin_budget_pass=true -> no failed packet required. | pass 行不会制造伪回流。 |
| all_pass_empty_packet | no failed rows -> all_pass_empty_return_declaration. | 全 pass 情况必须显式声明，避免把缺 packet 误解成漏账。 |
| failed_rows_total | rankin_budget_pass=false -> exactly one failed return packet. | 每个失败颜色类必须有命名去向。 |
| two_exit_classification | failure_kind in {lowmod_core_crtdefect, constant_gap}. | Rankin 失败不能产生第三种无名出口。 |
| pdec_sae_not_closed_here | lowmod_core_crtdefect -> PDEC/SAE terminal remains downstream. | 本步只回流，不排斥 PDEC/SAE。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FailedRankinReturnGateActive | `true` | `false` | 上一层已把最窄点推进到 failed Rankin return packet。 | FailedRankinReturnPacketLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ManifestAndPerColorFilesImported | `true` | `true` | manifest 行与逐色 Rankin verdict 已固定。 | 失败行全集固定。 |
| BatchReturnSchemaImported | `true` | `true` | 批量 Rankin schema 已要求每行 pass 或合法回流。 | pass-or-return 字段固定。 |
| LowModAndFinalExitImported | `true` | `true` | low-mod spike 回流 PDEC/SAE；无 spike 进入 constant-gap refinement。 | PDECOrSAEUnifiedExclusionLedger or RankinConstantGapRefinementLedger |
| CanonicalReturnHashImported | `true` | `true` | return_packet_id 继承 source_tuple_hash、color_id 与 failure_kind。 | packet 身份稳定。 |
| FailedRankinReturnPacketLedger | `true` | `true` | 失败 Rankin 行要么不存在并写 all-pass 空声明，要么逐行生成命名回流 packet。 | BatchRankinCertificatesAllPassOrReturnToPDECSAE |

## 5. 下一步

当前回收目标为 `BatchRankinCertificatesAllPassOrReturnToPDECSAE`。

审稿边界：本步只证明 Rankin 失败不漏账；不排斥 PDEC/SAE，不关闭 DStructure/Rankin 最终晋级门。
