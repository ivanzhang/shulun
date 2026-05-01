# I1 固定阶局部交叉复杂度闭合审查（2026-05-01）

## 目标

四项输入中的 I1 要证明：固定阶局部交叉估计不会暗中使用完整 CRT 周期，而只使用截断权重和局部测试，因此有效复杂度满足

\[
Q_{\mathrm{eff},k}\le(\log P)^{C_k}
\]

对固定 `k` 成立。

## 已补正文稿

正式证明已写入：

- `docs/monograph/two-point-secondary-sieve-research.md` 第 340--344 节；
- `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的 `Fixed-order local crossing complexity` 引理。

## 证明核心

固定 `k` 阶局部测试只包含：

1. `k` 条新筛线素数 `p_i`；
2. 固定相位 `0,w`；
3. 极短块平移 `|h_i|<L`；
4. 截断硬骨架模数 `d_i<=R`；
5. 截断系数总变差 `sum_{d<=R}|lambda_d|<=polylog(P)`。

对固定模式，所有约束是一元线性同余。CRT 给出：系统要么无解，要么是模

\[
\operatorname{lcm}(d_1,\ldots,d_k)\operatorname{lcm}(p_1,\ldots,p_k)
\]

的一个剩余类。因此区间计数为主项加 `O(1)` 边界项。

其中 `p_i` 是显式求和变量，贡献通常的 `Y^k` 尺度；历史复杂度只来自

\[
\operatorname{lcm}(d_1,\ldots,d_k)\le R^k,
\qquad
L^{O(k)}
\]

个平移模式，以及截断系数总变差。故

\[
Q_{\mathrm{eff},k}
\ll_k
\left(\sum_{d\le R}|\lambda_d|\right)^kR^kL^{O(k)}
\le(\log P)^{C_k}.
\]

## 审稿状态

I1 已闭合，且不再作为独立条件输入。它只闭合“有效复杂度不取完整 primorial”这一点；它不替代：

- I2：自适应真实命中分层与 Single-Prime CRTDefect；
- I3：SC2 二阶相关、45-Main、小 `q<=100` 有限包；
- I4：Zero Mass 加权 Bonferroni 与平滑回退。

后续已继续处理 I4；当前真正剩余集中到 I2 与 I3。
