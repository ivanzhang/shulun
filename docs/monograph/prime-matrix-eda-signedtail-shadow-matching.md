# EDA-SignedTail：奇偶核心双向影子匹配路线

**状态：** `signed_tail_reduced_to_boundary_or_shadow_congestion`

本文继续专攻 `SignedTail-Balance`。上一稿已经把危险尾项压成：

```text
odd-core corridor mass exceeds even-core corridor mass.
```

本步进一步证明：这种失衡若发生，不是无结构现象，而必须来自两类具体缺陷：

```text
Boundary odd cores
或
Even-shadow congestion.
```

前者是在当前 `n` 的尾核心图中没有任何偶邻居的孤立奇数阶核心；后者是许多奇核心共享太少
偶核心影子，等价于固定偶核心被过多尾标签复用，可回流 Tail-anchor / Core-overlap / PDEC。

## 1. 点态尾核心图

固定 `p,x,K,D` 和一个数 `n in I_{p,x}`。令

\[
\mathcal T(n)=
\{d:\ d\mid n,\ d\mid M_{<p},\ \omega(d)\le K,\ d>D\}.
\tag{STM-1}
\]

分成奇偶两侧：

\[
\mathcal O(n)=\{d\in\mathcal T(n):\omega(d)\ {\rm odd}\},
\qquad
\mathcal E(n)=\{e\in\mathcal T(n):\omega(e)\ {\rm even}\}.
\tag{STM-2}
\]

建立二部图 `G(n)`：若 `d` 与 `e` 的素因子集合相差一个素因子，则连边

\[
d\in\mathcal O(n)\longrightarrow e\in\mathcal E(n).
\tag{STM-3}
\]

这条边表示一个危险奇核心 `d` 可以由相邻偶核心 `e` 抵消。允许上下两个方向很重要：
大单素数核心 `q>D` 虽然没有向下偶影子，但若同一个 `n` 还有另一个小素数 `r`，则偶核心
`qr>D` 可以与 `q` 配对。

## 2. 孤立奇核心

称 `d in O(n)` 是孤立奇核心，若它在 `G(n)` 中度数为 `0`。等价地：

\[
\forall q\mid d,\quad d/q\le D,
\qquad
\forall r\mid n,\ r\nmid d,\quad dr>D\ {\rm 不成立或}\ \omega(d)+1>K.
\tag{STM-4}
\]

典型孤立奇核心包括：

1. `omega(d)=1` 的大单素数核心 `d=q>D`，且 `n` 没有第二个 `<p` 小素因子可形成偶核心 `qr>D`；
2. `omega(d)=3` 且所有二因子子核心都不超过 `D` 的最小三核心。

这些对象不能由偶核心影子配对，只能通过 Tail-anchor、Rankin 走廊或低模缺陷处理。

## 3. 匹配定理

对每个 `n`，取 `G(n)` 中从奇核心到偶核心的最大匹配。令

\[
m(n)=\text{最大匹配大小},
\qquad
b(n)=|\mathcal O(n)|-m(n).
\tag{STM-6}
\]

则点态 signed tail 满足

\[
|\mathcal E(n)|-|\mathcal O(n)|\ge -b(n).
\tag{STM-7}
\]

**证明。**  
最大匹配把 `m(n)` 个奇核心注入到互不相同的偶核心。配对部分净贡献为 `0`，未配对奇核心至多
贡献 `-b(n)`，其余未用偶核心贡献非负。证毕。

对整行求和，令

\[
B_{p,K,D}(x)=\sum_{n\in I_{p,x}}b(n).
\tag{STM-8}
\]

则

\[
R_{p,K,D}(x)=U^+_{p,K,D}(x)-U^-_{p,K,D}(x)
\ge -B_{p,K,D}(x).
\tag{STM-9}
\]

因此若危险负尾项发生：

\[
R_{p,K,D}(x)<-T,
\tag{STM-10}
\]

则

\[
B_{p,K,D}(x)>T.
\tag{STM-11}
\]

这把 signed tail 失衡压成“最大匹配缺口”。

## 4. 缺口二分：孤立或拥塞

设 `Z(n)` 为孤立奇核心数，即 `G(n)` 中度数为 `0` 的奇侧顶点数。若

\[
b(n)>Z(n),
\tag{STM-12}
\]

则存在非边界奇核心仍无法匹配。由 Hall 定理，存在奇核心集合 `A⊂O(n)`，其中每个元素至少有
一个偶影子，但

\[
|N(A)|<|A|.
\tag{STM-13}
\]

这就是偶影子拥塞：许多奇核心只落到少数偶核心影子上。若拥塞来自上邻接，则固定偶核心
覆盖多个奇子核心；若来自下邻接，则固定偶核心被多个素数扩展成奇核心。两者都说明局部
尾核心图存在复用异常。

因此整行缺口二分为：

```text
Matching deficit
=> Isolated odd core pressure
   或 Even-shadow congestion.
```

前者进入 singleton / minimal-triple corridor 账本；后者进入固定核心复用、Tail-anchor 或
low-mod core CRTDefect。

## 5. 当前剩余

本步已经严格证明：

```text
SignedTail negative enough
=> large matching deficit
=> isolated odd cores or even-shadow congestion.
```

尚未闭合的是：

1. **Isolated odd core absorption.** 控制大单素数核心与最小三核心走廊；
2. **Shadow congestion exclusion.** 证明固定偶核心不能被过多奇扩展复用，或其失败给出
   `PDEC/SAE`；
3. **全局预算。** 将匹配缺口上界与 `EDA-BK` 阈值 `T` 对齐。

下一步审计任务：

```text
measure matching deficit, isolated odd cores, and shadow congestion
on the thinnest EDA rows.
```

## 6. 双向匹配审计事实

脚本：

```text
experiments/prime_matrix_eda_signedtail_matching_audit.py
```

命令：

```text
python3 experiments/prime_matrix_eda_signedtail_matching_audit.py --selected 101,199,499 --K 5 --D 100 --top 1
```

最薄行摘要：

| p | x | U | signed tail | odd | even | matched odd | deficit | isolated odd | congestion | max even degree |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 101 | 73 | 7 | 7 | 58 | 65 | 49 | 9 | 2 | 7 | 5 |
| 199 | 179 | 12 | 10 | 167 | 177 | 142 | 25 | 9 | 16 | 5 |
| 499 | 362 | 29 | 13 | 647 | 660 | 575 | 72 | 38 | 34 | 6 |

对比单向删除影子匹配，双向邻接允许大单素数核心向上配对到偶数二核心，使缺口显著下降。
样本显示：

1. 最薄行的 signed tail 仍为正；
2. 孤立奇核心数量远小于全部奇核心；
3. 影子拥塞缺口与孤立缺口同量级，但单个偶影子的最大复用度只有 `5--6`；
4. 当前危险若要发生，必须把这种低度局部拥塞在许多点上同步放大。

因此下一步最小硬点更新为：

```text
ShadowCongestion-Bound:
low-degree even-shadow congestion cannot accumulate beyond the BK threshold;
if it does, it yields a fixed-core reuse / low-mod core CRTDefect certificate.
```

孤立奇核心分支则缩为：

```text
IsolatedOdd-Absorption:
large singleton cores and minimal triple cores are absorbed by tail-anchor or Rankin corridor budgets.
```
