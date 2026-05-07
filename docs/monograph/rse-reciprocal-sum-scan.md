# RSE 粗数倒数指数和压力测试

**状态：** `experimental_bottleneck_split_not_a_proof`

本实验只用于定位 `RSE` 的真实瓶颈，不构成证明。扫描对象为

\[
S_{h,\ell}(M)=\sum_{m\sim M,\ P^-(m)>Y}
e\left(\frac{hX}{\ell m}\right)
\left(1-e\left(\frac{hH}{\ell m}\right)\right).
\]

## 参数

- `alpha=0.45`，`beta=0.73`，`H=P`。
- `P-list=[1009, 2003, 5003]`。
- `M=P^u`，`u-list=[1.0, 1.15, 1.3, 1.45]`。
- `h-list=[1, 2, 4, 8]`，`ell/P_m` 比例为 `[0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0]`。

## 总体结论

- 振荡区 `hP_m/ell>=10` 通常有明显归一化抵消，是 `van der Corput + Buchstab` 最可攻的区域。
- 平坦区 `hP_m/ell<1` 的相位不抵消，但振幅因子 `1-e(hH/(ell m))` 很小，适合改用振幅账本吸收。
- 临界区 `1<=hP_m/ell<10` 同时缺少强振荡且振幅未完全衰减，是当前 `RSE` 的最小硬核。
- 因此下一步应把 `RSE` 拆成 `RSE-OSC`、`RSE-AMP`、`RSE-CRIT` 三个子接口；真正需要新想法的是 `RSE-CRIT`。

## 平方后端点特例

新增 `docs/monograph/prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md` 后，
`x=P` 平方后端点的 `CarryDiscrepancy` 也落入同一倒数相位框架。其频率对象为

\[
S_r(P)=\sum_{P/e<a<P}e(rP^2/a)(1-e(rP/a)).
\]

这对应本页模型中的

```text
X=P^2, H=P, m=a~P, ell=1。
```

因此 `hP_m/ell=rP`，属于明显的 `RSE-OSC` 端点振荡区，而非 `RSE-CRIT` 临界带。
这给平方后端点一个更窄的审稿对象：先攻 `ell=1,m~P` 的倒数和 B-process/van der Corput
界；若失败，再把异常低频集中路由到 `HyperbolicDisc/PDEC`。

## 分样本摘要

### P=1009，M=P^1.0，Y=22，P_m=736.57，rough=171
- `oscillatory`: n=11 max|S|/amp=0.115 avg|S|/amp=0.051 max|S|/sqrtAmp2=1.48 max|S|/N=0.0611
- `critical`: n=15 max|S|/amp=0.633 avg|S|/amp=0.223 max|S|/sqrtAmp2=8.11 max|S|/N=0.00375
- `flat`: n=6 max|S|/amp=0.993 avg|S|/amp=0.940 max|S|/sqrtAmp2=12.73 max|S|/N=0.00266
- 最坏归一化项：bucket=flat h=1 ell=5892 hP_m/ell=0.13 |S|/amp=0.993 |S|/N=0.000736
- 最大地板余项：ell=36 E=3.701 E/N=0.0216

### P=1009，M=P^1.15，Y=22，P_m=261.05，rough=489
- `oscillatory`: n=11 max|S|/amp=0.048 avg|S|/amp=0.024 max|S|/sqrtAmp2=1.05 max|S|/N=0.0439
- `critical`: n=15 max|S|/amp=0.643 avg|S|/amp=0.223 max|S|/sqrtAmp2=13.93 max|S|/N=0.00379
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=21.54 max|S|/N=0.00266
- 最坏归一化项：bucket=flat h=1 ell=2088 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.000733
- 最大地板余项：ell=13 E=-5.226 E/N=-0.0107

### P=1009，M=P^1.3，Y=22，P_m=92.48，rough=1378
- `oscillatory`: n=11 max|S|/amp=0.037 avg|S|/amp=0.016 max|S|/sqrtAmp2=1.33 max|S|/N=0.0108
- `critical`: n=15 max|S|/amp=0.640 avg|S|/amp=0.222 max|S|/sqrtAmp2=23.27 max|S|/N=0.00379
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=36.16 max|S|/N=0.00267
- 最坏归一化项：bucket=flat h=1 ell=739 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.000735
- 最大地板余项：ell=4 E=4.014 E/N=0.00291

### P=1009，M=P^1.45，Y=22，P_m=32.77，rough=3883
- `oscillatory`: n=11 max|S|/amp=0.064 avg|S|/amp=0.018 max|S|/sqrtAmp2=3.88 max|S|/N=0.0158
- `critical`: n=15 max|S|/amp=0.639 avg|S|/amp=0.223 max|S|/sqrtAmp2=39.04 max|S|/N=0.00378
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=60.69 max|S|/N=0.00268
- 最坏归一化项：bucket=flat h=1 ell=262 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.000735
- 最大地板余项：ell=16 E=-4.485 E/N=-0.00115

### P=2003，M=P^1.0，Y=30，P_m=1462.19，rough=313
- `oscillatory`: n=11 max|S|/amp=0.071 avg|S|/amp=0.043 max|S|/sqrtAmp2=1.24 max|S|/N=0.0169
- `critical`: n=15 max|S|/amp=0.641 avg|S|/amp=0.222 max|S|/sqrtAmp2=11.12 max|S|/N=0.00191
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=17.23 max|S|/N=0.00134
- 最坏归一化项：bucket=flat h=1 ell=11697 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.00037
- 最大地板余项：ell=365 E=-0.594 E/N=-0.0019

