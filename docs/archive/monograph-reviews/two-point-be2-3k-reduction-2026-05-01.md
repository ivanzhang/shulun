# BE2-3 无黑箱化攻坚：压缩到 BE2-3K（2026-05-01）

## 本轮突破

BMD 不需要完整 `max_a` 型 BV-E2。由于 Rosser/Buchstab 筛权是 well-factorable，BMD 只需固定剩余类 `2 mod d` 的加权分布：

`WBE2 => BMD`。

这比完整 BV-E2 更贴近 BFI dispersion 方法。

## dispersion 展开

对平衡 Type-II 块，定义

`T_r=sum_{d<=Q}lambda_d(sum_{s=2r^{-1} mod d} beta_s - phi(d)^{-1}sum_{(s,d)=1}beta_s)`。

由 Cauchy，

`|E|^2 <= (sum |alpha_r|^2)(sum |T_r|^2)`。

所以核心是强方差界 `sum |T_r|^2`。

## Kloosterman 核

展开方差后，非对角条件为

`r s1 = 2 mod d1`, `r s2 = 2 mod d2`。

CRT 解出 `r` 后，对区间指示作 Fourier 展开，非零频率产生相位

`e(-2h s1^{-1} d2^{-1}/d1 - 2h s2^{-1} d1^{-1}/d2)`。

这就是 BE2-3 的真实抵消来源。

## 最小硬核

`BE2-3K`：weighted bilinear Kloosterman dispersion。

逻辑链：

`BE2-3K => BE2-3 => WBE2 => BMD => BST-2 => BST => TLI`。

## 审稿边界

BE2-3K 已经不是普通筛论或方阵几何问题，而是 Kloosterman 双线性平均。完全无黑箱证明必须继续证明 BE2-3K；否则需引用 BFI/Deshouillers--Iwaniec/Kuznetsov 型工具。
