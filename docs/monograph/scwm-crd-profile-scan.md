# signed-CWM / CRD 临界带剖面扫描

**状态：** `experimental_route_selection_not_a_proof`

本实验同时扫描三件事：

1. 临界带 Selberg 合成权的 signed/absolute 比例；
2. 真实粗数倒数核加权后的 signed-kernel/absolute-envelope 比例；
3. 临界质量在 `ell` 的小素支撑上的集中程度，用于判断是否转向 CRD。

实验仍不是证明；它只决定下一步应严攻 `signed-CWM` 还是 `CRD`。

## 摘要
- P=2003 M=P^1.0 R=P^0.3 terms=3 rough=313 sample=313 absMass=0.006045 signedMassRatio=0.421 signedKernelRatio=0.680 posNegBal=0.421 topPrime=5 share=0.834 verdict=CRD-prime-concentration
- P=2003 M=P^1.0 R=P^0.35 terms=50 rough=313 sample=313 absMass=0.03743 signedMassRatio=0.074 signedKernelRatio=0.421 posNegBal=0.074 topPrime=5 share=0.608 verdict=CRD-prime-concentration
- P=2003 M=P^1.2 R=P^0.3 terms=28 rough=1458 sample=1458 absMass=0.2842 signedMassRatio=0.618 signedKernelRatio=0.433 posNegBal=0.618 topPrime=2 share=0.672 verdict=CRD-prime-concentration
- P=2003 M=P^1.2 R=P^0.35 terms=146 rough=1458 sample=1458 absMass=0.633 signedMassRatio=0.402 signedKernelRatio=0.215 posNegBal=0.402 topPrime=2 share=0.572 verdict=CRD-prime-concentration
- P=2003 M=P^1.4 R=P^0.3 terms=72 rough=6615 sample=6615 absMass=2.526 signedMassRatio=0.195 signedKernelRatio=0.035 posNegBal=0.195 topPrime=2 share=0.515 verdict=signed-CWM-promising
- P=2003 M=P^1.4 R=P^0.35 terms=216 rough=6615 sample=6615 absMass=3.836 signedMassRatio=0.117 signedKernelRatio=0.096 posNegBal=0.117 topPrime=2 share=0.479 verdict=signed-CWM-promising
- P=5003 M=P^1.0 R=P^0.3 terms=6 rough=698 sample=698 absMass=0.00149 signedMassRatio=0.133 signedKernelRatio=0.769 posNegBal=0.133 topPrime=11 share=0.695 verdict=CRD-prime-concentration
- P=5003 M=P^1.0 R=P^0.35 terms=89 rough=698 sample=698 absMass=0.02345 signedMassRatio=0.096 signedKernelRatio=0.283 posNegBal=0.096 topPrime=5 share=0.556 verdict=CRD-prime-concentration
- P=5003 M=P^1.2 R=P^0.3 terms=57 rough=3918 sample=3918 absMass=0.1945 signedMassRatio=0.515 signedKernelRatio=0.174 posNegBal=0.515 topPrime=5 share=0.615 verdict=CRD-prime-concentration
- P=5003 M=P^1.2 R=P^0.35 terms=308 rough=3918 sample=3918 absMass=0.5542 signedMassRatio=0.279 signedKernelRatio=0.060 posNegBal=0.279 topPrime=2 share=0.518 verdict=CRD-prime-concentration
- P=5003 M=P^1.4 R=P^0.3 terms=126 rough=21400 sample=10000 absMass=2.476 signedMassRatio=0.060 signedKernelRatio=0.098 posNegBal=0.060 topPrime=2 share=0.552 verdict=signed-CWM-promising
- P=5003 M=P^1.4 R=P^0.35 terms=421 rough=21400 sample=10000 absMass=3.863 signedMassRatio=0.021 signedKernelRatio=0.080 posNegBal=0.021 topPrime=2 share=0.497 verdict=signed-CWM-promising
- P=10007 M=P^1.0 R=P^0.3 terms=13 rough=1290 sample=1290 absMass=0.0009125 signedMassRatio=0.098 signedKernelRatio=0.536 posNegBal=0.098 topPrime=13 share=0.617 verdict=CRD-prime-concentration
- P=10007 M=P^1.0 R=P^0.35 terms=110 rough=1290 sample=1290 absMass=0.02042 signedMassRatio=0.182 signedKernelRatio=0.204 posNegBal=0.182 topPrime=2 share=0.438 verdict=CRD-prime-concentration
- P=10007 M=P^1.2 R=P^0.3 terms=120 rough=8370 sample=8370 absMass=0.1852 signedMassRatio=0.398 signedKernelRatio=0.296 posNegBal=0.398 topPrime=3 share=0.564 verdict=CRD-prime-concentration
- P=10007 M=P^1.2 R=P^0.35 terms=441 rough=8370 sample=8370 absMass=0.5517 signedMassRatio=0.219 signedKernelRatio=0.095 posNegBal=0.219 topPrime=2 share=0.483 verdict=CRD-prime-concentration
- P=10007 M=P^1.4 R=P^0.3 terms=227 rough=52466 sample=10000 absMass=2.252 signedMassRatio=0.067 signedKernelRatio=0.035 posNegBal=0.067 topPrime=3 share=0.465 verdict=signed-CWM-promising
- P=10007 M=P^1.4 R=P^0.35 terms=602 rough=52466 sample=10000 absMass=3.819 signedMassRatio=0.050 signedKernelRatio=0.048 posNegBal=0.050 topPrime=3 share=0.402 verdict=signed-CWM-promising

