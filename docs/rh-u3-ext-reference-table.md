# U3 EXT 精确引用与定理定位表

本文处理最终升级清单 U3：为 `EXT-PC1-LI/KL/Vaaler/BG/Selberg/Vaughan` 给出可审稿的精确书目、章节/定理定位和使用边界。结论：U3 在“章节/论文级精确定位”层面完成；纸质专著的具体页码仍属最终排版核验，不再是数学逻辑缺口。

## 1. 总表

| EXT 标签 | 主稿使用形式 | 精确来源 | 定位粒度 | U3 状态 |
|---|---|---|---|---|
| `EXT-PC1-EF` | 平滑显式公式、Mellin 反演、ζ 零点残数 | Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed. | 显式公式/Perron--Mellin 章节；主稿已给文内证明替代 | 完成，页码待排版核验 |
| `EXT-PC1-LI` | Landau--Ingham 振荡，无穷尺度 `X^{β-o(1)}` | Ingham, *The Distribution of Prime Numbers*；Titchmarsh--Heath-Brown；Landau oscillation theorem | PC1 受限接口见 `docs/rh-ext-pc1-li-precision-final.md` | 完成，页码待排版核验 |
| `EXT-KL` | 素数模非退化 `ax+b/x` Weil/Kloosterman 完成和 | Iwaniec--Kowalski, *Analytic Number Theory*, Ch. 12；Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* | IK Ch. 12；Katz Chs. 11--13 / Kloosterman sheaves | 完成 |
| `EXT-Vaaler` | 一维区间指标 Vaaler/Beurling--Selberg 多项式逼近 | Vaaler, “Some extremal functions in Fourier analysis,” Bull. AMS 12(2), 183--216 (1985) | 论文卷期页码精确 | 完成 |
| `EXT-BG` | reciprocal interval 与 multilinear Kloosterman 固定对数节省 | Bourgain--Garaev, arXiv:1211.4184, 70 pp. | arXiv 编号与 DOI 精确 | 完成 |
| `EXT-Baker` | prime-variable Kloosterman sums | Baker, “Kloosterman sums with prime variable,” Acta Arith. 156(4), 351--372 (2012) | 论文卷期页码精确 | 完成 |
| `EXT-Selberg` | 固定维线性同余条件的 Selberg 上筛 | Halberstam--Richert, *Sieve Methods*；Iwaniec--Kowalski Ch. 6 | HR Selberg sieve chapters；IK Ch. 6 | 完成，页码待排版核验 |
| `EXT-Vaughan` | Vaughan identity 与 Type I/II 分解 | Vaughan, “Sommes trigonométriques sur les nombres premiers,” C. R. Acad. Sci. Paris Sér. A-B 285, A981--A983 (1977)；Iwaniec--Kowalski Type I/II chapters | 论文页码精确；教材章节级 | 完成 |

## 2. 受限使用边界

- `EXT-PC1`：只用于平滑 Chebyshev/von Mangoldt 权；有限边界零点情形已文内证明，外部 LI 只覆盖无限边界或上确界情形。
- `EXT-KL`：只用于素数模、非退化二项相位 `ax+b/x`；退化相位转 `FCT`。
- `EXT-Vaaler`：只用于一维区间/短弧截断，频率高度损失并入 `C_total`。
- `EXT-BG/Baker`：只要求固定对数节省，不要求最优幂指数。
- `EXT-Selberg`：只使用上筛上界，不使用素数渐近。
- `EXT-Vaughan`：只使用固定分块与对数损失的 Type I/II 分解。

## 3. 对主稿 U3 的结论

U3 可标记为完成：所有外部输入均已有正式书目与章节/论文级定位，且主稿使用形式弱于标准来源。最终期刊排版仍应补齐专著页码或具体定理号，但该工作不改变当前逻辑链。

## 4. 已核验的公开来源记录

- Vaaler 论文公开记录：Bull. AMS 12(2), 183--216 (1985)。
- Baker 论文公开记录：Acta Arith. 156(4), 351--372 (2012)。
- Bourgain--Garaev 公开记录：arXiv:1211.4184，题名、作者和 DOI 可核验。
- Katz PDF 目录显示 Kloosterman sheaves 与 integral monodromy/equidistribution 章节，足以定位本稿受限的 Kloosterman sheaf 背景引用。
