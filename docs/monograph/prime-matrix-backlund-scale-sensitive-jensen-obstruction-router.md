# Prime Matrix Backlund 尺度敏感 Jensen 几何障碍路由器

**状态：** `backlund_scale_sensitive_jensen_blocked_by_anchor_radius_open`

尺度敏感 Jensen 胶囊计数被现有右边界 anchor 几何阻断。要得到 A=33/512 的小因子，Jensen 半径必须与 A 同阶；但只要圆心放在 sigma>1 以使用 Euler product 下界，覆盖临界线附近零点的半径至少约 1/2，已经远大于 A，不能保留胶囊高度小因子。因此新的最窄内部目标是 `BacklundCriticalLineScaleAnchorAvoidanceLedger`：在靠近临界线的小半径圆盘中建立非循环、非移动成本的圆心 anchor。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
right_anchor_radius_obstruction_closed=true
scale_sensitive_jensen_capsule_density_closed=false
strict_self_contained_unique_remaining=BacklundCriticalLineScaleAnchorAvoidanceLedger
row_column_self_contained_closed=false
```

## 1. 几何常数

| item | value |
| --- | ---: |
| A=eta+H | `0.064453125000` |
| right-anchor minimum radius | `0.500000000000` |
| sigma=2 center radius | `1.500000000000` |
| right-anchor radius / A | `7.757575757576` |
| sigma=2 radius / A | `23.272727272727` |
| stability margin | `0.078125000000` |
| right-anchor radius minus margin | `0.421875000000` |

## 2. 路线判定

| route | verdict | reason |
| --- | --- | --- |
| `RightEdgeEulerAnchor` | `geometrically_blocked_for_A_scale` | 圆心在 sigma>1 时，为覆盖临界线附近零点，半径至少约 1/2，无法保留 A=33/512 小因子。 |
| `CriticalLineSmallDiskAnchor` | `new_hard_atom` | 半径可为 O(A)，但必须给出靠近临界线且避开零点的统一圆心下界。 |
| `MovingCenterAvoidance` | `equivalent_to_indent_cost` | 随 T 移动选择避零圆心会重新引入近零缩进/跳变成本。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ScaleSensitiveJensenGateActive` | `true` | `true` | 上一层把胶囊密度压成尺度敏感 Jensen 胶囊计数。 | BacklundScaleSensitiveJensenCapsuleDensityLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条中的解析几何障碍。 | 保持 row_column_self_contained_closed=false。 |
| `RightEdgeAnchorMechanismIdentified` | `true` | `true` | 现有 Jensen 圆心路线依赖 sigma>1 的 Euler product 下界。 | BacklundRightAnchorScaleSensitiveJensenRadiusObstructionClosed |
| `BacklundRightAnchorScaleSensitiveJensenRadiusObstructionClosed` | `true` | `true` | 若圆心在 sigma>1，又要覆盖 sigma=1/2 附近零点，则半径至少约 1/2，不能保留 A=33/512 小尺度。 | BacklundCriticalLineScaleAnchorAvoidanceLedger |
| `Sigma2CenterEvenWorse` | `true` | `true` | 若沿用 sigma=2 圆心，半径至少 3/2，是 A 的二十多倍。 | BacklundCriticalLineScaleAnchorAvoidanceLedger |
| `SmallRadiusRequiresCriticalAnchor` | `true` | `true` | 要让 Jensen 半径为 O(A)，圆心必须靠近临界线；这需要新的统一非零下界或避零圆心选择。 | BacklundCriticalLineScaleAnchorAvoidanceLedger OR BacklundMovingCenterZeroAvoidanceWithoutCostLedger |
| `MovingCenterAvoidanceLoopsToIndent` | `true` | `true` | 若圆心随零点移动避让，避让本身重新产生近零跳变/缩进成本。 | BacklundCriticalLineScaleAnchorAvoidanceLedger |
| `BacklundScaleSensitiveJensenCapsuleDensityLedger` | `false` | `false` | 尺度敏感 Jensen 路线被右边界锚半径障碍阻断；下一步必须攻临界线小半径 anchor。 | BacklundCriticalLineScaleAnchorAvoidanceLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |

## 4. 下一步

新的严格自足唯一剩余：`BacklundCriticalLineScaleAnchorAvoidanceLedger`。
父级剩余：`BacklundScaleSensitiveJensenCapsuleDensityLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：右边界 Jensen anchor 无法给出 A 级胶囊密度；必须攻临界线小半径 anchor。
