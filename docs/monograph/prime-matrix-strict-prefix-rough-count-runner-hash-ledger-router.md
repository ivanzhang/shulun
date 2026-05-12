# Prime Matrix strict prefix rough-count runner/hash 账本路由器

**状态：** `prefix_rough_count_runner_hash_ledger_closed_analytic_tail_bridge_open`

`ReproduciblePrefixRoughCountRunnerHashLedger` 可关闭为可复核 hash 账本：runner 脚本、输入 prime/alpha 参数、输出 JSON/MD 与 3001<=P<100000 finite subset 指标均已登记，且 dynamic skeleton 路由器引用的 JSON hash 与当前文件一致。本步没有重新执行全量 replay，也不证明 P>=100000 解析尾桥，因此 finite prefix 证书尚未闭合。

```text
reproducible_prefix_rough_count_runner_hash_ledger_proved=true
runner_full_replay_executed=false
analytic_tail_bridge_proved=false
finite_boundary_prefix_certificate_proved=false
row_column_unconditional_closed=false
```

## 1. Hash Ledger

| item | sha256 |
| --- | --- |
| `runner_script_sha256` | `421b0b560766b74e466352a6d28b340382495b48d28ec123aca72cd2d66c8ebb` |
| `runner_json_sha256` | `bcf59b855586af801870feaec670c9adf1a498e72a51ae0bcdd25f83d90570d9` |
| `runner_md_sha256` | `2f969b929575670054ac5cdf28a641555fcf294f0bf73cb4c00e00b3c8e649ce` |
| `runner_parameters_sha256` | `5ec0916fcd5d8f6bdce1e0e3f53fe54563e54e0cfe290746746b71d17b2ba72b` |
| `finite_subset_metrics_sha256` | `edfc244e94025a5aec52786ae1268ec2e360bd036546ba766f7ea42d785a7f83` |

## 2. Finite Subset Metrics

| metric | value |
| --- | ---: |
| `all_prime_count` | 9587 |
| `all_record_count` | 19174 |
| `all_prime_min` | 13 |
| `all_prime_max` | 99991 |
| `finite_prime_count` | 9162 |
| `finite_record_count` | 18324 |
| `finite_prime_min` | 3001 |
| `finite_prime_max` | 99991 |
| `finite_min_skeleton_count` | 456 |
| `target_s` | 401 |
| `finite_two_sides_per_prime` | `true` |
| `finite_all_records_pass_target` | `true` |

Worst finite record:

```json
{
  "cutoff": 31,
  "low_prime_count": 11,
  "p": 3023,
  "side": "plus",
  "skeleton_count": 456
}
```

## 3. Replay Contract

| field | value |
| --- | --- |
| `script` | experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py |
| `alpha_argument` | 0.43 |
| `prime_list_source` | docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json:parameters.primes |
| `out_prefix` | docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506 |
| `canonical_replay_command` | python3 experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py --primes "$(jq -r '.parameters.primes\|join(",")' docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json)" --alphas 0.43 --out-prefix docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506 |
| `full_replay_executed_in_this_router` | False |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RunnerTargetImported` | `true` | `false` | 上一层已把同参数窗口后的 finite prefix 首字段定为 runner/hash 账本。 | ReproduciblePrefixRoughCountRunnerHashLedger |
| `RunnerArtifactPresent` | `true` | `true` | runner 脚本、JSON 输出和 Markdown 摘要均在仓库中。 | artifact hash ledger |
| `ParameterVectorPinned` | `true` | `true` | 输出文件内置完整 prime list 与 alpha=0.43；有限桥使用其 3001<=P<100000 子区间。 | canonical replay command can be derived from JSON parameters. |
| `FiniteBridgeSubsetMetricsMatch` | `true` | `true` | 从 runner JSON 复算出的 finite subset 指标与 dynamic skeleton 路由器登记值一致。 | analytic monotone bridge still separate. |
| `FiniteTargetPass` | `true` | `true` | 3001<=P<100000 每个素数两侧均有记录，且 skeleton_count>=401。 | does not cover P>=100000 tail by itself. |
| `HashLedgerMatchesImportedSource` | `true` | `true` | dynamic skeleton 路由器登记的 runner JSON hash 与当前文件 hash 一致。 | full replay not executed in this router. |
| `ReproducibleRunnerHashLedgerClosed` | `true` | `true` | 脚本 hash、输入参数 hash、输出 JSON/MD hash 和有限子区间指标已形成可复核账本。 | AnalyticTailToFiniteBoundaryMonotoneBridge |
| `FiniteBoundaryPrefixCertificateProved` | `false` | `false` | runner/hash 只覆盖可复核计算账本；解析尾桥、类型阈值和最终正余量仍未闭合。 | AnalyticTailToFiniteBoundaryMonotoneBridge AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse |

## 5. 下一最窄点

```text
AnalyticTailToFiniteBoundaryMonotoneBridge
```

并行保留：

```text
FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本步是 hash/replay 账本，不是全量重跑证明，也不是解析尾段桥。
