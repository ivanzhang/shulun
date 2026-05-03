# BPN-BK 尾项核心桶二分定理

**状态：** `tail_budget_reduced_to_tail_core_bucket_defect`

本文继续收窄 `BPN-BK` 剩余硬点。目标不是直接估计全部尾项，而是证明一个严格二分：

```text
边界零行
=> BK-DEC
   或 TailCoreBucket/CoreK-Density。
```

这样，“尾项预算”不再是模糊黑箱；若预算失败，它必须输出一个可审查的尾核心桶过密证书。

## 1. 尾项与尾核心关联

沿用 `prime-matrix-bpn-bk-dec-bridge-proof.md` 的符号。令

\[
I_r=[(r-1)P+1,rP-1]\cap\mathbb Z.
\]

对奇数 `K` 与 level `D`，低阶外尾项为

\[
R_{K,>D}(r)=
\sum_{\substack{d|M_{<P}\\ \omega(d)\le K\\ d>D}}\mu(d)A_d(r).
\]

定义其绝对关联质量

\[
U_{K,D}(r)=
\sum_{\substack{d|M_{<P}\\ \omega(d)\le K\\ d>D}}A_d(r).
\tag{1}
\]

显然

\[
|R_{K,>D}(r)|\le U_{K,D}(r).
\tag{2}
\]

把 `(1)` 展开为点-核心关联：

\[
U_{K,D}(r)
=
\#\{(n,d):n\in I_r,\ d|n,\ d|M_{<P},\ \omega(d)\le K,\ d>D\}.
\tag{3}
\]

这就是尾项的刚性意义：尾项大不是随机误差大，而是短窗中出现了大量
“由 `<P` 小素数组成的大 squarefree 核心 `d`”。

## 2. TailCoreBucket 定义

取尾关联集合

\[
\Omega_{K,D}(r)=
\{(n,d):n\in I_r,\ d|n,\ d|M_{<P},\ \omega(d)\le K,\ d>D\}.
\]

取一个有限分块族 `\mathfrak C`，把所有可能的 `(n,d)` 按以下坐标分块：

1. `d` 的 dyadic 尺度；
2. 互补因子 `a=n/d` 的 dyadic 尺度；
3. `\omega(d)`；
4. 可选的低模相位 `d mod m` 或 `a mod m`。

对块 `C∈\mathfrak C` 定义

\[
U_C(r)=\#(\Omega_{K,D}(r)\cap C).
\]

**Definition TCB（尾核心桶缺陷）。**
若存在 `C∈\mathfrak C` 使

\[
U_C(r)\ge \eta_C,
\tag{TCB}
\]

则称 `I_r` 触发 `TailCoreBucket/CoreK-Density` 缺陷。

该定义统一覆盖两种情况：

```text
小/中 d 桶过密：固定核心倍数或窄走廊过密；
大 d≈n 桶过密：互补因子 a 很小，形成 Tail-anchor。
```

## 3. 零行二分定理

令

\[
V_{K,D}=\sum_{\substack{d|M_{<P}\\ \omega(d)\le K\\ d\le D}}\frac{\mu(d)}d,
\]

并取尾预算阈值 `T>0`。设

\[
\Delta=(P-1)V_{K,D}-T>0.
\tag{4}
\]

**Theorem BKT-1（BK-DEC 或尾核心桶）。**
若 `I_r` 是边界零行，则至少发生以下二者之一：

1. `BK-DEC`：

\[
E_{K,D}(r)\le-\Delta;
\tag{5}
\]

2. 尾核心过量：

\[
U_{K,D}(r)>T.
\tag{6}
\]

**证明。**
由 BK 分解

\[
S_K(r)=(P-1)V_{K,D}+E_{K,D}(r)+R_{K,>D}(r).
\]

边界零行中每个 `n` 都有 `\omega_P(n)\ge1`，奇阶 BK 权满足
`b_K(\omega_P(n))<=0`，故 `S_K(r)<=0`。

若 `(5)` 不成立，则

