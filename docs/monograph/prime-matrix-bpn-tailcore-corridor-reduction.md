# BPN TailCoreBucket 到尾锚/走廊饱和的严格归约

**状态：** `tailcore_reduced_to_anchor_or_corridor_saturation`

本文继续处理 `TailCoreBucket/CoreK-Density` 出口。目标是把“尾核心桶过密”严格拆成两种
可继续攻击的几何缺陷：

```text
TailCoreBucket
=> Tail-anchor concentration
   或 Distributed corridor saturation。
```

这一步仍不是最终排斥；它把抽象尾桶过密变成短窗乘法几何中的锚集中或走廊饱和。

## 1. 尾核心桶的乘法坐标

令

\[
I=[L,R]\cap\mathbb Z,\qquad R-L+1=P-1.
\]

一个尾核心桶 `C` 由下列有限条件给出：

- 核心 `d` 在 dyadic 区间 `D_0\le d<2D_0`；
- 互补因子 `a=n/d` 在 dyadic 区间 `A_0\le a<2A_0`；
- `d|M_{<P}`、`\omega(d)\le K`、`d>D`；
- 可选低模相位条件。

桶内点数为

\[
U_C(I)=
\#\{(a,d):ad\in I,\ A_0\le a<2A_0,\ D_0\le d<2D_0,\ d|M_{<P},\omega(d)\le K\}.
\]

对每个互补因子 `a` 定义走廊

\[
\mathcal J_a(I;D_0)=
\{d:D_0\le d<2D_0,\ ad\in I\}.
\]

于是有精确恒等式

\[
U_C(I)=
\sum_{A_0\le a<2A_0}
\#\{d\in\mathcal J_a(I;D_0):d|M_{<P},\omega(d)\le K,\text{phase}(d)\}.
\tag{1}
\]

这不是估计，而是变量替换 `n=ad`。

## 2. 走廊宽度上界

对固定 `a`，

\[
\mathcal J_a(I;D_0)
\subseteq
\left[\frac{L}{a},\frac{R}{a}\right].
\]

因此整数宽度满足

\[
|\mathcal J_a(I;D_0)\cap\mathbb Z|
\le
1+\frac{P-1}{a}
\le
1+\frac{P}{A_0}.
\tag{2}
\]

定义桶的裸几何容量

\[
\operatorname{Cap}(C)
=
\sum_{A_0\le a<2A_0}
\left(1+\frac{P}{a}\right).
\tag{3}
\]

则无条件有

\[
U_C(I)\le \operatorname{Cap}(C).
\tag{4}
\]

更精细地，若 `A_0>P`，每条走廊宽度 `<2`；若 `A_0\ge P` 且端点不跨整数，
几乎所有走廊为 singleton 或空走廊。这正是此前 singleton corridor 路线的自然入口。

## 3. 锚集中或分布式走廊饱和

给定阈值 `0<\theta\le1`。称 `a` 是 `\theta`-饱和尾锚，若

\[
\#\{d\in\mathcal J_a(I;D_0):d|M_{<P},\omega(d)\le K,\text{phase}(d)\}
\ge
\theta\left(1+\frac{P}{a}\right).
\tag{5}
\]

**Theorem TCR-1（尾桶到锚/走廊二分）。**
若 `U_C(I)=U`，则至少发生以下一项：

1. 存在一个 `\theta`-饱和尾锚 `a`；
2. 非饱和走廊总贡献满足

\[
U
\le
\theta\,\operatorname{Cap}(C)
+
N_{\rm sat}\left(1+\frac{P}{A_0}\right),
\tag{6}
\]

其中 `N_sat` 是饱和尾锚个数。特别地，若无饱和尾锚，则

\[
U\le \theta\,\operatorname{Cap}(C).
\tag{7}
\]

**证明。**
按 `a` 分解 `(1)`。若某条走廊满足 `(5)`，得到第一项。否则每条走廊贡献都小于
`\theta(1+P/a)`，求和即得 `(7)`。一般情形把饱和尾锚先取出；每个饱和尾锚的
粗上界由 `(2)` 给出，剩余走廊用非饱和上界，得到 `(6)`。证毕。

**Corollary TCR-2（过容量必有结构缺陷）。**
若

\[
U_C(I)>\theta\,\operatorname{Cap}(C),
\]

则存在 `\theta`-饱和尾锚。若饱和尾锚被另行排除，而 `U_C(I)` 仍大，则只能是
大量走廊同时接近容量上限，即 `Distributed corridor saturation`。

## 4. 与 Tail-anchor 的精确定义

`a` 是互补因子，即 `n=ad` 中除去大 squarefree 核心 `d` 后的剩余锚。若同一 `a`
支撑异常多的 `d`，则所有点 `n=ad` 落在同一条双曲走廊

\[
d\in [L/a,R/a],
\]

并共享同一互补锚 `a`。这正是 `Tail-anchor concentration`。

若没有单一锚集中，则异常只能来自许多 `a` 的走廊同时接近裸容量 `(2)`。这类
分布式饱和比单锚更强：它要求大量不同互补锚的 `d` 同时满足 `<P` 小素核心、
低模相位和短窗乘法约束。该对象应接入已有的
`disjoint corridor Selberg` 或低模端点缺陷路线。

## 5. 当前剩余

本文已严格证明：

```text
TailCoreBucket/CoreK-Density
=> Tail-anchor concentration
   或 Distributed corridor saturation。
```

因此 `BPN-BK` 的尾项出口进一步缩为：

```text
Tail-anchor 排斥；
Distributed corridor saturation 的 Selberg/CRTDefect 排斥。
```

下一步最小硬点是后者：证明分布式走廊不能在边界短窗中长期接近裸容量；
若接近，则其低模相位必须产生 `Directed CRTDefect/Tail-anchor`。

## 6. 尾锚出口已持续化

补充文档 `prime-matrix-bpn-tailanchor-persistence-dichotomy.md` 已处理第一类出口：

```text
Tail-anchor concentration
=> SAE-anchor
   或 Persistent Tail-anchor defect。
```

证明只用两个事实：单锚若承担过大质量就是单窗锚逃逸；否则大量饱和锚按低模 `Q`
分相位后，必有某个相位类过密，进而通过有限 Fourier 展开进入低模 CRT 缺陷。
所以尾锚分支已经并回最终统一出口：

```text
PDEC-or-SAE。
```

尾项侧当前真正剩余只剩：

```text
Distributed corridor saturation 的 Selberg/CRTDefect 排斥。
```

## 7. 分布式走廊已拆成重叠/着色预算

补充文档 `prime-matrix-bpn-distributed-corridor-saturation-reduction.md` 已证明：

```text
Distributed corridor saturation
=> High-overlap fixed-core defect
   或 Colored disjoint-corridor budget violation。
```

证明使用精确换序

\[
U=\sum_d \sigma(d)m(d)
\]

和区间图着色。若重叠函数 `m(d)` 大，则固定核心 `d` 被过多互补锚复用，进入
尾锚/低模相位集中；若重叠受控，则走廊族可按最大重叠度着色为不相交走廊并集，
逐色接入有限走廊筛预算。于是 `Distributed corridor saturation` 不再是单独出口，
而被压缩为：

```text
High-overlap fixed-core defect -> PDEC-or-SAE；
Colored disjoint-corridor budget violation -> 核心筛预算或 low-mod CRTDefect。
```
