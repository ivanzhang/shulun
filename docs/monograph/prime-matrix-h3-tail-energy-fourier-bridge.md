# H3 尾标签能量到 Fourier/PDEC 的桥接引理

**状态：** `proved_deterministic_fourier_bridge_not_defect_exclusion`

本文补齐 `prime-matrix-h3-global-tail-energy-lemma.md` 的第二出口：

```text
TailEnergy(d,L)
=> 非零 Fourier/CRT 能量
=> H3-PDEC/ColumnCRT 入口。
```

该桥接是 Parseval 恒等式，不依赖随机模型；它不排斥缺陷，只把尾标签能量精确改写为可审查的
非零低模 Fourier 缺陷。

## 1. 设置

沿用 H3 符号。对 `ell>y`，令

\[
A_{s,\ell}=\{n\in A_s:P^-(n)=\ell\},
\qquad
N_\ell=\#A_{s,\ell}.
\]

对模数 `d>=2`，定义残基计数

\[
\mu_\ell(b;d)=\#\{n\in A_{s,\ell}:n\equiv b\pmod d\}.
\]

尾标签能量为

\[
E_y(d)=
\sum_{y<\ell\le p}
\sum_{b\bmod d}
\left(\mu_\ell(b;d)-{N_\ell\over d}\right)^2.
\tag{TEF-1}
\]

## 2. Fourier 形式

记

\[
\widehat\mu_\ell(a;d)=
\sum_{b\bmod d}\mu_\ell(b;d)e^{2\pi iab/d}.
\]

当 `a=0` 时，`\widehat\mu_\ell(0;d)=N_\ell`。Parseval 给出

\[
\sum_{b\bmod d}
\left(\mu_\ell(b;d)-{N_\ell\over d}\right)^2
=
{1\over d}\sum_{1\le a\le d-1}
\left|\widehat\mu_\ell(a;d)\right|^2.
\tag{TEF-2}
\]

对 `ell` 求和，得到精确恒等式

\[
E_y(d)=
{1\over d}
\sum_{y<\ell\le p}
\sum_{1\le a\le d-1}
\left|\widehat\mu_\ell(a;d)\right|^2.
\tag{TEF-3}
\]

因此 `E_y(d)>L` 等价于尾 first-factor 标签在非零低模频率上有总 Fourier 能量超过 `dL`。

## 3. PDEC/ColumnCRT 入口

定义 H3 尾频缺陷

\[
\mathcal F_y(d)=
\sum_{y<\ell\le p}
\sum_{1\le a\le d-1}
\left|\widehat\mu_\ell(a;d)\right|^2.
\]

由 `(TEF-3)`，

\[
E_y(d)>L
\quad\Longleftrightarrow\quad
\mathcal F_y(d)>dL.
\tag{TEF-4}
\]

这就是 `H3-PDEC/ColumnCRT` 的同口径入口：如果坏窗集合在同一个低模 `d` 上持续出现尾标签能量，
则其非零 Fourier 频率具有正能量；若只在孤立端点出现，则进入 `SAE`；若随行号持久旋转，则进入
`ColumnCRT`。

## 4. 单频见证

若需要单一见证，可由鸽巢原理得到：设

\[
\mathcal L_y=\{\ell:y<\ell\le p,\ A_{s,\ell}\ne\varnothing\}.
\]

若 `E_y(d)>L`，则存在 `ell in L_y` 与 `1<=a<=d-1` 使

\[
\left|\widehat\mu_\ell(a;d)\right|^2
>
{dL\over (d-1)\#\mathcal L_y}.
\tag{TEF-5}
\]

更强且更适合主链的是聚合形式 `(TEF-4)`，因为 PDEC 本来就是能量型排斥，而不是必须退化到单频
最大值。

## 5. 当前闭合状态

结合全局尾标签能量引理：

```text
M_H3(p,s)<B
=> C_y>#A_s-B-2L
   or F_y(d)>dL.
```

再结合小骨架 PDEC 桥接：

```text
M_H3(p,s)<B
=> D_y>V_y-B-2L
   or F_y(d)>dL.
```

因此第二出口已经完全转化为非零 Fourier/CRT 缺陷。剩余不是能量生成，而是证明这些缺陷在正式
坏窗族中不能持续，或会被 `PDEC/SAE/ColumnCRT` 证书排斥。
