# HLC-KLS-core 完全自足化证明脊柱

**状态：** `hlc_kls_core_self_contained_spine_reduces_to_kuznetsov_large_sieve_atom`

本文继续只攻击同一个剩余命题：

```text
HLC-KLS-core (CORE-5).
```

目标是把“完全自足证明”拆成逐行可审查的内部步骤。结论必须诚实：本文完成了从 clean
HLC 标准核到谱大筛原子的所有代数、平滑、completion、范数和损失账本；若不引用外部
DI/BFI/Kuznetsov，唯一仍需内联证明的行是 `Kuznetsov-LS atom` 本身。

## 1. 起点：标准 clean block

核心块为

\[
\mathfrak S(\mathcal D)
=
\sum_{c\in \mathcal C_0}\sum_{0<|h|\le H_0}
\gamma_{c,h}
\sum_{\substack{\ell\sim L_0\\(\ell,R(c))=1}}
a_\ell e_{R(c)}(-h\rho(c)\bar\ell)
\sum_{m\sim M_0}
b_m V_{\ell,c,h}(m)e_{R(c)}(hm).
\tag{SC-1}
\]

K1--K6 已提供：

1. `R(c)≈R0`，且 high-lcm 已剥离；
2. `0<|h|<=H0`；
3. `V_{\ell,c,h}` 光滑，端点损失为多对数；
4. `a_\ell,b_m,\gamma_{c,h}` 的二范数进入 `\mathcal N(\mathcal D)`；
5. gcd/unit 层只付 `log^{O(1)}y`；
6. 分块数为 `log^{O(1)}y`。

因此不能再把失败归因于 high-lcm、endpoint、coefficient concentration 或 short-arc；
这些已经是 clean 假设外的命名出口。

## 2. Step A：平滑 completion

对固定 `(c,h,\ell)`，设

\[
F_{\ell,c,h}(m)=b_mV_{\ell,c,h}(m).
\]

用长度 `M0` 的平滑 Fourier completion 写成

\[
\sum_{m\sim M_0}F_{\ell,c,h}(m)e_{R(c)}(hm)
=
\sum_{|r|\le R(c)\log^{B_1}y/M_0}
\widehat F_{\ell,c,h}(r)\,
\mathcal E_{R(c)}(h+r)
+O_A(y^{-A}).
\tag{SC-2}
\]

其中 `\mathcal E_R(u)` 是模 `R` 的标准 additive completion 因子，且由 K3 的导数账本有

\[
\sum_r |\widehat F_{\ell,c,h}(r)|^2
\ll
\|b\|_2^2\log^{C_1}y.
\tag{SC-3}
\]

这是 Fourier 分部积分和 Parseval 的直接结果，不需要外部深定理。

## 3. Step B：逆元变量 completion

将 `ell≈L0` 的平滑截断也 completion 到模 `R(c)` 的单位群。对每个 smooth 子块，

\[
\sum_{\substack{\ell\sim L_0\\(\ell,R)=1}}
a_\ell U(\ell/L_0)e_R(-h\rho\bar\ell)
=
\sum_{|s|\le R\log^{B_2}y/L_0}
\widehat A(s)\,
S(s,-h\rho;R)
+O_A(y^{-A}),
\tag{SC-4}
\]

其中

\[
S(s,b;R)=\sum_{x\bmod R}^{*}e_R(sx+b\bar x)
\tag{SC-5}
\]

是标准 Kloosterman 和。并且

\[
\sum_s|\widehat A(s)|^2\ll \|a\|_2^2\log^{C_2}y.
\tag{SC-6}
\]

这一步也只是平滑 completion、单位群剥离和 Parseval；gcd/imprimitive 损失由 K5 吸收。

## 4. Step C：把核心块化为 Kloosterman 二次型

把 `(SC-2)` 与 `(SC-4)` 代回 `(SC-1)`，并把所有 completion 频率、dyadic 标签和 Type
标签吸收进一个新索引 `u`。得到

\[
\mathfrak S(\mathcal D)
=
\sum_{R\sim R_0}
\sum_{u\in\mathcal U(R)}
\eta_{R,u}\,S(a_u,b_u;R)
+O_A(y^{-A}),
\tag{SC-7}
\]

其中：

- `a_u` 来自 `ell` completion 频率；
- `b_u=-h\rho(c)` 与 `m` completion 频率合并后的逆元频率；
- `\eta_{R,u}` 是 `\gamma_{c,h}`、`\widehat A`、`\widehat F`、completion 权和分块权的乘积。

