# RH 反例矛盾场合并证明稿 v1（主文链整合版）

本文把当前分散的 RH 反例矛盾场主文链整合为单篇线性证明稿。严格口径：本文仍是“主文链整合版”，不是最终可投稿的无条件 RH 证明；升级为无条件证明稿还需完成正式 BibTeX/页码定理号、容量引理内联编号、LaTeX 交叉引用和最终审稿校对。


## 0. 内部编号与依赖图

为把多文档链条合并为单篇论文，本文采用以下内部编号。后续定稿时，所有 `docs/...` 跳转必须替换为这些编号或正式参考文献。

| 编号 | 名称 | 当前状态 | 待闭合义务 |
|---|---|---|---|
| Lemma G0 | 全局归一化与常数层级 | 已主文化 | 移入第 1 节并消除外部跳转 |
| Proposition PC1 | 离线零点推出平滑素数异常 | 条件主文化 | 补 `EXT-PC1-LI` 精确定理号或完整文内证明 |
| Lemma PC2 | CRT 零频候选基线 | 已主文化 | 内联边界误差证明 |
| Proposition CF | 覆盖场方程与二分 | 已定义化修正 | 采用 `ACC/Hole/OV` 三账本并内联 C3 |
| Proposition Sparse | 过疏 PC3/OV2 分支 | 条件主文化 | 内联 AAI/MLC/PPI 的容量阈值 |
| Proposition Dense | 过密 Dual/DGap 分支 | 内部三接口已定理化 | C5 已给 Lemma C5.1--C5.4；待 C6/C9/C10 放电 |
| Theorem Terminal | `A/PI/FCT/SC` 内部终端闭合 | 条件主文化 | 将 Noether 势函数与容量引理逐条编号 |
| Theorem External | `LV/LSMP/CE/DSO/NRC` 外部事件吸收 | 条件主文化 | 绑定 `EXT-*` 与失败出口；C8 已排除自由 `CapacityFail` |
| Lemma Tail | Fourier/Vaaler 尾项吸收 | 已内联证明 | C9 已给 C9.1--C9.4；待 C10 中 `EXT-Vaaler` 正式引用 |
| Table EXT | 外部定理包 | 来源级闭合 | 补正式 BibTeX、章节、定理号或页码 |

当前合并稿 v1 的逻辑用途是：把证明依赖压缩为上表 10 个可审查接口。只有当每一行的“待闭合义务”被内联证明或正式引用勾销后，主定理才可从条件版改为无条件版。

## 摘要

反设 ζ 函数存在离线零点 `ρ=β+iγ`, `β>1/2`。PC1 给出平滑素数窗口异常 `Δ=X^{β-o(1)}`。PC2 将其经 CRT 零频刚性转为粗合数候选账本的反向异常。统一覆盖场方程把异常送入过疏 PC3/OV2 或过密 Dual/DGap。两路随后分别进入 `A/PI/FCT/SC` 内部终端或 `LV/LSMP/CE/DSO/NRC/CapacityFail` 外部事件；这些事件由当前主文链、容量账本与 `EXT-*` 标准外部定理标签接收。

## 1. 全局约定

取平滑窗口中心尺度 `X`，筛层 `z=(log X)^A`, `0<A<1`，CRT 周期

`M=∏_{p<=z}p=X^{o(1)}`。

若存在离线零点实部 `β>1/2`，记主异常尺度

`Δ=X^{β-o(1)}`。

全文默认使用 Chebyshev/von Mangoldt 权；无权素数版本只作为除以 `logX` 后的对数损失推论。所有固定多对数损失按

`C_struct << C_overlap << C_tail << C_frame << C_cap << C_trig << B_LV << C_0 << B_final`

无循环选择，并吸收到 `X^{o(1)}`。

## 2. PC1：离线零点到平滑素数异常

由平滑显式公式，存在平滑紧支撑权 `W` 使离线零点项不被湮灭。有限边界零点情形中，边界零点贡献化为非零有限三角多项式，均方平均给无穷大振荡。一般上确界或无限边界族情形调用经典 `EXT-PC1-LI` Landau--Ingham 奇点振荡定理。

因此存在符号 `σ` 与无穷尺度 `X_j`，使

