# Local-Exit-Proofs 形式化附录（一）：低黑箱出口闭合与解析硬出口隔离

本文推进 `docs/rh-unconditional-final-gap-audit.md` 中的 `Local-Exit-Proofs`。目标是把九出口拆成可逐条审稿的命题，并诚实区分：哪些出口仅依赖阈值、势函数、转移账本即可闭合；哪些出口仍依赖外部解析输入或未完全展开的容量定理。

## 1. 统一前提

全篇使用 `docs/rh-transfer-accounting-formal-appendix.md` 的路由账本。设

`Load(E;X)=Σ_{a,s routed finally to E} θ(a,E,s)Excess(a)`。

所有吸收阈值统一由 `docs/rh-gee-threshold-constant-table.md` 给出：若某入口满足

`Mass_eff(a) log^{C_E}X <= Δ/log^{B_E}X`,

且 `B_E>=B_final+C_total`，则该入口总贡献为 `o(Δ)`。

## 2. 可无外部黑箱闭合的六个出口

### 2.1 LV

**Proposition LV.** 真正登记为 `LV` 的原子满足相对主异常低体积阈值，则 `Load(LV;X)=o(Δ)`。

**证明。** 对每个 LV 原子，平凡体积估计给 `Excess(a)<=Mass_eff(a)log^{C_LV}X<=Δ/log^{B_LV}X`。有限入口数、dyadic 层和路由重叠总损失被 `C_total` 支配，故总和 `<=Δ/log^{B_final}X=o(Δ)`。不满足阈值者按定义转出，不计入 LV。证毕。

### 2.2 CE 与 LSMP

**Proposition CE/LSMP.** CE/LSMP 中满足小质量、coarea、薄层、平方可和或复杂度可吸收阈值的部分贡献为 `o(Δ)`；不满足者由 Transfer-Accounting 唯一转出。因此最终登记在 `CE/LSMP` 的负担为 `o(Δ)`。

**证明。** 可吸收部分由统一阈值求和给 `o(Δ)`。不可吸收部分不是 CE/LSMP 终态，而是按 seed 表转入 `A/PI/FCT/SC/LV/DSO/NRC`，源状态权重被删除。由 Transfer-Accounting，不会在 CE/LSMP 与目标出口双计，且有限重叠只贡献 `log^{C_transfer}X`。证毕。

### 2.3 FCT

**Proposition FCT.** 若 FCT Noether 势函数有下界且每个真闭包步严格下降，则 `FCT` 无最终未处理负担。

**证明。** 进入 FCT 的原子沿规范状态递推。真闭包步只作为内部下降，不登记最终 `Load(FCT)`；势函数离散有下界，故真下降有限。若出现旧 span 外新频率，则转入 `NRC/DSO/PI`；若出现重复规范状态，则转入 `PI/SC/LV/LSMP/DSO/CE`；若低体积或短簇条件出现，则转入 `LV/SC/LSMP`。Transfer-Accounting 删除源状态并控制重叠。因此无叶节点最终停留在 FCT，`Load(FCT;X)=0`。证毕。

### 2.4 SC

**Proposition SC.** 若 SC 局部容量阈值、短簇递归势函数下降和重复模板转出机制成立，则最终登记在 `SC` 的负担为 `o(Δ)`。

**证明。** 满足局部容量阈值的短簇项由统一阈值吸收。非吸收项若是真短簇递归，则物理长度、Bohr 体积、锚自由度或 dyadic 高度之一严格下降，作为内部路由不登记最终负担；下降有限。终止而未吸收时，必为重复短簇模板或容量失败，转入 `A/PI/FCT/LV/LSMP/CE` 或容量矛盾。由 Transfer-Accounting 去重。证毕。

### 2.5 A

**Proposition A.** 若 ACC 同步势函数下降和固定模板重复转出机制成立，则最终登记在 `A` 的负担为 `o(Δ)`。

**证明。** 可吸收 ACC 过剩由阈值吸收。非吸收真同步步使 `𝓐pot` 下降，作为内部路由不计最终负担；下降有限。若递推终止且未吸收，则固定 ACC 模板重复同向过剩，按 A-L1 转入 `PI/FCT/SC/LV/LSMP/DSO/CE`。Transfer-Accounting 确保 A 源状态删除且有限重叠。故 A 无最终未处理负担。证毕。

## 3. 仍需解析输入的三个出口

### 3.1 PI

`PI` 的最终上界依赖投影容量、lacunary/dense 二分、Carleson/square-function 型估计与 Baseline-Subtraction。Baseline-Subtraction 是账本定理；真正解析输入是 dense/lacunary 容量上界和异常 `L^2` 控制。

当前状态：可作为条件闭合出口，不应标为完全无条件闭合。

### 3.2 DSO

`DSO` 需要新增频率包的 square-function/Parseval 总量界，并保证失败项进入 `PI/FCT/LSMP/NRC/CE`。这属于解析容量输入，不由 Transfer-Accounting 自动给出。

当前状态：条件闭合，需 `DSO-SF` 无幂损失版本。

### 3.3 NRC

`NRC` 的单变量非共振倒数包可由平方根完成和闭合；双变量 PPI 与 DSO-E 非共振包仍需逐入口参数匹配。若出现幂级自由度因子，单变量完成和不能闭合。

当前状态：单变量/Tail 层可闭合；双变量/DSO-E 仍是解析硬缺口。

## 4. Local-Exit-Proofs 当前结论

九出口中：

- 已由本附录形式化闭合或化为内部转移的出口：`LV/CE/LSMP/FCT/SC/A`；
- 仍需解析或容量输入的出口：`PI/DSO/NRC`。

因此 `Local-Exit-Proofs` 已部分完成，但不能整体勾选为无条件完成。剩余最小数学硬点压缩为：

1. `PI/DSO` 的无幂损失容量与 square-function 上界；
2. `NRC` 双变量与 DSO-E 逐入口参数匹配；
3. 外部定理精确适配；
4. 所有 review-form proof 的正式化。
