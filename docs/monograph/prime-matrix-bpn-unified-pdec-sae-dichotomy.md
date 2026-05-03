# BPN 统一 PDEC-or-SAE 二分定理

**状态：** `endpoint_and_core_defects_unified_to_pdec_or_sae`

本文把 endpoint sawtooth 缺陷与 smooth-core 低模缺陷统一成同一个有限测试函数框架。
目标是闭合以下桥接层：

```text
named low-mod defect
=> Persistent Fourier defect
   或 Single-window escape obligation。
```

这仍不是最终排斥；它把最后出口统一成两个明确任务。

## 1. 统一低模测试函数

令 `Q` 为低模周期，`X` 为同一阶段的窗口索引集合。对每个窗口 `x∈X`，有一个
低模测试函数

\[
F_x:\mathbb Z/Q\mathbb Z\to\mathbb C
\]

满足均值为零：

\[
\sum_{t\bmod Q}F_x(t)=0.
\tag{1}
\]

两类已有缺陷都属于该框架：

1. **Endpoint 缺陷：** `F_x(t)` 是端点 sawtooth 块投影；
2. **Core 缺陷：** `F_x(t)` 是 smooth-core residue/Fourier 投影。

窗口 `x` 的相位记为 `\tau(x)\in\mathbb Z/Q\mathbb Z`。若

\[
\Re F_x(\tau(x))\ge \kappa,
\tag{2}
\]

则称 `x` 是同一低模块的坏窗。

## 2. 坏窗集合二分

令

\[
S=\{x\in X:\Re F_x(\tau(x))\ge\kappa\}.
\]

取密度阈值 `\beta>0`。

**Theorem UPS-1（统一 PDEC-or-SAE 二分）。**
若 `S` 非空，则必有以下一项：

1. **Persistent branch：** `|S|\ge\beta |X|`；
2. **Sparse branch：** `0<|S|<\beta |X|`。

第一项是 `PDEC` 候选；第二项是 `SAE` 候选。

**证明。**
这是按集合大小的排中律。证毕。

该定理看似简单，但它的作用是审稿分工：任何命名低模缺陷都必须明确落入这两个分支之一，
不能把“单窗尖峰”误当作“全周期 CRT 矛盾”。

## 3. Persistent 分支推出 Fourier 缺陷

为简洁先写 `F_x=F` 固定的情况；分块固定后 endpoint/core 缺陷均可如此处理。
令

\[
g(t)=\#\{x\in S:\tau(x)=t\}.
\]

若 `|S|\ge\beta |X|`，且 `F` 均值为零，则

\[
\sum_{t\bmod Q}g(t)\Re F(t)
=\sum_{x\in S}\Re F(\tau(x))
\ge \kappa |S|.
\tag{3}
\]

由于 `F` 零均值，只有 `g` 的非零 Fourier 模式贡献。由 Parseval 与 Cauchy--Schwarz：

\[
\sum_{h\ne0}|\widehat g(h)|^2
\ge
\frac{\kappa^2 |S|^2}{\|F\|_2^2}.
\tag{4}
\]

因此存在 `h\ne0` 使

\[
|\widehat g(h)|
\ge
\frac{\kappa |S|}{\sqrt{Q-1}\,\|F\|_2}.
\tag{5}
\]

这就是统一 `PDEC`：坏窗相位分布在某个非零低模频率上异常。

## 4. Sparse 分支就是 SAE 义务

若 `0<|S|<\beta |X|`，Fourier 下界 `(5)` 太弱，不能推出全局 CRT 矛盾。此时必须逐个坏窗证明
单窗逃逸不可能：

```text
SAE(x):
触发低模缺陷的孤立坏窗 x
必须含旧核心素数、壳层旧筛幸存者，
或触发更高层尾锚/复用能量超标。
```

Endpoint 版本称为 `SAE-endpoint`；core 版本称为 `SAE-core`。二者共享同一逻辑：

```text
isolated low-mod spike
cannot alone erase all local survivors.
```

## 5. 统一主链

因此任意 endpoint/core 命名缺陷都满足：

```text
named low-mod defect
=> PDEC
   或 SAE。
```

更精确地：

```text
Persistent branch
=> nonzero Fourier/CRT defect of bad-window indicator；

Sparse branch
=> finite list of single-window escape obligations。
```

## 6. 当前未闭合部分

本文闭合的是统一二分和 persistent 分支的 Fourier 化。仍未闭合的是两个最终排斥：

1. **PDEC 排斥：** 证明坏窗指示函数的非零低模频率与 CRT 均衡/列见证/镜像端点刚性矛盾；
2. **SAE 排斥：** 证明孤立坏窗不能同时避开旧核心素数、壳层旧筛幸存者和尾锚复用能量。

因此 `BPN-BK` 当前最终剩余为：

```text
PDEC exclusion
+ SAE local escape exclusion
+ finite Rankin smooth-core ledger constants。
```

这比先前的 endpoint/core 分散出口更窄：所有低模缺陷已经统一到同一 `PDEC-or-SAE`
主接口。
