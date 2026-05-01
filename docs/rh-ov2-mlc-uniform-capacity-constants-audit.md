# OV2/MLC Uniform 零频容量常数化审查

本文补强 `docs/rh-ov2-mlc-uniform-absorption.md` 的最后容量硬点：当主层 overlap 质量对 PPI 所有允许窗口均不可检测，并且已排除 FCT、SC/LV、DSO/PI 时，Uniform 零频背景为何不能承载 `E_ov>X^{1+ε}` 级异常。本文只做条件化常数化审查，不宣称 RH 已证明。

## 1. Uniform 分支输入

固定主层 `Q,R`，满足 AAI 正规形

`n=q_1q_2r`, `q_i~Q`, `r~R`, `Q^2R~X`。

设 `μ=μ_{Q,R}` 为 overlap 推送到 PPI 相位空间的测度，`μ^0` 为零频基线。Uniform 分支假设：

1. 对所有允许窗口 `A∈𝓦(K')`，`|μ(A)-μ^0(A)|<τ`；
2. 质量不集中到短窗或低体积集，故非 `SC/LV/LSMP`；
3. 频率不落入固定低维闭包，故非 `FCT`；
4. 分散非主频率平方能量不超过 DSO/PI 容量。

## 2. partition 复杂度与误差预算

取固定复杂度 PPI partition `𝓟`，由 dyadic 层、倒数环带、Bohr 短弧和有限布尔组合生成。由固定复杂度假设，

`|𝓟| <= log^{C_P}X`, `Σ_{P∈𝓟} μ^0(P) <= W_Q log^{C_P}X`。

若 partition 复杂度超过该量级，则不是 Uniform，而进入 `CE/LSMP/FCT`。若边界或 Vaaler 尾项承载固定比例能量，则由 `docs/rh-fourier-vaaler-tail-uniform-audit.md` 转入 `CE/LSMP/DSO-PI`。

## 3. PPI 不可检测反面阈值

令 `τ` 为 PPI seed 触发阈值的反面。可取保守形式

`τ = W_Q^{1/2} log^{-C_τ}X`。

若某允许窗口偏差 `>=τ`，则 PPI 触发 D 组终端；当前 Uniform 分支排除该情形。因此每个 partition 原子的误差贡献满足

`|μ(P)-μ^0(P)| <= τ`。

平方能量误差和由

`Σ_{P∈𝓟}|μ(P)-μ^0(P)|^2 <= |𝓟|τ^2 <= W_Q log^{C_P-2C_τ}X`。

取 `C_τ>C_P+C_margin`，该项被 `W_Q log^{-C_margin}X` 吸收。

## 4. Uniform 零频能量界

Uniform 能量分解为零频主项与不可检测误差项：

`E_unif(Q,R) <= Σ_P μ^0(P)^2/μ^0(P) + Σ_P |μ(P)-μ^0(P)|^2/μ^0(P)`。

用有限重叠与下截断处理小 `μ^0(P)` 原子：

- 正常原子给 `<= W_Q log^{C_P}X`；
- 小 `μ^0(P)` 原子若总质量可求和，则由 LV/LSMP 吸收；若不可求和且偏差集中，则触发 SC/PI。

在当前非终端 Uniform 分支中，得到

`E_unif(Q,R) <= W_Q log^{C_U}X`。

## 5. 与大能量阈值比较

MLC 大能量阈值为 `X^{1+ε}` 级。若 Uniform 分支承载该量级，则必须有

`W_Q >= X^{1+ε}log^{-C_U}X`。

但 `W_Q` 是主层零频容量/有效权。若 `W_Q` 达到该量级，则对应允许 partition 中某个窗口的零频质量和实际质量同时很大；结合主层门槛 `W_Q^{1/2}`，PPI 反面阈值会被突破，转入可检测 PPI 分支。若未突破，则 `E_unif` 低于大能量阈值，不能解释 OV2 大 overlap。

因此 Uniform 不能作为独立大能量通道。

## 6. 主定理

**Theorem OV2-MLC-Uniform-Capacity-Constants（条件化）。** 在 AAI 主层正规形、固定复杂度 PPI partition、非 `FCT/SC/LV/LSMP/DSO-PI/CE` 假设下，MLC Uniform 零频背景满足

`E_unif(Q,R) <= W_Q log^{C_U}X`。

若 `E_unif(Q,R)` 达到 OV2 大 overlap 阈值 `X^{1+ε}`，则 PPI 可检测阈值被触发；否则 Uniform 低于阈值。故 Uniform 分支不能作为独立终端。

**证明。** 第 2 节给 partition 有限复杂度与零频有限重叠。第 3 节用 PPI 反面阈值控制所有不可检测误差平方和。第 4 节处理零频主项与小原子，得到 `W_Qlog^{C_U}X`。第 5 节把该界与大能量阈值比较：若足够大，则违反不可检测假设；若不大，则不能支撑 OV2 大 overlap。证毕。

## 7. 对容量矩阵的影响

本文把 `OV2/MLC Uniform` 零频容量从剩余硬点降为条件化常数化接口。剩余工作主要是全局 `log^C X` 常数层级排序，以及 PI dense/Carleson 与 DSO bridge 的适用条件无回流审查。
