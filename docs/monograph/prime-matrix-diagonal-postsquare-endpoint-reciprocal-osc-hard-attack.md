# 平方后端点 EndpointReciprocal-OSC 硬攻

**状态：** `hard_attack_contract_not_a_proof`

本文接续 `CarryDiscrepancy` 的倒数相位化。当前目标不是再寻找新的几何模型，而是证明一个明确的端点倒数相位不等式，或把失败转成 `PDEC` 证书。

## 1. 最小对象

尾段 `P>=10007` 已知只需

\[
D(P)\le 1.98\sqrt P.
\tag{ERO-1}
\]

其中

\[
D(P)=
\sum_{P/e<a<P}
\left(1_{\{P^2/a\}>1-\{P/a\}}-\{P/a\}\right).
\tag{ERO-2}
\]

Vaaler/Fourier 展开给出核心端点相位

\[
S_r(P)=
\sum_{P/e<a<P}e(rP^2/a)(1-e(rP/a)).
\tag{ERO-3}
\]

所以最小解析目标是控制

\[
\sum_{1\le r\le R}{1\over \pi r}\operatorname{Im} S_r(P)
\]

加上截断尾项。

## 2. 为什么这是 RSE-OSC

对应 `RSE` 参数：

```text
X=P^2；
H=P；
m=a~P；
ell=1；
h=r。
```

因此

\[
{hP_m\over \ell}\asymp rP,
\qquad P_m=X/M\asymp P.
\]

这远离 `ell≈hP_m` 的临界带，属于强振荡端。相位

\[
f_r(a)=rP^2/a
\]

满足

\[
f_r''(a)\asymp r/P,\qquad P/e<a<P.
\tag{ERO-4}
\]

标准 B-process/van der Corput 应给出 `sqrt(P)` 级抵消；真正难点是常数和 Fourier 截断账本，而不是是否有振荡。

更精确地，驻相点满足

\[
n={rP^2\over a^2},\qquad r<n<e^2r,
\]

从而

\[
a=P\sqrt{r/n},\qquad
f_r(a)+na=2P\sqrt{rn}.
\tag{ERO-5}
\]

端点因子同时变为

\[
1-e(rP/a)=1-e(\sqrt{rn}).
\tag{ERO-6}
\]

于是所有潜在无振荡驻相项 `rn=s^2` 都被 `(ERO-6)` 精确消去。这是当前最强的结构性新发现：危险平方共振不存在，剩余都是非平方根频率。

## 3. 证据账本

审计文件：

```text
docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p50000_20260505.md
docs/diagonal_postsquare_endpoint_bprocess_skeleton_r64_20260505.md
docs/diagonal_postsquare_bprocess_model_audit_r64_20260505.md
docs/diagonal_postsquare_bprocess_envelope_scan_p100000_20260505.md
docs/monograph/prime-matrix-diagonal-postsquare-ero-low-bprocess-envelope.md
```

读数：

```text
10007<=P<=50000；
top D samples=20；
frequency cutoff R=64；
max D/sqrt(P)=1.285713 at P=36739；
at that sample:
  partial/sqrt(P)=1.367904；
  abs budget/sqrt(P)=1.932652；
  error/sqrt(P)=-0.082190。
selected samples max abs budget/sqrt(P)=2.266653 at P=25939。
B-process skeleton R=64:
  stationary terms=13258；
  square stationary terms=171；
  square raw budget=0.283225；
  square weighted budget=1.743e-15。
B-process model audit:
  best kappa=1/8；
  RMSE=0.0019165；
  max abs error=0.004077。
B-process envelope scan, 10007<=P<=100000:
  prime_count=8363；
  failures over 1.55 = 0；
  max partial/sqrt(P)=1.369773 at P=36739；
  max core=1.180590；
  max positive tail=0.523830, but then core=0.362995；
  if core>=1.10, max tail=0.198029。
```

解释：

- 实际有符号低频量明显低于 `1.98`。
- 纯绝对值谐和预算在部分样本已超过 `1.98`，所以只靠粗糙的 `sum |S_r|/r` 上界可能常数不够。
- 必须保留有符号结构，或把绝对预算超标解释为非零频率集中缺陷。
- B-process 中最危险的平方共振项被端点因子完全杀掉；这给 `ERO-Low` 一个可攻的有限非平方频率账本。
- B-process 主项与真实低频量的误差在最大样本集上只有 `0.004` 量级，因此 `ERO-Low` 已经实质降为有限非平方三角包络。

## 4. 当前最窄合同

可审稿合同应拆成三块：

```text
ERO-Low:
  对 1<=r<=64 做 B-process，证明有限非平方三角包络 <=1.55。
  进一步拆为 CoreKernel-Lock + CoreTail-AntiLock + Edge-Remainder。
  或把失败转成 endpoint PDEC。

ERO-Tail:
  证明 r>64 的 Vaaler/Fejer 尾项 <=0.43 sqrt(P)
  或把尾部集中转成 HyperbolicDisc/PDEC。

ERO-Edge:
  单独处理等号边界 a=(P+1)/2 与 floor(P/e) 截断误差，
  证明其总贡献为 O(1) 并可被余量吸收。
```

常数 `1.55+0.43=1.98` 只是当前工作分配，不是最终定理常数。若后续审计或证明显示低频自然上界更接近 `1.65`，应相应收紧尾项或提高有限阈值。

## 5. 失败出口

若 `ERO-Low` 失败，则存在低频 `r` 使

\[
\left|\sum_{P/e<a<P}e(rP^2/a)(1-e(rP/a))\right|
\]

或其有符号投影异常大。这是固定端点双曲倒数相位集中，可直接作为 `HyperbolicDisc/PDEC` 的非零频率证书。

若 `ERO-Tail` 失败，则高频 Vaaler 尾部必须在很多相邻阈值处同步偏向同一侧。这等价于端点分数点

\[
(\{P^2/a\},\{P/a\})
\]

在窄边界层过密，也应路由为 `PDEC/SAE`：持续过密给低模相位缺陷，孤立过密给单窗逃逸证书。

因此平方后端点当前主攻不是新素数估计，而是：

```text
Endpoint reciprocal signed oscillation
or endpoint frequency defect exclusion。
```
