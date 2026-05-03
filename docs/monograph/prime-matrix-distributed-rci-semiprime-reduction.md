# Distributed-RCI 的平衡双尾半素数归约

**状态：** `proved_reduction_to_prime_vs_balanced_semiprime_count_for_large_p`

本文继续专攻 `CDB-1 / Distributed-RCI`。上一阶段把终端硬点压为

\[
|R_0(h)|>\sum_{j\ge2}(j-1)|R_j(h)|.
\tag{RCI}
\]

本文进一步说明：在自然阈值之后，`RCI` 不是抽象多尾问题，而是一个非常具体的
短块计数不等式：

```text
终端块中的素数数 > 终端块中的平衡双尾半素数数。
```

这就是当前最小可攻的 `Distributed-RCI`。

## 1. 设定

设 `p<q` 为相邻奇素数，取

\[
y=\max(2,\lfloor p/e\rfloor).
\]

在一个终端 `q` 块 `I_h` 中，低筛骨架为

\[
R_y(I_h)=\{n\in I_h^\ast:\ r\nmid n\ \text{for all prime }r\le y\}.
\]

尾素数集合为

\[
\mathcal T=\{\ell:\ y<\ell\le p,\ \ell\ \text{prime}\}.
\]

令 `\omega_T(n)` 为 `n` 的不同尾素因子个数。

## 2. 无尾项就是素数

**Lemma 1（无尾储备素性）。**
若 `n\in I_h^\ast` 且 `n` 没有任何素因子 `<=p`，则 `n` 是素数。

**证明。**
因为 `n<q^2`，若 `n` 合数，则 `n=ab` 且 `2<=a<=b`。若 `a>p`，
则 `b>=a>p`，所以 `n=ab>p^2`。在相邻素数 `p<q` 之间没有素数，
因此小于 `q` 的素因子不可能落在 `(p,q)`；若两个因子都至少为 `q`，
则 `n>=q^2`，与 `n\in I_h^\ast` 矛盾。故合数 `n<q^2` 必有素因子
`<=p`。证毕。

因此 `R_0(h)` 精确等于该终端块中的素数集合。

## 3. 多尾项的半素数化

**Lemma 2（三尾排除）。**
若

\[
y^3>q^2,
\tag{T3}
\]

则任意 `n<q^2` 至多含两个不同尾素因子。

**证明。**
三个不同尾素因子的乘积大于 `y^3`，由 `(T3)` 大于 `q^2`，不可能整除
`n<q^2`。证毕。

**Lemma 3（残因子排除）。**
若

\[
{q^2\over y^2}<y,
\tag{R}
\]

则任何含两个尾素因子且仍在低筛骨架中的 `n<q^2` 必为

\[
n=\ell_1\ell_2,
\qquad y<\ell_1,\ell_2\le p.
\]

**证明。**
写 `n=\ell_1\ell_2 t`。由 `n<q^2` 得

\[
t<q^2/y^2.
\]

若 `(R)` 成立，则 `t<y`。又 `n` 在低筛骨架中，所以 `t` 没有任何素因子
`<=y`。这迫使 `t=1`。证毕。

注意 `(R)` 与 `(T3)` 是同一个尺度条件 `y^3>q^2` 的等价写法。

## 4. Distributed-RCI 的精确形式

在 `y^3>q^2` 后，`RCI` 变为

\[
\pi(I_h)
>
B_{\rm bal}(I_h),
\tag{DRCI}
\]

其中：

- `\pi(I_h)` 是 `I_h^\ast` 中的素数数；
- `B_{\rm bal}(I_h)` 是 `I_h^\ast` 中形如
  `\ell_1\ell_2`、`y<\ell_1,\ell_2<=p` 的平衡双尾半素数数。

这是当前最小硬点的关键化简。

它比普通短区间素数存在性更窄：我们不需要证明素数很多，只需要证明它们多于
一个非常受限的半素数族。

## 5. 与 CDB 的耦合

每个平衡双尾半素数

\[
n_c=\ell_1\ell_2
\]

若位于目标行列点 `c`，则列命题给出同列素数见证 `\pi_c`。位移
`d_c` 满足

\[
d_c\not\equiv0\pmod{\ell_1},\qquad
d_c\not\equiv0\pmod{\ell_2}.
\]

因此若 `(DRCI)` 失败，平衡半素数至少与素数一样多；这些半素数又必须在列方向
产生大量避零位移约束。这正是 `CDB` 可发挥作用的地方：

```text
DRCI failure
=> many balanced semiprimes
=> many displacement nonzero constraints
=> distributed case impossible or concentrated defect.
```

## 6. 实验支撑

审计见：

```text
experiments/prime_matrix_distributed_rci_semiprime_audit.py
docs/monograph/prime-matrix-distributed-rci-semiprime-audit.md
```

`p<=2000` 下：

- 全局最小 `RCI margin` 为 `1`；
- 最后出现双尾残因子 `>1` 的 `p` 为 `13`；
- 最后出现三尾或更多尾因子的 `p` 为 `7`；
- 无尾但非素数的情况没有出现；
- 最大 `balanced_semiprime/no_tail` 比值为 `2/3`。

这说明从很小的范围以后，负项确实已经完全半素数化，且实验最坏比例仍明显小于
`1`。

## 7. 剩余不等式

现在 `CDB-1 / Distributed-RCI` 可以写成单一不等式：

```text
对每个终端块 I_h，
balanced semiprimes with both factors in (y,p]
<
primes in I_h.
```

集中分支已经交给 `CDB-2/CDB-3/PDEC`。因此下一步最优证明目标是：

**Distributed Semiprime Inequality.**
若平衡半素数没有尾标签集中、没有位移余类集中，则

\[
B_{\rm bal}(I_h)<\pi(I_h).
\]

这就是当前真正的最小硬点。

进一步的局部配对路线见
`docs/monograph/prime-matrix-distributed-rci-local-pairing-route.md`：把该不等式
转化为平衡半素数到附近素数的 Hall 匹配；若匹配失败，则失败区间同时给出
半素数过密与素数过疏，可送入 `Tail-anchor/PDEC`。
