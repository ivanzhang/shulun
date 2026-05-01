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
