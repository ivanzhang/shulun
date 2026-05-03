# H5.1：RRD-low 出口定理

本文档专攻 H5.1。目标是把 `RRD-low` 超预算严格路由到两个命名出口：

```text
OSPC*
or weighted CRTDefect / Tail-anchor.
```

结论边界：本文闭合的是 `RRD-low` 的**出口路由**，不是排除这些出口。`OSPC*` 与 `weighted CRTDefect` 的最终排斥仍归入 H4 的 `PDEC-or-SAE` / Tail-anchor 义务。

## 0. 参数

固定

```text
epsilon_low = 0.006
delta_dir = 1/4
theta_WCRT = epsilon_low / sqrt(1+delta_dir)
           = 0.005366563145999495
```

这里 `theta_WCRT` 与 `docs/monograph/rse-low-block-exit-criterion.json` 中的 `allowed_weighted_crt_defect` 一致。

## 1. 低模块对象

在 dyadic 层 `m~M` 上，令

\[
a(m)=1_{P^-(m)>Y}-\rho_M,
\qquad
a_{\rm low}=\Pi_{\le Z}a.
\]

把低模字典分解成有限块族 `\mathcal B`。对每个块 `B`，令 `r_B` 为辅助模，令

\[
C_{B,a}=\sum_{m\equiv a\pmod {r_B}} W_B(m),
\qquad
\mathcal A_B=\sum_m |W_B(m)|.
\]

定义有向能量

\[
E_{\rm dir}(B)=
{(r_B-1)\sum_a |C_{B,a}|^2\over \mathcal A_B^2}.
\]

定义块质量

\[
m_B={\mathcal A_B\over \sqrt{r_B-1}},
\]

并令 `kappa_B` 表示真实粗数残差在该块残基分解上的归一化 CRT 缺陷强度，即

\[
\left|\sum_a d_{B,a}C_{B,a}\right|
\le
\kappa_B
\left(\sum_a |C_{B,a}|^2\right)^{1/2}.
\tag{1}
\]

这里 `d_{B,a}` 是该块上真实粗数残差的残基向量。

## 2. 两个出口定义

**OSPC\*.** 若存在块 `B` 使

\[
E_{\rm dir}(B)>1+\delta_{\rm dir},
\]

则称出现 `OSPC*` 出口。

**Weighted CRTDefect.** 若

\[
\sum_{B\in\mathcal B}\kappa_B m_B>\theta_{\rm WCRT},
\tag{2}
\]

则称出现 `weighted CRTDefect`。该出口表示真实粗数残差在低模块字典上出现加权 CRT 缺陷；它应送入 `PDEC-or-SAE` 或 Tail-anchor 排斥，而不是在 H5.1 内直接判矛盾。

## 3. H5.1 出口定理

**Theorem H5.1-RRD-low-exit.** 假设低模字典已经分块，且 Gram/非正交损失已计入 `RRD-conversion`。若没有 `OSPC*` 且没有 `weighted CRTDefect`，则

\[
|\mathcal E_{\rm low}|\le 0.006.
\]

等价地，

```text
|E_low| > 0.006
=> OSPC* or weighted CRTDefect.
```

**证明。** 由块分解，

\[
\mathcal E_{\rm low}
=
\sum_B \sum_a d_{B,a} C_{B,a}.
\]

对每个块用 `(1)`，得

\[
|\mathcal E_{\rm low}|
\le
\sum_B
\kappa_B
\left(\sum_a |C_{B,a}|^2\right)^{1/2}.
\tag{3}
\]

若没有 `OSPC*`，则对每个 `B` 有

\[
E_{\rm dir}(B)\le1+\delta_{\rm dir}.
\]

按 `E_dir` 定义，

\[
\left(\sum_a |C_{B,a}|^2\right)^{1/2}
\le
{\sqrt{1+\delta_{\rm dir}}\over \sqrt{r_B-1}}\mathcal A_B
=
\sqrt{1+\delta_{\rm dir}}\,m_B.
\tag{4}
\]

将 `(4)` 代入 `(3)`：

\[
|\mathcal E_{\rm low}|
\le
\sqrt{1+\delta_{\rm dir}}
\sum_B\kappa_Bm_B.
\]

若没有 `weighted CRTDefect`，则

\[
\sum_B\kappa_Bm_B
\le
{0.006\over\sqrt{1+\delta_{\rm dir}}}.
\]

故 `|E_low|<=0.006`。取逆否命题即得超预算必进入 `OSPC*` 或 `weighted CRTDefect`。证毕。

## 4. 与 H5 总账本的关系

H5.1 的预算项现在可写成：

```text
RRD-low <= 0.006 unless OSPC* or weighted CRTDefect.
```

因此，在 H5 常数账本中，`RRD-low` 不再是未命名误差；它已经被路由为：

1. 小情形：直接消耗 `0.006`；
2. 大情形 A：`OSPC*`，进入 H5.4 / H4 出口排斥；
3. 大情形 B：`weighted CRTDefect`，进入 `PDEC-or-SAE` / Tail-anchor 排斥。

## 5. 仍未完成的下游义务

H5.1 不排除 `OSPC*` 或 `weighted CRTDefect`。当前诚实状态是：

```text
H5.1 exit routing: closed.
OSPC*/weighted CRTDefect exclusion: still open, delegated to H4/PDEC-or-SAE.
```

特别地，不能写成：

```text
RRD-low is unconditionally <=0.006 in all cases.
```

只能写成：

```text
RRD-low is <=0.006 outside the named OSPC*/weighted-CRTDefect exits.
```

这正是后续攻 H5.4 与 H4 的入口。
