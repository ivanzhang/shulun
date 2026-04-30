# EXT 外部定理精确引用最终审查表

本表把 `docs/external-theorem-package.md` 的 `EXT-*` 输入落实为投稿可替换的参考文献条目和使用边界。其作用是审稿定位：正文可先引用 `EXT-*` 标签，LaTeX 定稿时再替换为对应书籍章节、定理或论文编号。

## 1. EXT-KL

**使用命题。** 素数模数 Kloosterman 完整和 Weil 界与不完全区间完成法：

`|sum_{x mod p}^* e_p(ax+b/x)| <= 2p^{1/2}`，不完全区间多 `O(log p)` 损失。

**首选引用。** Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory*, AMS Colloquium Publications, vol. 53, American Mathematical Society, 2004, Chapter 12 on trace functions/Kloosterman sums and completion.

**可替换引用。** Nicholas M. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Annals of Mathematics Studies, Princeton University Press, 1988, Kloosterman sheaf/Weil bound special case.

**本文使用位置。** `docs/nrc-theoremization.md`、`docs/d-structure-formal-appendix.md`、`docs/rks-bridge-partition.md`。

**审稿边界。** 本文只需要素数模数、二项有理函数 `ax+b/x` 的经典特例；不调用 Deligne 一般形式。

## 2. EXT-BG

**使用命题。** 倒数变量的双线性或多线性 Kloosterman 型和在 Bourgain--Garaev 覆盖区给出固定节省；本文只需任意固定对数节省。

**首选引用。** Jean Bourgain and M. Z. Garaev, *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*, arXiv:1211.4184.

**辅助显式引用。** Roger C. Baker, *Kloosterman sums with prime variable*, Acta Arithmetica 156 (2012), no. 4, 351--372.

**本文使用位置。** `docs/tail-log4-formal-appendix.md`、`docs/tail-log4-theoremization.md`、`docs/rks-log-reference-audit.md`、`docs/rks-bridge-partition.md`、`docs/rks-parameter-audit.md`。

**审稿边界。** 当前主链不要求抽取 BG 的最佳幂指数；`K_sieve_log_saving=128` 只需要固定对数节省。若审稿人要求全显式数值常数，可用 Baker 显式结果替换相应 prime-variable 子区间，并把剩余多线性区间保留为 BG 引用。

## 3. EXT-Vaaler

**使用命题。** 区间指标的三角多项式上下逼近，频率高度 `H`，积分误差 `O(H^{-1})`，Fourier 系数 `O(min(|m|^{-1}, |I|))`。

**首选引用。** Jeffrey D. Vaaler, *Some extremal functions in Fourier analysis*, Bulletin of the American Mathematical Society 12 (1985), no. 2, 183--216.

**本文使用位置。** `docs/tail-log4-formal-appendix.md`、`docs/tail-log4-theoremization.md`、`docs/d-structure-formal-appendix.md`、`docs/ab-to-d-interface-match.md`。

**审稿边界。** 本文只用一维区间指标的 Beurling--Selberg/Vaaler 截断；不使用高维极值函数。

## 4. EXT-Selberg

**使用命题。** Selberg 上筛基本引理及二维线性形式的上界筛模板。

**首选引用。** Heini Halberstam and Hans-Egon Richert, *Sieve Methods*, London Mathematical Society Monographs, no. 4, Academic Press, 1974, Selberg upper-bound sieve chapters.

**可替换引用。** Iwaniec--Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, Chapter 6 on elementary sieve methods.

**本文使用位置。** `docs/tail-log4-formal-appendix.md`、`docs/tail-log4-theoremization.md` 的 TL4-M 系列。

**审稿边界。** 本文只使用上界筛，不使用等差数列素数渐近或 Bombieri--Vinogradov 型平均定理。

## 5. EXT-Vaughan

**使用命题。** Vaughan 恒等式和 von Mangoldt 权 Type I/II 分解，分块只产生固定次对数损失。

**首选引用。** R. C. Vaughan, *Sommes trigonométriques sur les nombres premiers*, C. R. Acad. Sci. Paris Sér. A-B 285 (1977), A981--A983.

**可替换引用。** Iwaniec--Kowalski, *Analytic Number Theory*, Type I/II decomposition sections.

**本文使用位置。** Tail-log4 的素变量尾部锚求和、`docs/rks-bridge-partition.md` 与 `docs/rks-parameter-audit.md`。

**审稿边界。** 本文不需要 Vaughan 恒等式的最优参数，只需固定分块与固定对数损失；该损失由 `C_vaughan_blocks=10` 与 RKS 账本吸收。

## 6. 最终引用结论

五个 `EXT-*` 输入均已降为标准文献引用或明确论文引用。审稿版正文不再需要出现“标准事实”而无来源的表述；若期刊要求逐页定位，定稿阶段只需在上述首选引用中补页码或定理编号，不改变证明逻辑。
