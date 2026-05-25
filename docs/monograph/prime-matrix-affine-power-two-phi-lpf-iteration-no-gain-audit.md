# Prime Matrix power-two affine Phi-LPF iteration no-gain audit

**状态：** `power_two_affine_iteration_is_shifted_residue_conjugacy_no_parity_gain`
**核验日期：** `2026-05-25`

## 1. 迭代对象

```text
m_t = 2^t n + (2^t-1)
p | m_t  <=>  n == -(2^t-1)*(2^t)^(-1) mod p     (p odd)
```

这说明每次迭代仍只是每个奇素数删除一个 shifted residue 类。

## 2. 有限读数

| P | t | survivor | prime m_t | rough composite | expected 2-adic gap | observed naive gap | corrected error |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 1 | 290 | 282 | 7 | 0.500000 | 0.506950 | -0.013899 |
| 31 | 2 | 290 | 264 | 26 | 0.750000 | 0.753475 | -0.013899 |
| 31 | 3 | 292 | 243 | 49 | 0.875000 | 0.875887 | -0.007098 |
| 31 | 4 | 295 | 226 | 69 | 0.937500 | 0.937306 | 0.003103 |
| 101 | 1 | 2355 | 2279 | 75 | 0.500000 | 0.515561 | -0.031122 |
| 101 | 2 | 2360 | 2142 | 218 | 0.750000 | 0.757266 | -0.029065 |
| 101 | 3 | 2380 | 2006 | 374 | 0.875000 | 0.877605 | -0.020837 |
| 101 | 4 | 2405 | 1870 | 535 | 0.937500 | 0.938159 | -0.010552 |
| 251 | 1 | 12099 | 11765 | 333 | 0.500000 | 0.521586 | -0.043173 |
| 251 | 2 | 12105 | 11102 | 1003 | 0.750000 | 0.760675 | -0.042698 |
| 251 | 3 | 12241 | 10450 | 1791 | 0.875000 | 0.878993 | -0.031943 |
| 251 | 4 | 12427 | 9903 | 2524 | 0.937500 | 0.938577 | -0.017234 |
| 1009 | 1 | 155132 | 151285 | 3846 | 0.500000 | 0.529033 | -0.058066 |
| 1009 | 2 | 155495 | 143923 | 11572 | 0.750000 | 0.763965 | -0.055862 |
| 1009 | 3 | 157528 | 137173 | 20355 | 0.875000 | 0.880440 | -0.043518 |
| 1009 | 4 | 159920 | 131100 | 28820 | 0.937500 | 0.939312 | -0.028994 |

## 3. 结论

```text
all_shifted_residue_formula_verified=true
iteration_creates_new_phi_lpf_information=false
euler_product_half_main_error_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

naive gap 随 `t` 变成 `1-2^{-t}`，说明它是 2-adic residue-space 归一化，不是有限欧拉乘积截断误差。归一化后仍有 rough composite survivors，所以 LPF/Phi 递推迭代没有自动突破奇偶性障碍。

## 4. 最新开放口

```text
PowerTwoAffineShiftedResidueSignedPayloadConstructorOrNamedReturn AND PrimeExtractionFromAffineRoughSurvivorsBeyondParity
```
