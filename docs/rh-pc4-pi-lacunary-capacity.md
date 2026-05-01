# PC4-PI：Lacunary 容量上界

本文补齐 `docs/rh-pc4-pi-terminal-audit.md` 指出的最小剩余硬点 `PI-Lacunary-Capacity`。目标是证明：固定投影模板在强 lacunary 尺度包中只有有限重叠/Carleson 容量，不能无成本承载 PI-Seed 的发散能量；若 lacunary 分离失败，则转入 dense 包；若支撑集中或边界异常，则转入 SC/LV/CE。

## 1. Lacunary 包定义

令 `X_j` 为 PI-Seed 抽取的固定模板尺度。称子列 `𝓛` 为 `B`-lacunary，若

`X_{j_{m+1}} >= X_{j_m}^B`

其中 `B>1` 固定且足够大，吸收模板支撑宽度、平滑尾和 dyadic 边界常数。

固定模板 `𝓦_*` 在尺度 `X_j` 的窗口记为 `A_j`，零频质量为 `μ_j^0(A_j)`，能量为

`e_j=δ_j^2 μ_j^0(A_j)`。

## 2. Mellin 支撑有限重叠

把物理变量写为 `t=log n`。固定平滑窗口 `W(n/X_j)` 的 Mellin 支撑落在

`I_j=[log X_j-C_W, log X_j+C_W]`。

若 `X_{j_{m+1}}>=X_{j_m}^B` 且 `B` 足够大，则 `I_j` 两两相距趋于无穷，特别有限重叠数为 `1`。CRT/Bohr/倒数模板只改变每个 `I_j` 内的相对选择，不扩大 Mellin 支撑到相邻尺度。

因此

`Σ_{j∈𝓛} 1_{I_j}(t) <= C(𝓦_*)`。

## 3. Lacunary 容量上界

**Lemma PI-Lac-1（lacunary 零频容量）。** 对任意有限 `B`-lacunary 截断 `𝓛_N`，有

`Σ_{j∈𝓛_N} μ_j^0(A_j) <= C(𝓦_*) Cap(𝓛_N)`，

其中 `Cap(𝓛_N)` 是这些 disjoint Mellin 支撑的总零频容量。若采用每尺度归一化容量，则 `Cap(𝓛_N)≈#𝓛_N`；若采用全局包容量，则它等于 disjoint 支撑的总测度。

**证明。** 由第 2 节的有限重叠，固定模板的窗口指标在 Mellin 轴上的和逐点受 `C(𝓦_*)` 控制。对零频测度积分即得。证毕。

## 4. Lacunary 能量上界

单尺度归一化偏差 `δ_j` 若超过固定常数，则已经触发单尺度容量异常、短簇或高投影极端终端。因此在非终端假设下可取 `δ_j^2<=C(𝓦_*)`。

**Theorem PI-Lacunary-Capacity（lacunary 能量容量上界）。** 在非终端假设下，对任意有限 `B`-lacunary 截断 `𝓛_N`，

`Σ_{j∈𝓛_N} e_j <= C(𝓦_*) Cap(𝓛_N)`。

若该界失败，则触发 SC、LV、CE 或单尺度 PI 极端终端。

**证明。** 由 `e_j=δ_j^2 μ_j^0(A_j)` 与非终端下 `δ_j^2<=C`，得

`Σe_j<=CΣμ_j^0(A_j)`。

再用 PI-Lac-1。若 `δ_j` 无界或窗口支撑不满足固定模板有限重叠，分别是单尺度极端、短簇/低体积或复杂度逃逸。证毕。

## 5. 与 PI-Seed 的关系

PI-Lacunary-Capacity 本身给的是“容量上界”，不是单独矛盾。它在事件图中的作用是：若 PI-Seed 的发散能量全落在 lacunary 包，则必须伴随 `Cap(𝓛_N)` 同步发散；这不是额外异常，而是可由 disjoint 尺度容量解释。若 RH 反例需要在固定总容量包内产生发散能量，则 lacunary 上界给矛盾；若容量随尺度无限增长，则该部分不形成跨尺度同相位压缩，剩余同相位相干必须在 dense 包或终端分支中出现。

因此 PC4-PI 的闭合口径应为：

- lacunary 部分受容量账本控制，不产生新逃逸；
- 超容量 lacunary 失败转 SC/LV/CE/PI 极端；
- 真正的无限同相位压缩由 dense 正交或其他终端处理。
