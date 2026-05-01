# RH 总攻最终合并状态与剩余缺口判定

本文对当前 RH 反例矛盾场文档包作最终合并状态审查。目标是明确哪些接口已被主文化、哪些只剩编辑引用义务、哪些仍不能据此宣称 RH 已无条件证明。本文保持严格口径：当前文档包已把条件化链条压缩到可审查主文链集合，但尚未形成顶刊意义上的单篇无条件 RH 证明。

## 1. 已主文化的核心链条

当前已新增或接入的主文链包括：

1. PC1 Landau--Ingham：`docs/rh-pc1-landau-ingham-maintext-chain.md`；
2. PC2 CRT 基线：`docs/rh-pc2-crt-baseline-maintext-appendix.md`；
3. PC3/OV2：`docs/rh-pc3-ov2-maintext-proof-chain.md`；
4. PPI 输出：`docs/rh-ppi-terminal-output-maintext-chain.md`；
5. NRC/EXT：`docs/rh-nrc-ext-maintext-closure.md`；
6. FCT：`docs/rh-fct-maintext-closure-chain.md`；
7. PI/DSO：`docs/rh-pi-dso-maintext-bridge-chain.md`；
8. SC：`docs/rh-sc-maintext-capacity-closure.md`；
9. DGap：`docs/rh-dgap-maintext-three-interface-chain.md`；
10. Fourier/Vaaler 尾项：`docs/rh-fourier-vaaler-tail-maintext-chain.md`；
11. LV/LSMP/CE：`docs/rh-lv-lsmp-ce-maintext-absorption-chain.md`；
12. EXT 引用：`docs/rh-ext-maintext-citation-closure.md`；
13. 全局归一化：`docs/rh-global-normalization-maintext-closure.md`。

这些文档把原来的矩阵式条件接口转写为连续证明链或明确外部定理标签。

## 2. 当前总链拼接

总链拼接为：

`离线零点`  
`=> PC1 平滑素数窗口异常`  
`=> PC2 粗合数候选账本反向异常`  
`=> 覆盖场方程`  
`=> 过疏 PC3/OV2 或过密 Dual/DGap`  
`=> A/PI/FCT/SC 或 LV/LSMP/CE/DSO/NRC/CapacityFail`  
`=> 已命名主文链或 EXT 外部定理标签`。

全局归一化链统一了 `X,z,M,Δ,E_z,B_z,ACC/O/Gap/DGap`，并确认所有固定对数损失吸收到 `X^{o(1)}`。

## 3. 仍不能宣称 RH 已无条件证明的原因

当前仍不能宣称 RH 已无条件证明，原因不是分支图遗漏，而是论文定稿标准尚未满足：

1. 多数主文链仍分散在多个 Markdown 附录中，尚未合并为一篇线性论文；
2. `EXT-PC1-LI` 一般情形仍需给精确书目、章节或定理号；
3. `EXT-KL/EXT-Vaaler/EXT-BG/EXT-Selberg/EXT-Vaughan` 仍需在最终稿中替换为正式 BibTeX/页码/定理号；
4. 部分容量语句仍以“对应容量文档可用”为前提，需要在单篇稿中逐条内联或编号引用；
5. 尚未做最终 LaTeX 交叉引用、符号表和定理编号检查；
6. 仓库中大量未跟踪实验材料未纳入正式审稿包，需保持排除或归档说明。

因此当前正确结论是：条件化 RH 反例矛盾场已高度主文化，剩余主要是单篇论文合并和正式引用工程；不是已经完成可投稿的无条件 RH 证明。

## 4. 无条件化完成判据

若要把本文档包升级为“无条件证明稿”，至少必须完成以下判据：

1. 单篇主稿中逐一定义所有对象，不依赖读者在多个审查表间跳转；
2. 每个主定理只引用已编号的本文引理或 `EXT-*` 正式外部定理；
3. 所有 `EXT-*` 均有正式文献条目、章节、定理号或页码；
4. 所有 `CapacityFail` 在主稿中绑定到已证明容量引理或明确反设矛盾；
5. 全文使用同一权重口径，默认 Chebyshev 权，无权版本只作推论；
6. 全文常数层级在开头声明，并在关键引理中不出现反向依赖；
7. 最终结论段明确由“假设离线零点”推出矛盾，且不再含“若接口成立”条件。