## 证明路线判读

- `signedKernelRatio` 小：真实 RSE 核已经在 Selberg 符号权下相消，优先严写 signed-CWM。
- `signedMassRatio` 小但 `signedKernelRatio` 不小：权重本身有相消，但相位核与符号相关，需要 kernel-signed-CWM。
- `topPrime share` 大：临界 lcm 质量集中到少数小素支撑，应转向 CRD 辅助模缺陷。
- 三者混合：需要二分定理，不应单独假设绝对 CWM。

## 最坏贡献项

### P=2003 M=P^1.0 R=P^0.3
- h=1 ell=30 theta=48.740 w=-0.0987 |K|=0.976 |contrib|=0.0963 supp=3 factors=[2, 3, 5]
- h=1 ell=42 theta=34.814 w=-0.0422 |K|=2.12 |contrib|=0.0895 supp=3 factors=[2, 3, 7]
- h=1 ell=35 theta=41.777 w=0.0612 |K|=1.31 |contrib|=0.0802 supp=2 factors=[5, 7]

### P=2003 M=P^1.0 R=P^0.35
- h=1 ell=42 theta=34.814 w=-0.169 |K|=2.12 |contrib|=0.358 supp=3 factors=[2, 3, 7]
- h=1 ell=30 theta=48.740 w=-0.317 |K|=0.976 |contrib|=0.31 supp=3 factors=[2, 3, 5]
- h=1 ell=35 theta=41.777 w=0.205 |K|=1.31 |contrib|=0.269 supp=2 factors=[5, 7]
- h=1 ell=33 theta=44.309 w=0.107 |K|=1.32 |contrib|=0.141 supp=2 factors=[3, 11]
- h=1 ell=70 theta=20.888 w=-0.067 |K|=1.13 |contrib|=0.0755 supp=3 factors=[2, 5, 7]

### P=2003 M=P^1.2 R=P^0.3
- h=1 ell=6 theta=53.277 w=0.65 |K|=3.52 |contrib|=2.29 supp=2 factors=[2, 3]
- h=1 ell=15 theta=21.311 w=0.268 |K|=3.14 |contrib|=0.841 supp=2 factors=[3, 5]
- h=2 ell=15 theta=42.622 w=0.268 |K|=3.44 |contrib|=0.461 supp=2 factors=[3, 5]
- h=1 ell=14 theta=22.833 w=0.157 |K|=2.66 |contrib|=0.416 supp=2 factors=[2, 7]
- h=1 ell=21 theta=15.222 w=0.114 |K|=2.98 |contrib|=0.341 supp=2 factors=[3, 7]

