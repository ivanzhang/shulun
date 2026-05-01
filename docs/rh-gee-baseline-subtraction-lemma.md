# GEE Baseline-Subtraction：PI/DSO 零频容量扣除引理

本文专攻 `docs/rh-gee-dense-carleson-load-bridge.md` 留下的账本硬点：PI/DSO 的 lacunary/dense 零频容量不能重复计入异常负担。核心原则是：GEE-0 的 `Load(E;X)` 只能登记相对 CRT 零频基线的超额偏差；普通零频容量属于 PC2/MLC 基线，已经在 `w_X^0` 中扣除。

## 1. 问题来源

GEE-0 定义原子偏差为

`bias(a)=σΣ_{n∈a}(w_X(n)-w_X^0(n))`。

因此若一个 PI/DSO 投影包 `A` 的实际质量满足

`μ(A)=μ^0(A)+Err(A)`,

那么可登记异常只能来自 `Err(A)`，而不是 `μ^0(A)` 本身。Carleson 容量界给出的

`Σ_j e_j <= C Cap(𝓙)`

若其中 `Cap(𝓙)` 是零频容量，就不能直接当作 `Load(PI/DSO)`；必须先扣除零频基线。

## 2. 超额偏差定义

对 PI/DSO 包 `A_j`，定义

`Excess(A_j)=max(0, σ(μ_j(A_j)-μ_j^0(A_j)))`。

若使用平方能量形式 `e_j=δ_j^2 μ_j^0(A_j)`，则只把超过零频容量账本可解释的部分登记为异常：

`ExcessEnergy_j=max(0, e_j-C_0 μ_j^0(A_j))`。

这里 `C_0` 是固定模板和归一化允许的零频容量常数。`μ_j^0(A_j)` 或 `Cap(𝓙)` 本身归入基线，不属于出口负担。

## 3. Baseline-Subtraction Lemma

**Lemma Baseline-Subtraction.** 在 PC2 的 CRT 零频基线匹配和 GEE-0 的统一权重定义下，对任意 PI/DSO 尺度包 `𝓙`，有

`Load_{PI/DSO}(𝓙;X) <= Σ_{j∈𝓙} Excess(A_j) + Err_route`,

或在平方能量口径下

`Load_{PI/DSO}(𝓙;X) <= Σ_{j∈𝓙} ExcessEnergy_j + Err_route`。

其中 `Err_route` 只包含路由有限重叠、平滑边界和 Vaaler 尾项，均已由 GEE-0 bookkeeping 或命名出口处理。特别地，零频容量 `Σ μ_j^0(A_j)`、`Cap_lac`、`Cap_dense` 不得单独计入 `Load(PI/DSO)`。

**证明。** GEE-0 的原子集合 `𝓐_X` 来自 `w_X-w_X^0` 的同向正偏差。把任一 PI/DSO 包内的实际权重分解为零频基线加偏差：`w_X=w_X^0+(w_X-w_X^0)`。第一项在 PC2/MLC 零频基线中已经计入，不属于异常原子；第二项才贡献 `bias(a)`。若包按多个投影模板重复记录，拆分权重 `θ_{a,E}` 只作用于同一个偏差项，不会把 `w_X^0` 重新加入。平方能量口径是同一事实的二次化：容量界中的零频项是允许背景，只有超过固定容量常数的能量超额可登记为异常。边界和尾项由 GEE-0 的 `Err_PC2=o(Δ)` 与路由常数表吸收或转入命名出口。证毕。

## 4. 对 lacunary 与 dense 的统一处理

### 4.1 Lacunary

lacunary 分支的 `Cap_lac` 是 disjoint Mellin/CRT 支撑的零频容量。由本引理，若

`Σ_{j in lac} e_j <= C Cap_lac + Δ/log^B X`，

则可登记负担至多 `Δ/log^B X`；`C Cap_lac` 不计入异常。若 `e_j` 超过容量界固定比例，则触发 PI 容量矛盾或 `SC/LV/CE`。

### 4.2 Dense

dense 分支由 Carleson/square-function 给

`Σ_{j in dense} e_j <= C Cap_dense + Err_named`。

扣除 `C Cap_dense` 后，留给 `Load(PI/DSO)` 的只有 `Err_named` 和超额能量。前者转命名出口，后者若超过 `Δ/log^B X` 则是容量界违反或结构事件；否则为 `o(Δ)`。

## 5. GEE-PI/DSO 扣除定理

**Theorem GEE-PI-DSO-Baseline-Subtracted.** 假设：

1. lacunary 与 dense 分支分别满足既有容量界；
2. 容量界适用条件失败均按 NoReturn 转入 `SC/LV/LSMP/CE/FCT/NRC`；
3. 超过零频容量界的剩余偏差若大于 `Δ/log^B X`，则触发容量矛盾或命名出口；

则

`Load(PI;X)+Load(DSO;X)=o(Δ)`。

**证明。** 对 PI/DSO 包按 lacunary/dense 二分。每一部分先用对应容量界控制总能量，再由 Baseline-Subtraction 扣除零频容量项。适用条件失败进入命名出口，不留在 PI/DSO。剩余超额若大于阈值，按假设触发容量矛盾或结构出口；否则有限重叠求和给 `o(Δ)`。证毕。

## 6. 当前状态与诚实口径

本文闭合的是 PI/DSO 的“重复计数”账本硬点。它仍依赖：

- lacunary/dense 容量界本身；
- NoReturn 的失败出口分类；
- 超额容量违反能被识别为容量矛盾或命名结构事件。

在这些已按现有文档引用的前提下，`GEE-PI/DSO` 可以标记为“基线扣除条件闭合”。要升级为全局无条件闭合，仍需把 `GEE-SC/GEE-LSMP/GEE-CE/GEE-FCT/GEE-A` 等接收出口逐一证明为 `o(Δ)`。
