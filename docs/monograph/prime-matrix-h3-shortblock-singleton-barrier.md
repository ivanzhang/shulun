# H3 短尾块路由与单点尾块硬障碍

**状态：** `shortblock_identities_proved_singleton_tail_barrier_open`

本文继续攻击同一个 H3/行命题闭合目标。上一层已经证明：

```text
宏观连续尾补洞链不能存在。
```

因此如果坏行仍存在，尾补洞点只能分裂成很多短块。本文严写这一步的精确组合恒等式，并指出
真正剩余硬障碍不是“短块很多”本身，而是：

```text
大量孤立 y-rough 尾点能否全部是双粗合数，而没有任何素数幸存？
```

这仍是原 `Square-root Defect Exclusion` 的内部硬核，没有转换命题。

## 1. 三色分解

固定相邻素数 `p<q`、H3 行候选链

\[
A=\{a_1<a_2<\cdots<a_N\},
\qquad N={q\over3}+O(1).
\tag{SBB-1}
\]

给定 cutoff `y<p`，把候选点分为三类：

\[
S_y=\{a_j:P^-(a_j)\le y\},
\tag{SBB-2}
\]

\[
T_y=\{a_j:y<P^-(a_j)\le p\},
\tag{SBB-3}
\]

\[
M_y=\{a_j:P^-(a_j)>p\}.
\tag{SBB-4}
\]

在 `a_j<q^2` 的壳层内，`M_y` 中的点就是旧筛幸存素数。因此 H3 行命题的坏行假设为

\[
M_y=\varnothing,
\qquad
A=S_y\sqcup T_y .
\tag{SBB-5}
\]

这里 `S_y` 是小骨架覆盖点，`T_y` 是尾标签/双粗补洞点。

## 2. 尾块分解

按候选链顺序，把 `T_y` 分解成极大连续尾块：

\[
T_y=B_1\sqcup\cdots\sqcup B_J,
\qquad
B_i=\{a_{u_i},a_{u_i+1},\ldots,a_{v_i}\}.
\tag{SBB-6}
\]

记

\[
k_i=|B_i|,
\qquad
T=|T_y|=\sum_i k_i .
\tag{SBB-7}
\]

定义尾块内部相邻边数与三连数：

\[
E=\sum_i (k_i-1)=T-J,
\tag{SBB-8}
\]

\[
R=\sum_i \max(k_i-2,0).
\tag{SBB-9}
\]

这些不是估计，而是恒等式。上一层二维 Selberg 上筛正是控制 `E` 与 `R`：

\[
E\ll {q\over(\log y)^2},
\qquad
R\ll {q\over(\log y)^2}
\tag{SBB-10}
\]

在 `y=q^\alpha` 的宏观 cutoff 下成立。

## 3. 长链排除后的精确后果

由 `(SBB-8)` 得

\[
J=T-E.
\tag{SBB-11}
\]

所以如果坏行中尾点总量仍为自然粗数尺度

\[
T\asymp {q\over\log y},
\tag{SBB-12}
\]

则由于 `E=O(q/log^2 y)`，

\[
J=T+O\!\left({q\over(\log y)^2}\right).
\tag{SBB-13}
\]

也就是说，绝大多数尾块必须是单点块或极短块；尾点之间几乎不相邻。

更精确地，设

\[
J_1=\#\{i:k_i=1\}.
\tag{SBB-14}
\]

因为每个非单点块至少贡献一条内部边，

\[
J-J_1\le E.
\tag{SBB-15}
\]

结合 `(SBB-11)`，

\[
J_1\ge T-2E.
\tag{SBB-16}
\]

若 `T` 是 `q/log y` 级而 `E` 是 `q/log^2 y` 级，则

\[
J_1=T+O\!\left({q\over(\log y)^2}\right).
\tag{SBB-17}
\]

这证明：长尾链排除后，坏行的尾部压力几乎全部集中在孤立尾点上。

## 4. 为什么“小骨架切割很多”本身不够矛盾

由尾块极大性，相邻两个尾块之间至少有一个小骨架点。因此

\[
|S_y|\ge J-1.
\tag{SBB-18}
\]

但这不是强矛盾。因为

\[
|S_y|=N-T,
\tag{SBB-19}
\]

而自然情况下 `N~q/3`、`T~q/log y`，所以 `S_y` 本来就是 `q` 级。下界
`|S_y|\ge q/log y` 远远低于小骨架的自然规模。

