# RH 无条件化攻坚路线图：剩余条件割集与优先顺序

本文接续 `docs/rh-final-consistency-review.md`。目标是继续向 RH 无条件证明推进，但保持严格诚实口径：当前已有的是条件化反例矛盾场与审稿矩阵；要升级为无条件证明，必须逐项消除剩余条件割集。

## 1. 当前不可跳过的事实

当前链条不能直接宣称 RH 已证明，原因是若干接口仍以“容量定理成立”“外部输入可用”“终端定义匹配”形式存在。它们已被命名和定位，但命名不等于证明完成。

因此下一阶段不是再增加新分支，而是把每个剩余条件变成：

1. 标准外部定理精确引用；或
2. 文内逐行证明；或
3. 明确无法由当前工具证明的开放硬点。

## 2. 最小剩余条件割集

按当前总攻链条，最小割集可压缩为五类：

| 编号 | 割集 | 当前入口 | 无条件化目标 |
| --- | --- | --- | --- |
| R1 | `EXT-*` 页码/定理号 | `docs/rh-nrc-ext-final-citation-audit.md` | 精确引用化，不改变逻辑 |
| R2 | `CapacityFail` 具体容量证明 | `docs/rh-lsmp-fct-capacity-final-audit.md` | 每个容量失败绑定并证明/转事件 |
| R3 | `LSMP/FCT` 定义匹配 | `docs/omr-cgtp-lsmp-theoremization.md`, `docs/fct-tree-wfe-theoremization.md` | coarea/DPI/Tree-WFE 与 PC4 seed 完全对齐 |
| R4 | `DGap` 三接口强度 | `docs/rh-pc4-dual-*.md` | 盒有限重叠、投影正交化、低维抽取逐行化 |
| R5 | 论文一体化形式化 | 所有矩阵 | 消除“见审查矩阵”的跳转式证明 |

## 3. 优先顺序

最优顺序不是从最难处硬跳，而是先压缩自由度：

1. **先攻 R2-CapacityBinding**：把所有 `CapacityFail` 出现位置列成表，逐项绑定唯一容量文档；这能立刻暴露真正未证容量。
2. **再攻 R3-LSMP/FCT-Match**：检查 LSMP 输出的 PI/FCT seed 与 PC4 终端定义是否完全同型。
3. **再攻 R4-DGap-Interfaces**：DGap 依赖三接口，是过密分支最后结构硬点。
4. **最后攻 R1/R5 编辑化**：外部定理页码和论文一体化。

## 4. 第一硬点：CapacityBinding

`CapacityFail` 当前已被要求绑定到具体容量文档，但还缺一张“出现位置 -> 绑定文档 -> 状态”的全局表。若某处 `CapacityFail` 不能绑定，则它是真正漏洞；若全部可绑定，则下一步只需逐个证明对应容量定理。

**目标命题 R2-CapacityBinding。** 当前正式审稿入口中的每个 `CapacityFail` 或“容量失败”均可绑定到以下之一：

- DSO 正交容量；
- PI lacunary/Carleson 容量；
- SC 局部乘积容量；
- OV2/MLC 主层容量；
- DGap 盒/投影容量；
- AAI/主层整除容量。

且绑定后出口只能是矛盾或已命名事件。

## 5. 本轮推进任务

本轮先完成 `R2-CapacityBinding` 的全局扫描表。若表中出现未绑定项，则下一轮专攻该项；若没有未绑定项，则转入最弱容量定理的逐行证明强度审查。


## 6. R2 首轮推进记录

`DGap 投影正交化` 的逐行强度补强已写入 `docs/rh-dgap-projection-line-by-line-audit.md`，将原先的直和分解口径替换为 frame 上界、常数方向剥离、Cauchy 下界与逐步正交投影。

## 7. R4 第二轮推进记录

`DGap 低维频率抽取` 的逐行强度补强已写入 `docs/rh-dgap-lowdim-extraction-line-by-line-audit.md`。该补强把原先“非 PI 则固定低维”的跳步拆成：有限频率截断、无界新增独立频率触发 DSO/PI、尺度漂移逃逸归入 CE/LSMP/FCT/SC、固定短弧同相位抽取为 FCT_seed。

当前 R4 剩余不再是 DGap 内部分类，而是外部接口的定量化：`DSO/PI` square-function 到允许投影族的常数、`FCT_seed` 定义完全同型匹配、Fourier/Vaaler 尾项平方可和的统一模板证明。

## 8. R4 第三轮推进记录

`DSO/PI square-function` 到允许投影族的桥接已写入 `docs/rh-dso-pi-squarefunction-bridge-audit.md`。该补强把“新增独立频率包触发 PI”的跳步拆成：允许投影族有限交表示、martingale difference 拉回、lacunary/dense 尺度二分、非允许/误差/高重叠逃逸排除。

当前 DGap 外部剩余硬点进一步缩小为两项：`FCT_seed` 与低维相位证书的逐字同型匹配；Fourier/Vaaler 尾项平方可和在全部固定盒模板上的统一证明。

## 9. R4 第四轮推进记录

`FCT_seed` 与 DGap 低维相位证书的逐字同型匹配已写入 `docs/rh-fct-seed-isomorphism-audit.md`。该补强用字段表统一 `Λ_*`、整数关系模板、自然缩放子列、短弧、同向符号和外部终端排除清单。

