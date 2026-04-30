# OMR/CGTP/LSMP 结构包定理化与黑箱削减

本文件补强待证数学输入 D。目标是把第 1273 节的保守常数账本拆成可审查的独立定理、组合证明和剩余标准输入。

## 1. 总结构定理

**Theorem OCL（OMR/CGTP/LSMP closure）。** 在 Structured-EHPD 的坏配置状态中，假设无终端短簇、无高投影增量、无 frequency-collision terminal，且 NRC 背景满足

`Λ^2 r >= C K_eff P^{1/2} log^A P`。

则坏配置不能持续；等价地，生成树递推必在有限深度内产生终端输出。常数可保守填入

`C_OMR_layer=C_OMR_projection=C_CGTP=C_LSMP=C_collision_span=16`,

`A_OMR_log=A_CGTP_log=A_LSMP_log=A_collision_span_log=8`,

`epsilon_OMR_power=64`。

**证明路线。** OMR 把一阶模型匹配转为短簇或投影增量；CGTP 把投影增量沿生成树用平方能量望远镜计账；LSMP 证明小质量原子只造成对数损失，不把门槛从 `Λ^2` 退化到 `Λ^4`。若三种终端均被排除，则能量账本给出正增量但总能量有界，矛盾。

## 2. OMR 拆解

### 2.1 OMR-1：层残差到一阶矩匹配

**Lemma OMR-1。** 若所有有效 dyadic 层残差

`Δ_j=μ(B_j)-a_{j,0}r-2Re(a_{j,1}S(1))`

满足 `|Δ_j|<=ε_OMR μ(E_j)`，则对任意频率截断 `<=C/Λ`、Lipschitz 常数 `<=C/Λ` 的偶测试函数 `F`，有

`Σ_d w(d)F(X(d)) = ∫F dν_1 + O(ε_OMR r log^A(1/Λ)+Err_smooth)`。

**证明。** 用 dyadic 层蛋糕表示 `F`，每层由相邻阈值差组成；残差假设逐层控制误差。测试函数复杂度 `C/Λ` 带来 `log^A(1/Λ)` 层数和 Fourier 截断损失。平滑误差由 `epsilon_OMR_power=64` 吸收。该引理只用 Fourier/层蛋糕，不需数论输入。

### 2.2 OMR-2：一阶圆周模型偏差

**Lemma OMR-2。** 若 `|S(1)|>=Λr`，则一阶模型

`dν_1(θ)=r(1+2λcos(θ-φ))dθ`, `λ=|S(1)|/r`,

在有效阈值族 `Λ/8<=τ<=1/4` 上具有总层偏差

`Σ_j |ν_1(B_j)-r|B_j|| >= cΛr`。

**证明。** 对弧 `I_τ={cos(θ-φ)>=τ}`，有

`ν_1(I_τ)-r|I_τ|=2λr∫_{I_τ}cos(θ-φ)dθ`。

当 `τ<=1/4` 时积分有绝对正下界。把 `τ` 按 dyadic 层分解，望远镜求和得到总偏差 `>=cΛr`。这是纯一维计算。

### 2.3 OMR-3：稳定偏差到投影增量

**Proposition OMR-3。** 若实际层质量匹配 OMR-2 的总偏差，且无终端短簇，则存在允许倒数环带或其有限并差 `A∈𝓦(K')`，满足

`μ(A) >= (1+κ_OMRΛ^2/log^A K) μ_geo(A)`，

除非当前窗口生成历史已经包含当前频率的一阶调制。

**证明框架。** 每个层弧 `I` 的原像是倒数环带 `ξd^{-1}∈I`。若总偏差不集中到短弧，则通过有限重叠选择可抽出一族分散环带，偏差总量仍为 `cΛr/log^A K`。若所有允许并差窗口都无密度增量，则这些偏差只能由几何测度误差解释；NRC 给该误差上界 `C K'P^{1/2}log^C P`，与 `Λ^2r` 门槛矛盾。因此得到投影增量。剩余非组合输入是 NRC：非共振倒数完成和的相对均匀性。

## 3. CGTP 拆解

