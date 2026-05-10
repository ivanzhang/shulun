# Prime Matrix strict Rosser floor 终端收费路由器

**状态：** `rosser_floor_failure_charged_to_named_terminal_family_margin_table_still_open`

本步直接硬攻 D0 前沿的 Rosser floor 缺口。结论不是证明 D0 已有数值下界，而是证明一个更窄的收费纪律：内部 sawtooth/近平方条带若失败，不能继续作为无名 D0 损失；它已经由 exact sawtooth 标准形、二次圆弧、近平方条带缺陷证书和 strict high-tail 校准，强制进入同 formal unit 的 PDEC/SAE/ColumnCRT/CleanKLS 终端家族。因此下一步最窄点从“继续盲攻 Rosser floor”转为生成同一 parameter_id 下的 NamedReturnSameParameterDeductionTable；并行保留 strict 终端家族排斥、外部 rough 下界、finite prefix hash、冷供给数值表和 DStructure/Rankin 独立验收门。

```text
parameter_id=alpha043_pge100000_external_b3_pending_finite_prefix_named_return
sawtooth_failure_no_free_d0_loss_closed=true
weighted_floor_d0_available=false
external_short_interval_rough_lower_bound_accepted=false
finite_boundary_prefix_certificate_proved=false
named_return_same_parameter_deduction_table_proved=false
concrete_same_parameter_margin_table_certificate_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. D0 前沿改写

改写前：

```text
(RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043) AND FiniteBoundaryPrefixRoughCountCertificate AND NamedReturnSameParameterDeductionTable AND ColdSupplySameParameterNumericEnvelope AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

改写后：

```text
FiniteBoundaryPrefixRoughCountCertificate AND (RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR SawtoothFailureChargedToNamedTerminalFamily) AND (NamedReturnSameParameterDeductionTable OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily) AND ColdSupplySameParameterNumericEnvelope AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

核心收费律：

```text
FiniteBoundaryPrefixRoughCountCertificate AND (RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR SawtoothFailureChargedToNamedTerminalFamily)
```

## 2. 分支收费表

| branch | condition | routed_to | closed_as_logic | proved_now | consequence |
| --- | --- | --- | --- | --- | --- |
| `weighted_floor_success` | Rosser floor/sawtooth loss is within the 10% budget | D0_prefix_lower_bound | `true` | `false` | 可给 D0，但仍需 finite prefix hash 与 E0/U0 同参数字段。 |
| `external_rough_success` | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 is accepted | D0_prefix_lower_bound | `true` | `false` | 外部 rough 下界可绕过内部 sawtooth，但仍是外部输入。 |
| `sawtooth_or_strip_failure` | weighted floor bound fails through exact sawtooth / near-square strip | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily and then NamedReturnSameParameterDeductionTable | `true` | `false` | 失败态必须登记为同 formal unit 的 PDEC/SAE/ColumnCRT/CleanKLS 终端收费，不能作为无名 D0 损失。 |
| `finite_prefix_absent` | tail lane available but finite boundary prefix certificate is absent | FiniteBoundaryPrefixRoughCountCertificate | `true` | `false` | 没有有限边界 hash，任何渐近尾段余量都不能升级为全局 D0。 |
| `named_return_not_numeric` | terminal charge exists but same-parameter E_named table is absent | NamedReturnSameParameterDeductionTable | `true` | `false` | 下一步必须给同一 parameter_id 下的命名扣除表，否则收费不能进入 margin_delta。 |
| `cold_supply_not_numeric` | nonpersistent supply can still absorb demand | ColdSupplySameParameterNumericEnvelope AND SparseHistoryDemandExceedsNonpersistentSupplyBudget | `true` | `false` | 冷供给上界仍需和 D0-E0 做同参数比较。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍在假设早期零行反例链内部收费，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `RosserFloorSplitImported` | `true` | `true` | Rosser floor 旧原子已拆成 lower weights 与 exact sawtooth。 | 继续接 sawtooth/条带失败态。 |
| `SawtoothFailureNoFreeD0Loss` | `true` | `false` | 若 sawtooth/近平方条带估计失败，失败态已经强制变成命名终端家族，不再是无名 D0 黑洞。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily OR NamedReturnSameParameterDeductionTable |
| `D0FrontRewritten` | `true` | `false` | D0 前沿由单纯 Rosser floor 证明，改写为 floor 成功、外部 rough 成功、或失败收费三分支。 | FiniteBoundaryPrefixRoughCountCertificate AND (RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR SawtoothFailureChargedToNamedTerminalFamily) |
| `ConcreteD0AvailableNow` | `false` | `false` | 本轮没有证明新的 D0 数值下界；只关闭了失败态收费纪律。 | RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR charged terminal exclusion |
| `NamedReturnSameParameterNeeded` | `false` | `false` | 收费后真正需要把终端回流写成同一参数行的 E0 扣除表。 | NamedReturnSameParameterDeductionTable |
| `ConcreteSameParameterMarginTableProved` | `false` | `false` | D0/E0/U0 仍未同时数值化，不能推出 margin_delta>0。 | FiniteBoundaryPrefixRoughCountCertificate AND (RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR SawtoothFailureChargedToNamedTerminalFamily) AND (NamedReturnSameParameterDeductionTable OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily) AND ColdSupplySameParameterNumericEnvelope AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `DirectTerminalContradictionReached` | `false` | `false` | 尚未得到反例链与真实结构链的无条件终端矛盾。 | NamedReturnSameParameterDeductionTable OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR FiniteBoundaryPrefixRoughCountCertificate |

## 4. 下一真正最窄点

首攻：

```text
NamedReturnSameParameterDeductionTable
```

并行保留：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR FiniteBoundaryPrefixRoughCountCertificate OR ColdSupplySameParameterNumericEnvelope OR SparseHistoryDemandExceedsNonpersistentSupplyBudget OR DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只关闭 Rosser floor 失败态的收费纪律；它没有证明同参数 E0 数值表，也没有证明行/列命题无条件闭合。
