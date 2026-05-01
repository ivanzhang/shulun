# RH 反例矛盾场总攻框架

本文把当前 RH 探索路线的 PC1--PC4、PC4-Dual 与 DGap 三接口合并为一个全局“反例矛盾场”审查框架。本文仍不是 RH 的无条件证明；它给出的是：若所有已列解析输入、CRT/覆盖接口与 PC4 closure 均无条件化，则离线零点反例将无处吸收，因而形成矛盾。

## 1. 反例输入

反设存在离线零点 `ρ=β+iγ`, `β>1/2`。由 `docs/rh-pc1-offline-zero-smooth-window.md`，存在平滑窗口、无穷尺度 `X_j` 与异常幅度

`Δ_j=X_j^{β-o(1)}`，

使素数计数相对连续主项出现带符号异常

`E_z(X_j)=P_z(X_j)-P_z^0(X_j)`, `|E_z(X_j)|>=Δ_j`。

这里允许 Chebyshev 权或经对数损失吸收后的无权版本。

## 2. CRT 零频刚性投影

由 `docs/rh-pc2-li-crt-baseline-match.md`，取 `z=(log X)^A`, `A<1`，CRT 候选总量刚性给

`C_z(X)=C_z^0(X)+o(Δ)`。

因此真实粗合数候选账本满足

`B_z-B_z^0=-E_z+o(Δ)`。

这一步把解析零点的连续波动投影到 CRT 筛余候选集合内部：候选总量不能跟随离线零点同幅波动，所以素数异常必须由粗合数/覆盖账本反向补偿。

## 3. 覆盖恒等式与统一矛盾场方程

由 `docs/rh-pc4-dual-gap-ledger.md`，允许覆盖、overlap 扣重与缺口账本满足

`B_z=ACC_z-O_z+Gap_z`，

相减得到统一场方程

`-E_z=(ACC_z-ACC_z^0)-(O_z-O_z^0)+(Gap_z-Gap_z^0)+o(Δ)`。

这就是当前路线的核心矛盾场方程。它把离线零点波动强迫进入三个离散结构场：

1. `ACC`：允许斜线覆盖容量；
2. `O`：多锚 overlap 扣重；
3. `Gap`：真实粗合数但未被允许覆盖解释的缺口。

## 4. 过疏分支

若 `E_z<=-Δ`，则

`B_z-B_z^0>=Δ-o(Δ)`。

由 `docs/rh-pc3-ov2-bridge-theorem.md`，过疏推出：

1. `ACC_z>=ACC_z^0+cΔ`，进入 PC4-A；或
2. overlap 大，触发 D 组终端：SC、PI、FCT、NRC 或 LV/LSMP。

这些终端分别由以下 closure 文档接收：

- `docs/rh-pc4-acc-closure-theorem.md`；
- `docs/rh-pc4-short-cluster-closure-theorem.md`；
- `docs/rh-pc4-pi-closure-theorem.md`；
- `docs/rh-pc4-fct-closure-theorem.md`；
- NRC/EXT 与 LV/LSMP 相关接口文档。

## 5. 过密分支

若 `E_z>=Δ`，则

`B_z-B_z^0<=-Δ+o(Δ)`。

由 `docs/rh-pc4-dual-overdense-closure.md` 与 `docs/rh-pc4-dual-gap-ledger.md`，过密推出三分：

1. `ACC_z^0-ACC_z>=cΔ`：ACC 负向同步，进入 PC4-A；
2. `O_z-O_z^0>=cΔ`：overlap 过剩，进入 OV2/D 组终端；
3. `DGap_z=Gap_z^0-Gap_z>=cΔ`：对偶缺口压缩异常。

第三项由 `docs/rh-pc4-dual-dgap-decomposition.md` 继续分解，并由三个基础接口支撑：

- `docs/rh-pc4-dual-box-overlap.md`：盒分解有限重叠；
- `docs/rh-pc4-dual-projection-orthogonalization.md`：分散盒质量转投影能量；
- `docs/rh-pc4-dual-lowdim-frequency-extraction.md`：PI 不可检测时抽取低维频率，进入 FCT。

因此过密分支最终也被送入 PC4-A/SC/PI/FCT/LV/LSMP/OV2。

## 6. 全局排斥定理（条件化）

**Theorem RH-Contradiction-Field-Conditional-Closure（RH 反例矛盾场条件化闭合）。** 假设以下文档中的输入均无条件成立或已由精确外部定理引用：

