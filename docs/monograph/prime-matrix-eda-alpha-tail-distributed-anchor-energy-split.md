# 分散高尾锚点能量拆分

**状态：** `alpha_tail_distributed_anchor_energy_split_reduction_open`

本文处理 `Tail-anchor energy route` 的分散能量分支。目标是把

\[
\sum_q |A_q(r)|^2
\tag{DAE-1}
\]

拆成点负载平方和与跨点相关；前者是 Rankin 型局部负载，后者是 PDEC/ColumnCRT 型相位相关。

## 1. 点锚点向量

对每个 `d in A_r` 与高素 `q`，定义

\[
a_q(d)=
\begin{cases}
-2W_q(d),& q\nmid r,\ d\equiv0\ {\rm or}\ -r\pmod q,\\
0,& \text{otherwise}.
\end{cases}
\tag{DAE-2}
\]

于是

\[
A_q(r)=\sum_{d\in A_r}a_q(d).
\tag{DAE-3}
\]

## 2. 能量展开

有精确恒等式

\[
\sum_q |A_q(r)|^2
=
\sum_{d\in A_r}\sum_q |a_q(d)|^2
+
\sum_{\substack{d_1,d_2\in A_r\\d_1\ne d_2}}
\sum_q a_q(d_1)a_q(d_2).
\tag{DAE-4}
\]

第一项是点负载平方和；第二项是跨点锚点相关。

## 3. 二分

若 `(DAE-1)` 大，则至少发生一项：

1. **点负载异常。**

\[
\sum_{d\in A_r}\left(\#\{q:a_q(d)\ne0\}\right)^2
\tag{DAE-5}
\]

大。这意味着许多 `d,d+r` 带有过多未锁高素单边因子，进入 `Rankin/Tail` 上界。

2. **跨点相位相关。**

\[
\sum_{d_1\ne d_2}\sum_q a_q(d_1)a_q(d_2)
\tag{DAE-6}
\]

大。这意味着不同点在同一高素锚点和同一低模符号下同步，进入 `PDEC/ColumnCRT`。

## 4. Rankin 负载上界接口

若 `a_q(d)\ne0`，则 `q` 整除 `d(d+r)` 且 `q>R`、`q\nmid r`。因此点负载被

\[
\Omega_{>R}(d(d+r))
\tag{DAE-7}
\]

控制。Rankin 不等式给出

\[
\#\{d:\Omega_{>R}(d(d+r))\ge L\}
\le
2^{-L}\sum_{d\in A_r}2^{\Omega_{>R}(d(d+r))}.
\tag{DAE-8}
\]

这把点负载异常送入已有 Rankin/Tail 账本。

## 5. 审稿边界

审计脚本：

```text
experiments/prime_matrix_alpha_tail_anchor_energy_audit.py
```

样本：

| p | block | shift | R | pairs | active anchors | total tail | energy | point-load bound | max point |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 31 | 710 | 124 | 82 | 13436 | 14780 | 8 |
| 5003 | 8192 | -36 | 31 | 2416 | 450 | 402 | 50076 | 54996 | 8 |
| 10007 | 16384 | -900 | 31 | 5107 | 887 | 680 | 168496 | 127648 | 8 |

样本显示单点负载最大仅为 `8`，点负载不是主要爆炸源；真正硬点更可能是跨点锚点相关的同号累积，
即 `PDEC/ColumnCRT` 分支。

## 6. 审稿边界

已证明：

```text
distributed anchor energy
=> point-load Rankin anomaly 或 cross-point PDEC/ColumnCRT correlation.
```

尚未证明：

```text
两类异常不可能。
```

下一步最小硬点是核验 Rankin 点负载预算；若预算失败，输出具体高负载点并回流 SAE/ColumnCRT。
