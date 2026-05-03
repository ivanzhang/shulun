# H3-DSB 高 lcm high-gcd cap 的低有效模下降

**状态：** `hlc_high_gcd_descent_proved_lower_mod_exit_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层把 Bohr-cap 剩余拆成：

```text
high-gcd cap / short-arc cap.
```

本文专攻 `high-gcd cap`。目标是证明它不是独立逃逸，而是严格下降到更低有效模数的
PDEC/ColumnCRT 或 KLS 可控分支。

## 1. 投影 formal unit

固定 HLC formal unit `B`，模数为 `R`，相位计数为 `g(a)`。设失败频率满足

\[
d=(h,R)>1,\qquad R'=R/d,\qquad h'=h/d,\qquad (h',R')=1.
\tag{HGD-1}
\]

定义投影计数

\[
g'(b)=\sum_{\substack{a\bmod R\\ a\equiv b\pmod {R'}}}g(a),
\qquad b\bmod R'.
\tag{HGD-2}
\]

并记

\[
U'=\sum_{b\bmod R'}g'(b)=\sum_{a\bmod R}g(a)=U.
\tag{HGD-3}
\]

这是同一物理事件集合的低有效模投影，不改变事件质量，只遗忘 `R'` 纤维内坐标。

## 2. Fourier 系数精确下降

因为

\[
e\!\left(\frac{ha}{R}\right)
=
e\!\left(\frac{h'a}{R'}\right),
\tag{HGD-4}
\]

所以

\[
\sum_{a\bmod R}g(a)e\!\left(\frac{ha}{R}\right)
=
\sum_{b\bmod R'}g'(b)e\!\left(\frac{h'b}{R'}\right).
\tag{HGD-5}
\]

因此 high-gcd 失败频率不是高模新频率，而是低模 `R'` 上的普通非零频率。

## 3. Bohr-cap 也精确下降

对任意方向 `zeta` 与阈值 `alpha`，

\[
\{a\bmod R:\Re(\zeta e(ha/R))\ge\alpha\}
\tag{HGD-6}
\]

正是低模帽

\[
\{b\bmod R':\Re(\zeta e(h'b/R'))\ge\alpha\}
\tag{HGD-7}
\]

的全原像。因此帽内质量满足

\[
G_\alpha(R,h,g)
=
G_\alpha(R',h',g').
\tag{HGD-8}
\]

上一层得到的帽质量下界在下降后完全保留。

## 4. 严格下降和终止

若 `d>D_0`，则

\[
R'=\frac{R}{d}<\frac{R}{D_0}.
\tag{HGD-9}
\]

因此每次 high-gcd cap 都把有效模数至少缩小一个因子 `D_0`。迭代不可能无限进行；最多

\[
\left\lceil\frac{\log R}{\log D_0}\right\rceil
\tag{HGD-10}
\]

步后，必达到以下二者之一：

1. `R_eff` 进入 KLS-window/低模 PDEC 可控范围；
2. 当前失败频率满足 `(h,R_eff)<=D_0`，转入 short-arc cap。

## 5. 结论：high-gcd cap 不再是剩余硬点

由 `(HGD-5)` 与 `(HGD-8)`，high-gcd cap 的全部 Fourier 质量和 Bohr-cap 质量都无损下降
到低有效模数。由 `(HGD-9)`，该下降严格终止。因此：

```text
high-gcd cap
=> lower-effective-modulus PDEC/ColumnCRT or KLS branch
   or eventually short-arc cap.
```

本文仍未证明低有效模 PDEC/ColumnCRT 出口和 short-arc cap 不可能；但它证明 high-gcd cap
不能作为独立剩余障碍保留。

后续 short-arc 压力判据见
`docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-density-pressure.md`。该文证明若
short-arc 组件不产生局部密度尖峰，则必须满足显式标量不等式
`R(L-alpha U)/(D0(1-alpha)U(D0+omega(alpha)R)) <= 1+epsilon`；否则该组件强制进入
PDEC 局部密度约束或 `SAE/endpoint`。
