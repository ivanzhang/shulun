# HLC 的 Kuznetsov-LS 原子展开

**状态：** `sc9_expanded_to_kuznetsov_trace_bessel_spectral_dispersion_atoms`

本文继续只攻击同一剩余：

```text
Kuznetsov-LS atom (SC-9).
```

目标是把 `(SC-9)` 从一句“谱大筛原子”展开成可逐行内联证明的四个子原子。本文完成这些
子原子推出 `(SC-9)` 的推导；若要求完全自足，仍必须继续证明四个子原子本身，尤其是
Kuznetsov trace formula 与 spectral large sieve。

## 1. 待证明原子

`SC-9` 要控制

\[
\mathcal Q
=
\sum_{R\sim R_0}\sum_{u\in\mathcal U(R)}
\eta_{R,u}S(a_u,b_u;R),
\tag{KZ-1}
\]

并证明

\[
|\mathcal Q|
\le
C_A
\left(\sum_{R,u}|\eta_{R,u}|^2\right)^{1/2}
\frac{\mathfrak W(\mathcal D)}{\log^A y}.
\tag{KZ-2}
\]

其中 `R≈R0`、`a_u,b_u` 来自 clean HLC completion 频率，所有 gcd/unit/endpoint/high-lcm
失败项已被排除。

## 2. 子原子 KZ-A：Kloosterman 权重平滑化

把 `R≈R0` 的硬截断换成光滑权 `\Phi_R`：

\[
\mathcal Q
=
\sum_{a,b}
\sum_{R\ge1}
\xi_{a,b}(R)\Phi_R(R)\,S(a,b;R)
+O_A(y^{-A}),
\tag{KZ-3}
\]

其中

\[
\sum_{a,b,R}|\xi_{a,b}(R)|^2
\ll
\sum_{R,u}|\eta_{R,u}|^2\log^{C_1}y.
\tag{KZ-4}
\]

这一步只使用 dyadic smoothing、Cauchy--Schwarz 和 K1--K6 的多对数账本，可在文内自足证明。

## 3. 子原子 KZ-B：Kuznetsov trace formula 专门化

对每个固定 `(a,b)`，设

\[
\mathcal K_{a,b}(\Phi)
=
\sum_{R\ge1}
\frac{S(a,b;R)}{R}\Phi\!\left(\frac{4\pi\sqrt{|ab|}}{R}\right).
\tag{KZ-5}
\]

Kuznetsov trace formula 的本文专门化为

\[
\mathcal K_{a,b}(\Phi)
=
\mathcal M_{a,b}^{\rm cusp}(\widetilde\Phi)
+\mathcal M_{a,b}^{\rm hol}(\widetilde\Phi)
+\mathcal M_{a,b}^{\rm Eis}(\widetilde\Phi)
+\mathcal D_{a,b}(\Phi),
\tag{KZ-6}
\]

其中右侧分别是 Maass cusp、holomorphic、Eisenstein 和 diagonal/exceptional 项。

本文 HLC 的 clean 支持中，`a` 或 `b` 为零的退化项已经由主项/endpoint 账本剥离；若出现
`ab=0`，必须回到 K3 endpoint 或低频主项，而不能进入 `(SC-9)`。因此 `(SC-9)` 的主层只需
处理 `ab\ne0`。

**KZ-B 原子。** 公式 `(KZ-6)` 对本文平滑权成立，且所有 oldform、Eisenstein、exceptional
项的规范化常数可统一进入 `log^{O(1)}y` 账本。

这是第一个真正谱理论输入。完全自足版必须从 Poincare series、Fourier 展开、Parseval 和
Bessel kernel 恒等式证明它。

## 4. 子原子 KZ-C：Bessel transform 窗口衰减

由 clean HLC 平滑权的导数条件，Bessel transform `\widetilde\Phi(t)` 满足：

\[
\widetilde\Phi(t)
\ll_A
R_0\,\left(1+\frac{|t|}{T_0}\right)^{-A}\log^{C_2}y,
\tag{KZ-7}
\]

并且 holomorphic 权重也满足同型衰减。这里 `T_0=T_0(\mathcal D)` 是由
`R_0`、`|ab|` 和窗口长度确定的谱频率尺度。

**KZ-C 原子。** 对本文所有 smooth dyadic block，`(KZ-7)` 成立，且截断到
`|t|\le T_0\log^{B}y` 的损失为 `O_A(y^{-A})`。

这一步是 Bessel 函数振荡积分估计。它比完整 Kuznetsov 轻，但若完全自足，仍必须逐段处理
小 `t`、过渡区和大 `t` 的积分分部。