### P=2003 M=P^1.2 R=P^0.35
- h=1 ell=6 theta=53.277 w=0.758 |K|=3.52 |contrib|=2.67 supp=2 factors=[2, 3]
- h=1 ell=15 theta=21.311 w=0.455 |K|=3.14 |contrib|=1.43 supp=2 factors=[3, 5]
- h=1 ell=14 theta=22.833 w=0.387 |K|=2.66 |contrib|=1.03 supp=2 factors=[2, 7]
- h=1 ell=21 theta=15.222 w=0.307 |K|=2.98 |contrib|=0.914 supp=2 factors=[3, 7]
- h=1 ell=30 theta=10.655 w=-0.317 |K|=2.82 |contrib|=0.896 supp=3 factors=[2, 3, 5]

### P=2003 M=P^1.4 R=P^0.3
- h=1 ell=2 theta=34.939 w=-0.9 |K|=12.8 |contrib|=11.5 supp=1 factors=[2]
- h=1 ell=3 theta=23.292 w=-0.75 |K|=12.2 |contrib|=9.17 supp=1 factors=[3]
- h=1 ell=6 theta=11.646 w=0.65 |K|=8.05 |contrib|=5.24 supp=2 factors=[2, 3]
- h=1 ell=10 theta=6.988 w=0.366 |K|=13.5 |contrib|=4.94 supp=2 factors=[2, 5]
- h=2 ell=6 theta=23.292 w=0.65 |K|=12.2 |contrib|=3.97 supp=2 factors=[2, 3]

### P=2003 M=P^1.4 R=P^0.35
- h=1 ell=2 theta=34.939 w=-0.931 |K|=12.8 |contrib|=11.9 supp=1 factors=[2]
- h=1 ell=3 theta=23.292 w=-0.827 |K|=12.2 |contrib|=10.1 supp=1 factors=[3]
- h=1 ell=10 theta=6.988 w=0.559 |K|=13.5 |contrib|=7.54 supp=2 factors=[2, 5]
- h=1 ell=6 theta=11.646 w=0.758 |K|=8.05 |contrib|=6.1 supp=2 factors=[2, 3]
- h=1 ell=15 theta=4.658 w=0.455 |K|=11.9 |contrib|=5.42 supp=2 factors=[3, 5]

### P=5003 M=P^1.0 R=P^0.3
- h=1 ell=70 theta=52.174 w=-0.0318 |K|=1.06 |contrib|=0.0337 supp=3 factors=[2, 5, 7]
- h=1 ell=66 theta=55.336 w=-0.0195 |K|=0.891 |contrib|=0.0174 supp=3 factors=[2, 3, 11]
- h=1 ell=55 theta=66.403 w=0.0247 |K|=0.471 |contrib|=0.0116 supp=2 factors=[5, 11]
- h=1 ell=77 theta=47.431 w=0.0152 |K|=0.204 |contrib|=0.0031 supp=2 factors=[7, 11]
- h=1 ell=110 theta=33.202 w=-0.00514 |K|=0.379 |contrib|=0.00195 supp=3 factors=[2, 5, 11]

### P=5003 M=P^1.0 R=P^0.35
- h=1 ell=70 theta=52.174 w=-0.197 |K|=1.06 |contrib|=0.208 supp=3 factors=[2, 5, 7]
- h=1 ell=66 theta=55.336 w=-0.145 |K|=0.891 |contrib|=0.13 supp=3 factors=[2, 3, 11]
- h=1 ell=55 theta=66.403 w=0.168 |K|=0.471 |contrib|=0.0793 supp=2 factors=[5, 11]
- h=1 ell=51 theta=71.612 w=0.0474 |K|=1.44 |contrib|=0.068 supp=2 factors=[3, 17]
- h=1 ell=105 theta=34.783 w=-0.0545 |K|=1.21 |contrib|=0.0657 supp=3 factors=[3, 5, 7]