当前 DGap 外部剩余进一步缩小为：Fourier/Vaaler 尾项平方可和在全部固定盒模板上的统一证明；以及 FCT phase drift/closure 的无无限递归排除。

## 10. R4 第五轮推进记录

Fourier/Vaaler 尾项在全部固定盒模板上的统一平方可和审查已写入 `docs/rh-fourier-vaaler-tail-uniform-audit.md`。该补强逐项覆盖物理窗、硬边界、倒数环带、Bohr 短弧、CRT 字符和有限布尔组合，并规定失败只能转入 `CE/LSMP/LV/SC/DSO-PI`。

当前 DGap 外部接口主要剩下 `FCT phase drift/closure` 的无无限递归排除，以及总攻上游外部引用和容量常数的最终标准化。

## 11. R4 第六轮推进记录

`FCT phase drift/closure` 的无无限递归最终审查已写入 `docs/rh-fct-closure-no-cycle-final-audit.md`。该补强把 `Seed -> Drift -> NewClosure -> NoetherDescent/RepeatState -> terminal` 写成事件图，并确认每条边都进入已命名终端或离散势函数下降。

至此，DGap/FCT 内部剩余跳步已压缩到全局外部义务：上游解析输入标准化、容量定理常数核验、PC4-A/SC/Dual 与外部吸收的无回流总审查。

## 12. PC1 上游输入推进记录

PC1 外部解析输入标准化已写入 `docs/rh-pc1-external-input-standardization-audit.md`。该补强把离线零点推出平滑素数窗口异常压缩为 `EXT-PC1-EF` 平滑显式公式、`EXT-PC1-LI` Landau--Ingham 振荡，以及权函数非湮灭、素数幂去除、对数权转换三个初等步骤。

当前 PC1 剩余不再是数学接口黑箱，而是最终投稿编辑义务：给两个外部标签选择精确书目、章节或定理号，并全文统一 Chebyshev 权或无权素数口径。

## 13. 容量常数与适用条件推进记录

容量定理常数与适用条件统一核验已写入 `docs/rh-capacity-constants-applicability-audit.md`。该表把 DSO、PI、SC、OV2/MLC、AAI、DGap、FCT/LSMP、PC2 基线等容量接口逐项登记为：对象、适用条件、容量界、允许损失、常数余量和失败出口。

当前容量剩余硬点不再是无绑定 `CapacityFail`，而是 SC 局部乘积容量、OV2/MLC Uniform 零频容量、PI dense/Carleson 与 DSO bridge 适用条件的逐行证明强度。

## 14. SC 局部乘积容量推进记录

SC 局部乘积容量的全 dyadic 层核验已写入 `docs/rh-sc-local-product-capacity-dyadic-audit.md`。该补强把 `Vol_eff(I;Q,R)` 拆成短窗比例项 `(L/X)RQlog^C X` 与端点薄壳项 `Rlog^C X`，并规定比例均衡、端点控制或低体积吸收失败时只能转入 `PI/A/FCT/LV/LSMP/SC`。

当前容量剩余最弱项转向 `OV2/MLC Uniform` 零频容量最终常数化，以及所有 `log^C X` 常数层级的全局排序。

## 15. OV2/MLC Uniform 容量推进记录

OV2/MLC Uniform 零频容量常数化已写入 `docs/rh-ov2-mlc-uniform-capacity-constants-audit.md`。该补强把不可检测 Uniform 分支量化为固定 partition 复杂度、PPI 反面阈值、零频有限重叠和小原子吸收，得到 `E_unif(Q,R)<=W_Qlog^{C_U}X`。

当前容量剩余硬点转向 PI dense/Carleson 与 DSO bridge 适用条件的无回流审查，以及全局 `log^C X` 常数层级排序。

## 16. PI dense/DSO bridge 无回流推进记录

PI dense/Carleson 与 DSO bridge 适用条件无回流审查已写入 `docs/rh-pi-dense-dso-bridge-no-return-audit.md`。该补强逐项登记 lacunary/dense 二分、固定模板、martingale 拉回、允许投影有限交、误差吞噬和高重叠失败的命名出口。

当前容量链主要剩余为全局 `log^C X` 常数层级排序，以及最终论文中容量接口的交叉引用编辑化。

## 17. 全局 log 常数层级推进记录

全局 `log^C X` 常数层级排序已写入 `docs/rh-global-log-constant-hierarchy-audit.md`。该账本按 `C_struct << C_overlap << C_tail << C_frame << C_cap << C_trig << B_LV << C_0 << B_final` 的顺序选择常数，确认所有多对数损失均可吸收到 `X^{o(1)}`，且不产生循环依赖。

当前容量链剩余主要转为编辑义务：在最终论文中把匿名 `C` 改写为该层级常数族，并完成交叉引用。

## 18. 最终论文编辑入口

RH 反例矛盾场论文整合稿已写入 `docs/rh-final-paper-draft.md`。该稿把 PC1--PC4、Dual/DGap、容量矩阵与常数层级串成单篇论文结构，同时明确标注仍需无条件化或精确引用的接口。

重要口径：该稿是条件化定稿版，不宣称 RH 已证明；若要升级为无条件证明，需要把第 9 节列出的接口逐项改写为标准定理证明或精确外部引用。