由 `(SC-3)`、`(SC-6)`、K4 和 Cauchy--Schwarz，

\[
\sum_{R\sim R_0}\sum_{u\in\mathcal U(R)}
|\eta_{R,u}|^2
\ll
\mathcal N(\mathcal D)^2\log^{C_3}y.
\tag{SC-8}
\]

因此 `CORE-5` 归结为一个单一谱大筛原子。

## 5. 唯一原子：Kuznetsov-LS

**Kuznetsov-LS atom.** 对任意支撑在同一个 clean HLC dyadic block 的系数 `\eta_{R,u}`，
若 `R≈R0`、频率范围由 K1--K3 给出、窗口导数损失为多对数，则对任意 `A>0`，

\[
\left|
\sum_{R\sim R_0}\sum_{u\in\mathcal U(R)}
\eta_{R,u}S(a_u,b_u;R)
\right|
\le
C_A
\left(
\sum_{R,u}|\eta_{R,u}|^2
\right)^{1/2}
\frac{\mathfrak W(\mathcal D)}{\log^A y}.
\tag{SC-9}
\]

该原子就是 Kuznetsov trace formula 加谱大筛在本文窗口族上的专门化。它不是普通大筛，
也不是单个 Kloosterman 和的 Weil 界。

## 6. `Kuznetsov-LS atom => CORE-5`

由 `(SC-7)` 和 `(SC-9)`：

\[
|\mathfrak S(\mathcal D)|
\ll_A
\left(\sum_{R,u}|\eta_{R,u}|^2\right)^{1/2}
\frac{\mathfrak W(\mathcal D)}{\log^A y}
+O_A(y^{-A}).
\tag{SC-10}
\]

再用 `(SC-8)`，并把 `log^{C_3}y` 损失并入指数，把 `A` 替换成 `A+C_3+10`，得到

\[
|\mathfrak S(\mathcal D)|
\le
C_A\frac{\mathcal N(\mathcal D)}{\log^A y}.
\tag{SC-11}
\]

这正是 `(CORE-5)`。因此：

```text
Kuznetsov-LS atom => HLC-KLS-core => HLC-KLS-ext => clean HLC contradiction.
```

## 7. 为什么点态 Weil 不能闭合

若只用点态 Weil

\[
|S(a,b;R)|\ll_\epsilon R^{1/2+\epsilon}(a,b,R)^{1/2},
\tag{SC-12}
\]

代入 `(SC-7)`，Cauchy 后只能给

\[
|\mathfrak S(\mathcal D)|
\ll
R_0^{1/2+\epsilon}
\left(\#\mathcal U\right)^{1/2}
\left(\sum_{R,u}|\eta_{R,u}|^2\right)^{1/2}.
\tag{SC-13}
\]

在 clean HLC 的临界窗口中，`\#\mathcal U` 包含模数、频率、completion 频率和 Type
标签的总族。`R_0^{1/2}(\#\mathcal U)^{1/2}` 只能给临界平方根级控制，不能产生任意
`\log^{-A}` 节省。也就是说，单模平方根抵消不能替代模数族与频率族上的谱平均抵消。

这排除了“用 Weil 一句闭合”的伪证明路线。

## 8. 当前完全自足闭合度

本文已经完成：

1. `CORE-5` 到标准 Kloosterman 二次型 `(SC-7)` 的平滑 completion；
2. 系数二范数账本 `(SC-8)`；
3. `Kuznetsov-LS atom => CORE-5` 的逐行推导；
4. 点态 Weil 路线不足的量级审查。

本文仍未完成：

```text
在文内证明 Kuznetsov-LS atom (SC-9)。
```

所以当前不能诚实宣称“完全自足无黑箱闭合”。真正下一步不是改命题，也不是重新拆 high-lcm；
而是继续在 `(SC-9)` 上展开 Kuznetsov trace formula、Bessel transform 和 spectral large
sieve 的完整证明，或明确引用外部定理。

进一步展开见 `docs/monograph/prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md`。
该文件把 `(SC-9)` 拆成 KZ-A--KZ-E：平滑化、Kuznetsov trace formula、Bessel transform
衰减、spectral large sieve、BFI/well-factorable dispersion 对数节省，并证明这些子原子
推出 `(SC-9)`。
