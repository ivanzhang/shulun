# H3-HLC clean Kloosterman window 的 DI/BFI 外部适配

**状态：** `hlc_kls_external_adaptation_proved_external_theorem_self_contained_open`

本文只处理当前唯一剩余接口：

```text
HLC-KLS-ext for the clean HLC Kloosterman window (CKR-4).
```

目标不是改换命题，而是把 `docs/monograph/prime-matrix-h3-dsb-hlc-clean-kls-reduction.md`
中的 clean 窗口对象逐项接到可引用的 DI/BFI/Kuznetsov 型窗口化 Kloosterman 输入。

## 1. Clean HLC 外部定理模板

**Theorem HLC-KLS-ext（外部深定理版）。** 设 `B` 是 clean HLC formal unit。假设：

1. K1--K6 admission 全部成立；
2. `R(c)` 已限制在 KLS 可处理的 dyadic level 内，所有 high-lcm 质量已经由 HLC clamp/PDEC/SAE
   分支排除或剥离；
3. 有效频率满足 `0<|h|<=H_0`，高频 sawtooth 尾已进入 endpoint 账本；
4. `W_{\ell,c}` 为支持在 `J_\ell=I/\ell` 上的平滑窗口，端点误差为多对数损失；
5. 系数 `alpha_\ell`、`beta_{c,h}` 与 `Lambda(m)` 经 dyadic 分块和 Vaughan/Heath-Brown
   分解后满足 divisor-bounded/L2-flat 条件；
6. gcd 与非单位层只贡献 `log^{O(1)}q` 损失。

接受 Deshouillers--Iwaniec 谱 Kloosterman 大筛与 Bombieri--Friedlander--Iwaniec
dispersion/well-factorable 权重框架的窗口化形式后，clean HLC 窗口

\[
\begin{aligned}
\mathcal K_{\rm HLC}(B)
=
\sum_{c\in B}\sum_{0<|h|\le H_0}
\beta_{c,h}
\sum_{y<\ell\le p}\alpha_\ell
e\!\left(-\frac{h\rho(c)\bar\ell}{R(c)}\right)
\sum_m \Lambda(m)W_{\ell,c}(m)e\!\left(\frac{hm}{R(c)}\right)
\end{aligned}
\tag{HLC-KLS-1}
\]

满足

\[
\mathcal K_{\rm HLC}(B)
=O_A\!\left(\frac{q}{\log^A y}\right),
\tag{HLC-KLS-2}
\]

特别取 `A=2` 得到 `(CKR-5)`。

**审稿边界。** 该定理是外部深定理版输入；本文没有在此重证 Kuznetsov trace formula、
DI 谱大筛或 BFI dispersion。若要求完全自足版，剩余任务就是从这些谱/dispersion 工具
开始重证 `(HLC-KLS-2)`。

## 2. `(CKR-4)` 到标准 Kloosterman 窗口的变量适配

| 核查项 | `(CKR-4)` 对象 | 外部 KLS 对象 | 适配结论 |
|---|---|---|---|
| 模数 | `R(c)=lcm(r_-,r_+)` | Kloosterman 模数/dispersion level | K1 保证在低有效模 dyadic level；高 `R` 已由 HLC clamp 分支剥离 |
| 逆元变量 | `ell`, `(ell,R(c))=1` | Kloosterman 可逆类变量 | 相位含 `bar(ell)`，方向完全匹配 |
| 逆元相位 | `e(-h rho(c) bar(ell)/R(c))` | `S(a,b;R)` 的 `b\bar x` 相位 | 取 `b=-h rho(c)` |
| 线性相位 | `e(hm/R(c))` | `S(a,b;R)` 的 `ax` 或 Fourier 线性项 | 由 Poisson/dispersion 后进入标准线性参数 |
| 频率 | `0<|h|<=H_0` | Fourier/Bessel 频率 | K2 与 sawtooth 截断保证 |
| 窗口 | `m in J_ell=I/ell` | smooth compact window | K3 平滑端点保证，短窗口只增加平滑账本 |
| 素数权 | `Lambda(m)`, `alpha_ell` | Dirichlet polynomial coefficients | Vaughan/Heath-Brown 分解后进入 Type I/II 块 |
| 系数二范数 | `(CKR-1)` | 谱大筛二范数输入 | K4 直接供给 |
| gcd/unit | 非单位与共同因子层 | imprimitive/gcd strata | K5 保证只付多对数损失 |
| 分块 | dyadic、tail label | finite smooth decomposition | K6 保证分块数为多对数 |

