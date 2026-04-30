# 参考文献与引用标签

本文件为审稿版附录使用的统一 bibliography 草稿。最终投稿时需转换为期刊要求的 BibTeX/LaTeX 格式。

## EXT 标签映射

投稿版正文统一引用以下标签，再由 BibTeX 展开为期刊格式：

- `EXT-KL` -> [Weil-Kloosterman]。建议正式来源：Iwaniec--Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, Chapter 12；或 Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* 的 Kloosterman 特例。
- `EXT-BG` -> [BG2012]。arXiv:1211.4184，标题与作者已核对。
- `EXT-Vaaler` -> [Vaaler-Beurling]。建议正式来源：Vaaler 的 Fourier extremal functions/Beurling--Selberg majorant-minorant 定理，或 Montgomery--Vaughan 中区间指标截断引理。
- `EXT-Selberg` -> [Selberg-Sieve]。建议正式来源：Halberstam--Richert 或 Iwaniec--Kowalski 中 Selberg 上筛基本引理。
- `EXT-Vaughan` -> [Vaughan]。建议正式来源：Vaughan 恒等式标准定理或 Iwaniec--Kowalski 的 Type I/II 分解。

当前附录中的外部引用不得再写成“标准事实”而不带 `EXT-*` 标签。

## [BG2012] Bourgain--Garaev reciprocals and multilinear Kloosterman

J. Bourgain and M. Z. Garaev, *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*, arXiv:1211.4184.

本文使用位置：

- `docs/rks-log-reference-audit.md`：引用匹配审查；
- `docs/rks-bridge-partition.md`：BG 覆盖区域；
- `docs/rks-parameter-audit.md`：RKS 参数账本；
- `docs/tail-log4-theoremization.md`：TL4-L 的 RKS-log 输入。

需引用的具体结果：

- Theorem `Kloost 1/2`：多线性倒数 Kloosterman，乘积长度 `>p^{1/2+ε}`；
- Theorem `Kloost double 18/37`：双线性倒数 Kloosterman 的不平衡区间版本；
- Corollary `th1KloostPrimespowerFull range`：素变量倒数和处理中的 Vaughan 分解与短侧 Weil 吸收范式。

## [Weil-Kloosterman]

标准 Weil 界 / Kloosterman 完成和界：对非退化有理函数完整和

`Σ_{t mod p}^{*} e_p(αt^{-1}+βt)`

有 `O(p^{1/2})` 上界；不完全区间和通过完成法多一个 `log p` 损失。

本文使用位置：

- `docs/nrc-theoremization.md`：NRC 非共振完成和；
- `docs/rks-bridge-partition.md`：短侧逐变量 Weil 吸收；
- `docs/rks-parameter-audit.md`：短侧 `<=P^{1/18}` 区域。

最终投稿可引用任一标准教材或 Deligne/Weil 曲线指数和定理的 Kloosterman 特例。

## [Selberg-Sieve]

Selberg 上筛与二维线性形式上筛基本引理。

本文使用位置：

- `docs/tail-log4-theoremization.md`：TL4-M1 二维线性 Selberg 上筛模板；
- `docs/tail-log4-theoremization.md`：TL4-M2 平均奇异级数账本；
- `docs/tail-log4-theoremization.md`：TL4-M3 平均大模数二元上筛。

最终投稿需给出标准上筛基本引理引用，并说明本文只使用上界筛，不需要 AP 中素数渐近。

## [Vaaler-Beurling]

Vaaler 多项式 / Beurling--Selberg majorant-minorant 截断，用于区间指标 Fourier 近似。

本文使用位置：

- `docs/tail-log4-theoremization.md`：TL4-L 低谱窗口展开；
- `docs/tail-log4-theoremization.md`：TL4-S 平滑与端点余项；
- `docs/rks-parameter-audit.md`：Vaaler 截断缓冲账本。

## [Vaughan]

Vaughan 恒等式与素数 von Mangoldt 和 Type I/II 分解。

本文使用位置：

- `docs/tail-log4-theoremization.md`：TL4-L 从素数 q 和到 Type I/II；
- `docs/rks-bridge-partition.md`：Type I/II 长度分区；
- `docs/rks-parameter-audit.md`：Vaughan 分块对数损失。

## [Brun-Titchmarsh]

Brun--Titchmarsh 型上界，仅作为背景安全上界；当前最终主链主要使用 Selberg 上筛平均版，不依赖单个大模数 AP 渐近。

## [Rudnev-RNRS]

Rudnev 点-平面 incidence 与 Roche-Newton--Rudnev--Shkredov sum-product 能量估计。当前最终接口索引中不作为主链必需引用；仅供历史探索段或后续增强版本使用。

## 最终 BibTeX 候选条目

- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory*, American Mathematical Society Colloquium Publications, vol. 53, American Mathematical Society, Providence, RI, 2004.
- Nicholas M. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Annals of Mathematics Studies, Princeton University Press, 1988.
- Jean Bourgain and M. Z. Garaev, *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*, arXiv:1211.4184.
- Roger C. Baker, *Kloosterman sums with prime variable*, Acta Arithmetica 156 (2012), no. 4, 351--372.
- Jeffrey D. Vaaler, *Some extremal functions in Fourier analysis*, Bulletin of the American Mathematical Society 12 (1985), no. 2, 183--216.
- Heini Halberstam and Hans-Egon Richert, *Sieve Methods*, London Mathematical Society Monographs, no. 4, Academic Press, 1974.
- R. C. Vaughan, *Sommes trigonométriques sur les nombres premiers*, C. R. Acad. Sci. Paris Sér. A-B 285 (1977), A981--A983.
