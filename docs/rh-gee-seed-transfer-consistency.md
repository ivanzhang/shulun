# GEE Seed-Transfer Consistency：CE/LSMP 输出 seed 的转出与去重账本

本文补齐 `docs/rh-gee-ce-lsmp-load-bound-audit.md` 的剩余硬点：CE/LSMP 输出的 seed 必须从 CE/LSMP 负担中删除，并有限重叠地转入目标出口。目标是避免同一异常原子既作为 CE/LSMP 失败项又作为 PI/FCT/SC/A 等 seed 被重复计数。

## 1. seed 类型表

CE/LSMP 可能输出的 seed 及目标出口如下：

| seed 类型 | 来源 | 目标出口 |
|---|---|---|
| `PI_seed` | LSMP 方向筛选、尾项可检测、投影重复 | `PI` |
| `FCT_seed` | 频率原子落入祖先短深度 span、旧坐标闭包 | `FCT` |
| `SC_seed` | 短窗、端点或局部乘积集中 | `SC` |
| `A_seed` | 覆盖同步/正向过剩容量 | `A` |
| `DSO_seed` | 新增独立频率平方能量 | `DSO` |
| `NRC_seed` | 非共振倒数完成和入口 | `NRC` |
| `LV_seed` | 低体积边界/薄层 | `LV` |
| `CapacityFail` | 已绑定容量界被违反 | 对应容量出口或直接矛盾 |

该表没有新增出口，只是把 CE/LSMP 内部失败边落到既有 `𝓔={A,PI,FCT,SC,LV,LSMP,CE,DSO,NRC}`。

## 2. 转出账本定义

对每个原始异常原子 `a∈𝓐_X`，GEE-0 已有拆分权重 `θ_{a,E}`。若 `a` 先进入 CE/LSMP，但随后输出 seed 到目标 `T`，则执行替换：

`θ_{a,CE/LSMP}^{old} -> θ_{a,T}^{new}`，

并令

`θ_{a,CE/LSMP}^{new}=0`

除非该原子还有独立可吸收子质量。若 seed 只占原子的一部分，先把原子细分为 `a_abs ⊔ a_seed`，分别继承权重；细分层数只产生固定对数损失。

## 3. 有限重叠继承

CE/LSMP 的 seed 转出只使用已经存在的有限模板操作：dyadic 层、频率层、Vaaler 频率、maximal disjoint 薄层和短窗选择。它们均包含在 GEE-0 的路由常数表中。因此存在常数 `C_seed`，使

`Σ_E θ_{a,E}^{after seed} <= log^{C_route+C_seed}X`。

把 `C_seed` 吸收到原有 `C_route` 后，GEE-0 下界保持 `X^{β-o(1)}` 级，不改变总矛盾结构。

## 4. Theorem Seed-Transfer Consistency

**Theorem Seed-Transfer Consistency.** 假设 CE/LSMP 的每个失败项均按第 1 节 seed 表给出目标出口，且 seed 生成只使用固定复杂度路由操作。则可以重定义 GEE 负担，使：

1. 可吸收 CE/LSMP 项仍计入 `Load_abs(CE/LSMP;X)`；
2. seed 项不再计入 `CE/LSMP`；
3. seed 项有限重叠地计入对应目标出口；
4. 总路由重叠仍为 `log^{C}X`；
5. GEE-0 的负担下界不变为

   `Σ_E Load(E;X)>=X^{β-o(1)}`。

**证明。** 对每个进入 CE/LSMP 的原子按吸收/seed 二分。吸收部分保留在 `Load_abs`。seed 部分按第 1 节确定目标出口，并把原 CE/LSMP 权重转移到该出口。由于转出操作只是原路由树的细分和重标记，不增加新的数学分支；细分次数由 dyadic、频率和薄层层数控制，为多对数。故总拆分权重仍受 `log^C X` 控制。每个原始异常偏差仍被某个出口接收，因此 GEE-0 下界保持。证毕。

## 5. 对 CE/LSMP 的闭合影响

结合 `docs/rh-gee-ce-lsmp-load-bound-audit.md`：

- 可吸收项给 `Load_abs(CE)+Load_abs(LSMP)=o(Δ)`；
- seed 项由本文转入 `A/PI/FCT/SC/LV/DSO/NRC`；
- 不存在同一 seed 在 CE/LSMP 与目标出口中重复计数。

因此 `GEE-CE/LSMP` 可以标记为：**吸收项闭合，seed 转出一致性闭合**。剩余真正出口压力集中到 `GEE-FCT/GEE-SC/GEE-A` 以及已接收 seed 的目标出口上界。
