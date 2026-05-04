# TailParity 高素锚点能量路线

**状态：** `alpha_tail_tailanchor_energy_route_reduction_open`

上一层把高尾奇偶偏置写成未锁高素数 `q` 的单边零类锚点贡献。本文把“许多锚点同号累积”
继续压缩成二分：单锚点集中，或锚点二次能量异常。

## 1. 锚点贡献

沿用

\[
T_R(r)=\sum_{d\in A_r}\Psi_{R,r}(d)(\Theta_{R,y,r}(d)-1).
\tag{TER-1}
\]

由首锚展开，

\[
T_R(r)=\sum_{\substack{R<q\le y\\ q\nmid r}} A_q(r),
\tag{TER-2}
\]

其中

\[
A_q(r)=
-2
\sum_{\substack{d\in A_r\\ d\equiv0\ {\rm or}\ -r\pmod q}}
\Psi_{R,r}(d)
\prod_{R<\ell<q}\psi_{\ell,r}(d).
\tag{TER-3}
\]

## 2. 单锚/能量二分

设

\[
|T_R(r)|\ge T_0,
\qquad
N_R=\#\{q:R<q\le y,\ q\nmid r\}.
\tag{TER-4}
\]

对任意阈值 `Lambda>0`，至少发生一项：

1. **单锚点集中。**

\[
\max_q |A_q(r)|\ge \Lambda;
\tag{TER-5}
\]

2. **分散锚点能量。**

\[
\sum_q |A_q(r)|^2
\ge {T_0^2\over N_R},
\qquad
\max_q|A_q(r)|<\Lambda.
\tag{TER-6}
\]

第二式由 Cauchy--Schwarz 直接得到；阈值 `Lambda` 用于把第一分支剥离。

## 3. 单锚点集中出口

若 `(TER-5)` 成立，则存在明确的高素数 `q` 和两个剩余类 `0,-r mod q`，使低模符号函数

\[
\Psi_{R,r}(d)\prod_{R<\ell<q}\psi_{\ell,r}(d)
\tag{TER-7}
\]

在该单边零类上显著偏置。这是 `ColumnCRT/SAE` 证书：固定列相位、固定高素锚点、固定低模符号。

## 4. 分散能量出口

若 `(TER-6)` 成立，则展开平方得到大量成对锚点相关：

\[
\sum_{q_1,q_2}
\sum_{\substack{d_1,d_2\in A_r\\
d_i\equiv0\ {\rm or}\ -r\pmod {q_i}}}
W_{q_1}(d_1)W_{q_2}(d_2),
\tag{TER-8}
\]

其中 `W_q` 是 `(TER-7)` 的符号权。若这些相关集中在少数低模相位，进入 `PDEC/ColumnCRT`；
若只在单窗口偶发，进入 `SAE`；若完全分散，则需要 Rankin/large-sieve 型能量上界。

## 5. 当前最小硬点

`TailParity` 当前被压成：

```text
Single high-prime anchor concentration
or distributed tail-anchor energy.
```

本文只证明二分；还未排斥两个出口。下一步应对 `(TER-5)` 生成具体 `ColumnCRT/SAE` 证书模板，
并对 `(TER-6)` 建立锚点能量上界或回流 `PDEC`。
