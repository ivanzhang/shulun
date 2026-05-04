# EDA-BK：正主项阶数与低模/尾项二分

**状态：** `positive_order_and_dichotomy_proved_exits_open`

本文在 `EDA-BK endpoint defect bridge` 之后继续压缩硬点。目标是证明两件事：

1. 总能选择一个奇数阶 `K` 使截断 Euler 主项 `G_K(p)>0`；
2. 一旦早期避让失败，负端点缺陷必二分为低模端点缺陷或高模尾项集中。

这一步仍不宣称闭合 `EDA`，但把剩余义务变成两个明确出口。

## 1. 正主项奇数阶

令

\[
\mathcal P_{<p}=\{q:\ q<p,\ q\ {\rm prime}\},\qquad m=\#\mathcal P_{<p}.
\tag{ELT-1}
\]

记

\[
V(p)=\prod_{q<p}\left(1-{1\over q}\right)>0,
\tag{ELT-2}
\]

并令 `e_j` 为 `{1/q:q<p}` 的第 `j` 个初等对称和。则

\[
V(p)=\sum_{j=0}^{m}(-1)^j e_j.
\tag{ELT-3}
\]

选择

\[
K_*(p)=
\begin{cases}
m,&m\ {\rm odd},\\
m-1,&m\ {\rm even}.
\end{cases}
\tag{ELT-4}
\]

于是 `K_*(p)` 为奇数，且

\[
G_{K_*}(p)=\sum_{j=0}^{K_*(p)}(-1)^j e_j>0.
\tag{ELT-5}
\]

**证明。**
若 `m` 为奇数，则 `K_*=m`，所以 `G_{K_*}=V(p)>0`。

若 `m` 为偶数，则

\[
G_{K_*}(p)=G_{m-1}(p)=V(p)-e_m.
\tag{ELT-6}
\]

这里

\[
{V(p)\over e_m}
=\prod_{q<p}(q-1).
\tag{ELT-7}
\]

当 `p>=5` 时，集合中至少含 `2,3`，上式至少为 `1\cdot2>1`，故 `V(p)>e_m`，
从而 `G_{m-1}(p)>0`。`p=3` 可直接检查。证毕。

## 2. 失败必给出定量负端点缺陷

令 `H=p-1`。若 `EDA(p)` 失败，则存在 `1<=x<=p` 使 `U_p(x)=0`。取上节的
`K_*(p)`，由奇数阶 Bonferroni 与端点缺陷桥接得到

\[
E_{K_*}(p,x)\le -H\,G_{K_*}(p).
\tag{ELT-8}
\]

设

\[
\Lambda_p=H\,G_{K_*}(p)>0.
\tag{ELT-9}
\]

则反例行必满足

\[
E_{K_*}(p,x)\le-\Lambda_p.
\tag{ELT-10}
\]

这给出一个不含素数位置的必要条件：早期零行必须制造强负端点锯齿缺陷。

## 3. 低模/尾项二分

对任意 cutoff `D>=1`，分解

\[
E_{K_*}(p,x)=E_{\le D}(p,x)+E_{>D}(p,x),
\tag{ELT-11}
\]

其中

\[
E_{\le D}(p,x)=
\sum_{\substack{d\mid M_{<p}\\ \omega(d)\le K_*\\ d\le D}}
(-1)^{\omega(d)}\varepsilon_d(x),
\tag{ELT-12}
\]

\[
E_{>D}(p,x)=
\sum_{\substack{d\mid M_{<p}\\ \omega(d)\le K_*\\ d>D}}
(-1)^{\omega(d)}\varepsilon_d(x).
\tag{ELT-13}
\]

**定理 ELT-Dichotomy.**  
若 `EDA(p)` 失败，则对任意 `D` 与任意 `0<=T<\Lambda_p`，至少发生以下一项：

```text
Tail:    |E_{>D}(p,x)| > T;
LowMod:  E_{\le D}(p,x) <= -(\Lambda_p-T).
```

**证明。**
若 `Tail` 不发生，则 `E_{>D}(p,x)>=-T`。由 `(ELT-10)`，

\[
E_{\le D}(p,x)
=E_{K_*}(p,x)-E_{>D}(p,x)
\le -\Lambda_p+T
=-(\Lambda_p-T).
\]

这正是 `LowMod`。证毕。

## 4. CRT 结构含义

`LowMod` 分支只涉及 `d<=D` 的有限 squarefree 模。由于 `d|M_{<p}` 且 `p\nmid d`，
乘法 `x -> px mod d` 是模 `d` 的单位旋转。因此每个

\[
\varepsilon_d(x)=
\left\{ {px\over d}\right\}
-\left\{ {px+H\over d}\right\}
\tag{ELT-14}
\]

都是 `x mod d` 的纯 CRT 相位函数。若 `LowMod` 在大量候选行上持续出现，它自动形成
低模 Fourier/PDEC 缺陷；若它只在少数行出现，则进入 SAE 型局部逃逸。

`Tail` 分支则表示大 squarefree 核的端点相位总量无法忽略。这与前文
`CoreK-Density/Tail-anchor` 是同一个对象：高模尾项若过大，要么集中在少数尾锚，
要么在分散走廊中产生可证书化的 smooth-core/Rankin 预算压力。

## 5. 当前最小剩余

本步已经无条件证明：

```text
EDA failure
=> positive-main endpoint defect
=> LowMod endpoint CRTDefect or Tail/Core concentration.
```

尚未证明的是两个出口排斥：

1. `LowMod endpoint CRTDefect` 不可能覆盖早期全部候选反例行；
2. `Tail/Core concentration` 必可由 Tail-anchor、Rankin smooth-core 账本或 `PDEC/SAE`
   吸收。

因此 `EDA` 当前不再是无结构的短区间素数问题，而是以下可验收二分：

```text
prove LowMod exclusion  and  prove Tail/Core absorption.
```