因此不能把“尾点被切成很多短块”直接写成 `PDEC` 缺陷。若这样写，就是把自然小骨架密度误判成
异常密度，审稿上不成立。

正确的剩余硬核是：

```text
这些孤立 y-rough 尾点为什么不能全部是双粗合数？
```

## 5. 孤立尾点的局部方程

设 `a_j` 是单点尾块。则

\[
a_j=\ell_j m_j,\qquad y<\ell_j\le p,\qquad P^-(m_j)\ge \ell_j,
\tag{SBB-20}
\]

并且左右相邻 H3 候选若存在，均属于小骨架：

\[
P^-(a_{j-1})\le y,\qquad P^-(a_{j+1})\le y.
\tag{SBB-21}
\]

由于 H3 相邻差为 `2/4`，单点尾块的局部相位是

\[
a_j-\delta_-\in S_y,\qquad a_j+\delta_+\in S_y,
\qquad
\delta_\pm\in\{2,4\}.
\tag{SBB-22}
\]

换成同余语言，存在小素数 `r_-,r_+\le y` 使

\[
a_j\equiv \delta_-\pmod{r_-},
\qquad
a_j\equiv -\delta_+\pmod{r_+},
\tag{SBB-23}
\]

同时又有尾标签条件

\[
a_j\equiv0\pmod{\ell_j},\qquad \ell_j>y.
\tag{SBB-24}
\]

这就是单点尾块的真实矛盾场：一个大素数零类被左右两个小骨架非零类夹住。

## 6. 单点尾块不能由二维边筛排除

二维 rough 对上筛只控制相邻两个尾点或三连端点尾点。因此它控制 `E` 和 `R`，但不直接控制
`J_1`。由 `(SBB-16)` 可见，排除长链反而把主要质量推向 `J_1`。

所以剩余不能再继续使用同一个边容量不等式。必须直接处理单点尾块：

```text
Singleton Tail Exclusion.
大量满足 (SBB-20)--(SBB-24) 的孤立尾点若全部为合数，
则其尾标签、左右小素标签或互补商相位必须产生
PDEC/ColumnCRT/endpoint/cofactor 缺陷。
```

这就是当前唯一剩余硬障碍的精确形态。

## 7. 可审查的下一不等式

令 `U_y` 为单点尾块集合。对每个 `a_j in U_y` 选择：

1. 尾标签 `ell_j=P^-(a_j)>y`；
2. 左小骨架标签 `r_-(j)<=y`，若左邻存在；
3. 右小骨架标签 `r_+(j)<=y`，若右邻存在。

定义三重相位计数

\[
\mathcal N(\ell,r_-,r_+)
=
\#\{a_j\in U_y:
a_j\equiv0\pmod\ell,\ 
a_j\equiv\delta_-\pmod{r_-},\ 
a_j\equiv-\delta_+\pmod{r_+}\}.
\tag{SBB-25}
\]

若所有孤立尾点都能无缺陷存在，则必须有

\[
\sum_{\ell>y}\sum_{r_-,r_+\le y}\mathcal N(\ell,r_-,r_+)
\ge
T-O\!\left({q\over(\log y)^2}\right).
\tag{SBB-26}
\]

因此下一步最小闭合目标是证明：

\[
\sum_{\ell>y}\sum_{r_-,r_+\le y}\mathcal N(\ell,r_-,r_+)
<
T-c{q\over\log y}
\tag{SBB-27}
\]

或证明 `(SBB-26)` 强制某个低模投影出现超过 CRT 均衡允许的偏差，即进入
`PDEC/ColumnCRT/endpoint/cofactor`。

## 8. 本步实际推进

本步完成的是严格定位：

1. 尾块分解恒等式 `T=J+E`；
2. 二维上筛排除长尾链后，绝大多数尾点必须是单点块；
3. “小骨架切割很多”本身不构成 PDEC 缺陷，因为小骨架自然就是 `q` 级；
4. 当前唯一真正剩余硬障碍是单点尾块的夹逼相位系统 `(SBB-20)--(SBB-24)`；
5. 下一步必须证明单点尾块三重相位计数 `(SBB-26)` 不能达到满尾质量，或它必然触发命名缺陷。

这不是退回平均尺度，也不是转换命题；它把原尾补洞障碍推进到最窄的孤立尾点层。
