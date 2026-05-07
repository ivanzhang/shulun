# 对角平方后端点 CarryDiscrepancy 的倒数相位化

**状态：** `reduction_to_endpoint_reciprocal_phase_not_a_proof`

本文记录 `RFP-Area` 进位偏差的最新压缩。关键结论是：原先看似二次的
`CarryDiscrepancy`，在平方后端点 `x=P` 上完全退化为标准端点倒数相位和。

## 1. 精确恒等式

令

\[
y=\lfloor P/e\rfloor,\qquad y<a<P,\qquad q=\lfloor P/a\rfloor,\qquad h=P-qa.
\]

在该区间内 `q in {1,2}`，且

\[
\{P/a\}=h/a,\qquad \{P^2/a\}=\{h^2/a\}.
\tag{CRF-1}
\]

进位条件

\[
\{h^2/a\}>1-h/a
\]

因此等价为

\[
\{P^2/a\}>1-\{P/a\}.
\tag{CRF-2}
\]

所以

\[
D(P)=
\sum_{y<a<P}
\left(1_{\{P^2/a\}>1-\{P/a\}}-\{P/a\}\right).
\tag{CRF-3}
\]

这一步去掉了 `q` 与 `h` 的几何分段，是本轮最重要的结构压缩。

## 2. Fourier 对象

记 `e(t)=exp(2 pi i t)`。对

\[
F(x,u)=1_{x>1-u}-u
\]

作频率展开，正频率项给出

\[
D(P)
=
\sum_{r\ge1}{1\over \pi r}
\operatorname{Im}
\sum_{y<a<P}
e(rP^2/a)\bigl(e(rP/a)-1\bigr)
\]

在通常 Vaaler/Fejer 截断意义下附带可控边界项。于是自然的指数和是

\[
S_r(P)=
\sum_{y<a<P}
e(rP^2/a)\bigl(1-e(rP/a)\bigr).
\tag{CRF-4}
\]

这正是 `RSE` 中的端点倒数相位核，参数为

```text
X=P^2, H=P, m=a~P, ell=1, frequency=r。
```

由于 `ell=1`，该对象落在 `RSE-OSC` 振荡端，而不是 `RSE-CRIT` 临界带。

## 3. 数值审计

脚本：

```text
experiments/prime_matrix_diagonal_postsquare_carry_reciprocal_frequency_audit.py
```

报告：

```text
docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p30000_20260505.md
docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p50000_20260505.md
```

参数与读数：

```text
10007<=P<=50000；
candidate_count=3904；
freq=64；
max D/sqrt(P)=1.285713 at P=36739；
selected-sample max weighted |S_r|/sqrt(P)=2.975493；
selected-sample max unweighted reciprocal |T_r|/sqrt(P)=2.240281。
```

最大 `D` 样本 `P=36739` 中，64 频部分给出

```text
D/sqrt(P)=1.285713；
partial_error/sqrt(P)=-0.082190。
```

这说明实际偏差主要已被低频端点倒数相位解释；但该读数仍只是实验支持，不是证明。

## 4. 新最小接口

`RFP-Area` 的尾段当前可写成：

```text
P<=2003:
  lowband finite certificate。

2003<=P<10007:
  finite carry certificate。

P>=10007:
  CarryMain gives allowance-W >= 1.98 sqrt(P)；
  it remains to prove D(P)<=1.98 sqrt(P)。
```

借助 `(CRF-4)`，剩余硬点变为：

```text
EndpointReciprocal-OSC:
  用 RSE-OSC / van der Corput / B-process 型倒数和界控制
  sum_r Im S_r(P)/r，并证明 D(P)<=1.98sqrt(P)。

EndpointReciprocal-PDEC:
  若上述控制失败，则某些低频 S_r(P) 或截断尾部产生固定端点
  HyperbolicDisc/PDEC 非零频率证书。
```

进一步的硬攻合同见：

```text
docs/monograph/prime-matrix-diagonal-postsquare-endpoint-reciprocal-osc-hard-attack.md
docs/monograph/prime-matrix-diagonal-postsquare-ero-low-bprocess-envelope.md
docs/diagonal_postsquare_endpoint_bprocess_skeleton_r64_20260505.md
```

这比原来的“二次地板偏差”更窄：失败必须表现为
`e(rP^2/a)(1-e(rP/a))` 的端点倒数相位异常，而不是任意二次相位异常。

最新 B-process 骨架还显示：驻相相位为 `e(2P sqrt(rn))`，但所有平方共振 `rn=s^2`
都因端点因子 `1-e(sqrt(rn))` 精确为零。这把 `EndpointReciprocal-OSC` 的低频部分进一步压成
非平方根频率的有符号有限账本。

## 5. 对证明链的影响

原链：

```text
CarryDiscrepancy -> quadratic floor phase -> HyperbolicDisc/PDEC
```

应替换为：

```text
CarryDiscrepancy
=> endpoint reciprocal phase S_r(P)
=> RSE-OSC bound
   or HyperbolicDisc/PDEC endpoint frequency defect。
```

因此 `x=P` 平方后端点不再需要新建一套二次和理论；它应并入既有
`RSE/reciprocal-sum` 主线，并作为 `ell=1, m~P` 的端点振荡子问题审稿。
