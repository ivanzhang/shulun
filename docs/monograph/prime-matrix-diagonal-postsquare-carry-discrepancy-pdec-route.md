# 对角平方后端点 CarryDiscrepancy/PDEC 路线

**状态：** `carry_discrepancy_reduced_to_endpoint_reciprocal_phase`

本文接续 `RFP-Area` 的进位分解。低段与主量已经剥离后，面积尾段的最小硬点变为：

```text
CarryDiscrepancy:
P>=10007 时证明 D(P)<=1.98 sqrt(P)，
或把更大正偏差路由到 HyperbolicDisc/PDEC。
```

## 1. 精确设置

令

\[
y=\max(2,\lfloor P/e\rfloor),\qquad y<a<P,\qquad q=\lfloor P/a\rfloor,\qquad h=P-qa.
\]

由于 `a>P/e>P/3`，有 `q in {1,2}`。进位条件为

\[
\left\lfloor {P^2+P-1\over a}\right\rfloor-
\left\lfloor {P^2\over a}\right\rfloor
=q+1.
\]

写 `P=qa+h` 后，`P^2 mod a = h^2 mod a`。所以进位条件等价于

\[
(h^2\bmod a)+h>a,
\tag{CD-1}
\]

也就是

\[
\{h^2/a\}>1-h/a.
\tag{CD-2}
\]

定义

\[
C(P)=\sum_{y<a<P}1_{\{h^2/a\}>1-h/a},
\qquad
W(P)=\sum_{y<a<P}{h\over a},
\qquad
D(P)=C(P)-W(P).
\tag{CD-3}
\]

`W(P)` 是连续主量，`D(P)` 是分数部分偏差。它表面含有 `h^2/a`，但在平方后端点可继续化简为端点倒数相位。

## 2. 已剥离部分

低段有限证书：

```text
docs/diagonal_postsquare_lowband_finite_certificate_p2003_20260505.md
```

面积进位审计：

```text
docs/diagonal_postsquare_area_carry_audit_p10000_20260505.md
```

调和主量审计：

```text
docs/diagonal_postsquare_carry_main_identity_audit_p100000_20260505.md
```

给出：

```text
P<=2003: finite endpoint/dimension certificate closed；
2003<=P<10007: finite carry certificate covers RFP-Area；
P>=10007: CarryMain supplies at least 1.98 sqrt(P) by an elementary harmonic bound。
```

因此 `P>=10007` 的面积命题只需：

\[
D(P)\le1.98\sqrt P.
\tag{CD-4}
\]

## 3. 倒数相位化

由于

\[
\{P/a\}=h/a,\qquad \{P^2/a\}=\{h^2/a\},
\tag{CD-5}
\]

进位条件 `(CD-2)` 等价为

\[
\{P^2/a\}>1-\{P/a\}.
\tag{CD-6}
\]

所以

\[
D(P)=
\sum_{y<a<P}
\left(1_{\{P^2/a\}>1-\{P/a\}}-\{P/a\}\right).
\tag{CD-7}
\]

用 Fourier/Vaaler 展开后，核心频率对象不是一般二次和，而是

\[
S_r(P)=
\sum_{y<a<P}
e(rP^2/a)\bigl(1-e(rP/a)\bigr).
\tag{CD-8}
\]

这正是 `RSE` 的端点倒数相位核，参数为 `X=P^2,H=P,m=a~P,ell=1`。专门审计见：

```text
experiments/prime_matrix_diagonal_postsquare_carry_reciprocal_frequency_audit.py
docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p30000_20260505.md
docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p50000_20260505.md
docs/monograph/prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md
docs/monograph/prime-matrix-diagonal-postsquare-endpoint-reciprocal-osc-hard-attack.md
```

读数：

```text
10007<=P<=50000；
max D/sqrt(P)=1.285713 at P=36739；
64-frequency partial error/sqrt(P)=-0.082190 at that sample；
selected-sample max weighted |S_r|/sqrt(P)=2.975493。
```

## 4. PDEC 路由

若 `(CD-4)` 失败，则由 `(CD-7)` 可知

\[
\sum_{y<a<P}\left(1_{\{h^2/a\}>1-h/a}-{h\over a}\right)
>1.98\sqrt P.
\tag{CD-9}
\]

这是固定端点倒数相位偏差。用 Erdős-Turán/Vaaler 型不等式，可把它转成有限频率和：

\[
D(P)
\le
{N\over H+1}
+
\sum_{1\le r\le H}{1\over r}
\left|
\sum_{y<a<P} e(rP^2/a)(1-e(rP/a))
\right|
+ boundary(H),
\tag{CD-10}
\]

其中 `N=P-y-1`。因此若 `D(P)` 大于 `1.98sqrt(P)`，必有某个低频 `r<=H`
满足

\[
\left|
\sum_{y<a<P} e(rP^2/a)(1-e(rP/a))
\right|
\gg {\sqrt P\over \log H}.
\tag{CD-11}
\]

这正是 `HyperbolicDiscFailure/PDEC`：双曲端点倒数相位在固定端点窗口内出现非零频率集中。

## 5. 当前最小验收对象

后续只剩两种选择：

```text
CarryDiscrepancy-Analytic:
用 RSE-OSC / van der Corput / B-process 型倒数和界证明 D(P)<=1.98sqrt(P) for P>=10007。

CarryDiscrepancy-PDEC:
证明任何违反该界的低频相位集中都会生成已有 PDEC 证书，并被排斥。
```

这一步不再涉及素数、筛下界或短区间素数。它是纯粹的端点倒数相位问题，因而是当前 `RFP-Area` 的最小硬点。
