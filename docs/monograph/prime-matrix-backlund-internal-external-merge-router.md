# Prime Matrix Backlund 内部主攻与外部合并路由器

**状态：** `backlund_external_analytic_package_merged_dstructure_open_internal_backlund_target_locked`

内部路线现在集中攻 `ClassicalBacklundZeroIndentationCostInternalProofLedger`。外部路线把经典 Backlund/Rosser-McCurley/Trudgian 缩进处理作为引用输入接入后，CS8、端点 convention、RVM->CN16 已合并到最终晋级门前。但完整无条件闭合仍被 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 阻断，作者侧不能把该独立验收门自审关闭。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
internal_primary_target=ClassicalBacklundZeroIndentationCostInternalProofLedger
external_backlund_input=ClassicalBacklundZeroIndentationCostExternalAccepted
external_theorem_index=docs/monograph/external-theorem-index.md
external_analytic_backlund_package_merged=true
dstructure_rankin_independent_acceptance_completed=false
row_column_self_contained_closed=false
row_column_external_route_closed=false
```

## 1. 外部 Backlund 输入

| source | url | role |
| --- | --- | --- |
| Trudgian 2012 | https://doi.org/10.1090/S0025-5718-2011-02537-8 | Backlund/Rosser--McCurley 轮廓方法给出 arg zeta/S(t) 的显式上界。 |
| Trudgian 2014 arXiv:1208.5846 | https://arxiv.org/abs/1208.5846 | 现代显式 Backlund 方法与 S(T) 零点处理 convention 的引用入口。 |

## 2. 内部主攻义务

| obligation | content |
| --- | --- |
| `ClassicalContourIndentationProof` | 从局部避零轮廓直接证明近零缩进项被同一 Backlund 轮廓恒等式吸收。 |
| `EndpointAndMultiplicityLimit` | 端点落零先避开再取极限，零点按解析重数登记，且不新增 C_S 常数。 |
| `BudgetPreservingJumpLedger` | 证明局部 jump 不作为额外正比例成本进入 C_S=8；这是内部证明的核心。 |
| `NoDetourDiscipline` | 不再走权重吸收、镜像抵消、胶囊密度、小半径 anchor 或 RVM 反调用。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 合并仍只处理假设链条中的解析输入，不使用真实零行缺席。 | 保持自足与外部两条链分离。 |
| `InternalBacklundTargetLocked` | `true` | `true` | 内部路线集中攻经典 Backlund 零点缩进成本内部证明，不再转移目标。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `ExternalBacklundIndentAcceptedForRoute` | `true` | `false` | 外部路线把经典 Backlund 缩进处理作为引用输入接入。 | ClassicalBacklundZeroIndentationCostExternalAccepted |
| `ExternalBacklundDownstreamCS8Closed` | `true` | `true` | 接受外部缩进输入后，C_S=8 紧等号验收已闭合。 | BacklundCS8SlackAfterBridgeClosedTightHalf |
| `ExternalEndpointConventionClosed` | `true` | `true` | 端点避零与重数极限 convention 已闭合。 | EndpointZeroAvoidanceMultiplicityConventionClosedByLimit |
| `ExternalRVMToCN16Closed` | `true` | `true` | 原始 arg zeta 归一化下，RVM 到 C_N=16 合并已闭合。 | RVMToCN16LocalInequalityClosedWithRawArgCS8 |
| `ExternalAnalyticBacklundPackageMerged` | `true` | `false` | 外部 Backlund 解析包已合并到最终晋级门前。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `DStructureRankinBoundaryClosed` | `true` | `true` | DStructure/Tail-log4/finite Rankin 的验收边界已列清。 | independent acceptance |
| `DStructureRankinIndependentlyAccepted` | `false` | `false` | 该门仍需独立审稿/复现接受，作者侧不能自审关闭。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnExternalRouteClosed` | `false` | `false` | 外部 Backlund 包合并后仍缺 DStructure/Rankin 独立接受。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnSelfContainedClosed` | `false` | `false` | 内部经典 Backlund 缩进成本尚未作者侧重证。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |

## 4. 下一步

内部主攻：`ClassicalBacklundZeroIndentationCostInternalProofLedger`。
外部路线下一门：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

判定：外部 Backlund 解析包已合并到晋级门前；完整闭合仍需 DStructure/Rankin 独立验收或内部 Backlund 重证完成。
