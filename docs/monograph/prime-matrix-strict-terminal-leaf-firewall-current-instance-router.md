# Prime Matrix strict 终端叶子防火墙当前实例压缩路由器

**状态：** `strict_terminal_leaf_firewall_current_instance_reduced_future_schema_disciplined`

本步把 `TerminalLeafFirewallInputs` 做当前实例压缩：已物化 PDEC 前沿与 sparse/LocalSurvivor 前沿均为零，所以 `FutureExplicitPrimitivePDECSchema_if_new` 与 `FutureExplicitSparsePacketExtractorSchema_if_new` 在当前证明语料中不是活动数学障碍，而是未来准入纪律。它们不能被删除为全局不存在，只能从当前活动叶子中移出。因此当前 strict 自足终端剩余压成 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode`。noncanonical 合法闭合模式仍未证明，canonical-lock 也仍未证明；行/列命题仍未无条件闭合。

```text
current_materialized_pdec_frontier_closed=true
current_materialized_sparse_frontier_closed=true
future_pdec_schema_admission_discipline_closed=true
future_sparse_schema_admission_discipline_closed=true
current_leaf_firewall_active_basis_reduced=true
future_schema_global_nonexistence_claimed=false
terminal_leaf_firewall_inputs_proved_or_accepted=false
noncanonical_legal_closure_mode_proved=false
acyclic_terminal_canonical_lock_proved=false
strict_acyclic_terminal_family_proved=false
row_column_unconditional_closed=false
terminal_gap_after_current_instance_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode
```

## 1. 当前实例压缩链

```text
AcyclicTerminalLeafFirewallInputs[
  FutureExplicitPrimitivePDECSchema_if_new
  OR FutureExplicitSparsePacketExtractorSchema_if_new
  OR NoncanonicalFullSComplementLegalClosureMode
]
  + current materialized PDEC frontier = 0
  + current materialized sparse frontier = 0
  + future schema clauses are admission discipline only
  -> current active leaf = NoncanonicalFullSComplementLegalClosureMode
```

注意：这一步只移动当前活动硬点，不声明未来 PDEC/sparse family 全局不存在。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalLeafFirewallInputActive` | `true` | `false` | 上一层把无隐藏循环终端压到 canonical-lock 或叶子防火墙输入。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode] |
| `CurrentPDECInstanceFrontierZeroImported` | `true` | `true` | 当前已物化合法非二点 primitive PDEC 候选为零；这只清理当前语料实例。 | 未来新 PDEC 必须先提交 FutureExplicitPrimitivePDECSchema。 |
| `CurrentSparseInstanceFrontierZeroImported` | `true` | `true` | 当前 sparse/LocalSurvivor 前沿没有开放物化义务；这只清理当前语料实例。 | 未来新 sparse route 必须先提交 FutureExplicitSparsePacketExtractorSchema。 |
| `FuturePDECSchemaNotCurrentMathObligation` | `true` | `true` | FutureExplicitPrimitivePDECSchema_if_new 是准入纪律，不是当前已经出现的叶子障碍。 | 若未来新增 PDEC family，则重开显式 schema 审查。 |
| `FutureSparseSchemaNotCurrentMathObligation` | `true` | `true` | FutureExplicitSparsePacketExtractorSchema_if_new 是准入纪律，不是当前已经出现的叶子障碍。 | 若未来新增 sparse family，则重开有限 extractor schema 审查。 |
| `CurrentLeafFirewallActiveBasisReduced` | `true` | `true` | 在当前已物化实例内，叶子防火墙活动数学硬点只剩 noncanonical full-S 合法闭合模式。 | NoncanonicalFullSComplementLegalClosureMode |
| `NoncanonicalLegalClosureModeCurrentCorpusProved` | `true` | `false` | noncanonical full-S 补集仍未自足闭合；generic WFD 反原子已经不能使用。 | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource OR accept/prove exact FullS-KLS-ext |
| `CanonicalLockStillOpenAlternative` | `true` | `false` | canonical-lock 是并列替代路线，但需要 seed 因子嵌入、同集推前和无 payload 残留。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `TerminalLeafFirewallInputsCurrentInstanceProved` | `true` | `false` | 当前实例已压缩，但 noncanonical 合法模式未证，所以不能说叶子输入已全部证明或接受。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |
| `StrictAcyclicTerminalFamilyCurrentCorpusProved` | `true` | `false` | 终端硬点更窄，但仍未闭合 acyclic terminal family。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 仍缺 terminal 二选一、高段 Mertens/PNT 自足尾项或外部接受、DStructure/Rankin 替代包。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

严格自足基更新为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`NoncanonicalFullSComplementLegalClosureMode_OR_CanonicalLock`。

必须证明：
- 主攻 noncanonical full-S：证明实际源恒等，或证明强化实际源反原子，或明确接受/证明 exact FullS-KLS-ext。
- 并行备用 canonical-lock：证明 acyclic seed 可测有限因子嵌入、终端证书同集推前、无 noncanonical payload 残留。
- 若未来有人提出新 PDEC/sparse 路线，必须先提交对应显式 schema，不得作为隐藏终端使用。
- 保持高段 Mertens/PNT 自足尾项与 DStructure/Rankin 替代包独立验收。

不能作为证明使用：
- 把当前 PDEC/sparse 前沿为零说成未来全局 family 不存在。
- 把 future schema firewall 当作 future schema 内容本身。
- 把 noncanonical 三歧边界闭合当成 noncanonical 分支已证明。
- 把 canonical-source PDEC-CAP 闭合直接导入 acyclic noncanonical 分支。
- 把外部 FullS-KLS 或 Mertens/theta 输入写成 strict 自足证明。
