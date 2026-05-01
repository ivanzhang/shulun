# 外部定理包与精确引用模板

本文件把最终审稿稿中使用的外部数学事实集中为可编号引用的定理包。正文和附录只引用下列标签，避免“标准事实”散落成黑箱。

## EXT-KL：Weil/Kloosterman 完整和与完成法

**定理 EXT-KL。** 设 `p` 为素数，`a,b in F_p` 不同时为零，则

`|sum_{x in F_p^*} e_p(ax+b/x)| <= 2 p^{1/2}`。

若 `I` 是区间，则不完全和满足

`|sum_{x in I, x!=0} e_p(ax+b/x)| <= C p^{1/2} log p`。

**引用来源。** 首选 Iwaniec--Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, Chapter 12；也可引用 Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* 的 Kloosterman 特例。本文只用素数模数、非退化有理函数的特例。

**使用位置。** `docs/nrc-theoremization.md`、`docs/d-structure-formal-appendix.md`、`docs/rks-bridge-partition.md`。

## EXT-BG：倒数 Kloosterman 多线性对数节省

**定理 EXT-BG。** 对素数模数 `p`，倒数变量的双线性或多线性 Kloosterman 型和在 Bourgain--Garaev 覆盖区域内给出固定幂或固定对数节省。本文只需任意固定 `log^{-B}p` 节省，且所有损失由 `K_sieve_log_saving=128` 吸收。

**引用来源。** Bourgain--Garaev, *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*, arXiv:1211.4184；prime-variable 显式补充可引用 Baker, *Kloosterman sums with prime variable*, Acta Arith. 156 (2012), no. 4, 351--372。

**使用位置。** Tail-log4 的 `TL4-L` 与 RKS-log 桥接文件。

## EXT-Vaaler：区间指标截断

**定理 EXT-Vaaler。** 任一区间指标可由频率高度 `H` 的三角多项式上下逼近，积分误差 `O(H^{-1})`，Fourier 系数满足 `O(min(|m|^{-1}, |I|))` 型界。

**引用来源。** Vaaler, *Some extremal functions in Fourier analysis*, Bull. Amer. Math. Soc. 12 (1985), no. 2, 183--216。

**使用位置。** `docs/tail-log4-formal-appendix.md`、`docs/tail-log4-theoremization.md`、`docs/d-structure-formal-appendix.md` 的层蛋糕平滑误差。

## EXT-Selberg：二维线性 Selberg 上筛

**定理 EXT-Selberg。** 对有限个线性同余条件给出的二维整数点集，Selberg 上筛给出只含局部密度与奇异级数的上界，误差由筛维数和对数损失控制。本文只使用上界筛，不使用等差数列中素数渐近。

**引用来源。** Halberstam--Richert, *Sieve Methods*, London Math. Soc. Monographs 4, Academic Press, 1974；也可引用 Iwaniec--Kowalski Chapter 6。

**使用位置。** Tail-log4 的 `TL4-M` 中谱平均二元上筛。

## EXT-Vaughan：Vaughan 恒等式与 Type I/II

**定理 EXT-Vaughan。** von Mangoldt 权可分解为 Type I、Type II 与可控余项；分块后只产生固定次对数损失。

**引用来源。** Vaughan, *Sommes trigonométriques sur les nombres premiers*, C. R. Acad. Sci. Paris Sér. A-B 285 (1977), A981--A983；也可引用 Iwaniec--Kowalski 的 Type I/II 分解章节。

**使用位置。** Tail-log4 的素变量尾部锚求和与 RKS-log 桥接。

## EXT-PC1-EF / EXT-PC1-LI：平滑显式公式与 Landau--Ingham 振荡

**定理 EXT-PC1-EF。** 对 `W∈C_c^∞((0,∞))`，平滑 Chebyshev 和满足标准 ζ 显式公式：主项来自 `s=1`，非平凡零点贡献为 `-Σ_ρ X^ρ\widehat W(ρ)`，平凡零点与截线积分为低阶项。文内证明版本见 `docs/rh-pc1-explicit-formula-proof-appendix.md`。

**定理 EXT-PC1-LI。** 若 ζ 存在离线零点 `ρ=β+iγ`, `β>1/2`，且平滑权不湮灭该零点，则平滑 Chebyshev 误差在无穷多尺度上有 `X^{β-o(1)}` 级振荡。

**引用来源。** 可引用 Titchmarsh, *The Theory of the Riemann Zeta-function* 中显式公式与 Landau 振荡定理，或 Ingham 关于素数计数误差振荡的标准定理；平滑权版本也可由 Mellin 反演与 Landau--Ingham 奇点原理逐行推出。

**使用位置。** `docs/rh-pc1-analytic-input-theoremization.md` 与 `docs/rh-pc1-analytic-input-citation-audit.md`。

## 审稿使用规则

- 所有外部输入在正文中只按 `EXT-*` 标签引用；
- 精确引用审查表见 `docs/ext-citation-final-audit.md`；
- 本文没有使用未命名的新解析数论猜想，所有非初等解析输入均归入上述七类标签。
