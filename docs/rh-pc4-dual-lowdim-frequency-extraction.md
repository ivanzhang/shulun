# PC4-Dual：DGap 低维频率抽取接口

本文补强 `docs/rh-pc4-dual-projection-orthogonalization.md` 的最后剩余接口：若 `DGap` 的盒空间能量没有进入 PC4-PI 的可检测投影族，也没有落入短簇、低体积或误差逃逸，则它必须由固定低维 CRT/Bohr 频率 span 吸收，从而进入 PC4-FCT。

## 1. 输入：PI 不可检测的盒能量

设 `h=g_z^0-g_z`，盒空间投影满足

`||P_V h||_2^2 >= X^{2β-1-o(1)}`，`β>1/2`。

由 `docs/rh-pc4-dual-projection-orthogonalization.md`，若 PC4-PI 没有被触发，则 `P_V h` 的主要能量不在允许投影族 `V_PI`。排除 SC、LV/LSMP 与误差逃逸后，剩余部分记为

`u=P_{res}h`。

`u` 属于固定复杂度 CRT/Bohr 模板族的闭包，但对所有允许高投影窗口均不可检测。

## 2. 频率截断与谱支撑

固定复杂度盒函数由有限个倒数环带、短弧、Bohr 切片和 dyadic 标签生成。按 Vaaler/Fourier 截断，可把 `u` 写成

`u=u_{<=H}+u_{tail}`，

其中 `u_{<=H}` 是有限频率组合，`u_{tail}` 平方可和或进入 Complexity-Escape/LSMP。排除尾项逃逸后，能量主要在 `u_{<=H}`。

设 `Spec(u)` 是非平凡 CRT 字符频率集合。若 `Spec(u)` 在无穷尺度上产生无界新独立频率，则这些新增频率按 DSO-C/DSO-E 正交给出 PC4-PI 能量，矛盾。因此在非 PI 假设下，必须存在固定维数 `d=O(1)` 与固定整数关系模板，使主要谱支撑落在

`Λ_* = span_Z{λ_1,...,λ_d}`。

## 3. 低维抽取引理

**Lemma LFE-1（非 PI 能量的低维谱抽取）。** 在固定复杂度模板、平方可和尾项、无 PC4-PI 的假设下，若 `||u||_2^2` 在无穷多尺度上保持 `X^{2β-1-o(1)}` 级别，则存在无穷子列与固定低维频率族 `Λ_*`，使

`||P_{Λ_*}u||_2^2 >= c||u||_2^2`。

**证明。** 对每个尺度作有限 Fourier 截断。若没有固定低维族承载固定比例能量，则可抽取无穷多个彼此独立的新增频率包。由 CRT 新增坐标正交与 `docs/rh-pc4-dso-crt-martingale.md` 的 square-function，上述独立频率包的平方和必须进入 PC4-PI 或被 DSO 容量吸收，不能长期承载离线零点级能量。故存在固定低维主谱。证毕。

## 4. 从低维谱到 FCT 证书

低维谱支撑 `Λ_*` 表示：DGap 压缩异常主要由有限个 CRT 字符、倒数相位或 Bohr 短弧共同决定。于是每个成功尺度上存在固定短弧 `I_*`，使

`phase(Λ_*(X)) - γlogX ∈ I_*`

承载同向异常。该陈述正是 `docs/rh-pc4-fct-seed.md` 的固定低维编码输入。

若新增 CRT 坐标推进后 `Λ_*` 仍持续命中同一短弧，则 `docs/rh-pc4-fct-phase-drift.md` 给出漂移压力：零频命中不足、平方能量转 PI/短簇，或生成新的 FCT 闭包证书。后者由 `docs/rh-pc4-fct-closure-theorem.md` 处理。

## 5. LFE 主命题

**Theorem DGap-LowDim-Frequency-Extraction（DGap 低维频率抽取，条件化）。** 假设：

1. `DGap-Projection-Orthogonalization` 已把分散盒质量转为盒空间能量；
2. 固定复杂度模板的 Fourier/Vaaler 尾项平方可和，或尾项逃逸进入 CE/LSMP；
3. PC4-PI、SC、LV/LSMP 与边界误差不作为当前终端。

若盒空间能量不能被 PC4-PI 允许投影族检测，则存在固定低维 CRT/Bohr 频率族 `Λ_*` 与无穷子列，使 DGap 压缩异常由 `Λ_*` 同相位吸收。因此该情形进入 PC4-FCT。

**证明。** 排除尾项和误差后，盒空间能量由有限频率组合承载。若频率维数或新独立频率无界，则由 CRT martingale 正交与 DSO/PI 接口产生可检测投影能量，矛盾。故主要能量落在固定低维谱族。该低维谱族沿无穷子列同相位承载离线零点异常，给出 FCT-Seed 的低维编码证书。证毕。

## 6. 对 DGap-Decomposition 的影响

本文把“PI 不可检测”情形严格转入 PC4-FCT。至此，DGap 分解的三个基础接口已全部定理化为条件化文档：

1. 盒有限重叠：`docs/rh-pc4-dual-box-overlap.md`；
2. 投影正交化：`docs/rh-pc4-dual-projection-orthogonalization.md`；
3. 低维频率抽取：本文。

剩余总攻义务不再是 DGap 内部分类，而是把这些接口依赖的 DSO/CE/FCT/LSMP 外部结构逐项无条件化。
