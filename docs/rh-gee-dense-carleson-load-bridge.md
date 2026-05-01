# GEE Dense-Carleson 负担桥接

本文专攻 `docs/rh-gee-pi-dso-load-bound-target.md` 中最硬的 `Dense-Carleson`。已有 `PC4-PI-Dense` 证明固定模板密集尺度包满足容量界：

`E_dense(𝓘) <= C(𝓦_*) Cap(𝓘)`。

但 GEE 需要的是负担上界 `Load(PI)+Load(DSO)=o(Δ)`。因此本文补上从 dense 容量界到 GEE 负担的桥接，并明确仍需 `Anomaly-L2-Control` 或容量扣除。

## 1. Dense-Carleson 已有核心

由 `docs/rh-pc4-dso-crt-martingale.md`，固定 `L^2` 函数在 inverse-limit CRT 空间上的 martingale difference 满足

`Σ_k ||D_kF||_2^2 <= ||F||_2^2`。

由 `docs/rh-pc4-pi-dense-closure-theorem.md`，固定模板、自然细化、误差平方可和且无 `FCT/LSMP/LV/SC/CE/NRC` 时，任意 dense 包满足

`Σ_{j in dense} e_j <= C(𝓦_*) Cap_dense(𝓘)`。

因此 `Dense-Carleson` 的 Hilbert 空间核心不是剩余硬点；剩余是 GEE 归一化：`Cap_dense` 是否已从异常负担中扣除，或是否小于 `Δ/log^B X`。

## 2. GEE 负担归一化

GEE-0 中的 `Load(E;X)` 只应记录“相对零频基线的异常负担”，不能把零频容量本身重复计为异常。因此 dense 包有两种合法登记方式：

1. **容量基线登记：** `Cap_dense` 是零频背景，已在 PC2/MLC 基线中扣除；则只有超过容量界的部分能进入 `Load(PI/DSO)`。
2. **异常能量登记：** 若 `Cap_dense` 本身被当作待排除负担，则必须证明 `Cap_dense<=Δ/log^B X`，否则 GEE-PI/DSO 不能闭合。

这一区分是必要的；否则会把普通零频候选容量误记为反例异常。

## 3. Dense-Carleson-GEE 定理

**Theorem Dense-Carleson-GEE-Bridge.** 假设：

1. `PC4-PI-Dense` 容量界成立；
2. dense 包的零频容量按 GEE-0 路由不重复计入异常负担；
3. 超过零频容量的偏差若大于 `Δ/log^B X`，则触发 `PI` 容量矛盾或 `SC/LSMP/CE/FCT`；

则 dense PI/DSO 分支对 GEE 的贡献满足

`Load_dense(PI/DSO;X)=o(Δ)`。

**证明。** 由 `PC4-PI-Dense`，dense 能量不超过 `C Cap_dense` 加命名误差。按假设 2，`Cap_dense` 属于零频基线，不登记为异常。剩余可登记负担只能是超过容量界或超过基线扣除后的偏差。若该偏差大于 `Δ/log^B X`，假设 3 将其转入容量矛盾或命名出口；若不大，则有限重叠求和给 `o(Δ)`。证毕。

## 4. 仍需补齐的基线扣除一致性

本文把 `Dense-Carleson` 的剩余硬点进一步压缩为：

**Baseline-Subtraction Lemma.** 在 GEE-0 的 `Load` 定义中，PI/DSO dense 包的 `Cap_dense` 只作为零频容量基线出现，不能重复计为异常负担；真正进入 `Load(PI/DSO)` 的是超过基线与 Carleson 容量界的超额偏差。

这与 `Lac-Baseline` 是同一个账本问题。若该账本证明完成，则 `Dense-Carleson` 可从 GEE 割集中移除。

## 5. 当前状态

- `Dense-Carleson` 的正交/Carleson 上界：由 `PC4-PI-Dense` 条件化闭合；
- 适用条件失败：由 NoReturn 转入 `SC/LV/LSMP/CE/FCT/NRC`；
- GEE 负担桥接：本文给出条件定理；
- 剩余最小硬点：`Baseline-Subtraction`，统一处理 lacunary 与 dense 的零频容量扣除，避免重复计数。

因此 `Dense-Carleson` 与 `Baseline-Subtraction` 已在 GEE 账本中拼接；后续最优攻坚应转向接收出口 `SC/LSMP/CE/FCT/A` 的全局上界。

## 6. Baseline-Subtraction 已补齐

新增 `docs/rh-gee-baseline-subtraction-lemma.md`。该文把 PI/DSO 的零频容量从异常负担中扣除：`Load(PI/DSO)` 只登记超过 `μ^0/Cap` 基线与 Carleson 容量界的超额偏差。
