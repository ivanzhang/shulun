# Prime Matrix strict post-new-joint KZ 非循环门同步证书

**状态：** `post_new_joint_kz_nocycle_gate_reduced_to_kze_direct_log_saving_open`

本步继续攻击 post-new-joint 后的非循环 KZ/DLS 门。既有 windowed DLS 形式层和 KZ-A--KZ-D 谱脊柱已经可导入；但 KZ-E 的现有路线通过 NC-BLK/source anti-atom 获得 log-saving，而该路线又回到 source-root/terminal cycle。由于当前门名要求 `without NCBLK/source-root reuse`，这条旧路线不能计入非循环证明。故当前内部 KZ 路线已饱和，剩余被压成直接的 KZ-E well-factorable dispersion log-saving 证明，且不得经过 NC-BLK 投影；同时高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。行/列命题仍未无条件闭合。

```text
latest_kz_nocycle_gate_active=true
windowed_dls_formal_layer_imported=true
kz_abcd_spine_imported=true
existing_kz_e_route_factors_through_ncblk=true
ncblk_projection_forbidden_for_nocycle_gate=true
noncircular_kuznetsov_dls_without_source_root_reuse_proved=false
kz_e_direct_log_saving_without_ncblk_projection_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestKZNoCycleGateImported` | `true` | `false` | post-new-joint 同步后，直接主攻点是不得复用 NCBLK/source-root 的非循环 KZ/DLS。 | NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse |
| `WindowedDLSFormalLayerImported` | `true` | `true` | windowed DLS 的对象、相位、L2 范数和失败字母表已压尽，剩 KZ/DLS 谱原子。 | SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `KZABCDSpineImported` | `true` | `true` | KZ-A 平滑、KZ-B trace formula、KZ-C Bessel 衰减、KZ-D 谱大筛脊柱已由既有证书关闭。 | KZ-E well-factorable dispersion log-saving |
| `ExistingKZERouteFactorsThroughNCBLK` | `true` | `false` | 既有 KZ-E 路线把 log-saving 压到 NC-BLK/source anti-atom；这不是独立非循环谱证明。 | AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom |
| `NCBLKProjectionForbiddenForNoCycleGate` | `true` | `true` | 当前门名已经禁止复用 NCBLK/source-root；因此经 NC-BLK/source-root 的 KZ-E 证明不能计入本门闭合。 | AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection |
| `NCBLKReturnToTerminalImported` | `true` | `true` | NC-BLK/source anti-atom 若失败，会物化为 moving atom 并回到 GlobalPDEC/sparse 终端与模型账本。 | GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger |
| `TerminalCycleGuardImported` | `true` | `true` | 裸 direct PDEC 与 direct CleanKLS 终端路线已识别为自回流，不能作为进展量。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `ExistingKZTerminalSyncImported` | `true` | `false` | 直接沿现有 KZ/DLS 下钻只回到 strict acyclic 终端家族和模型余量账本。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `StrictGlobalTerminalScopeStillOpen` | `true` | `false` | canonical-source 终端闭合不能直接导入 acyclic noncanonical seed。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `NonCircularKZCurrentInternalRouteSaturated` | `true` | `false` | 当前内部 KZ/DLS 旧路线不满足 no-NCBLK/source-root 限制；若要继续，必须直接证明 KZ-E log-saving。 | AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection |
| `HighModelRateDStructureStillOpen` | `true` | `false` | KZ 门之外，高段模型、RatePreservation 与 DStructure/Rankin 仍是独立开放门。 | HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把非循环 KZ 门压到 KZ-E 直接 log-saving；没有得到无条件终端矛盾。 | AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 最新内部非循环基

```text
AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件外部线：

```text
(AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection
```

## 3. 诚实边界

- 本证书不证明 KZ-E log-saving，也不证明非循环 KZ/DLS。
- 它只说明现有 KZ-E 经 NC-BLK/source-root 的路线不能满足 no-cycle 门。
- 外部 DI/BFI/Kuznetsov 只能作为条件输入，不能冒充严格自足闭合。
- 高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_post_new_joint_kz_nocycle_gate_sync_router.py` | `50be914b8e41e9fe1682807a8644bb1c878b73f958ca081b6bfcf4ab1066aa0a` |
| `docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json` | `b399e75cd4c9aba64d2566b9d05f961d504cddb416a1d3f6fabb53e4126bca62` |
| `docs/monograph/prime-matrix-strict-acyclic-windowed-dls-estimate-router.json` | `89f695e1ad123d1461acb338ddf0b371ef49a266baf3b2580961148943c5f594` |
| `docs/monograph/prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json` | `fb988aea08dcdf541574fa412e2e37254570b8ad688b010a6c0366c03c4e7270` |
| `docs/monograph/prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json` | `ac1c3264c5130a87e0f43e77ad6f7c201a4a7efd7942f686e317161c2cddbfa2` |
| `docs/monograph/prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json` | `70b20d8ddca4337179a495286b7249b4ebda9790a65cede89225306711a9cb16` |
| `docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json` | `223f7e68d259298177cb2eb4afd3bc6c0f8f7c696f37633ba1cca7407ac07395` |
| `docs/monograph/prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json` | `9e04c7da91dd0ad9473fea5aefef4e5fab5b2708139c1e08cca40b9ac6c5d93e` |
| `docs/monograph/prime-matrix-strict-global-terminal-scope-router.json` | `cb8e05a82c80e38481fd3b97bd57038b21638dafbb0ba0ae97cc54dc574abd9d` |
