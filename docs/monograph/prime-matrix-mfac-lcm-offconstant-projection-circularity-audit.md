# MFAC LCM 去常数投影循环审计

## 范围

本证书只审计实际整数区间 \(1\le n\le 60\) 上的直接秩一
\(e_1\) 投影模板。LCM Gram 核为

\[
K_X(d,e)=\left\lfloor\frac{X}{\operatorname{lcm}(d,e)}\right\rfloor.
\]

令 \(w_d=-\mu(d)\log d\)、\(g=w-e_1\)。在实数域中，直接计算给出

\[
\langle g,e_1\rangle_{K_X}=\psi(X)-X,
\qquad \lVert e_1\rVert_{K_X}^2=X.
\]

当前有限精度审计的投影残差为
`1.3322676295501878e-15`；未中心化读数为
`-2.4667898501237873`，Chebyshev 误差读数为
`-2.4667898501237886`。

## 唯一系数与循环

对任意实数 \(\alpha\)，直接缺陷满足

\[
\langle g-\alpha e_1,e_1\rangle_{K_X}
=\psi(X)-X-\alpha X.
\]

因此令其正交的唯一系数为
\(\alpha_X=(\psi(X)-X)/X\)。本证书的该系数读数为
`-0.04111316416872981`，正交化后的有限精度缺陷为
`1.3322676295501878e-15`，理论缺陷残差为
`1.3322676295501878e-15`。

这说明**只拒绝直接秩一** \(e_1\) 模板：若它把 `psi(X)-X` 用作系数输入，
分类为 `direct_e1_projection_uses_target_or_forbidden_analytic_input`，即在中心化定义时读取待控制的目标误差。

## 未被虚构的出口

不读取目标误差的命名输入只被分类为
`direct_e1_projection_independence_unverified`，而不是被说成已经构造的独立算术对象。因此本步不排除
非秩一、非后验的实际算术结构；它也不证明所有可能的 coercive 能量机制不存在。

## 结论边界

本步固定
`actual_lcm_e1_projection_identity_available=true`、
`unique_e1_orthogonal_alpha_requires_target_error=true` 与
`direct_e1_projection_template_rejected=true`。它**不是 RH** 证明，也不提供
\(\psi\) 平滑误差、Mellin 收缩或零点排除；
`noncircular_offconstant_witness_constructed=false`、
`mathematical_nonexistence=false`、
`actual_chebyshev_mellin_contraction=false`、`rh=false`。

下一正向数学门为
`NoncircularActualOffConstantCoerciveWitnessBeforeMellin`。
