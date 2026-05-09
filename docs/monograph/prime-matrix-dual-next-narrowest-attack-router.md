# Prime Matrix 内外两线下一最窄硬攻路由器

**状态：** `dual_next_narrowest_reduced_to_new_full_s_source_theorem_or_accepted_external_contract_plus_referee_open`

下一最窄目标已经重新压缩：canonical actual-source provenance 已只在 canonical 分支关闭，不能再作为全局剩余继续攻；unrestricted generic WFD 模板已被 moving-delta 阻断。完全自足线只剩 NewFullSNonAPSourceAntiAtomTheoremInput。黑箱外部线可以明确接受 FullS-KLS-ext 合同；若不接受黑箱，则 DI/BFI 主来源特化和 APSourceLift 都已被 no-go 排除，外部线也只剩 NewFullSTheoremInput。三条数学路径之后都必须通过 DStructure/Tail-log4/finite Rankin 独立验收。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
dual_next_narrowest_boundary_closed=true
all_required_inputs_proved_or_accepted=false
row_column_unconditional_closed=false
```

## 1. 下一最窄目标

完全自足线：

```text
NewFullSNonAPSourceAntiAtomTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部黑箱合同线：

```text
AcceptFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部证明线：

```text
NewFullSTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

统一二线输入基：

```text
((NewFullSNonAPSourceAntiAtomTheoremInput) OR AcceptFullSKLSExtExternalContract OR NewFullSTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 2. 路由审查表

| gate | lane | boundary closed | proved/accepted | evidence | consequence | next target |
| --- | --- | --- | --- | --- | --- | --- |
| `TerminalBoundaryImported` | `both` | `true` | `false` | terminal_closure_gap_split_to_actual_source_or_external_contract_plus_referee_open | 旧终端已拆成自足、外部黑箱、无黑箱外部证明和独立晋级门。 | `DualLaneNextNarrowestCompression` |
| `CanonicalActualSourceNoLongerNextTarget` | `self-contained` | `true` | `true` | NoFurtherActualSourceProvenanceGap | canonical 分支来源账本已闭合；继续攻它不能覆盖 noncanonical full-S 补集。 | `NewFullSNonAPSourceAntiAtomTheoremInput` |
| `GenericWFDTemplateForbidden` | `self-contained` | `true` | `true` | generic_wfd_template_available=false | moving-delta no-go 后，不能把 unrestricted generic WFD 当作自足引理继续使用。 | `NewFullSNonAPSourceAntiAtomTheoremInput` |
| `SelfContainedNextNarrowestPinned` | `self-contained` | `true` | `false` | NewFullSNonAPSourceAntiAtomTheoremInput | 完全自足线被压到一个新源定理：实际 noncanonical full-S 源的强化反原子。 | `NewFullSNonAPSourceAntiAtomTheoremInput` |
| `ExternalBlackBoxContractAvailable` | `external-blackbox` | `true` | `false` | full_s_kls_ext_contract_closed_primary_source_proof_open | 接受 FullS-KLS-ext 作为外部深定理合同时，外部数学 lane 可关闭；当前未把它登记为最终已接受输入。 | `AcceptFullSKLSExtExternalContract` |
| `PrimarySourceSpecializationRejected` | `external-no-blackbox` | `true` | `false` | NewFullSTheoremInputOrAPSourceLift | 现有 DI/BFI 主来源不能逐项推出当前 full-S non-AP KLS-ext。 | `NewFullSTheoremInputOrAPSourceLift` |
| `APSourceLiftRejected` | `external-no-blackbox` | `true` | `true` | NewFullSTheoremInput | non-AP generic WFD 补集不能无损回提到 AP-source；无黑箱外部线只剩新 full-S 定理证明。 | `NewFullSTheoremInput` |
| `ExternalNoBlackBoxNextNarrowestPinned` | `external-no-blackbox` | `true` | `false` | primary_source_no_go + ap_source_lift_no_go | 若不接受黑箱合同，外部路线也不再是找旧 DI/BFI 引文，而是新增或证明能覆盖 full-S non-AP 对象的定理。 | `NewFullSTheoremInput` |
| `DStructureRankinRefereeGateStillSeparate` | `referee` | `true` | `false` | dstructure_rankin_promotion_boundary_closed_referee_acceptance_open | 任何数学 lane 闭合后，仍需 DStructure/Tail-log4/finite Rankin 独立验收。 | `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 3. 当前判定

本路由闭合的是“下一步应攻哪里”的边界，不证明新 full-S 源反原子，也不把 FullS-KLS-ext 自动登记为已接受外部输入，更不替代 DStructure/Rankin 独立验收。
因此完整行/列无条件命题仍未闭合；下一步最窄硬点已经固定为上述三条路径之一。
