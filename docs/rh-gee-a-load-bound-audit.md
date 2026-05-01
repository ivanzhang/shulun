# GEE-A 负担上界审查：ACC 同步、势函数下降与 seed 转出

本文专攻 `GEE-A`。A/ACC 分支记录覆盖同步或正向过剩容量。现有 `docs/rh-pc4-acc-sync-ledger.md` 已证明：ACC 同步不能形成无限自循环；若固定模板重复同向过剩，则转入 `PI/FCT/SC/LV/LSMP/DSO/CE`。本文把该结构转写为 GEE 出口负担口径。

## 1. A 的正确 GEE 口径

A 分支不是最终自由出口，而是 ACC 同步压力的内部账本。将进入 A 的原子分为：

- `Load_abs(A;X)`：过剩容量已被零频基线、低体积或平方容量预算吸收的部分；
- `Seed_sync(A;X)`：真 ACC 状态变化，作为内部同步转移；
- `Seed_rep(A;X)`：固定 ACC 模板重复过剩，转入 `PI/FCT/SC/LV/LSMP/DSO/CE`。

最终 GEE-A 只登记无法吸收、无法转移的 ACC 终态；ACC-Sync-No-Cycle 说明这种终态不存在。

## 2. 可吸收 ACC 项

若 ACC 过剩容量满足相对异常阈值

`Excess_ACC log^C X <= Δ/log^{B_A}X`，

则由平凡容量或对应 square-function/零频预算吸收，给 `o(Δ)`。若过剩来自低体积切片、边界或小质量层，则转入 `LV/LSMP`，不保留在 A。

## 3. 非吸收 ACC 的内部转移/转出

非吸收 ACC 只可能有两类。

1. **真 ACC 同步变化。** 模板复杂度、Bohr/CRT 体积、dyadic 层或过剩容量账本发生真变化。若变化可留在 A 内，则 ACC 势函数 `𝓐pot` 下降；否则转 `CE/FCT/LSMP/LV/SC`。真变化作为内部路由，不计最终 `Load(A)`。
2. **固定模板重复。** 同一 ACC 模板在无穷尺度上重复同向过剩。由 A-L1，必触发 `PI/FCT/SC/LV/LSMP/DSO/CE`。

势函数有下界，故真内部变化有限；终止时若未吸收，必为固定模板重复并转出。

## 4. Theorem GEE-A-Transfer

**Theorem GEE-A-Transfer.** 假设 ACC-Sync-No-Cycle、Seed-Transfer 去重账本和 PI/FCT/SC/LV/LSMP/DSO/CE 接收出口成立。则可以重定义 GEE 路由，使：

1. 可吸收 ACC 项贡献 `Load_abs(A;X)=o(Δ)`；
2. 真 ACC 同步步作为内部路由，不计最终 `Load(A)`；
3. 固定模板重复过剩转入 `PI/FCT/SC/LV/LSMP/DSO/CE`；
4. seed 转出不再重复计入 A；
5. 最终留在 A 的未处理负担为零。

因此在该路由定义下，

`Load(A;X)=o(Δ)`。

**证明。** 对进入 A 的异常原子，先检查可吸收容量阈值。满足阈值者给 `o(Δ)`。否则沿规范 ACC 状态递推。每个真同步步使 `𝓐pot` 下降或转出；由于势函数有下界，真内部步有限。若递推终止且未吸收，则同一规范 ACC 模板重复承载同向过剩，由 A-L1 转入 `PI/FCT/SC/LV/LSMP/DSO/CE`。Seed-Transfer 保证转出有限重叠且从 A 删除。故 A 无最终未处理负担。证毕。

## 5. 对 Global-Exit-Exclusion 的影响

结合此前文档：

- `LV/NRC/PI/DSO/CE/LSMP/FCT/SC` 已分别被写成低体积吸收、非共振上界、基线扣除、seed 转出或内部转移；
- 本文把最后显性 `A` 出口也改写为容量吸收 + 内部同步转移；
- 因而九个 GEE 出口均已有对应的 `o(Δ)` 或转出闭合口径。

剩余工作不应再声称“RH 已证明”，而应进入最终总审查：逐项检查这些条件闭合是否存在循环依赖、是否有 seed 未接收、是否所有 `o(Δ)` 阈值使用同一 `Load` 口径。