### P=5003 M=P^1.2 R=P^0.3
- h=1 ell=10 theta=66.484 w=0.503 |K|=3.72 |contrib|=1.87 supp=2 factors=[2, 5]
- h=1 ell=15 theta=44.323 w=0.393 |K|=1.86 |contrib|=0.73 supp=2 factors=[3, 5]
- h=1 ell=14 theta=47.489 w=0.313 |K|=2.08 |contrib|=0.651 supp=2 factors=[2, 7]
- h=1 ell=21 theta=31.659 w=0.242 |K|=2.51 |contrib|=0.608 supp=2 factors=[3, 7]
- h=1 ell=35 theta=18.996 w=0.153 |K|=3.01 |contrib|=0.46 supp=2 factors=[5, 7]

### P=5003 M=P^1.2 R=P^0.35
- h=1 ell=10 theta=66.484 w=0.646 |K|=3.72 |contrib|=2.4 supp=2 factors=[2, 5]
- h=1 ell=21 theta=31.659 w=0.425 |K|=2.51 |contrib|=1.07 supp=2 factors=[3, 7]
- h=1 ell=14 theta=47.489 w=0.508 |K|=2.08 |contrib|=1.06 supp=2 factors=[2, 7]
- h=1 ell=15 theta=44.323 w=0.562 |K|=1.86 |contrib|=1.04 supp=2 factors=[3, 5]
- h=1 ell=35 theta=18.996 w=0.308 |K|=3.01 |contrib|=0.927 supp=2 factors=[5, 7]

### P=5003 M=P^1.4 R=P^0.3
- h=1 ell=2 theta=60.511 w=-0.922 |K|=14.4 |contrib|=13.3 supp=1 factors=[2]
- h=1 ell=3 theta=40.340 w=-0.805 |K|=9.93 |contrib|=7.99 supp=1 factors=[3]
- h=1 ell=7 theta=17.289 w=-0.387 |K|=15.7 |contrib|=6.06 supp=1 factors=[7]
- h=1 ell=6 theta=20.170 w=0.727 |K|=7.24 |contrib|=5.27 supp=2 factors=[2, 3]
- h=1 ell=14 theta=8.644 w=0.313 |K|=15.2 |contrib|=4.75 supp=2 factors=[2, 7]

### P=5003 M=P^1.4 R=P^0.35
- h=1 ell=2 theta=60.511 w=-0.945 |K|=14.4 |contrib|=13.6 supp=1 factors=[2]
- h=1 ell=7 theta=17.289 w=-0.563 |K|=15.7 |contrib|=8.82 supp=1 factors=[7]
- h=1 ell=3 theta=40.340 w=-0.861 |K|=9.93 |contrib|=8.54 supp=1 factors=[3]
- h=1 ell=14 theta=8.644 w=0.508 |K|=15.2 |contrib|=7.72 supp=2 factors=[2, 7]
- h=1 ell=11 theta=11.002 w=-0.337 |K|=17.5 |contrib|=5.9 supp=1 factors=[11]

### P=10007 M=P^1.0 R=P^0.3
- h=1 ell=110 theta=66.410 w=-0.0343 |K|=1.06 |contrib|=0.0364 supp=3 factors=[2, 5, 11]
- h=1 ell=91 theta=80.276 w=0.0297 |K|=0.847 |contrib|=0.0252 supp=2 factors=[7, 13]
- h=1 ell=143 theta=51.085 w=0.0121 |K|=0.566 |contrib|=0.00685 supp=2 factors=[11, 13]
- h=1 ell=154 theta=47.436 w=-0.00584 |K|=1.09 |contrib|=0.00638 supp=3 factors=[2, 7, 11]
- h=1 ell=130 theta=56.193 w=-0.0158 |K|=0.355 |contrib|=0.00561 supp=3 factors=[2, 5, 13]

