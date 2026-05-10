# Prime Matrix strict RKS2/RKS3 仿射平方集自交前沿证书

**状态：** `true_cubic_collision_linearized_to_nontrivial_affine_self_intersections_of_short_square_set`

完全非对角三次碰撞可以进一步线性化。令 `x=t1,u=t2,y=d1^2,v=d2^2`，碰撞式 `u(x^2-y)-x(u^2-v)=0` 等价于 `v=(u/x)y+u(u-x) mod P`。由于 `x!=u`，斜率非 1；由于 `d->d^2` 至多二重，差变量只造成常数损失。因此当前唯一剩余变成短平方集 `D` 在参数化非平凡仿射映射族下的总自交固定幂节省。

```text
affine_square_set_linearization_closed=true
nontrivial_affine_square_set_energy_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 仿射平方集正规形

| field | value |
| --- | --- |
| `variables` | x=t1, u=t2, y=d1^2, v=d2^2 |
| `true_scope` | x!=u and y!=v |
| `cubic_collision` | u(x^2-y)-x(u^2-v)=0 mod P |
| `affine_square_equation` | v=(u/x)y+u(u-x) mod P |
| `slope` | lambda=u/x, and lambda!=1 in the non-diagonal t-layer |
| `translation` | mu=u(u-x) |
| `short_square_set` | D={d^2: d is an allowed root-box difference} |
| `multiplicity` | each y in D has at most two signed d-preimages, so d-multiplicity costs only an absolute factor |
| `collision_count_bound` | true cubic collisions <=4*sum_{x!=u} \|D cap A_{x,u}^{-1}(D)\| |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FullyNonDiagonalCollisionTargetActive` | `true` | `true` | 上一证书已把剩余压成 `t1!=t2` 且 `d1^2!=d2^2` 的真三次碰撞。 | FullyNonDiagonalDistinctDifferenceRootBoxCubicCollisionPowerSaving |
| `AffineSquareSetLinearizationClosed` | `true` | `true` | 代入 `y=d1^2,v=d2^2` 后，碰撞式对 `y,v` 是一条非恒等仿射关系。 | NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving |
| `SignedDifferenceMultiplicityControlled` | `true` | `true` | `d->d^2` 在根定位盒中至多二重，转成平方值集合只损失常数。 | constant factor |
| `NontrivialAffineMapsIdentified` | `true` | `true` | `t1!=t2` 等价于斜率 `u/x!=1`，所以剩余排除了恒等仿射退化。 | NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving |
| `NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving` | `false` | `false` | 仓库内尚未证明短平方集在这族非平凡仿射映射下的总自交有固定幂节省。 | RootBoxTParameterAffineSquareSetIncidencePowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只线性化真三次碰撞，未证明仿射平方集自交估计。 | NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving |

## 3. 下一最窄自足目标

```text
NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving
```
