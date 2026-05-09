# Prime Matrix Backlund 近零胶囊密度松弛路由器

**状态：** `backlund_zero_jump_reduced_to_capsule_density_open`

未配对跳变零系数不是必要条件。利用已固定的 eta=1/16 与 H=1/512，近零胶囊半高 A=eta+H=33/512，若能独立证明未配对胶囊零点密度系数不超过 A/pi，则跳变成本至多 A=33/512，小于稳定余量 5/64=40/512。因此当前更优的严格自足目标是 `BacklundIndependentCapsuleZeroDensityCoefficientLedger`；它必须独立于 Backlund/RVM 证明，不能退回 Jensen C16 粗计数。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
zero_coefficient_relaxation_closed=true
capsule_density_self_contained_closed=false
strict_self_contained_unique_remaining=BacklundIndependentCapsuleZeroDensityCoefficientLedger
row_column_self_contained_closed=false
```

## 1. 关键常数

| item | value |
| --- | ---: |
| eta | `0.062500000000` |
| H | `0.001953125000` |
| A=eta+H | `0.064453125000` |
| stability margin | `0.078125000000` |
| allowed zero coefficient | `0.024867959858` |
| capsule target zero coefficient | `0.020516066883` |
| jump cost at capsule target | `0.064453125000` |
| cost slack | `0.013671875000` |
| Jensen C16 jump cost | `50.265482457437` |

等价看法：`A=33/512`，而稳定余量 `5/64=40/512`，还剩 `7/512` 成本余量。

## 2. 候选路线

| route | status | content |
| --- | --- | --- |
| `BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger` | `sufficient_but_stronger_than_needed` | 证明未配对跳变 log(T) 系数为 0；足够闭合，但比实际预算需求更强。 |
| `BacklundIndependentCapsuleZeroDensityCoefficientLedger` | `new_best_internal_target` | 证明近零胶囊内未配对零点数系数不超过 (eta+H)/pi，并且不调用 Backlund/RVM。 |
| `ClassicalBacklundZeroIndentationCostExternalAccepted` | `external_escape` | 接受经典 Backlund 缩进引理，直接关闭该预算包；不是严格自足路线。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ZeroCoefficientGateActive` | `true` | `true` | 上一层把严格自足唯一剩余压成未配对跳变零系数预算。 | BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条的解析预算，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `EtaAndWindowImported` | `true` | `true` | 近零半径 eta=1/16 与短窗口 H=1/512 已固定，因此胶囊半高 A=eta+H=33/512。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |
| `ZeroCoefficientSufficientButNotNecessary` | `true` | `true` | 零系数可以闭合预算，但实际只需未配对零点密度低于 5/(64*pi)。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |
| `CapsuleDensityTargetFitsMargin` | `true` | `true` | 若未配对胶囊零点系数 <=(eta+H)/pi，则跳变成本 <=eta+H=33/512<5/64。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |
| `JensenC16StillTooCoarse` | `true` | `true` | Jensen C16 粗数给出 16*pi 的跳变系数，远超余量；必须证明胶囊高度比例密度。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |
| `NoRVMCircularityStillRequired` | `true` | `true` | 不能直接调用由 Backlund C_S 推出的 RVM/CN16；胶囊密度必须独立证明。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |
| `BacklundIndependentCapsuleZeroDensityCoefficientLedger` | `false` | `false` | 当前仓库还没有独立证明近零胶囊未配对零点数具有 (eta+H)/pi 级密度系数。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger OR BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |
| `BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger` | `false` | `false` | 零系数原子被放宽为更优的胶囊密度原子；二者任一闭合即可推进内部缩进成本。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |

## 4. 下一步

新的严格自足最优剩余：`BacklundIndependentCapsuleZeroDensityCoefficientLedger`。
更强充分目标仍可选：`BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：零系数目标已被更优的胶囊密度目标替代；该目标尚未自足闭合。
