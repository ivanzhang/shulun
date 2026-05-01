# DSO-SF 输入最终化：martingale square-function 基线容量界

本文专攻最终剩余容量输入 `DSO-SF`。结论：在固定模板自然细化（TC）与误差/复杂度失败已转出后，`DSO-SF` 本身是 Hilbert 空间 martingale square-function 定理，可在文内无外部黑箱证明。其容量基线应定义为

`Cap_0(Ω)=||F-E_0F||_2^2`

或对应允许投影子空间的零频扣除后 `L^2` 容量。

## 1. 命题

**Theorem DSO-SF.** 设 `F∈L^2(G_∞)`，`𝔽_k` 为 CRT 逆极限概率空间的递增 σ-代数，`E_kF=E(F|𝔽_k)`，`D_kF=E_kF-E_{k-1}F`。则

`Σ_k ||D_kF||_2^2 <= ||F-E_0F||_2^2`。

若固定复杂度 DSO 包 `Ω` 由各层 martingale difference 的正交子投影组成，且 frame 重叠至多 `log^C X`，则

`Σ_{ω∈Ω} |S_ω|^2 <= log^C X · Cap_0(Ω) + Err_tail`。

其中 `Err_tail` 若不满足 `<=Δ^2/log^B X`，则进入 `CE/LSMP/LV`，不留在 DSO。

## 2. 证明

条件期望 `E_k` 是 Hilbert 空间 `L^2(G_∞)` 到闭子空间 `L^2(𝔽_k)` 的正交投影。对 `j<k`，`D_jF` 是 `𝔽_j` 可测，且 `D_kF` 与 `𝔽_{k-1}` 正交；因 `𝔽_j⊂𝔽_{k-1}`，得

`<D_jF,D_kF>=0`。

于是对任意 `N`，

`||E_NF-E_0F||_2^2=Σ_{k<=N}||D_kF||_2^2`。

令 `N→∞`，由 `L^2` martingale 收敛，`E_NF→F`，故

`Σ_k||D_kF||_2^2<=||F-E_0F||_2^2`。

若 `P_{Ω,k}` 是第 `k` 层固定复杂度频率子包的正交投影，则

`Σ_{Ω at k} ||P_{Ω,k}D_kF||_2^2 <= log^C X ||D_kF||_2^2`，

其中 `log^C X` 只来自有限 frame 重叠；若重叠超出多对数，则按定义进入 `SC/LV/CE`。对 `k` 求和即得 DSO 包平方函数界。模板拉回误差 `err_k` 平方可和时并入 `Err_tail`；不可和时进入 `CE/LSMP/LV`。证毕。

## 3. 对 AEX-2/AEX-3 的影响

AEX-2 所需的 `DSO-SF` 已完成：新增频率包的平方和由零频扣除后的 martingale 容量控制，超额项由阈值吸收，失败项转命名出口。

AEX-3 中 DSO-E 入口对 `DSO-SF` 的依赖也随之解除；剩余只需 `EXT-KL` 对非共振 Kloosterman/Weil 完成和作精确引用。

## 4. 审稿结论

`DSO-SF` 可在最终剩余输入表中勾选完成。当前真正剩余输入只剩：

1. `EXT-Precision`；
2. `Review-Form-Elimination`。
