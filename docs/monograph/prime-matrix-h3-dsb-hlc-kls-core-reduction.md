# H3-HLC KLS-core 归约：把剩余障碍压成单一谱平均定理

**状态：** `hlc_kls_ext_reduced_to_single_core_spectral_mean`

本文继续只攻击同一命题内部的唯一剩余接口：

```text
HLC-KLS-ext for clean HLC windows.
```

上一层已经把 `(CKR-4)` 逐项适配到 DI/BFI/Kuznetsov 型窗口化 Kloosterman 输入。本文再前进
一步：把“引用 DI/BFI/Kuznetsov”压缩成一个单一、标准化、可审稿核查的核心平均定理
`HLC-KLS-core`，并证明该核心定理推出 `(CKR-5)`。

## 1. Clean HLC dyadic block

从 clean 窗口

\[
\mathcal K_{\rm HLC}(B)
=
\sum_{c\in B}\sum_{0<|h|\le H_0}
\beta_{c,h}
\sum_{y<\ell\le p}\alpha_\ell
e\!\left(-\frac{h\rho(c)\bar\ell}{R(c)}\right)
\sum_m \Lambda(m)W_{\ell,c}(m)e\!\left(\frac{hm}{R(c)}\right)
\tag{CORE-1}
\]

出发。按 `R(c)`、`h`、`\ell`、`m` 支持和权重标签作 dyadic/smooth 分块。K6 保证块数为
`\log^{O(1)}q`。一个 dyadic block 记为

\[
\mathscr D=(R_0,H_0,L_0,M_0,\mathcal C_0).
\]

在该块内：

```text
R(c)≈R0,      0<|h|<=H0,
ell≈L0,       m≈M0,
L0 M0 <= q+O(L0),   M0 <= q/L0+O(1).
```

K1 保证 `R0` 位于外部 KLS admissible level；high-lcm 质量不进入本文核心。K2--K5 保证频率、
端点、二范数和 gcd/unit 损失都已经进入多对数账本。

## 2. 标准化核心和

对一个 dyadic block，Vaughan/Heath-Brown 分解 `Lambda(m)` 后得到有限个 Type-I/Type-II
子块。每个子块都可写成如下标准核：

\[
\begin{aligned}
\mathfrak S(\mathscr D)
=
\sum_{c\in \mathcal C_0}\sum_{0<|h|\le H_0}
\gamma_{c,h}
\sum_{\substack{\ell\sim L_0\\(\ell,R(c))=1}}
a_\ell\,
e_{R(c)}(-h\rho(c)\bar\ell)
\sum_{m\sim M_0}
b_m\,V_{\ell,c,h}(m)\,e_{R(c)}(hm).
\end{aligned}
\tag{CORE-2}
\]

这里：

- `V_{\ell,c,h}` 是光滑紧支撑窗口，导数损失为 `log^{O(1)}q`；
- `a_\ell`、`b_m` 为 divisor-bounded 或 Type-I/II 分解后的二范数可控系数；
- `gamma_{c,h}` 吸收 `beta_{c,h}`、平滑分块权和 sawtooth/Fourier 权；
- 非单位层 `(ell,R(c))>1` 已由 K5 剥离，剩余只在单位群上求和。

定义该块的自然谱范数为

\[
\mathcal N(\mathscr D)
=
\left(\sum_{c,h}|\gamma_{c,h}|^2\right)^{1/2}
\left(\sum_{\ell\sim L_0}|a_\ell|^2\right)^{1/2}
\left(\sum_{m\sim M_0}|b_m|^2\right)^{1/2}
\mathfrak W(\mathscr D),
\tag{CORE-3}
\]

其中 `\mathfrak W(\mathscr D)` 记录 DI/BFI/Kuznetsov 谱大筛中由模数、频率和窗口长度产生的
标准尺度因子。对 clean HLC block，K1--K6 与 `(CKR-1)` 给出总预算

\[
\sum_{\mathscr D}\mathcal N(\mathscr D)\ll q\,\log^{C_{\rm blk}}y.
\tag{CORE-4}
\]

`(CORE-4)` 不是新的解析深输入；它只是 clean admission 的二范数、分块和窗口长度账本。

## 3. 唯一核心输入

**Theorem HLC-KLS-core（窗口化 Kloosterman 谱平均核心）。** 对每个 clean HLC dyadic/Type
block `\mathscr D`，若 K1--K6 admission 成立，则对任意 `A>0`，

