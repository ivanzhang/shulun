# ERO-Low 的 B-process 包络压缩

**状态：** `ero_low_reduced_to_finite_nonsquare_envelope`

本文接续 `EndpointReciprocal-OSC`。目标是把低频部分从原始倒数和进一步压成一个有限非平方根三角包络。

## 1. B-process 主项

对

\[
S_r(P)=\sum_{P/e<a<P}e(rP^2/a)(1-e(rP/a))
\]

作 B-process。驻相点满足

\[
n={rP^2\over a^2},\qquad r<n<e^2r.
\]

归一化到 `sqrt(P)` 后，低频主项为

\[
\mathcal B_R(P)=
-\operatorname{Im}
\sum_{1\le r\le R}
\sum_{r<n<e^2r}
{r^{1/4}\over \sqrt2\,n^{3/4}\pi r}
\bigl(1-e(\sqrt{rn})\bigr)
e(2P\sqrt{rn}+1/8),
\tag{BEL-1}
\]

并附带端点截断余项。

若 `rn=s^2`，则 `1-e(sqrt(rn))=0`，所以平方共振项精确消失。剩余频率均为非平方根频率。

## 2. 模型校准

脚本：

```text
experiments/prime_matrix_diagonal_postsquare_bprocess_model_audit.py
```

报告：

```text
docs/diagonal_postsquare_bprocess_model_audit_r64_20260505.md
```

在 `docs/diagonal_postsquare_carry_reciprocal_frequency_audit_p50000_20260505.json`
的 20 个最大 `D/sqrt(P)` 样本上，扫描相位常数得到：

```text
best kappa = 1/8；
RMSE = 0.0019165；
max abs error = 0.004077。
```

这说明 `(BEL-1)` 几乎完全解释了真实 64 频有符号低频量；剩余应归入 `ERO-Edge`，不是新的主硬点。

## 3. 包络扫描

脚本：

```text
experiments/prime_matrix_diagonal_postsquare_bprocess_envelope_scan.py
```

报告：

```text
docs/diagonal_postsquare_bprocess_envelope_scan_p100000_20260505.md
docs/monograph/prime-matrix-square-row-wheel-rigidity.md
```

参数：

```text
10007<=P<=100000, P prime；
R=64；
threshold=1.55；
term_count=13258。
```

读数：

```text
prime_count=8363；
failure_count=0；
max partial/sqrt(P)=1.369773 at P=36739；
margin to 1.55 = 0.180227。
```

最大点的平方自由核贡献：

```text
core kernels {2,3,5,6,7,10,14,15,21,30,42}:
  core=1.171744；
tail signed contribution:
  tail=0.198029；
tail grouped abs:
  2.353211。
```

核心最大点：

```text
P=95093；
core=1.180590；
total=1.172998。
```

尾核分组绝对量最大点：

```text
P=76207；
tail_group_abs=2.712994；
tail signed=-0.098448；
total=0.137899。
```

尾核有符号正贡献最大点：

```text
P=86531；
tail=0.523830；
core=0.362995；
total=0.886826。
```

条件尾核表显示核心越高，尾核可正堆积越低：

```text
core>=0.80: max tail=0.306925；
core>=1.00: max tail=0.245942；
core>=1.10: max tail=0.198029。
```

因此 `ERO-Low` 的下一个真实硬点不是“尾核绝对值很小”，也不是“尾核正贡献全局小”。
尾核可以正到 `0.52`，但它不能和核心高峰同步。

## 4. 新二分接口

`ERO-Low` 应拆成：

```text
CoreKernel-Lock:
  小平方自由核 {2,3,5,6,7,10,14,15,21,30,42}
  的多频三角和不能同步超过约 1.25；
  若超过，则 P 同时落入多个 sqrt(d) Bohr cap，进入 endpoint PDEC/Diophantine defect。

TailKernel-Signed:
  非核心核的分组绝对量可大，正贡献也可达 0.52；
  但当 core>=1.0 时，tail 必须降到约 0.25 以下；
  若核心高峰与尾核正堆积同步，则抽取高维非平方根频率集中，进入 HyperbolicDisc/PDEC。

CoreTail-AntiLock:
  证明 core 与 tail 的联合上界，而不是分别证明二者很小。

Edge-Remainder:
  B-process 模型误差约 0.004 的量级，需升格为端点余项引理。
```

若三者分别给出

```text
CoreKernel-Lock <= 1.25；
CoreTail-AntiLock supplies tail <= 0.27 when core is high；
Edge-Remainder <= 0.03；
```

则得到

```text
ERO-Low <= 1.55。
```

这些常数是当前工作分配，不是最终定理常数。

## 5. 证明方向

核心核部分是有限维 Bohr-cap 排斥问题：坏点必须同时让若干

\[
2P\sqrt d \pmod 1
\]

落入短弧。由于 `d=2,3,5,6,7,10,...` 含多个二次域方向，这种同步若持续，应产生可命名的 endpoint PDEC。

离散轮筛版本中，同一核心结构表现为 `P^2 mod 210` 只有 6 个平方残基，
`P^2±k` 的低模候选集是 `U_W±P^2` 的刚性平移。核心相位高峰若与尾核正堆积同步，
必须同时尊重这些低模平移骨架，因此更适合转成 `Wheel-Core Lock` 的 CRT 缺陷证书。

尾核部分不适合用绝对值。应保留有符号结构，并证明尾核正堆积与核心高峰反锁定；
若失败，则失败本身就是非零频率集中证书。

因此当前最小硬点已经从原始倒数和变为：

```text
finite nonsquare trigonometric envelope
or endpoint PDEC certificate。
```
