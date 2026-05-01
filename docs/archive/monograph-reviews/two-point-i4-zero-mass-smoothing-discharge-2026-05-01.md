# I4 Zero-Mass 与平滑回退放电审查（2026-05-01）

## 目标

I4 原作为独立输入，包括：

1. 加权 Bonferroni Zero-Mass 下界；
2. 平滑窗口回退尖锐窗口的端点损失控制。

本轮证明显示：I4 不需要作为独立结构输入保留。它可以放电为 I3 的矩常数与 Directional Balance 端点估计。

## 文稿位置

- `docs/monograph/two-point-secondary-sieve-research.md` 第 345--349 节；
- `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的 `Zero-mass and smoothing discharge` 引理。

## Zero-Mass 放电

对每个整数 `R>=0`，

\[
1_{R=0}\ge 1-R+\binom R2-\binom R3_+.
\]

乘以 `X_B>=0` 并对块求和。若 I3 给出

\[
M_1\le0.45,\qquad M_2\ge0.05,\qquad M_3\le0.03,
\]

其中

\[
M_1=\frac{\sum X_BR_B}{\sum X_B},\quad
M_2=\frac{\sum X_B\binom{R_B}{2}}{\sum X_B},\quad
M_3=\frac{\sum X_B\binom{R_B}{3}_+}{\sum X_B},
\]

则

\[
\rho_0
\ge 1-M_1+M_2-M_3
\ge 0.57.
\]

这强于所需 `rho0>=0.30`。

## 平滑回退放电

取 `W_- <= 1_{|t|<1} <= W_+`，且 `W_+-W_-` 支撑在端点层 `1-Delta <= |t| <= 1+Delta`。若 I3 的 Directional Balance 给出

\[
N_{endpoint}/N_{total}\le C_{end}\Delta+o(1),
\]

则选择 `Delta <= 0.01/C_end` 后，对充分大 `P` 有

\[
E_{smooth}<0.03.
\]

## 当前状态

I4 已降级为 I3 的两个接口：

- 矩接口：`M1<=0.45`, `M2>=0.05`, `M3<=0.03`；
- 端点接口：`N_endpoint/N_total <= C_end Delta + o(1)`。

因此当前真正剩余为：

1. I2：自适应真实命中分层与 Single-Prime CRTDefect；
2. I3：SC2/45-Main/小素有限包，并同时提供 I4 的矩常数和端点平衡。
