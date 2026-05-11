# Prime Matrix strict source-admission 分支吸收路由器

**状态：** `strict_source_admission_absorbed_as_branch_statement_moving_atom_open`

`A1CleanBranchCanonicalSourceAdmission` 继续下压后不是一个能独立排斥全局反例的终端原子。既有 A1 canonical branch admission 路由已经把它化为分支陈述：canonical RIW/Buchstab 分支由内部链条闭合，generic/noncanonical 分支必须外部化或回流。因此把它放在 strict 终端 OR 中会过强；本步将它吸收为分支边界纪律，并把当前 strict 活动终端从三选一压成 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion`。这不是命题闭合；moving atom 排斥和 canonical-lock 仍未证明。

```text
source_admission_reduced_to_branch_statement=true
canonical_branch_self_contained_closed_with_scope=true
source_admission_standalone_global_contradiction=false
source_admission_absorbed_from_active_or=true
moving_atom_unique_noncanonical_strict_leaf=true
actual_noncanonical_clean_core_moving_atom_exclusion_proved=false
acyclic_terminal_canonical_lock_proved=false
row_column_unconditional_closed=false
strict_self_contained_terminal_after_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion
```

## 1. 吸收链

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR A1CleanBranchCanonicalSourceAdmission
OR ActualNoncanonicalCleanCoreMovingAtomExclusion

A1CleanBranchCanonicalSourceAdmission
  -> A1CanonicalSourceBranchStatementAndCoverage
  -> canonical branch closed with scope; generic branch still external/noncanonical
  -> not a standalone global contradiction

therefore active strict terminal:
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR ActualNoncanonicalCleanCoreMovingAtomExclusion
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TripleTerminalInputActive` | `true` | `false` | 上一层把 strict 终端写成 canonical-lock、A1 源准入或 moving-atom 排斥三选一。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `A1SourceAdmissionReducedToBranchStatement` | `true` | `true` | A1CleanBranchCanonicalSourceAdmission 已被既有路由压成 canonical 内部分支与 generic 外部分支的陈述覆盖合同。 | A1CanonicalSourceBranchStatementAndCoverage |
| `CanonicalBranchSelfContainedClosedWithScope` | `true` | `true` | canonical RIW/Buchstab source branch 的内部链条已经闭合，但陈述边界限定在 canonical-source 分支。 | 不覆盖 unrestricted generic/noncanonical complement。 |
| `A1SourceAdmissionNotStandaloneGlobalContradiction` | `true` | `true` | 该准入只说明 canonical 分支可内部处理；若反例落在 noncanonical 分支，仍需 moving-atom 排斥或外部谱线。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `OROverclaimRemoved` | `true` | `true` | 把 A1CleanBranchCanonicalSourceAdmission 作为独立 OR 终端会把分支陈述误当全局排斥，因此从活动 OR 中吸收掉。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `CanonicalLockStillStrongerParallelRoute` | `true` | `false` | canonical-lock 仍保留，因为它要求 acyclic terminal 证书同集推前且无 noncanonical payload，强于单纯 A1 分支陈述。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `MovingAtomNowUniqueNoncanonicalStrictLeaf` | `true` | `false` | 删除分支陈述伪终端后，strict noncanonical 活动叶子只剩 actual clean-core moving atom 排斥。 | ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 仍缺 canonical-lock 或 moving-atom 排斥、高段自足尾项或外部接受、DStructure/Rankin 替代包。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

严格自足基更新为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

条件外部线可写为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion OR AcceptOrProveExactFullS-KLS-ext) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualNoncanonicalCleanCoreMovingAtomExclusion) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`ActualNoncanonicalCleanCoreMovingAtomExclusion_OR_AcyclicTerminalCanonicalLock`。

必须证明：
- 若走 noncanonical 主线，证明 actual clean-core 容量测度没有 moving same-(u,v) 大原子。
- 若走 canonical-lock 备用线，证明 acyclic terminal 证书同集推前且 canonical 投影后无 noncanonical payload。
- 继续把 A1 canonical 分支陈述作为边界纪律使用，不再把它当独立全局排斥原子。
- 保留外部 FullS-KLS 为条件线，保留高段 Mertens/PNT 与 DStructure/Rankin 为独立门。

不能作为证明使用：
- 把 canonical-source 分支闭合写成 unrestricted global 闭合。
- 把 A1CleanBranchCanonicalSourceAdmission 作为单独 OR 关闭全局反例。
- 用后验覆盖图或数值缺席生成 pre-Cauchy source。
- 用 formal WFD/Type/Fourier/K4/K6 推出 moving-atom 排斥。
- 把外部 FullS-KLS 条件线写成 strict 自足闭合。
