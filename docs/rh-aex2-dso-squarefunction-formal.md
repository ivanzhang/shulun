# AEX-2 DSO square-function 总量不等式正式化审查

本文专攻 `docs/rh-analytic-exit-reduction-table.md` 中的 AEX-2：DSO 新增频率包的无幂损失 square-function 总量。本文把 AEX-2 拆成纯正交账本、误差/逃逸转出、以及仍需容量输入的 dense pack 控制。

## 1. AEX-2 目标

对新增频率包集合 `Ω`，目标为

`Σ_{ω∈Ω}|S_ω|^2 <= log^C X · Cap_0(Ω)+Δ^2/log^{B_DSO}X`，

并在扣除零频或允许容量基线 `Cap_0` 后得到

`Excess_DSO <= Δ/log^{B_DSO}X`

或转入命名出口。

## 2. 正交账本

每个 DSO 包由固定复杂度 CRT/Bohr 标签有限交生成。将尺度窗口拉回 inverse-limit CRT 空间，写成

`F_j=E_{k_j}F+err_j`。

新增坐标部分为 martingale difference `D_{k_j}F` 的有限频率子包。若 `P_{Ω_j}` 为该子包投影，则有限群 Parseval 给

`Σ_{Ω_j at level k} ||P_{Ω_j}D_kF||_2^2 <= ||D_kF||_2^2`。

固定复杂度 frame 与平滑边界只造成 `log^C X` 损失。因此

`Σ_j ||P_{Ω_j}F_j||_2^2 <= log^C X · Σ_k ||D_kF||_2^2 + Σ_j ||err_j||_2^2`。

## 3. 误差与逃逸

若 `Σ_j||err_j||_2^2 > Δ^2/log^{B}X`，则误差本身不是 DSO 终态，而进入 `CE/LSMP/LV`。若频率包不是固定复杂度允许标签有限交，则进入 `CE`。若包重叠超过 `log^C X`，则进入 `SC/LV`。这些转出由 Transfer-Accounting 删除源 DSO 状态。

因此非逃逸分支满足

`Σ_j ||P_{Ω_j}F_j||_2^2 <= log^C X · Σ_k ||D_kF||_2^2 + Δ^2/log^B X`。

## 4. DSO 容量输入

剩余需要的容量输入是：

**Input DSO-SF.** 对所有允许 DSO 层，martingale square-function 基线满足

`Σ_k ||D_kF||_2^2 <= Cap_0(Ω)+Δ^2/log^{B}X`，

或触发 `PI/FCT/NRC/CE/LSMP`。

该输入是 AEX-2 的真正数学核心。若它成立，则 AEX-2 成立；若只证明“能量反馈到 PI”而不给二次总量上界，则 AEX-2 仍未完全闭合。

## 5. AEX-2 条件闭合定理

**Theorem AEX-2.** 假设固定复杂度 frame、误差/逃逸转出、Transfer-Accounting 和 DSO-SF 均成立，则

`Excess_DSO <= Δ/log^{B_final}X=o(Δ)`。

**证明。** 第 2 节把 DSO 包平方和控制到 martingale square-function 总量加误差。第 3 节把误差过大、非允许包和高重叠包转入命名出口，源 DSO 状态删除。第 4 节 DSO-SF 控制剩余 square-function 基线；扣除 `Cap_0` 后只剩 `Δ^2/log^B X` 级超额。由 Cauchy/能量到负担转换和全局阈值选择，得到 `Excess_DSO<=Δ/log^{B_final}X=o(Δ)`。证毕。

## 6. 审稿结论

AEX-2 已压缩为单一核心输入 `DSO-SF`。纯 Parseval 正交、误差转出和有限重叠账本已形式化；但 `DSO-SF` 本身仍需在最终稿中逐行证明或精确引用。因此 AEX-2 尚不能勾选为无条件完成。
