# DGap 低维频率抽取逐行强度审查

本文补强 `docs/rh-pc4-dual-lowdim-frequency-extraction.md` 的核心跳步：从“PI 不可检测的剩余盒能量”推出“固定低维频率族承载固定比例能量”，再推出 `FCT_seed`。本文仍属于 RH 反例矛盾场的条件化无条件化推进，不宣称 RH 已证明；它的作用是把 `DGap` 内部第三接口压缩到可审查的谱抽取义务。

## 1. 输入与非逃逸假设

从 `docs/rh-dgap-projection-line-by-line-audit.md` 得到剩余能量

`u=P_res h`, `||u||_2^2 >= E_X`, `E_X=X^{2β-1-o(1)}`, `β>1/2`。

当前分支同时假设以下终端均未触发：

1. `PC4-PI`：允许投影族没有检测到固定比例能量；
2. `SC`：短簇局部容量没有承载主要质量；
3. `LV/LSMP`：低体积或低尺度乘积逃逸没有发生；
4. `CE`：模板复杂度逃逸没有发生；
5. `Err`：边界、尾项、平滑截断误差没有承载主要质量。

因此，任何后续“逃逸”都必须回到上述五类之一；若无法回到这些类，则必须产生固定结构证书。

## 2. 有限频率截断的可审查形式

固定一个尺度 `X`。盒模板由有限个物理窗、dyadic 标签、CRT/Bohr 相位窗与平滑边界组成。对每个模板函数 `ψ_B` 取 Fourier/Vaaler 截断：

`ψ_B = ψ_{B,<=H}+ψ_{B,>H}`。

选择 `H=log^A X`，其中 `A` 大于模板复杂度常数。若

`Σ_B |<h,ψ_{B,>H}>|^2 >= cE_X`,

则尾项不是平方可和误差，而是一个可命名高复杂度事件；按定义进入 `CE/LSMP`。在当前非逃逸分支中，存在固定 `c_0>0` 使

`||P_{<=H}u||_2^2 >= c_0||u||_2^2`。

这一步只使用 Parseval、Vaaler 截断余项的 `L^2` 可加性，以及 `docs/rh-capacityfail-binding-table.md` 中 `DGap 盒有限重叠` 的绑定；统一尾项证明见 `docs/rh-fourier-vaaler-tail-uniform-audit.md`，没有引入新的自由事件。

## 3. 频率包与新增独立性

把 `u_{<=H}` 的谱支撑分成频率包 `Ω_j(X)`。每个频率包由以下数据确定：

- CRT 字符坐标；
- Bohr 倒数相位标签；
- dyadic 尺度标签；
- 短弧相位标签；
- 一个有界整数关系矩阵。

称两个包在尺度列上“新增独立”，若它们含有不能由既有有界关系矩阵生成的新 CRT/Bohr 坐标。新增独立包有两个后果：

1. 它们对既有低维 span 的投影残差保持正比例；
2. 在新增 CRT 坐标上形成 martingale difference 或近正交差分。

于是若无穷多尺度上不断出现承载固定比例能量的新增独立包，则由 `docs/rh-pc4-dso-crt-martingale.md` 的 DSO square-function 产生可检测平方函数能量；其到 `PC4-PI` 允许投影族的桥接见 `docs/rh-dso-pi-squarefunction-bridge-audit.md`，并由 `docs/rh-pc4-pi-lacunary-capacity.md` 或 `docs/rh-pc4-pi-cap-carleson.md` 转成 `PC4-PI` 或 DSO 容量终端。当前分支排除 `PC4-PI/DSO`，所以新增独立包不能无限次承载固定比例能量。

## 4. 固定低维族抽取

令 `η>0` 为固定小常数。对每个成功尺度取最少包族 `𝒫_X`，使

`||P_{𝒫_X}u_{<=H}||_2^2 >= (1-η)||u_{<=H}||_2^2`。

若最少包族的独立维数 `dim_Z span(𝒫_X)` 沿成功尺度无界，则可贪心抽取彼此新增独立的包列，每个包列至少承载 `η/log^C X` 的能量。有限重叠给出的损失只有 `log^C X`，仍足以在离线零点异常量级 `E_X=X^{2β-1-o(1)}` 下产生 `X^{2β-1-o(1)}` 级平方函数能量，触发 `PC4-PI/DSO`。矛盾。

