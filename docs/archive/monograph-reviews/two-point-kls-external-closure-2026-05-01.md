# KLS-window 外部深定理版闭合审查（2026-05-01）

## 结论

KLS-window 已完成外部深定理版闭合关联。

逻辑链：

`DI + BFI => KLS-window => BE2-3K => BE2-3 => WBE2 => BMD`。

## 外部定理源

1. Deshouillers, J.-M.; Iwaniec, H., *Kloosterman sums and Fourier coefficients of cusp forms*, Inventiones Mathematicae 70(2), 219--288, 1982, DOI `10.1007/BF01390728`.

2. Bombieri, E.; Friedlander, J. B.; Iwaniec, H., *Primes in Arithmetic Progressions to Large Moduli. II*, Mathematische Annalen 277, 361--394, 1987.

## 变量匹配

- `d,c`：Kloosterman 模数/level；
- `h`：加法频率；
- `s`：逆元变量；
- `beta_s`：divisor-bounded Dirichlet 多项式系数；
- `lambda_d`：well-factorable Rosser/Buchstab 权重；
- `C,S,H≈P/log^{O(1)}P`：谱大筛/dispersion 的窗口尺度。

## 审稿边界

该闭合是“外部深定理版闭合”，不是“完全无黑箱自证”。若审稿要求文内重证 Kuznetsov trace formula、谱大筛和 BFI dispersion，则仍需新增长篇谱理论附录。

## 当前状态

二点筛 BMD 链条可以标为：

`external-theorem closed`。

不能标为：

`fully self-contained no-black-box closed`。
