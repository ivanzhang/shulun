# Prime Matrix strict BG/Baker 与 Structured-EHPD 同步证书

**状态：** `bg_baker_history_recovered_structured_ehpd_replacement_lane_restored_final_acceptance_open`

BG/Baker 旧研究已经找到了两件关键事实：Baker 单频率素变量定理可抽取但不能处理 d 层平均，EXT-BG/RKS 外部固定对数节省可与 Tail-log4 参数严格匹配。随后 Structured-EHPD/OMR 保守结构包已把作者侧路线从旧 BG 四常数阻塞中解耦，并由 `log_P0=3.5` 与 `P<=exp(5)` 有限验证形成常数层面闭合。因此当前真正最精确硬点不是继续把 BG 自足重证当作唯一剩余，而是对 `StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance` 做最终接口验收，并保留独立 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 晋级门。

```text
baker_theorem_extracted_in_prior_work=true
baker_single_frequency_replacement_insufficient=true
ext_bg_rks_external_match_ready=true
structured_ehpd_decouples_old_bg_constants=true
structured_lane_packet_ready=true
bg_self_proof_as_unique_hardpoint_rejected=true
row_column_unconditional_closed=false
```

## 1. 纠偏后的硬点顺序

| order | target |
| ---: | --- |
| 1 | `StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance` |
| 2 | `ExplicitIndependentPromotionAcceptanceRecord` |
| 3 | `SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving OR BakerFrequencyLargeSieveOrDBGAverageReplacement` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PriorBakerTheoremExtractionRecovered` | `true` | `true` | 旧材料已抽取 Baker Theorem 1：单频率素变量有显式指数，但仍有常数和 d 平均问题。 | history recovered |
| `BakerSingleFrequencyInsufficiencyPreserved` | `true` | `true` | Baker 点态素变量估计不能直接控制 coherent d 层绝对值平均。 | BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `EXTBGRKSExternalMatchReady` | `true` | `true` | BG/RKS 外部路线只需固定对数节省，参数匹配与引用边界已经定位。 | Accept EXT-BG if external lane is used |
| `StructuredEHPDDecouplesOldBGConstants` | `true` | `true` | 旧 `delta_BG_*` 四常数阻塞已被 `use_structured_ehpd + use_omr_pack` 路线绕开。 | BG reproof is no longer the unique internal route |
| `OMRCGTPLSMPNRCFCTPacketPresent` | `true` | `true` | D 组结构包已拆成 OMR/CGTP/LSMP、NRC、FCT/Tree-WFE 的可审查定理族。 | final symbol/interface audit |
| `RowColumnToStructuredEHPDReductionPresent` | `true` | `true` | 行/列反例到 Structured-EHPD 坏配置的 A/B 归约已经成稿。 | A/B-D interface consistency |
| `ConservativeP0AndFiniteOverlapClosed` | `true` | `true` | 保守结构常数包给 log_P0=3.5，有限验证覆盖到 exp(5)，两段重叠。 | certificate reproducibility |
| `OldBGSelfProofAsUniqueHardpointRejected` | `true` | `true` | 继续把 BG 自足重证写成唯一剩余会漏掉 Structured-EHPD/OMR 保守替代路线。 | StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance |
| `StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance` | `false` | `false` | 结构路线证据包和常数层面已齐；但顶刊审查口径仍要求把最终接口作为独立接受/最终审稿验收项。 | StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance OR ExplicitIndependentPromotionAcceptanceRecord |
| `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | `false` | `false` | DStructure/Tail-log4/finite Rankin 晋级门尚无独立接受记录。 | ExplicitIndependentPromotionAcceptanceRecord OR SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步完成路线同步与硬点纠偏；未生成独立验收事件，故不宣称无条件闭合。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最精确硬攻点

```text
StructuredEHPDConservativePackageFinalInterfaceAuditAndAcceptance
```
