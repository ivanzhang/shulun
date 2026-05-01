# PC4-Dual：DGap 投影正交化接口

本文补强 `docs/rh-pc4-dual-dgap-decomposition.md` 的第二个基础接口：当 `DGap` 正质量不集中于短簇或低体积盒时，如何把分散盒质量严格转成 PC4-PI 可检测的投影能量。本文仍是条件化接口，但把“盒函数正交化”拆成可审查的 Hilbert 空间步骤。

## 1. 输入：分散正质量

设 `h=g_z^0-g_z`，盒族 `𝓑` 已满足 `docs/rh-pc4-dual-box-overlap.md` 的有限重叠。记

`H(B)=<h,1_B>_W=Σ_{n∈B} h(n)W(n/X)`，

`μ^0(B)=<1_B,1_B>_0` 为零频体积。

排除 SC 与 LV/LSMP 后，存在中等体积盒族 `𝓑_*`，使

`Σ_{B∈𝓑_*} H(B)_+ >= cΔ`,

每个盒满足 `H(B)_+<ηΔ` 且 `μ^0(B)>X^{1/2-o(1)}`。

## 2. 归一化盒函数

对每个盒定义零均值归一化函数

`φ_B=(1_B-μ^0(B))/sqrt(μ^0(B))`

更准确地，在 CRT 零频概率空间中写

`φ_B=(1_B-E_0 1_B)/||1_B-E_0 1_B||_2`。

若 `μ^0(B)` 不过大，两个定义只差固定常数；若盒过大，其低频常数项被扣除，剩余仍检测偏差。于是

`<h,φ_B> ≍ H(B)/sqrt(μ^0(B))`

除非 `h` 的质量主要落在常数方向；常数方向对应全局基线误差，已由 PC2 排除。

## 3. Bessel/Cauchy 能量下界

令 `V=span{φ_B:B∈𝓑_*}`，`P_V` 为正交投影。若盒函数有限重叠，则 Gram 矩阵满足

`||G||_{op} <= log^C X`。

因此

`||P_V h||_2^2 >= log^{-C}X · Σ_{B∈𝓑_*} |<h,φ_B>|^2`。

结合 Cauchy，得到

`||P_V h||_2^2 >= log^{-C}X · (Σ_B H(B)_+)^2 / Σ_B μ^0(B)`。

在主层 `Σ_B μ^0(B)<=X^{1+o(1)}` 下，若 `Δ=X^{β-o(1)}`，则

`||P_V h||_2^2 >= X^{2β-1-o(1)}`。

## 4. 从盒空间到允许投影族

每个盒是物理窗、dyadic 锚层与 CRT/Bohr 相位原子的交。其指标函数属于固定复杂度模板族生成的有限布尔代数。由 `docs/rh-pc4-dso-template-consistency.md`，该模板族可用有限个允许投影函数与平方可和误差逼近。

因此 `V` 可分解为

`V=V_PI ⊕ V_low ⊕ V_err`，

其中：

1. `V_PI` 由 PC4-PI 允许投影族张成；
2. `V_low` 是常数、低体积、短簇或固定低维频率部分；
3. `V_err` 为平方可和截断误差或边界误差。

若 `P_V h` 的主要能量落在 `V_PI`，则得到 PC4-PI 高投影增量。若落在 `V_low`，则分别转入 PC2 基线失败、LV/LSMP、SC，或由 `docs/rh-pc4-dual-lowdim-frequency-extraction.md` 抽取固定低维频率后进入 FCT。若落在 `V_err`，则进入 Complexity-Escape 或边界接口失败。

## 5. 投影正交化定理

**Theorem DGap-Projection-Orthogonalization（DGap 投影正交化，条件化）。** 假设：

1. `DGap-Box-Overlap` 的有限重叠成立；
2. 盒指标属于固定复杂度 CRT/Bohr/dyadic 模板族，或复杂度逃逸转入 CE/FCT/LSMP；
3. PC2 已排除常数方向基线误差；
4. SC、LV/LSMP 与 FCT 低频部分不作为当前终端。

若 `DGap` 正质量在中等体积盒中分散且不集中于短簇，则至少发生一项：

1. PC4-PI 允许投影族获得能量下界

   `||P_PI h||_2^2 >= X^{2β-1-o(1)}`；

2. 能量落入固定低维频率 span，按 `docs/rh-pc4-dual-lowdim-frequency-extraction.md` 进入 PC4-FCT；
3. 能量落入低体积或短簇子空间，进入 LV/LSMP 或 PC4-SC；
4. 模板复杂度或误差不可控，进入 Complexity-Escape/接口失败。

**证明。** 由第 3 节，分散正质量给盒空间投影能量下界。由第 4 节，盒空间按允许投影、低频/终端子空间与误差子空间分解。若允许投影部分承载固定比例能量，得 1。否则能量主要落入低维频率、低体积/短簇或误差逃逸，分别给 2、3、4。证毕。

## 6. 对 DGap-Decomposition 的影响

本文把 `DGap-Decomposition` 中“分散正质量产生投影能量”的步骤严写为 Hilbert 空间正交化：有限重叠给 Gram 上界，Cauchy 给能量下界，模板一致性把盒空间接入 PC4-PI。PI 不可检测时的低维频率抽取见 `docs/rh-pc4-dual-lowdim-frequency-extraction.md`。