\[
|\mathfrak S(\mathscr D)|
\le
C_A\,\frac{\mathcal N(\mathscr D)}{\log^A y}.
\tag{CORE-5}
\]

该定理的相位是标准 Kloosterman 逆元相位：

\[
e_{R(c)}(-h\rho(c)\bar\ell),
\]

即 `S(a,b;R)` 中 `b=-h\rho(c)` 的逆元项；`m` 方向的 `e_{R(c)}(hm)` 与平滑窗口进入
Poisson/Kuznetsov/BFI dispersion 的外层 Fourier 参数。

**审稿边界。** `(CORE-5)` 是现在唯一真正深输入。若引用 DI/BFI/Kuznetsov 型窗口化谱平均，
它就是外部定理；若要求完全自足，则必须从 Kuznetsov trace formula、谱大筛和 BFI
dispersion 开始证明 `(CORE-5)`。

## 4. `HLC-KLS-core => HLC-KLS-ext`

**命题。** 若 `HLC-KLS-core` 成立，则 `(CKR-5)` 成立：

\[
\mathcal K_{\rm HLC}(B)=O\!\left(\frac{q}{\log^2 y}\right).
\tag{CORE-6}
\]

**证明。**

1. **平滑分块。** 用单位分解把 `(CORE-1)` 拆成 `\log^{C_1}q` 个 dyadic block。
   K6 保证没有过度尾标签分裂；否则已经进入 tail-label concentration 出口。
2. **素数权分解。** 对每个 block 中的 `\Lambda(m)` 使用 Vaughan/Heath-Brown 分解。Type-I、
   Type-II 和端点块数为 `\log^{C_2}q`；端点超预算由 K3/endpoint 出口处理。
3. **单位与 gcd 剥离。** `(ell,R(c))>1` 或 imprimitive 层由 K5 剥离。不相容层为空；相容层
   只产生 `\tau(R(c))` 型多对数损失。
4. **标准化。** 每个剩余子块都有 `(CORE-2)` 形式。K4 的 L2-flat 估计供给
   `a_\ell,b_m,\gamma_{c,h}` 的二范数账本；K1--K2 供给模数与频率范围。
5. **调用核心定理。** 对每个子块以指数
   \[
   A_*=2+C_1+C_2+C_3+C_{\rm blk}+10
   \]
   调用 `(CORE-5)`，得到该子块贡献
   `<= \mathcal N(\mathscr D)/log^{A_*}y`。
6. **求和吸收。** 对全部 block 求和并用 `(CORE-4)`：
   \[
   |\mathcal K_{\rm HLC}(B)|
   \le
   \frac{1}{\log^{A_*}y}
   \sum_{\mathscr D}\mathcal N(\mathscr D)\log^{C_1+C_2+C_3}y
   \ll
   \frac{q}{\log^2 y}.
   \]

这正是 `(CKR-5)`。证毕。

## 5. 反例排斥链条

clean HLC residual 若承载 `q/log y` 级反例质量，则非零频率归约给出

\[
|\mathcal K_{\rm HLC}(B)|\gg q/\log y.
\tag{CORE-7}
\]

而 `(CORE-6)` 给出

\[
|\mathcal K_{\rm HLC}(B)|\ll q/\log^2 y.
\tag{CORE-8}
\]

对充分大 `y`，两式矛盾。因此在 `HLC-KLS-core` 成立或被外部定理引用时，clean HLC branch
不能存在。

## 6. 本步压缩后的唯一剩余

本步完成：

1. 把 `(CKR-4)` 的所有 dyadic/Type 子块写成同一个 `(CORE-2)`；
2. 把 `HLC-KLS-ext` 的证明压缩为 `HLC-KLS-core` 加多对数账本；
3. 明确 high-lcm、endpoint、coefficient concentration 不进入核心，而是已命名出口；
4. 把完全自足版缺口从“DI/BFI/Kuznetsov 总称”压缩为单一命题 `(CORE-5)`。

当前不应再重复拆 high-lcm 或 short-arc。剩余只有：

```text
prove HLC-KLS-core internally,
or cite an external windowed Kloosterman spectral/dispersion theorem that implies (CORE-5).
```

完全自足化证明脊柱见
`docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md`。该文把 `(CORE-5)`
继续拆成平滑 completion、标准 Kloosterman 二次型、系数二范数账本和唯一的
`Kuznetsov-LS atom (SC-9)`，并证明 `SC-9 => CORE-5`。因此当前唯一未内联证明的行已经
精确变为 `(SC-9)`，不是 high-lcm、short-arc、L2-flat 或普通 Weil 估计。
