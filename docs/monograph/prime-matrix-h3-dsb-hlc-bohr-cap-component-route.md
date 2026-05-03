# H3-DSB 高 lcm Bohr-cap 的组件路由

**状态：** `hlc_bohr_cap_component_route_proved_component_exclusion_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层已经证明：若 HLC formal unit 的 PDEC 上界失败，则存在非零频率 `h`、方向 `zeta`
和阈值 `alpha`，使 Bohr-cap

\[
\mathcal C_\alpha(h,\zeta)=
\{a\bmod R:\Re(\zeta e(ha/R))\ge\alpha\}
\tag{HBCR-1}
\]

承载显式质量。本文继续把这个帽集中拆成 gcd 层与短弧组件。

## 1. 有效模数分解

令

\[
d=(h,R),\qquad R'=R/d,\qquad h'=h/d.
\tag{HBCR-2}
\]

则 `(h',R')=1`。映射

\[
a\bmod R\longmapsto h'a\bmod R'
\tag{HBCR-3}
\]

在每个 `a mod R'` 类上有正好 `d` 个原像。因此 Bohr-cap 是商群 `Z/R'Z` 中一个余弦弧
的 `d` 重提升。

## 2. 组件长度

设

\[
\omega(\alpha)=\frac{\arccos(\alpha)}{\pi}\qquad(0\le\alpha<1).
\tag{HBCR-4}
\]

则 `cos` 正帽在单位圆上的相对长度为 `omega(alpha)`。因此 `\mathcal C_\alpha`
可写成至多 `d` 个等距提升组件的并：

\[
\mathcal C_\alpha=\bigcup_{\nu=1}^{J}\mathcal I_\nu,
\qquad J\le d,
\tag{HBCR-5}
\]

其中每个组件在商模 `R'` 上是一个连续弧，其长度满足

\[
|\mathcal I_\nu|
\le
d\bigl(1+\omega(\alpha)R'\bigr)
=
d+\omega(\alpha)R.
\tag{HBCR-6}
\]

这里 `1` 是端点取整损失；该界完全来自有限循环群几何。

## 3. 质量鸽巢

若 Bohr-cap 总质量为

\[
G_\alpha=\sum_{a\in\mathcal C_\alpha}g(a),
\tag{HBCR-7}
\]

则存在一个组件 `I_*` 满足

\[
\sum_{a\in I_*}g(a)\ge \frac{G_\alpha}{J}\ge \frac{G_\alpha}{d}.
\tag{HBCR-8}
\]

结合上一层的下界

\[
G_\alpha\ge\frac{L-\alpha U}{1-\alpha},
\tag{HBCR-9}
\]

得到单组件质量下界

\[
M_*
\ge
\frac{L-\alpha U}{d(1-\alpha)}.
\tag{HBCR-10}
\]

## 4. 二出口：高 gcd 或短弧集中

给定阈值 `D_0`，由 `(HBCR-10)` 得确定性二分：

```text
High-gcd cap:
  d=(h,R)>D0；

Short-arc cap:
  d<=D0，存在一个长度 <= d+omega(alpha)R 的组件承载
  >= (L-alpha U)/(D0(1-alpha)) 的 HLC 质量。
```

两者都不是新命题。

1. **High-gcd cap。** `d` 大说明失败频率只看见低有效模数 `R'=R/d`。这是低有效模集中，
   必须回到 `Clamp concentration / PDEC / ColumnCRT`。
2. **Short-arc cap。** `d` 小则存在一个短弧组件承载确定质量。该组件是同一 formal unit
   内的局部相位窗口；若跨行持久，它成为 PDEC 约束行，若孤立，则进入 `SAE/endpoint`。

## 5. 当前实际闭合度

本文完成：

1. Bohr-cap 的 `d=(h,R)` 有效模数分解；
2. 组件长度界 `(HBCR-6)`；
3. 单组件质量下界 `(HBCR-10)`；
4. 高 gcd / 短弧集中二出口。

本文仍未完成：

```text
排除 high-gcd cap 与 short-arc cap，
或把它们全部物化为通过的 PDEC/SAE/endpoint 证书。
```

这就是 Bohr-cap 层面的最窄剩余。

后续 high-gcd 下降见 `docs/monograph/prime-matrix-h3-dsb-hlc-high-gcd-descent.md`。该文证明
若 `d=(h,R)>D_0`，则失败频率和 Bohr-cap 质量都无损投影到 `R'=R/d`：
`\hat g_R(h)=\hat g_{R'}(h/d)`，且帽内质量保持。每次下降使有效模数至少缩小 `D_0`，
所以 high-gcd cap 不能作为独立出口，最终回到低有效模 PDEC/KLS 或 short-arc cap。
