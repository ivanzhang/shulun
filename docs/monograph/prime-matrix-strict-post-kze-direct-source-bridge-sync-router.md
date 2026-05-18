# Prime Matrix strict post-KZ-E direct source-bridge 同步证书

**状态：** `post_kze_direct_no_projection_reduced_to_actual_source_admission_open`

本步继续攻击 KZ-E direct no-projection 门。既有 KZ-E spine 的泛 WFD 自足路线已经被分类：canonical-restricted 分支可闭合，unrestricted generic 分支被 moving-delta 反证，外部 generic 合同只能作为条件线。由于当前 no-cycle 门禁止经 NC-BLK/source-root 投影，noncanonical moving-atom/anti-atom 回流不能计入 KZ-E 直接谱证明。因此，若不接受外部 no-projection DI/BFI/Kuznetsov 证书，内部剩余压成一个具体 source bridge：在 Cauchy/dispersion 前证明当前 clean A1 反例分支准入 canonical RIW/Buchstab source。高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合，行/列命题仍未无条件闭合。

```text
kze_direct_no_projection_gate_active=true
self_contained_taxonomy_imported=true
canonical_provenance_closed_only_for_canonical_branch=true
source_lock_scoped_not_global=true
actual_source_bridge_obstruction_imported=true
noncanonical_moving_atom_not_kz_nocycle_proof=true
kze_direct_current_internal_route_reduced_to_source_admission=true
a1_clean_branch_canonical_source_admission_proved=false
exact_external_dibfi_kuznetsov_no_projection_certificate_accepted=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `KZEDirectNoProjectionGateActive` | `true` | `false` | 上一轮已经把非循环 KZ/DLS 压成不得经 NC-BLK 投影的 KZ-E 直接 dispersion log-saving。 | AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection |
| `KZESpineStillGenericWFD` | `true` | `false` | KZ-E spine 的自足深核仍是 generic/full-S WFD；其完全自足旧路最终触及 NC-BLK 或外部 DI/BFI。 | actual-source bridge or external no-projection theorem |
| `SelfContainedTaxonomyImported` | `true` | `true` | 外部 generic 合同版闭合、canonical-restricted 自足版闭合、unrestricted generic 自足版被 moving-delta 反证。 | ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput |
| `CanonicalProvenanceClosedOnlyForCanonicalBranch` | `true` | `true` | canonical 分支中 pre-Cauchy lambda_c 可定义为 RIW/Buchstab 决策树系数；这不是 generic 分支闭合。 | A1CleanBranchCanonicalSourceAdmission |
| `SourceLockScopedNotGlobal` | `true` | `false` | source-lock 合同只在证明当前 clean A1 分支准入 canonical source 后可用，不能从下游覆盖图反推。 | A1CleanBranchCanonicalSourceAdmission |
| `BranchStatementCoverageImported` | `true` | `true` | canonical branch 与 generic complement 的覆盖陈述已闭合；generic complement 只能外部化或回流。 | generic complement external/PDEC-SAE route |
| `ActualSourceBridgeObstructionImported` | `true` | `false` | actual-source bridge 已压到 source admission 或 noncanonical moving atom exclusion；二者当前均未证明。 | A1CleanBranchCanonicalSourceAdmission OR ActualNoncanonicalCleanCoreMovingAtomExclusion |
| `NoncanonicalMovingAtomNotKZNoCycleProof` | `true` | `true` | noncanonical moving atom/anti-atom 线会回到终端回流链；它不是当前 KZ no-cycle gate 的直接谱证明。 | terminal return, not KZ-E direct log-saving |
| `CanonicalBridgeNotGlobalUnrestricted` | `true` | `true` | actual-source bridge 只在 canonical 分支吸收；不能升级成完整 unrestricted/global 无条件闭合。 | noncanonical complement anti-atom or external DI/BFI |
| `KZEDirectCurrentInternalRouteReducedToSourceAdmission` | `true` | `false` | 若不走外部 no-projection 定理，KZ-E direct no-NCBLK 门的内部路线只剩 actual clean branch canonical admission。 | A1CleanBranchCanonicalSourceAdmission |
| `ExternalNoProjectionStillConditional` | `true` | `false` | 外部 DI/BFI/Kuznetsov no-projection 可作为条件输入，但不能作为 strict 自足证明写入。 | ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 KZ-E direct 门压到 actual source admission；没有产生无条件终端矛盾。 | A1CleanBranchCanonicalSourceAdmission AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 最新内部非循环基

```text
A1CleanBranchCanonicalSourceAdmission AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件外部线：

```text
(A1CleanBranchCanonicalSourceAdmission OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
A1CleanBranchCanonicalSourceAdmission
```

## 3. 诚实边界

- 本证书不证明 source admission，也不证明外部 no-projection 定理。
- canonical 分支闭合只在源头已锁定为 RIW/Buchstab 时可用，不能偷渡到 generic/noncanonical 分支。
- noncanonical moving-atom/anti-atom 回流不是当前 KZ no-cycle gate 的直接谱证明。
- 高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_post_kze_direct_source_bridge_sync_router.py` | `b0e8dc640166b052fc0b61e1431cec014d83c6e7040c1d862c9118b34c7e13e8` |
| `docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json` | `daf08ea0d88fb2c0729398c4a59702b9a59e46efb38aae7fe9e2f369e99633d6` |
| `docs/monograph/prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md` | `77c5833ef537dd1855744997c11810c25857ff27cfc31f2c4ce0763afb130a26` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json` | `c17dfbff54f991a819fcaa607f001860adcc8e3f950de77c233c4dff834227ad` |
| `docs/monograph/prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json` | `0f222c5ddb147aab3039cefc58a57015d3a89cc14fbf89287ed735971273ad0d` |
| `docs/monograph/prime-matrix-triad-a1-source-lock-contract-router.json` | `039a29ac39132bbd6023352a51712e0c079efe7a1ad326fa19f511c4a9a55dee` |
| `docs/monograph/prime-matrix-triad-a1-branch-statement-coverage-router.json` | `570acc92351eb91ab4005f64e028fad0cddddc29e9a935b9f4043ef6aaab4234` |
| `docs/monograph/prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json` | `a8d5e1712a81352db9bec901a6e1fdfbb6135b745872c6855f43567e892a77b7` |
| `docs/monograph/prime-matrix-actual-source-bridge-global-reconciliation-router.json` | `4d5c17126ea796ee37ae469a3684ef634899dfea0b4af3352c3bf29d0f874e59` |
| `docs/monograph/prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json` | `fcbc9c954360a067c00bb161118936041aaeed458841a5162fd199bbb04e2b92` |
