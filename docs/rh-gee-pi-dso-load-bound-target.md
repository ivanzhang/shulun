# GEE-PI/DSO 负担上界目标与剩余硬点

本文接收 `docs/rh-nrc-2d-midcap-structure-route.md` 中 MidCap 转出的相位盒/投影集中分支，专攻 Global-Exit-Exclusion 的 `GEE-PI` 与 `GEE-DSO`。现有文档已经证明很多“无回流”和“桥接”语义；但 GEE 需要的是定量上界：

`Load(PI;X)+Load(DSO;X)=o(Δ)`。

因此本文把 PI/DSO 的剩余问题改写为一个统一 Carleson-square-function 负担不等式。

## 1. 入口负担

PI/DSO 入口来自三类：

1. PPI 或 MidCap 的相位盒重复集中；
2. DSO 新增独立频率包；
3. FCT/DGap/Fourier 尾项中转出的允许投影能量。

对每个尺度包 `j`，记投影偏差能量为

`e_j=δ_j^2 μ_j^0(A_j)`。

GEE-0 路由给出总异常下界时，若 PI/DSO 承载固定比例异常，则有

`Σ_j e_j >= cΔ/log^C X`。

要排除 PI/DSO 出口，需要证明相反方向：在非 `SC/LV/LSMP/CE/FCT/NRC` 分支中，允许投影族总能量为 `o(Δ)`。

## 2. 已有桥接能做什么

现有文件提供了三件事：

- `PI-lacunary`：强 lacunary 尺度包有 Mellin 支撑有限重叠；
- `DSO/PI bridge`：新增独立频率包必须反馈到允许投影检测；
- `NoReturn`：适用条件失败不会回流，而转入命名出口。

这些说明 PI/DSO 不是自由逃逸通道，但还没有单独给出 `Load=o(Δ)`。真正缺口是 dense 包的统一容量上界。

## 3. 统一目标不等式

**GEE-PI/DSO-Carleson Target.** 对任意固定允许投影模板族 `𝓦_*` 与任意非终端尺度包 `𝓙`，有

`Σ_{j∈𝓙} e_j <= Cap(𝓙;𝓦_*)/log^B X + Err_named`，

其中：

- `Cap(𝓙;𝓦_*)` 是零频容量或 martingale square-function 容量；
- `Err_named` 全部转入 `SC/LV/LSMP/CE/FCT/NRC`；
- 对 GEE-PI/DSO 仍登记的包，`Cap(𝓙;𝓦_*) <= Δ/log^B X`。

若该目标成立，则

`Load(PI;X)+Load(DSO;X)=o(Δ)`。

## 4. Lacunary 分支

强 lacunary 子列满足 Mellin 支撑有限重叠，已有 `PI-Lacunary-Capacity` 给

`Σ_{j in lac} e_j <= C Cap_lac + Err`。

若 `Cap_lac<=Δ/log^B X`，则该分支为 `o(Δ)`；若 `Cap_lac` 达到 `Δ` 级，则它不是压缩异常，而是 disjoint 容量本身大量存在。此时必须由 GEE-0 负担路由判定：

- 若这些 disjoint 容量已计入零频基线，不能再作为异常负担；
- 若偏差超过零频容量，触发 PI 容量矛盾或 `SC/LV/CE`。

因此 lacunary 分支的剩余义务是“基线扣除一致性”，不是新的正交估计。

## 5. Dense/DSO 分支：真正硬点

Dense 包不能靠支撑 disjoint。需要 martingale/Carleson 型平方函数：

`Σ_{j in dense} ||Π_j h||_2^2 <= C ||h||_2^2 + Err_named`。

若 `h` 是离线异常归一化后的同向函数，则还需证明

`||h||_2^2 <= Δ/log^B X`

或超过该界时已经触发 `SC/LSMP/CE/FCT`。这就是当前 `GEE-PI/DSO` 的核心硬点：**dense 投影包的 square-function 容量必须小于主异常。**

## 6. Theorem GEE-PI/DSO（条件化目标版）

**Theorem GEE-PI-DSO-Conditional.** 假设以下三项成立：

1. **Lac-Baseline：** lacunary disjoint 容量已从异常负担中扣除，超容量偏差转入 `SC/LV/CE`；
2. **Dense-Carleson：** dense 允许投影包满足 `Σ||Π_jh||_2^2 <= C||h||_2^2+Err_named`；
3. **Anomaly-L2-Control：** 非终端分支中 `||h||_2^2 <= Δ/log^B X`，否则触发 `SC/LSMP/CE/FCT`；

则

`Load(PI;X)+Load(DSO;X)=o(Δ)`。

**证明。** 对 PI/DSO 入口按尺度二分。Lacunary 部分由 Lac-Baseline 与有限重叠吸收或转命名出口。Dense 与 DSO 新频率部分由 DSO/PI bridge 拉回允许投影；Dense-Carleson 给平方函数总界；Anomaly-L2-Control 把总界压到 `Δ/log^B X`。所有适用条件失败由 NoReturn 审查转入命名出口，故留在 PI/DSO 的负担为 `o(Δ)`。证毕。

## 7. 当前剩余最小割集

`GEE-PI/DSO` 当前不是完全闭合，而是被压缩为三项：

1. `Lac-Baseline`：lacunary 零频容量与异常负担不重复计数；
2. `Dense-Carleson`：dense 投影包 square-function 容量上界；
3. `Anomaly-L2-Control`：非终端离线异常函数的 `L^2` 质量低于 `Δ/log^B X`，否则触发结构出口。

其中 `Dense-Carleson` 的正交核心已由 `docs/rh-gee-dense-carleson-load-bridge.md` 接入；当前最硬点转为 `Baseline-Subtraction`：把 lacunary/dense 的零频容量与 GEE-0 异常负担严格分离。

## 8. Dense-Carleson 推进

新增 `docs/rh-gee-dense-carleson-load-bridge.md`。审查结果：Dense-Carleson 的 Hilbert/martingale 核心已由 `PC4-PI-Dense` 条件化闭合；GEE 剩余不是正交估计，而是 `Baseline-Subtraction`：dense/lacunary 零频容量不能重复计入异常负担。

## 9. Baseline-Subtraction 更新

新增 `docs/rh-gee-baseline-subtraction-lemma.md`。`Lac-Baseline` 与 `Dense-Carleson` 的账本缺口合并为 Baseline-Subtraction，并已定理化为 PI/DSO 零频容量扣除引理。当前 `GEE-PI/DSO` 可标记为“基线扣除条件闭合”，剩余压力转入接收出口 `SC/LV/LSMP/CE/FCT/NRC` 的全局上界。