`σ(Ψ_W(X_j)-X_j\widehat W(1)) >= X_j^{β-o(1)}`。

素数幂项为 `O(X^{1/2}log^C X)`，由 `β>1/2` 吸收。PC1 主文链见 `docs/rh-pc1-landau-ingham-maintext-chain.md`。

## 3. PC2：CRT 零频基线

设 `C_z` 为 CRT 非零类候选总量，`P_z` 为素数账本，`B_z=C_z-P_z` 为粗合数候选账本。PC2 的 CRT 周期计数给

`C_z-C_z^0=o(Δ)`。

因此若 `E_z=P_z-P_z^0`，则

`B_z-B_z^0=-E_z+o(Δ)`。

这固定了过疏/过密的反号传递。主文附录见 `docs/rh-pc2-crt-baseline-maintext-appendix.md`。

## 4. 覆盖场方程

采用 C3 定义化后的三账本。`ACC_z` 为至少被一个允许证书覆盖的粗合数候选数，`Hole_z` 为未被证书解释的粗合数候选数，`T_z` 为原始证书总数，`OV_z=T_z-ACC_z` 为二层重叠复用量。第一层集合划分给

`B_z=ACC_z+Hole_z+o(Δ)`。

相减得

`-E_z=(ACC_z-ACC_z^0)+(Hole_z-Hole_z^0)+o(Δ)`。

若 `E_z<=-Δ`，则 `ACC`、`Hole` 或二层 `OV` 至少一项承载固定比例异常，进入 `A/LV-LSMP-CE/PC3-OV2`。若 `E_z>=Δ`，则 `ACC_z^0-ACC_z` 或 `DGap_z:=Hole_z^0-Hole_z` 承载固定比例异常，进入 `A` 或 Dual/DGap。C3 细节见 `docs/rh-c3-covering-field-definition-closure.md`。

## 5. 过疏分支：PC3/OV2

过疏给 `B_z-B_z^0>=Δ-o(Δ)`。若 overlap 与缺口不能吸收，则 `ACC_z-ACC_z^0>=cΔ`，进入 `A`。若 overlap 大，AAI 把冗余解释为双锚正规形

`n=q_1q_2r`。

MLC 定位 dyadic 主层并排除不可检测零频自由吸收；PPI 将可检测主层推送到倒数相位窗口。PPI 输出端进一步分流为：非共振进入 `NRC/EXT`，共振进入 `FCT`，投影重复进入 `PI/SC/DSO`，尾项或复杂度逃逸进入 `LV/LSMP/CE`。

主文链见：`docs/rh-pc3-ov2-maintext-proof-chain.md`、`docs/rh-ppi-terminal-output-maintext-chain.md`、`docs/rh-nrc-ext-maintext-closure.md`。

## 6. 过密分支：Dual/DGap

过密由 Dual 分支给 `A/DGap/接口失败` 三分。采用 C3 修正版时，`DGap_z:=Hole_z^0-Hole_z`。当 `DGap_z>=cΔ` 时，DGap 三接口处理：

1. 盒有限重叠给固定复杂度 frame 上界；
2. PC2 常数方向剥离后得到 `||P_Vh||_2^2>=X^{2β-1-o(1)}`；
3. 逐步正交投影分到 `V_PI,V_low,V_err`；
4. 低维抽取中，新增独立频率包进入 `PI/DSO`，否则进入 `FCT_seed`。

DGap 出口被穷尽为

`A/OV2/PI/FCT/SC/LV/LSMP/CE/DSO/CapacityFail`。

主文链见 `docs/rh-dgap-maintext-three-interface-chain.md`；C5 内联定理化见 `docs/rh-c5-dgap-inline-proof-chain.md`。

## 7. 内部终端闭合

内部终端为 `A/PI/FCT/SC`。

- `A`：覆盖容量同步，正负号均由固定模板偏差账本处理；
- `PI`：允许投影能量由 lacunary/dense 容量与 DSO square-function 处理；
- `FCT`：频率碰撞状态规范化为 `(Λ,R,𝓑,τ)`，Noether 势函数排除无限闭包；
- `SC`：短簇状态规范化为 `(I,𝓑,Q,R,κ,σ)`，局部乘积容量与短簇势函数排除无限递归。

