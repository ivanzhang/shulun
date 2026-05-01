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
