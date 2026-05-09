# Prime Matrix Backlund sign-change 吸收障碍路由器

**状态：** `backlund_signchange_absorption_reduced_to_auxiliary_realpart_jensen_open`

sign-change 吸收不能直接使用 xi 真零点的 Jensen C16 计数：实部过零是曲线穿过一条直线，通常不等于 F=0。因此上一层的无重复吸收命题被进一步压成：必须构造经典 Backlund 的辅助实部解析计数对象，对该对象建立 Jensen 计数，并证明它与真零点、端点重数和缩进登记不重复扣费。这正是外部经典 Backlund 引理可整体接受的内容；严格自足版仍未闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
previous_unique_remaining=BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger
rejected_false_route=BacklundSignChangeZerosInjectIntoXiZeroJensenLedger
new_unique_internal_remaining=BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger
row_column_self_contained_closed=false
row_column_external_route_closed=false
```

## 1. 结构障碍

| model | sign-change event | meaning |
| --- | --- | --- |
| `F(x)=x+i` | Re F(0)=0 且 F(0)=i != 0 | 实部过零只说明曲线穿过虚轴，不说明 F 有零点。 |
| `F(x)=e^{ix}` | Re F(x)=0 在 x=pi/2+k*pi 出现，但 F(x) 从不为 0 | sign-change 数可与解析零点数完全脱钩。 |
| `F(s)=(s-rho)^m g(s)` | 若路径命中 rho，则缩进 jump 按 m 登记；但非零穿轴事件仍可能存在 | 重数登记只处理真零点；经典 Backlund 还必须计数非零的实部过零。 |

结论：`Re(e^{-i theta}F)=0` 是一维实方程，`F=0` 是二维解析零点条件；前者不能注入后者。旧的 xi 真零点 Jensen C16 只能计真零点，不能自动计所有 Backlund sign-change。

## 2. 新的精确剩余

```text
BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger
  =>
NOT BacklundSignChangeZerosInjectIntoXiZeroJensenLedger
  AND
BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger
```

新的内部硬点：`BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger`。

它要求构造辅助实部函数、证明 Jensen 计数、再证明无重复扣费；这比“直接注入 xi 零点计数”严格得多。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只检查假设链条里的解析计数对象，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `SignChangeAbsorptionGateActive` | `true` | `true` | 上一层把内部剩余压成 sign-change 登记表对 Jensen C16 的无重复吸收。 | BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger |
| `XiZeroJensenC16AvailableExternally` | `true` | `false` | 外部低高度输入下，xi 真零点的 Jensen C16 计数可作为参照。 | BacklundIndependentJensenZeroCountC16AggregationExternalClosed |
| `LittlewoodZeroWeightIdentityAvailable` | `true` | `true` | Littlewood 矩形恒等式登记的是解析零点横向权重，不是所有实部过零。 | BacklundLittlewoodRectangleArgumentClosed |
| `SignChangeNotXiZeroObstructionClosed` | `true` | `true` | Re(e^{-i theta}F) 的零点通常只是曲线穿过一条直线；F 本身可以非零。 | BacklundSignChangeZerosInjectIntoXiZeroJensenLedger |
| `DirectInjectionIntoXiZeroJensenRejected` | `true` | `true` | 不能把 sign-change 事件逐项注入 xi 零点 Jensen 计数；这会漏掉非零穿轴事件。 | BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger |
| `AuxiliaryRealPartAnalyticFunctionNeeded` | `true` | `true` | 经典 Backlund 必须为实部/旋转实部构造辅助解析计数对象，并对该对象应用 Jensen。 | BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger |
| `NoDoubleCountConditionStillNeeded` | `false` | `false` | 辅助实部 Jensen 计数完成后，还需证明它与 xi 真零点、端点重数和缩进登记不重复扣费。 | BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger |
| `SelfContainedBacklundIndentStillOpen` | `false` | `false` | 内部经典 Backlund 缩进证明仍未闭合；现在精确剩余是辅助实部 Jensen 计数和无重复扣费。 | BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger |
| `ExternalBacklundStillClosesThisPackage` | `true` | `false` | 外部经典 Backlund 引理正是对该辅助实部计数和缩进 convention 的整体引用。 | ClassicalBacklundZeroIndentationCostExternalAccepted |
| `ExternalRouteStillNeedsDStructure` | `false` | `false` | 接受外部 Backlund 后仍不能跳过 DStructure/Rankin 独立验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步

内部唯一最窄点：`BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger`。
外部逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。
外部路线最终仍需：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

判定：自足版不能用 xi 真零点 Jensen 计数伪闭合；必须重证经典 Backlund 辅助实部 Jensen 包，或接受外部 Backlund 引理。
