# Prime Matrix Backlund 辅助实部 Jensen 构造路由器

**状态：** `backlund_auxiliary_realpart_jensen_formal_construction_closed_constants_open`

经典 Backlund 辅助实部函数的形式层已闭合：B_{T,theta}(z)=1/2(e^{-i theta}xi(z+iT)+e^{i theta}xi(z-iT)) 是整函数，在实轴上等于旋转后的实部，故其零点正是 sign-change 计数对象。右边相位 anchor 与 xi 圆周上界可由既有 Jensen 圆心、Euler 下界和 xi 边界包转移。剩余未闭合的是辅助函数 Jensen 常数聚合，以及它与 xi 真零点/缩进登记的无重复扣费纪律。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
parent_remaining=BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger
formal_construction_closed=true
right_edge_phase_anchor_closed=true
boundary_majorant_transfer_closed_symbolic=true
new_unique_internal_remaining=BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger AND BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger
row_column_self_contained_closed=false
```

## 1. 构造步骤

| step | content | status |
| --- | --- | --- |
| `define_auxiliary_entire` | B_{T,theta}(z)=1/2*(exp(-i theta) xi(z+iT)+exp(i theta) xi(z-iT))。 | `closed_formal` |
| `real_axis_identity` | z=x 为实数时，由 xi(conj s)=conj xi(s)，得 B_{T,theta}(x)=Re(exp(-i theta) xi(x+iT))。 | `closed_formal` |
| `right_edge_phase_anchor` | 取 theta=arg xi(2+iT)，则 B_{T,theta}(2)=\|xi(2+iT)\|，圆心不为零。 | `closed_given_right_edge_anchor` |
| `boundary_transfer` | \|B_{T,theta}(z)\| <= (\|xi(z+iT)\|+\|xi(z-iT)\|)/2，圆周上界可由既有 xi 边界包转移。 | `closed_symbolic` |

## 2. 新剩余

```text
BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger
  =>
BacklundAuxiliaryRealPartEntireFunctionConstructionClosed AND BacklundAuxiliaryRealPartRightEdgePhaseAnchorClosed AND BacklundAuxiliaryRealPartBoundaryMajorantTransferredClosed
  AND
(BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger AND BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger)
```

前三个形式/anchor/边界转移项本步关闭；括号内两项仍开。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只构造经典 Backlund 辅助函数和 Jensen 接口，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `AuxiliaryRealPartJensenGateActive` | `true` | `true` | 上一层已证明不能把 sign-change 直接注入 xi 真零点计数，必须构造辅助实部 Jensen 包。 | BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger |
| `AuxiliaryEntireFunctionConstructionClosed` | `true` | `true` | B_{T,theta}(z) 由 xi 的两个平移共轭项组成，是整函数。 | BacklundAuxiliaryRealPartEntireFunctionConstructionClosed |
| `RealAxisSignChangeIdentityClosed` | `true` | `true` | 在实轴上 B_{T,theta}(x) 正是旋转后 xi(x+iT) 的实部，因此其零点计数 sign-change。 | BacklundAuxiliaryRealPartEntireFunctionConstructionClosed |
| `RightEdgeCenterGeometryAvailable` | `true` | `true` | 既有 z0=2、R=4、r=sqrt(5) 的 Jensen 圆心几何可复用到辅助函数。 | BacklundJensenRightEdgeCenterChoiceConventionClosedR4 |
| `RightEdgePhaseAnchorClosed` | `true` | `true` | 取 theta=arg xi(2+iT) 后圆心值为 \|xi(2+iT)\|；sigma=2 的 Euler 下界给非零 anchor。 | BacklundAuxiliaryRealPartRightEdgePhaseAnchorClosed |
| `BoundaryMajorantTransferClosedSymbolic` | `true` | `true` | 辅助函数的圆周上界由两个 xi 圆周上界平均控制，形式上不新增零点计数输入。 | BacklundAuxiliaryRealPartBoundaryMajorantTransferredClosed |
| `EndpointMultiplicityCompatible` | `true` | `true` | 端点落在辅助函数零点时仍按避零序列和解析重数取极限。 | EndpointZeroAvoidanceMultiplicityConventionClosedByLimit |
| `AuxiliaryJensenConstantAggregationOpen` | `false` | `false` | 还未把辅助函数边界上界、右边 anchor、低高度项聚合成目标 C16 或可被 C_S=8 吸收的常数。 | BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger |
| `AuxiliaryNoDoubleCountingOpen` | `false` | `false` | 还未证明辅助实部零点计数、xi 真零点重数和缩进登记三者没有重复扣费。 | BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger |
| `SelfContainedAuxiliaryBacklundPackageOpen` | `false` | `false` | 形式构造已完成；常数聚合与无重复扣费未完成前，内部经典 Backlund 缩进证明仍开。 | BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger AND BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger |
| `ExternalBacklundStillAvailable` | `true` | `false` | 外部经典 Backlund 引理可整体替代辅助实部 Jensen 计数与无重复扣费证明。 | ClassicalBacklundZeroIndentationCostExternalAccepted |

## 4. 下一步

内部剩余：`BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger AND BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger`。
外部逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：辅助实部 Jensen 的形式层已完成，常数聚合和无重复扣费仍是当前内部硬点。
