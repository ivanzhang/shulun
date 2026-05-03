# H3-DSB 高 lcm short-arc pressure 的参数优化与平坦残余

**状态：** `hlc_short_arc_pressure_optimizer_proved_flat_residual_kls_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层把 short-arc cap 压成密度压力公式。本文处理剩余的低压参数区：把它精确改写为
`t=L/U` 的一维阈值，并证明低压残余必然是相位平坦残余，可回到 KLS-window 系数范数
或 coefficient concentration 分支。

## 1. 归一化压力函数

令

\[
t=\frac{L}{U},\qquad \rho=\frac{D_0}{R},
\qquad
\omega(\alpha)=\frac{\arccos(\alpha)}{\pi}.
\tag{SAPO-1}
\]

其中 `0<t<=1`，`0<=alpha<t`。上一层压力公式等价于

\[
\mathcal P_{D_0,R}(t,\alpha)
=
\frac{t-\alpha}
{D_0(1-\alpha)(\rho+\omega(\alpha))}.
\tag{SAPO-2}
\]

定义最优压力

\[
\Psi_{D_0,R}(t)
=
\sup_{0\le\alpha<t}\mathcal P_{D_0,R}(t,\alpha).
\tag{SAPO-3}
\]

由于 `(SAPO-2)` 对 `t` 单调递增，`\Psi_{D_0,R}(t)` 也是单调递增。

## 2. 压力二分的精确形式

给定 `epsilon>0`，short-arc 分支满足确定性二分：

```text
若 Psi_{D0,R}(t)>1+epsilon，
  则存在 alpha 使 short-arc 局部密度尖峰触发 PDEC/SAE；

若无 PDEC/SAE 尖峰，
  则 Psi_{D0,R}(t)<=1+epsilon。
```

因此低压残余被精确描述为

\[
t\le\tau_{D_0,R,\epsilon},
\qquad
\tau_{D_0,R,\epsilon}
:=
\sup\{s\in[0,1]:\Psi_{D_0,R}(s)\le1+\epsilon\}.
\tag{SAPO-4}
\]

这一步没有经验拟合，也没有新增命题；它只是把 short-arc 低压区写成一维阈值。

## 3. 显式可审查下界

实际审稿时不必求完整上确界。任取 `0<lambda<1` 并置 `alpha=lambda t`，有

\[
\Psi_{D_0,R}(t)
\ge
\frac{(1-\lambda)t}
{D_0(1-\lambda t)(\rho+\omega(\lambda t))}.
\tag{SAPO-5}
\]

因此若某个 `lambda` 使

\[
\frac{(1-\lambda)t}
{D_0(1-\lambda t)(\rho+\omega(\lambda t))}
>1+\epsilon,
\tag{SAPO-6}
\]

则 short-arc 尖峰已经被强制。反之，低压残余必须满足 `(SAPO-6)` 对全部选择的
`lambda` 都失败。这给出一个可逐项核验的有限参数证书格式。

## 4. 低压残余推出 L2 平坦性

由 HLC PDEC 阈值定义，

\[
L^2=
\frac{R\sum_a g(a)^2-U^2}{R-1}.
\tag{SAPO-7}
\]

若低压残余成立，即 `t=L/U<=tau`，则

\[
\sum_a g(a)^2
\le
\frac{1+(R-1)\tau^2}{R}\,U^2.
\tag{SAPO-8}
\]

这是同一 formal unit 的 L2 平坦性约束。

进一步令 `A=#\{a:g(a)>0\}`。由 Cauchy 不等式，

\[
A
\ge
\frac{U^2}{\sum_a g(a)^2}
\ge
\frac{R}{1+(R-1)\tau^2}.
\tag{SAPO-9}
\]

所以低压残余不能是少数短弧或少数相位类集中；它必须在模 `R` 上有大支持。

## 5. 与 KLS/coefficient 分支的接口

`(SAPO-8)` 正是 Kloosterman window 中需要的系数二范数输入形态：

```text
低压 short-arc residual
=> L2-flat coefficient vector on the same HLC formal unit.
```

若 `(SAPO-8)` 失败，则 coefficient concentration 分支触发；
若 `(SAPO-8)` 成立，则该残余应进入低二范数 KLS-window 参数核验，而不是保留为
short-arc 新出口。

## 6. 当前实际闭合度

本文完成：

1. short-arc pressure 的一维最优函数 `Psi_{D0,R}(t)`；
2. 低压残余等价于 `t<=tau_{D0,R,epsilon}`；
3. 可审查的有限 `lambda` 压力证书 `(SAPO-6)`；
4. 低压残余推出 L2 平坦性 `(SAPO-8)` 与支持下界 `(SAPO-9)`；
5. 将低压残余接回 `KLS-window / coefficient concentration`。

本文仍未完成：

```text
为全部 HLC formal unit 选择 D0,epsilon,lambda 证书，
或证明 L2-flat residual 满足 KLS-window 的全部参数条件。
```

这就是 short-arc 低压残余的当前最窄剩余。

后续 KLS admission 接口见
`docs/monograph/prime-matrix-h3-dsb-hlc-l2-flat-kls-admission.md`。该文把 L2-flat residual
接入 KLS-window 的 K1--K6 核查表：有效模数、频率、平滑端点、系数二范数、gcd/unit 层、
dyadic/尾标签分块。任一失败项回到既有出口；全部通过时 residual 才可调用 KLS-window。
