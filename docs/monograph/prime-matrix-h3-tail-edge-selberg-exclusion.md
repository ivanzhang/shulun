# H3 尾链边容量的二维 Selberg 排斥

**状态：** `macroscopic_tail_chain_excluded_by_2d_upper_sieve_explicit_constants_pending`

本文继续攻击同一个硬障碍：

```text
尾标签/双粗点是否能沿 H3 候选链连续拼成一个满尾补洞块？
```

上一篇 `prime-matrix-h3-tail-filler-global-chain-capacity.md` 已把满尾链压成
`EdgeCap(B;y)=|B|-1` 与 `TriCap(B;y)=|B|-2`。本文证明一个关键排斥：任何宏观长度的满尾链
会产生过多相邻 `y`-rough 对或端点 `y`-rough 对，这超过二维 Selberg 上筛容量。

## 1. 二维 rough 对上筛输入

固定非零偶数 `delta in {2,4,6}`。令 `I` 是长度 `H` 的整数区间，`z>=3`。定义

\[
S_\delta(I,z)=
\#\{n\in I:\gcd(n(n+\delta),P(z))=1\},
\tag{ESE-1}
\]

其中

\[
P(z)=\prod_{r<z}r .
\]

本文使用以下经典二维 Selberg 上筛形式。

**二维上筛定理。** 对任意固定 `0<theta<1`，存在有效常数 `A_delta(theta)` 与
`H_delta(theta)`，使得当

\[
3\le z\le H^\theta,\qquad H\ge H_\delta(\theta),
\tag{ESE-2}
\]

时，

\[
S_\delta(I,z)
\le
A_\delta(\theta)\,
{H\over(\log z)^2}.
\tag{ESE-3}
\]

这里维数为 `2`，因为除有限多个 `r|delta` 的素数外，局部被禁止的剩余类是

\[
n\equiv0\pmod r,\qquad n\equiv-\delta\pmod r .
\]

因此筛密度为

\[
\prod_{r<z}\left(1-{\nu_\delta(r)\over r}\right)
\asymp_\delta {1\over(\log z)^2},
\qquad
\nu_\delta(r)=
\begin{cases}
1,&r\mid\delta,\\
2,&r\nmid\delta.
\end{cases}
\tag{ESE-4}
\]

`(ESE-3)` 是标准上筛，不涉及素数下界，也不触碰奇偶障碍；它只给出 rough 对的上界。
若需要顶刊级完全内联，后续只需把 `A_delta(theta)` 由 Selberg 二次型或 beta-sieve 常数显式化。

## 2. 边容量上界

令 `B={a_u,...,a_v}` 为一段 H3 候选连续链，`K=|B|`。设该链位于一个长度不超过 `q+6` 的
行窗口中，且 cutoff 满足

\[
3\le y\le (q+6)^\theta .
\tag{ESE-5}
\]

如果一条相邻边 `a_j,a_{j+1}` 被尾补洞解释，则二者均没有小于等于 `y` 的素因子，故对应起点
属于 `S_2(I,y)` 或 `S_4(I,y)`。因此

\[
\mathrm{EdgeCap}(B;y)
\le
S_2(I,y)+S_4(I,y).
\tag{ESE-6}
\]

由 `(ESE-3)`，

\[
\mathrm{EdgeCap}(B;y)
\le
A_E(\theta)\,{q+6\over(\log y)^2},
\qquad
A_E(\theta)=A_2(\theta)+A_4(\theta).
\tag{ESE-7}
\]

若 `B` 被尾补洞拼满，则由全局链容量判据

\[
K-1=\mathrm{EdgeCap}(B;y).
\]

于是得到必要条件

\[
K
\le
1+
A_E(\theta)\,{q+6\over(\log y)^2}.
\tag{ESE-8}
\]

这就是边容量排斥的显式形式。

## 3. 三连容量上界

若三连 `a_j,a_{j+1},a_{j+2}` 被尾补洞解释，则端点 `a_j,a_{j+2}` 均为 `y`-rough，且

\[
a_{j+2}-a_j=6 .
\]

因此

