# RH 反例矛盾场论文整合稿（条件化定稿版）

本文整合当前仓库中关于 RH 反例矛盾场的 PC1--PC4、Dual/DGap、容量矩阵与常数层级文档。必须明确：本文当前给出的是一条高度结构化的条件化闭合证明链；只有当文中列出的外部解析输入、容量定理与 PC4 终端接口全部以标准定理或逐行证明方式无条件化后，才能升级为 RH 的无条件证明。本文不在当前版本中宣称 RH 已证明。

## 摘要

反设 ζ 函数存在离线零点 `ρ=β+iγ`，`β>1/2`。PC1 将该零点转化为平滑素数窗口异常 `X^{β-o(1)}`；PC2 利用 CRT 零频候选总量刚性，将素数异常投影为粗合数候选账本的反向异常；PC3/OV2 把过疏异常送入允许覆盖过剩或 D 组终端；PC4 通过 A/PI/FCT/SC 事件图、外部吸收矩阵、Dual/DGap 三接口和容量常数层级，排斥所有可持续吸收通道。最终得到：在所有列明接口无条件成立时，离线零点反例无处吸收，形成矛盾。

## 1. 反例输入与 PC1 解析异常

PC1 的精确输入是：若存在 `ρ=β+iγ`，`β>1/2`，则存在平滑紧支撑权 `W`、符号 `σ` 与无穷尺度 `X_j`，使

`σ(Ψ_W(X_j)-X_j\widehat W(1)) >= X_j^{β-o(1)}`。

该输入被标准化为：

- 文内平滑显式公式证明：`docs/rh-pc1-explicit-formula-proof-appendix.md`；
- Landau--Ingham 振荡拆分：`docs/rh-pc1-landau-ingham-oscillation-appendix.md`；
- Landau--Ingham 主文链：`docs/rh-pc1-landau-ingham-maintext-chain.md`；
- 权函数非湮灭；
- 素数幂去除；
- Chebyshev 权到无权口径的对数损失。

引用与标准化入口见：

- `docs/rh-pc1-analytic-input-citation-audit.md`；
- `docs/rh-pc1-external-input-standardization-audit.md`。

## 2. PC2：CRT 零频基线刚性

取 `z=(log X)^A`。CRT 候选总量满足

`C_z(X)=C_z^0(X)+o(Δ)`, `Δ=X^{β-o(1)}`。

因此素数异常不能由候选总量自身吸收，只能转为粗合数候选账本反向异常：

`B_z-B_z^0=-E_z+o(Δ)`。

主文证明附录见：

- `docs/rh-pc2-crt-baseline-maintext-appendix.md`；
- `docs/rh-pc2-baseline-unconditional-audit.md`；
- `docs/rh-pc2-crt-baseline-explicit.md`。

## 3. 统一覆盖场方程

允许覆盖、overlap 扣重与缺口账本满足

`B_z=ACC_z-O_z+Gap_z`。

相减得到核心场方程：

`-E_z=(ACC_z-ACC_z^0)-(O_z-O_z^0)+(Gap_z-Gap_z^0)+o(Δ)`。

该方程是反例矛盾场的核心：离线零点异常必须投影到 `ACC`、`O`、`Gap` 三个离散结构场之一。

## 4. 过疏分支

若 `E_z<=-Δ`，则粗合数候选账本过剩。PC3/OV2 给出二分：

1. `ACC` 正向过剩，进入 PC4-A；
2. overlap 大，进入 D 组终端：SC、PI、FCT、NRC、LV/LSMP。

主要入口：

- `docs/rh-pc3-ov2-bridge-theorem.md`；
- `docs/rh-pc3-ov2-maintext-proof-chain.md`；
- `docs/rh-ppi-terminal-output-maintext-chain.md`；
- `docs/rh-nrc-ext-maintext-closure.md`；
- `docs/rh-fct-maintext-closure-chain.md`；
- `docs/rh-pi-dso-maintext-bridge-chain.md`；
- `docs/rh-sc-maintext-capacity-closure.md`；
- `docs/rh-dgap-maintext-three-interface-chain.md`；
- `docs/rh-fourier-vaaler-tail-maintext-chain.md`；
- `docs/rh-lv-lsmp-ce-maintext-absorption-chain.md`；
- `docs/rh-pc3-ov2-upstream-unconditional-audit.md`；
- `docs/rh-ov2-mlc-uniform-capacity-constants-audit.md`。

## 5. 过密分支与 Dual/DGap

若 `E_z>=Δ`，则粗合数候选账本不足。Dual 分支给出：

1. `ACC` 负向同步，进入 PC4-A；
2. overlap 过剩，进入 OV2/D 组终端；
3. `DGap` 压缩异常。

`DGap` 由三接口处理：

- 盒有限重叠；
- 投影正交化；
- 低维频率抽取。

逐行补强入口：

- `docs/rh-dgap-projection-line-by-line-audit.md`；
- `docs/rh-dgap-lowdim-extraction-line-by-line-audit.md`；
- `docs/rh-dso-pi-squarefunction-bridge-audit.md`；
- `docs/rh-pi-dense-dso-bridge-no-return-audit.md`；
- `docs/rh-fct-seed-isomorphism-audit.md`；
- `docs/rh-fourier-vaaler-tail-uniform-audit.md`；
- `docs/rh-fct-closure-no-cycle-final-audit.md`。

