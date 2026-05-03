# H3-DSB 高 lcm PDEC 失败的相位局部化

**状态：** `hlc_pdec_failure_localization_proved_bohr_cap_exclusion_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层把 persistent 高 `lcm` 出口压成同一 formal unit 的阈值检验：

```text
U_CRT(B)<L_HLC(B).
```

本文处理该检验失败时的精确形态：失败不再是自由缺口，而是某个非零频率方向上的
Bohr-cap 相位集中。该集中必须回流到 `SAE/endpoint` 或成为新的同口径 PDEC 约束行。

## 1. 失败对象

固定 HLC formal unit：

```text
R=R(B)；
g(a)>=0, a mod R；
U=sum_a g(a)；
L=L_HLC(B)。
```

若 PDEC 上界证书不能证明 `U_CRT<L`，则按 `h4-pdec-certificate-template.md` 的失败输出规则，
存在非零频率 `h` 与单位方向 `zeta`，使

\[
\Re\left\{\zeta\sum_{a\bmod R}g(a)e\!\left(\frac{ha}{R}\right)\right\}
\ge L.
\tag{HFL-1}
\]

记

\[
c_{h,\zeta}(a)=
\Re\left\{\zeta e\!\left(\frac{ha}{R}\right)\right\}\in[-1,1].
\tag{HFL-2}
\]

于是 `(HFL-1)` 等价于

\[
\sum_a g(a)c_{h,\zeta}(a)\ge L.
\tag{HFL-3}
\]

## 2. Bohr-cap 局部化引理

对任意 `0<=alpha<1`，定义相位帽

\[
\mathcal C_\alpha(h,\zeta)
=
\{a\bmod R:c_{h,\zeta}(a)\ge\alpha\}.
\tag{HFL-4}
\]

记

\[
G_\alpha=\sum_{a\in\mathcal C_\alpha(h,\zeta)}g(a).
\tag{HFL-5}
\]

因为帽内 `c<=1`，帽外 `c<alpha`，由 `(HFL-3)` 得

\[
L
\le
G_\alpha+\alpha(U-G_\alpha)
=
\alpha U+(1-\alpha)G_\alpha.
\tag{HFL-6}
\]

故

\[
G_\alpha
\ge
\frac{L-\alpha U}{1-\alpha}
\qquad(0\le\alpha<L/U).
\tag{HFL-7}
\]

特别取 `alpha=L/(2U)`，得到

\[
G_{L/(2U)}
\ge
\frac{L/2}{1-L/(2U)}.
\tag{HFL-8}
\]

当 `L<=U` 时，右侧至少 `L/2`。

## 3. 几何含义

集合 `\mathcal C_\alpha(h,\zeta)` 是模 `R` 上的 Bohr-cap：在商群
`Z/(R/(h,R))Z` 中，它是一段余弦正相位弧的原像。若记 `d=(h,R)`，则它由 `d`
个等距相位弧组成，每个弧的角宽为

\[
2\arccos(\alpha).
\tag{HFL-9}
\]

因此 PDEC 失败必产生如下具体结构：

```text
至少约 L/2 个 HLC 事件集中在同一非零频率 h 的正相位 Bohr-cap 中。
```

这比“PDEC 证书失败”更窄：失败相位、方向、帽阈值、帽内质量都可记录并审查。

## 4. 回流规则

`(HFL-7)` 给出的 Bohr-cap 集中只能有两个合法出口：

1. **持久相位帽。** 同一 `(R,h,zeta,alpha)` 帽集中跨多个坏行复现，则它本身就是新的
   admissible PDEC 约束来源；必须加入同一 formal unit 的 `A,b,E,e`。
2. **孤立相位帽。** 若帽集中只在少数行出现，则它是 `SAE/endpoint` 单窗局部化：
   需要用端点、镜像、列见证或 cofactor 位移排除该帽内事件。

因此，`U_CRT<L_HLC` 失败不会把论证带回 KLS 主项，也不会产生新命题。它只输出
一个可审查的相位帽集中证书。

## 5. 当前实际闭合度

本文完成：

1. PDEC 阈值失败 `=>` 非零频率方向 `(h,zeta)`；
2. 非零频率方向 `=>` Bohr-cap 质量下界 `(HFL-7)`；
3. 规范回流到同口径 PDEC 约束或 `SAE/endpoint`。

本文仍未完成：

```text
排除所有 Bohr-cap 集中，或把它们全部物化为通过的 PDEC/SAE 证书。
```

这就是当前剩余障碍的更窄形式。

后续组件路由见 `docs/monograph/prime-matrix-h3-dsb-hlc-bohr-cap-component-route.md`。该文令
`d=(h,R)`、`R'=R/d`，证明 Bohr-cap 是商群 `Z/R'Z` 上余弦弧的 `d` 重提升，
每个组件长度至多 `d+omega(alpha)R`，并由鸽巢给出单组件质量
`M_* >= (L-alpha U)/(d(1-alpha))`。因此剩余进一步拆为 high-gcd cap 或 short-arc cap。
