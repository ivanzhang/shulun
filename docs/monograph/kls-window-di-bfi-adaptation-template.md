# KLS-window 的 DI/BFI 外部定理适配模板

本文档完成外审前 H7 义务：把二点筛链条中的 `KLS-window` 精确改写为可由 Deshouillers--Iwaniec 谱 Kloosterman 大筛与 Bombieri--Friedlander--Iwaniec dispersion/well-factorable 权重框架引用闭合的适配表。

## 0. 审稿结论

在允许引用 DI/BFI 经典外部深定理的版本中，本文使用的链条为：

```text
DI spectral Kloosterman large sieve
+ BFI dispersion with well-factorable weights
=> KLS-window
=> BE2-3K
=> BE2-3
=> WBE2
=> BMD
```

该链条闭合的是二点筛中的 `BMD` 分布输入。它不等于二点筛终局命题的无条件闭合；终局仍需另行审查 `BMD=>TLI` 是否隐藏素数对下界或 parity barrier。

完全自足无黑箱版本仍未闭合：若不引用 DI/BFI，则必须从 Kuznetsov trace formula、谱大筛和 BFI dispersion 机制开始重证 `KLS-window`。

## 1. 外部输入

### 1.1 DI 谱 Kloosterman 大筛

来源：

Deshouillers, J.-M.; Iwaniec, H., *Kloosterman sums and Fourier coefficients of cusp forms*, Inventiones Mathematicae 70(2), 219--288, 1982, DOI `10.1007/BF01390728`.

本文只使用其功能性输出：Kloosterman 和在模数族、频率族和光滑权族上的平均抵消。点态 Weil 界不足以替代该输入。

### 1.2 BFI dispersion 与 well-factorable 权重

来源：

Bombieri, E.; Friedlander, J. B.; Iwaniec, H., *Primes in Arithmetic Progressions to Large Moduli. II*, Mathematische Annalen 277, 361--394, 1987.

本文只使用其功能性输出：well-factorable 筛权、Dirichlet 多项式卷积、dispersion 展开和 Kloosterman 平均之间的组合闭合。普通大筛不足以替代该输入，因为平衡块会差一个 `P` 量级。

## 2. 本文 KLS-window 形式

设

```text
C ≍ P/log^{O(1)}P,
S ≍ P,
0<|h|<=H<=P/log^{O(1)}P.
```

`KLS-window` 需要控制 gcd 剥离、well-factorable 分解和平滑截断后的窗口化 Kloosterman 二次型：

\[
\mathcal K_{\rm win}
\ll_A {N^2\over R\log^A P}.
\]

这里 `beta_s` 为 divisor-bounded 系数，`lambda_c` 为 well-factorable 模权，`h` 权来自 sawtooth/Fourier 截断。本文只需要任意对数节省，不需要超过 DI/BFI 标准平均抵消强度的点态估计。

## 3. 相位归一化

互素主层中出现的核心相位为

\[
e\!\left(
-2h{\overline{s_1}\,\overline{d_2}\over d_1}
-2h{\overline{s_2}\,\overline{d_1}\over d_2}
\right),
\quad (d_1,d_2)=1.
\]

令 `c=d_1d_2`，并令 `s` 为满足

\[
s\equiv s_1\pmod {d_1},\qquad s\equiv s_2\pmod {d_2}
\]

的 CRT 合并变量。则

\[
{\overline{s}\over c}
\equiv
{\overline{s_1}\,\overline{d_2}\over d_1}
+
{\overline{s_2}\,\overline{d_1}\over d_2}
\pmod 1.
\]

因此上述相位等于

\[
e_c(-2h\,\overline{s}),
\]

即标准 Kloosterman 逆元相位。若外层还有线性相位或平滑 Fourier 权，则进入标准

\[
S(a,b;c)=\sum_{x\bmod c}^{*} e_c(ax+b\overline{x})
\]

的 `a` 与 `b` 参数，其中 `b=-2h`。这就是本文 Kloosterman 核与 DI/BFI 输入的相位接口。

## 4. 非互素 gcd 层

当 `g=(d_1,d_2)>1` 时，相容性强迫

\[
s_1\equiv s_2\pmod g.
\]

不相容层贡献为零。相容层可写成模

\[
c=\operatorname{lcm}(d_1,d_2)=d_1d_2/g
\]

上的同类逆元相位，并额外携带：

1. `s_1≡s_2 mod g` 的稀疏约束；
2. `g` 的除数层求和；
3. 局部单位群剥离带来的 `tau(d_1d_2)` 型损失。

