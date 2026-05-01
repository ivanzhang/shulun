# OV2-MLC：不可检测均匀质量吸收定理

本文补齐 `docs/rh-ov2-mlc-unconditional-core.md` 中留下的 MLC 最后硬点：主层 overlap 质量若对 PPI 的所有允许窗口都不可检测，为什么它不能仍然承载 `E_ov>X^{1+ε}` 级异常。结论是：不可检测质量只有四个出口——FCT、短簇/LV、DSO/PI、零频均匀背景；排除前三者后，第四者受容量界控制，不能形成大能量。

Uniform 零频容量的常数化审查见 `docs/rh-ov2-mlc-uniform-capacity-constants-audit.md`。

## 1. 不可检测质量定义

固定主层 `Q,R`。令 `μ_{Q,R}` 为该层 overlap 推送到 PPI 相位空间后的测度，`μ_{Q,R}^0` 为零频基线。称该层对 PPI 不可检测，若对所有允许窗口 `A∈𝓦(K')`，均有

`|μ_{Q,R}(A)-μ_{Q,R}^0(A)| < τ_{Q,R}`，

其中 `τ_{Q,R}` 是 PPI 可触发 D 组终端的阈值。

## 2. 不可检测四分

不可检测并不意味着没有结构。按 `docs/rh-ov2-ppi-unconditional-theorem.md`，窗口偏差的 Fourier 展开落入三类：非共振频率、FCT 共振频率、复杂度/截断尾项。再加上物理空间集中，得到四分：

1. **FCT**：频率落入祖先短深度 span；
2. **SC/LV**：质量集中在短窗、少数尾因子或低体积盒；
3. **DSO/PI**：非共振频率分散但有平方能量；
4. **Uniform**：所有可检测频率与物理局部盒都接近零频。

前三者是已列终端或接口；本文只需证明第 4 类不能承载大能量。

## 3. 均匀背景容量界

本节的常数化版本见 `docs/rh-ov2-mlc-uniform-capacity-constants-audit.md`。

若属于 Uniform 类，则对固定复杂度相位 partition `𝓟` 的每个原子 `P` 有

`μ_{Q,R}(P)=μ_{Q,R}^0(P)+O(τ_{Q,R})`。

令总零频容量为 `W_Q`。有限重叠给

`Σ_{P∈𝓟} μ_{Q,R}^0(P) <= W_Q log^C X`。

于是均匀部分的平方能量满足

`E_{unif}(Q,R) <= W_Q log^C X + |𝓟|τ_{Q,R}^2`。

取 `τ_{Q,R}` 为 PPI 阈值的反面，并把 `|𝓟|` 的固定复杂度损失并入 `log^C X`，得到

`E_{unif}(Q,R) <= W_Q log^C X`。

在 MLC 主层门槛中，若此量超过 `X^{1+ε}`，则 `W_Q` 本身过大并产生 PPI 可检测偏差；否则它低于大能量阈值。

## 4. DSO/PI 分散能量吸收

若不可检测质量不在 Uniform 类，而是在许多新增 CRT 坐标上产生分散非主频率平方能量，则由 `docs/rh-pc4-dso-crt-martingale.md` 的 martingale square-function 与 `docs/rh-pc4-dso-template-consistency.md` 的固定模板一致性控制。若平方能量超过 DSO 容量，就进入 `docs/rh-pc4-pi-closure-theorem.md` 的高投影增量分支；若模板复杂度逃逸，则进入 `docs/rh-pc4-complexity-escape-interface.md`。

因此分散正交能量不是新的 MLC 终端。

## 5. MLC 均匀吸收主定理

**Theorem MLC-Uniform-Absorption（不可检测均匀质量吸收，条件化到已列接口）。** 假设 AAI、PPI 无条件核心、MLC 容量核心、LV/LSMP、FCT 与 DSO/PI 接口均可用。若某主层 overlap 质量对所有 PPI 允许窗口不可检测，则至少发生一项：

1. 频率落入低维 span，触发 FCT；
2. 质量集中在短窗、少数尾因子或低体积盒，触发 SC 或 LV/LSMP；
3. 分散非主频率平方能量超过容量，触发 PI 或 CE；
4. 剩余为零频均匀背景，满足

   `E_{unif}(Q,R)<=X^{1+ε}/log^B X`

   对足够大的对数余量 `B` 成立。

**证明。** 由 PPI Fourier 三分，将不可检测质量拆成共振频率、非共振频率、尾项与零频背景。共振频率给 FCT。尾项或物理集中给 SC/LV/LSMP。非共振分散频率由 DSO square-function 控制；若控制失败即 PI/CE。剩余项在每个固定复杂度 partition 原子上与零频相差低于阈值，按第 3 节容量估计得到零频均匀背景上界。证毕。

## 6. 对 OV2 的影响

结合 `docs/rh-ov2-mlc-unconditional-core.md`，MLC 现在形成完整链条：

`大 overlap -> dyadic 主层定位 -> PPI 可检测 或 不可检测`

可检测由 PPI/NRC/FCT/PI 处理；不可检测由本文转入 FCT、SC/LV、PI/CE 或零频均匀背景。故 MLC 不再保留独立黑箱，只剩它依赖的 FCT、LV/LSMP、DSO/PI 等全局接口需要继续无条件化。
