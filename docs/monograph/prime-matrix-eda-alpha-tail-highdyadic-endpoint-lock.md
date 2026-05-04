# AlphaTail 高 dyadic 块的单命中端点锁

**状态：** `alpha_tail_highdyadic_endpoint_lock_reduction_open`

本文接续 dyadic PDEC 证书。新的压缩点是：一旦证书所在模数块满足 `d>p-1`，每个模数在
对角短窗中最多命中一次，端点缺陷不再是一般锯齿和，而是一个带 Möbius 符号的 CRT 单命中计数。

## 1. 高块单命中

沿用

\[
H=p-1,\qquad y=\lfloor0.9p\rfloor.
\tag{HDL-1}
\]

对 squarefree `d|M_y`，令 `rho_d(p)` 为 `-p^2 mod d` 在 `{1,\ldots,d}` 中的正代表。

若 `d>H`，则

\[
N_d(p)=\mathbf 1_{\rho_d(p)\le H}.
\tag{HDL-2}
\]

**证明。**  
满足 `d|p^2+k` 的 `k` 必须同余于 `rho_d(p) mod d`。而 `1<=k<=H<d`，所以同余类在
短窗中至多出现一次，且出现当且仅当其正代表不超过 `H`。证毕。

于是对任意高块区间 `I\subset(H,\infty)`，

\[
E_I(p)=A_I(p)-H R_I,
\tag{HDL-3}
\]

其中

\[
A_I(p)=
\sum_{\substack{d\in I\\ d\mid M_y\\ d\ {\rm squarefree}}}
\mu(d)\mathbf 1_{\rho_d(p)\le H},
\qquad
R_I=
\sum_{\substack{d\in I\\ d\mid M_y\\ d\ {\rm squarefree}}}
{\mu(d)\over d}.
\tag{HDL-4}
\]

这就是高 dyadic 块的精确端点锁。

## 2. 符号分解

把 `mu(d)=+1` 与 `mu(d)=-1` 两部分分开：

\[
A_I^\pm(p)=
\#\{d\in I:d\mid M_y,\ d\ {\rm squarefree},\ \mu(d)=\pm1,\ \rho_d(p)\le H\},
\tag{HDL-5}
\]

\[
R_I^\pm=
\sum_{\substack{d\in I\\ d\mid M_y\\ d\ {\rm squarefree}\\ \mu(d)=\pm1}}
{1\over d}.
\tag{HDL-6}
\]

则

\[
E_I(p)
=
\bigl(A_I^+(p)-H R_I^+\bigr)
-
\bigl(A_I^-(p)-H R_I^-\bigr).
\tag{HDL-7}
\]

因此若

\[
E_I(p)\le-\tau,
\tag{HDL-8}
\]

则至少发生一项：

\[
A_I^+(p)\le H R_I^+-{\tau\over2},
\tag{HDL-9}
\]

或

\[
A_I^-(p)\ge H R_I^-+{\tau\over2}.
\tag{HDL-10}
\]

**证明。**  
若 `(HDL-9)` 与 `(HDL-10)` 都不发生，则

\[
A_I^+(p)-H R_I^+>-{\tau\over2},
\qquad
A_I^-(p)-H R_I^-<{\tau\over2}.
\]

代入 `(HDL-7)` 得 `E_I(p)>-\tau`，与 `(HDL-8)` 矛盾。证毕。

## 3. 结构含义

`(HDL-9)` 是偶 Möbius 模数的短端点命中亏损；`(HDL-10)` 是奇 Möbius 模数的短端点命中过剩。
二者都不是普通素数分布命题，而是固定二次相位

\[
\rho_d(p)\equiv -p^2 \pmod d
\tag{HDL-11}
\]

在一族 squarefree 低素模数上的端点偏斜。

结合 dyadic 归约可得：

```text
PrimeVoid
=> AlphaTailStrong
=> dyadic endpoint defect
=> 若缺陷块在 d>p-1，则发生 HDL-9 或 HDL-10。
```

这比一般 PDEC 更窄：反例必须让 `p^2` 在大量低素 squarefree 模数中同时落入或避开同一个
长度约 `p` 的端点弧。

## 4. 与现有刚性约束的接口

高块单命中可直接接入三个已建立出口。

1. **ColumnCRT。**  
   `rho_d(p)<=H` 等价于存在列 `k` 使所有 `q|d` 同时满足 `k≡-p^2 mod q`；
   这是列残基相位的交集事件。
2. **PDEC。**  
   `(HDL-9)` 或 `(HDL-10)` 若在无限多 `p` 上持续出现，就是明确的低素 squarefree 模数族端点偏斜。
3. **SAE。**  
   若偏斜只发生在稀疏单窗，则它成为 sparse endpoint escape，而不是全局均衡问题。

## 5. 审稿边界

已证明：

```text
高 dyadic 强负缺陷
=> 偶 Möbius 端点命中亏损 或 奇 Möbius 端点命中过剩。
```

尚未证明：

```text
HDL-9 与 HDL-10 不可能。
```

下一步最窄硬点是对 `(HDL-9)/(HDL-10)` 做 ColumnCRT/PDEC 能量化：证明这种符号端点偏斜若达到
`p/log p` 尺度，必产生可排斥的列相位集中或持久 Fourier 缺陷。
