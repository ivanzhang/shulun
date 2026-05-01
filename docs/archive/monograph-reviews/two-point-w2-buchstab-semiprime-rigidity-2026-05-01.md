# w=2 的 Buchstab 半素数刚性数值审查

日期：2026-05-01

## 实验文件

- 脚本：`experiments/rb_tli_w2_scan.py`
- 结果：`docs/rb-tli-w2-scan.md`
- 大尺度结果：`docs/rb-tli-w2-scan-large.md`
- 参数结果：`docs/rb-tli-w2-alpha080.md`, `docs/rb-tli-w2-alpha085.md`

## 确定性刚性

取 `Y=P^alpha` 且 `alpha>2/3`。若 `x` 与 `x-2` 均避开所有 `q<=Y`，并且 `Y<p<=P` 命中 `x` 或 `x-2`，则互补商必为素数。

理由：互补商 `m<=P^{2-alpha}`，且没有素因子 `<=Y`。若 `m` 合成，则 `m>Y^2=P^{2alpha}`，与 `alpha>2/3` 矛盾。

实验中所有扫描均显示商素性失败数为 `0`。

## 主常数修正

真实条件命中均值不应使用 naive `2log(1/alpha)`，而应使用 Buchstab 条件主常数

\[
K(\alpha)=
\frac{2\log((2-\alpha)/\alpha)}
{1+\log((2-\alpha)/\alpha)}.
\]

实验对照：

| alpha | P | E_U D | K(alpha) | 1-E_U D |
|---:|---:|---:|---:|---:|
| 0.75 | 10007 | 0.691696 | 0.676220 | 0.308304 |
| 0.80 | 10007 | 0.589679 | 0.576984 | 0.410321 |
| 0.85 | 10007 | 0.477321 | 0.464233 | 0.522679 |

## 新最小攻坚命题

BST（二点 Buchstab 半素数转移稳定性）：

\[
\mathbb E_{x\in U_Y}D_Y^P(x)
\le K(\alpha)+\varepsilon_{\rm BST}(\alpha),
\qquad
\varepsilon_{\rm BST}(\alpha)<1-K(\alpha).
\]

若 BST 成立，则 TLI 成立并闭合二点筛命题。当前 BST 仍未无条件证明，但它比原 RB-TLI 更精确，且实验余量明显。
