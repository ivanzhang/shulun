# MFAC 去常数强制性到 Mellin 的未闭合义务

## 当前范围

有限维审计已在若干明确 `limit` 与候选索引上验证实际 LCM Gram 核的去常数正交性，并记录正的有限主子式与 Gershgorin 下界。这些读数不构成维度一致、尺度一致或无穷维的强制性定理。

## 义务一：全尺度强制常数

需要给出独立于候选维度、截断范围与 dyadic 尺度的常数 \(c>0\)，并证明对允许的全部去常数向量族有对应能量下界。有限矩阵的最小读数、正主子式或 Gershgorin 下界都不能替代该命题。

## 义务二：实际 Chebyshev 误差的非循环能量桥接

需要证明实际 Chebyshev 误差产生的对象如何进入已构造的去常数能量，且构造不能把 \(\psi(X)-X\) 当作系数、投影参数或后验输入。任何使用 `psi(X)-X`、`Chebyshev_error`、`Mellin`、`zeta_zero` 或 `explicit_formula` 的候选都不满足此义务。

## 义务三：dyadic 能量到 Mellin 范数的可和性

即使前两项成立，仍须单独建立跨尺度求和/积分引理，把实际 dyadic 能量控制转换成所需 Mellin 半平面范数控制。该引理必须写明权重、收敛区间、边界项及其不依赖 RH 或零自由区域的来源。

## 状态

```text
uniform_coercivity_proved=false
actual_chebyshev_energy_bridge_proved=false
dyadic_to_mellin_summability_proved=false
actual_mellin_contraction_present=false
rh_proved=false
```

在三项义务全部以独立定理闭合之前，本路线只能视为有限结构审计，不可称为 RH 证明进展。