\[
E_{K,D}(r)>-\Delta=-(P-1)V_{K,D}+T.
\]

代回 `S_K(r)<=0` 得

\[
0\ge (P-1)V_{K,D}+E_{K,D}(r)+R_{K,>D}(r)
>T+R_{K,>D}(r),
\]

所以

\[
R_{K,>D}(r)<-T.
\]

由 `(2)` 得 `U_{K,D}(r)\ge |R_{K,>D}(r)|>T`。证毕。

**Corollary BKT-2（尾项失败必给桶证书）。**
若 `U_{K,D}(r)>T`，则对任意有限分块 `\mathfrak C`，存在 `C∈\mathfrak C`
使

\[
U_C(r)> \frac{T}{|\mathfrak C|}.
\tag{7}
\]

因此取 `\eta_C=T/|\mathfrak C|` 时，`TailCoreBucket/CoreK-Density` 必发生。

**证明。**
若所有块均满足 `U_C(r)<=T/|\mathfrak C|`，则求和得
`U_{K,D}(r)<=T`，矛盾。证毕。

## 4. 与 CoreK 的关系

若某个 `n` 被计入 `U_{K,D}`，则 `n` 有一个由 `<P` 小素数组成的 squarefree
核心 `d>D`。若同一 `n` 承载许多这样的 `d`，则 `\omega_P(n)` 必大，直接进入
`CoreK` 高重惩罚。若许多不同 `n` 各承载少数这样的 `d`，则这些 `n=ad`
在短窗 `I_r` 中形成固定互补因子或窄 dyadic 走廊过密，即 `Tail-anchor`。

形式化地，任取阈值 `H>=1`。将

\[
\Omega_{K,D}(r)
=\Omega_{\rm heavy}\sqcup\Omega_{\rm spread}
\]

其中 `\Omega_heavy` 来自 `u(n)>H` 的点，

\[
u(n)=\#\{d:(n,d)\in\Omega_{K,D}(r)\}.
\]

若 `|\Omega_heavy|>T/2`，则某些点有大量尾核心，给出 `CoreK` 高重集中；
若 `|\Omega_spread|>T/2`，则至少 `T/(2H)` 个不同点 `n` 承载尾核心，按
`a=n/d` 与 `d` 的 dyadic 块分桶后给出 `TailCoreBucket`。

这说明尾项失败没有第三种自由形态。

## 5. 当前剩余义务

本文已严格证明：

```text
边界零行
=> BK-DEC 或 TailCoreBucket/CoreK-Density。
```

因此 `BPN-BK` 主链现在变为：

```text
边界零行
=> Directed Endpoint CRTDefect
   或 TailCoreBucket/CoreK-Density
=> PDEC-or-SAE / Tail-anchor 排斥
=> 矛盾。
```

真正未闭合的只剩两个出口排斥：

1. `Directed Endpoint CRTDefect` 的 `PDEC-or-SAE` 排斥；
2. `TailCoreBucket/CoreK-Density` 的 Tail-anchor 或固定核心走廊排斥。

## 6. TailCoreBucket 的进一步几何化

补充文档 `prime-matrix-bpn-tailcore-corridor-reduction.md` 已把第二个出口继续拆开：

```text
TailCoreBucket/CoreK-Density
=> Tail-anchor concentration
   或 Distributed corridor saturation。
```

证明只是乘法变量替换 `n=ad` 和走廊宽度上界：

\[
\mathcal J_a(I)=\{d:ad\in I\},\qquad |\mathcal J_a(I)|\le 1+P/a.
\]

若某个互补因子 `a` 的走廊接近该容量，就是尾锚集中；若没有单锚集中而总桶质量仍大，
则许多走廊必须同时接近裸容量，形成分布式走廊饱和。于是尾项出口不再是抽象
`CoreK`，而是两个可继续审查的几何出口：

```text
Tail-anchor 排斥；
Distributed corridor saturation 的 Selberg/CRTDefect 排斥。
```
