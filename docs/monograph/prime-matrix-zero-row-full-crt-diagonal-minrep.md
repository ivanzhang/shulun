# 零行全量 CRT 方程组与对角最小代表屏障

**状态：** `exact_equivalence_proved_global_minrep_barrier_open`

本文从零行的全量 CRT 方程组出发，精确说明命题

```text
若 px+1,...,px+p 都被 <=p 的素数覆盖，则最小这样的 x 必大于 p
```

等价于所有早期 `p` 对齐短区间含素数。该等价式是严格定理；但“最小 `x>p`”本身仍需
证明 `EDA-Dual / LowMod-Tail` 出口排斥，不能只由形式 CRT 相容性自动推出。

## 1. 零行方程组

固定奇素数 `p`。第 `p` 列

\[
px+p=p(x+1)
\tag{ZC-1}
\]

自动被素数 `p` 覆盖。因此零行条件只需检查

\[
1\le k<p.
\tag{ZC-2}
\]

令

\[
Q_p=\{q:\ q<p,\ q\ {\rm prime}\},\qquad
M_p=\prod_{q\in Q_p}q.
\tag{ZC-3}
\]

零行乘数集合为

\[
Z_p=
\{x\ge1:\ \forall 1\le k<p,\ \exists q\in Q_p,\ q\mid px+k\}.
\tag{ZC-4}
\]

对每个列 `k` 选择一个覆盖素数 `q_k\in Q_p`。于是得到方程组

\[
px+k\equiv0\pmod {q_k},\qquad 1\le k<p.
\tag{ZC-5}
\]

由于 `p` 与每个 `q_k` 互素，

\[
x\equiv -k p^{-1}\pmod {q_k}.
\tag{ZC-6}
\]

## 2. 相容性是精确的

若同一素数 `q` 同时负责覆盖两列 `a,b`，则 `(ZC-6)` 要求

\[
-a p^{-1}\equiv -b p^{-1}\pmod q,
\tag{ZC-7}
\]

等价于

\[
a\equiv b\pmod q.
\tag{ZC-8}
\]

反过来，若所有同标签列都满足 `(ZC-8)`，则同一 `q` 下的方程相容；不同素数之间由
中国剩余定理相容。因此，一个标签函数

\[
\tau:\{1,\ldots,p-1\}\to Q_p
\tag{ZC-9}
\]

给出可解零行方程组，当且仅当

\[
\tau(a)=\tau(b)=q\quad\Longrightarrow\quad a\equiv b\pmod q.
\tag{ZC-10}
\]

称满足 `(ZC-10)` 的 `\tau` 为完整覆盖 CRT 证书。令

\[
D_\tau=\prod_{q\in{\rm im}(\tau)}q.
\tag{ZC-11}
\]

则存在唯一残基

\[
x\equiv r_\tau\pmod {D_\tau}.
\tag{ZC-12}
\]

于是有精确分解

\[
Z_p=
\bigcup_{\tau}
\{x\ge1:\ x\equiv r_\tau\pmod {D_\tau}\},
\tag{ZC-13}
\]

其中并集遍历所有完整覆盖 CRT 证书。首个零行乘数为

\[
X_0(p)=\min_{\tau}r_\tau^+,
\tag{ZC-14}
\]

`r_\tau^+` 表示残基类 `(ZC-12)` 的最小正代表。

这说明首零行问题的精确 CRT 形态是：

```text
证明每个完整覆盖证书 tau 的最小正代表 r_tau^+ 都大于 p。
```

## 3. 对角区段命题的等价式

命题

\[
X_0(p)>p
\tag{ZC-15}
\]

等价于

\[
\forall 1\le x\le p,\quad x\notin Z_p.
\tag{ZC-16}
\]

由 `(ZC-4)`，这又等价于

\[
\forall 1\le x\le p,\quad
\exists 1\le k<p:\quad (px+k,M_p)=1.
\tag{ZC-17}
\]

此处 `k<p` 保证 `p\nmid px+k`。因此 `(ZC-17)` 中的数没有任何 `<=p` 的素因子。

## 4. 早期未覆盖点必为素数

**引理 ZC-Prime.**  
若 `1<=x<=p`、`1<=k<p` 且 `(px+k,M_p)=1`，则 `px+k` 是大于 `p` 的素数。

**证明。**  
记

\[
n=px+k.
\tag{ZC-18}
\]

则

\[
p<n\le p^2+p-1.
\tag{ZC-19}
\]

又因 `k<p`，有 `p\nmid n`；结合 `(n,M_p)=1`，可知 `n` 没有任何 `<=p` 的素因子。
若 `n` 合成，则它的每个素因子都大于 `p`。由于 `p` 为奇素数，大于 `p` 的最小可能素数
至少是 `p+2`，故

\[
n\ge(p+2)^2=p^2+4p+4>p^2+p-1,
\tag{ZC-20}
\]

与 `(ZC-19)` 矛盾。因此 `n` 必为素数。证毕。

由此得到严格等价：

\[
X_0(p)>p
\Longleftrightarrow
\forall 1\le x\le p,\quad
\pi(px+p-1)-\pi(px)>0.
\tag{ZC-21}
\]

也就是说，首个零行必在对角区段之后，当且仅当每个早期短区间

\[
(px,\ px+p),\qquad 1\le x\le p,
\tag{ZC-22}
\]

都含有素数。

## 5. 审稿级结论

从全量 CRT 方程组出发，已经无条件证明的是：

```text
零行存在
<=> 存在完整覆盖 CRT 证书 tau
<=> x 落在 tau 的 CRT 残基类中。
```

以及：

```text
首零行在对角之后
<=> 所有证书的最小正代表 > p
<=> 每个 p 对齐早期短区间含素数。
```

因此，若要证明“最小 `x` 必大于 `p`”，剩余不能只是重复 CRT 相容性；必须实际证明以下
等价目标之一：

1. **MinRep 屏障：** 每个完整覆盖证书 `\tau` 的 `r_\tau^+>p`；
2. **EDA-Dual 正余量：** 对所有 `1<=x<=p`，精确筛余
   \[
   U_p(x)=\#\{1\le k<p:(px+k,M_p)=1\}
   \tag{ZC-23}
   \]
   为正；
3. **低模/尾项出口排斥：** 由 `EDA-BK` 已得的
   `LowMod endpoint CRTDefect / Tail-Core concentration` 两个出口均不可能发生。

这就是当前命题的最窄闭合口。

