# MFAC primitive 归一化不可识别性审计

**状态：** `global_square_base_seed_does_not_identify_primitive_orientation_or_local_factor`

```text
normalization_underdetermination_verified=true
actual_primitive_orientation_bound=false
actual_primitive_local_factor_bound=false
actual_square_base_signed_coefficient_bound=false
```

global square-base seed 的 log(p) 只固定三个 primitive 字段的乘积，不能反推其中任一字段。
下一关必须正向声明 `PrimitiveOrientationLocalFactorProductLawBeforePushforward`，或给出 actual primitive unit 的独立构造。
