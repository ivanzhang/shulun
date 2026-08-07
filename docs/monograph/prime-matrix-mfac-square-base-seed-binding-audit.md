# MFAC 平方基 global seed 与 primitive-binding 缺口审计

**状态：** `global_square_base_mobius_seed_closed_actual_primitive_binding_open`
**核验日期：** `2026-08-07`

对每个素数 p，p² 的 global colored-word source 中仅 (d,e)=(p,p) 携带非零质量 log p。
这闭合 global square-base seed，不闭合 actual primitive coefficient。

```text
global_square_base_seed_verified=true
unique_active_source_verified=true
actual_square_base_signed_coefficient_bound=false
primitive_orientation_local_factor_law_bound=false
downstream_recovery_used=false
row_column_unconditional_closed=false
```

## 结论边界

每个平方基 p² 在全局 Möbius colored-word 层有唯一非零 payload source (d,e)=(p,p)，其质量为 log p。该结果给出不依赖 payment/zero-row 的 global square-base seed，但尚未定义 actual primitive coefficient a_p(p) 的 orientation、local factor 或归一化。

下一关是 `PrimitiveOrientationLocalFactorProductLawBeforePushforward`：必须把 global seed 正向绑定到 actual primitive unit，或给出最小 normalization/orientation 冲突。
