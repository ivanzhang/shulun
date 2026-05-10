# Prime Matrix strict RKS2/RKS3 Möbius 谱到仿射倒数自交高谱证书

**状态：** `mobius_overlap_spectrum_reduced_to_affine_progression_inverse_self_intersection_high_spectrum`

当前唯一内部自足线继续缩窄：`phi_s(a)=a/(sa-1)` 的区间重叠不是一般 Möbius 图问题，而是完全等价于仿射等差段 `A_s=sJ-1` 的倒数自交 `|A_s∩A_s^{-1}|`。同时低重叠层由 `Σ_s r_s=N^2` 自动吸收；真正剩余只剩高重叠谱排斥：证明不能有许多 `s` 使同一个仿射进度段在取倒数后仍大量落回自身。

```text
affine_inverse_self_intersection_identity_closed=true
low_overlap_layer_automatically_absorbed=true
affine_inverse_high_spectrum_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 仿射倒数自交改写

| field | value |
| --- | --- |
| `mobius_overlap` | r_J(s)=#{a in J: a/(s*a-1) in J} |
| `affine_progression` | A_s=sJ-1={s*a-1: a in J} |
| `inverse_self_intersection_identity` | r_J(s)=\|A_s cap A_s^(-1)\| |
| `proof_line` | x=s*a-1 and b=a/(s*a-1) imply s*b-1=x^(-1) |
| `low_overlap_absorption` | for any fixed eta>0, sum_{r_s<=N^(1-eta)} r_s^2 <= N^(1-eta) sum_s r_s = N^(3-eta) |
| `remaining_high_spectrum` | control s with \|A_s cap A_s^(-1)\| > N^(1-eta) |
| `structural_meaning` | a bad spectrum means many affine images of J are unusually stable under inversion |
| `allowed_next_tools` | self-contained incidence on xy=1 against affine progressions, or PGL2 almost-stabilizer expansion |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MobiusSpectrumTargetActive` | `true` | `true` | 上一证书已把固定幂能量核心压成一参数 Möbius interval-overlap 谱。 | OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving |
| `AffineInverseSelfIntersectionIdentityClosed` | `true` | `true` | `phi_s` 重叠完全等价于仿射等差段 `A_s=sJ-1` 与其倒数像自交。 | AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23 |
| `LowOverlapLayerAutomaticallyAbsorbed` | `true` | `true` | 低重叠层由 `sum r_s=N^2` 直接给固定幂节省；只有高重叠谱需要深估计。 | AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23 |
| `IncidenceAndSumProductRouteStillAligned` | `true` | `true` | Rudnev/RNRS/sum-product 路线可解释为 `xy=1` 与仿射进度族的高自交排斥。 | RudnevRNRSAffineProgressionInverseIntersectionIncidenceEstimate |
| `AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23` | `false` | `false` | 仓库内尚未证明许多 `s` 不能使 `\|A_s cap A_s^{-1}\|` 达到高重叠规模。 | RudnevRNRSAffineProgressionInverseIntersectionIncidenceEstimate OR PGL2IntervalAlmostStabilizerPowerSavingForMobiusInvolutions |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是等价改写和低重叠吸收，不是高谱排斥本身。 | AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23 |

## 3. 下一最窄自足目标

```text
AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23
```
