# RH 无条件化最终剩余缺口审查

本文按顶级数学期刊审稿标准审查当前 RH/GEE 总稿。结论必须诚实：本轮已完成 GEE 单篇内联与 LaTeX 主稿迁移，但仍不能把当前材料宣称为 RH 无条件证明定稿。原因不是缺少“文件工程”，而是仍有若干命名输入需要标准外部定理精确引用或逐行证明。

## 1. 已完成的工程闭合

- GEE 单篇 Markdown 内联稿：`docs/rh-gee-single-paper-inline-draft.md`。
- GEE LaTeX 主稿迁移：`paper/rh-proof/rh-contradiction-field.tex` 新增 `Global Exit Exclusion` 节。
- GEE 核心对象已在单篇主稿中统一：`Load/Excess`、九出口矩阵、事件图无循环、阈值常数、GEE 下界与上界。
- 清单中过期的“事件图、阈值、Load、单篇内联”义务可视为工程层面完成。

## 2. 仍不能跳过的数学缺口

### G1：外部定理精确适配

PC1 的 Landau--Ingham 振荡、NRC 的 Kloosterman/Weil 完成和、Vaaler 逼近、BG/Baker reciprocal-sum savings、Selberg/Vaughan 输入仍需在正式稿中给出定理编号、页码、假设范围、归一化匹配与常数依赖。

可修补方案：在 `paper/rh-proof/rh-references.bib` 与主稿 `External references` 节中逐条补“定理号 + 使用形式 + 变量替换 + 损失常数”。

### G2：命名引理逐行证明

`Seed-Transfer`、`Baseline-Subtraction`、`PPI-Rank`、`MidCap-Structure`、`A/FCT/SC` 势函数下降、`PI/DSO` 容量桥接仍主要以引用文档或 review proof 形式出现。

可修补方案：把每个命名引理迁入 LaTeX 附录，证明中不得出现“由对应文档可知”“按定义转出”这类未展开跳步；每个转出都要给出唯一目标、权重守恒或有限重叠不等式。

### G3：GEE 上界仍是条件合成

`Theorem GEE upper bound` 目前依赖九个局部 exit 机制已成立。虽然事件图合成层面已闭合，但局部机制本身仍需逐条接受。

可修补方案：将九出口拆成九个正式命题：`LV`、`NRC`、`PI`、`DSO`、`CE`、`LSMP`、`FCT`、`SC`、`A`。每个命题必须以同一 `Load` 定义给出 `o(Δ)`、内部下降或合法转出。

### G4：主定理仍是 review form

当前 LaTeX 主定理明确写为 review form。只要主稿仍依赖 review-form proof 和 restricted external inputs，就不能改成“RH 无条件证明”。

可修补方案：只有当 G1--G3 全部完成，且所有 `proof sketch`、`review proof`、`restricted use` 被正式证明或精确引用替代后，才可改标题与主定理表述。

## 3. 最小剩余割集

当前真正最小割集为：

1. `EXT-Precision`：外部定理逐条精确适配；
2. `Local-Exit-Proofs`：九出口局部命题逐条证明；
3. `Transfer-Accounting`：已由 `docs/rh-transfer-accounting-formal-appendix.md` 补齐；
4. `Review-Form-Elimination`：删除或升级所有 proof sketch/review proof。

若四项任一未完成，则不能声称 RH 已无条件证明。

## 4. 下一步建议

下一步最优不是继续扩大框架，而是选择一个最小割集逐条严写。优先级建议：

1. `Transfer-Accounting`，因为它是纯内部账本，最可能无外部黑箱完成；
2. `Local-Exit-Proofs` 中的 `LV/CE/LSMP/FCT/SC/A`，因为它们主要是势函数或阈值闭合；
3. `PI/DSO/NRC`，因为它们依赖外部解析输入；
4. `EXT-Precision`，最后按期刊格式补定理号、页码和变量匹配。

## 5. 审稿结论

当前仓库已经形成 RH/GEE 条件合成的单篇审稿主稿和完整工程归档；但按顶刊标准，尚未完成 RH 无条件证明。任何最终稿必须保留这一结论，直到上述最小割集全部被逐行证明或精确引用替代。

## 6. Transfer-Accounting 补强状态

新增 `docs/rh-transfer-accounting-formal-appendix.md`，并在 `paper/rh-proof/rh-contradiction-field.tex` 的 GEE 节加入 Transfer-accounting proposition。该补强把 seed 转出、内部下降、吸收停止和有限细分统一为四类允许操作，证明质量不增、源目标不双计、最终路由重叠为 `log^{C_route+C_transfer}X`。

因此最小剩余割集更新为三项：`EXT-Precision`、`Local-Exit-Proofs`、`Review-Form-Elimination`。其中 `Local-Exit-Proofs` 仍包含九出口局部上界本身，不能由本账本附录替代。

## 7. Local-Exit-Proofs 第一阶段补强

新增 `docs/rh-local-exit-proofs-formal-appendix.md`，并在 LaTeX GEE 节加入 Low-black-box local exits proposition。该补强将 `LV/CE/LSMP/FCT/SC/A` 六个出口写成阈值吸收、内部势函数下降或源删除转出命题。

剩余 `Local-Exit-Proofs` 不再是九出口整体，而压缩为三个解析硬出口：`PI/DSO/NRC`。其中 `PI/DSO` 需要无幂损失容量与 square-function 上界，`NRC` 需要双变量和 DSO-E 逐入口参数匹配。

## 8. 解析出口统一归约

新增 `docs/rh-analytic-exit-reduction-table.md`，并在 LaTeX GEE 节加入 Analytic exit reduction proposition。该补强把剩余 `PI/DSO/NRC` 三出口压缩为三条不等式：AEX-1 投影容量、AEX-2 DSO square-function、AEX-3 NRC 逐入口参数匹配。

因此 `Local-Exit-Proofs` 的剩余不再是泛泛九出口证明，而是 AEX-1--AEX-3 三个具体数学目标。

## 9. AEX-1 投影容量补强

新增 `docs/rh-aex1-projection-capacity-formal.md`，并在 LaTeX GEE 节加入 AEX-1 projection capacity proposition。该补强把 AEX-1 压缩为两个正式容量输入：`PI-Lac` 与 `PI-Dense`。其中基线扣除、失败转出和有限重叠账本已闭合；剩余是 dense/lacunary 容量定理在最终稿中的正式证明或精确引用。

## 10. AEX-2 DSO square-function 补强

新增 `docs/rh-aex2-dso-squarefunction-formal.md`，并在 LaTeX GEE 节加入 AEX-2 DSO square-function proposition。该补强把 AEX-2 压缩为一个核心输入 `DSO-SF`：martingale square-function 基线必须由允许容量加 `Δ^2/log^B X` 控制。Parseval/frame、误差转出和有限重叠账本已形式化。

## 11. AEX-3 NRC 参数匹配补强

新增 `docs/rh-aex3-nrc-parameter-match-formal.md`，并在 LaTeX GEE 节加入 AEX-3 NRC parameter matching proposition。该补强把 NRC 入口分成四类：单变量 PPI 直接平方根闭合，Tail/RKS 分流，双变量 PPI 经 MidCap 转出，DSO-E 依赖 `DSO-SF`。

因此 NRC 剩余不再是泛泛双变量硬点，而主要依赖 `EXT-KL` 精确适配与 `DSO-SF`。
