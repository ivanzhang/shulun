# Prime Matrix strict acyclic 终端下降到防火墙输入路由器

**状态：** `strict_acyclic_terminal_descent_schema_closed_leaf_firewall_inputs_open`

本步把 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 的无隐藏循环部分关闭为 schema：固定 PDEC 细化、new-layer 塔、复合 cofactor、LocalSurvivor/SAE、short-window、point-load 和 fixed-wheel 都不能形成无名自回流；它们要么下降，要么进入显式 PDEC/sparse 叶子，要么回到 noncanonical 合法闭合模式。但这不是终端叶子排斥证明。当前最窄剩余从“循环”压成 `TerminalLeafFirewallInputs` 或 canonical-lock：未来 PDEC/sparse 必须提交显式 schema，noncanonical 分支必须证明实际源恒等/强化反原子或接受外部合同。行/列命题仍未无条件闭合。

```text
terminal_return_well_founded_descent_schema_closed=true
hidden_terminal_cycle_removed=true
current_materialized_pdec_frontier_closed=true
current_materialized_sparse_frontier_closed=true
acyclic_terminal_return_well_founded_descent_proved=false
terminal_leaf_firewall_inputs_proved_or_accepted=false
noncanonical_legal_closure_mode_proved=false
strict_acyclic_terminal_family_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode]
```

## 1. 下降到叶子

```text
acyclic terminal self-return
  -> fixed PDEC cap no-cycle
  -> new-layer entropy tower dichotomy
  -> composite cofactor well-founded descent
  -> LocalSurvivor/SAE/short-window/point-load/fixed-wheel named returns
  -> no hidden terminal cycle
  -> explicit leaf firewall inputs
```

关闭的是无隐藏循环，不是叶子输入本身。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WellFoundedDescentInputActive` | `true` | `false` | 上一层把 direct 终端自回流压成 canonical-lock 或 well-founded descent 证书。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `FixedPDECRefinementNoCycleClosed` | `true` | `true` | 固定有限签名群内 cap 细化由 Boolean algebra 秩严格上升控制，不能无限循环。 | 升层或叶子终端仍需处理。 |
| `NewLayerTowerNoUnnamedEscapeClosed` | `true` | `true` | 无限升层有熵发散 PDEC、有限截断 ColumnCRT/PDEC、熵可和 CleanKLS 或 Multiplicity/Stitching 四归宿。 | 这些归宿是命名叶子，不是终端排斥证明。 |
| `CompositeCofactorDescentClosed` | `true` | `true` | 复合 cofactor 递归以 m<P 或粗因子深度下降，不能形成无穷无名链。 | 持久进 PDEC，孤立进 sparse/SAE。 |
| `LocalSurvivorAndSAESchemaClosed` | `true` | `true` | early-band、short-window、point-load 与 fixed-wheel 专属出口均已命名为 finite packet、PDEC/ColumnCRT 或 CleanKLS 回流。 | 全局 PDEC/sparse 叶子排斥未完成。 |
| `SourceLoopReimportBlocked` | `true` | `true` | 若终端包经 signed/source 路线回到 clean-core 来源，会落入已切断来源环并回到 moving-block/终端包。 | 不能把该环当证明；必须落到终端防火墙输入。 |
| `CurrentMaterializedPDECFrontierZero` | `true` | `true` | 当前已物化合法非二点 primitive PDEC 候选为零；未来 PDEC 必须提交显式 primitive schema。 | FutureExplicitPrimitivePDECSchema_if_new。 |
| `CurrentMaterializedSparseFrontierZero` | `true` | `true` | 当前 sparse/LocalSurvivor 前沿没有开放物化义务；未来 sparse 必须提交有限 packet extractor schema。 | FutureExplicitSparsePacketExtractorSchema_if_new。 |
| `TerminalDescentSchemaClosed` | `true` | `true` | 跨 PDEC/SAE/ColumnCRT/CleanKLS 的无名自回流已被下降 schema 与防火墙边界删除。 | AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode] |
| `TerminalLeafExclusionCurrentCorpusProved` | `true` | `false` | 叶子终端仍未全部排斥；当前结论只是要求它们以显式 schema 或 noncanonical 合法模式进入。 | AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode] |
| `NoncanonicalLegalClosureModeCurrentCorpusProved` | `true` | `false` | noncanonical full-S 补集仍需实际源恒等、强化实际源反原子或外部 FullS-KLS/DI-BFI 合同之一。 | NoncanonicalFullSComplementLegalClosureMode。 |
| `StrictAcyclicTerminalFamilyCurrentCorpusProved` | `true` | `false` | 终端家族不再有隐藏循环，但叶子防火墙输入尚未全部证明或接受。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode] |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 下降防火墙后仍缺终端叶子输入、高段自足尾项或外部接受、DStructure/Rankin 替代包。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode]) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode]) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode]) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`TerminalLeafFirewallInputs_OR_CanonicalLock`。

必须证明：
- 若坚持 canonical-lock，证明同集推前、有限因子图和无 noncanonical payload 残留。
- 若出现未来 PDEC 叶子，提交并排斥 FutureExplicitPrimitivePDECSchema。
- 若出现未来 sparse 叶子，提交并排斥 FutureExplicitSparsePacketExtractorSchema。
- 关闭 noncanonical full-S 合法模式：实际源恒等、强化实际源反原子，或明确接受外部 FullS-KLS/DI-BFI。
- 继续独立处理高段 Mertens/PNT 自足尾项与 DStructure/Rankin 替代包。

不能作为证明使用：
- 把无隐藏循环当作叶子终端已经排斥。
- 把当前物化前沿为零当作未来全局 family 不存在。
- 把 future schema firewall 当作 schema 内容本身。
- 把 noncanonical 外部合同写成 strict 自足证明。
- 把 DStructure/Rankin 晋级门混入终端叶子排斥。
