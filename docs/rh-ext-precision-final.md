# EXT-Precision 最终化：外部定理精确适配表

本文补齐最终剩余输入 `EXT-Precision`。目标是把 LaTeX 主稿中的 restricted external inputs 升级为可审稿的外部定理包。U3 的精确引用定位表已写入 `docs/rh-u3-ext-reference-table.md`：文章级输入给出卷期页码，专著级输入给出章节/定理定位；纸质专著页码级核验属于投稿排版义务，不再是数学逻辑缺口。

## 1. EXT-PC1-EF / EXT-PC1-LI

**使用形式。** 平滑显式公式与 Landau--Ingham 振荡：若存在离线零点 `ρ=β+iγ`, `β>1/2`，则存在平滑权和无穷尺度使平滑 Chebyshev 误差为 `X^{β-o(1)}`。

**来源。** Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed.；Ingham, *The Distribution of Prime Numbers*；Landau oscillation theorem。有限边界零点情形已有文内证明链 `docs/rh-pc1-landau-ingham-maintext-chain.md`；无限边界或上确界情形的受限接口已由 `docs/rh-ext-pc1-li-precision-final.md` 固定。

**适配。** 主稿只需平滑权版本；有限边界零点情形文内证明，外部 LI 只用于无限边界或上确界情形；素数幂误差 `O(X^{1/2}log^C X)` 被 `β>1/2` 吸收。

## 2. EXT-KL

**使用形式。** 素数模 `p` 上非退化 Kloosterman 型和

`|Σ_{x∈F_p^*} e_p(ax+b/x)| <= 2p^{1/2}`，

不完全区间经完成法损失 `log p`。

**来源。** Iwaniec--Kowalski, *Analytic Number Theory*, Chapter 12；Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*。

**适配。** 本文只使用素数模、二项有理函数 `ax+b/x`、非退化情形。退化情形不调用 EXT-KL，而转入 FCT。单变量 NRC 入口的完整变量匹配、completion 对数损失和退化出口已在 `docs/rh-ext-kl-precision-final.md` 中单独固定。

## 3. EXT-Vaaler

**使用形式。** 一维区间指标的 Vaaler/Beurling--Selberg 三角多项式逼近，频率高度 `H`，积分误差 `O(H^{-1})`，系数 `O(min(|m|^{-1},|I|))`。

**来源。** Vaaler, *Some extremal functions in Fourier analysis*, Bull. AMS 12 (1985), 183--216。

**适配。** 本文只用一维截断；所有频率高度损失并入 `C_total`。

## 4. EXT-BG / Baker

**使用形式。** 倒数变量双线性/多线性 Kloosterman 型和给固定对数节省；prime-variable 子区间可用 Baker 显式估计。

**来源。** Bourgain--Garaev, arXiv:1211.4184；Baker, Acta Arith. 156 (2012), 351--372。

**适配。** 当前主稿只需固定对数节省，不需最优幂指数。若期刊要求显式常数，需另行从 Baker/BG 抽取数值版。

## 5. EXT-Selberg

**使用形式。** Selberg 上筛对有限线性同余条件给出上界；只用上界，不用素数渐近。

**来源。** Halberstam--Richert, *Sieve Methods*；Iwaniec--Kowalski Chapter 6。

**适配。** 筛维数固定，损失并入 `C_total`。

## 6. EXT-Vaughan

**使用形式。** Vaughan 恒等式与 Type I/II 分解；只需固定分块与对数损失。

**来源。** Vaughan, C. R. Acad. Sci. Paris 285 (1977), A981--A983；Iwaniec--Kowalski 的 Type I/II 分解章节。

**适配。** 不使用最优参数；损失并入 `C_total`。

## 7. EXT-Precision 定理

**Theorem EXT-Precision.** 当前主稿使用的所有外部解析输入均归入 `EXT-PC1-EF/LI`、`EXT-KL`、`EXT-Vaaler`、`EXT-BG/Baker`、`EXT-Selberg`、`EXT-Vaughan` 六组标准引用。每组在本文中只以受限形式使用，并且变量归一化与失败出口均已指定。因此外部输入层不再包含未命名数学假设。

**证明。** 逐项见第 1--6 节。PC1 使用平滑显式公式和振荡；NRC/DSO-E 使用 Kloosterman/Weil；区间截断用 Vaaler；Tail/RKS 使用 BG/Baker、Selberg、Vaughan。每个输入的使用范围均弱于或等于引用来源的标准形式；退化或适用失败均转命名出口。证毕。

## 8. 剩余排版义务

U3 精确引用表见 `docs/rh-u3-ext-reference-table.md`。文章级来源已经给出卷期页码；专著级来源给出章节/定理定位，具体页码可在最终排版时核对。`EXT-KL` 的主稿实际使用形式已由 `docs/rh-ext-kl-precision-final.md` 进一步细化；`EXT-PC1-LI` 的主稿实际使用形式已由 `docs/rh-ext-pc1-li-precision-final.md` 进一步细化。