1. PC1：离线零点到平滑素数异常（见 `docs/rh-pc1-analytic-input-theoremization.md`）；
2. PC2：Li/CRT 零频基线匹配（见 `docs/rh-pc2-crt-baseline-explicit.md`）；
3. PC3-OV2：过疏到 ACC 过剩或 D 组终端；
4. PC4-A/SC/PI/FCT closure，并由 `docs/rh-pc4-terminal-final-no-cycle-audit.md` 合并为 PC4 终端无循环事件图；
5. PC4 外部事件吸收矩阵：`docs/rh-pc4-external-event-absorption-audit.md`；
6. PC4-Dual、Dual-Gap-Ledger 与 DGap 三接口，并由 `docs/rh-pc4-dual-dgap-event-match-audit.md` 匹配到 PC4 终端事件图；
7. 全文接口一致性审查：`docs/rh-global-interface-consistency-audit.md`；
8. NRC/EXT、LV/LSMP、AAI/PPI/MLC、DSO/CE 等外部结构接口，其中 NRC/EXT 引用审查见 `docs/rh-nrc-ext-final-citation-audit.md`，LSMP/FCT/CapacityFail 审查见 `docs/rh-lsmp-fct-capacity-final-audit.md`。

则不存在离线零点 `β>1/2` 能被该 CRT/覆盖动力系统吸收。

**证明。** 反设存在离线零点。PC1 给无穷多尺度上的素数异常 `|E_z|>=Δ=X^{β-o(1)}`。PC2 把该异常投影为粗合数账本反向异常 `B_z-B_z^0=-E_z+o(Δ)`。由覆盖恒等式，异常必须进入 `ACC`、`O` 或 `Gap` 三个结构场。

若 `E_z<0`，由 PC3-OV2 进入 ACC 正向过剩或 D 组终端，再由 PC4 终端无循环事件图与 NRC/LV 等外部吸收排斥。若 `E_z>0`，由 PC4-Dual 进入 ACC 负向同步、overlap 过剩或 `DGap` 压缩异常；前两者进入 PC4-A 或 OV2/D，第三者由 DGap-Decomposition 进入 SC/PI/FCT/LV 或 A/OV2。所有内部分支由 `PC4-Terminal-No-Cycle` 排除，外部分支由假设 closure 吸收，矛盾。证毕。

## 7. 剩余无条件化清单

当前总攻链条的剩余不是再寻找新分支，而是逐项降低条件化接口：

1. **解析输入**：PC1 的 Landau--Ingham 平滑振荡和权函数非湮灭，引用级审查见 `docs/rh-pc1-analytic-input-citation-audit.md`；
2. **基线输入**：PC2 的 CRT 候选边界误差与权重正规化，最终无条件化审查见 `docs/rh-pc2-baseline-unconditional-audit.md`；
3. **覆盖输入**：AAI/PPI/MLC 内部接口已拆解，上游最终审查见 `docs/rh-pc3-ov2-upstream-unconditional-audit.md`；剩余依赖已转入 FCT、LV/LSMP、DSO/PI、NRC/EXT；
4. **正交输入**：最终合并审查见 `docs/rh-pc4-orthogonality-final-closure-audit.md`，DSO/容量最终矩阵见 `docs/rh-dso-capacity-final-audit.md`；分散正交能量已转入 DSO 容量上界或 PI-Seed/FCT/LSMP/LV/NRC；
5. **终端输入**：PC4-A/SC/PI/FCT 已由 `docs/rh-pc4-terminal-final-no-cycle-audit.md` 合并为无循环事件图；
6. **外部吸收**：LV/LSMP/NRC/CE/DSO/CapacityFail 见 `docs/rh-pc4-external-event-absorption-audit.md`；
7. **对偶输入**：DGap 三接口已由 `docs/rh-pc4-dual-dgap-event-match-audit.md` 匹配到终端事件图；
8. **接口一致性**：尺度、符号与误差传递见 `docs/rh-global-interface-consistency-audit.md`。

## 8. 诚实结论

本文可以作为 RH 总攻的条件化骨架：它说明离线零点异常一旦被投影到 CRT/覆盖动力系统，便只能进入有限个结构场，而这些结构场已被当前 closure 文档逐一围堵。

但本文不能写成“RH 已证明”。真正的下一步是转入最终外部定理与容量定理审稿：PC1/PC2/PC3 上游输入均已完成引用级、初等或事件矩阵审查。
