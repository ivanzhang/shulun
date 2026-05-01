# PC1 外部解析输入标准化审查

本文补强 `docs/rh-pc1-analytic-input-citation-audit.md` 的剩余投稿义务：将 PC1 使用的 `EXT-PC1-EF` 与 `EXT-PC1-LI` 从命名标签标准化为可替换的外部定理/文内证明接口。本文只处理“离线零点推出平滑素数窗口异常”的解析输入，不宣称 RH 已证明。

其中 `EXT-PC1-EF` 的文内证明版本见 `docs/rh-pc1-explicit-formula-proof-appendix.md`。

## 1. PC1 要证明的精确输入

若 ζ 存在零点 `ρ=β+iγ`，`β>1/2`，则存在平滑紧支撑权 `W`、符号 `σ∈{±1}` 与无穷尺度 `X_j`，使

`σ(Ψ_W(X_j)-X_j\widehat W(1)) >= X_j^{β-o(1)}`。

去除素数幂后同样给 Chebyshev 素数权异常；若需要无权版本，局部除以 `logX` 只损失 `X^{o(1)}`。

## 2. EXT-PC1-EF：平滑显式公式

### 2.1 可引用版本

可引用任一标准版本：

- Titchmarsh, *The Theory of the Riemann Zeta-function*，Perron/Mellin 显式公式章节；
- Iwaniec--Kowalski, *Analytic Number Theory*，ζ 函数显式公式与 Mellin 反演章节。

所需形式为：对 `W∈C_c^∞((0,∞))`，

`Ψ_W(X)=X\widehat W(1)-Σ_ρ X^ρ\widehat W(ρ)+E_W(X)`，

其中平凡零点、极点截线和横向积分均为低阶或快速收敛项。

### 2.2 文内证明替代

若不引用教材，可用 Mellin 反演：

1. 写 `Ψ_W(X)=1/(2πi)∫ -(ζ'/ζ)(s)\widehat W(s)X^s ds`；
2. 由 `\widehat W(s)` 快速衰减移动积分线；
3. 穿过 `s=1` 与 ζ 零点得到主项和零点项；
4. 平凡零点与新竖线由快速衰减控制。

这是一段标准逐行证明，不依赖 RH 或其他猜想。

## 3. 权函数非湮灭

对固定 `ρ`，映射

`W -> \widehat W(ρ)`

是 `C_c^∞((0,∞))` 上非零连续线性泛函。若它对所有 `W` 为零，则分布 `t^{ρ-1}` 在 `(0,∞)` 上为零，矛盾。因此可选 `W` 使 `\widehat W(ρ)≠0`。

若需要实值非负权，先取复值 `W_0`，再取实部或虚部使配对非零；最后加一个足够小的正 bump 或使用有限实值权线性组合。该过程只改变常数，不改变 `X^β` 量级。

## 4. EXT-PC1-LI：Landau--Ingham 振荡

### 4.1 可引用版本

所需标准结论是：若 Dirichlet/Mellin 变换在边界 `Re s=β` 有不可消除奇点，且测试权不湮灭该奇点，则对应误差项不可能为 `o(X^β)`；更具体地，存在无穷尺度使误差达到 `X^{β-o(1)}`。

投稿版可引用：

- Landau oscillation theorem 的 Mellin/Laplace 形式；
- Ingham 关于 ζ 零点导致 `ψ(x)-x` 振荡的定理；
- Titchmarsh 中“零点推出 Chebyshev 函数振荡”的标准推论。

### 4.2 文内证明替代

若 `ρ` 是孤立极大实部零点，且同实部可见零点有限，则由显式公式得到有限三角多项式

`Σ_{β(ρ')=β} c_{ρ'} e^{iγ'logX}`。

该非零三角多项式在无穷多点有固定正实部，给 `X^β` 级振荡。

若同实部零点无限或只取上确界，则用 Landau--Ingham 定理避免有限多项式不足。该接口的有限边界零点文内证明与一般情形标准定理拆分见 `docs/rh-pc1-landau-ingham-oscillation-appendix.md`。此处必须引用标准振荡定理，不能用有限三角多项式偷换。

## 5. 素数幂与无权化接口

显式公式输出 `Λ(n)` 权。素数幂项满足

`Σ_{m>=2} Σ_{p^m≈X} logp · W(p^m/X) = O(X^{1/2}log^C X)`。

因 `β>1/2`，该项为 `o(X^{β-o(1)})`。因此异常来自素数项。

若主链使用无权素数计数，在固定 multiplicative 窗口内 `logp=logX+O(1)`，除以 `logX` 只产生对数损失，吸收到 `X^{o(1)}`。若主链保留 Chebyshev/Buchstab 权，则无需无权化。

## 6. PC1 标准化定理

**Theorem PC1-External-Input-Standardization。** PC1 所需外部解析输入可标准化为：文内证明的平滑显式公式 `docs/rh-pc1-explicit-formula-proof-appendix.md`、拆分审查的 Landau--Ingham 振荡 `docs/rh-pc1-landau-ingham-oscillation-appendix.md`，以及权函数非湮灭、素数幂去除和对数权转换三个初等步骤。接受这些标准输入后，离线零点 `β>1/2` 无条件推出 PC1 的平滑素数窗口异常。

**证明。** 由第 3 节选取不湮灭零点的权函数。第 2 节显式公式把该零点作为非零项写入 `Ψ_W(X)`。第 4 节 Landau--Ingham 振荡给无穷尺度上的 `X^{β-o(1)}` 异常。第 5 节处理素数幂和无权化。证毕。

## 7. 对总攻割集的影响

本文将 PC1 从“解析黑箱”降为一个文内显式公式证明、一个外部 `EXT-PC1-LI` 振荡定理和三个初等步骤。剩余编辑义务主要是给 `EXT-PC1-LI` 选定具体书目、章节或定理号；这不改变当前逻辑链。