KZ-C 已在 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-c-bessel-transform-decay.md` 中用
Bessel 微分方程、自伴算子和反复分部积分内联证明。因此它不再是未闭合谱黑箱。

## 5. 子原子 KZ-D：谱大筛

令 `\alpha_n` 支撑在本文 completion 产生的频率集合上，长度为 `N_0`，二范数有限。谱大筛
专门化为

\[
\sum_{|t_j|\le T}
\left|\sum_{n\le N_0}\alpha_n\rho_j(n)\right|^2
+\int_{-T}^{T}
\left|\sum_{n\le N_0}\alpha_n\rho_t(n)\right|^2dt
\ll
(T^2+N_0)\log^{C_3}y\sum_n|\alpha_n|^2.
\tag{KZ-8}
\]

holomorphic 谱满足同型估计。

**KZ-D 原子。** `(KZ-8)` 对本文需要的 level、nebentypus/oldform 分解和 Eisenstein 连续谱
统一成立，所有 level 与 oldform 损失为多对数。

这是第二个真正谱理论输入。完全自足版必须用正交性、Petersson/Kuznetsov 反向公式或
pre-trace 大筛证明。

## 6. 子原子 KZ-E：BFI/well-factorable dispersion 对数节省

Kuznetsov 与谱大筛给出平方根平均控制；要得到任意 `log^{-A}`，还需要本文 clean HLC
权重的 well-factorable/dispersion 结构把外层模数、频率、Type-I/II 分块的总损失吸收。
抽象写成：

\[
\mathfrak W_{\rm raw}(\mathcal D)
\le
\frac{\mathfrak W(\mathcal D)}{\log^A y}
\tag{KZ-9}
\]

在选择足够大的分解参数 `B(A)` 后成立。

**KZ-E 原子。** clean HLC 的 `gamma_{c,h}` 与 Type-I/II 系数在 well-factorable 分解后满足
`(KZ-9)`。

这是 BFI dispersion 结构在本文窗口上的专门化。若完全自足，必须展开筛权分解、Type-I/II
分块、Cauchy 后的非对角项和模数互换，而不能只引用“BFI”。

## 7. 四原子推出 SC-9

**命题。** KZ-A、KZ-B、KZ-C、KZ-D、KZ-E 成立，则 `(SC-9)` 成立。

**证明。**

1. 由 KZ-A，把 `(KZ-1)` 平滑化为 `(KZ-3)`，二范数只损失 `log^{C_1}y`。
2. 对每个 `(a,b)` 应用 KZ-B，把 Kloosterman 模数和转到 Maass、holomorphic、Eisenstein
   三个谱侧以及 diagonal/exceptional 项。
3. 由 clean 主项剥离，diagonal/exceptional 项为零或进入 endpoint/low-frequency 账本。
4. 由 KZ-C，把谱参数截断到 `|t|\le T_0\log^B y`，尾项为 `O_A(y^{-A})`。
5. 对截断后的谱侧应用 Cauchy--Schwarz；一侧由 KZ-D 谱大筛控制，另一侧由
   `(KZ-4)` 和 clean L2 账本控制。
6. 得到 raw bound
   \[
   |\mathcal Q|
   \ll
   \left(\sum_{R,u}|\eta_{R,u}|^2\right)^{1/2}
   \mathfrak W_{\rm raw}(\mathcal D)\log^{C_4}y.
   \tag{KZ-10}
   \]
7. 由 KZ-E，选 `B(A)=A+C_1+C_2+C_3+C_4+10`，把所有多对数损失吸收为
   `\log^{-A}y`，得到 `(KZ-2)`。

证毕。

## 8. 当前无黑箱闭合度

本文已经完成：

1. `(SC-9)` 到五个可审查子原子 KZ-A--KZ-E 的拆解；
2. KZ-A 的普通平滑/二范数性质定位；
3. KZ-A--KZ-E 推出 `(SC-9)` 的逐步证明；
4. 明确 diagonal/exceptional/退化频率只能回到已命名 endpoint/low-frequency 出口。

本文仍未完成完全自足闭合：

```text
KZ-B: Kuznetsov trace formula 专门化；
KZ-D: spectral large sieve 含 oldform/Eisenstein；
KZ-E: BFI/well-factorable dispersion 对数节省。
```

因此，下一步若继续无黑箱硬攻，应从 KZ-D 开始：它直接控制谱侧二范数；随后攻 KZ-B，
最后攻 KZ-E。不能把这些原子省略后宣称完全自足闭合。
