# EXT 外部定理主文引用闭合链

本文把 RH 反例矛盾场总攻稿中仍出现的 `EXT-*` 外部输入统一整理为主文可引用的定理包。目标是明确：这些输入均为标准外部定理或已文内证明的接口；若投稿阶段需要更细页码，只需编辑补页码，不改变逻辑链。

本文不宣称 RH 已证明；它闭合的是外部引用标签的审稿口径。

## 1. EXT-KL：Kloosterman--Weil 与完成法

**使用命题。** 对素数模数 `p`，非退化二项有理相位满足

`|Σ_{x∈F_p^*} e_p(ax+b/x)| <= 2p^{1/2}`，

不完全区间和经完成法多 `O(logp)` 损失。

**引用。** Iwaniec--Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, Chapter 12；或 Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* 的 Kloosterman 特例。

**使用边界。** 本文只用素数模数和 `ax+b/x` 特例，不调用 Deligne 一般形式。主使用位置为 NRC/EXT 与 DSO-E 非共振输入。

## 2. EXT-Vaaler：区间截断

**使用命题。** 区间指标由 Vaaler/Beurling--Selberg 三角多项式上下逼近，频率高度 `H`，积分误差 `O(H^{-1})`，Fourier 系数满足 `O(min(|m|^{-1},|I|))` 型界。

**引用。** Vaaler, *Some extremal functions in Fourier analysis*, Bull. Amer. Math. Soc. 12 (1985), no. 2, 183--216。

**使用边界。** 本文只用一维区间、短弧和环带截断；高维组合由固定布尔复杂度和主文尾项链处理。

## 3. EXT-PC1-EF / EXT-PC1-LI

**EXT-PC1-EF。** 平滑 Chebyshev 显式公式已在 `docs/rh-pc1-explicit-formula-proof-appendix.md` 文内证明；可引用 Titchmarsh 或 Iwaniec--Kowalski 的显式公式章节作为替代来源。

**EXT-PC1-LI。** 一般 Landau--Ingham 奇点振荡用于：离线零点不被权函数湮灭时，平滑 Chebyshev 误差在无穷尺度上有 `X^{β-o(1)}` 级振荡。有限边界零点情形已由 `docs/rh-pc1-landau-ingham-maintext-chain.md` 文内证明；一般上确界/无限边界族引用 Titchmarsh 中 Landau 振荡定理或 Ingham 素数误差振荡定理。

**使用边界。** PC1 只需要存在无穷大振荡子列，不需要零点密度估计或 RH 等价命题。

## 4. EXT-BG / EXT-Selberg / EXT-Vaughan

这些输入主要支撑 Tail-log4、RKS 与 D 组结构附录。

- `EXT-BG`：Bourgain--Garaev 倒数 Kloosterman 多线性节省；本文只需要固定对数节省。可辅以 Baker, *Kloosterman sums with prime variable*, Acta Arith. 156 (2012)。
- `EXT-Selberg`：Halberstam--Richert *Sieve Methods* 的 Selberg 上筛，或 Iwaniec--Kowalski Chapter 6；本文只用上界筛。
- `EXT-Vaughan`：Vaughan 恒等式与 Type I/II 分解，引用 Vaughan 1977 或 Iwaniec--Kowalski 相关章节；本文只用固定分块与固定对数损失。

这些引用不承担 PC1--PC4 主链的核心振荡或 Kloosterman 完成和角色；它们只用于已命名尾部/D 组附录，损失由全局对数常数层级吸收。

## 5. 引用闭合定理

**Theorem EXT-Maintext-Citation-Closure。** 当前 RH 反例矛盾场总攻稿中所有非初等外部解析输入均归入以下标签：

`EXT-KL`, `EXT-Vaaler`, `EXT-PC1-EF`, `EXT-PC1-LI`, `EXT-BG`, `EXT-Selberg`, `EXT-Vaughan`。

其中 `EXT-PC1-EF` 已有文内证明；`EXT-PC1-LI` 的有限边界情形已有文内证明，一般情形为经典 Landau--Ingham 外部定理；`EXT-KL`、`EXT-Vaaler`、`EXT-BG`、`EXT-Selberg`、`EXT-Vaughan` 均有明确标准文献来源和使用边界。因此外部引用层不产生新的数学假设或未命名接口。

**证明。** 第 1--4 节逐项列出所有外部输入的命题、来源和使用边界。此前主文链已把 NRC、PPI、DGap、尾项、PC1 分别接入这些标签。若某期刊要求页码或定理编号，按 `docs/ext-citation-final-audit.md` 和 `docs/bibliography.md` 补充即可，不改变证明逻辑。证毕。

## 6. 剩余编辑义务

1. 在最终 LaTeX/BibTeX 中把 `EXT-*` 标签替换为正式引用；
2. 给 Titchmarsh/Ingham 的 `EXT-PC1-LI` 补具体章节或定理号；
3. 给 Iwaniec--Kowalski/Katz 的 `EXT-KL` 补章节页码；
4. 全文统一“外部输入只按 EXT 标签引用”的格式。
