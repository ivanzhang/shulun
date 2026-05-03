# BPN 着色不相交走廊的核心筛预算

**状态：** `colored_corridor_budget_reduced_to_finite_rankin_ledger_or_lowmod_defect`

本文处理上一节留下的出口：

```text
Colored disjoint-corridor core-sieve budget / low-mod CRTDefect。
```

重要校正：这里计数的是 `d|M_{<P}`、`\omega(d)\le K` 的小素数 squarefree
核心，即 smooth-core 计数；不能直接套用 rough-number Selberg 下界。可无条件使用的是
有限 Rankin 账本；若相对模型预算失败，则失败必须表现为低模相位缺陷。

## 1. 着色走廊计数对象

固定一个颜色类 `c`。它给出不相交走廊并集

\[
\mathcal C=\bigsqcup_{j=1}^{J}[A_j,B_j]\cap\mathbb Z
\subset [D_0,2D_0).
\]

令

\[
\sigma_K(d)=1_{d|M_{<P}}\,1_{\mu(d)^2=1}\,1_{\omega(d)\le K}\,1_{\mathrm{phase}(d)}.
\]

颜色类核心计数为

\[
N_K(\mathcal C)=\sum_{d\in\mathcal C}\sigma_K(d).
\tag{1}
\]

这里 `phase(d)` 表示前文保留下来的有限低模相位条件；没有相位条件时取恒等为 `1`。

## 2. 有限 Rankin 账本

对任意 `s>0`，因 `d<2D_0`，有

\[
1\le \left({2D_0\over d}\right)^s.
\]

于是得到完全有限的 Rankin 上界：

\[
N_K(\mathcal C)
\le
(2D_0)^s
\sum_{d\in\mathcal C}
{\sigma_K(d)\over d^s}.
\tag{2}
\]

若去掉走廊位置，仅保留全局 smooth-core 条件，则

\[
N_K(\mathcal C)
\le
(2D_0)^s
\sum_{j=0}^{K}
e_j\left(\{p^{-s}:p<P\}\right),
\tag{3}
\]

其中 `e_j` 是初等对称多项式，且相位条件只会进一步减小右端。这是无条件可计算包络，
但可能过粗。

更细的有限账本保留走廊与相位：

\[
\mathcal R_s(\mathcal C;K)
=
(2D_0)^s
\sum_{d\in\mathcal C}{\sigma_K(d)\over d^s}.
\tag{4}
\]

则

\[
N_K(\mathcal C)\le \mathcal R_s(\mathcal C;K).
\tag{5}
\]

`(4)` 是有限和，不含外部解析定理。

## 3. 低模残差账本

取低模 `Q`，把 `\mathcal C` 分为剩余类：

\[
\mathcal C_b=\{d\in\mathcal C:d\equiv b\pmod Q\}.
\]

定义

\[
N_b=\sum_{d\in\mathcal C_b}\sigma_K(d),
\qquad
R_b(s)=
(2D_0)^s\sum_{d\in\mathcal C_b}{\sigma_K(d)\over d^s}.
\]

则逐类有

\[
N_b\le R_b(s),\qquad
N_K(\mathcal C)\le\sum_{b\bmod Q}R_b(s).
\tag{6}
\]

给定一个模型预算 `B_b`。若

\[
N_K(\mathcal C)>\sum_{b\bmod Q}B_b,
\tag{7}
\]

则至少存在一个 `b` 使

\[
N_b>B_b.
\tag{8}
\]

这就是低模核心相位缺陷。若 `B_b` 取为按 `R_b(s)` 证明的可审查上界，则 `(8)`
不可能；若 `B_b` 取为均匀模型预算，则 `(8)` 是 `low-mod CRTDefect` 的核心版。

## 4. 预算二分定理

**Theorem CCB-1（着色走廊预算二分）。**
给定目标预算 `B`、Rankin 参数 `s>0`、低模 `Q` 与逐类预算 `B_b`，若

\[
N_K(\mathcal C)>B,
\tag{9}
\]

则至少发生以下一项：

1. 有限 Rankin 账本本身不足：

\[
\mathcal R_s(\mathcal C;K)>B;
\tag{10}
\]

