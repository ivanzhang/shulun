# Prime Matrix strict RKS2/RKS3 斜率二次曲线束前沿证书

**状态：** `affine_square_set_frontier_reduced_to_nontrivial_slope_localized_conic_bundle`

仿射平方集自交族还能继续缩窄。斜率 `lambda=u/x` 一旦固定，平移项不是自由参数，而是 `lambda(lambda-1)x^2`。因此剩余等价嵌入非平凡斜率上的局部二次曲线束 `d2^2=lambda*d1^2+lambda(lambda-1)*x^2`，并带有 `x,lambda*x in T` 的根盒限制。下一唯一内部输入是该非退化曲线束的总解数固定幂节省。

```text
conic_bundle_identity_closed=true
slope_conic_bundle_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 斜率曲线束正规形

| field | value |
| --- | --- |
| `slope` | lambda=u/x |
| `nontrivial_scope` | lambda not in {0,1}; lambda=1 is t-diagonal and lambda=0 is impossible because u=t2!=0 |
| `root_box_restriction` | x in T and lambda*x in T |
| `affine_translation_identity` | u(u-x)=lambda(lambda-1)x^2 |
| `conic_equation` | d2^2=lambda*d1^2+lambda(lambda-1)*x^2 mod P |
| `bundle_form` | sum over nontrivial slopes lambda of localized solutions (x,d1,d2) |
| `nonsingularity` | for lambda not in {0,1}, the ternary quadratic form has three nonzero coefficients |
| `why_narrower` | the affine maps are tied to square translations from the same t-box, not arbitrary affine maps |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AffineSquareSetTargetActive` | `true` | `true` | 上一证书已把剩余压成短平方集的非平凡仿射自交能量。 | NontrivialAffineSelfIntersectionEnergyOfShortSquareSetPowerSaving |
| `SlopeParameterizationClosed` | `true` | `true` | 令 `lambda=u/x` 后，仿射平移项强制等于 `lambda(lambda-1)x^2`。 | NontrivialSlopeLocalizedTernaryConicBundlePowerSaving |
| `ConicBundleIdentityClosed` | `true` | `true` | 剩余自交等价嵌入斜率局部二次曲线束 `d2^2=lambda d1^2+lambda(lambda-1)x^2`。 | NontrivialSlopeLocalizedTernaryConicBundlePowerSaving |
| `NontrivialSlopesNonsingular` | `true` | `true` | `lambda` 不为 `0,1` 时二次型非退化；已排除恒等/零斜率退化。 | RootBoxSlopeConicIncidencePowerSaving |
| `NontrivialSlopeLocalizedTernaryConicBundlePowerSaving` | `false` | `false` | 仓库内尚未证明该局部斜率二次曲线束的总解数固定幂节省。 | RootBoxSlopeConicIncidencePowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只把仿射自交族缩成斜率二次曲线束，未证明曲线束估计。 | NontrivialSlopeLocalizedTernaryConicBundlePowerSaving |

## 3. 下一最窄自足目标

```text
NontrivialSlopeLocalizedTernaryConicBundlePowerSaving
```
