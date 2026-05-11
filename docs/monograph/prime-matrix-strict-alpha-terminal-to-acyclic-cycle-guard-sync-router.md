# Prime Matrix strict alpha 终端到 acyclic 循环守卫同步路由器

**状态：** `strict_alpha_terminal_synced_to_acyclic_cycle_guard_open`

本步把本轮 alpha 局部闭合后的 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 接回 strict acyclic 终端循环守卫。结论是：direct PDEC / direct CleanKLS 裸路线会自回流，不能当作闭合；当前真正最窄点是 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate`，并行备用为 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`。仍未发现终端直接矛盾，行/列命题不能宣称无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
counterexample_assumption_only=true
alpha_terminal_to_acyclic_cycle_guard_sync_router_closed=true
raw_direct_pdec_clean_routes_count_as_closure=false
acyclic_terminal_canonical_lock_proved=false
acyclic_noncanonical_terminal_return_well_founded_descent_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 自回流链

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily -> DirectAcyclicSameSetPDECCapDualCertificate
DirectAcyclicSameSetPDECCapDualCertificate -> AcyclicFiniteArcCapMassBoundsOrNamedReturn
AcyclicFiniteArcCapMassBoundsOrNamedReturn -> DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
DirectAcyclicCleanKLSDLSEstimateWithNamedReturn -> AcyclicWindowedKloostermanDLSInternalEstimate
AcyclicWindowedKloostermanDLSInternalEstimate -> SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks -> AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom -> GlobalPDECorSparseTerminalExclusion
GlobalPDECorSparseTerminalExclusion -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```

## 2. 同步律

Once the alpha local frontier has returned to PDEC-CAP/CleanKLS, the direct terminal labels do not give a proof. Direct PDEC routes to finite arcs and then clean KLS; direct clean KLS routes through windowed DLS, Kuznetsov/NC-BLK and back to the global terminal family. Therefore the strict acyclic terminal family can only advance by an actual canonical-lock certificate or by a well-founded descent measure that strictly decreases across every named terminal return.

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本同步仍只整理早期零行反例链中的终端路线，不用真实样本缺席或当前物化前沿清零替代全局证明。 | row_column_unconditional_closed=false。 |
| `AlphaLocalFrontierReachedGlobalTerminal` | `true` | `false` | alpha row formula 局部前沿已清完，下一目标进入全局 PDEC-CAP / internal CleanKLS 终端门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `StrictScopeRequiresAcyclicTerminalFamily` | `true` | `false` | canonical-source 终端晋级不能直接导入 strict noncanonical；必须使用 acyclic terminal family 口径。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `AcyclicTerminalCycleGuardImported` | `true` | `false` | 裸 direct PDEC 与裸 direct CleanKLS 路线已经识别为自回流，不能作为证明进展量。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `DirectPDECNotProgressMeasure` | `true` | `false` | direct acyclic same-set PDEC 只完成作用域审查；若要复用 canonical same-set，必须先证明 canonical-lock。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `DirectCleanNotProgressMeasure` | `true` | `false` | direct clean residual 被压到 windowed DLS/Kuznetsov 大筛原子，但该原子继续接回 NC-BLK/终端家族。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `CanonicalLockScopedOnly` | `true` | `false` | canonical-lock 若五项 exact same-set 证书齐备，只是 scoped canonical case；缺证书时不能调用。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `PriorDescentReturnedThroughAlphaFormula` | `true` | `false` | 上一轮 well-founded descent 下钻已进入逐点核表和 alpha formula；本轮已把 alpha 局部前沿同步回终端门。 | 需要真正下降量，而不是再次走同一路由。 |
| `TerminalCycleSyncClosed` | `true` | `false` | 当前 PDEC/CleanKLS 终端门已压成 canonical-lock 精确证书或非循环严格下降证书；裸终端标签删除。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `false` | `false` | 尚未证明 canonical-lock 五项证书，也未提交跨 PDEC/SAE/ColumnCRT/CleanKLS 回流的下降复杂度。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一主攻点

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
```

并行保留：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```
