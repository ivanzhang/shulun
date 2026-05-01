# 二次筛窗口压缩审查归档（2026-05-01）

## 审查结论

本轮补正澄清了一个逻辑口径：`w=2` 推出孪生素数猜想并不是否定证明的理由。若证明链确实独立、逐行、无缺口，则可以升级为无条件定理。随后 I1 固定阶局部交叉复杂度已被内联证明，I4 Zero-Mass 与平滑回退已放电为 I3 常数接口，I2 自适应分层已放电为贪心分层/Single-Prime CRTDefect 二分；当前仍保持条件状态的原因是：二次筛章节依赖的剩余 I3-Core 真实剩余相关定理尚未内联为独立验收的无条件证明。

## 显式窗口公式

设顶层参数 `Y=P^{3/4}`，并设固定阶有效复杂度满足

\[
Q_{\mathrm{eff}}\le C_Q(\log P)^C.
\]

对连续 `H(P)` 行窗口 `I`，有 `|I|=H(P)P+O(P)`。中高尺度 `K=2` 近交叉主误差为

\[
\operatorname{Err}_2(I)
\ll
\frac{Q_{\mathrm{eff}}Y^2}{|I|}
\ll
\frac{C_Q P^{1/2}(\log P)^C}{H(P)}.
\]

若给该误差分配预算 `\varepsilon_{\mathrm{SC2}}`，则当前条件链可支撑的显式行数阈值为

\[
H_{\min}^{\mathrm{cond}}(P;\varepsilon_{\mathrm{SC2}})
=
\left\lceil
\frac{C_Q}{\varepsilon_{\mathrm{SC2}}}
P^{1/2}(\log P)^C
\right\rceil.
\]

若不固定常数包，则采用渐近阈值

\[
H_{\min}^{\mathrm{asym}}(P)
=
\left\lceil P^{1/2}(\log P)^{C_*}\right\rceil,
\qquad C_*>C.
\]

## 文稿更新

- `docs/monograph/two-point-window-compression-and-unconditionality.md`：新增无条件化边界澄清与 `H_min` 公式。
- `docs/monograph/two-point-secondary-sieve-research.md`：第 335--339 节更新为显式窗口阈值版本。
- `paper/contradiction-field-monograph/contradiction-field-monograph.tex`：合著稿加入显式 `H_min^{cond}` 与渐近 `H_min^{asym}`。
- `docs/monograph/claim-status-table.md`：状态表更新窗口压缩公式与条件状态。

## 当前状态

当前二次筛窗口压缩命题的最强可审查表述为：

> 在 I1 固定阶复杂度引理、I2 分层二分、I4 放电引理和剩余 I3-Core 成立的条件下，后半方阵中的任意连续窗口可从约 `P/2` 行压缩到  
> `ceil((C_Q/eps) P^{1/2}(log P)^C)` 行；渐近写法为 `ceil(P^{1/2}(log P)^{C_*})`, `C_*>C`。

该归档不宣称已经无条件证明孪生素数或固定偶差素数对。