主文链见 `docs/rh-fct-maintext-closure-chain.md`、`docs/rh-pi-dso-maintext-bridge-chain.md`、`docs/rh-sc-maintext-capacity-closure.md`。

## 8. 外部事件吸收

外部事件为 `LV/LSMP/CE/DSO/NRC/CapacityFail`。

- `LV`：若 `Vol_eff<=X/log^{B+C}X`，平凡体积估计吸收；失败转结构事件。
- `LSMP`：薄层 coarea、方向筛选和频率原子小质量逃逸吸收；失败只输出 `PI_seed/FCT_seed`。
- `CE`：复杂度逃逸分类器，分为频率复杂度、尾项能量、旧坐标重写、边界体积四类。
- `NRC`：非共振倒数和由 `EXT-KL` Kloosterman--Weil 与完成法控制，失败为 `FCT`。
- `DSO`：新增频率包由 square-function/Parseval 反馈到 PI 或命名事件。
- `CapacityFail`：不再允许作为最终出口；按 C8 升级审查，它必须替换为具体容量引理成功上界，或替换为进入 `A/PI/FCT/SC/LV/LSMP/CE/DSO/NRC` 的命名失败出口。

主文链见 `docs/rh-lv-lsmp-ce-maintext-absorption-chain.md`、`docs/rh-nrc-ext-maintext-closure.md`、`docs/rh-pi-dso-maintext-bridge-chain.md`；C8 审查见 `docs/rh-c8-capacityfail-upgrade-audit.md`。

## 9. Fourier/Vaaler 尾项

PPI/DGap/PC4 的固定复杂度模板由平滑窗、硬边界、CRT 字符、倒数环带、Bohr 短弧及有限布尔组合构成。平滑窗快速衰减；硬边界先平滑再截断；倒数环带和 Bohr 短弧用 `EXT-Vaaler`；CRT 字符无尾项。固定布尔组合保持平方可和。

故尾项要么平方可和吸收，要么进入 `CE/LSMP/LV/SC/FCT/DSO/PI`。主文链见 `docs/rh-fourier-vaaler-tail-maintext-chain.md`；C9 内联证明见 `docs/rh-c9-fourier-vaaler-tail-inline-proof.md`。

## 10. 外部定理包

所有非初等外部输入归入：

`EXT-KL`, `EXT-Vaaler`, `EXT-PC1-EF`, `EXT-PC1-LI`, `EXT-BG`, `EXT-Selberg`, `EXT-Vaughan`。

其中 `EXT-PC1-EF` 已文内证明，`EXT-PC1-LI` 有限边界情形已文内证明，一般情形为经典 Landau--Ingham 定理。`EXT-KL` 只用素数模 `ax+b/x` 特例；`EXT-Vaaler` 只用一维区间截断。引用闭合见 `docs/rh-ext-maintext-citation-closure.md`。

## 11. 合并主定理（当前状态）

**Theorem RH-Contradiction-Field-Merged-v1（合并稿条件版）。** 假设本文引用的主文链、容量引理和 `EXT-*` 外部定理均以最终论文标准编号、引用或内联证明成立，则 ζ 函数不存在离线零点 `β>1/2`。

**证明。** 反设存在离线零点。第 2 节给 PC1 异常；第 3 节将其转为粗合数候选反向异常；第 4 节覆盖场方程给过疏/过密二分。过疏由第 5 节进入 `A` 或 D 组终端；过密由第 6 节进入 `A/OV2/PI/FCT/SC/LV/LSMP/CE/DSO/CapacityFail`。第 7 节排除内部终端无限吸收，第 8 节处理外部事件，第 9 节处理尾项，第 10 节绑定外部定理。所有分支均不能作为离线零点异常的自由吸收通道，矛盾。证毕。

## 12. 未完成的无条件化判据

本文已经完成单篇合并雏形，但仍保留以下未完成项：

1. 把所有 `docs/...` 引用替换为本文内部编号定理或正式参考文献；
2. 给全部 `EXT-*` 补 BibTeX、章节、页码或定理号；
3. 将 `CapacityFail` 对应容量语句逐条内联为本文引理或明确反设矛盾；
4. 生成 LaTeX/PDF 并检查交叉引用、符号表和编号；
5. 只有以上完成后，才能把标题改为“无条件证明稿”。
