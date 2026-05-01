# RH 合并稿无条件化判据勾销表

本文是 `docs/rh-merged-proof-draft-v1.md` 的审稿工程清单。目标不是宣布 RH 已证，而是把“合并稿条件版”中每一个条件接口转化为可逐项勾销的证明义务。

## 1. 判据总表

| ID | 接口 | 当前证据位置 | 无条件化要求 | 状态 |
|---|---|---|---|---|
| C0 | 全局符号、尺度、权重一致 | `docs/rh-global-normalization-maintext-closure.md` | 合并入主稿第 1 节，消除反向常数依赖 | 待内联 |
| C1 | PC1 Landau--Ingham 振荡 | `docs/rh-pc1-landau-ingham-maintext-chain.md` | 给出 `EXT-PC1-LI` 精确定理来源；有限边界情形保留文内证明 | 待引用精确化 |
| C2 | PC2 CRT 零频基线 | `docs/rh-pc2-crt-baseline-maintext-appendix.md` | 逐行证明 `C_z-C_z^0=o(Δ)` 且说明边界项被 `X^{β-o(1)}` 吸收 | 待内联 |
| C3 | 覆盖场方程 | `docs/rh-c3-covering-field-definition-closure.md` | 已发现原 `ACC-O+Gap` 写法逐点恒等式风险；改为 `ACC+Hole` 一层划分与 `OV` 二层事件 | 已修正，待内联 |
| C4 | 过疏 PC3/OV2 | `docs/rh-c4-sparse-pc3-ov2-inline-proof.md` | C4.1--C4.4 已内联；非共振完成和正式引用归 C10 | 已内联，待 C10 |
| C5 | 过密 Dual/DGap | `docs/rh-c5-dgap-inline-proof-chain.md` | Lemma C5.1--C5.4 已定理化；C6/C9 已内联，剩余依赖 C2/C10 | 内部已闭合，待依赖放电 |
| C6 | 内部终端 `A/PI/FCT/SC` | `docs/rh-c6-internal-terminal-inline-proof.md` | C6.1--C6.4 已内联为统一无循环定理；外部出口归 C7/C10 | 已内联，待外部出口 |
| C7 | 外部事件 `LV/LSMP/CE/DSO/NRC` | LV/LSMP/CE、NRC、PI/DSO 主文链 | 每个失败出口必须回到已编号终端，不能产生新假设 | 待出口核验 |
| C8 | `CapacityFail` | `docs/rh-c8-capacityfail-upgrade-audit.md` | 自由黑箱已排除；C4/C5/C6/C9 已处理，剩余随 C1/C10 的引用与主稿工程放电 | 依赖型待闭合 |
| C9 | Fourier/Vaaler 尾项 | `docs/rh-c9-fourier-vaaler-tail-inline-proof.md` | C9.1--C9.4 已内联；剩余 `EXT-Vaaler` 正式引用归 C10 | 已内联，待 C10 |
| C10 | `EXT-*` 外部定理 | `docs/rh-ext-maintext-citation-closure.md` | BibTeX、章节、定理号/页码、使用范围逐项匹配 | 待精确引用 |
| C11 | LaTeX 审稿工程 | 尚未生成 | 定理编号、交叉引用、符号表、参考文献编译通过 | 待执行 |

## 2. 当前最小闭合割集

当前阻止“无条件证明稿”口径的最小割集为：

`{C1, C10, C11}`。

其中 C2、C7 仍应在最终稿中内联；C9 已完成内联但其 Vaaler 来源仍归 C10 精确引用。

## 3. 优先顺序

1. C3 已完成定义化修正；最终主稿需内联 `ACC+Hole` 与 `OV` 二层账本。
2. C8 已从自由黑箱降级为依赖型义务；C4/C5/C6/C9 已处理，最终随 C10 放电。
3. C4 过疏、C5 DGap、C6 内部终端与 C9 尾项均已内联；下一步优先补 C10 正式引用，并将 C1 并入 PC1 引用包。
4. 再补 C1/C10：把外部解析输入替换为正式引用。
5. 最后执行 C11：生成 LaTeX/PDF 并做交叉引用审查。

## 4. 严格口径

在 C0--C11 全部勾销前，只能称为“RH 反例矛盾场合并证明稿/条件闭合稿”。若任一核心容量接口无法逐行证明，则必须降级为条件命题，不能改写为 RH 无条件证明。
