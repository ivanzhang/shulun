# SKT 平滑 Selberg 变换扫描

**状态：** `smooth_transform_scan_not_a_proof`

本实验只检查 `SKT` 的平滑部分。核心比较为

\[
M\sum_{h,\ell}\frac{\omega_\ell}{h}F(hP_m/\ell)
\quad\text{与}\quad
-2\pi iH\sum_{h,\ell}\frac{\omega_\ell}{\ell}G(hP_m/\ell).
\]

若 `linear_error_ratio` 小，则可以把 `SKT` 严格化为一维核 `G` 的 Selberg 合成权相消问题。

## 摘要
- P=2003 M=P^1.2 R=P^0.3 terms=28 exact/env=0.390 linear/env=0.392 linearErr/env=0.0227 topH=h1:18,h2:4,h3:0.76
- P=2003 M=P^1.2 R=P^0.35 terms=146 exact/env=0.186 linear/env=0.186 linearErr/env=0.00834 topH=h1:27,h2:9.9,h3:2.8
- P=2003 M=P^1.4 R=P^0.3 terms=72 exact/env=0.024 linear/env=0.026 linearErr/env=0.00332 topH=h2:60,h1:60,h3:32
- P=2003 M=P^1.4 R=P^0.35 terms=216 exact/env=0.088 linear/env=0.089 linearErr/env=0.000747 topH=h2:75,h1:34,h4:26
- P=5003 M=P^1.2 R=P^0.3 terms=57 exact/env=0.086 linear/env=0.084 linearErr/env=0.00669 topH=h1:7.6,h2:2.7,h3:2.1
- P=5003 M=P^1.2 R=P^0.35 terms=308 exact/env=0.010 linear/env=0.012 linearErr/env=0.00224 topH=h1:8.9,h3:5,h2:4.7
- P=5003 M=P^1.4 R=P^0.3 terms=126 exact/env=0.081 linear/env=0.080 linearErr/env=0.0019 topH=h1:71,h2:40,h3:33
- P=5003 M=P^1.4 R=P^0.35 terms=421 exact/env=0.073 linear/env=0.073 linearErr/env=0.000422 topH=h1:1.3e+02,h2:87,h4:57
- P=10007 M=P^1.2 R=P^0.3 terms=120 exact/env=0.285 linear/env=0.285 linearErr/env=0.00383 topH=h1:35,h2:12,h3:3.1
- P=10007 M=P^1.2 R=P^0.35 terms=441 exact/env=0.085 linear/env=0.084 linearErr/env=0.00122 topH=h1:44,h2:23,h3:7.5
- P=10007 M=P^1.4 R=P^0.3 terms=227 exact/env=0.029 linear/env=0.029 linearErr/env=0.000245 topH=h2:85,h1:81,h3:56
- P=10007 M=P^1.4 R=P^0.35 terms=602 exact/env=0.044 linear/env=0.044 linearErr/env=0.00014 topH=h2:1.6e+02,h1:86,h4:72

## 证明含义

- 线性化误差小：临界带振幅因子的一阶展开可作为正式证明入口。
- `linear/env` 小：主要相消已经发生在 Selberg 合成权与一维核 `G` 的卷积中。
- 若某些 `h` 独大，应进一步对固定 `h` 的 `ell`-和证明相消；若多个 `h` 抵消，则需要保留 `h`-平均。

## 下一步接口

将 `SKT` 拆为：

```text
SKT-LIN: 振幅一阶展开误差可吸收；
SKT-TRANS: sum omega_l/l * G(hP_m/l) 的临界变换相消。
```
