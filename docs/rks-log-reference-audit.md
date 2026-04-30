# RKS-log 引用匹配审查

统一参考文献标签见 `docs/bibliography.md`。
本文件审查 `docs/tail-log4-theoremization.md` 中 RKS-log 输入与 Bourgain--Garaev 型文献定理的匹配程度。

## 1. 本地核验来源

本轮抓取并核验 arXiv:1211.4184 源文件 `BGkl.tex`，题名为 *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*。文中相关定理包括：

- Theorem `Kloost 1/2`：若区间 `I_1,...,I_n` 满足 `|I_1|...|I_n|>p^{1/2+ε}`，则多线性倒数 Kloosterman 和有 `p^{-δ}` 节省。
- Theorem `Kloost double 18/37`：双线性区间在 `|I_1|>p^{1/18}`、`|I_2|>p^{5/12+ε}` 范围有幂节省。
- Corollary `th1KloostPrimespowerFull range`：素变量倒数幂和可得 `p^{23/24+o(1)}` 型全范围界。

## 2. 与 RKS-log 的匹配情况

`RKS-log` 在当前稿中的理想形式是：若双线性 Type I/II 块体积 `MN>=p/log^A p`，则有任意固定对数节省。

文献定理可直接支持的部分：

1. **多线性大体积块**：若 Vaughan/Heath--Brown 分解后能形成 `n` 个区间变量，且乘积体积 `>p^{1/2+ε}`，Theorem `Kloost 1/2` 可给幂节省，从而强于任意固定对数节省。
2. **平衡双线性块**：若能落入 `Kloost double 18/37` 或 `Th1GenBil` 的长度条件，可给幂节省。
3. **单素变量全范围参考**：素变量倒数和存在 `p^{23/24+o(1)}` 型界，但它不直接覆盖本文所有加权双线性块。

不能直接支持的部分：

- 文献没有直接给出“任意双线性块只要 `MN>=p/log^A p` 就有对数节省”的定理。
- 当 Type I/II 块只有两个变量且乘积接近 `p/log^A p`，但无法再分裂成满足 `p^{1/2+ε}` 乘积阈值的多线性源时，RKS-log 仍需桥接证明。
- divisor-bounded 稀疏系数虽然通常可 dyadic 分层处理，但必须在最终稿中说明它们如何满足引用定理的系数假设。

## 3. 审稿结论

RKS-log 不能直接作为已由 Bourgain--Garaev 文献完全覆盖的黑箱。更严谨的口径应为：

> BG 多线性定理覆盖 RKS-log 中所有可多线性分裂且体积超过 `p^{1/2+ε}` 的块；剩余近临界 `p/log^A p` 双线性块需要额外桥接引理，或必须在 TL4-L 中改用完成和/Weil 平凡吸收并重新核算余量。

因此，Tail-log4 当前剩余最小引用义务不是泛泛 “BG/coherent”，而是：

**RKS-bridge.** 对 TL4-L 的 Vaughan Type I/II 分块，证明每个未被平凡吸收的块都能进一步分裂或重组为 BG `Kloost 1/2`/`Kloost double` 可覆盖的形式；否则给出单独的近临界双线性对数节省证明。

## 4. 对最终接口表的影响

`Tail-log4` 的剩余审稿义务应从“RKS-log 与文献精确匹配”细化为：

- `RKS-covered`：列出已被 BG 定理覆盖的 Type I/II 块范围；
- `RKS-bridge`：处理 `MN≈p/log^A p` 但不满足现有 BG 定理阈值的近临界块；
- `Coefficient audit`：核对 Vaughan 系数、divisor-bounded 系数和 dyadic 平滑权满足引用定理假设。

## 5. RKS-bridge 分区补充

近临界块的具体分区见 `docs/rks-bridge-partition.md`。进一步核验后，短侧低于 `P^{1/18}` 的近极端不平衡块可由逐短变量 Weil 吸收；当前最小剩余降为 RKS-parameter-audit，即核对 Vaughan 分解所有块均落入 BG 覆盖、Weil 吸收或平凡吸收区域，并核算总对数损失。