这些损失均为多对数级，可并入 `log^C P` 账本；它们不改变所需的任意 `log^{-A}` 节省。

## 5. 变量适配表

| 核查项 | 本文对象 | DI/BFI 对象 | 适配状态 |
|---|---|---|---|
| Kloosterman 相位 | `e_c(-2h \bar{s})` | `S(a,b;c)` 中的逆元相位 | 由 CRT 归一化完成 |
| 模数族 | `c,d≈P/log^{O(1)}P` | Kloosterman 模数与 dispersion level | dyadic 后匹配 |
| 频率族 | `0<|h|<=H<=P/log^{O(1)}P` | Fourier/Bessel 频率 | sawtooth 截断后匹配 |
| 逆元变量 | `s≈P`, `(s,c)=1` | Kloosterman 可逆类变量 | CRT 合并后匹配 |
| 系数 | divisor-bounded `beta_s` | Dirichlet 多项式系数 | dyadic 分块后匹配 |
| 权重 | `lambda_d` Rosser/Buchstab 权 | BFI well-factorable 权 | level 分解后匹配 |
| gcd 层 | `(d_1,d_2)=g` | 非互素模数层 | 相容层多对数损失 |
| 平滑 | dyadic、窗口、sawtooth | smooth compact weights | partial summation 吸收 |
| 目标强度 | `log^{-A}` | 任意对数节省 | 选大 `B(A)` 吸收损失 |

## 6. `B(A)` 损失账本

把所有非核心损失统一记为 `log^{C_0}P`。来源如下：

| 损失来源 | 规模 | 处理 |
|---|---|---|
| dyadic 分块 | `log^{C_1}P` | 有限块求和 |
| sawtooth Fourier 截断 | `log^{C_2}P` | 令 `H<=P/log^{B_2}P` |
| gcd strata | `log^{C_3}P` | 除数函数与相容层求和 |
| 端点平滑 | `log^{C_4}P` | partial summation |
| well-factorable 分解层数 | `log^{C_5}P` | BFI 权重分解吸收 |
| 系数 divisor bound | `log^{C_6}P` | 二范数账本吸收 |

给定目标 `A`，在外部定理中选择

\[
B(A)=A+C_0+10
\]

即可把所有多对数损失吸收到最终 `log^{-A}` 余量中。这里 `+10` 是安全缓冲；若最终稿抽取具体常数，可把 `C_i` 逐项固定。

## 7. 外部定理版命题

**Theorem H7-KLS-ext.** 接受 DI 谱 Kloosterman 大筛与 BFI dispersion/well-factorable 权重定理，并假设第 5 节变量条件成立，则本文的 `KLS-window` 成立。

**证明。** 先按 dyadic 分块和平滑截断把 BE2-3K 的非对角核化为有限个窗口块。gcd 剥离后，不相容层为零，相容层只付出第 4 节列出的多对数损失。互素主层由第 3 节的 CRT 恒等式化为标准逆元 Kloosterman 相位 `e_c(-2h\bar{s})`。`lambda_d` 的 Rosser/Buchstab 权由 well-factorable 分解进入 BFI dispersion 框架；`beta_s` 的 divisor-bounded 性和 dyadic 支持满足 DI 谱大筛的二范数输入。应用 DI/BFI 得到任意对数节省，再按第 6 节选择 `B(A)` 吸收所有分块、gcd、端点和平滑损失，得到 `KLS-window`。证毕。

**Corollary H7-BMD-ext.** 在外部定理版中，

```text
KLS-window => BE2-3K => BE2-3 => WBE2 => BMD.
```

因此 `BMD` 是 external-theorem closed。

## 8. 不能越界使用的结论

1. H7 不证明 `BMD=>TLI`；该转移仍是 H8。
2. H7 不证明固定差素数对非空性；它只提供一个有符号分布输入。
3. H7 不消除 parity barrier；若后续从 BMD 推出二点筛终局，必须单独展示 Buchstab 转移没有偷用目标下界。
4. H7 不使全书成为完全自足无黑箱证明；无黑箱版仍需重证 DI/BFI。

## 9. 外审前剩余动作

1. 最终 LaTeX 稿中给 DI/BFI 文献补正式 BibTeX 条目。
2. 若审稿人要求原文定理号，需逐页核对 DI/BFI 中对应的定理/命题编号。
3. H8 必须继续审查 `BMD=>TLI`，避免把外部分布输入误写成二点筛终局证明。
