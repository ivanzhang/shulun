# 对角平方后端点尾碰撞消失

**状态：** `postsquare_multi_tail_collision_vanishes_for_p_ge_23`

本文继续压缩 `PostSquare-RCI/PDEC`。核心结论是：平方后端点的双尾碰撞在 `P>=23` 后定理性消失。

## 1. 设置

取

\[
y=\max(2,\lfloor P/e\rfloor)
\]

并考察端点窗口

\[
P^2<n<P^2+P.
\]

尾素数为

\[
y<\ell<P.
\]

## 2. 双尾碰撞不可能落入平方后窗口

若 `P>=23`，审计和直接不等式给出

\[
y^3>P^2+P.
\tag{TCV-1}
\]

因此任何低筛骨架点 `n` 至多含两个不同尾素因子。若它含两个不同尾素因子
`\ell_1,\ell_2<P`，且没有低素因子，则不可能再有第三个因子，所以

\[
n=\ell_1\ell_2.
\]

但

\[
\ell_1<P,\qquad \ell_2<P
\quad\Longrightarrow\quad
n=\ell_1\ell_2<P^2,
\]

与 `n>P^2` 矛盾。因此：

```text
P>=23 时，平方后端点没有多尾碰撞超额。
```

`P=13` 的唯一碰撞样本是 `175=5^2*7`，正是因为此时 `(TCV-1)` 尚未成立。

## 3. 对 RCI 的影响

`PostSquare-RCI`

\[
G_y-T_y
=
R_0-\sum_{j\ge2}(j-1)R_j
\]

在 `P>=23` 后退化为

\[
G_y-T_y=R_0.
\tag{TCV-2}
\]

这里 `R_0` 就是端点窗口中没有任何 `<P` 素因子的点数；由于窗口位于
`(P^2,(P+1)^2)` 内，它们全部是素数。

## 4. 更新后的端点硬点

平方后端点现在不再需要控制双尾碰撞。真正剩余是：

```text
Tail-Perfect-Cover Exclusion:
低筛骨架 G_y 不能被一尾项 y<ell<P 完全吃掉。
```

若 `R_0=0`，则每个低筛骨架点都必须恰有一个尾素因子：

\[
n=\ell m,\qquad y<\ell<P,\qquad P^-(m)>y.
\]

这是一种极强的单尾完美匹配。下一步应证明这种完美匹配触发固定端点相位的
`PDEC/Tail-anchor` 缺陷，或直接构造一个低骨架点逃出所有尾素数。

进一步压缩见：

```text
docs/monograph/prime-matrix-diagonal-postsquare-tail-cofactor-identity.md
```

该文证明 `P>=23` 时上述互补因子 `m` 必为素数，且对每条 `ell` 只落入长度至多 `3`
的短区间。因此剩余硬点可改写为 `Short Prime-Cofactor Perfect-Cover Exclusion`：
短窗素互补因子不能完美吃掉平方后端点的低筛骨架。