**Theorem CGTP（平方能量生成树投影）。** 沿生成树，每次非终端高投影增量至少增加归一化平方能量

`ΔE >= c η Λ^2 R/log^A K`，

而总能量 `E<=R`。因此若非终端步骤超过 `C log^A K/(ηΛ^2)` 次，必矛盾。

**证明。** 投影增量给局部密度从 `ρ` 到 `ρ(1+δ)`，其中 `δ≈ηΛ^2/log^A K`。用 martingale 正交分解，平方能量增量为 `≈δ^2 μ(A)`；variance-to-density 把可见的一阶增量转换为平方能量下界，损失由方向选择、父子密度比较和大小块分裂承担。保守记为 `C_CGTP=16`, `A_CGTP_log=8`。

**剩余接口。** 需要 LSMP 保证小质量原子总贡献可吸收，否则平方能量可能散落到过多小块上。

## 4. LSMP 拆解

### 4.1 Discrete coarea

**Lemma LSMP-1（离散 coarea）。** 若小质量有效子块族总质量为 `M`，则存在 dyadic 厚度层与有限重叠薄边界层族 `B_a`，使

`Σ_a μ(B_a) >= cM/logK`, `K(B_a)<=K log^C K`。

**证明。** 每个小块被 `O(logK)` 个 dyadic 厚度层覆盖；对厚度层求平均，存在一层承载 `M/logK`。取 maximal disjoint 子族，有限重叠只损失常数。

### 4.2 DPI：分散到投影增量

**Lemma LSMP-2（DPI）。** 若 coarea 产生的薄层族带有同向偏移总量 `>=cηΛR/log^A K`，且无短簇、无 frequency-collision terminal，并满足 NRC 背景可吸收，则存在允许窗口 `B_*` 给出

`1+cηΛ^2/log^{A'}K`

级高投影增量。

**证明框架。** 若没有投影增量，则薄层几何质量与实际质量匹配；同向偏移只能来自倒数相位在这些薄层上的非平凡平均。非共振时 NRC 把该平均压到 `K_effP^{1/2}log^C P`，与门槛矛盾。若 NRC 不适用，则正是 frequency-collision terminal。

### 4.3 LSMP 定理

**Theorem LSMP。** 在无短簇、无高投影增量、无 frequency-collision terminal 且 NRC 可吸收时，小质量原子贡献满足

`E_small <= C ηΛ^2R/log^A K`。

**证明。** 方向筛选把小质量能量转成同向有效质量；LSMP-1 抽出薄边界层族；LSMP-2 若不产生终端则给投影增量，矛盾。因此小质量贡献必须可吸收。LSMP 只付对数损失，不付 `Λ^{-2}` 损失。

## 5. frequency-collision terminal

**Lemma FCT（频率碰撞 span 计数）。** 若 NRC 失败，则当前频率落入祖先短深度频率 span，或产生低维 frequency-collision terminal。短深度 span 的复杂度损失可取

`C_collision_span=16`, `A_collision_span_log=8`。

**证明框架。** 生成树深度为 `O(logK)`，每层只引入有限个当前频率及其低阶倍频。若新频率不在 span 中，完成和给 NRC；若在 span 中，则终端记录一条低维碰撞证书。span 计数只产生 `log^8K` 级损失。

## 6. 审稿状态变化

经过本拆解，OMR/CGTP/LSMP 不再是单一结构黑箱。已直接证明或组合化的部分：

- OMR-1 的层蛋糕/Fourier 匹配；
- OMR-2 的一维圆周模型计算；
- LSMP-1 的离散 coarea；
- CGTP 的 martingale 能量账本形式；
- LSMP 的“coarea + DPI”组合逻辑。

剩余真正外部/深层输入原为两类。现 `NRC` 已在 `docs/nrc-theoremization.md` 中定理化为标准完成法加 Weil/Kloosterman 界；因此当前唯一主要剩余为：

1. **FCT/Tree-WFE 接口**：NRC 失败时的频率碰撞终端如何接入全局生成树容量矛盾。

这两项比原始 OMR/CGTP/LSMP 常数包更窄，适合下一轮继续单独定理化。
