# HDL 到逐列 CoreLoad 的恒等式

**状态：** `alpha_tail_hdl_coreload_identity_reduction_open`

本文把高 dyadic 端点锁继续压缩为逐列低素核心负载。目标是把 `HDL-9/HDL-10` 从“模数端点异常”
改写成“某些列的低素因子子集乘积异常”，从而接入已有的 TailCore、ColumnCRT 与 PDEC 出口。

## 1. 逐列低素核心

固定

\[
H=p-1,\qquad y=\lfloor0.9p\rfloor,\qquad n_k=p^2+k\quad(1\le k\le H).
\tag{HCL-1}
\]

定义列 `k` 的低素 squarefree 核：

\[
G_y(k)=\prod_{\substack{q\le y\\ q\ {\rm prime}\\ q\mid n_k}}q.
\tag{HCL-2}
\]

对高 dyadic 区间 `I\subset(H,\infty)`，定义符号核心负载

\[
C_I^\pm(k)=
\#\{d\in I:d\mid G_y(k),\ \mu(d)=\pm1\}.
\tag{HCL-3}
\]

这里 `d|G_y(k)` 自动表示 `d` squarefree 且所有素因子 `<=y`。

## 2. CoreLoad 恒等式

沿用高块端点锁中的

\[
A_I^\pm(p)=
\#\{d\in I:d\mid M_y,\ d\ {\rm squarefree},\ \mu(d)=\pm1,\ \rho_d(p)\le H\}.
\tag{HCL-4}
\]

则有精确恒等式

\[
A_I^\pm(p)=\sum_{k=1}^H C_I^\pm(k).
\tag{HCL-5}
\]

**证明。**  
当 `d>H` 时，`rho_d(p)<=H` 当且仅当存在唯一 `k in [1,H]` 使 `d|p^2+k`。
若再要求 `d|M_y`，则 `d` 的所有素因子均 `<=y`，等价于 `d|G_y(k)`。
按这个唯一 `k` 分组求和，得到 `(HCL-5)`。证毕。

## 3. HDL 异常的逐列形式

由高 dyadic 端点锁，若

\[
E_I(p)\le-\tau,
\tag{HCL-6}
\]

则至少发生

\[
\sum_{k=1}^H C_I^+(k)\le H R_I^+-{\tau\over2},
\tag{HCL-7}
\]

或

\[
\sum_{k=1}^H C_I^-(k)\ge H R_I^-+{\tau\over2}.
\tag{HCL-8}
\]

其中

\[
R_I^\pm=
\sum_{\substack{d\in I\\ d\mid M_y\\ \mu(d)=\pm1}}{1\over d}.
\tag{HCL-9}
\]

这说明 `HDL` 异常不是孤立模数现象，而是逐列低素核心子集乘积的总负载异常。

## 4. 三个可用出口

`(HCL-7)` 与 `(HCL-8)` 分别对应不同的后续攻击。

1. **奇核心过剩。**  
   `(HCL-8)` 给出奇 Möbius 高核心子集乘积过多。若集中在少数列，则进入 Tail-anchor；
   若分散在许多列，则进入 Distributed-CoreLoad 预算。
2. **偶核心亏损。**  
   `(HCL-7)` 表示偶核心高子集乘积相对 harmonic 期望不足。若这种不足持续出现，等价于
   `p^2` 固定相位在大量偶核心模数上系统性避开端点，进入 PDEC。
3. **列残基异常。**  
   对固定列 `k`，`C_I^\pm(k)` 只由低素因子集合 `{q<=y:q|p^2+k}` 决定；若负载尖峰或空洞
   超过短窗几何预算，则进入 ColumnCRT。

## 5. 当前最小硬点

当前最窄剩余已变成：

```text
证明 HCL-7/HCL-8 的总量异常
必进入 Tail-anchor、Distributed-CoreLoad、ColumnCRT 或 PDEC，
并排斥这些出口。
```

本文只完成恒等式和路由，不排斥出口；因此不升级 Prime Matrix 对角分支状态。