\[
\mathrm{TriCap}(B;y)
\le
S_6(I,y).
\tag{ESE-9}
\]

二维上筛给出

\[
\mathrm{TriCap}(B;y)
\le
A_6(\theta)\,{q+6\over(\log y)^2}.
\tag{ESE-10}
\]

若 `B` 被尾补洞拼满，则

\[
K-2=\mathrm{TriCap}(B;y),
\]

所以

\[
K
\le
2+
A_6(\theta)\,{q+6\over(\log y)^2}.
\tag{ESE-11}
\]

三连版本通常比相邻边版本更贴近六轮结构，因为它直接利用二步差恒等于 `6`。

## 4. 宏观满尾链不可能

令

\[
A_*(\theta)=\max(A_E(\theta),A_6(\theta)).
\]

由 `(ESE-8)` 与 `(ESE-11)` 可得：

**定理。** 若 `3<=y<=(q+6)^theta` 且 `q` 足够大，则任何被尾补洞拼满的连续 H3 块 `B`
都满足

\[
|B|
\le
2+
A_*(\theta){q+6\over(\log y)^2}.
\tag{ESE-12}
\]

特别地，对任意固定 `alpha>0`，若

\[
y\ge q^\alpha,\qquad y\le(q+6)^\theta,
\tag{ESE-13}
\]

则

\[
|B|\ll_{\alpha,\theta}{q\over(\log q)^2}.
\tag{ESE-14}
\]

因此长度为正比例 `c q` 的宏观尾补洞块不可能存在。

## 5. 对整行尾补洞的直接排斥

H3 六轮候选在一行长度 `q` 中的数量满足

\[
\#A_s={q\over3}+O(1).
\tag{ESE-15}
\]

若整行候选全由尾补洞解释，则 `K=#A_s`，而 `(ESE-12)` 要求

\[
{q\over3}+O(1)
\le
2+
A_*(\theta){q+6\over(\log y)^2}.
\tag{ESE-16}
\]

当 `y>=q^alpha` 且 `q` 超过显式阈值后，右端是 `o(q)`，与左端矛盾。

所以：

```text
整行尾标签/双粗点精确补洞器在无限尺度上被排除。
```

这一步没有使用素数下界，只使用二维 rough 对上界。因此它避开了线性筛奇偶障碍：我们不问
`a_j` 是否为素数，只问所有相邻端点同时避开小素数的次数能否达到满链量级。

## 6. 与 H3 主链的接口

这一步实际攻下的是尾分支中的“宏观连续拼接”：

```text
Full tail chain
=> too many y-rough adjacent pairs/triples
=> violates two-dimensional upper-bound sieve.
```

但它还没有单独闭合一般混合坏行。原因是小素数骨架可能把尾点切成许多短块：

```text
small skeleton / tail / small skeleton / tail / ...
```

这种情形已经属于统一缺陷判据中的另一个出口：

```text
SmallSkeletonOverload => PDEC defect.
```

因此当前主链的状态应精确写为：

1. 宏观满尾补洞块已由二维上筛排除；
2. 若坏行仍存在，则尾点只能分散在许多短块中；
3. 这种分散必须由小骨架密集切割解释，因而回到 `D_y`/`PDEC` 缺陷；
4. 或者短块虽多但相位集中，进入 `ColumnCRT/endpoint/cofactor` 缺陷。

## 7. 剩余的真正窄口

本步把“尾补洞能否整行拼满”从开放硬核降为以下更窄接口：

```text
Short-block extraction / PDEC routing.
If no tail block has length > C q/log^2 q, but the H3 row is still fully blocked,
then the small-factor skeleton must cut the row often enough to force a D_y defect,
or the short tail blocks must create endpoint/ColumnCRT/cofactor concentration.
```

这是仍需补齐的最后连接层。它不再是粗略的尾半素数补洞问题，而是：

```text
二维上筛已禁止长尾链；
剩余坏行只能靠小骨架高频切割；
证明这种高频切割必触发 PDEC/CRT 缺陷。
```

这保持在原 H3 缺陷排斥内部，没有转换命题。
