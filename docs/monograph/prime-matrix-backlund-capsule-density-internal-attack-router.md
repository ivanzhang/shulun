# Prime Matrix Backlund 胶囊密度内部攻坚路由器

**状态：** `backlund_capsule_density_reduced_to_scale_sensitive_jensen_open`

胶囊密度目标不能由现有固定半径 Jensen C16 粗计数关闭，也不能直接调用 RVM。C16 跳变成本约为胶囊目标成本的 780 倍。因此当前真正最窄的内部目标是 `BacklundScaleSensitiveJensenCapsuleDensityLedger`：必须在 Jensen/xi 平均中保留胶囊高度 A=33/512 的尺度小因子，同时保持 Gamma 主项相消与 zeta 平均控制。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
capsule_density_reduction_closed=true
scale_sensitive_jensen_capsule_density_closed=false
strict_self_contained_unique_remaining=BacklundScaleSensitiveJensenCapsuleDensityLedger
row_column_self_contained_closed=false
```

## 1. C16 与胶囊目标对比

| item | value |
| --- | ---: |
| capsule target zero coefficient | `0.020516066883` |
| fixed Jensen C16 coefficient | `16.000000000000` |
| coefficient overshoot factor | `779.876576309321` |
| capsule target jump cost | `0.064453125000` |
| fixed C16 jump cost | `50.265482457437` |
| cost overshoot factor | `779.876576309321` |
| remaining cost slack at capsule target | `0.013671875000` |

## 2. 路线判定

| route | verdict | reason |
| --- | --- | --- |
| `RVMLocalDensity` | `blocked_by_circularity` | RVM 局部计数需要 Backlund/arg zeta 端点控制；当前正是在证明该控制。 |
| `FixedRadiusJensenC16` | `too_coarse` | C16 没有胶囊高度 A 的小因子，跳变成本约 50.265，远超 5/64。 |
| `ScaleSensitiveJensenCapsule` | `next_internal_atom` | 需要 Jensen/xi 圆周平均保留尺度 A 的 Gamma 主项相消和 zeta 平均控制。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CapsuleDensityGateActive` | `true` | `true` | 上一层已把零系数目标松弛为独立胶囊密度目标。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条中的解析计数，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `BacklundNearZeroCapsuleCoverGeometryClosed` | `true` | `true` | eta 邻域沿 H 窗口扫出半高 A=eta+H 的胶囊；几何覆盖本身无剩余。 | BacklundScaleSensitiveJensenCapsuleDensityLedger |
| `BacklundNoRVMScaleSensitiveDensityDisciplineClosed` | `true` | `true` | 胶囊密度不能直接调用待证 Backlund 后推出的 RVM/CN16。 | BacklundScaleSensitiveJensenCapsuleDensityLedger |
| `JensenFormalLayerAvailable` | `true` | `true` | Jensen 公式形式层可用，可作为尺度敏感计数的唯一非循环候选工具。 | BacklundScaleSensitiveJensenCapsuleDensityLedger |
| `CenterAnchorSymbolicAvailable` | `true` | `true` | xi 圆心 anchor 已有符号有限常数，但还没有尺度 A 的数值密度聚合。 | BacklundScaleSensitiveJensenCapsuleDensityLedger |
| `FixedC16RouteRejectedForCapsule` | `true` | `true` | 固定半径 C16 计数比胶囊目标粗约 780 倍，不能支付跳变预算。 | BacklundScaleSensitiveJensenCapsuleDensityLedger |
| `BacklundScaleSensitiveJensenCapsuleDensityLedger` | `false` | `false` | 仍需证明 Jensen 胶囊计数保留 A=33/512 的尺度小因子，且不借用 Backlund/RVM。 | BacklundScaleSensitiveJensenCapsuleDensityLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |
| `BacklundIndependentCapsuleZeroDensityCoefficientLedger` | `false` | `false` | 胶囊密度目标已压成尺度敏感 Jensen 胶囊计数。 | BacklundScaleSensitiveJensenCapsuleDensityLedger |

## 4. 下一步

新的严格自足唯一剩余：`BacklundScaleSensitiveJensenCapsuleDensityLedger`。
父级剩余：`BacklundIndependentCapsuleZeroDensityCoefficientLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：胶囊密度目标已压成尺度敏感 Jensen 计数；尚未闭合。