因此存在固定维数 `d=O_{template,η}(1)` 与无穷子列，使主要谱支撑落入一个固定整数关系模板

`Λ_* = span_Z{λ_1,...,λ_d}`，且

`||P_{Λ_*}u||_2^2 >= c_1||u||_2^2`。

这里“固定”指关系模板固定；具体相位可随 `X` 漂移，但漂移必须服从同一有界维数的频率坐标。

## 5. 排除尺度漂移逃逸

还需排除一种隐藏逃逸：每个尺度都有低维族，但低维族随尺度漂移，导致没有单一 `Λ_*` 可沿无穷子列固定。

由于模板复杂度、dyadic 标签数、短弧标签数与有界关系矩阵的高度均为 `log^O(1)X`，若没有固定模板沿无穷子列出现，则模板每次更新都必须新增一个坐标或提高关系高度。坐标新增回到第 3 节的 DSO/PI；关系高度提高回到 `CE/LSMP`；短弧标签无限细化回到 `FCT` 的相位漂移树或 `SC` 短簇。因此，在当前非逃逸分支中，可以抽取无穷子列并固定 `Λ_*` 的组合类型。

## 6. 从固定低维族到 FCT_seed

在固定低维族上，异常项可写为有限和

`Σ_{m=1}^M a_m(X)e(θ_m(X))`, `M=O(1)`，

其中 `θ_m(X)` 由 `Λ_*` 的 CRT/Bohr 相位和离线零点相位 `γlogX` 共同决定。若该有限和在无穷多成功尺度上同号承载固定比例异常，则按短弧 pigeonhole，存在固定短弧 `I_*` 与固定子和，使

`θ_m(X) mod 1 ∈ I_*`

并承载 `c_2E_X` 级能量。该数据正是 `docs/rh-pc4-fct-seed.md` 所需的低维编码种子：固定频率模板、固定相位短弧、固定同向异常符号；逐项同型匹配见 `docs/rh-fct-seed-isomorphism-audit.md`。

若相位不能固定在短弧中，则有限和发生抵消，不能长期承载 `E_X`；若通过不断换弧避免抵消，则进入 `docs/rh-pc4-fct-phase-drift.md` 的漂移压力分支。因此低维承载必然给出 `FCT_seed` 或回到已命名终端。

## 7. 主定理

**Theorem DGap-LowDim-LineByLine（DGap 低维抽取逐行版，条件化）。** 假设 `DGap-Projection-LineByLine` 给出剩余盒能量 `u`，且 `PC4-PI/DSO/SC/LV/LSMP/CE/Err` 均未触发。则存在固定低维 CRT/Bohr 频率族 `Λ_*`、固定短弧 `I_*` 与无穷成功尺度子列，使 `u` 的固定比例能量由 `Λ_*` 同相位承载，并给出 `FCT_seed`。

**证明。** 第 2 节把能量截断到有限频率，否则尾项进入 `CE/LSMP`。第 3--4 节说明若无固定低维族承载固定比例能量，则新增独立频率包无限出现，触发 DSO square-function 与 `PC4-PI`，矛盾。第 5 节排除低维族随尺度漂移的逃逸：漂移只能表现为坐标新增、关系高度增长或短弧无限细化，分别进入 `DSO/PI`、`CE/LSMP` 或 `FCT/SC`。故存在固定 `Λ_*`。第 6 节用有限相位和的短弧 pigeonhole 抽取固定同向相位证书，得到 `FCT_seed`。证毕。

## 8. 对剩余割集的影响

本文不消除所有 RH 总攻条件，但把 `R4-DGap` 的第三接口从“低维抽取直觉”降为三项可审查义务：

1. Fourier/Vaaler 尾项平方可和或进入 `CE/LSMP`，统一审查见 `docs/rh-fourier-vaaler-tail-uniform-audit.md`；
2. 新增独立频率包触发 `DSO/PI` 的 square-function，桥接审查见 `docs/rh-dso-pi-squarefunction-bridge-audit.md`；
3. 固定低维相位同向性精确匹配 `FCT_seed`，同型审查见 `docs/rh-fct-seed-isomorphism-audit.md`。

因此，下一步最硬点应从 `DGap` 内部跳步转向这些外部接口的精确引用或逐行证明，尤其是 `DSO/PI` square-function 到允许投影族的定量常数，以及 `FCT_seed` 定义的完全同型匹配。
