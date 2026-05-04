# ShiftSmooth 删除后 Möbius 符号闸门

**状态：** `alpha_tail_shiftsmooth_mobius_gate_reduction_open`

近线性删除恒等式把无符号双光滑对数降到大素数删除集问题；但真正的 `D_sigma` 还要求平方自由与
Möbius 同符号。本文把该剩余过滤精确拆成一阶 Möbius 偏置和二点 Möbius 相关。

## 1. 删除后平方自由支撑

令 `A_r` 为满足以下条件的 `d` 集合：

1. `d,d+r` 都落在高块 `(B,2B]`；
2. `d,d+r` 都为 `y`-smooth；
3. `d,d+r` 都 squarefree。

定义

\[
\mu_1(d)=\mu(d),\qquad \mu_2(d)=\mu(d+r).
\tag{MBG-1}
\]

对固定 `sigma in {+1,-1}`，

\[
C_\sigma(r)=
\#\{d\in A_r:\mu_1(d)=\sigma,\ \mu_2(d)=\sigma\}.
\tag{MBG-2}
\]

## 2. 精确闸门恒等式

在 `A_r` 上有

\[
\mathbf 1_{\mu_1=\sigma}\mathbf 1_{\mu_2=\sigma}
=
{1\over4}
\left(
1+\sigma\mu_1+\sigma\mu_2+\mu_1\mu_2
\right).
\tag{MBG-3}
\]

因此

\[
C_\sigma(r)=
{1\over4}
\left(
|A_r|
\sigma M_1(r)
\sigma M_2(r)
K(r)
\right),
\tag{MBG-4}
\]

其中

\[
M_1(r)=\sum_{d\in A_r}\mu(d),\qquad
M_2(r)=\sum_{d\in A_r}\mu(d+r),
\qquad
K(r)=\sum_{d\in A_r}\mu(d)\mu(d+r).
\tag{MBG-5}
\]

## 3. 热门同符号的二分

若

\[
C_\sigma(r)\ge {1\over4}|A_r|+\Gamma,
\tag{MBG-6}
\]

则至少发生一项：

\[
|M_1(r)|\ge {4\Gamma\over3},
\quad
|M_2(r)|\ge {4\Gamma\over3},
\quad
K(r)\ge {4\Gamma\over3}.
\tag{MBG-7}
\]

这是由 `(MBG-4)` 的三项贡献鸽巢得到。`M_1,M_2` 是删除后平方自由支撑上的一阶 Möbius 偏置；
`K(r)` 是二点 Möbius 同号相关。

## 4. 出口解释

1. **一阶偏置。**  
   若 `M_1` 或 `M_2` 大，说明删除后剩余的 `y`-smooth squarefree 集合在 Möbius 奇偶上失衡，
   进入 `PDEC/ColumnCRT`。
2. **二点相关。**  
   若 `K(r)` 大，说明位移 `r` 使 `d` 与 `d+r` 的素因子奇偶同步异常，进入
   `MobiusCorr/ShiftSmooth` 硬点。
3. **孤立窗口。**  
   若上述异常只在单个窗口发生，则进入 `SAE`。

## 5. 审稿边界

审计脚本：

```text
experiments/prime_matrix_alpha_tail_nearlinear_deletion_audit.py
```

样本：

| p | block | shift | smooth pairs | squarefree pairs | same | opposite | plus | minus | K |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 2001 | 710 | 456 | 254 | 207 | 249 | 202 |
| 5003 | 8192 | -36 | 5774 | 2416 | 1451 | 965 | 810 | 641 | 486 |
| 10007 | 16384 | -900 | 11381 | 5107 | 2963 | 2144 | 1685 | 1278 | 819 |

这里 `K=same-opposite`。样本显示同符号偏多确实主要体现为正的二点 Möbius 相关 `K`；
下一步应优先攻击 `K(r)`，而不是只估无符号双光滑数量。

## 6. 审稿边界

已证明：

```text
删除后同符号过多
=> 一阶 Möbius 偏置 或 二点 Möbius 相关异常。
```

尚未证明：

```text
这些 Möbius 异常不可能。
```

下一步最小硬点是对删除后支撑 `A_r` 证明一阶偏置和二点相关的上界；失败则输出
`PDEC/ColumnCRT/SAE` 证书。
