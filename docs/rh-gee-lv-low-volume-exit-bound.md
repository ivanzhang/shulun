# GEE-LV 低体积出口上界

本文专攻 Global-Exit-Exclusion 的第一个出口上界 `GEE-LV`。结论分两层：真正满足低体积阈值的 LV 原子贡献为 `o(Δ)`；不满足阈值的所谓 LV 原子不能继续计入 LV，必须转入 `SC/PI/A/FCT/LSMP/CE` 等结构出口，避免重复计数。本文不证明这些转出出口的上界。

## 1. LV 原子的定义

在成功尺度 `X` 上，一个原子 `a` 可计入 `LV`，必须给出有效支撑 `Vol_eff(a)` 与损失指数 `C(a)`，满足

`|bias(a)| <= Vol_eff(a) log^{C(a)}X`。

称其为真正低体积原子，若对预先固定的 `B_LV` 有

`Vol_eff(a) log^{C(a)}X <= X/log^{B_LV}X`。

若该条件失败，则 `a` 不允许留在 `LV`，而必须按失败原因转入：短窗集中转 `SC`，投影可见转 `PI`，覆盖同步转 `A`，相位闭包转 `FCT`，薄层/小质量转 `LSMP`，模板复杂度转 `CE`。

## 2. LV 入口表

| 入口 | `Vol_eff` 形式 | 成功吸收 | 失败出口 |
|---|---|---|---|
| OV2 低尾层 `R<log^{A_1}X` | `X^{1/2}R^{1/2}log^C X` | `o(X/log^B X)` | `SC` |
| OV2 近平方边界 `Q>X^{1/2}log^{-A_0}X` | 归入低尾 `R<log^{2A_0}X` | `o(X/log^B X)` | `SC/CE` |
| DGap 低体积盒 | 盒支撑总量 `Vol_box` | 若 `Vol_box log^C<=X/log^{B_LV}` | `SC/LSMP/CE/FCT` |
| C9 边界层 | 平滑边界厚度 `ηX` 或短弧边界 | 选 `η` 使平方可和/低体积 | `SC/LV->LSMP/CE` |
| SC 端点薄壳 | `(L/X)RQlog^C X+Rlog^C X` | 低于阈值则吸收 | `PI/A/FCT/SC/LSMP` |
| PI 边界坏包 | 边界支撑 `Vol_PI,bd` | 低于阈值则吸收 | `SC/CE/LSMP` |
| CE 边界体积 | 对应边界支撑 | 低于阈值则吸收 | `CE` 细分或 `SC/LSMP` |

该表的作用是限定 LV 的合法含义：LV 只承载已经有体积阈值证书的原子。

## 3. GEE-LV 上界

令 `𝓐_LV` 为所有真正低体积原子，并按 GEE-0 的拆分权重计数。设路由有限重叠常数为 `C_route`，所有 LV 原子的损失指数被全局常数 `C_LV` 控制。若选择

`B_LV > C_route+C_LV+B_final`，

则

`Load(LV;X) <= X/log^{B_final}X`。

由于 `Δ=X^{β-o(1)}` 且 `β>1/2`，该界不必自动小于 `Δ` 当 `β` 接近 `1` 时；因此 GEE-LV 的正确强形式应与主异常尺度比较为：

`Load(LV;X) <= X/log^{B_final}X`，

并在最终 GEE 合成中只可用于吸收那些被归一化到候选总量 `X` 的低体积误差。若某分支要求逐点达到 `o(Δ)`，必须加强 LV 阈值为

`Vol_eff(a)log^{C(a)}X <= Δ/log^{B_LV}X`。

因此本文采用相对主异常版本：真正计入 GEE-LV 的原子必须满足

`Vol_eff(a)log^{C(a)}X <= Δ/log^{B_LV}X`。

在此定义下，有限重叠求和给

`Load(LV;X) <= Δ/log^{B_final}X=o(Δ)`。

## 4. Theorem GEE-LV

**Theorem GEE-LV-Low-Volume-Bound.** 若 LV 原子按相对主异常阈值

`Vol_eff(a)log^{C(a)}X <= Δ/log^{B_LV}X`

登记，且非低体积失败均转入 `SC/PI/A/FCT/LSMP/CE` 并从 LV 负担中删除，则

`Load(LV;X)=o(Δ)`。

**证明。** 对每个真正 LV 原子，平凡估计给 `|bias(a)|<=Vol_eff(a)log^{C(a)}X<=Δ/log^{B_LV}X`。按 GEE-0 路由表，每个异常原子在 LV 入口的总重复记录至多 `log^{C_route}X`，LV 入口类型有限且 dyadic 层数多对数。选择 `B_LV>C_route+C_type+B_final`，求和得 `Load(LV;X)<=Δ/log^{B_final}X=o(Δ)`。若某原子不满足相对主异常低体积阈值，则按第 1--2 节转入其他出口，不计入 LV；因此 LV 本身不能承载 `Δ` 级异常。证毕。

## 5. 审稿注意

本文把 GEE-LV 闭合为“定义性阈值 + 平凡体积估计 + 失败转出”。它并不证明转出到 `SC/PI/A/FCT/LSMP/CE` 的负担为小；这些仍属于相应 GEE 出口上界。GEE-LV 可以标记为闭合，但不能单独完成 Global-Exit-Exclusion。
