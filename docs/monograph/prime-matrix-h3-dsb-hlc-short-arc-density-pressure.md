# H3-DSB 高 lcm short-arc cap 的密度压力判据

**状态：** `hlc_short_arc_density_pressure_proved_spike_exclusion_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层已经把 high-gcd cap 无损下降，剩余核心变成 `short-arc cap`。本文把 short-arc
从“相位短弧”压成显式密度压力不等式。

## 1. short-arc 输入

固定一个 HLC formal unit，模数为 `R`，总质量为 `U`，PDEC 失败阈值为 `L`。设
`0<=alpha<L/U`，并记

\[
\omega(\alpha)=\frac{\arccos(\alpha)}{\pi}.
\tag{SADP-1}
\]

在 short-arc 分支中，存在 `d<=D_0` 和一个相位弧组件 `I_*`，满足

\[
|I_*|\le W_\alpha:=D_0+\omega(\alpha)R,
\tag{SADP-2}
\]

且

\[
M_*:=\sum_{a\in I_*}g(a)
\ge
\frac{L-\alpha U}{D_0(1-\alpha)}.
\tag{SADP-3}
\]

这里 `(SADP-2)` 使用上一层的最坏 `d<=D_0` 统一化，避免把常数隐藏在组件选择里。

## 2. 密度放大因子

定义 short-arc 组件相对全局平均密度的放大因子

\[
\Pi_{\rm arc}
:=
\frac{M_*/|I_*|}{U/R}.
\tag{SADP-4}
\]

由 `(SADP-2)` 与 `(SADP-3)` 得到确定性下界

\[
\Pi_{\rm arc}
\ge
\frac{R(L-\alpha U)}
{D_0(1-\alpha)U\bigl(D_0+\omega(\alpha)R\bigr)}.
\tag{SADP-5}
\]

这就是 short-arc cap 的核心压力公式。

## 3. 无尖峰假设下的排斥判据

给定 `epsilon>0`。若同一 formal unit 满足局部无尖峰条件

\[
\sum_{a\in I}g(a)
\le
(1+\epsilon)\frac{U}{R}|I|
\tag{SADP-6}
\]

对所有长度不超过 `W_alpha` 的相位弧 `I` 成立，则 short-arc cap 必须满足

\[
\frac{R(L-\alpha U)}
{D_0(1-\alpha)U\bigl(D_0+\omega(\alpha)R\bigr)}
\le
1+\epsilon.
\tag{SADP-7}
\]

反过来，若

\[
\frac{R(L-\alpha U)}
{D_0(1-\alpha)U\bigl(D_0+\omega(\alpha)R\bigr)}
>
1+\epsilon,
\tag{SADP-8}
\]

则 short-arc cap 强制产生局部密度尖峰：

\[
\exists I,\ |I|\le W_\alpha,\qquad
\sum_{a\in I}g(a)>
(1+\epsilon)\frac{U}{R}|I|.
\tag{SADP-9}
\]

该尖峰是同一 formal unit 内的可审查对象。

## 4. 回流规则

`(SADP-9)` 的局部密度尖峰只有两个合法出口：

1. **持久短弧尖峰。** 若同一长度尺度与相位弧在多个坏行复现，则它给出新的 PDEC
   约束行：局部弧质量不能超过 `(1+epsilon)U|I|/R`。
2. **孤立短弧尖峰。** 若只在单行或少数行出现，则它是 `SAE/endpoint` 局部逃逸；
   必须用端点、镜像、列见证或 cofactor 位移排除。

因此 short-arc cap 不再是模糊相位异常，而是一个密度压力判据：

```text
SADP pressure > 1+epsilon
=> PDEC local-density row or SAE/endpoint.

SADP pressure <= 1+epsilon
=> 留下一个显式标量不等式待优化 alpha,D0,epsilon。
```

## 5. 当前实际闭合度

本文完成：

1. short-arc 组件质量和长度的统一下界/上界；
2. 密度放大公式 `(SADP-5)`；
3. 无尖峰假设下的排斥判据 `(SADP-7)`；
4. 尖峰强制回流到 PDEC 或 `SAE/endpoint`。

本文仍未完成：

```text
对全部 HLC formal unit 证明 SADP pressure > 1+epsilon，
或证明 pressure <=1+epsilon 的残余参数区由 KLS/PDEC/SAE 覆盖。
```

这就是 short-arc 层面的当前最窄剩余。

