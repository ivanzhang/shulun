# Prime Matrix Backlund 辅助实部无重复扣费路由器

**状态：** `backlund_auxiliary_no_double_count_closed_constants_only_open`

辅助实部 Jensen 与 xi 真零点 Jensen 的无重复扣费纪律已作为账本替换规则闭合：内部路线使用辅助实部 Jensen 来替换旧缩进成本，不把它叠加到逐零点 pi 成本或外部 Backlund 引理上；xi 真零点计数仍只服务于倒距离/密度账本。因此当前内部唯一剩余收缩为辅助实部 Jensen 的 C16 常数聚合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
parent_remaining=BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger AND BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger
closed_atom=BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosClosedAsReplacement
new_unique_internal_remaining=BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger
row_column_self_contained_closed=false
```

## 1. 扣费纪律

| rule | content |
| --- | --- |
| `replacement_not_addition` | 辅助实部 Jensen 计数替换旧 `BacklundZeroProximityIndentationCostLedger`，不能与逐零点 pi 成本叠加。 |
| `separate_roles` | xi 真零点 Jensen 只服务于倒距离/局部零点密度账本；辅助实部零点服务于水平 trace 的 arg/sign-change 账本。 |
| `endpoint_multiplicity_single_registry` | 端点和重零先进入统一避零极限登记，再按所属账本调用一次，不重复出现在两个成本项中。 |

## 2. 剩余收缩

```text
BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger AND BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger
  =>
BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosClosedAsReplacement AND BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只处理解析预算账本的归属，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `NoDoubleCountGateActive` | `true` | `true` | 上一层剩余包含辅助实部 Jensen 常数聚合与无重复扣费两项。 | BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger |
| `NearZeroPartitionAvailable` | `true` | `true` | 近零/远零分区已固定：eta 内原本交给缩进账本，eta 外交给倒距离账本。 | BacklundNearZeroIndentSeparationClosedEta1Over16 |
| `AuxiliaryCountReplacesIndentCost` | `true` | `true` | 在内部 Backlund 路线中，辅助实部 Jensen 计数是缩进成本的替代证明，不是新增成本项。 | BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosClosedAsReplacement |
| `XiZeroDistanceRoleSeparated` | `true` | `true` | xi 真零点 Jensen 与辅助实部 Jensen 的用途分离：前者控制倒距离，后者控制水平 trace sign-change。 | BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosClosedAsReplacement |
| `EndpointMultiplicitySingleRegistry` | `true` | `true` | 端点和重零只通过统一极限 convention 登记一次，再路由到所属账本。 | BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosClosedAsReplacement |
| `OldExternalIndentStillAvailableButNotStacked` | `true` | `false` | 若选择外部 Backlund，引理整体关闭缩进包；若选择内部辅助 Jensen，则不得再叠加外部缩进成本。 | ClassicalBacklundZeroIndentationCostExternalAccepted |
| `CS8TightBudgetDisciplinePreserved` | `true` | `true` | C_S=8 是紧等号；本步的替换纪律正是为了不新增正比例成本。 | BacklundCS8SlackAfterBridgeClosedTightHalf |
| `AuxiliaryNoDoubleCountingClosed` | `true` | `true` | 无重复扣费纪律作为账本替换规则闭合。 | BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosClosedAsReplacement |
| `OnlyAuxiliaryJensenConstantsRemain` | `false` | `false` | 现在内部剩余只剩辅助实部 Jensen 常数聚合。 | BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger |

## 4. 下一步

内部唯一最窄点：`BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger`。
外部逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：无重复扣费已闭合；下一步只攻辅助实部 Jensen C16 常数聚合。