### P=2003，M=P^1.15，Y=30，P_m=467.48，rough=993
- `oscillatory`: n=11 max|S|/amp=0.036 avg|S|/amp=0.017 max|S|/sqrtAmp2=1.12 max|S|/N=0.014
- `critical`: n=15 max|S|/amp=0.641 avg|S|/amp=0.222 max|S|/sqrtAmp2=19.81 max|S|/N=0.00191
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=30.69 max|S|/N=0.00134
- 最坏归一化项：bucket=flat h=1 ell=3739 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.00037
- 最大地板余项：ell=46 E=-0.784 E/N=-0.000789

### P=2003，M=P^1.3，Y=30，P_m=149.46，rough=3102
- `oscillatory`: n=11 max|S|/amp=0.056 avg|S|/amp=0.017 max|S|/sqrtAmp2=3.03 max|S|/N=0.00576
- `critical`: n=15 max|S|/amp=0.640 avg|S|/amp=0.220 max|S|/sqrtAmp2=34.95 max|S|/N=0.00191
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=54.25 max|S|/N=0.00135
- 最坏归一化项：bucket=flat h=1 ell=1195 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.00037
- 最大地板余项：ell=14 E=-1.705 E/N=-0.00055

### P=2003，M=P^1.45，Y=30，P_m=47.78，rough=9677
- `oscillatory`: n=11 max|S|/amp=0.035 avg|S|/amp=0.014 max|S|/sqrtAmp2=3.41 max|S|/N=0.00205
- `critical`: n=15 max|S|/amp=0.640 avg|S|/amp=0.228 max|S|/sqrtAmp2=61.76 max|S|/N=0.00191
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=95.82 max|S|/N=0.00135
- 最坏归一化项：bucket=flat h=1 ell=382 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.00037
- 最大地板余项：ell=2 E=5.402 E/N=0.000558

### P=5003，M=P^1.0，Y=46，P_m=3652.19，rough=698
- `oscillatory`: n=11 max|S|/amp=0.045 avg|S|/amp=0.016 max|S|/sqrtAmp2=1.17 max|S|/N=0.00173
- `critical`: n=15 max|S|/amp=0.639 avg|S|/amp=0.226 max|S|/sqrtAmp2=16.54 max|S|/N=0.000761
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=25.73 max|S|/N=0.000537
- 最坏归一化项：bucket=flat h=1 ell=29217 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.000148
- 最大地板余项：ell=913 E=-0.530 E/N=-0.000759

### P=5003，M=P^1.15，Y=46，P_m=1017.82，rough=2554
- `oscillatory`: n=11 max|S|/amp=0.026 avg|S|/amp=0.012 max|S|/sqrtAmp2=1.27 max|S|/N=0.00126
- `critical`: n=15 max|S|/amp=0.642 avg|S|/amp=0.224 max|S|/sqrtAmp2=31.80 max|S|/N=0.000765
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=49.23 max|S|/N=0.000537
- 最坏归一化项：bucket=flat h=1 ell=8142 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.000148
- 最大地板余项：ell=254 E=1.059 E/N=0.000414

### P=5003，M=P^1.3，Y=46，P_m=283.65，rough=9165
- `oscillatory`: n=11 max|S|/amp=0.027 avg|S|/amp=0.013 max|S|/sqrtAmp2=2.49 max|S|/N=0.0012
- `critical`: n=15 max|S|/amp=0.641 avg|S|/amp=0.220 max|S|/sqrtAmp2=60.15 max|S|/N=0.000764
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=93.25 max|S|/N=0.000538
- 最坏归一化项：bucket=flat h=1 ell=2269 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.000148
- 最大地板余项：ell=28 E=-1.623 E/N=-0.000177

### P=5003，M=P^1.45，Y=46，P_m=79.05，rough=32740
- `oscillatory`: n=11 max|S|/amp=0.055 avg|S|/amp=0.019 max|S|/sqrtAmp2=9.76 max|S|/N=0.000959
- `critical`: n=15 max|S|/amp=0.641 avg|S|/amp=0.223 max|S|/sqrtAmp2=113.68 max|S|/N=0.000765
- `flat`: n=6 max|S|/amp=0.994 avg|S|/amp=0.941 max|S|/sqrtAmp2=176.24 max|S|/N=0.000538
- 最坏归一化项：bucket=flat h=1 ell=632 hP_m/ell=0.13 |S|/amp=0.994 |S|/N=0.000148
- 最大地板余项：ell=7 E=10.832 E/N=0.000331

## 对证明链的硬约束

实验把原来的单个 `RSE` 接口压缩为三段：

1. `RSE-OSC`：证明 `hP_m/ell>=L` 时粗数倒数相位的平均抵消。
2. `RSE-AMP`：证明 `hP_m/ell<1/L` 时振幅小量在 Selberg 二次权平均后可吸收。
3. `RSE-CRIT`：处理 `1/L<=hP_m/ell<L` 的薄临界带，这是当前唯一不能由振荡或振幅直接解释的剩余硬点。

其中 `L` 可取 `log^A P`。若能证明临界带在 Selberg 合成权下的总质量只占 `o(|G_Y(I)|)`，则

```text
RSE-OSC + RSE-AMP + RSE-CRIT => RSE => BSI => PTA-GSL。
```
