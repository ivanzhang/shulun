# 对角平方后端点 RCI 硬点

**状态：** `diagonal_endpoint_reduced_to_postsquare_rci_pdec`

本文处理早期对角段中最不能绕开的端点：

\[
x=P,\qquad P^2+1,\ldots,P^2+P-1.
\]

这一步等价于证明 `(P^2,P^2+P)` 中存在素数。普通因子降阶不能处理它，因为 `x=P` 没有 `<P` 的内部因子。

## 1. RCI 分层

取

\[
y=\max(2,\lfloor P/e\rfloor).
\]

对列 `1<=k<P`，令 `n=P^2+k`。先保留避开所有 `ell<=y` 的低筛骨架点，再统计这些点被尾素数
`y<ell<P` 命中的不同尾因子数 `omega_T(n)`。

于是有精确恒等式：

\[
G_y-T_y
=
\sum_{P^-(n)>y}(1-\omega_T(n))
=
R_0-\sum_{j\ge2}(j-1)R_j.
\tag{DPR-1}
\]

所有恰有一个尾素因子的点贡献为 `0`；真正竞争只在：

```text
无尾储备  vs  多尾碰撞超额。
```

若 `(DPR-1)>0`，则存在某个 `P^2+k` 没有任何 `<P` 素因子。由于

\[
P^2<P^2+k<P^2+P<(P+1)^2,
\]

该点必为素数。

## 2. 双尾化

若

\[
y^3>P^2+P,
\tag{DPR-2}
\]

则每个点最多含两个不同尾素因子，目标变成

```text
no_tail_reserve > two_tail_count。
```

审计中 `(DPR-2)` 的最后例外是 `P=23`。

## 3. 审计

脚本：

```text
experiments/prime_matrix_diagonal_postsquare_rci_audit.py
```

输出：

```text
docs/diagonal_postsquare_rci_audit_p10000_20260505.md
docs/diagonal_postsquare_rci_audit_p10000_20260505.json
```

读数：

```text
max_p=10000；
odd primes checked=1228；
certified=1228；
bad_count=0；
min margin=1；
max omega_tail=2；
last y^3<=p^2+p exception p=23。
```

阈值样本显示非小素数区间余量迅速增厚：

```text
p>=251  最小 margin=18；
p>=501  最小 margin=34；
p>=1009 最小 margin=65；
p>=1500 最小 margin=93。
```

## 4. 更新后的端点硬点

`x=P` 端点现在有一个与终端平方前行同型的最小接口：

```text
PostSquare-RCI/PDEC:
证明对角平方后端点中无尾储备严格大于双尾碰撞；
若失败，则失败必须表现为固定端点相位的 CRT/PDEC 缺陷。
```

这仍不是无条件闭合证明，但它把裸短区间素数命题压缩为一个可逐项审查的筛余抵消不等式。

进一步压缩见：

```text
docs/monograph/prime-matrix-diagonal-postsquare-tail-collision-vanishing.md
docs/monograph/prime-matrix-diagonal-postsquare-tail-cofactor-identity.md
```

该文证明 `P>=23` 后平方后端点的多尾碰撞超额为 `0`。所以端点剩余硬点不是双尾碰撞控制，
而是排斥“一尾项完美吃掉全部低筛骨架”的 `Tail-Perfect-Cover`。进一步的互补因子恒等式
把一尾项压缩为唯一的短窗素互补因子 `P^2+k=ell*m`，其中 `y<ell<P<m` 且每条 `ell`
只有至多 `3` 个 `m` 候选。
