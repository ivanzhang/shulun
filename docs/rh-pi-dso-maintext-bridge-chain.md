# PI/DSO 主文桥接链：投影增量、平方函数与无回流容量

本文把 RH 反例矛盾场中 `PI/DSO` 相关接口合成为一条可并入主文的闭合链。它接收来自 PPI、FCT、DGap 和 PC4 事件图的高投影增量或新增独立频率包，并证明：在固定复杂度和已命名终端吸收口径下，这些能量不能停留为未命名的 DSO 或 PI 自由回流；它们必须进入 `PI` 容量账本、`DSO` 正交账本，或转入 `FCT/SC/LV/LSMP/CE/NRC`。

本文不宣称 RH 已证明；它闭合的是 PI/DSO 互相引用的桥接疑点。下游 `SC` 局部乘积容量、`LV/LSMP/CE` 与 DGap 尾项仍需继续主文化。

## 1. 入口对象

PI/DSO 链处理两类输入。

1. **PI 输入。** 固定模板窗口 `A_j` 在尺度 `X_j` 上承载相对偏差 `δ_j`，能量

   `e_j=δ_j^2 μ_j^0(A_j)`。

2. **DSO 输入。** 新增独立 CRT/Bohr 频率包 `Ω_j` 承载能量

   `e_j >= log^{-C}X_j E_{X_j}`，

   且该包不在旧频率 span 内；若在旧 span 内，则进入 `FCT`。

两类输入的共同本质是：一个固定复杂度投影族在无穷多尺度上承载离线零点级异常。

## 2. 允许投影族

允许投影族由以下有限模板生成：

- CRT 新坐标字符投影；
- Bohr 或倒数短弧相位投影；
- dyadic 尺度局部投影；
- 上述投影的有限交、有限并差和平滑边界版本。

每个 PPI/FCT/DGap 输出的固定复杂度频率包都可写成允许投影族的有限线性组合。若不能这样写，则不是 PI/DSO 内部问题，而是模板复杂度逃逸 `CE` 或低质量逃逸 `LSMP`。

## 3. DSO 到 PI：平方函数桥接

在 inverse-limit CRT 空间中，将尺度 `X_j` 的窗口拉回为 `F_j`。自然细化给出

`F_j=E_{k_j}F+err_j`，

其中误差平方可和；若不可和，则进入 `CE/LSMP/LV`。新增坐标部分是 martingale difference `D_{k_j}F` 的有限频率子包。由有限群 Parseval 与 martingale square-function，

`||P_{Ω_j}F_j||_2^2 <= C||D_{k_j}F||_2^2+O(||err_j||_2^2)`。

反向地，若 `Ω_j` 承载 `e_j` 能量，则允许投影 `Π_j=P_{Ω_j}` 检测到

`||Π_j h||_2^2 >= log^{-C}e_j-O(||err_j||_2^2)`。

因此 DSO 新频率包不能停留为未命名 DSO 能量：它必须反馈到允许投影检测，或转入 `CE/LSMP/LV/SC/FCT`。

## 4. Lacunary/dense 尺度二分

对承载投影能量的尺度列作二分。

### 4.1 Lacunary 包

若可抽取强 lacunary 子列，则 Mellin 支撑有限重叠。PI lacunary 容量账本给出

`Σ_{j in lacunary} e_j <= C Cap_lac + Err`。

若左侧达到离线零点异常所需的同相位压缩规模，则触发 `PI` 终端；若违反容量界，则是容量反设矛盾或 `SC/LV/CE` 出口。

### 4.2 Dense 包

若没有 lacunary 承载子列，则存在 dense pack。固定模板可拉回 CRT martingale，得到 Carleson/平方函数容量界

`Σ_{j in pack} ||Π_jh||_2^2 <= C Cap_dense + Err`。

若 dense pack 仍承载固定比例异常，则进入 `PI`；若容量界适用条件失败，则按失败原因进入 `CE/FCT/LV/LSMP/SC`；若容量界本身被反设违反，则为对应容量矛盾。

## 5. DSO-E 局部正交输入

新增 Euler 局部因子的非主偏差按四类处理。

1. 单层字符正交：有限阿贝尔群 Parseval，无需深外部输入；
2. 倒数/混合相位非共振：由 `NRC/EXT-KL` 控制；
3. 可控多频层：局部平方能量由系数平方和控制；
4. 大局部复杂度：剥离后进入 `FCT`、`LSMP` 或返回可控多频层。

所以 DSO-E 的失败边是

`FCT / LSMP / NRC / PI-Seed / CE`，

而不是“先假设 PI 闭合再证明 PI 闭合”。这排除了 DSO 与 PI 之间的循环依赖。

## 6. 无回流清单

PI/DSO 桥接中所有适用条件失败均有命名出口：

- 投影不允许：`CE/FCT/LSMP`；
- 自然细化失败：`CE/LV/FCT`；
- 误差吞噬能量：`LSMP/LV/CE`；
- 频率包重叠过高：`SC/LV/CE`；
- 非共振失败：`FCT`；
- 完成和或外部解析上界失败：`NRC/EXT`；
- 容量适用条件失败：按原因转入上述命名事件；
- 容量界被反设违反：作为容量矛盾终止。

因此不存在从 `CapacityFail`、DSO square-function 或 PI dense pack 返回自身的未标记循环。

## 7. PI/DSO 主文桥接定理

**Theorem PI-DSO-Maintext-Bridge。** 在固定复杂度模板、自然细化、有限重叠、平方可和尾项和已命名终端吸收假设下，任何 PI 高投影增量或 DSO 新增独立频率包若在无穷多尺度上承载离线零点级异常，则必发生以下之一：

1. `PI` lacunary 或 dense 容量账本触发；
2. `DSO` square-function/Parseval 容量账本触发；
3. `FCT/SC/LV/LSMP/CE/NRC` 中某个命名终端触发；
4. 对应容量界被反设违反，形成容量矛盾。

特别地，`PI/DSO` 不构成自由吸收通道，也不形成相互引用循环。

**证明。** DSO 输入由第 3 节反馈到允许投影族；PI 输入已在允许投影族内。尺度列由第 4 节分为 lacunary 或 dense，两者分别由 PI lacunary 容量或 dense Carleson/square-function 容量处理。DSO-E 局部非主项由第 5 节输入到 NRC/FCT/LSMP/PI-Seed/CE，不回用 PI 闭合作前提。所有适用条件失败由第 6 节列入命名出口。分支穷尽，故结论成立。证毕。

## 8. 对全局无条件化的影响

本文把 FCT 重复状态、PPI 投影重复和 DGap 新频率包共同流向的 `PI/DSO` 接口主文化。下一步剩余压力主要转为：

1. `SC` 局部乘积容量与短簇终端；
2. `LV/LSMP/CE` 外部吸收的主文合并；
3. DGap 三接口与 Fourier/Vaaler 尾项平方可和的主文化；
4. `EXT-*` 外部定理精确页码与最终符号口径统一。