因此 clean admission 的意义是：所有不能进入外部 KLS 的参数失败都已经命名为内部出口；
剩下的 `(HLC-KLS-1)` 正是窗口化 Kloosterman 平均输入。

## 3. 相位归一化

对每个 `c`，记 `R=R(c)`、`\rho=\rho(c)`。单位层中

\[
m\equiv \rho\bar\ell \pmod R
\]

的非零 Fourier 展开给出

\[
e_R(hm-h\rho\bar\ell).
\tag{HLC-KLS-3}
\]

把 `ell` 作为 Kloosterman 可逆变量 `x`，则 `(HLC-KLS-3)` 的逆元部分为

\[
e_R(b\bar x),\qquad b=-h\rho.
\tag{HLC-KLS-4}
\]

外部 DI/Kuznetsov 输入处理的标准核为

\[
S(a,b;R)=\sum_{x\bmod R}^{*}e_R(ax+b\bar x).
\tag{HLC-KLS-5}
\]

本文的 `ell` 方向没有额外线性 `a ell` 项时可取 `a=0`，有 dyadic/Poisson/dispersion
产生的线性项时并入 `a`；`m` 变量的 `e_R(hm)` 与平滑窗口进入外层 Fourier/Bessel 变换。
故 `(CKR-4)` 的相位属于标准 Kloosterman 逆元相位类。

## 4. 损失账本

把非核心损失统一写作 `log^{C_H}q`：

| 损失来源 | 来源条件 | 吸收方式 |
|---|---|---|
| dyadic 分块 | `ell,m,c,h` 分块 | K6，有限多对数块求和 |
| sawtooth 截断 | 有效频率 `H_0` | K2，选择外部节省指数 `A+C_H+10` |
| 窗口平滑 | `J_ell` 端点依赖 `ell` | K3，partial summation |
| von Mangoldt 分解 | `Lambda(m)` | Vaughan/Heath-Brown，Type I/II 块 |
| gcd/unit 层 | `(ell,R)>1` 或 imprimitive 模数 | K5，非相容层为零，相容层付除数函数损失 |
| 系数范数 | `alpha_\ell,beta_{c,h}` | K4 的 L2-flat 账本 |
| high-lcm 剥离 | `R(c)` 过大 | 不由 KLS 吸收，已路由到 HLC clamp/PDEC/SAE |

给定目标 `q/log^2 y`，外部定理调用时取任意对数节省指数 `A=2+C_H+10`，
所有损失吸收后得到 `(HLC-KLS-2)` 的 `A=2` 版本。

## 5. 与 clean reduction 的闭合关系

由 `prime-matrix-h3-dsb-hlc-clean-kls-reduction.md`：

```text
clean HLC residual
=> K1--K6 admission
=> clean Kloosterman window (CKR-4).
```

由本文外部适配：

```text
DI/BFI/Kuznetsov window input
=> HLC-KLS-ext
=> K_HLC(B)=O(q/log^2 y).
```

而 clean residual 若仍承载 H3 反例质量，则前层非零频率归约要求

```text
|K_HLC(B)| >> q/log y
```

在同一 formal unit 上成立。两者相差一个 `log y` 因子，矛盾。因此：

```text
clean HLC branch is closed in the external-deep-theorem version.
```

完全自足无黑箱版仍保留一个准确缺口：

```text
prove HLC-KLS-ext internally, i.e. reprove the needed DI/BFI/Kuznetsov window theorem.
```

进一步压缩见 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-reduction.md`。该文件把
`HLC-KLS-ext` 归约为单一核心谱平均命题 `HLC-KLS-core`，并逐步证明
`HLC-KLS-core => (CKR-5)`。因此完全自足版的真正剩余已经不再是宽泛的“DI/BFI 总称”，而是
证明或精确引用该核心 `(CORE-5)`。

## 6. 不能越界的结论

1. 本文闭合的是 `HLC-KLS-ext` 的外部定理适配，不是 DI/BFI 本身的重证。
2. 本文不把 high-lcm、endpoint、coefficient concentration 失败项交给 KLS；这些失败项必须
   继续由已命名的 HLC clamp/PDEC/SAE 出口处理。
3. 若投稿要求外部文献原文定理号，还需对 DI/BFI 原文做书目级逐条定位；这不改变本文的
   变量适配链，但属于最终外审前的引用精确化义务。
