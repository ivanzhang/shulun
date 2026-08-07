# MFAC 实际 LCM Gram 能量审计

## 范围

本证书只审计实际整数区间 \(1\\le n\\le 60\) 内的有限结构。LCM Gram
核为

\[
K_X(d,e)=\\left\\lfloor\\frac{X}{\\operatorname{lcm}(d,e)}\\right\\rfloor,
\]

它精确等于两个实际整除特征函数在该有限区间内的 Gram 内积。因此，该核给出一个
非标签的正半定实际整数核；这不是任意自由模型或后验标签化结构。

## Möbius--Lambda 能量

实数域中有精确恒等式

\[
\\Lambda(n)=-\\sum_{d\\mid n}\\mu(d)\\log d,
\qquad
\\sum_{n\\le X}\\Lambda(n)^2
=\\sum_{d,e\\le X}\\mu(d)\\mu(e)\\log d\\log e\,K_X(d,e).
\]

代码对上式在浮点运算下作有限精度数值审计，而不把数值残差称为任何 \(\\psi\)
误差项。当前读数为：LCM Möbius 能量 `168.95392237932234`，
Lambda 平方能量 `168.95392237932234`，浮点审计残差
`0.0`。

## 常数方向障碍

对 \(\\Lambda(n)-1\) 的普通 Cauchy 投影，常数方向的范数平方为
`60`，故只产生
\(|\\sum(\\Lambda(n)-1)|^2\\le X\\sum(\\Lambda(n)-1)^2\) 型界。其 \(\\sqrt X\)
常数方向规模正是本审计记录的障碍：仅靠普通 Cauchy 不能导出所需的 off-constant
coercivity 或 Mellin 收缩。六倍数非素数幂见证为：`6, 12, 18, 24, 30, 36, 42, 48, 54, 60`。

## 中心化输入边界

中心化合同样本读取 `psi(X)` 时被拒绝，分类为
`centered_kernel_uses_target_or_forbidden_analytic_input`。这只说明该样本
不构成独立算术输入；并未证明数学上所有可能的中心化或收缩机制都不存在。

## 结论边界

本成果固定了实际整数嵌入、实际 Chebyshev 测度、非标签带符号 LCM 核及其正半定
能量身份，并记录普通 Cauchy 的常数方向障碍。它**不是** \(\\psi\) 平滑误差估计、
零点排除或 RH 证明；`actual_chebyshev_mellin_contraction_present=false`、
`mathematical_nonexistence_proved=false`、`rh_proved=false`。

下一正向数学门为
`ActualOffConstantCoerciveEnergyIdentityBeforeMellin`。
