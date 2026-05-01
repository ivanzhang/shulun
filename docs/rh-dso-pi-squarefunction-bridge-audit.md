# DSO/PI square-function 到允许投影族桥接审查

本文补强 `docs/rh-dgap-lowdim-extraction-line-by-line-audit.md` 的外部接口：当新增独立频率包在无穷多尺度上承载固定比例能量时，为什么它不能停留为一个未命名的 DSO 能量，而必须触发 `PC4-PI` 的允许投影族、或进入已命名外部容量终端。本文仍是 RH 反例矛盾场的无条件化推进文档，不宣称 RH 已证明。

PI dense/Carleson 与 DSO bridge 的适用条件无回流审查见 `docs/rh-pi-dense-dso-bridge-no-return-audit.md`。

## 1. 输入：新增独立频率包

从 DGap 低维抽取审查得到一列频率包 `Ω_j`，满足：

1. 每个 `Ω_j` 在尺度 `X_j` 上承载能量 `e_j >= log^{-C}X_j E_{X_j}`；
2. `Ω_j` 含有相对既有频率 span 的新增 CRT/Bohr 坐标；
3. `Ω_j` 不属于短簇、低体积、复杂度逃逸或尾项误差；
4. 频率包由固定复杂度模板自然细化产生。

目标是证明：若这样的包列不能抽取固定低维 FCT 证书，则必有一个允许投影族 `Π` 检测到

`Σ_j ||Π_j h||_2^2 >= log^{-C} Σ_j e_j`，

从而触发 `PC4-PI` 或 DSO 容量矛盾。

## 2. 允许投影族的最小定义

本文把 `PC4-PI` 的允许投影族统一为四类模板投影：

- CRT 新坐标字符投影；
- Bohr 短弧相位投影；
- dyadic 尺度局部投影；
- 上述三类的有限交投影。

每个新增频率包 `Ω_j` 由这些标签的有限交定义。因此其正交投影 `P_{Ω_j}` 不是外来对象，而是允许投影族的有限线性组合；若需要平滑边界，只产生 `log^C X_j` 的 frame 损失，已由 `docs/rh-dgap-projection-line-by-line-audit.md` 的 frame 上界吸收。

## 3. DSO square-function 到投影能量

在 inverse-limit CRT 空间中，把尺度 `X_j` 的窗口拉回为 `F_j`。模板自然细化保证

`F_j = E_{k_j}F + err_j`, `Σ_j ||err_j||_2^2 < ∞`

或误差进入 `CE/LSMP`。新增坐标部分为 martingale difference `D_{k_j}F` 的一个有限频率子包。

由 `docs/rh-pc4-dso-crt-martingale.md` 的 Parseval 公式，

`||P_{Ω_j}F_j||_2^2 <= C ||D_{k_j}F||_2^2 + O(||err_j||_2^2)`，

反向地，若 `Ω_j` 承载 `e_j` 能量，则允许投影 `Π_j=P_{Ω_j}` 满足

`||Π_j h||_2^2 >= log^{-C} e_j - O(||err_j||_2^2)`。

这里的 `log^{-C}` 损失来自：盒 frame、平滑边界、有限交投影与谱包粗化；固定复杂度保证这些损失都是多对数级。

## 4. 稀疏与密集尺度二分

对包列 `Ω_j` 作尺度二分。

### 4.1 Lacunary 子列

若存在强 lacunary 子列，则 Mellin 支撑有限重叠。由 `docs/rh-pc4-pi-lacunary-capacity.md`，允许投影能量不能在无限 lacunary 子列上无界累积；若累积达到离线零点异常规模，则触发 `PC4-PI`。

### 4.2 Dense 子列

若不存在 lacunary 承载子列，则存在 dense pack。新增 CRT 层的 martingale square-function 给出

`Σ_{j in pack} ||Π_jh||_2^2 <= C Cap(pack)+Err`。

若左边仍承载固定比例离线异常，则进入 `PC4-PI`；若容量界失败，则按 `docs/rh-capacityfail-binding-table.md` 绑定到 DSO/PI 容量失败，不是自由事件。

因此新增独立频率包不能同时避开 lacunary PI 与 dense DSO/PI。

## 5. 隐藏逃逸排除

可能的逃逸只有三类：

1. **投影不允许**：但第 2 节说明固定复杂度新增包由允许标签有限交生成；否则即为模板复杂度逃逸 `CE`。
2. **误差吞噬能量**：若 `Σ||err_j||_2^2` 不可忽略，则进入 `CE/LSMP/LV`，与当前分支假设矛盾。
3. **频率包重叠过高**：若重叠超过 `log^C`，则不是固定复杂度盒族，而进入 `SC` 或低体积拥挤事件；有限重叠时由 frame 上界吸收。

故在非逃逸分支中，DSO square-function 必须反馈到允许投影族。

## 6. 桥接定理

**Theorem DSO-PI-SquareFunction-Bridge（条件化桥接）。** 在固定复杂度、自然细化、平方可和误差假设下，若一列新增独立 CRT/Bohr 频率包在无穷多尺度上承载固定比例盒能量，并且不进入 `SC/LV/LSMP/CE/Err/FCT`，则 `PC4-PI` 的允许投影族检测到固定比例能量；若检测容量失败，则该失败已绑定到 DSO/PI 容量终端。

**证明。** 每个新增包由允许投影标签有限交生成，故 `P_{Ω_j}` 可由允许投影族表示，最多损失 `log^C`。模板自然细化把新增坐标拉回 martingale difference，Parseval 给 square-function 控制。尺度列若 lacunary，则由 lacunary 容量触发 PI；若 dense，则由 DSO square-function 与 Carleson/PI 容量触发 PI 或容量终端。三类隐藏逃逸分别转入 `CE`、`LSMP/LV`、`SC`，均已排除。故结论成立。证毕。

## 7. 对 RH 总攻割集的影响

本文把 `DGap-LowDim-LineByLine` 中“新增独立频率包触发 DSO/PI”的引用展开为可审查桥接：

- 新增包必须是允许投影族的有限交；
- square-function 能量必须回到投影检测；
- lacunary/dense 尺度均有容量出口；
- 非允许、误差吞噬、重叠过高分别转入已命名终端。

剩余硬点进一步缩小为两项：

1. `FCT_seed` 与低维相位证书的逐字同型匹配；
2. Fourier/Vaaler 尾项平方可和在全部固定盒模板上的统一证明。