## 6. PC4 终端闭合结构

PC4 内部终端为 `A/PI/FCT/SC`。当前文档包已将这些分支写成条件化无循环事件图：

- PC4-A：ACC 不同步排斥；
- PC4-PI：高投影增量容量排斥；
- PC4-FCT：频率闭包 Noether 终止；
- PC4-SC：短簇质量平衡与局部乘积容量。

统一入口：

- `docs/rh-pc4-terminal-final-no-cycle-audit.md`；
- `docs/rh-pc4-external-event-absorption-audit.md`。

## 7. 容量矩阵与常数层级

所有 `CapacityFail` 必须绑定到具体容量文档，不允许作为独立终端。容量接口统一登记为：对象、适用条件、容量界、允许损失、常数余量与失败出口。

当前常数层级采用

`C_struct << C_overlap << C_tail << C_frame << C_cap << C_trig << B_LV << C_0 << B_final`。

任何有限多对数损失均吸收到 `X^{o(1)}`，不会破坏 PC1 的 `X^{β-o(1)}` 主异常。入口：

- `docs/rh-capacityfail-binding-table.md`；
- `docs/rh-capacity-constants-applicability-audit.md`；
- `docs/rh-global-log-constant-hierarchy-audit.md`；
- `docs/rh-ext-maintext-citation-closure.md`；
- `docs/rh-global-normalization-maintext-closure.md`。

## 8. 条件化主定理

**Theorem RH-Contradiction-Field-Conditional.** 假设 PC1、PC2、PC3/OV2、PC4-A/PI/FCT/SC、Dual/DGap、NRC/EXT、LV/LSMP/CE/DSO 与容量矩阵中的所有接口均已按本文引用文档无条件证明或标准外部定理精确引用，则 ζ 函数不存在离线零点 `β>1/2`。

**证明。** 反设存在离线零点。PC1 给出无穷尺度的素数异常；PC2 将其转为粗合数候选账本反向异常；统一覆盖场方程迫使该异常进入 `ACC/O/Gap`。过疏时由 PC3/OV2 进入 PC4-A 或 D 组终端；过密时由 Dual/DGap 进入 PC4-A、OV2 或 SC/PI/FCT/LV/LSMP。PC4 内部终端无循环，外部事件均被吸收或转为已命名容量矛盾。故所有分支均不能长期吸收离线零点异常，矛盾。证毕。

## 9. 仍需无条件化的接口

为达到真正“无条件 RH 证明”标准，仍必须完成以下工作：

1. PC1 显式公式与 Landau--Ingham 主文链已新增 `docs/rh-pc1-explicit-formula-proof-appendix.md` 与 `docs/rh-pc1-landau-ingham-maintext-chain.md`；仍需给一般情形 `EXT-PC1-LI` 补精确书目、章节或定理号；
2. 将 `docs/rh-pc2-crt-baseline-maintext-appendix.md` 合并入主文，并全文统一 Chebyshev 权或无权口径；
3. AAI/PPI/MLC/OV2 已新增连续主文证明链 `docs/rh-pc3-ov2-maintext-proof-chain.md`，PPI 输出端已新增 `docs/rh-ppi-terminal-output-maintext-chain.md`；后续义务是把 MLC、LV 与 D 组终端逐项并入最终主文；
4. 将 PC4-A/PI/FCT/SC 的无循环审查从文档矩阵合并为单篇定理链；
5. NRC/EXT 非共振分支已新增 `docs/rh-nrc-ext-maintext-closure.md`，FCT 无循环闭包已新增 `docs/rh-fct-maintext-closure-chain.md`，PI/DSO 桥接已新增 `docs/rh-pi-dso-maintext-bridge-chain.md`，SC 局部乘积容量已新增 `docs/rh-sc-maintext-capacity-closure.md`，DGap 三接口已新增 `docs/rh-dgap-maintext-three-interface-chain.md`，Fourier/Vaaler 尾项平方可和已新增 `docs/rh-fourier-vaaler-tail-maintext-chain.md`；
6. `LV/LSMP/CE` 外部吸收已新增 `docs/rh-lv-lsmp-ce-maintext-absorption-chain.md`，全局常数/尺度/符号归一化已新增 `docs/rh-global-normalization-maintext-closure.md`；
7. 外部定理引用已新增 `docs/rh-ext-maintext-citation-closure.md`；最终编辑仍需把 `EXT-KL/BG/Vaaler/Selberg/Vaughan/PC1` 替换为正式 BibTeX、页码或定理号；
8. 最终义务转为单篇论文合并、LaTeX 交叉引用、BibTeX 页码定理号和符号表编辑审查。

## 10. 结论

最终合并状态与剩余缺口判定见 `docs/rh-final-merge-status-and-gap-closure.md`。


本文给出一条明确的 RH 反例矛盾场闭合路线：离线零点异常经 PC1--PC2 投影到 CRT 覆盖动力系统后，被统一场方程迫入有限个结构分支；这些分支在当前文档包中已被压缩为可审查的条件化闭合接口。下一步若要真正完成无条件 RH 证明，不是再增加新分支，而是将上述接口逐项改写成单篇论文中的标准定理证明与精确引用。
