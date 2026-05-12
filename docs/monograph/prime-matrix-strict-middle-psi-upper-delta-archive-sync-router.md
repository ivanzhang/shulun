# Prime Matrix strict 中段 psi 上界 delta-aware 归档同步证书

**状态：** `middle_psi_upper_100002841_closed_by_delta_aware_full_archive_table_algorithm_still_open`

中段 `psi(x)<1.00002841x` 的来源/覆盖账本已由最新 delta-aware 完整归档同步关闭：完整 646258 节点表存在，hash 与证书一致，节点数、连续性和余量审计通过。这回收了旧 machine-readable archive 证书中的开放状态。但这只关闭中段上界分支；整个 Schoenfeld/Dusart epsilon 表算法仍需 Table 6.3、Table 6.4、零点输入绑定、区间传播与可复现 hash。

```text
middle_psi_upper_100002841_source_closed=true
middle_finite_interval_psi_cover_closed=true
middle_psi_fine_mesh_node_slack_floor_hash_closed=true
machine_readable_node_archive_closed=true
psi_epsilon_table_algorithm_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 归档摘要

| field | value |
| --- | --- |
| `path` | `/opt/code/shulun/data/middle-psi-fine-mesh-node-table.jsonl` |
| `sha256` | `41742cf17b4d62730bb486bb3e368788b03a729d4125e88fa6b06d04af69ad02` |
| `node_count` | `646258` |
| `expected_node_count` | `646258` |
| `min_slack` | `22569065.07008830` |
| `required_node_slack_floor` | `3073386.85452651` |
| `error_count` | `0` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MiddlePsiUpperTargetActive` | `true` | `true` | psi epsilon 表算法把当前最窄点设为中段 1.00002841 的来源/覆盖账本。 | MiddlePsiUpper100002841SourceLedger |
| `UpstreamReductionChainRecognized` | `true` | `true` | 中段上界已沿 source -> finite cover -> fine mesh -> node data -> machine archive 链条传递。 | FullDeltaAwarePsiNodeArchiveRunAndHashLedger |
| `OldMachineArchiveCertificatesStaleOpen` | `true` | `true` | 旧 machine/full-node 证书记录的是完整归档生成前状态，需要由 delta-aware 证书覆盖同步。 | use newest delta-aware archive certificate |
| `DeltaAwareFullArchiveClosed` | `true` | `true` | delta-aware 分段增量算法已生成完整 646258 节点归档，并通过 hash/连续性/余量审计。 | closed |
| `ArchiveHashRegistered` | `true` | `true` | 完整节点表文件存在，且证书 hash 与实际文件 hash 一致。 | 41742cf17b4d62730bb486bb3e368788b03a729d4125e88fa6b06d04af69ad02 |
| `MiddleFineMeshNodeSlackClosed` | `true` | `true` | 节点余量下界已由完整归档关闭，因此中段 fine mesh/hash 守门关闭。 | MiddlePsiFineMeshNodeSlackFloorAndHashLedger |
| `MiddleFiniteIntervalPsiCoverClosed` | `true` | `true` | 细网格覆盖路线关闭后，8e11 到 e^28 的中段 psi 覆盖闭合。 | MiddleFiniteIntervalPsiCover8e11ToE28Ledger |
| `MiddlePsiUpper100002841SourceClosed` | `true` | `true` | 中段 psi(x)<1.00002841x 的来源/覆盖账本由 delta-aware 完整归档给出。 | MiddlePsiUpper100002841SourceLedger |
| `PsiEpsilonTableAlgorithmStillOpen` | `true` | `false` | 关闭中段上界不等于关闭整个 epsilon 表算法；Table 6.3、Table 6.4、零点输入绑定、传播与 hash 仍需合取。 | MachineReadableDusartTable63EpsilonPsiLedger AND ThetaLessThanIdentityTable64To8e11SourceLedger AND VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 中段 psi 归档不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最窄点

```text
MachineReadableDusartTable63EpsilonPsiLedger
```

