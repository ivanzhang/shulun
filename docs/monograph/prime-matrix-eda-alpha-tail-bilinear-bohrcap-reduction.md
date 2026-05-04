# AlphaTail 双线性 Fourier 证书到 Bohr-cap 能量

**状态：** `alpha_tail_bilinear_bohrcap_reduction_open`

本文继续压缩 `WSS` 的双线性 Fourier 证书。目标是把

\[
B_h(M,D)=\sum_{m\in M}\sum_{d\in D}e(hmd/Q)
\tag{BBC-1}
\]

的大值改写成更几何的对象：`D` 的差集必须在频率 `h/Q` 的短 Bohr 弧上聚集；否则普通矩形核
预算已经足以吸收。

## 1. 区间核平方展开

令 `M=[M_0,M_1]` 为互补因子区间，`L=|M|`，`D` 为高块中的低素 squarefree 集合。
记

\[
\alpha={h\over Q},\qquad e(t)=e^{2\pi i t}.
\tag{BBC-2}
\]

定义区间核

\[
K_M(t)=\sum_{m\in M}e(\alpha mt).
\tag{BBC-3}
\]

则

\[
|B_h(M,D)|^2
=
\sum_{d,d'\in D}K_M(d-d').
\tag{BBC-4}
\]

因此

\[
|B_h(M,D)|^2
\le
L|D|+
\sum_{\substack{d,d'\in D\\ d\ne d'}}
|K_M(d-d')|.
\tag{BBC-5}
\]

## 2. Bohr-cap 二分

对任意 `T>=1`，定义 Bohr 差集计数

\[
\mathcal P_T(D;h,Q)
=
\#\left\{(d,d')\in D^2:d\ne d',\
\left\|{h(d-d')\over Q}\right\|\le {1\over T}
\right\}.
\tag{BBC-6}
\]

区间核有标准界

\[
|K_M(t)|\le \min\left(L,{1\over 2\|\alpha t\|}\right).
\tag{BBC-7}
\]

于是

\[
|B_h(M,D)|^2
\le
L|D|+L\mathcal P_T(D;h,Q)+{T\over2}|D|^2.
\tag{BBC-8}
\]

**证明。**  
对角项贡献 `L|D|`。非对角中，若 `(d,d')` 落入 `(BBC-6)` 的 Bohr cap，用平凡界 `L`；
否则由 `(BBC-7)` 得 `|K_M(d-d')|<=T/2`。求和即得。证毕。

## 3. 大双线性和推出 Bohr 聚集

设

\[
|B_h(M,D)|\ge \Xi.
\tag{BBC-9}
\]

若

\[
\Xi^2>L|D|+{T\over2}|D|^2,
\tag{BBC-10}
\]

则

\[
\mathcal P_T(D;h,Q)
\ge
{\Xi^2-L|D|-(T/2)|D|^2\over L}.
\tag{BBC-11}
\]

这就是 `Bohr-cap certificate`：频率证书不能仅以总相位大值存在；它强制 `D` 中大量差值
`d-d'` 使 `h(d-d')/Q` 接近整数。

## 4. 与 AlphaTail 结构的结合

在 AlphaTail 中，`D` 不是任意集合，而是

```text
D = {d in (B,2B] : d squarefree, P^+(d)<=0.9p, mu(d)=-1}
```

或对应正符号集合。`D` 的元素全由低素数生成，同时还落在固定高 dyadic 块。

因此 `(BBC-11)` 有三种出口：

1. **Bohr-cap/PDEC。**  
   若同一频率或同一低模投影在无限多 `p` 上持续出现，得到持久 Fourier/CRT 缺陷。
2. **Bohr-cap/ColumnCRT。**  
   若聚集对应到固定列残基差，说明低素 squarefree 核的列相位不是 CRT 均衡。
3. **Sparse SAE。**  
   若只在单个窗口、单个频率偶发，则进入 sparse endpoint escape。

## 5. 审稿边界

已证明：

```text
大双线性 Fourier 证书
=> 普通矩形预算足够，或 D 差集出现 Bohr-cap 聚集。
```

尚未证明：

```text
Bohr-cap 聚集不可能。
```

下一步最小硬点变为：对低素 squarefree 高块集合 `D` 证明 Bohr-cap 差集计数上界，或证明其失败
必产生可排斥的 `PDEC/ColumnCRT/SAE` 证书。

## 6. 低频警告与正确使用

`(BBC-11)` 只能解释振荡频率上的大值。若 `h` 很小，则

\[
e(hmd/Q)
\]

在整个互补因子矩形上变化缓慢，`B_h(M,D)` 可以接近 `|M||D|`。这不是 PDEC 缺陷，而是
Fourier 展开中连续短区间核的平滑低频部分。它必须先由 `CIN` 中的 local/global model mismatch
分支吸收。

因此正式链条应写成：

```text
WSS excess
=> low-frequency model mismatch
   或 high-frequency bilinear certificate
=> high-frequency Bohr-cap / PDEC / ColumnCRT / SAE.
```

脚本审计也确认这一点：全矩形未中心化审计中，最佳频率通常是 `h=1`，其巨大数值只说明低频
平滑项存在，不能被误读为反例缺陷。

审计脚本：

```text
experiments/prime_matrix_alpha_tail_bilinear_bohr_audit.py
```

样本：

| p | block | sign | m count | d count | best h | best abs | best norm |
|---:|---:|:---:|---:|---:|---:|---:|---:|
| 997 | 4096 | - | 121 | 697 | 1 | 75082.701523 | 258.541829 |
| 5003 | 8192 | - | 1529 | 1645 | 1 | 2228855.725453 | 1405.384837 |
| 10007 | 16384 | - | 3056 | 3338 | 1 | 9058607.164540 | 2836.230907 |

这组数据促使下一步必须先严写低频平滑吸收，再攻击高频 Bohr-cap。
