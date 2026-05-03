# H5.4：OSPC*/weighted CRTDefect 吸收到 PDEC-or-SAE

本文档专攻 H5.4 与 H4 的接口。目标不是直接排除 `OSPC*` 或 `weighted CRTDefect`，而是证明它们不是新的独立出口：二者都可统一吸收到

```text
PDEC-or-SAE
```

即 persistent 低模 Fourier/CRT 缺陷或 sparse 单窗逃逸义务。

## 0. 审稿结论

当前闭合：

```text
OSPC* or weighted CRTDefect
=> named low-mod defect
=> PDEC or SAE.
```

当前未闭合：

```text
PDEC exclusion
SAE local escape exclusion.
```

因此 H5.4 的**出口吸收**已完成，但 H5.4 的**出口排斥**仍属于 H4 的最终硬义务。不能把本文写成 `OSPC*` 已矛盾。

## 1. 统一低模缺陷框架

沿用 `docs/monograph/prime-matrix-bpn-unified-pdec-sae-dichotomy.md`。

令 `X` 为同一阶段的坏窗索引集合，`Q` 为低模周期。每个低模块 `B` 给出一个零均值测试函数

\[
F_B:\mathbb Z/Q\mathbb Z\to\mathbb C,\qquad
\sum_{t\bmod Q}F_B(t)=0.
\]

每个窗口 `x` 有相位

\[
\tau(x)\in\mathbb Z/Q\mathbb Z.
\]

若

\[
\Re F_B(\tau(x))\ge \kappa_B^\star,
\tag{1}
\]

则称窗口 `x` 触发低模块 `B` 的命名缺陷。坏窗集合为

\[
S_B=\{x\in X:\Re F_B(\tau(x))\ge \kappa_B^\star\}.
\]

若 `|S_B|>=\beta |X|`，进入 `PDEC`；若 `0<|S_B|<\beta |X|`，进入 `SAE`。

## 2. OSPC* 产生低模测试函数

对 H5.1 中的低模块 `B`，按辅助模 `r_B` 的非零残基分解

\[
C_{B,a}=\sum_{m\equiv a\pmod {r_B}}W_B(m),
\qquad
\mathcal A_B=\sum_m |W_B(m)|.
\]

`OSPC*` 定义为

\[
E_{\rm dir}(B)=
{(r_B-1)\sum_a |C_{B,a}|^2\over\mathcal A_B^2}
>1+\delta_{\rm dir}.
\tag{2}
\]

令

\[
F_B(a)=
|C_{B,a}|^2
-
{1\over r_B-1}\sum_{u}|C_{B,u}|^2.
\tag{3}
\]

则 `F_B` 在 `(\mathbb Z/r_B\mathbb Z)^\times` 上均值为零。由 `(2)` 可知残基能量不均匀，因此存在 `a` 使

\[
F_B(a)>0.
\]

把窗口相位 `\tau(x)` 取为该低模块在窗口 `x` 中对应的辅助残基相位，即得到 `(1)` 型命名低模缺陷。因此：

```text
OSPC* => named low-mod defect.
```

该步骤只使用有限残基能量分解，不使用任何未证明素数分布输入。

## 3. Weighted CRTDefect 产生低模测试函数

`weighted CRTDefect` 定义为

\[
\sum_B \kappa_B m_B>\theta_{\rm WCRT}.
\tag{4}
\]

其中 `kappa_B` 满足

\[
\left|\sum_a d_{B,a}C_{B,a}\right|
\le
\kappa_B
\left(\sum_a |C_{B,a}|^2\right)^{1/2}.
\tag{5}
\]

若 `(4)` 成立，则存在一个块 `B` 和一个符号 `\varepsilon\in\{\pm1\}`，使真实粗数残差与该块残基测试函数同向偏大。取

\[
F_B(a)=
\varepsilon\,
\left(d_{B,a}C_{B,a}
-
{1\over r_B-1}\sum_u d_{B,u}C_{B,u}\right).
\tag{6}
\]

该函数同样均值为零。超界条件 `(4)` 保证某个窗口相位满足 `(1)`，于是：

```text
weighted CRTDefect => named low-mod defect.
```

这一步把加权 CRT 缺陷从一个总和阈值转成有限低模块上的零均值测试函数。

## 4. 吸收定理

**Theorem H5.4-Absorption.** 任意由 H5.1 产生的 `OSPC*` 或 `weighted CRTDefect`，都进入统一 `PDEC-or-SAE` 二分：

```text
OSPC* / weighted CRTDefect
=> PDEC or SAE.
```

**证明。**

由第 2 节，`OSPC*` 给出零均值低模测试函数 `F_B` 与非空坏窗集合 `S_B`。由第 3 节，`weighted CRTDefect` 也给出同样对象。对该 `S_B` 应用 `prime-matrix-bpn-unified-pdec-sae-dichotomy.md` 的 `UPS-1`：若 `|S_B|>=\beta|X|`，则是 persistent 分支，产生坏窗指示函数的非零 Fourier/CRT 缺陷，即 `PDEC`；若 `0<|S_B|<\beta|X|`，则是 sparse 分支，即 `SAE` 单窗逃逸义务。二分穷尽所有非空坏窗集合，故结论成立。证毕。

## 5. 对 H5 常数账本的影响

H5.4 现在应写成：

```text
C_OSPC <= 0.020 outside PDEC-or-SAE exits;
OSPC*/weighted CRTDefect exits are delegated to H4.
```

如果 H4 的 `PDEC exclusion + SAE local escape exclusion` 被证明，则这些出口贡献为零，H5.4 自动满足其 `0.020` 预算。

如果 H4 未证明，则 H5 仍不能标记为闭合。

## 6. 下一步唯一硬点

完成本文后，H5/H4 的最优硬攻顺序变为：

1. 给每个 persistent 低模块提交 `PDEC-Cert`，即证明
   \[
   \mathcal U_{\rm CRT}<\mathcal L_{\rm PDEC}.
   \]
2. 给每个 sparse 坏窗提交 `SAE-Cert`：survivor、lift 或 higher-defect。
3. 然后回到 H5.2，证明 `RRD-perp<=0.012`。

当前不能宣称：

```text
OSPC* / weighted CRTDefect are impossible.
```

只能宣称：

```text
OSPC* / weighted CRTDefect have been absorbed into PDEC-or-SAE.
```
