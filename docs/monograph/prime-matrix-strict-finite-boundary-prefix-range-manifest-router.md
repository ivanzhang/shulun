# Prime Matrix strict 有限边界 prefix 范围 manifest 路由器

**状态：** `finite_boundary_prefix_range_manifest_closed_same_parameter_window_open`

`FiniteBoundaryPrefixRangeAndParameterManifest` 已可关闭：当前同参数 D0 行固定为 `alpha043_pge100000_external_b3_pending_finite_prefix_named_return`，即 alpha=0.43、P>=100000、prefix 区间 1<=c<P；3001<=P<100000 作为已归档的动态粗骨架有限桥接边界，不混入当前 D0 runner。真正剩余转为同参数窗口规格、runner/hash 和解析尾段桥接。

```text
range_manifest_target_imported=true
candidate_parameter_id_pinned=true
pre_tail_finite_bridge_located=true
tail_object_interface_matched=true
range_and_parameter_manifest_closed=true
same_parameter_window_specification_proved=false
runner_hash_ledger_proved=false
analytic_tail_bridge_proved=false
finite_boundary_prefix_certificate_proved=false
row_column_unconditional_closed=false
```

## 1. Manifest

| field | value |
| --- | --- |
| `parameter_id` | alpha043_pge100000_external_b3_pending_finite_prefix_named_return |
| `alpha` | 0.43 |
| `s` | 2.3255813953488373 |
| `p_tail_start` | 100000 |
| `z_rule` | z=floor(P^0.43) or equivalent monotone cutoff recorded in same-parameter window |
| `sieve_level_rule` | D comparable to P, with squarefree d<P in the prefix CRT count formula |
| `prefix_interval` | 1<=c<P |
| `rough_object` | #{1<=c<P: xP+c avoids the prescribed residue class modulo each q<=z} |
| `target_lower_bound_role` | D0_prefix_lower_bound for terminal margin table |
| `finite_bridge_before_tail` | 3001<=P<100000 handled by dynamic skeleton finite certificate, not by the current D0 p>=100000 table row |

## 2. Range Rows

| range | role | status | meaning |
| --- | --- | --- | --- |
| P<3001 | outside_current_manifest | not_part_of_current_alpha043_pge100000_D0_row | 更小 P 属于旧有限桥或其它全局边界，不由本 D0 同参数行关闭。 |
| 3001<=P<100000 | pre_tail_bridge | closed_by_dynamic_skeleton_finite_certificate | 已有动态粗骨架有限桥；最小值 456，目标 401。 |
| P>=100000 | active_same_parameter_prefix_tail | manifest_closed_runner_and_tail_bridge_open | 当前 finite prefix 证书的同参数 D0 行从这里开始；需要同参数窗口、runner/hash 和解析尾段桥接。 |

## 3. 有限桥摘要

| item | value |
| --- | ---: |
| prime_min | 3001 |
| prime_max | 99991 |
| record_count | 18324 |
| prime_count | 9162 |
| min_skeleton_count | 456 |
| target_s | 401 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RangeManifestTargetImported` | `true` | `false` | 上一层已把 finite prefix 首字段定为范围与参数 manifest。 | FiniteBoundaryPrefixRangeAndParameterManifest |
| `CandidateParameterIdPinned` | `true` | `true` | 当前同参数 D0 行固定为 alpha=0.43, P>=100000。 | parameter row pinned |
| `PreTailFiniteBridgeLocated` | `true` | `true` | 3001<=P<100000 的动态粗骨架有限桥已有证书，不应混入当前 P>=100000 D0 runner。 | pre-tail bridge imported as boundary evidence |
| `TailObjectInterfaceMatched` | `true` | `true` | P>=100000 尾段对象已经对齐为一维 prefix rough-count / B3 lower-sieve 对象。 | SameParameterPrefixWindowSpecification |
| `RangeAndParameterManifestClosed` | `true` | `true` | 有限桥、尾段起点、alpha/z 规则、prefix 区间和目标角色已经列为可审查 manifest。 | SameParameterPrefixWindowSpecification |
| `SameParameterWindowStillOpen` | `false` | `false` | manifest 只列清范围；还没有证明 D0、M#、terminal budget 使用完全同一 z,D,Lambda/type alphabet。 | SameParameterPrefixWindowSpecification AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse |
| `FiniteBoundaryPrefixCertificateProved` | `false` | `false` | runner/hash 与解析尾段桥接仍未完成，因此 finite prefix 证书尚未闭合。 | SameParameterPrefixWindowSpecification AND ReproduciblePrefixRoughCountRunnerHashLedger AND AnalyticTailToFiniteBoundaryMonotoneBridge |

## 5. 下一最窄点

```text
SameParameterPrefixWindowSpecification
```

并行保留：

```text
ReproduciblePrefixRoughCountRunnerHashLedger AND AnalyticTailToFiniteBoundaryMonotoneBridge AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse
```

审稿边界：本步只关闭范围与参数 manifest；没有证明同参数窗口、runner/hash 或尾段桥接，因此 D0 仍未数值化。
