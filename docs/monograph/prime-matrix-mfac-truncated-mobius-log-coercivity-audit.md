# MFAC 截断 Möbius--log 强制性有限审计

## 参数

- `limit`: `4096`
- `theta`: `0.25`
- `cutoff`: `8`
- `window`: `linear`
- `support_size`: `5`

## 有限比率

- `weighted_mass`: `963.431069893684`
- `normalized_energy_ratio`: `0.41230989094787657`

## 直接/核残差

- `direct_centered_energy`: `397.23215936366086`
- `quadratic_centered_energy`: `397.2321593636609`
- `energy_identity_residual`: `5.684341886080802e-14`

## 对照见证

- `squarefree_mobius`: status=`computed_finite_scale`, coefficient_count=`5`, weighted_mass=`5500.342857142857`, normalized_energy_ratio=`0.37572724388000817`
- `primorial`: status=`computed_finite_scale`, coefficient_count=`1`, weighted_mass=`682.6666666666666`, normalized_energy_ratio=`0.8326821327209473`
- `single_prime_layer`: status=`computed_finite_scale`, coefficient_count=`2`, weighted_mass=`1404.3428571428572`, normalized_energy_ratio=`0.8236920833587646`
- `high_divisor_composite`: status=`computed_finite_scale`, coefficient_count=`1`, weighted_mass=`512.0`, normalized_energy_ratio=`0.875`

## 状态块

```text
status=numerical_only_finite_structured_coercivity_profile
coefficient_family_status=specified
coefficient_independence_verified=true
finite_profile_status=completed_numerical_only
chebyshev_bridge_status=not_started
mellin_status=not_started
structured_coercivity_status=unproved
rh_proved=false
uniform_in_limit_coercivity_proved=false
zero_free_region_proved=false
```

本证书只记录有限浮点数值审计读数；不构成统一强制性、Chebyshev 能量桥、Mellin 收缩，也不构成 RH 证明。
