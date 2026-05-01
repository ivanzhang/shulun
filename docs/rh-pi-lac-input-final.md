# PI-Lac 输入最终化：lacunary 投影容量界

本文把 `docs/rh-pc4-pi-lacunary-capacity.md` 迁入 AEX-1 的正式输入 `PI-Lac`。目标是证明：强 lacunary 尺度包的投影能量只能由其互不重叠的零频容量支付，不能形成额外的 `Load(PI)`。

## 1. 命题

**Theorem PI-Lac.** 设 `𝓛` 是固定模板 `𝓦_*` 的强 lacunary 尺度包，窗口为 `A_j`，零频容量为 `Cap_j^0`，超额能量余量为 `R_j`。在非终端假设下，即没有 `CE/LSMP/LV/SC/FCT/NRC` 失败事件，任意有限截断满足

`Σ_{j∈𝓛_N} R_j <= C(𝓦_*) Σ_{j∈𝓛_N} Cap_j^0`。

扣除零频容量后，lacunary 包对 AEX-1 的异常负担为零；若出现超过该容量界的同向超额，则触发 `SC/LV/CE` 或单尺度 PI 极端终端。

## 2. 证明

把物理变量写为 `t=log n`。固定平滑窗口 `W(n/X_j)` 的 Mellin 支撑包含在

`I_j=[log X_j-C_W,log X_j+C_W]`。

强 lacunary 条件 `X_{j_{m+1}}>=X_{j_m}^B` 且 `B` 足够大，保证这些区间有限重叠：

`Σ_j 1_{I_j}(t)<=C(𝓦_*)`。

CRT、Bohr、倒数相位等固定模板只在每个 `I_j` 内选择子结构，不把支撑扩展到相邻尺度。因此对零频测度积分得

`Σ_j Cap_j^0 <= C(𝓦_*) Cap_lac(𝓛_N)`。

在非终端假设下，单尺度归一化偏差有固定上界；否则即为单尺度 PI 极端、短簇、低体积或复杂度逃逸。因此

`R_j <= C(𝓦_*) Cap_j^0`。

求和即得命题。若该界失败，则必是固定模板、有限重叠或单尺度偏差上界之一失败，分别进入 `CE/LSMP/LV/SC` 或单尺度 PI 极端终端。证毕。

## 3. 对 AEX-1 的影响

AEX-1 中 lacunary 部分已完成：它不是独立异常负担，而是零频容量账本的正常支出。由 Baseline-Subtraction，零频容量不计入 `Load(PI)`；超容量失败进入命名出口并由 Transfer-Accounting 源删除。

因此 `PI-Lac` 可在最终剩余输入表中勾选完成。AEX-1 剩余只剩 `PI-Dense`。
