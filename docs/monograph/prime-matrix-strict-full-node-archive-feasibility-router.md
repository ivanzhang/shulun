# Prime Matrix strict 完整 psi 节点归档可行性路由器

**状态：** `full_archive_single_node_recompute_rejected_incremental_or_external_archive_open`

完整节点归档的最窄点进一步明确：当前原生 range runner 仍是逐节点重算。目标首节点约 56.39 秒，外推 646258 个节点约 421.8 天，因此不能作为现实闭合路线。下一步必须写真正增量/分段的 range 算法，或导入外部完整节点归档并验收 hash。

```text
timing_sample_present=true
native_range_psi_theta_batch_executable_closed=true
single_node_recompute_archive_route_rejected=true
full_node_archive_completeness_and_hash_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 成本画像

```text
expected_node_count=6.462580000000000e+05
observed_seconds_per_node=5.639000000000000e+01
estimated_total_seconds=3.644248862000000e+07
estimated_total_hours=1.012291350555555e+04
estimated_total_days=4.217880627314814e+02
single_node_recompute_full_archive_practical=false
```

## 2. 剩余替换

```text
FullNodeArchiveCompletenessAndHashLedger
  =>
DeltaAwareIncrementalPsiRangeAlgorithmLedger OR ExternalPrecomputedPsiNodeArchiveWithHashLedger

MachineReadableNodeArchiveLedger
  =>
FullNodeArchiveCompletenessAndHashLedger AND audit pass

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计节点归档生成可行性，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `TimingSampleLedger` | `true` | `true` | 原生 range runner 的目标首节点计时样本已经取得。 | single-node timing only |
| `SingleNodeRecomputeArchiveRouteRejected` | `true` | `true` | 按当前逐节点重算速度，完整 646258 节点归档估计需要数百天，不能作为现实闭合路线。 | DeltaAwareIncrementalPsiRangeAlgorithmLedger OR ExternalPrecomputedPsiNodeArchiveWithHashLedger |
| `DeltaAwareIncrementalPsiRangeAlgorithmLedger` | `false` | `false` | 需要真正利用相邻 x_i=x_0+i h 的增量结构，避免每个节点从零重算 psi。 | incremental segmented prime-power update or library-level range API |
| `ExternalPrecomputedPsiNodeArchiveWithHashLedger` | `false` | `false` | 或者导入外部已经计算完成的全节点归档，并用现有 audit 脚本验收。 | external full JSONL archive and hash |
| `FullNodeArchiveCompletenessAndHashLedger` | `false` | `false` | 完整节点表尚未存在；当前逐节点重算方案被成本审计排除。 | DeltaAwareIncrementalPsiRangeAlgorithmLedger OR ExternalPrecomputedPsiNodeArchiveWithHashLedger |
| `MachineReadableNodeArchiveLedger` | `false` | `false` | 完整归档/hash 未闭合时，机器可读节点归档仍不能升级。 | FullNodeArchiveCompletenessAndHashLedger |
| `MiddlePsiFineMeshNodeSlackFloorAndHashLedger` | `false` | `false` | 节点表未闭合时，节点余量/hash 守门仍开放。 | FullNodeArchiveCompletenessAndHashLedger AND SourceAlgorithmToDusartConventionMatch |
| `RowColumnUnconditionalClosed` | `false` | `false` | 完整归档可行性审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
DeltaAwareIncrementalPsiRangeAlgorithmLedger
```
