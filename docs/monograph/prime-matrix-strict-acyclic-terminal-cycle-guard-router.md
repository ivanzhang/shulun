# Prime Matrix strict acyclic 终端家族循环守卫路由器

**状态：** `strict_acyclic_terminal_family_reduced_to_canonical_lock_or_well_founded_descent_open`

本步发现并固定 strict acyclic 终端家族的真正循环障碍：裸 direct PDEC 分支已经被路由到有限弧，再到 direct clean KLS；裸 direct clean KLS 又经 windowed DLS、Kuznetsov/KZ-E、NC-BLK/moving-atom 回到 global terminal family。因此不能再把 direct PDEC 或 direct CleanKLS 的标签本身当作进展。固定有限签名群内的 PDEC no-cycle 只防止同层无限细分，不足以排斥跨层回流。最新最窄剩余压成：证明 acyclic terminal canonical-lock，或提交跨 PDEC/SAE/ColumnCRT/CleanKLS 回流的 well-founded 严格下降证书。行/列命题仍未无条件闭合。

```text
counterexample_assumption_only=true
terminal_family_self_return_detected=true
direct_pdec_raw_route_self_return_detected=true
direct_clean_raw_route_self_return_detected=true
fixed_level_pdec_no_cycle_imported=true
fixed_level_no_cycle_sufficient_for_global_terminal_family=false
raw_direct_pdec_clean_routes_count_as_closure=false
acyclic_terminal_canonical_lock_proved=false
acyclic_terminal_return_well_founded_descent_proved=false
strict_acyclic_terminal_family_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
```

## 1. 自回流链

```text
F := PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily

F
  -> DirectAcyclicSameSetPDECCapDualCertificate
  -> AcyclicFiniteArcCapMassBoundsOrNamedReturn
  -> DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
  -> AcyclicWindowedKloostermanDLSInternalEstimate
  -> SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
  -> AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
  -> GlobalPDECorSparseTerminalExclusion
  -> F
```

该链条只有在附带严格下降量时才是证明；否则只是循环路由。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AcyclicTerminalFamilyActiveAfterSeedFusion` | `true` | `false` | seed 融合后，当前唯一数学终端门是 acyclic noncanonical PDEC-CAP 或内部 CleanKLS。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `ThreeAtomSplitImported` | `true` | `true` | 终端家族已拆成 canonical-lock、direct PDEC、direct clean KLS 三个入口。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `DirectPDECRouteSelfReturnDetected` | `true` | `true` | direct PDEC 的同集输入和 dual-cap 定位闭合后，有限弧高质量若不命名回流就进入 direct clean KLS。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn。 |
| `DirectCleanRouteSelfReturnDetected` | `true` | `true` | direct clean KLS 经 windowed DLS、KZ-E、NC-BLK/moving-atom 后又接回 global terminal family。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `RawDirectEstimatesNotProgressMeasure` | `true` | `true` | 裸 direct PDEC 或裸 direct clean KLS 标签会形成 F -> ... -> F 的证明循环，不能作为闭合证明。 | 必须给出严格下降量或 canonical-lock。 |
| `FixedLevelPDECNoCycleImported` | `true` | `true` | 固定有限签名群内的 PDEC cap 细化无循环已可用。 | 该事实只防止同一有限层无限细分。 |
| `FixedLevelNoCycleInsufficientGlobally` | `true` | `true` | strict 终端家族回流允许换层、new-layer、CleanKLS 和 global terminal scope；固定层无循环不足以排斥全局自回流。 | 需要跨回流的 well-founded descent certificate。 |
| `CanonicalLockStillLegalExit` | `true` | `false` | 若能证明全部 acyclic terminal certificates canonical-lock 到 canonical-source 边界，则可复用 canonical 闭合。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary。 |
| `WellFoundedDescentGuardPinned` | `true` | `false` | 不走 canonical-lock 时，必须给每次 PDEC/SAE/ColumnCRT/CleanKLS 回流赋予严格下降的有限复杂度。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate。 |
| `TerminalCycleGuardReduced` | `true` | `false` | 三原子终端门已压成 canonical-lock 或非循环下降证书；裸 direct PDEC/CleanKLS 不再单独计为闭合路线。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `StrictAcyclicTerminalFamilyCurrentCorpusProved` | `true` | `false` | 当前仓库尚未证明 canonical-lock，也未提交跨回流的严格下降量。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | 终端循环守卫后仍缺 canonical-lock/下降证书、高段自足尾项或外部接受、DStructure/Rankin 替代包。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate_OR_CanonicalLock`。

必须证明：
- 定义每个 acyclic terminal record 的有限复杂度向量，例如 formal-unit level、未结坏窗数、签名秩、payload 维度、回流深度。
- 证明 PDEC/SAE/ColumnCRT/CleanKLS 每次命名回流在字典序上严格下降，或进入已封闭 canonical boundary。
- 证明 new-layer/refined PDEC 不能无限增广复杂度；若增广，则必须以更低未结质量或更小坏窗义务支付。
- 证明下降到底时只能到达已闭合的有限 packet、已排斥二点 tautology、或 canonical-source 边界。
- 若不能给下降量，则改证 AcyclicTerminalCanonicalLockToCanonicalSourceBoundary。

不能作为证明使用：
- 重复 direct PDEC -> finite arc -> clean KLS -> NC-BLK -> terminal family 的自回流链。
- 把固定有限签名群 no-cycle 当作跨层全局 no-cycle。
- 把当前已物化有限塔证据当作全局有限塔证明。
- 把 canonical-source PDEC-CAP 闭合直接导入 acyclic noncanonical 终端。
- 把外部 DI/BFI/Kuznetsov 写成严格自足终端家族证明。
