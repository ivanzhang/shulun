# 二次筛 TLI 总覆盖容量路线归档

日期：2026-05-01

## 本轮结论

TRC-1G-H 的逐点新模均衡要求可进一步弱化为平均型总覆盖容量不等式 TLI。

## 充分条件

设

\[
U_Y(I)=\{x\in I:q\nmid x(x-w)\ \forall q\le Y\}.
\]

若

\[
\sum_{Y<p\le P}A_p(I;Y)<|U_Y(I)|,
\qquad
A_p(I;Y)=\#\{x\in U_Y(I):p\mid x(x-w)\},
\]

则存在 `x` 不被任何 `p\le P` 命中。由于 `x,x-w<P^2`，这推出 `x` 与 `x-w` 都是素数。

## 模型常数

取 `Y=P^alpha`。CRT 均衡模型给

\[
\frac1{|U_Y|}\sum_{P^\alpha<p\le P}A_p
\approx
2\sum_{P^\alpha<p\le P}\frac1p
=2\log(1/\alpha)+o(1).
\]

当 `alpha=3/4` 时：

\[
2\log(4/3)=0.57536\ldots,\qquad
1-2\log(4/3)=0.42463\ldots .
\]

因此只要真实误差小于该余量，总覆盖无法全覆盖。

## 审稿边界

TLI 尚未无条件证明。普通上界筛可估计分子，但要与 `|U_Y|` 比较仍需要真实剩余集下界或等价的总均衡输入。大筛可限制大量模数同时异常，但不能单独推出点态或总量级的精确 `2/p` 主常数。因此当前二次筛命题仍为条件研究命题。