## 5. 合并稿 v1

单篇合并雏形已写入 `docs/rh-merged-proof-draft-v1.md`。该稿按证明顺序整合 PC1、PC2、覆盖场方程、过疏 PC3/OV2、过密 Dual/DGap、内部终端、外部吸收、尾项和 EXT 引用。它仍保留 `docs/...` 交叉引用和条件版主定理，因此是合并雏形，不是最终无条件证明稿。

## 6. 下一步最优工作

下一步不应再新造分支，而应进入论文合并工程：

1. 新建或重写最终主稿，把第 1 节列出的主文链按证明顺序合并；
2. 把第 4 节判据作为 checklist 逐项勾销；
3. 同步维护 `docs/final-submission-manifest.md` 与 `docs/references-and-appendices.md`；
4. 每次合并后运行现有阈值/有限验证脚本和 Markdown diff 检查；
5. 最后做一次诚实口径审查：只有当第 4 节全部完成，才可把标题从“条件化/总攻稿”改为“无条件证明稿”。

## 6.1 合并稿无条件化判据表

新增 `docs/rh-merge-unconditional-checklist.md`，把合并稿条件接口拆为 C0--C11。当前最小闭合割集为 `{C1,C4,C10,C11}`。这意味着下一轮应优先补过疏 PC3/OV2 与正式外部引用 C10，而不是继续增加新分支。

## 6.2 C3 覆盖场修正

新增 `docs/rh-c3-covering-field-definition-closure.md`。审查中发现原 `B_z=ACC_z-O_z+Gap_z` 若按逐点集合账本理解存在恒等式风险；现改为一层严格划分 `B_z=ACC_z+Hole_z+o(Δ)`，并把 overlap 写成二层事件 `OV_z=T_z-ACC_z`。因此 C3 从最小割集中移出，但仍需最终主稿内联。

## 6.3 C8 CapacityFail 升级审查

新增 `docs/rh-c8-capacityfail-upgrade-audit.md`。结论是：自由 `CapacityFail` 已排除，但 C8 不能独立完全勾销；它随 C4/C10 的容量定理化与正式引用一起放电。当前最小闭合割集更新为 `{C1,C4,C10,C11}`。

## 6.4 C5 DGap 内联证明链

新增 `docs/rh-c5-dgap-inline-proof-chain.md`。DGap 过密分支已与 C3 修正版匹配，入口为 `DGap_z=Hole_z^0-Hole_z`；内部三接口被拆成 C5.1 盒局部化、C5.2 frame 投影能量、C5.3 正交投影分配、C5.4 低维频率抽取。当前最小闭合割集更新为 `{C1,C4,C10,C11}`。

## 6.5 C9 Fourier/Vaaler 尾项内联

新增 `docs/rh-c9-fourier-vaaler-tail-inline-proof.md`。尾项处理被拆成 C9.1 单原子尾项、C9.2 固定布尔组合稳定、C9.3 有限重叠盒族求和、C9.4 高频异常命名出口。C9 已从“待内联”改为“已内联，待 C10 正式引用”。当前最小闭合割集更新为 `{C1,C4,C10,C11}`。

## 6.6 C6 内部终端无循环内联

新增 `docs/rh-c6-internal-terminal-inline-proof.md`。内部终端 `A/PI/FCT/SC` 被拆成 C6.1 ACC no-cycle、C6.2 PI terminal reduction、C6.3 FCT Noether descent、C6.4 SC descent，并由 Theorem C6 统一排除内部无限逃逸路径。当前最小闭合割集更新为 `{C1,C4,C10,C11}`。

## 7. 状态定理

**Theorem Final-Merge-Status.** 当前仓库中的 RH 总攻文档包已经把主要条件接口压缩为主文链、外部定理标签和全局归一化账本；但在未完成单篇论文合并、正式引用替换、容量定理内联和交叉引用审查前，不能宣称 RH 已无条件证明。

**证明。** 第 1 节列出已主文化链条，第 2 节给出全局拼接，第 3 节列出仍缺少的顶刊证明稿条件，第 4 节给出升级判据。由于第 4 节尚未全部完成，当前状态只能是“高度主文化的条件化总攻文档包”，而非最终无条件证明。证毕。
