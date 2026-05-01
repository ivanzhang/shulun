# PI-Dense 输入最终化：dense 投影容量界归约

本文把 `PI-Dense` 从独立剩余输入改写为 `DSO-C/TC/DSO-E` 组合输入，并进一步归约到当前已经列出的 `DSO-SF` 与 `EXT-KL`。目标是避免在最终剩余表中重复计算 dense Carleson 容量与 DSO square-function 容量。

## 1. 命题

**Theorem PI-Dense-Reduction.** 对 fixed-template dense pack `𝓘`，若以下输入成立：

1. `DSO-C`：CRT martingale square-function 正交；
2. `TC`：固定模板自然细化，失败转 `CE/LSMP/FCT/LV`；
3. `DSO-E-Match`：Euler 局部因子分支由 `EXT-KL/NRC`、`FCT`、`LSMP` 或 `PI-Seed` 接收；
4. `DSO-SF`：martingale square-function 基线容量界；
5. Transfer-Accounting 与低黑箱出口闭合；

则 dense fixed-template Carleson/square-function 容量界成立：

`Σ_{j∈dense} R_j <= Δ/log^{B_PI}X`

或该 dense pack 转入命名出口。

## 2. 证明

在固定模板、平方可和误差和自然细化成立时，dense pack 可拉回 CRT inverse-limit 空间。`DSO-C` 给 martingale difference 正交，`TC` 保证该 fixed-template pack 确实接入 DSO-C；若 TC 失败，则进入 `CE/LSMP/FCT/LV`，不是 PI-Dense 终态。

在接入 DSO-C 后，dense pack 的投影能量由 martingale square-function 控制。此处所需的全局容量化正是 `DSO-SF`：

`Σ_k ||D_kF||_2^2 <= Cap_0 + Δ^2/log^B X`

或触发命名出口。扣除零频容量后，剩余贡献为 `o(Δ)`。

若出现 Euler 局部因子复杂度逃逸，则由 `DSO-E-Match` 处理：非共振部分调用 `EXT-KL/NRC`，共振失败进入 `FCT`，小质量分散进入 `LSMP`，可控多频层返回 DSO-C。所有转出由 Transfer-Accounting 从 PI-Dense 删除。

故 dense pack 不是独立剩余输入；其唯一未闭合的实质输入已包含在 `DSO-SF` 与 `EXT-KL` 中。证毕。

## 3. 审稿结论

`PI-Dense` 可从最终剩余输入表中移除为独立项，改记为依赖：

- `DSO-SF`；
- `EXT-KL` 精确适配；
- 已闭合的 Transfer-Accounting 与低黑箱出口。

因此当前剩余容量输入主要集中到 `DSO-SF`。
