# Prime Matrix strict descent 叶子防火墙 alpha 回流同步路由器

**状态：** `strict_descent_leaf_firewall_alpha_return_synced_active_bridge_open`

本步直接下钻 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 的最新最窄处：下降防火墙已经删除无隐藏循环，但旧的 pointwise/alpha 展开路线会经 alpha row formula 回到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`，再被 acyclic 循环守卫送回终端家族。因此该路线只能登记为回边，不能算 well-founded descent。当前 strict 自足线的活动剩余被压成 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn`。后者要求在进入 alpha 回边前独立证明 actual-source 恒等或强化反原子。尚未发现终端直接矛盾，行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
counterexample_assumption_only=true
descent_leaf_firewall_alpha_return_sync_router_closed=true
terminal_return_well_founded_descent_schema_closed=true
old_pointwise_alpha_descent_route_reclassified_as_backedge=true
pointwise_alpha_route_counts_as_well_founded_descent=false
independent_actual_source_bridge_proved=false
acyclic_terminal_canonical_lock_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn
```

## 1. 回边链

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate -> TerminalLeafFirewallInputs_OR_CanonicalLock
TerminalLeafFirewallInputs_OR_CanonicalLock -> NoncanonicalFullSComplementLegalClosureMode_OR_CanonicalLock
NoncanonicalFullSComplementLegalClosureMode -> ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput
ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput -> NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem -> PreTerminalActualFullSFactorSupportCapacityTheorem
PreTerminalActualFullSFactorSupportCapacityTheorem -> NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource
NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource -> ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger
ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger -> PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate -> AlphaRowAnchorPhaseEmissionFormulaLedger
AlphaRowAnchorPhaseEmissionFormulaLedger -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve -> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
```

这条链说明：继续沿旧 pointwise/alpha 路线下钻，会回到同一个终端家族；它是审稿意义上的回边，不是下降量。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本同步仍只在早期零行反例链内工作，不使用真实样本缺席或数值前沿清零替代假设链证明。 | direct_unconditional_contradiction_found=false。 |
| `DescentFirewallSchemaImported` | `true` | `true` | 无隐藏终端循环已由下降防火墙 schema 删除；固定 PDEC、new-layer、cofactor 与 SAE/ColumnCRT 回流已命名。 | AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode] |
| `TerminalLeafInputsStillOpen` | `true` | `false` | 下降防火墙只关掉无名循环，不排斥叶子防火墙输入。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicTerminalLeafFirewallInputs[FutureExplicitPrimitivePDECSchema_if_new OR FutureExplicitSparsePacketExtractorSchema_if_new OR NoncanonicalFullSComplementLegalClosureMode] |
| `OldPointwiseAlphaRouteDetected` | `true` | `false` | 旧的 descent 下钻链把 actual-source/rank 包继续展开到逐点 alpha/delta 核表和 alpha row formula。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate -> AlphaRowAnchorPhaseEmissionFormulaLedger |
| `AlphaRouteReturnsToTerminal` | `true` | `false` | alpha row formula 的局部前沿已同步回 PDEC-CAP/CleanKLS，并被 acyclic 循环守卫判为终端回流。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve -> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `PointwiseAlphaRouteCannotBeProgressMeasure` | `true` | `true` | 若把旧 pointwise/alpha 展开当作 well-founded descent，它的终端又回到同一终端家族，故只能记为回边，不能记为严格下降量。 | 必须改攻叶子输入或提交新的严格下降势函数。 |
| `CurrentLeafFirewallInstanceReduced` | `true` | `true` | 当前已物化 PDEC/sparse 前沿被清到准入纪律后，活动叶子从 future schema 压到 noncanonical full-S 或 canonical-lock。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |
| `NoncanonicalModeFilteredToActualSourceBridge` | `true` | `false` | 严格自足线过滤外部 FullS-KLS 与 generic WFD 后，noncanonical 叶子压到 actual-source 锁定或强化反原子。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput |
| `CanonicalLockScopedButNotGlobal` | `true` | `false` | canonical-lock 若证书齐备只进入 scoped canonical case；证书缺失时不可调用，不能作为 unrestricted noncanonical 矛盾。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `IndependentActualSourceBridgeRequired` | `true` | `false` | actual-source 桥若继续经 exact-UV/rank/alpha 展开会回到终端；因此必须在进入 alpha 回边前独立证明源恒等或强化反原子。 | IndependentActualSourceBridgeNotFactoredThroughAlphaReturn |
| `DescentLeafAlphaReturnSyncClosed` | `true` | `false` | 本同步关闭的是路线分类：旧 alpha 下钻不再算进展；当前最窄数学输入被钉到独立 actual-source 桥或 canonical-lock。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 尚未提交独立 actual-source 桥、canonical-lock 全证书、高段自足尾项或 DStructure/Rankin 替代包。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

条件外部线可写为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab OR FullSNonAPStrengthenedSourceAntiAtomForActualSource OR AcceptOrProveExactFullS-KLS-ext) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`IndependentActualSourceBridgeNotFactoredThroughAlphaReturn`。

必须证明：
- 在进入 exact-UV/rank/alpha 回边前，证明 actual full-S non-AP 源就是 canonical RIW/Buchstab 决策树源。
- 或直接证明 actual source 的强化反原子：最终容量测度不存在 moving same-(u,v) 大原子。
- 若走 canonical-lock，并行提交 acyclic 同集推前、有限因子图和无 noncanonical payload 残留五项证书。
- 高段 Mertens/PNT 自足尾项与 DStructure/Rankin 替代包继续独立验收。

不能作为证明使用：
- 把旧 pointwise/alpha 展开当作终端下降量。
- 把 alpha 局部公式回流终端当成终端矛盾。
- 把当前 PDEC/sparse 前沿为零说成未来 family 全局不存在。
- 把 canonical scoped 分支推广成 unrestricted noncanonical 闭合。
- 把外部 FullS-KLS 合同写成 strict 自足证明。
