# 底部缺口对容量硬点

**状态：** `bottom_band_exact_decomposition_reduced_to_square_root_prime_windows`

本文接续圆柱斜线完成模型，专门处理

\[
x=P-h,\qquad 1\le h<\sqrt P
\]

的底部带。这里未完成高素斜线的补洞不再是任意覆盖，而有精确二次坐标。

## 1. 精确分解

第 `P-h` 行的列为

\[
N=(P-h)P+c,\qquad 1\le c<P.
\]

若 `N` 属于低骨架残洞 `R_{P-h}` 且为合数，则 `N` 没有 `<=P-h` 的素因子。
又 `N<P^2`，所以它只能有两个大因子，且两个因子都落在 `(P-h,P)`。

写

\[
N=(P-a)(P-b).
\]

因为 `1<=a,b<h` 且 `ab<h^2<P`，比较

\[
P(P-h)+c=P^2-(a+b)P+ab
\]

得到

\[
a+b=h,\qquad c=ab.
\tag{BDP-1}
\]

因此底部带中有精确并集：

\[
R_{P-h}
=
\{\text{本行素数列}\}
\sqcup
\{a(h-a):1\le a\le h/2,\ P-a,\ P-h+a\text{ 均为素数}\}.
\tag{BDP-2}
\]

第二项就是未完成高素斜线补洞 `F_{P-h}`。

## 2. 修正后的容量界

由 `(BDP-2)` 立刻得到

\[
|F_{P-h}|\le \left\lfloor {h\over2}\right\rfloor.
\tag{BDP-3}
\]

这里必须使用 `floor(h/2)`，不能使用 `floor((h-1)/2)`。当 `h` 为偶数且
`P-h/2` 为素数时，平方

\[
(P-h/2)^2
\]

确实是合法的高素补洞。样本中已经出现：

```text
P=997,  h=28: (983)^2, column=196；
P=5003, h=68: (4969)^2, column=1156。
```

所以底部带闭合可写为

\[
|R_{P-h}|>\left\lfloor {h\over2}\right\rfloor.
\tag{BDP-4}
\]

等价地，由 `(BDP-2)` 看，必须证明本行素数列足以超过缺失的补洞容量。

## 3. 与终端行的关系

`h=1` 时没有高素对补洞，`(BDP-4)` 退化为

```text
(P^2-P, P^2) 中存在素数。
```

这正是 `TerminalSquareGap`。因此底部带不是终端硬点的替代品，而是把终端行和近平方多行统一成同一个平方根长度短区间问题：

```text
每个长度约 P 的近平方行窗口内，素数洞不能全部消失。
```

## 4. 分段审计

脚本：

```text
experiments/prime_matrix_bottom_deficit_pair_bound_segmented_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_bottom_deficit_pair_bound_segmented_audit.py \
  --p-list 997,1999,5003,10007,20011,50021,100003 --format table
```

完整输出保存于：

```text
docs/bottom_deficit_pair_bound_segmented_audit_run_20260505.txt
```

摘要：

| P | 底部行数 | 每行有素数 | 最小素数洞 | 修正最小余量 | 最大补洞对 | 平方补洞样本行 |
|---:|---:|---|---:|---:|---:|---|
| 997 | 30 | True | 61 | 51 | 1 | 12,28 |
| 1999 | 43 | True | 114 | 93 | 2 | 4,12,24,40 |
| 5003 | 69 | True | 260 | 245 | 2 | 8,20,32,60,68 |
| 10007 | 99 | True | 511 | 468 | 1 | 68,80 |
| 20011 | 140 | True | 966 | 901 | 4 | 28,36,40,64,76 |
| 50021 | 222 | True | 2207 | 2116 | 3 | 44,56,60,128,156 |
| 100003 | 315 | True | 4218 | 4100 | 7 | 24,28,64,84,148 |

这些数据说明：修正平方通道后，容量余量仍很厚；最薄行通常不是补洞对最多的行，而是素数短区间密度较低的行。

## 5. 当前最小硬点

底部带的几何部分已经闭合为 `(BDP-2)`。剩余硬点不再是“未完成线能否任意补洞”，而是：

```text
BottomPrimeWindow:
对 1<=h<sqrt(P)，区间 ((P-h)P, (P-h+1)P) 中存在足够素数，
至少要使 prime_holes + pair_holes > floor(h/2)。
```

若坚持纯方阵内部闭合，下一步应证明 `BottomPrimeWindow` 失败会触发
`SAE/PDEC/ColumnCRT` 缺陷；若允许外部输入，则它应明确标注为平方根尺度短区间素数输入。
