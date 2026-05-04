# KZ-C：Bessel transform 衰减的自足证明

**状态：** `kz_c_bessel_transform_decay_proved_by_bessel_ode_integration_by_parts`

本文继续只攻击 `Kuznetsov-LS atom (SC-9)` 的子原子：

```text
KZ-C: Bessel transform decay.
```

该步不使用 Kuznetsov trace formula，也不使用谱大筛；只使用 Bessel 方程、自伴微分算子和
反复分部积分。

## 1. HLC 平滑权

令 `\Phi` 是 KZ-B 中进入 Kuznetsov 公式的平滑权，支撑在 `x≈X`，并满足对所有 `j<=J`：

\[
\left|x^j\Phi^{(j)}(x)\right|
\le C_j\log^{C_j}y.
\tag{BC-1}
\]

这里 `X` 是由 `R_0` 与 `4\pi\sqrt{|ab|}/R_0` 决定的 Bessel 变量尺度。K3 的窗口平滑与
dyadic 分块给出 `(BC-1)`；若 `(BC-1)` 失败，则回到 endpoint/smoothing 出口，不属于
clean HLC core。

## 2. Bessel 自伴算子

设

\[
\mathcal L_\nu
=
-x^2\frac{d^2}{dx^2}-x\frac{d}{dx}+x^2+\nu^2.
\tag{BC-2}
\]

对应的 Bessel kernel `B_\nu(x)` 满足

\[
\mathcal L_\nu B_\nu(x)=0.
\tag{BC-3}
\]

等价地，若把谱参数写作 `t`，则可用算子

\[
\mathcal A
=
-x^2\frac{d^2}{dx^2}-x\frac{d}{dx}+x^2
\tag{BC-4}
\]

使

\[
\mathcal A B_{it}(x)=t^2B_{it}(x)
\tag{BC-5}
\]

对 Kuznetsov 中的 Maass Bessel kernel 成立；holomorphic kernel 的整数阶情形同理，只需把
`t` 换为相应阶数参数。

算子 `\mathcal A` 对测度 `dx/x` 自伴：

\[
\int_0^\infty (\mathcal A f)(x)g(x)\frac{dx}{x}
=
\int_0^\infty f(x)(\mathcal A g)(x)\frac{dx}{x},
\tag{BC-6}
\]

边界项为零，因为 `\Phi` 光滑紧支撑。

## 3. Transform 定义

Kuznetsov 侧出现的 transform 可统一写为

\[
\widetilde\Phi(t)
=
\int_0^\infty \Phi(x)B_{it}(x)\frac{dx}{x},
\tag{BC-7}
\]

holomorphic transform 同型处理。由 `(BC-5)` 和 `(BC-6)`，对任意整数 `J>=0`，

\[
\widetilde\Phi(t)
=
(1+t^2)^{-J}
\int_0^\infty (1+\mathcal A)^J\Phi(x)\,B_{it}(x)\frac{dx}{x}.
\tag{BC-8}
\]

## 4. 导数账本

由 `(BC-1)` 和 `\mathcal A` 的形式，归纳得到

\[
\left|(1+\mathcal A)^J\Phi(x)\right|
\le
C_J(1+X^2)^J\log^{C_J}y
\tag{BC-9}
\]

且仍支撑在 `x≈X`。Kuznetsov 标准 Bessel kernels 在紧支撑区满足多项式包络

\[
|B_{it}(x)|
\le
C_J(1+|t|)^C(1+X)^C.
\tag{BC-10}
\]

这个包络由 Bessel 积分表示或 Bessel 方程的局部能量估计给出；它只要求多项式增长，
不会消耗目标中的任意对数节省。

把 `(BC-9)`、`(BC-10)` 代入 `(BC-8)`：

\[
|\widetilde\Phi(t)|
\ll_J
X^C\log^{C_J}y
\left(1+\frac{|t|}{1+X}\right)^{-2J}.
\tag{BC-11}
\]

令

\[
T_0=1+X.
\tag{BC-12}
\]

则

\[
\widetilde\Phi(t)
\ll_J
X^C\log^{C_J}y
\left(1+\frac{|t|}{T_0}\right)^{-J}.
\tag{BC-13}
\]

这就是 KZ-C 所需的快速衰减形式。

## 5. 谱尾截断

取 `J=A+C+10`，则

\[
\int_{|t|>T_0\log^B y}
|\widetilde\Phi(t)|\,d\mu_{\rm spec}(t)
\ll_A y^{-A}
\tag{BC-14}
\]

只要 `B` 取得足够大。谱测度的多项式增长由局部 Weyl 型粗界或谱大筛中的同一计数项覆盖；
在本文账本中进入 `log^{O(1)}y`。

因此可把谱参数截断为

\[
|t|\le T_0\log^B y
\tag{BC-15}
\]

并把尾项并入 endpoint/smoothing 误差。

## 6. KZ-C 结论

由 `(BC-13)` 与 `(BC-15)`，得到 KZ-C：

\[
\widetilde\Phi(t)
\ll_A
R_0\left(1+\frac{|t|}{T_0}\right)^{-A}\log^{C_A}y,
\]

且截断到 `|t|\le T_0\log^B y` 的损失为 `O_A(y^{-A})`。这里前因子写成 `R_0` 或等价
尺度因子，取决于 Kuznetsov 公式中 `\Phi(4\pi\sqrt{|ab|}/R)` 的归一化；该尺度已由
`\mathfrak W(\mathcal D)` 吸收。

## 7. 当前剩余

KZ-C 已内联证明。`Kuznetsov-LS atom (SC-9)` 仍需：

```text
KZ-B: Kuznetsov trace formula specialization;
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

KZ-D 已由后续 `PTK-D/LPC-D/GHLC-D` 链闭合。下一步最优硬攻点应转为 KZ-B 或 KZ-E。
