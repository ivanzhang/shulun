# `q|w` 局部塌缩对 RB-TLI 的影响审查

日期：2026-05-01

## 局部事实

对奇素数 `q`，二次筛禁类为 `{0,w}`。

- 若 `q\nmid w`，禁类数为 `2`，局部允许密度 `1-2/q`。
- 若 `q|w`，两禁类重合，禁类数为 `1`，局部允许密度 `1-1/q`。

相对最硬情形的局部增益为

\[
\frac{1-1/q}{1-2/q}=\frac{q-1}{q-2}.
\]

固定 `w` 时，所有奇素因子给出有限奇异因子

\[
\prod_{\substack{q|w\\q>2}}\frac{q-1}{q-2}.
\]

## 对 RB-TLI 的影响

正确筛余密度为

\[
V_w(Y)=\frac12\prod_{\substack{3\le q\le Y}}\left(1-\frac{\nu_q(w)}q\right),
\qquad
\nu_q(w)=1_{q|w}+2\cdot1_{q\nmid w}.
\]

模型上：

\[
|U_Y(I)|\approx |I|V_w(Y),
\qquad
A_p(I;Y)\approx \frac{2}{p}|I|V_w(Y)
\]

对充分大的新素数 `p>Y>|w|` 成立。因此相对平均为

\[
\frac{\sum_{Y<p\le P}A_p}{|U_Y|}
\approx
2\sum_{Y<p\le P}\frac1p
=2\log(1/\alpha)+o(1).
\]

`q|w` 的塌缩因子在分子和分母中同步出现，主相对常数不变。

## 审稿结论

该刚性真实有用：它增大绝对候选密度、削弱小素同步峰、改善有限阈值。但它不能单独证明 RB-TLI。对全部偶数 `w` 的命题，最硬情形仍是 `w=2`，因为没有奇素 `q|w` 的塌缩增益。
