# Prime Matrix strict RKS2/RKS3 差平方退化碰撞吸收证书

**状态：** `equal_difference_square_collision_absorbed_true_cubic_distinct_difference_remains`

非对角碰撞中 `d1^2=d2^2` 的退化层可以自足吸收。此时碰撞式化为 `t1*t2+d^2=0 mod P`，整数提升为 `t1*t2+d^2=lP`；在平方根颈部只有 `log^O(P)` 个 `l`，固定 `d,l` 后由除数界控制。因此真正剩余进一步压成 `t1!=t2` 且 `d1^2!=d2^2` 的完全非对角三次碰撞。

```text
equal_difference_square_divisor_absorbed=true
true_cubic_collision_scope_is_distinct_difference_square=true
fully_nondiagonal_distinct_difference_cubic_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 同差平方退化层

| field | value |
| --- | --- |
| `starting_collision` | t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P |
| `layer_condition` | t1!=t2 and d1^2=d2^2=d^2 |
| `reduced_equation` | t1*t2+d^2=0 mod P |
| `integer_lift` | t1*t2+d^2=lP |
| `branch_budget` | l<=O(U^2/P)=log^O(P) in the square-root collar |
| `divisor_count` | for fixed d,l, the number of (t1,t2) is <=tau(lP-d^2) |
| `total_size` | O(N log^O(P) P^o(1)) |
| `absorption` | this is far below N^(3-delta) for every fixed delta<2 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NonDiagonalCollisionTargetActive` | `true` | `true` | 上一证书已把剩余压成根定位盒的非对角三次碰撞。 | NonDiagonalRootBoxCubicCollisionPowerSaving |
| `EqualDifferenceSquareReductionClosed` | `true` | `true` | `d1^2=d2^2` 时非对角碰撞退化为 `t1*t2+d^2=0 mod P`。 | EqualDifferenceSquareCollisionDivisorAbsorption |
| `EqualDifferenceSquareDivisorAbsorbed` | `true` | `true` | 整数提升后只有 `log^O(P)` 个分支，固定分支由除数界控制，总规模可吸收。 | absorbed |
| `TrueCubicCollisionScopeIsDistinctDifferenceSquare` | `true` | `true` | 幸存碰撞必须同时满足 `t1!=t2` 与 `d1^2!=d2^2`。 | FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving |
| `FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving` | `false` | `false` | 仓库内尚未证明完全非对角、差平方不同的三次碰撞固定幂节省。 | DistinctDifferenceRootBoxCubicIncidencePowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只吸收同差平方退化层，未证明真三次碰撞估计。 | FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving |

## 3. 下一最窄自足目标

```text
FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving
```
