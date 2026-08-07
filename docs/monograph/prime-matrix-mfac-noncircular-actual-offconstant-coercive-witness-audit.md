# MFAC 非循环实际去常数强制见证（Mellin 前）

## 有限实际见证

本证书只使用有限实际整数区间 \(1\le n\le 60\) 的有限整数 LCM Gram 条目。

\[
K_X(d,e)=\left\lfloor\frac{X}{\operatorname{lcm}(d,e)}\right\rfloor.
\]

取实际一维方向

\[
h_X=e_2-\frac{\lfloor X/2\rfloor}{X}e_1.
\]

等价地，见证可记为 `h_X=e_2-floor(X/2)e_1/X`。

系数来源为 `K_X(1,2)/K_X(1,1)`；因此
\(\langle h_X,e_1\rangle_{K_X}=0\)。精确能量为

\[
\lVert h_X\rVert_{K_X}^2
=\frac{m_X(X-m_X)}{X},
\qquad m_X=\lfloor X/2\rfloor,
\]

并满足一维下界 \(\lVert h_X\rVert_{K_X}^2\ge 2X/9\)。当前
`limit=60` 的精确能量为
`15/1`，
下界读数为 `13.333333333333334`。

## 非循环合同

见证使用 `integer_limit_X, K_X(1,1), K_X(1,2)`，禁止依赖未被使用；
`forbidden_uses=()`。它不读取 Chebyshev 目标误差，
不读取 Mellin 输入、零点或显式公式输入，因而只是 Mellin 前的实际有限整数构造。

## 结论边界

这仅是实际一维方向强制性，不是全空间谱隙，也不是 Mellin 收缩。它不是
Chebyshev 误差界、非零点排除、非 RH；更具体地说，
`actual_chebyshev_mellin_contraction_present=false`、`rh_proved=false`。
它不宣称全空间去常数方向的一致强制性，也不提供任何解析收缩律。

下一正向数学门为 `UniformOffConstantCoercivityOrActualChebyshevMellinContractionLaw`。
