# PC4-PI-Cap：固定投影模板的跨尺度 Carleson 容量上界

本文专攻 `docs/rh-pc4-pi-seed.md` 留下的真正硬点 `PI-Cap`。直接断言

`Σ_j Energy_j(𝓦_*)<∞`

过强，因为尺度可以无限增长且每个尺度都有新的质量。更可证的版本应是 Carleson 包上界：对任意 disjoint multiplicative 尺度包，固定投影模板的归一化能量总量受该包的零频容量控制。若离线零点驱动的增量在这些包内给出超容量下界，则矛盾。

## 1. 固定模板与尺度包

固定一个投影模板 `𝓦_*`，它由同一有限布尔表达式、同一相对 dyadic 层、同一频率阶数和同一窗口类型组成。对每个尺度 `X_j`，令 `A_j∈𝓦_*` 是该模板在尺度 `X_j` 的自然缩放。

取 multiplicative 尺度包

`𝓘=[Y, Y^B]`

或更一般的 disjoint 包族 `𝓘_m=[Y_m,Y_m^B]`，满足 `Y_{m+1}>Y_m^B`。包内能量定义为

`E_{𝓦_*}(𝓘)=Σ_{X_j∈𝓘} δ_j^2 μ_j^0(A_j)`。

## 2. Carleson 容量形式

**Conjectural Lemma PI-Cap（全局容量形式，待证）。** 对固定模板 `𝓦_*`，存在常数 `C(𝓦_*)`，使任意 disjoint 尺度包族满足

`Σ_m E_{𝓦_*}(𝓘_m) <= C(𝓦_*) Σ_m Cap(𝓘_m)`。

其中 `Cap(𝓘_m)` 是该包内零频可用容量；在归一化能量账本中应为 `O(1)` 或至多 `log^C Y_m`。

这一定理若成立，将与 PI-Seed 的发散种子冲突。

## 3. 可证弱版：有限包能量上界

**Lemma PIC-1（有限包平凡 Carleson 上界）。** 对任意有限尺度包 `𝓘`，有

`E_{𝓦_*}(𝓘) <= Σ_{X_j∈𝓘} μ_j^0(A_j)`。

**证明。** 高投影增量的相对密度增幅 `δ_j` 在 D 组归一化中小于绝对常数；否则单尺度已触发极端短簇或容量矛盾。故 `δ_j^2<=C`，吸收常数后得到结论。证毕。

该弱版本身不足以排斥 RH，因为右侧可能随尺度数发散；但它说明真正需要的是零频容量的跨尺度重叠控制。

## 4. 可证弱版：lacunary 子列容量上界

若尺度强 lacunary，例如 `X_{j+1}>=X_j^B`，固定模板窗口在整数轴或 Mellin 轴上近似 disjoint。

**Lemma PIC-2（lacunary disjoint 包上界）。** 对强 lacunary 子列和任意有限包截断 `J`，固定模板的零频质量满足

`Σ_{j in J} μ_j^0(A_j; normalized) <= C(𝓦_*) Cap(J)`,

其中 `Cap(J)` 是这些 disjoint Mellin 支撑的总归一化长度。若采用每尺度单位归一化，则 `Cap(J)≈#J`；若采用全局 Mellin 包归一化，则 `Cap(J)` 为包总长度。

**证明框架。** 将每个 `A_j` 拉回到 Mellin 变量 `t=log n`。强 lacunary 使支撑区间近似 disjoint；固定模板保证每个点最多落入有界个拉回窗口。于是由有限重叠得到包容量上界。证毕。

这给出一个真实但较弱的结论：lacunary 本身只提供无重叠容量控制；要与 PI-Seed 矛盾，还需要离线零点下界超过相同包容量，或引入额外正交归一化。

## 5. 中等密度尺度的障碍

离线零点相位 `γlogX` 允许在相对密集的 `logX` 序列中反复落入同一相位弧。此时窗口支撑不 disjoint，PIC-2 只给平凡包容量，不给平方根级正交。需要新的正交机制：

1. **Mellin 频率正交**：不同 `X_j` 的平滑窗口在 Mellin 频率上形成近正交波包；
2. **CRT 模数增长正交**：不同 `z_j` 的 primorial CRT 系统细化，非零类基线形成 martingale 差；
3. **Euler product 因子正交**：新增素因子层提供独立局部坐标，固定模板不能长期同向偏置所有新增层。

这三种机制是 PI-Cap 的真正候选证明路线。

## 6. PI-Cap 可攻命题

**Proposition PIC-Route（PI-Cap 分解）。** 要证明 PC4-PI，只需证明以下二者之一：

1. **Lacunary super-capacity**：离线零点导致的高投影增量可抽取强 lacunary 子列，且 PI-Seed 下界超过 PIC-2 的包容量上界。
2. **Dense-scale orthogonality**：若不能抽取强 lacunary 超容量子列，则密集尺度包内的固定模板投影满足 Mellin/CRT martingale 正交上界

   `Σ_{X_j in 𝓘} δ_j^2 μ_j^0(A_j) <= C(𝓦_*) Cap(𝓘)`，

   且该上界强到低于离线零点给出的同包下界。

**证明。** 任意无穷子列按 `log log X` 间距分成强 lacunary 部分与密集包部分。若可在 lacunary 部分证明超容量下界，则用 PIC-2；否则所有可能矛盾必须来自密集包，需 Dense-scale orthogonality。证毕。

## 7. 当前闭合状态

PI-Cap 尚未完全证明，但已经从模糊的“全局容量界”压缩成两个具体攻坚点：

- 强 lacunary 包容量上界：可由 disjoint 支撑证明，但还需超容量下界才能矛盾；
- 密集尺度包正交：需要 Mellin/CRT martingale 或 Euler product 新输入。

Dense-scale orthogonality 已从 `docs/rh-pc4-dense-scale-orthogonality.md` 的 DSO-M/DSO-C/DSO-E 接口推进到 `docs/rh-pc4-pi-dense-closure-theorem.md` 的 PC4-PI-Dense 闭合命题。下一步最优专攻是把 lacunary 分包与 dense 闭合合并为 PC4-PI-Closure。


## 8. Lacunary 容量定理入口

强 lacunary 分包的 Mellin 有限重叠、Carleson 容量上界和失败分支见 `docs/rh-pc4-pi-lacunary-capacity.md`。
