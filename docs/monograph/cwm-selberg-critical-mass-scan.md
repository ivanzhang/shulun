# CWM 临界 Selberg 合成权质量扫描

**状态：** `model_weight_scan_not_a_proof`

本扫描使用模型上界权

\[
\lambda_d=\mu(d)\frac{\log(R/d)}{\log R},\qquad d\le R,
\]

并合成

\[
\omega_\ell=\sum_{[d_1,d_2]=\ell}\lambda_{d_1}\lambda_{d_2}.
\]

它不是正式 Selberg 最优权证明，只用于判断 `CWM` 是否现实。

## 总体判断

- 若 `critical_abs_mass` 已明显趋小，则 `CWM` 有希望直接闭合。
- 若 `critical_abs_mass` 不小但 `critical_signed_mass` 很小，则应利用 Selberg 符号相消，转向 signed-CWM。
- 若二者都不小，则应走 `CRD`：临界 lcm 层共振推出 CRTDefect。

## 样本摘要
- P=5003 M=P^1.0 R=P^0.25 Pm=3652.19 R=8 omega=13 critAbs=0 critSigned=0 fracAbs=0.000 maxH=1 mass=0 ellCount=0
- P=5003 M=P^1.0 R=P^0.3 Pm=3652.19 R=12 omega=21 critAbs=0.00149 critSigned=-0.0001982 fracAbs=0.000 maxH=1 mass=0.001443 ellCount=5
- P=5003 M=P^1.0 R=P^0.35 Pm=3652.19 R=19 omega=58 critAbs=0.02345 critSigned=-0.002247 fracAbs=0.001 maxH=1 mass=0.01865 ellCount=35
- P=5003 M=P^1.2 R=P^0.25 Pm=664.84 R=8 omega=13 critAbs=0.06667 critSigned=0.05078 fracAbs=0.002 maxH=1 mass=0.05669 ellCount=7
- P=5003 M=P^1.2 R=P^0.3 Pm=664.84 R=12 omega=21 critAbs=0.1947 critSigned=0.1 fracAbs=0.006 maxH=1 mass=0.1367 ellCount=15
- P=5003 M=P^1.2 R=P^0.35 Pm=664.84 R=19 omega=58 critAbs=0.575 critSigned=0.1464 fracAbs=0.015 maxH=1 mass=0.2965 ellCount=52
- P=5003 M=P^1.4 R=P^0.25 Pm=121.02 R=8 omega=13 critAbs=1.622 critSigned=-0.2902 fracAbs=0.052 maxH=1 mass=0.941 ellCount=12
- P=5003 M=P^1.4 R=P^0.3 Pm=121.02 R=12 omega=21 critAbs=2.676 critSigned=-0.1351 fracAbs=0.077 maxH=1 mass=1.158 ellCount=20
- P=5003 M=P^1.4 R=P^0.35 Pm=121.02 R=19 omega=58 critAbs=4.581 critSigned=0.09761 fracAbs=0.119 maxH=1 mass=1.411 ellCount=57
- P=20011 M=P^1.0 R=P^0.25 Pm=14608.03 R=11 omega=21 critAbs=0 critSigned=0 fracAbs=0.000 maxH=1 mass=0 ellCount=0
- P=20011 M=P^1.0 R=P^0.3 Pm=14608.03 R=19 omega=58 critAbs=0.001036 critSigned=-0.0006389 fracAbs=0.000 maxH=1 mass=0.001036 ellCount=16
- P=20011 M=P^1.0 R=P^0.35 Pm=14608.03 R=32 omega=127 critAbs=0.01542 critSigned=-0.003554 fracAbs=0.000 maxH=1 mass=0.01295 ellCount=73
- P=20011 M=P^1.2 R=P^0.25 Pm=2015.30 R=11 omega=21 critAbs=0.02476 critSigned=0.001782 fracAbs=0.001 maxH=1 mass=0.02206 ellCount=11
- P=20011 M=P^1.2 R=P^0.3 Pm=2015.30 R=19 omega=58 critAbs=0.1579 critSigned=0.02439 fracAbs=0.004 maxH=1 mass=0.1046 ellCount=45
- P=20011 M=P^1.2 R=P^0.35 Pm=2015.30 R=32 omega=127 critAbs=0.5215 critSigned=0.0537 fracAbs=0.012 maxH=1 mass=0.2378 ellCount=114
- P=20011 M=P^1.4 R=P^0.25 Pm=278.03 R=11 omega=21 critAbs=1.25 critSigned=0.1122 fracAbs=0.037 maxH=1 mass=0.6514 ellCount=19
- P=20011 M=P^1.4 R=P^0.3 Pm=278.03 R=19 omega=58 critAbs=2.69 critSigned=0.3155 fracAbs=0.070 maxH=1 mass=0.9383 ellCount=56
- P=20011 M=P^1.4 R=P^0.35 Pm=278.03 R=32 omega=127 critAbs=4.849 critSigned=0.6045 fracAbs=0.112 maxH=1 mass=1.218 ellCount=125
- P=100003 M=P^1.0 R=P^0.25 Pm=73002.19 R=17 omega=46 critAbs=0 critSigned=0 fracAbs=0.000 maxH=1 mass=0 ellCount=0
- P=100003 M=P^1.0 R=P^0.3 Pm=73002.19 R=31 omega=127 critAbs=5.356e-05 critSigned=-8.123e-06 fracAbs=0.000 maxH=1 mass=5.356e-05 ellCount=16
- P=100003 M=P^1.0 R=P^0.35 Pm=73002.19 R=56 omega=348 critAbs=0.007437 critSigned=-0.0006977 fracAbs=0.000 maxH=1 mass=0.006369 ellCount=192
- P=100003 M=P^1.2 R=P^0.25 Pm=7300.18 R=17 omega=46 critAbs=0.01053 critSigned=-0.003218 fracAbs=0.000 maxH=1 mass=0.009544 ellCount=23
- P=100003 M=P^1.2 R=P^0.3 Pm=7300.18 R=31 omega=127 critAbs=0.0958 critSigned=-0.009287 fracAbs=0.002 maxH=1 mass=0.05869 ellCount=98
- P=100003 M=P^1.2 R=P^0.35 Pm=7300.18 R=56 omega=348 critAbs=0.4194 critSigned=-0.003346 fracAbs=0.009 maxH=1 mass=0.1668 ellCount=314
- P=100003 M=P^1.4 R=P^0.25 Pm=730.01 R=17 omega=46 critAbs=0.9242 critSigned=0.2771 fracAbs=0.025 maxH=1 mass=0.4603 ellCount=42
- P=100003 M=P^1.4 R=P^0.3 Pm=730.01 R=31 omega=127 critAbs=2.375 critSigned=0.4194 fracAbs=0.055 maxH=1 mass=0.7454 ellCount=123
- P=100003 M=P^1.4 R=P^0.35 Pm=730.01 R=56 omega=348 critAbs=4.685 critSigned=0.6478 fracAbs=0.098 maxH=1 mass=1.041 ellCount=344

## 对硬点的影响

这一扫描若显示临界绝对质量不随 `P` 下降，就说明不能只靠粗糙绝对值账本闭合 `RSE-CRIT`。
此时应把正式证明目标改为以下二选一：

1. `signed-CWM`：证明 Selberg 合成权在临界带内有足够符号相消；
2. `CRD`：证明临界绝对质量集中必然导致小模投影或短差值方向 CRTDefect。
