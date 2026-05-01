# PC4-PI 终端输入审查：固定模板能量上界

本文按 `docs/rh-pc4-terminal-closure-audit.md` 的排序，先审查 PC4-PI。目标是把高投影增量 closure 改写为事件图输入：PI-Seed 给能量下界；dense 包由正交输入最终审查支撑；lacunary 包仍是 PC4-PI 中最小剩余硬点。

## 1. PI 事件输入

单尺度高投影增量给窗口 `A_j` 与偏差 `δ_j`，能量项为

`e_j=δ_j^2 μ_j^0(A_j)`。

若 PI 作为最终逃逸通道，由 `docs/rh-pc4-pi-seed.md`，排除 CE/LSMP/LV/FCT/SC 后，可抽取固定模板 `𝓦_*` 与同相位无穷子列，使

`Σ_j e_j=∞`。

这就是 PI 事件图中的 `PI_seed`。

## 2. Dense 包状态

Dense 包依赖正交输入。当前状态：已由第 4 项最终合并审查支撑。

入口：

- `docs/rh-pc4-pi-dense-closure-theorem.md`；
- `docs/rh-pc4-orthogonality-final-closure-audit.md`。

结论：若 dense 包容量界失败，则不形成新逃逸，而是转入 PI-Seed、FCT、LSMP、LV、NRC 或 CE 事件。因此 dense 包可在事件图中视为已归约。

## 3. Lacunary 包状态

Lacunary 包来自尺度中心充分分离。`docs/rh-pc4-pi-cap-carleson.md` 已指出几何/Carleson 容量上界方向，但仍需要最终严写：

`Σ_{j in lacunary} e_j <= C(𝓦_*) Cap_lac`。

还需说明 PI-Seed 的离线零点下界若无限发生，必无法全部躲进容量有限的 lacunary 包；否则必须抽取 dense 包或触发终端。

该硬点已写入 `docs/rh-pc4-pi-lacunary-capacity.md`。其结论是 lacunary 部分受 disjoint Mellin/Carleson 容量控制；若超容量失败则转入 SC/LV/CE/单尺度 PI 极端。

## 4. PI 事件图归约

**Proposition PI-Terminal-Reduction（PI 终端输入归约）。** 假设：

1. PI-Seed 的固定模板能量下界成立；
2. dense 包由 `PC4-PI-Dense` 与正交输入最终审查归约；
3. lacunary 包满足 `docs/rh-pc4-pi-lacunary-capacity.md` 的 PI-Lacunary-Capacity；
4. CE/LSMP/LV/FCT/SC/NRC 作为事件图终端处理。

则 PI 不能作为最终逃逸通道。

**证明。** 反设 PI 最终逃逸。PI-Seed 给固定模板发散能量。按 PI-Cap 分成 lacunary 与 dense。Dense 包若承载发散能量，则由正交输入审查转入事件图终端或容量上界矛盾。Lacunary 包若承载发散能量，则违反 PI-Lacunary-Capacity。若两者都不承载发散能量，则与 PI-Seed 矛盾。证毕。

## 5. 下一步硬点

PI-Lacunary-Capacity 已补入 `docs/rh-pc4-pi-lacunary-capacity.md`。PI-Seed、dense 正交与 lacunary 容量三者的无循环事件图合并见 `docs/rh-pc4-pi-terminal-final-reduction.md`。下一步按 PC4 终端排序继续审查 FCT/SC/A 的剩余输入。
