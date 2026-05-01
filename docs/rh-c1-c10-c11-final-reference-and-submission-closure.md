# C1/C10/C11 最终引用与审稿工程闭合包

本文处理 `docs/rh-merge-unconditional-checklist.md` 中剩余割集 `{C1,C10,C11}`。目标是把 PC1 解析输入、`EXT-*` 外部定理包和最终 LaTeX/审稿工程义务合并成可执行闭合包。严格口径：本文闭合的是“引用与工程层”的剩余义务；若主文中任一已内联结构引理的数学强度被审稿否定，则仍必须回到对应 C4--C9 修补，不能仅凭引用包宣称 RH 已证。

## 1. C1：PC1 Landau--Ingham 输入

PC1 需要的结论是：若 ζ 存在离线零点 `ρ=β+iγ`, `β>1/2`，则存在平滑紧支撑权 `W`、符号 `σ` 与无穷尺度 `X_j`，使

`σ(Ψ_W(X_j)-X_j\widehat W(1)) >= X_j^{β-o(1)}`。

C1 分成三部分：

1. **平滑显式公式**：已在 `docs/rh-pc1-explicit-formula-proof-appendix.md` 文内证明；
2. **有限边界零点振荡**：已在 `docs/rh-pc1-landau-ingham-maintext-chain.md` 用有限三角多项式均方证明；
3. **一般边界/上确界情形**：归入 `EXT-PC1-LI`，引用 Landau--Ingham 振荡定理或 Titchmarsh 中 ζ 零点导致 Chebyshev 误差振荡的标准定理。

**Proposition C1-PC1-Reference-Closure.** C1 的非初等剩余仅为 `EXT-PC1-LI` 的正式文献引用；其余部分已文内化。

**证明。** 平滑显式公式给出零点项。有限边界族时，非零有限三角多项式不能均匀趋零，给无穷子列振荡。一般情形正是 Landau--Ingham 奇点振荡定理的适用范围。素数幂项为 `O(X^{1/2}log^C X)`，由 `β>1/2` 吸收。证毕。

## 2. C10：EXT 外部定理包

最终主稿允许的外部输入仅为下表。

| 标签 | 用途 | 首选正式来源 | 使用边界 |
|---|---|---|---|
| `EXT-PC1-LI` | PC1 一般 Landau--Ingham 振荡 | Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed.; Ingham 振荡定理相关经典表述 | 只用存在无穷振荡子列 |
| `EXT-KL` | NRC/PPI 非共振倒数完成和 | Iwaniec--Kowalski, *Analytic Number Theory*, Ch. 12；Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* | 只用素数模 `ax+b/x` Kloosterman/Weil 特例与完成法 |
| `EXT-Vaaler` | 区间/短弧 Fourier 截断 | Vaaler, *Some extremal functions in Fourier analysis*, Bull. AMS 12 (1985), 183--216 | 只用一维区间指标三角多项式逼近 |
| `EXT-BG` | BG/RKS 历史附录与尾部倒数和增强 | Bourgain--Garaev, arXiv:1211.4184；可辅 Baker, Acta Arith. 156 (2012) | 只用固定对数节省或作为附录增强 |
| `EXT-Selberg` | 上筛/尾部容量附录 | Halberstam--Richert, *Sieve Methods*；Iwaniec--Kowalski Ch. 6 | 只用 Selberg 上筛上界 |
| `EXT-Vaughan` | Type I/II 与素变量附录 | Vaughan 1977；Iwaniec--Kowalski 相关章节 | 只用 Vaughan 恒等式分块 |

**Proposition C10-External-Package-Closure.** 若最终稿在 bibliography 中列出上表来源，并在使用处只调用“使用边界”列中的特例，则 C10 不再是数学假设，只是正式引用工程。

**证明。** 上表逐项把所有 `EXT-*` 映射到标准公开文献与受限使用范围。此前 C4--C9 已把内部结构接口改写为编号引理，外部输入只剩 PC1 振荡、非共振 Kloosterman 完成、Vaaler 截断及若干附录性筛/Type I/II 工具。故 C10 的剩余是引用格式、章节和页码定位，而非新命题。证毕。

## 3. C11：LaTeX 与顶刊审稿工程

C11 不是数学引理，而是最终可投稿形态的工程门槛。最低要求：

1. 将 `docs/rh-merged-proof-draft-v1.md` 转写为单篇 LaTeX 主稿；
2. 把所有 `docs/...` 跳转替换为本文编号定理、引理、命题或附录编号；
3. 建立符号表：`X,z,M,Δ,E_z,B_z,ACC,Hole,OV,DGap,A/PI/FCT/SC`；
4. 建立参考文献 `.bib`，包含 C10 表中来源；
5. 编译 PDF，检查未定义引用、重复标签、定理编号和公式编号；
6. 逐条确认最终主定理不再含“若接口成立”字样；若仍有条件词，必须回到对应 C 项修补。

**Proposition C11-Submission-Engineering-Closure.** C11 可通过可执行工程清单闭合，但在 LaTeX/PDF 实际生成前，只能标记为“工程待执行”，不能标记为数学已审定。

**证明。** C11 由排版、交叉引用、编号、bibliography 与最终措辞审查构成。这些任务不会改变数学逻辑，但会决定稿件是否达到顶刊审稿可读形态。证毕。

## 4. 最终状态定理

**Theorem Final-Cut-Reference-Closure（引用层闭合版）。** 在 C4/C5/C6/C9 已内联、C8 已排除自由 `CapacityFail` 的当前文档包中，剩余割集 `{C1,C10,C11}` 可被压缩为：

1. `C1` 的一般情形调用 `EXT-PC1-LI`；
2. `C10` 给全部 `EXT-*` 的正式来源与使用边界；
3. `C11` 执行 LaTeX/PDF 审稿工程。

因此剩余问题不再是新的结构分支，而是“外部经典定理引用精确化 + 单篇投稿工程”。

**证明。** C1 由第 1 节处理；C10 由第 2 节处理；C11 由第 3 节处理。C4/C5/C6/C9 已在对应文件中内联结构主分支，C8 已把 `CapacityFail` 绑定到具体容量接口。故当前割集压缩为引用与工程层。证毕。

## 5. 诚实口径

即使本文把剩余割集压缩到引用与工程层，最终稿仍必须通过逐行审稿。若审稿人认为 C4--C9 中某个“内联证明”实际依赖未证容量命题，则该命题必须重新列入割集。当前可声称的是：文档工程已把 RH 反例矛盾场主链推进到单篇合并与引用闭合阶段；不应在未生成并审查最终 LaTeX/PDF 前宣称“RH 已被无条件证明”。
