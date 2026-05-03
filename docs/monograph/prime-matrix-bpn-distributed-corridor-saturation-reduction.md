# BPN 分布式走廊饱和归约

**状态：** `distributed_corridor_saturation_reduced_to_overlap_or_colored_corridor_budget`

本文处理 `Distributed corridor saturation` 出口。核心目标是把“许多互补锚走廊同时接近裸容量”
严格拆成两类可审查缺陷：

```text
Distributed corridor saturation
=> High-overlap fixed-core defect
   或 Colored disjoint-corridor budget violation。
```

前者是固定核心 `d` 被过多互补锚复用；后者可接入不相交走廊的有限筛预算或低模端点缺陷。

## 1. 走廊族与乘法计数

令

\[
I=[L,R]\cap\mathbb Z,\qquad |I|=P-1.
\]

固定核心尺度 `D_0` 与互补锚集合 `\mathcal A`。每个 `a\in\mathcal A` 给出走廊

\[
J_a=\{d\in\mathbb Z:D_0\le d<2D_0,\ ad\in I\}.
\]

令 `\sigma(d)` 为核心 admissible 指示函数，例如

\[
\sigma(d)=1_{d|M_{<P}}1_{\omega(d)\le K}1_{\text{phase}(d)}.
\]

分布式走廊质量为

\[
U(\mathcal A)=\sum_{a\in\mathcal A}\sum_{d\in J_a}\sigma(d).
\tag{1}
\]

定义重叠函数

\[
m(d)=\#\{a\in\mathcal A:d\in J_a\}.
\]

则有精确换序恒等式

\[
U(\mathcal A)=\sum_{D_0\le d<2D_0}\sigma(d)m(d).
\tag{2}
\]

## 2. 高重叠或低重叠二分

给定重叠阈值 `\Omega\ge1`，把

\[
U=U_{\le\Omega}+U_{>\Omega}
\]

其中

\[
U_{\le\Omega}=\sum_{m(d)\le\Omega}\sigma(d)m(d),
\qquad
U_{>\Omega}=\sum_{m(d)>\Omega}\sigma(d)m(d).
\]

**Theorem DCS-1（重叠二分）。**
若 `U>U_*`，则至少发生以下一项：

1. 高重叠核心缺陷：

\[
U_{>\Omega}>U_*/2;
\tag{3}
\]

2. 低重叠走廊饱和：

\[
U_{\le\Omega}>U_*/2.
\tag{4}
\]

**证明。**
若二者都不成立，则 `U=U_{\le\Omega}+U_{>\Omega}\le U_*`，矛盾。证毕。

## 3. 高重叠核心缺陷的含义

若 `(3)` 成立，则存在许多 `d` 被多个互补锚 `a` 复用。固定 `d` 时，

\[
d\in J_a \iff a\in [L/d,R/d].
\]

因此可用互补锚数量满足

\[
m(d)\le 1+\frac{P}{d}.
\tag{5}
\]

若仍有大量 `m(d)>\Omega`，则必有一批核心 `d` 位于足够小的尺度，并且同一短区间
`[L/d,R/d]` 中聚集过多互补锚。这就是 `High-overlap fixed-core defect`：

```text
固定核心 d 复用过多
=> 互补锚短窗集中
=> Tail-anchor / low-mod CRTDefect。
```

形式上，对任意低模 `Q`，若高重叠核心集合中的互补锚不由单个锚逃逸吸收，
按 `a mod Q` 鸽巢必得到某个相位类过密，进而通过有限 Fourier 展开进入
`Directed CRTDefect`。这与 `prime-matrix-bpn-tailanchor-persistence-dichotomy.md`
的持续尾锚机制一致。

## 4. 低重叠走廊的着色

若 `(4)` 成立，考虑仅保留 `m(d)\le\Omega` 的走廊部分。整数区间图是完美图；
最大重叠度不超过 `\Omega` 的区间族可用 `\Omega` 种颜色着色，使每个颜色类内区间两两不交。

记颜色类为

\[
\mathcal A=\mathcal A_1\sqcup\cdots\sqcup\mathcal A_\Omega.
\]

对每个颜色 `c` 定义不相交走廊并集

\[
\mathcal C_c=\bigsqcup_{a\in\mathcal A_c}J_a.
\]

于是

\[
U_{\le\Omega}
\le
\sum_{c=1}^{\Omega}
\sum_{d\in\mathcal C_c}\sigma(d).
\tag{6}
\]

**证明。**
区间图着色定理可由贪心扫描端点证明：按左端点排序，每次给新区间分配当前未被
活动区间占用的最小颜色。活动区间数最多为最大重叠度 `\Omega`，故总能完成。
同色区间不相交。式 `(6)` 只是把低重叠贡献按颜色分开后求和。证毕。

## 5. Colored corridor budget

对每个不相交并集 `\mathcal C_c`，定义有限核心筛预算

\[
B_c(P,K,D_0)=
\operatorname{Budget}(\mathcal C_c;\sigma).
\]

这里 `Budget` 可取两种严格形式：

1. **精确有限预算：** 直接定义为 `\sum_{d\in\mathcal C_c}\sigma(d)`，用于有限验证或证书；
2. **Selberg/Rankin 预算：** 用有限二次型或 Rankin 光滑数包络给出显式上界，误差项写成低模端点缺陷。

于是 `(6)` 给出严格二分：

```text
若 sum_c B_c 能吸收 U_{\le\Omega}，则低重叠走廊不构成反例；
若不能吸收，则某个颜色类违反其 corridor budget。
```

违反预算的颜色类是 `Colored disjoint-corridor budget violation`。
若预算使用 Selberg/Rankin 上界，违反预算必表现为：

```text
低模端点/相位缺陷
或 光滑核心密度超过显式包络。
```

前者进入 `Directed CRTDefect`；后者是纯光滑数包络义务。

## 6. 主链更新

本文已严格证明：

```text
Distributed corridor saturation
=> High-overlap fixed-core defect
   或 Colored disjoint-corridor budget violation。
```

结合前文：

```text
High-overlap fixed-core defect
=> Tail-anchor/PDEC-or-SAE；

Colored disjoint-corridor budget violation
=> Selberg/Rankin budget failure
   或 low-mod CRTDefect。
```

因此分布式走廊出口已经缩到最后两个明确义务：

1. 固定核心高重叠的 `PDEC-or-SAE` 排斥；
2. 不相交着色走廊的核心筛预算或其低模缺陷排斥。

## 7. 着色走廊预算的有限 Rankin 化

补充文档 `prime-matrix-bpn-colored-corridor-core-sieve-budget.md` 已处理第二项。由于这里
计数的是 `d|M_{<P}`、`\omega(d)\le K` 的 smooth squarefree 核心，不能直接套用
rough-number Selberg 下界；可无条件使用有限 Rankin 账本：

\[
N_K(\mathcal C)
\le
(2D_0)^s\sum_{d\in\mathcal C}{\sigma_K(d)\over d^s}.
\]

若所有颜色类的该账本总和进入允许预算，则着色走廊出口闭合；若不进入，则剩余不是
新的结构命题，而是明确的常数/参数义务或低模 core CRTDefect：

```text
Colored corridor violation
=> finite Rankin smooth-core ledger obstruction
   或 low-mod core CRTDefect。
```
