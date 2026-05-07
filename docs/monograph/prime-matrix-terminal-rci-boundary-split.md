# Terminal-RCI 边界块剥离

**状态：** `terminal_rci_boundary_block_proved_nonbottom_remains`

本文接续 `Terminal-SAE` 单尾抵消恒等式。目标是解释为什么样本中的最小余量常为 `1`，并把这个边界块从真正硬点中剥离。

## 1. 镜像边界块

对相邻奇素数 `p<q`，终端镜像块的 `n` 区间为

\[
I_h=[q^2-hq+1,\ q^2-(h-1)q].
\]

当 `h=q` 时，

\[
I_q=[1,q].
\tag{RBS-1}
\]

端点 `n=1` 已被排除，`n=q` 是新素数，且没有任何 `<=p` 的素因子。

## 2. 恒定余量 1

取

\[
y=\max(2,\lfloor p/e\rfloor).
\]

若

\[
y^2>q,
\tag{RBS-2}
\]

则 `[1,q]` 中每个 `y`-rough 数除 `1` 外只能是素数。于是低筛骨架精确分为：

```text
y<ell<=p 的旧尾素数；
新素数 q。
```

旧尾素数各有且仅有一个尾素因子，在 `RCI` 中完全抵消；`q` 没有尾素因子，贡献一个无尾储备。因此

\[
G_y(q)-T_y(q)=1.
\tag{RBS-3}
\]

这不是偶然小余量，而是可证明的边界证书。`(RBS-2)` 之外的小素数只需有限核查。

## 3. 审计读数

脚本：

```text
experiments/prime_matrix_terminal_rci_boundary_split_audit.py
```

输出：

```text
docs/terminal_rci_boundary_split_audit_run_20260505.txt
```

基于 `docs/terminal_sae_cancellation_audit_p2000_20260505.json`：

```text
records=302；
global min at h=q records=295；
fraction=0.976821。
```

阈值摘要：

| p 下界 | 全块最小余量 | 非底块最小余量 | 非底块最坏位置 |
|---:|---:|---:|---|
| 23 | 1 | 2 | p=23,h=18 |
| 101 | 1 | 4 | p=101,h=46 |
| 251 | 1 | 11 | p=271,h=179 |
| 501 | 1 | 22 | p=509,h=352 |
| 1009 | 1 | 44 | p=1009,h=459 |
| 1500 | 1 | 69 | p=1597,h=1031 |

所以样本中的全局最小余量 `1` 主要来自已闭合的 `h=q` 边界块；剥离后，非底块余量随 `p` 明显增厚。

## 4. 更新后的最小硬点

终端支线应拆成：

```text
Boundary block h=q:
  proved by y^2>q plus finite small p check。

Nonbottom blocks 1<=h<q:
  prove RCI, i.e. no_tail_reserve > multi_tail_excess,
  or route failure to PDEC/Tail-anchor/endpoint defect。
```

这一步没有闭合 `TerminalSquareGap`，但清除了一个伪硬点：余量 `1` 的主来源不是深层碰撞，而是镜像边界上的新素数 `q`。