### P=10007 M=P^1.0 R=P^0.35
- h=1 ell=110 theta=66.410 w=-0.162 |K|=1.06 |contrib|=0.172 supp=3 factors=[2, 5, 11]
- h=1 ell=91 theta=80.276 w=0.161 |K|=0.847 |contrib|=0.136 supp=2 factors=[7, 13]
- h=1 ell=154 theta=47.436 w=-0.109 |K|=1.09 |contrib|=0.119 supp=3 factors=[2, 7, 11]
- h=1 ell=105 theta=69.572 w=-0.162 |K|=0.621 |contrib|=0.101 supp=3 factors=[3, 5, 7]
- h=1 ell=102 theta=71.619 w=-0.106 |K|=0.797 |contrib|=0.0847 supp=3 factors=[2, 3, 17]

### P=10007 M=P^1.2 R=P^0.3
- h=1 ell=15 theta=77.176 w=0.482 |K|=4.4 |contrib|=2.12 supp=2 factors=[3, 5]
- h=1 ell=30 theta=38.588 w=-0.351 |K|=3.75 |contrib|=1.32 supp=3 factors=[2, 3, 5]
- h=1 ell=21 theta=55.125 w=0.335 |K|=3.82 |contrib|=1.28 supp=2 factors=[3, 7]
- h=1 ell=14 theta=82.688 w=0.418 |K|=2.83 |contrib|=1.18 supp=2 factors=[2, 7]
- h=1 ell=35 theta=33.075 w=0.228 |K|=3.91 |contrib|=0.892 supp=2 factors=[5, 7]

### P=10007 M=P^1.2 R=P^0.35
- h=1 ell=15 theta=77.176 w=0.634 |K|=4.4 |contrib|=2.79 supp=2 factors=[3, 5]
- h=1 ell=30 theta=38.588 w=-0.584 |K|=3.75 |contrib|=2.19 supp=3 factors=[2, 3, 5]
- h=1 ell=21 theta=55.125 w=0.518 |K|=3.82 |contrib|=1.98 supp=2 factors=[3, 7]
- h=1 ell=14 theta=82.688 w=0.588 |K|=2.83 |contrib|=1.67 supp=2 factors=[2, 7]
- h=1 ell=22 theta=52.620 w=0.399 |K|=4.01 |contrib|=1.6 supp=2 factors=[2, 11]

### P=10007 M=P^1.4 R=P^0.3
- h=1 ell=3 theta=61.148 w=-0.835 |K|=19.1 |contrib|=16 supp=1 factors=[3]
- h=1 ell=6 theta=30.574 w=0.77 |K|=17.1 |contrib|=13.2 supp=2 factors=[2, 3]
- h=1 ell=5 theta=36.689 w=-0.647 |K|=19.4 |contrib|=12.5 supp=1 factors=[5]
- h=1 ell=14 theta=13.103 w=0.418 |K|=21.3 |contrib|=8.93 supp=2 factors=[2, 7]
- h=1 ell=10 theta=18.344 w=0.581 |K|=12.7 |contrib|=7.37 supp=2 factors=[2, 5]

### P=10007 M=P^1.4 R=P^0.35
- h=1 ell=3 theta=61.148 w=-0.884 |K|=19.1 |contrib|=16.9 supp=1 factors=[3]
- h=1 ell=5 theta=36.689 w=-0.75 |K|=19.4 |contrib|=14.5 supp=1 factors=[5]
- h=1 ell=6 theta=30.574 w=0.837 |K|=17.1 |contrib|=14.3 supp=2 factors=[2, 3]
- h=1 ell=14 theta=13.103 w=0.588 |K|=21.3 |contrib|=12.6 supp=2 factors=[2, 7]
- h=1 ell=21 theta=8.735 w=0.518 |K|=19.8 |contrib|=10.3 supp=2 factors=[3, 7]

## 当前硬攻结论

实验支持把 `RSE-CRIT` 写成更精确的核版本二分：

```text
kernel-signed-CWM 成立
=> 临界 RSE 加权和直接可吸收；

kernel-signed-CWM 失败
=> 权重符号与倒数相位核同向相关
=> 临界 lcm 支撑在小素/短差值方向集中
=> CRD。
```

下一步正式证明应避免只估计 `sum |omega_l|/l`，而应保留 Selberg 符号与实际 RSE 核。
