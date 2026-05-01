# BST-2 到 BMD 的最终改写审查

日期：2026-05-01

## 核心改写

BST-2 的单侧计数为

\[
\#\{(p,m):Y<p\le P,\ m>Y,\ pm\in I,\ pm-2\in U_Y\}.
\]

对旧素数 `q<=Y`，因为 `p,m` 非零，

\[
q|pm-2 \Longleftrightarrow pm\equiv2\pmod q.
\]

在 `(F_q^*)^2` 中，禁曲线 `pm=2` 有 `q-1` 个点，总点数 `(q-1)^2`，局部禁比例为

\[
\frac1{q-1}.
\]

因此 BST-2 是双素变量上的一维乘法筛。

## 最小输入

BMD（Biprime Multiplicative Dispersion）要求对 Rosser/Buchstab 筛权重有

\[
\sum_{d\le D}\lambda_d
\left(
\#\{(p,m):pm\in I,\ pm\equiv2\pmod d\}
-
\frac1{\varphi(d)}
\#\{(p,m):pm\in I\}
\right)
=o(|U_Y|).
\]

若 BMD 成立，则 BST-2 成立；若 BST-2 成立，则 TLI 闭合。

## 审稿边界

BMD 是双素 Type-II/dispersion 级估计。它比原始真实剩余均衡更具体，但不能由 CRT 局部代数直接推出。当前无条件证明仍缺这一项。
