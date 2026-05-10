# Prime Matrix strict 同参数终端余量表证书路由器

**状态：** `concrete_same_parameter_margin_table_attempted_blocked_by_missing_d0_e0_u0_fields`

`ConcreteSameParameterMarginTableCertificate` 已被直接尝试装配。可以生成唯一候选参数行 `alpha043_pge100000_external_b3_pending_finite_prefix_named_return`，并确认外部 B3 前沿可作为 D0 的解析尾段输入；但当前材料没有 D0_prefix_lower_bound、E0_named_return_deduction、U0_cold_supply_bound 的同参数数值字段，也没有 finite_boundary_hash，因此不能证明 margin_delta>0。直接证明失败不是换命题，而是把下一原子压成 `RosserIwaniecWeightedFloorRemainderTenPercentBound` 或外部短区间 rough 下界，并行保留有限 prefix/命名扣除/冷供给数值表。

```text
candidate_parameter_row_generated=true
b3_external_lane_imported=true
linear_lower_sieve_tail_ten_percent_margin_pge100000_proved=false
linear_sieve_tail_split_to_weighted_floor_or_external_rough=true
explicit_rosser_weight_ledger_compressed=true
finite_boundary_prefix_certificate_proved=false
finite_boundary_hash_available=false
d0_prefix_lower_bound_available=false
e0_named_return_deduction_available=false
u0_cold_supply_bound_available=false
margin_delta_available=false
concrete_same_parameter_margin_table_certificate_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 候选同参数行

| field | value |
| --- | --- |
| `parameter_id` | alpha043_pge100000_external_b3_pending_finite_prefix_named_return |
| `alpha` | 0.430000000000 |
| `s` | 2.325581395349 |
| `p_min` | 100000 |
| `z_rule` | z=P^0.43 or equivalent non-circular prefix cutoff inherited from B3 lane |
| `b3_tail_model_main_at_p_min` | 4896.256004000000 |
| `ten_percent_model_main_at_p_min` | 489.625600400000 |
| `target_S` | 401.000000000000 |
| `ten_percent_minus_target` | 88.625600400000 |
| `d0_prefix_lower_bound` | None |
| `e0_named_return_deduction` | None |
| `u0_cold_supply_bound` | None |
| `margin_delta` | None |
| `finite_boundary_hash` | None |
| `certificate_row_valid` | False |

## 2. 字段装配状态

| field | available | source | blocker |
| --- | --- | --- | --- |
| `parameter_id` | `true` | canonical alpha=0.43 / P>=100000 candidate row | none |
| `D0_prefix_lower_bound` | `false` | B3 external lane + finite prefix certificate | (RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043) AND FiniteBoundaryPrefixRoughCountCertificate |
| `E0_named_return_deduction` | `false` | named return exclusion/compression ledger | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND NamedReturnSameParameterDeductionTable |
| `U0_cold_supply_bound` | `false` | cold supply upper envelope + lambda discipline | ColdSupplySameParameterNumericEnvelope |
| `margin_delta` | `false` | D0-E0-U0 under same parameter_id | ConcreteSameParameterMarginTableCertificate |
| `finite_boundary_hash` | `false` | finite prefix audit/certificate | FiniteBoundaryPrefixRoughCountCertificate |

## 3. 直接生成/证明尝试

| attempt | success | evidence | meaning |
| --- | --- | --- | --- |
| `assemble candidate parameter row` | `true` | alpha043_pge100000_external_b3_pending_finite_prefix_named_return | 同一参数行可以命名，但尚不构成证明证书。 |
| `import external B3 tail margin` | `true` | 10% model main at P=100000 is 489.625600 | 解析尾段有条件可供 D0 使用；仍需有限 prefix 和真实 D0 表。 |
| `prove D0 lower bound` | `false` | missing weighted floor/sawtooth or external rough input, plus finite prefix hash | 无法从当前材料直接给出全局 D0。 |
| `prove E0 named deduction` | `false` | named compression closed but exclusion/numeric deduction open | 无法证明 E_named 不吞掉余量。 |
| `prove U0 cold dominance` | `false` | upper envelope formula exists; same-parameter numeric value missing | 有供给公式，但还不能和 D0-E0 比较。 |
| `derive margin_delta>0` | `false` | D0/E0/U0 not simultaneously numeric | 本轮直接证明失败，失败原因已原子化。 |

## 4. 失败回流表

| missing_or_failure | forced_return | closed_as_logic | proved_now |
| --- | --- | --- | --- |
| D0 absent or finite prefix undecided | FiniteBoundaryPrefixRoughCountCertificate | `true` | `false` |
| E0 named deduction absent | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR NamedReturnSameParameterDeductionTable | `true` | `false` |
| U0 too large or unregistered | SparseHistoryDemandExceedsNonpersistentSupplyBudget OR ColdSupplySameParameterNumericEnvelope | `true` | `false` |
| terminal promotion still external | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `true` | `false` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本证书仍只在早期零行反例链内尝试装配终端正余量表。 | 保持 row_column_unconditional_closed=false。 |
| `CandidateParameterRowGenerated` | `true` | `false` | 已生成 alpha=0.43, P>=100000 的候选同参数行；它只是装配目标，不是证明。 | fill D0/E0/U0/margin_delta/hash. |
| `ConcreteD0Available` | `false` | `false` | 当前不能给出 D0_prefix_lower_bound。 | (RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043) AND FiniteBoundaryPrefixRoughCountCertificate |
| `ConcreteE0Available` | `false` | `false` | 当前不能给出 E0_named_return_deduction。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND NamedReturnSameParameterDeductionTable |
| `ConcreteU0Available` | `false` | `false` | 当前只有 U_cold 公式，没有同参数数值上界。 | ColdSupplySameParameterNumericEnvelope |
| `ConcreteSameParameterMarginTableCertificateProved` | `false` | `false` | D0/E0/U0 未同时数值化，不能推出 margin_delta>0。 | (RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043) AND FiniteBoundaryPrefixRoughCountCertificate AND NamedReturnSameParameterDeductionTable AND ColdSupplySameParameterNumericEnvelope AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `DirectTerminalContradictionReached` | `false` | `false` | 还没有得到反例链与真实结构链的终端矛盾。 | ConcreteSameParameterMarginTableCertificate AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一最窄点

```text
(RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043) AND FiniteBoundaryPrefixRoughCountCertificate AND NamedReturnSameParameterDeductionTable AND ColdSupplySameParameterNumericEnvelope AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

当前最先攻 `RosserIwaniecWeightedFloorRemainderTenPercentBound`，因为已有材料已经把线性筛 10% 主项包压成该加权 floor 余项或外部短区间 rough 下界；没有 D0，后续 E0/U0 即使给出也无法形成正余量比较。有限 prefix hash、命名扣除表、冷供给数值包仍并行保留。

审稿边界：本文件直接生成了同参数候选行和 BLOCK 证书，但没有证明 `margin_delta>0`。
