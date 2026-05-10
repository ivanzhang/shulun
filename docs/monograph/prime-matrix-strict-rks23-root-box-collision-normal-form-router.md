# Prime Matrix strict RKS2/RKS3 根定位盒碰撞正规形证书

**状态：** `central_root_box_high_fiber_reduced_to_nondiagonal_cubic_collision_power_saving`

中央根定位盒的高重数可改写为同相位碰撞问题。对 `Phi(t,d)=(t^2-d^2)/(4t)`，两点同相位当且仅当 `t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P`。同 `t` 的退化只给 `d1=±d2`，规模为 `O(N^2)`，已低于固定幂能量目标。因此当前最窄剩余变成非对角根定位盒三次碰撞的固定幂节省。

```text
root_box_same_phase_collision_identity_closed=true
same_t_and_sign_diagonal_absorbed=true
nondiagonal_root_box_cubic_collision_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 碰撞正规形

| field | value |
| --- | --- |
| `root_box_variables` | t=a+b in J+J, d=a-b with \|d\|<\|J\| and matching parity |
| `phase_map` | Phi(t,d)=(t^2-d^2)/(4t) mod P |
| `same_phase_collision` | Phi(t1,d1)=Phi(t2,d2) |
| `cleared_denominator_form` | t2(t1^2-d1^2)-t1(t2^2-d2^2)=0 mod P |
| `diagonal_t_collision` | if t1=t2 then d1^2=d2^2, hence d1=±d2 in F_P |
| `diagonal_absorption` | same-t and sign-symmetry collisions contribute only O(N^2), below every N^(3-delta) target |
| `high_fiber_implication` | a fiber of size H produces >=H(H-2) non-diagonal same-phase collisions unless it is absorbed by the diagonal layer |
| `remaining_shape` | prove power saving for non-diagonal cubic collisions in the root-localized box |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CentralRootBoxTargetActive` | `true` | `true` | 上一证书已把幸存反例压入中央相位根定位盒。 | CentralPhaseRootLocalizedGraphBoxFiberPowerSaving |
| `RootBoxSamePhaseCollisionIdentityClosed` | `true` | `true` | 同相位条件精确等价于清分母三次碰撞式。 | RootBoxSamePhaseCollisionEnergyNormalForm |
| `SameTAndSignDiagonalAbsorbed` | `true` | `true` | `t1=t2` 只允许 `d1=±d2`，该退化层规模 `O(N^2)`。 | absorbed |
| `HighFiberForcesNonDiagonalCollisionMass` | `true` | `true` | 若中央相位仍有高纤维，则必须产生大量 `t1!=t2` 的同相位碰撞。 | NonDiagonalRootBoxCubicCollisionPowerSaving |
| `NonDiagonalRootBoxCubicCollisionPowerSaving` | `false` | `false` | 仓库内尚未证明根定位盒中非对角三次碰撞具有固定幂节省。 | RootBoxCubicIncidenceOrSumProductPowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只把剩余改写为非对角碰撞输入，没有证明该碰撞估计。 | NonDiagonalRootBoxCubicCollisionPowerSaving |

## 3. 下一最窄自足目标

```text
NonDiagonalRootBoxCubicCollisionPowerSaving
```
