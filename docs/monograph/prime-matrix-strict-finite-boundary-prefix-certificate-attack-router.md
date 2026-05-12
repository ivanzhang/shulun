# Prime Matrix strict 有限边界 prefix 证书攻坚路由器

**状态：** `finite_boundary_prefix_split_to_range_window_runner_tail_bridge_open`

`FiniteBoundaryPrefixRoughCountCertificate` 不能再被当作一个无结构的缺 hash 标签。它必须拆成四个可审查字段：有限区间与参数 manifest、同参数 prefix 窗口、可复现 runner/hash 清单、以及解析尾段到有限边界的单调桥接。当前材料尚未给出这些字段，因此本步没有闭合 D0；下一最窄点是 `FiniteBoundaryPrefixRangeAndParameterManifest`。

```text
finite_boundary_prefix_target_imported=true
rough_count_formula_available=true
candidate_parameter_row_available=true
finite_boundary_hash_present=false
boundary_range_manifest_present=false
same_parameter_window_locked=false
analytic_tail_bridge_present=false
finite_boundary_prefix_certificate_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 原子拆分

```text
FiniteBoundaryPrefixRoughCountCertificate
  =>
FiniteBoundaryPrefixRangeAndParameterManifest AND SameParameterPrefixWindowSpecification AND ReproduciblePrefixRoughCountRunnerHashLedger AND AnalyticTailToFiniteBoundaryMonotoneBridge
```

| component | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FiniteBoundaryPrefixRangeAndParameterManifest` | `false` | `false` | 明确有限边界覆盖的 P 区间、素数枚举边界、alpha/z/D/Lambda 与同参数 id。 | FiniteBoundaryPrefixRangeAndParameterManifest |
| `SameParameterPrefixWindowSpecification` | `false` | `false` | 把 D0 prefix lower bound、M# 势和 terminal budget 使用的 z,D,Lambda 锁成同一窗口。 | SameParameterPrefixWindowSpecification |
| `ReproduciblePrefixRoughCountRunnerHashLedger` | `false` | `false` | 提供可复现 runner、输入清单、输出摘要和 hash，证明有限区间内每个 P 的 prefix 粗筛余下界。 | ReproduciblePrefixRoughCountRunnerHashLedger |
| `AnalyticTailToFiniteBoundaryMonotoneBridge` | `false` | `false` | 证明有限 runner 终点之后由解析 B3/rough-count 下界接管，且没有参数换轨。 | AnalyticTailToFiniteBoundaryMonotoneBridge |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FiniteBoundaryPrefixTargetImported` | `true` | `false` | 最新强制负载前沿已把下一主攻点同步为有限边界 prefix 证书。 | FiniteBoundaryPrefixRoughCountCertificate |
| `RoughCountFormulaAvailable` | `true` | `true` | prefix 粗筛余公式已化为 lower weights 主项减边界项；有限证书只负责剩余边界区间。 | FiniteBoundaryPrefixRoughCountCertificate |
| `CandidateParameterRowAvailable` | `true` | `false` | 候选同参数行已可命名，但 D0/E0/U0 与 finite hash 未填入。 | fill D0/E0/U0/hash |
| `FiniteBoundaryHashPresent` | `false` | `false` | 当前没有可复核 finite boundary hash；因此不能把渐近余量升级为全局 D0。 | ReproduciblePrefixRoughCountRunnerHashLedger |
| `BoundaryRangeManifestPresent` | `false` | `false` | 当前语料没有明确 finite runner 应覆盖的闭区间、阈值来源和参数锁定清单。 | FiniteBoundaryPrefixRangeAndParameterManifest |
| `SameParameterWindowLocked` | `false` | `false` | finite prefix 不能单独跑；必须与终端预算中的 z,D,Lambda、row-free type alphabet 同步。 | SameParameterPrefixWindowSpecification AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse |
| `AnalyticTailBridgePresent` | `false` | `false` | 即使有限 runner 给出 hash，还需证明 runner 终点以后由解析尾段无缝接管。 | AnalyticTailToFiniteBoundaryMonotoneBridge |
| `FiniteBoundaryPrefixCertificateProved` | `false` | `false` | 有限边界 prefix 证书已被拆成四个字段，但当前四项均未同时完成。 | FiniteBoundaryPrefixRangeAndParameterManifest AND SameParameterPrefixWindowSpecification AND ReproduciblePrefixRoughCountRunnerHashLedger AND AnalyticTailToFiniteBoundaryMonotoneBridge |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只是把 finite prefix 原子拆细；命名回流、moving atom 和 DStructure 仍未闭合。 | FiniteBoundaryPrefixRoughCountCertificate AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最窄点

```text
FiniteBoundaryPrefixRangeAndParameterManifest
```

并行保留：

```text
SameParameterPrefixWindowSpecification AND ReproduciblePrefixRoughCountRunnerHashLedger AND AnalyticTailToFiniteBoundaryMonotoneBridge AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本步没有运行有限验证，也没有把 runner 缺口写成证明；它只把 finite prefix 证书拆成下一轮可生成和可审查的最小字段。
