# GEE-CE/LSMP 负担上界审查：吸收项、seed 转出与剩余接口

本文专攻 `GEE-CE` 与 `GEE-LSMP`。现有 `docs/rh-lv-lsmp-ce-maintext-absorption-chain.md` 已证明二者不是自由回流通道；但 GEE 需要定量出口上界：

`Load(CE;X)+Load(LSMP;X)=o(Δ)`。

因此必须把进入 CE/LSMP 的对象分成两类：真正可吸收项与 seed 转出项。只有前者能计入 `GEE-CE/LSMP` 的 `o(Δ)`；后者必须从 CE/LSMP 负担中删除，并转入 `A/PI/FCT/SC/DSO/NRC/LV` 等对应出口。

## 1. CE/LSMP 的正确 GEE 口径

`CE` 是复杂度逃逸分类器，`LSMP` 是小质量/薄层/coarea 吸收机制。它们不是最终结构终端。故定义：

- `Load_abs(CE/LSMP;X)`：已经满足固定阈值、可由平凡体积、coarea、小质量或平方可和尾项吸收的负担；
- `Seed(CE/LSMP;X)`：CE/LSMP 处理后输出的 `PI_seed/FCT_seed/SC/A/DSO/NRC/CapacityFail` 等结构种子。

GEE 出口上界只要求

`Load_abs(CE;X)+Load_abs(LSMP;X)=o(Δ)`。

`Seed` 部分不得继续计入 CE/LSMP，而必须转到对应 GEE 出口。

## 2. LSMP 可吸收项

LSMP 输入是一族有限重叠薄层或小质量原子 `B_a`，满足

`Σ_a μ(B_a) log^{C}X <= Δ/log^{B_LSMP}X`。

则平凡估计与 coarea 给

`Σ_a |Bias(B_a)| <= Δ/log^{B_final}X=o(Δ)`。

若上述小质量阈值失败，则 LSMP 主文链给二分：

1. 方向筛选/DPI 产生允许窗口偏差，转入 `PI`；
2. 频率原子进入祖先短深度 span，转入 `FCT`；
3. 若物理短窗或边界集中，则转入 `SC/LV`。

这些失败项不是 `Load_abs(LSMP)`。

## 3. CE 可吸收项

CE 四类逃逸的 GEE 处理如下：

| CE 类型 | 可吸收条件 | 失败转出 |
|---|---|---|
| 频率复杂度逃逸 | 独立新频率平方和由 DSO/NRC 控制且超额 `<=Δ/log^B` | `DSO/NRC/FCT/LSMP` |
| 尾项能量逃逸 | 尾项平方可和总量 `<=Δ/log^B` | `LSMP/PI/SC/LV` |
| 旧坐标重写逃逸 | 重写差集总量 `<=Δ/log^B` | `FCT/LV` |
| 边界体积逃逸 | 边界体积 `Vol_eff log^C<=Δ/log^B` | `LV/SC/LSMP` |

因此 CE 的可吸收负担是四类中满足阈值的部分；不满足阈值者必须绑定到命名出口，不留在 CE。

## 4. Theorem GEE-CE-LSMP-Split

**Theorem GEE-CE-LSMP-Split.** 假设：

1. CE/LSMP 的每个入口都按上表给出可吸收证书或 seed 转出标签；
2. 可吸收证书均满足相对异常阈值 `Mass_eff log^C X<=Δ/log^B X`；
3. seed 转出按 GEE-0 路由从 CE/LSMP 负担中删除并记入对应出口；

则

`Load_abs(CE;X)+Load_abs(LSMP;X)=o(Δ)`。

**证明。** 对可吸收项，用平凡质量、coarea 或平方可和尾项估计，每个入口贡献 `<=Δ/log^B X`；入口类型、dyadic 层、频率层和路由重叠仅损失固定对数幂，取 `B` 足够大即得 `o(Δ)`。对不满足阈值的项，假设 1 给出命名 seed，假设 3 将其从 CE/LSMP 删除。故 CE/LSMP 本身不能承载 `Δ` 级异常。证毕。

## 5. 当前剩余硬点

本文把 `GEE-CE/LSMP` 压缩为一个账本义务：

**Seed-Transfer Consistency.** 所有从 CE/LSMP 输出的 seed 必须在 GEE-0 的路由表中重新登记到唯一或有限重叠的目标出口，且不再重复计入 CE/LSMP。

若该一致性补齐，则 `GEE-CE/LSMP` 可标记为“吸收项闭合，seed 转出”。剩余压力转入 `GEE-FCT/GEE-SC/GEE-A` 以及已接收的 `PI/DSO/NRC/LV` 出口。

## 6. Seed-Transfer 已补齐

新增 `docs/rh-gee-seed-transfer-consistency.md`。CE/LSMP 输出 seed 的转出、去重和有限重叠继承已定理化；因此 CE/LSMP 可标记为“吸收项闭合，seed 转出一致性闭合”。
