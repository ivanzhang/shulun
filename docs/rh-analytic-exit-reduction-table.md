# 解析出口统一归约表：PI/DSO/NRC 的剩余硬点

本文接续 `docs/rh-local-exit-proofs-formal-appendix.md`。六个低黑箱出口 `LV/CE/LSMP/FCT/SC/A` 已形式化为阈值吸收、内部下降或源删除转出。剩余 `Local-Exit-Proofs` 的真正数学压力集中在三个解析出口：`PI/DSO/NRC`。

本文不伪称它们已经无条件闭合，而是把它们压缩为三条可审稿不等式。若三条不等式全部证明，`Local-Exit-Proofs` 才可整体勾选完成。

## 1. PI/DSO 统一负担公式

由 Baseline-Subtraction，`PI/DSO` 的负担不是零频容量本身，而是

`Load(PI)+Load(DSO) <= Excess_PI + Excess_DSO + Err_named`。

其中 `Err_named` 已由 Transfer-Accounting 转入 `LV/CE/LSMP/FCT/SC/A/NRC` 或吸收。故剩余目标为证明

`Excess_PI + Excess_DSO = o(Δ)`。

## 2. PI/DSO 需要的两个不等式

### AEX-1：无幂损失投影容量不等式

对所有允许投影包 `𝓙`，需有

`Excess_PI(𝓙) <= Δ/log^{B_PI}X`

或触发命名转出。等价地，lacunary 与 dense 两类容量界扣除零频后不能留下 `Δ` 级同向超额。

当前来源：`docs/rh-gee-baseline-subtraction-lemma.md`、`docs/rh-gee-dense-carleson-load-bridge.md`、`docs/rh-pi-dso-maintext-bridge-chain.md`。

尚需正式证明的点：Carleson/square-function 容量界在所有允许模板上只损失 `log^C X`，且适用条件失败必进入命名出口。

### AEX-2：DSO square-function 总量不等式

对新增频率包 `Ω`，需有

`Σ_{ω∈Ω} |S_ω|^2 <= log^C X · Cap_0(Ω) + Δ^2/log^{B_DSO}X`

其中 `Cap_0` 为零频或允许容量基线。扣除 `Cap_0` 后得到

`Excess_DSO <= Δ/log^{B_DSO}X`

或转入 `PI/FCT/LSMP/NRC/CE`。

尚需正式证明的点：Parseval/Carleson 正交化在所有 DSO 入口上无幂损失；不能只给定性分流。

## 3. NRC 需要的一条不等式

### AEX-3：NRC 逐入口参数匹配不等式

对每个 NRC 入口 `r`，需证明以下二择一：

1. 平方根完成和总量小：

   `K_eff,total(r) P_max(r)^{1/2} log^{A_r}X <= Δ/log^{B_NRC}X`；

2. 或 PPI/DSO 可检测偏差门槛严格大于 NRC 上界，导致该入口无法留在 NRC，必须转入 `LV/LSMP/SC/CE/FCT/PI/DSO`。

入口表：

| 入口 | 当前状态 | 剩余 |
|---|---|---|
| 单变量 PPI 倒数包 | 平方根完成和足够 | 外部 `EXT-KL` 精确引用 |
| Tail/RKS NRC | 低体积或主层回流 | 与 LV/主层路由一致性 |
| 双变量 PPI | MidCap 已分流 | 接收出口 `PI/DSO` 与参数门槛 |
| DSO-E 非共振包 | 依赖 DSO-SF | AEX-2 与 `EXT-KL` 参数匹配 |

## 4. 解析出口归约定理

**Theorem Analytic-Exit-Reduction.** 假设 AEX-1、AEX-2、AEX-3 成立，并且 Transfer-Accounting 与六个低黑箱出口命题成立，则

`Load(PI;X)+Load(DSO;X)+Load(NRC;X)=o(Δ)`。

**证明。** Baseline-Subtraction 把 PI/DSO 零频容量从 `Load` 中删除，剩余为 `Excess_PI+Excess_DSO+Err_named`。`Err_named` 由 Transfer-Accounting 转入已闭合低黑箱出口或 NRC。AEX-1 给 `Excess_PI=o(Δ)`，AEX-2 给 `Excess_DSO=o(Δ)`。NRC 的每个入口由 AEX-3 要么直接平方根总量小于 `Δ/log^B X`，要么转入命名出口；转出项不再计入 NRC。因此三解析出口总负担为 `o(Δ)`。证毕。

## 5. 当前审稿状态

本文将三解析出口的剩余义务压缩为 AEX-1、AEX-2、AEX-3 三条不等式。当前不能把 `Local-Exit-Proofs` 标记为全部完成；但可以把剩余任务明确为：

1. 严写 AEX-1；
2. 严写 AEX-2；
3. 严写 AEX-3；
4. 最后做 `EXT-Precision` 与 `Review-Form-Elimination`。
