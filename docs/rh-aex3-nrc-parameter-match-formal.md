# AEX-3 NRC 逐入口参数匹配正式化审查

本文专攻 `docs/rh-analytic-exit-reduction-table.md` 中的 AEX-3：NRC 逐入口参数匹配。目标是把 `GEE-NRC` 从泛泛“条件参数闭合”改写为四个入口的明确审稿表。

## 1. AEX-3 判定准则

每个 NRC 入口 `r` 必须满足二择一：

1. **Sqrt-Sum：**

   `K_eff,total(r) P_max(r)^{1/2} log^{A_r}X <= Δ/log^{B_NRC}X`；

2. **Dominance/Transfer：** PPI 或 DSO 的可检测偏差门槛大于 NRC 上界，因此该入口不能留在 NRC，必须转入 `LV/LSMP/SC/CE/FCT/PI/DSO`。

若二者都无法证明，则 NRC 出口未闭合。

## 2. 四入口参数表

| 入口 | 判定 | 证明义务 |
|---|---|---|
| 单变量 PPI 倒数包 | Sqrt-Sum 成立 | `K_eff,total=log^C X`, `P_max<=X`, 故 `X^{1/2}log^C X=o(Δ)` |
| Tail/RKS NRC | Transfer 成立 | 低体积进 `LV`；非低体积回主层 PPI，不作为独立 NRC 主入口 |
| 双变量 PPI | Transfer 成立，非直接 NRC | 高容量相对小，低体积进 `LV`，中间容量由 MidCap 转 `LSMP/SC/PI/DSO/CE` |
| DSO-E 非共振包 | 条件：依赖 AEX-2/DSO-SF | 若 DSO-SF 成立，则包数平方和无幂损失；否则不能闭合 |

## 3. 单变量入口证明

单变量包总量为多对数个完成和，每个满足 `EXT-KL` 型上界

`<=P^{1/2}log^A P`。

因 `P<=X` 且 `β>1/2`，有

`X^{1/2}log^C X=o(X^{β-o(1)})=o(Δ)`。

故单变量入口闭合，前提是 `EXT-KL` 精确引用成立且窗口复杂度确为多对数。

## 4. Tail/RKS 入口证明

Tail/RKS 若满足相对低体积阈值，则由 `LV` 吸收；若不满足，则其定义上不再是尾层 NRC，而回到主层 PPI/MLC 账本。由 Transfer-Accounting，转出后不计入 NRC。故 Tail/RKS 不是独立 NRC 主负担。

## 5. 双变量 PPI 入口证明状态

二维加性分离入口不应通过对一个变量完成、另一个变量平凡求和来闭合，因为这会产生 `Q·P^{1/2}` 的幂级损失。当前安全路线是：

- `PPI-Rank` 给有限分离秩；
- `Capacity-Match` 分高容量、低体积、中容量；
- `MidCap-Structure` 把中容量转入 `LSMP/SC/PI/DSO/CE`。

因此双变量 PPI 入口作为 NRC 自身是 Transfer 闭合，而不是 Sqrt-Sum 闭合。它的剩余压力已经转移到 `PI/DSO` 与低黑箱出口；低黑箱出口已处理，`PI/DSO` 依赖 AEX-1/AEX-2。

## 6. DSO-E 入口证明状态

DSO-E 非共振包若满足 AEX-2 的 `DSO-SF`，则 Cauchy 与 square-function 给多对数总复杂度，进而落入 Sqrt-Sum 条件。若 `DSO-SF` 未证明，则 DSO-E 不能标记为 NRC 闭合。

## 7. AEX-3 条件闭合定理

**Theorem AEX-3.** 假设：

1. `EXT-KL` 对单变量倒数包精确适用；
2. 单变量窗口复杂度为多对数；
3. Tail/RKS 路由与 LV/主层回流一致；
4. 双变量 PPI 按 `PPI-Rank + Capacity-Match + MidCap` 转出；
5. DSO-E 满足 `DSO-SF` 或转入 `PI/FCT/CE/LSMP`；

则

`Load(NRC;X)=o(Δ)`。

**证明。** 单变量入口由第 3 节直接给 `o(Δ)`。Tail/RKS 由第 4 节转出或吸收，不留在 NRC。双变量入口由第 5 节转出，不作为 NRC 终态。DSO-E 由第 6 节在 `DSO-SF` 成立时满足 Sqrt-Sum，否则按假设转出。所有转出由 Transfer-Accounting 从 NRC 删除。故最终 NRC 负担为 `o(Δ)`。证毕。

## 8. 审稿结论

AEX-3 已压缩为两个尚需外部/上游支持的输入：

1. `EXT-KL` 的精确引用与变量匹配；
2. `DSO-SF`，因为 DSO-E 入口依赖 AEX-2。

双变量 PPI 不再是独立 NRC 解析硬点，而是通过 MidCap 转移到 PI/DSO 与低黑箱出口。
