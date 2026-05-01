# PC1 解析输入引用审查：显式公式、Landau--Ingham、权函数非湮灭

本文补强 `docs/rh-pc1-analytic-input-theoremization.md` 的审稿口径。PC1 的任务是：若存在离线零点 `ρ=β+iγ`, `β>1/2`，则构造平滑素数窗口异常

`σ(P_z(X_j)-P_z^0(X_j)) >= X_j^{β-o(1)}`。

本文把该任务拆成可引用的标准解析输入，并明确哪些部分是初等证明、哪些部分应在投稿版中引用外部定理。

外部输入的投稿级标准化矩阵见 `docs/rh-pc1-external-input-standardization-audit.md`。

## 1. 输入矩阵

| PC1 子命题 | 状态 | 引用/证明来源 | 输出 |
| --- | --- | --- | --- |
| 平滑显式公式 | 标准无条件 | `EXT-PC1-EF` 或 Mellin 反演逐行证明 | 零点项进入 `Ψ_W(X)` |
| 权函数非湮灭 | 初等函数分析 | 测试函数分离分布 `t^{ρ-1}` | 取 `\widehat W(ρ)≠0` |
| Landau--Ingham 振荡 | 标准无条件 | `EXT-PC1-LI` | 无穷多尺度 `X^{β-o(1)}` 大振荡 |
| 素数幂去除 | 初等 | `O(X^{1/2}log^C X)` | Chebyshev 素数权异常 |
| Chebyshev 到无权 | 初等/可选 | 局部 `logp=logX+O(1)` 与 pigeonhole | 固定对数损失 |

## 2. 平滑显式公式引用口径

**定理标签 `EXT-PC1-EF`。** 对 `W∈C_c^∞((0,∞))`，Mellin 变换快速衰减，且

`Ψ_W(X)=X\widehat W(1)-Σ_ρ X^ρ\widehat W(ρ)+E_W(X)`，

其中平凡零点与截线积分为低阶项，零点和按平滑权收敛。

投稿版可引用：Iwaniec--Kowalski 的 ζ 函数显式公式章节，或 Titchmarsh, *The Theory of the Riemann Zeta-function* 中 Perron/Mellin 显式公式。本文当前保留 Mellin 反演逐行证明，因此不依赖新猜想。

## 3. 权函数非湮灭

给定 `ρ`，线性泛函

`W -> \widehat W(ρ)=∫_0^∞W(t)t^{ρ-1}dt`

不可能在全部 `C_c^∞((0,∞))` 上恒为零。若要求 `W` 非负，可先取复值测试函数使积分非零，再用实部/虚部和小正 bump 组合得到实值或非负权；或者在最终稿中允许有限个实值权并取线性组合。该步骤是测试函数分离分布的初等事实。

## 4. Landau--Ingham 振荡引用口径

**定理标签 `EXT-PC1-LI`。** 若平滑显式公式的 Mellin/Laplace 变换在 `s=ρ` 有非可去奇点，且测试权不湮灭该奇点，则误差项不能在所有大尺度上为 `o(X^{β})`；更一般地，若 `β` 是离线零点实部上确界或由零点逼近，则存在无穷多尺度满足

`|Ψ_W(X)-X\widehat W(1)| >= X^{β-o(1)}`。

若存在孤立极大实部零点，并且同实部可见零点族有限，则该结论可由显式公式中的非零三角多项式直接证明。若存在同实部无限零点或只取上确界，则引用 Landau--Ingham 振荡定理，防止用有限三角多项式论证覆盖不足。

投稿版可引用：Ingham 关于素数计数误差振荡的定理、Landau oscillation theorem，或 Titchmarsh 中关于 ζ 零点导致 `ψ(x)-x` 振荡的标准推论。本文使用平滑权版本，证明方式是 Mellin 变换奇点不能被全局小误差解析延拓消除。

## 5. Chebyshev 权去除

显式公式自然给

`Σ_nΛ(n)W(n/X)-X\widehat W(1)`。

素数幂项为 `O(X^{1/2}log^C X)=o(X^{β-o(1)})`。因此得到素数 Chebyshev 权异常。若主链保留 Buchstab/Chebyshev 权，则无需进一步无权化；若需无权版本，则在固定 multiplicative 窗口中 `logp=logX+O(1)`，除以 `logX` 只造成对数损失，仍并入 `X^{o(1)}`。

## 6. PC1 引用闭合定理

**Theorem PC1-Analytic-Citation-Closure。** 在接受 `EXT-PC1-EF` 与 `EXT-PC1-LI` 的标准解析输入，且使用第 3、5 节的初等处理后，`docs/rh-pc1-analytic-input-theoremization.md` 的 `PC1-Analytic-Input` 可作为无条件解析输入引用：离线零点 `β>1/2` 推出无穷多平滑素数窗口异常 `X^{β-o(1)}`。

**证明。** 由权函数非湮灭选择 `W`。`EXT-PC1-EF` 给零点项显式公式。`EXT-PC1-LI` 给由可见离线零点导致的无穷尺度振荡。素数幂与权重转换由第 5 节吸收。证毕。

## 7. 剩余投稿义务

PC1 现在不再是结构黑箱；`docs/rh-pc1-external-input-standardization-audit.md` 已将其压缩为两个经典外部标签与三个初等步骤。但最终投稿仍需完成两项编辑义务：

1. 在 bibliography 中加入 `EXT-PC1-EF` 与 `EXT-PC1-LI` 的正式文献条目；
2. 决定主文保留 Chebyshev/Buchstab 权还是转无权素数计数，并在 PC2/PC3 中保持同一口径。