2. 若 `B\ge\sum_b B_b` 且 `\mathcal R_s(\mathcal C;K)\le B`，则不可能有 `(9)`；
3. 若使用模型预算且 `B=\sum_b B_b`，则存在 `b` 满足 `(8)`，触发
   `low-mod core CRTDefect`。

**证明。**
由 `(5)`，若 `\mathcal R_s(\mathcal C;K)\le B`，则 `N_K(\mathcal C)\le B`，
与 `(9)` 矛盾。因此 `(9)` 首先强制 `(10)`，除非目标预算是按更细逐类模型
`B_b` 分配而非按 Rankin 账本分配。后一情形由 `(7)` 的鸽巢原理给出 `(8)`。
证毕。

## 5. 有限账本闭合条件

如果能对所有颜色类证明

\[
\sum_c \mathcal R_{s_c}(\mathcal C_c;K)
\le B_{\rm allowed},
\tag{11}
\]

则着色走廊预算闭合。若 `(11)` 失败，失败不是逻辑缺口，而是一个明确的常数/参数义务：

```text
选择更优 s_c、Q、相位分层；
或证明超预算来自低模 core CRTDefect；
或承认该路线当前不能闭合。
```

## 6. 当前主链含义

本文已严格证明：

```text
Colored disjoint-corridor budget violation
=> finite Rankin ledger obstruction
   或 low-mod core CRTDefect。
```

因此 `BPN-BK` 的当前最小剩余进一步变成：

```text
1. PDEC-or-SAE 排斥；
2. finite Rankin smooth-core ledger 常数闭合；
3. low-mod core CRTDefect 排斥。
```

第 2 项是可计算常数任务；第 1、3 项是同一类低模/单窗出口排斥任务。

补充文档 `prime-matrix-bpn-lowmod-core-crtdefect-bridge.md` 已将第 3 项并回
`PDEC-or-SAE`。若低模 residue 计数

\[
N_b=\sum_{d\equiv b\pmod Q}\sigma_K(d)
\]

出现尖峰 `N_b-N/Q>=\eta`，有限 Fourier 反演给出某个非平凡角色 `h` 满足

\[
\left|\sum_d\sigma_K(d)e_Q(hd)\right|\ge\eta.
\]

这就是 `Directed Core CRTDefect`；若持续出现则进入 `PDEC`，若孤立出现则进入
`SAE-core`。因此 low-mod core CRTDefect 不再是独立剩余出口。

## 7. 可执行证书格式

补充脚本 `experiments/prime_matrix_bpn_rankin_ledger_certificate_audit.py` 已将第 2 项转成
可复核证书：

```text
输入：P, K, 不相交走廊区间 [A_j,B_j], 低模 Q；
输出：exact smooth-core count, Rankin ledger, residue spike table。
```

若走廊并集跨多个 dyadic 尺度，Rankin 因子必须逐走廊使用右端点：

\[
1_{d\in[A_j,B_j]}
\le
\left({B_j\over d}\right)^s.
\]

因此证书账本应写为

\[
\mathcal R_s(\mathcal C;K)
=
\sum_j
\sum_{d\in[A_j,B_j]}
\sigma_K(d)\left({B_j\over d}\right)^s.
\tag{12}
\]

这比单一 `D_0` 因子更安全；若所有走廊同属 `[D_0,2D_0)`，则 `(12)` 退化到前文
`(2D_0)^s\sum \sigma_K(d)d^{-s}`。

审稿使用规则：

```text
若 Rankin ledger <= allowed budget，则该颜色类闭合；
若 Rankin ledger > allowed budget，查看 residue spike；
若某低模相位尖峰超过阈值，则登记为 low-mod core CRTDefect；
否则必须调参、细分走廊或承认常数账本未闭合。
```

补充文档 `prime-matrix-bpn-rankin-ledger-acceptance-theorem.md` 已把上述规则严写成
验收定理：若某颜色类证书给出

\[
\mathcal R_s(\mathcal C;K)\le B_{\rm allow},
\]

则该颜色类核心计数 `N_K(\mathcal C)` 自动不超过允许预算；多颜色类逐项求和即可。
若证书不通过，失败只能登记为常数账本未闭合或 `low-mod core CRTDefect`。
