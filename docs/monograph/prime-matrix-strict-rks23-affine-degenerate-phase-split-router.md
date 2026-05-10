# Prime Matrix strict RKS2/RKS3 仿射退化相位拆分证书

**状态：** `s_zero_affine_degenerate_phase_absorbed_nonzero_pgl2_high_spectrum_remains`

当前最窄点进一步校正：`s=0` 是真实仿射退化相位，方程退化为 `b=-a`，在对称区间中可产生线性重叠，不能被错误地并入非仿射高谱排斥。但它只有一个相位，能量贡献至多 `N^2`，被任意固定幂目标 `N^(3-delta)` 吸收。因此真正剩余变为 `s!=0` 的非退化 PGL2/Möbius 高谱排斥。

```text
degenerate_phase_s0_identified=true
degenerate_phase_s0_energy_absorbed=true
nonzero_affine_inverse_high_spectrum_proved=false
row_column_unconditional_closed=false
```

## 1. 退化相位账本

| field | value |
| --- | --- |
| `degenerate_phase` | s=0 |
| `equation` | a^(-1)+b^(-1)=0 iff b=-a |
| `mobius_map` | phi_0(a)=-a is affine, not genuinely non-affine |
| `possible_size` | r_J(0)=\|J cap (-J)\| can be as large as O(\|J\|) |
| `energy_contribution` | r_J(0)^2 <= \|J\|^2 |
| `absorption` | \|J\|^2 <= \|J\|^(3-delta) for every fixed delta<1 and \|J\|>=1 |
| `pole_issue_for_s_nonzero` | the pole a=s^(-1) contributes no solution and removes at most one point |
| `remaining_scope` | only s != 0, where phi_s(a)=a/(s*a-1) is a genuine non-affine PGL2 map |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AffineInverseHighSpectrumTargetActive` | `true` | `true` | 上一证书已把剩余压成仿射等差段倒数自交高谱。 | AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23 |
| `DegeneratePhaseS0Identified` | `true` | `true` | `s=0` 是真实存在的仿射退化相位，对应反中心配对 `b=-a`。 | single affine phase |
| `DegeneratePhaseS0EnergyAbsorbed` | `true` | `true` | `s=0` 纵使有线性重叠，也只贡献 `O(N^2)`，低于固定幂能量目标。 | removed from high-spectrum hardpoint |
| `NonzeroMapsAreGenuinePGL2` | `true` | `true` | 对 `s!=0`，`phi_s` 有唯一 pole 且不是仿射，剩余确为非退化 PGL2 高谱。 | NonzeroAffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23 |
| `NonzeroAffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23` | `false` | `false` | 仓库内尚未证明非零相位的仿射进度段倒数自交高谱有固定幂节省。 | RudnevRNRSAffineProgressionInverseIntersectionIncidenceEstimate OR NonzeroPGL2IntervalAlmostStabilizerPowerSavingForMobiusInvolutions |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只分离并吸收退化相位，未证明非零 PGL2 高谱排斥。 | NonzeroAffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23 |

## 3. 下一最窄自足目标

```text
NonzeroAffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23
```
