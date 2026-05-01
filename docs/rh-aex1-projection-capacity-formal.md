# AEX-1 投影容量不等式正式化审查

本文专攻 `docs/rh-analytic-exit-reduction-table.md` 中的 AEX-1：零频扣除后的 PI 投影容量不等式。目标是把 AEX-1 从“PI/DSO 剩余硬点”拆成可审稿的三段：基线扣除、lacunary 容量、dense Carleson 容量。本文能闭合的是账本和归约；真正需要外部或上游容量定理支持的是最后两类容量界本身。

## 1. AEX-1 目标

对所有允许投影包 `𝓙`，证明

`Excess_PI(𝓙) <= Δ/log^{B_PI}X`

或触发命名转出。这里

`Excess_PI(𝓙)=Σ_{j∈𝓙} max(0, Energy_j-C_0 Cap^0_j)`，

`Cap^0_j` 是 PC2/CRT 零频容量基线。

## 2. 基线扣除部分

由 `docs/rh-gee-baseline-subtraction-lemma.md`，PI 包的零频容量不计入异常负担。故 AEX-1 不需要证明

`Σ Cap^0_j=o(Δ)`，

只需要证明超过零频容量和投影容量界的超额部分小。

**Lemma AEX1-Baseline.** 若每个 PI 包有分解

`Energy_j <= C_0 Cap^0_j + R_j + Err_j`，

且 `Err_j` 转入命名出口或总和为 `o(Δ)`，则

`Excess_PI(𝓙) <= Σ_{j∈𝓙} R_j + o(Δ)`。

**证明。** 由 `ExcessEnergy=max(0,Energy-C_0Cap^0)` 的定义，代入上式即得。`Err_j` 若为吸收误差，由阈值给 `o(Δ)`；若为结构失败，由 Transfer-Accounting 转出并从 PI 删除。证毕。

## 3. Lacunary 投影容量

lacunary 子列满足尺度支撑有限重叠。需要的容量定理是：

**Input PI-Lac.** 对任一固定模板 lacunary 族，

`Σ_{j∈lac} R_j <= Δ/log^{B_PI}X`

或触发 `CE/LSMP/LV/FCT/SC`。

该输入通常由 Mellin 支撑有限重叠、Bessel/Parseval 和固定模板复杂度给出。若最终论文接受 PI-Lac，则 lacunary 部分满足 AEX-1。

## 4. Dense Carleson 投影容量

dense pack 满足固定模板下的 Carleson/square-function 上界。需要的容量定理是：

**Input PI-Dense.** 对任一 fixed-template dense pack，

`Σ_{j∈dense} R_j <= Δ/log^{B_PI}X`

或触发 `CE/LSMP/LV/FCT/SC/DSO` 或容量矛盾。

该输入是 `docs/rh-gee-dense-carleson-load-bridge.md` 调用的 `PC4-PI-Dense` 核心。AEX-1 的审稿要求是：PI-Dense 必须在所有允许模板上只损失 `log^C X`，不得隐藏幂级包数。

## 5. AEX-1 条件闭合定理

**Theorem AEX-1.** 假设 AEX1-Baseline、PI-Lac、PI-Dense、NoReturn 失败边和 Transfer-Accounting 均成立，则

`Excess_PI <= Δ/log^{B_final}X=o(Δ)`。

**证明。** 对允许 PI 投影包作 lacunary/dense 二分。Baseline Lemma 将负担改写为超额余量 `R_j` 之和。lacunary 部分由 PI-Lac 控制，dense 部分由 PI-Dense 控制。所有适用条件失败由 NoReturn 进入命名出口，并由 Transfer-Accounting 从 PI 删除。有限模板、dyadic 层和投影重叠的总损失并入 `C_total`，选择 `B_PI>=B_final+C_total` 后得到 `o(Δ)`。证毕。

## 6. 审稿结论

AEX-1 已被压缩为两个可引用容量输入：`PI-Lac` 与 `PI-Dense`。若这两个输入在最终 LaTeX 中以正式定理给出或精确引用，则 AEX-1 可勾选完成。当前不能把 AEX-1 视为无条件完成，因为 `PI-Dense` 的全模板 Carleson 容量仍需逐行定理化。
