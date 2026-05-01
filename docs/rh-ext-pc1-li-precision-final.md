# EXT-PC1-LI 精确适配最终记录

本文专门消除 PC1 中 `EXT-PC1-LI` 的投稿级适配义务。它只服务于主稿命题 PC1：从一个离线零点 `ρ_0=β+iγ`、`β>1/2`，推出某个平滑 Chebyshev 窗口在无穷多尺度上有 `X^{β-o(1)}` 级异常。

## 1. 主稿实际使用形式

**Proposition EXT-PC1-LI-Restricted.** 设 `R_W(X)=Ψ_W(X)-X\widehat W(1)`，其中 `W∈C_c^∞((0,∞))`，且平滑显式公式中至少有一个可见离线零点族在边界实部 `β>1/2` 上未被 `\widehat W` 湮灭。则存在无穷尺度 `X_j→∞`，使

`|R_W(X_j)| >= X_j^{β-o(1)}`。

进一步按符号分成正负两类，至少一类无限，因此存在固定 `σ∈{±1}` 满足

`σR_W(X_j) >= X_j^{β-o(1)}`。

## 2. 文内已证明情形

若可见边界零点族 `Re ρ=β` 有限，则主稿已给出完整证明：

1. 平滑显式公式给
   `e^{-βu}R_W(e^u)=T(u)+o(1)`；
2. `T(u)` 是非零有限三角多项式；
3. 正交均方给 `lim U^{-1}∫_0^U |T(u)|^2du>0`；
4. 因而存在无穷 `u_j` 使 `|T(u_j)|` 有正下界；
5. 固定实/虚投影与符号子列给所需 `σ`。

因此有限边界情形不依赖外部振荡黑箱。

## 3. 外部引用覆盖情形

外部 `EXT-PC1-LI` 只覆盖有限三角多项式不能直接处理的两种情形：

- 同一边界实部上可见零点无限；
- `β` 是可见离线零点实部的上确界，由零点序列逼近。

在这两种情形中，若 `R_W(X)=o(X^{β-o(1)})` 在所有大尺度成立，则其 Mellin/Laplace 变换边界奇点会被解析延拓消除；这与显式公式中未湮灭的 ζ 零点奇点矛盾。这正是 Landau--Ingham 振荡原理在平滑 Mellin 形式下的使用。

## 4. 标准来源

- Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford, 1986：显式公式、零点与素数误差项的标准 Ω/振荡推论。
- Ingham, *The Distribution of Prime Numbers*, Cambridge Tracts in Mathematics and Mathematical Physics, No. 30, Cambridge University Press, 1932：素数误差项与 ζ 零点分布之间的经典 Ingham 振荡框架。
- Landau oscillation theorem：Dirichlet/Mellin 变换边界奇点不能与误差项全局过小同时成立的经典形式。

主稿只需要上述理论的弱形式：存在无穷大尺度上的 `X^{β-o(1)}` 级异常；不需要最优常数、短区间最优长度或零点密度定理。

## 5. 变量与权重匹配

- 主稿使用平滑紧支撑权 `W`，因此 Mellin 变换整函数且竖线快速衰减。
- 权函数非湮灭由测试函数分离分布保证；若需实值权，可取实部/虚部有限线性组合。
- 输出先为 von Mangoldt/Chebyshev 权异常；素数幂项为 `O(X^{1/2}\log^C X)`，由 `β>1/2` 吸收。
- 若后续使用无权素数计数，固定 multiplicative 窗口内除以 `log X` 只产生 `X^{o(1)}` 损失。

## 6. 审稿结论

`EXT-PC1-LI` 可以标记为精确适配完成：有限边界零点情形已由主稿逐行证明；无限边界或上确界情形归入经典 Landau--Ingham 振荡原理。剩余若有，只是最终排版时给 Titchmarsh/Ingham/Landau 对应章节或定理号的页码核验，不是新的数学假设。
