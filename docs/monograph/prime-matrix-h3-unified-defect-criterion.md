# H3 全局统一缺陷判据

**状态：** `proved_conditional_closure_criterion_not_unconditional_h3`

本文把当前 H3 链条合成为一个全局、无限尺度、完全确定性的判据。它给出可审查的闭合形式：

```text
若 rough 计数 PDEC 缺陷与尾标签 Fourier 缺陷均被排斥，
则 H3 余量有正的 q/log q 下界。
```

这不是无条件 H3 定理；它精确指出完成无条件闭合还差哪一个统一缺陷排斥定理。

## 1. 统一符号

设 `p<q` 为相邻奇素数，`2<=s<=q`。令 `A_s` 为第 `s` 个 `q` 行窗口中的完整 3 行六轮候选集合。

定义 H3 余量

\[
M=M_{H3}(p,s)=\#\{n\in A_s:P^-(n)>p\}.
\]

对 cutoff `y<p`，定义

\[
C_y=\#\{n\in A_s:5\le P^-(n)\le y\},
\]

\[
R_y=\#\{n\in A_s:P^-(n)>y\},
\]

\[
V_y=\#A_s\prod_{5\le r\le y}\left(1-{1\over r}\right),
\qquad
D_y=V_y-R_y.
\]

令 `ell_+(y)` 为大于 `y` 的下一素数，并取

\[
d\ge 2\left(\left\lfloor {q\over \ell_+(y)}\right\rfloor+1\right).
\]

定义尾 Fourier 能量

\[
\mathcal F_y(d)=
\sum_{y<\ell\le p}
\sum_{1\le a\le d-1}
\left|
\sum_{n\in A_{s,\ell}} e^{2\pi ian/d}
\right|^2.
\]

## 2. 确定性闭合判据

**定理。** 给定 `B,L>0`。若同时满足

\[
D_y\le V_y-B-2L,
\tag{UDC-1}
\]

和

\[
\mathcal F_y(d)\le dL,
\tag{UDC-2}
\]

则

\[
M_{H3}(p,s)\ge B.
\tag{UDC-3}
\]

**证明。** 反设 `M<B`。由全局尾标签能量引理，

\[
C_y>\#A_s-B-2L
\]

或

\[
E_y(d)>L.
\]

若第一项成立，则 `R_y=#A_s-C_y<B+2L`，于是

\[
D_y=V_y-R_y>V_y-B-2L,
\]

与 `(UDC-1)` 矛盾。若第二项成立，由尾标签 Fourier 桥接

\[
\mathcal F_y(d)=dE_y(d)>dL,
\]

与 `(UDC-2)` 矛盾。两种可能均排除，故 `M>=B`。证毕。

## 3. `q/log q` 尺度版本

取

\[
B=c{q\over\log q},
\qquad
L=\lambda {q\over\log q}.
\]

若存在 `eta>0` 使

\[
V_y\ge (c+2\lambda+\eta){q\over\log q},
\tag{UDC-4}
\]

并且有两个排斥估计

\[
D_y\le \eta {q\over\log q},
\tag{UDC-5}
\]

\[
\mathcal F_y(d)\le d\lambda {q\over\log q},
\tag{UDC-6}
\]

则

\[
M_{H3}(p,s)\ge c{q\over\log q}.
\tag{UDC-7}
\]

这就是数据规律的理论形式：不是从 Mertens 平均直接推出逐窗正余量，而是证明任何低余量反例必须
突破 `(UDC-5)` 或 `(UDC-6)` 的低模缺陷上界。

## 4. 全局闭合还差的唯一类型输入

当前链条已经完成：

1. 低 H3 余量 `=>` 小骨架过载或尾能量；
2. 小骨架过载 `=>` rough 计数 PDEC 缺陷 `D_y`；
3. 尾能量 `=>` 非零 Fourier/PDEC 缺陷 `F_y(d)`；
4. 两个缺陷均排斥 `=>` H3 正下界。

因此无条件闭合不应再寻找有限模板，也不应再重复 Mertens 启发。真正剩余是统一缺陷排斥：

```text
Unified H3 Defect Exclusion.
For an admissible y=q^theta and all adjacent p<q, all 2<=s<=q,
both D_y and F_y(d) satisfy the bounds (UDC-5), (UDC-6).
```

若这个定理被证明，H3/行命题即全局闭合；若没有证明，主稿必须保持条件闭合判据状态。

## 5. 审稿口径

可在正文中宣称的已证内容：

```text
H3 has a global deterministic defect criterion at q/log q scale.
```

不可宣称的内容：

```text
H3 is unconditionally proved.
```

原因是 `(UDC-5)` 与 `(UDC-6)` 是平方根长度窗口上的低模缺陷排斥；它们正是当前主链的最后深输入，
不能由有限样本、普通 Mertens 乘积或线性筛临界下界自动推出。

补充边界文件：

```text
docs/monograph/prime-matrix-h3-pointwise-closure-boundary.md
```

该文件把最终硬点改写为第一行尺度的逐行转移：已证平均
`avg_s M_H3(p,s)~pi(q)/2`，未证点态 `M_H3(p,s)>=kappa*pi(q)`。统一缺陷判据正是证明该点态转移的
当前最短路线。

进一步硬边界见：

```text
docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md
```

该文件把点态转移等价化为平方根长度短区间素数下界，并解释为什么必须由 `D_y/F_y` 缺陷排斥来
突破线性筛 `u=2` 的奇偶障碍。
