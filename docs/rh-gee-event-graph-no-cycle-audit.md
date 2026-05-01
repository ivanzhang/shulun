# GEE 事件图无循环总审查

本文补 `docs/rh-gee-global-synthesis-audit.md` 的第一项剩余义务：把九个出口与 seed 转出边统一成有向事件图，并检查每个潜在有向环是否带有严格下降量、容量消耗或基线扣除。结论：在当前文档定义的“内部转移 + seed 转出 + 超额 Load”口径下，事件图不存在自由循环；但最终论文仍需把这些边内联为一张主图。

## 1. 节点与边

节点集合：

`𝓔={A,PI,FCT,SC,LV,LSMP,CE,DSO,NRC}`。

吸收节点：

- `LV_abs`：相对低体积 `o(Δ)`；
- `LSMP_abs/CE_abs`：小质量、coarea、平方可和、复杂度可吸收项；
- `NRC_abs`：非共振完成和相对小；
- `PI/DSO_abs`：扣除零频容量后的超额偏差 `o(Δ)`。

内部转移节点：

- `A_int`：ACC 同步势函数下降；
- `FCT_int`：Noether 势函数下降；
- `SC_int`：短簇势函数下降。

转出边：

| 来源 | 目标 | 边类型 | 严格控制量 |
|---|---|---|---|
| `A` | `PI/FCT/SC/LV/LSMP/DSO/CE` | 固定 ACC 模板重复 | ACC 势函数下降或转出 |
| `FCT` | `NRC/DSO/PI/SC/LV/LSMP/CE` | 重复闭包或独立频率 | Noether 势函数下降或转出 |
| `SC` | `A/PI/FCT/LV/LSMP/CE` | 重复短簇模板 | 短簇势函数下降或转出 |
| `CE/LSMP` | `A/PI/FCT/SC/LV/DSO/NRC` | seed 转出 | Seed-Transfer 去重 |
| `NRC-2D` | `LSMP/LV/SC/PI/DSO/CE` | MidCap 分流 | PPI-Rank/Capacity 分流 |
| `PI/DSO` | `SC/LV/LSMP/CE/FCT/NRC` | 适用条件失败 | NoReturn + Baseline-Subtraction |

## 2. 自环排除

- `A -> A`：只有真 ACC 同步变化才可留在 A；每次使 `𝓐pot` 下降。固定模板不降时转出。
- `FCT -> FCT`：只有真闭包步可留在 FCT；每次使 Noether 势函数 `𝓝` 下降。重复闭包转出。
- `SC -> SC`：只有真 `shorter_SC` 可留在 SC；每次使短簇势函数 `𝓥` 下降。重复短簇转出。
- `PI/DSO -> PI/DSO`：dense/lacunary 包只登记超额偏差；零频容量被扣除，重复投影能量由 Carleson/square-function 消耗。
- `CE/LSMP -> CE/LSMP`：CE/LSMP 不保留 seed，自身只保留可吸收项；因此无自环。
- `LV -> LV`、`NRC -> NRC`：分别为吸收或非共振估计；失败转出，不自环。

## 3. 混合环排除

任一混合环必须经过 `A/FCT/SC` 中至少一个内部转移节点，或经过 `PI/DSO` 容量节点，或经过 `CE/LSMP` seed 分类节点。

1. 若环中包含 `A` 且返回 `A`，则两次访问之间若无 ACC 势函数下降，第一次固定模板重复已转出为 `PI/FCT/SC/...`，不能作为同一 A 状态继续；若有下降，有限次后终止。
2. 若环中包含 `FCT` 且返回 `FCT`，同理 Noether 势函数下降；无下降则重复闭包已转出。
3. 若环中包含 `SC` 且返回 `SC`，同理短簇势函数下降；无下降则重复短簇已转出。
4. 若环只在 `PI/DSO/CE/LSMP/LV/NRC` 中循环，则 `CE/LSMP` 的 seed 转出会删除原负担；`PI/DSO` 只记录超额容量；`LV/NRC` 是吸收或转出节点。因此没有保持同一正负担的闭环。

三个离散势函数和一个容量超额账本共同构成 Lyapunov 向量：

`𝓛=(𝓐pot,𝓝,𝓥,ExcessCap,ComplexityRank)`。

沿任何非吸收、非转出路径，`𝓛` 按字典序下降或某个容量超额被扣除。由于各分量非负或有下界，并且复杂度固定，不能存在无限自由循环。

## 4. Theorem GEE-Event-No-Cycle

**Theorem.** 在 Seed-Transfer、Baseline-Subtraction、A/FCT/SC 三个势函数账本、PI/DSO Carleson 容量、LV/LSMP/CE 吸收阈值与 NRC 非共振上界均成立的假设下，GEE 事件图不存在承载正 `Load` 的无限有向循环。

**证明。** 自环由第 2 节排除。混合环由第 3 节的 Lyapunov 向量排除：若某内部节点反复出现，则对应势函数严格下降；若不下降，则该节点按定义转出，不再保持原边。若路径避开内部节点，则只剩吸收、基线扣除或 seed 分类节点，它们不能保持同一正 `Load` 回流。故无限正负担循环不存在。证毕。

## 5. 审稿备注

本文闭合的是事件图层面的自由循环问题。它不替代阈值常数表，也不替代单篇论文内联。下一步必须统一所有 `log^C X` 损失，确保每个吸收阈值都能取到 `Δ/log^B X` 余量。
