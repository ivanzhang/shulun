# BPN low-mod core CRTDefect 桥接定理

**状态：** `lowmod_core_spike_reduced_to_fourier_crtdefect`

本文处理 `low-mod core CRTDefect` 出口。目标是证明：

```text
smooth-core 低模相位尖峰
=> 非零 Fourier/CRT 模式异常
=> Directed Core CRTDefect
=> PDEC-or-SAE 框架。
```

这一步是有限循环群上的确定桥接，不使用概率模型。

## 1. 低模 core 计数场

设 `\mathcal C` 是一个着色后的不相交走廊并集，核心指示为

\[
f(d)=1_{\mathcal C}(d)\,1_{d|M_{<P}}\,1_{\mu(d)^2=1}\,
1_{\omega(d)\le K}\,1_{\mathrm{phase}(d)}.
\]

取低模 `Q`。定义 residue 计数

\[
N_b=\sum_{d\equiv b\pmod Q}f(d),\qquad b\in\mathbb Z/Q\mathbb Z,
\]

总量

\[
N=\sum_{b\bmod Q}N_b.
\]

若某个 `b` 的 `N_b` 明显高于均匀期望 `N/Q`，则称有低模 core 相位尖峰。

## 2. 相位尖峰到 Fourier 模式

令

\[
g(b)=N_b-\frac{N}{Q}.
\]

则

\[
\sum_{b\bmod Q}g(b)=0.
\]

对非平凡加性角色

\[
e_Q(hb)=\exp(2\pi i hb/Q),\qquad 1\le h<Q,
\]

定义 Fourier 系数

\[
\widehat g(h)=\sum_{b\bmod Q}g(b)e_Q(-hb)
=\sum_d f(d)e_Q(-hd).
\]

**Theorem LMC-1（相位尖峰推出非零模式）。**
若存在 `b_0` 使

\[
g(b_0)\ge \eta>0,
\tag{1}
\]

则存在 `1\le h<Q` 使

\[
|\widehat g(h)|\ge \eta.
\tag{2}
\]

**证明。**
有限 Fourier 反演给出

\[
g(b_0)=\frac1Q\sum_{h=0}^{Q-1}\widehat g(h)e_Q(hb_0).
\]

由于 `\widehat g(0)=\sum_b g(b)=0`，所以

\[
\eta\le |g(b_0)|
\le \frac1Q\sum_{h=1}^{Q-1}|\widehat g(h)|.
\]

若所有非零 `h` 都满足 `|\widehat g(h)|<\eta`，右侧严格小于
`(Q-1)\eta/Q<\eta`，矛盾。证毕。

该定理也适用于负尖峰：若 `g(b_0)\le-\eta`，对 `-g` 应用同一论证。

## 3. 模型预算尖峰版本

若预算不是均匀 `N/Q`，而是给定 `B_b`，定义

\[
g_B(b)=N_b-B_b.
\]

若总预算匹配

\[
\sum_b B_b=N,
\tag{3}
\]

且某个 `b_0` 满足 `g_B(b_0)\ge\eta`，同样得到非平凡 Fourier 模式

\[
\left|\sum_b g_B(b)e_Q(-hb)\right|\ge\eta.
\tag{4}
\]

若 `(3)` 不完全成立，则先扣除均值漂移

\[
\widetilde g_B(b)=g_B(b)-{1\over Q}\sum_c g_B(c),
\]

只要

\[
\widetilde g_B(b_0)\ge\eta,
\]

仍推出 `(4)` 的中心化版本。这给出审稿安全写法：所有模型预算必须先中心化，再谈
低模 Fourier 缺陷。

## 4. Directed Core CRTDefect 定义

**Definition LMC-Defect。**
若存在低模 `Q` 和非平凡 `h` 使

\[
\left|\sum_d f(d)e_Q(hd)\right|\ge \eta,
\tag{5}
\]

则称 `\mathcal C` 触发 `Directed Core CRTDefect`。

这是 `Directed Endpoint CRTDefect` 的 smooth-core 版本：端点缺陷的权重落在端点
sawtooth 上；core 缺陷的权重落在可用核心 `d` 的低模相位上。二者都只是有限 CRT
坐标上的非零频率异常。

## 5. 并入 PDEC-or-SAE

若同一 `Q,h` 异常在多个坏窗或多个颜色类中持续出现，则坏窗指示函数与该低模角色
发生相关，进入 `PDEC`：

```text
persistent Directed Core CRTDefect
=> bad-window Fourier/CRT defect。
```

若异常只出现在单个窗口，则它是单窗 core 锚逃逸：

```text
isolated Directed Core CRTDefect
=> SAE-core。
```

因此

```text
low-mod core CRTDefect
=> PDEC-or-SAE。
```

这一步与端点版 `PDEC-or-SAE` 完全同构；区别只在测试函数从端点 sawtooth 换成
smooth-core 低模角色。

## 6. 当前主链含义

本文已严格闭合：

```text
low-mod core residue spike
=> Directed Core CRTDefect
=> PDEC-or-SAE 出口。
```

所以 `BPN-BK` 当前剩余可进一步压缩为：

```text
1. PDEC-or-SAE 排斥；
2. finite Rankin smooth-core ledger 常数闭合。
```

low-mod core CRTDefect 不再是独立第三出口；它已经并入最终 `PDEC-or-SAE`。

补充文档 `prime-matrix-bpn-unified-pdec-sae-dichotomy.md` 已将这里的 core 版本与
endpoint sawtooth 版本统一：任意低模测试函数只要均值为零，命名缺陷都按坏窗集合大小
二分为 persistent Fourier defect 或 sparse single-window escape。故本文的
`Directed Core CRTDefect` 后续不需要单独处理，直接进入统一 `PDEC/SAE` 主接口。
