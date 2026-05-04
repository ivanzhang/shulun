# EDA-TailCore：尾项核心桶吸收路线

**状态：** `tailcore_bucket_reduction_proved_absorption_open`

本文专攻 `EDA-BK` 二分后的第二出口：

```text
Tail/Core concentration.
```

目标是把尾项过大从“无法控制的包含排除尾项”改写成可审稿的乘法几何对象：

```text
大尾项
=> TailCoreBucket
=> Tail-anchor concentration 或 Distributed corridor saturation
=> Rankin/low-mod/PDEC/SAE 出口。
```

本步闭合的是前两层严格归约；最终吸收仍需 EDA 专用 Rankin 常数账本或低模尖峰证书。

## 1. EDA 尾关联质量

固定奇素数 `p`、早期行 `1<=x<=p`，令

\[
I_{p,x}=\{px+1,\ldots,px+p-1\}.
\tag{ETC-1}
\]

取奇数阶 `K` 与 cutoff `D`。定义尾关联集合

\[
\Omega_{p,K,D}(x)=
\{(n,d): n\in I_{p,x},\ d\mid n,\ d\mid M_{<p},\ \omega(d)\le K,\ d>D\}.
\tag{ETC-2}
\]

其绝对质量为

\[
U_{p,K,D}(x)=|\Omega_{p,K,D}(x)|.
\tag{ETC-3}
\]

对应的有符号尾项为

\[
R_{p,K,D}(x)=
\sum_{(n,d)\in\Omega_{p,K,D}(x)}\mu(d).
\tag{ETC-4}
\]

显然

\[
|R_{p,K,D}(x)|\le U_{p,K,D}(x).
\tag{ETC-5}
\]

因此，若 `EDA-BK` 中低模分支已排除，而反例仍存在，则必须有

\[
U_{p,K,D}(x)>T
\tag{ETC-6}
\]

的尾关联过量。

## 2. TailCoreBucket 分桶

把 `(n,d)` 写成

\[
n=ad.
\tag{ETC-7}
\]

对 `d` 的 dyadic 尺度、互补因子 `a` 的 dyadic 尺度、`\omega(d)` 和可选低模相位分块。
记有限分块族为 `\mathfrak C`。对桶 `C` 定义

\[
U_C(x)=|\Omega_{p,K,D}(x)\cap C|.
\tag{ETC-8}
\]

**定理 ETC-Bucket.**  
若 `U_{p,K,D}(x)>T`，则存在桶 `C\in\mathfrak C` 使

\[
U_C(x)>{T\over |\mathfrak C|}.
\tag{ETC-9}
\]

**证明。**  
若所有桶都不超过 `T/|\mathfrak C|`，求和得 `U_{p,K,D}(x)\le T`，矛盾。证毕。

这说明尾项失败必输出一个具体桶，而不是无结构误差。

## 3. 有符号尾项的奇偶失衡细化

对证明 `S_K>0` 真正危险的不是尾关联总质量，而是有符号尾项的负方向。将尾关联分成

\[
U^+_{p,K,D}(x)=\#\{(n,d)\in\Omega_{p,K,D}(x):\omega(d)\ {\rm even}\},
\tag{ETC-10}
\]

\[
U^-_{p,K,D}(x)=\#\{(n,d)\in\Omega_{p,K,D}(x):\omega(d)\ {\rm odd}\}.
\tag{ETC-11}
\]

则

\[
R_{p,K,D}(x)=U^+_{p,K,D}(x)-U^-_{p,K,D}(x).
\tag{ETC-12}
\]

**定理 ETC-SignedBucket.**  
若

\[
R_{p,K,D}(x)<-T,
\tag{ETC-13}
\]

则

\[
U^-_{p,K,D}(x)>U^+_{p,K,D}(x)+T.
\tag{ETC-14}
\]

进一步，对任意有符号分块族 `\mathfrak C`，记

\[
R_C(x)=U_C^+(x)-U_C^-(x).
\tag{ETC-15}
\]

若 `\sum_C R_C(x)<-T`，则存在一个桶 `C` 使

\[
R_C(x)<-{T\over |\mathfrak C|}.
\tag{ETC-16}
\]

**证明。**  
`(ETC-14)` 是 `(ETC-12)` 的直接改写。若所有桶均满足 `R_C(x)\ge -T/|\mathfrak C|`，
则求和得到 `\sum_C R_C(x)\ge -T`，与假设矛盾。证毕。

因此 Tail/Core 的真正危险形态是：

```text
奇数阶核心桶相对偶数阶核心桶出现显著过量。
```

这比只控制总尾质量更精确，也更适合接入低模 residue 或 Rankin 账本。

## 4. 桶到尾锚/走廊二分

固定一个桶，设

\[
A_0\le a<2A_0,\qquad D_0\le d<2D_0.
\tag{ETC-17}
\]

对每个互补因子 `a` 定义走廊

\[
\mathcal J_a(I_{p,x};D_0)=
\{d:D_0\le d<2D_0,\ ad\in I_{p,x}\}.
\tag{ETC-18}
\]

由于 `I_{p,x}` 长度为 `p-1`，

\[
|\mathcal J_a(I_{p,x};D_0)\cap\mathbb Z|
\le
1+{p\over a}.
\tag{ETC-19}
\]

称 `a` 为 `\theta`-饱和尾锚，若该走廊中满足桶条件的 `d` 数量至少为

\[
\theta\left(1+{p\over a}\right).
\tag{ETC-20}
\]

**定理 ETC-AnchorCorridor.**  
若某个桶 `C` 的质量为 `U`，则至少发生以下一项：

1. 存在 `\theta`-饱和尾锚；
2. 若不存在饱和尾锚，则
   \[
   U\le
   \theta\sum_{A_0\le a<2A_0}\left(1+{p\over a}\right).
   \tag{ETC-21}
   \]

**证明。**  
按 `a` 分解桶质量。若某条走廊达到 `(ETC-20)`，得到第一项；否则每条走廊贡献均小于
`\theta(1+p/a)`，求和得到 `(ETC-21)`。证毕。

因此，桶过大只有两种形态：

```text
单个或少数互补因子 a 承担过多尾核心  => Tail-anchor；
许多互补因子走廊同时接近裸容量      => Distributed corridor saturation。
```

## 5. Core 高重合解释

对固定 `n`，令

\[
u(n)=\#\{d:(n,d)\in\Omega_{p,K,D}(x)\}.
\tag{ETC-22}
\]

若 `u(n)` 很大，则 `n` 含有许多 `<p` 小素数组成的大 squarefree 核。这只能来自
`\omega_p(n)` 较大，进入 `CoreK` 高重合分支。若 `u(n)` 不大而总质量仍大，则许多不同 `n`
各承载尾核心，按 `n=ad` 分解后进入 TailCoreBucket/走廊分支。

这给出点态二分：

```text
大量尾核心集中在少数 n       => Core high-overlap；
大量尾核心分散在许多 n       => Tail corridor saturation。
```

## 6. Rankin 账本入口

对一个走廊族 `\mathcal A`，需要计数

\[
\#\{(a,d):a\in\mathcal A,\ d\in\mathcal J_a,\ d\mid M_{<p},\ \omega(d)\le K\}.
\tag{ETC-23}
\]

可使用有限 Rankin 权。对任意 `s>0`，

\[
1_{d\in[L_a,R_a]}
\le
\left({R_a\over d}\right)^s,
\tag{ETC-24}
\]

因此

\[
\#\{d\in[L_a,R_a]:d\mid M_{<p},\omega(d)\le K\}
\le
R_a^s
\sum_{\substack{d\mid M_{<p}\\ \omega(d)\le K\\ d\ge L_a}} {1\over d^s}.
\tag{ETC-25}
\]

这不是下界筛；它是安全上界账本，不触发 parity barrier。若 Rankin 账本小于允许预算，
该走廊族被吸收。若 Rankin 账本失败，则失败必须表现为某些 `d` 的低模 residue 尖峰或
固定核心复用过多，从而回流 `PDEC/SAE`。

## 7. 当前剩余

本步已经严格证明：

```text
Tail/Core concentration
=> TailCoreBucket
=> Tail-anchor concentration 或 Distributed corridor saturation。
```

尚未闭合的是：

1. **Tail-anchor 排斥：** 饱和尾锚必须进入 `SAE-anchor` 或 persistent tail-anchor defect；
2. **Distributed corridor absorption：** 不相交走廊族的 Rankin 账本要小于允许预算；
3. **Rankin failure routing：** 若账本失败，必须给出 low-mod core CRTDefect 并接入 `PDEC/SAE`。

下一步最小审计任务：

```text
EDA-TailCore-Audit:
for thin EDA rows, measure U_{p,K,D}, top buckets, anchor concentration, and Rankin pressure.
```

## 8. 首轮审计事实

脚本：

```text
experiments/prime_matrix_eda_tailcore_audit.py
```

命令：

```text
python3 experiments/prime_matrix_eda_tailcore_audit.py --selected 101,199,499 --K 5 --D 100 --top 2
```

最薄行摘要：

| p | min row x | U | S5 | tail mass | even tail | odd tail | signed tail |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 101 | 73 | 7 | 7 | 123 | 65 | 58 | 7 |
| 199 | 179 | 12 | 12 | 344 | 177 | 167 | 10 |
| 499 | 362 | 29 | 28 | 1307 | 660 | 647 | 13 |

审计含义：

1. 尾关联总质量很大，但危险的有符号尾项在这些最薄行中为正；
2. 偶数阶核心桶略强于奇数阶核心桶，因此尾项没有吞掉正余量；
3. 顶部正桶多为 `omega=2`，顶部负桶多为 `omega=3`，这提示下一步应证明
   `omega=2` 偶核心走廊对 `omega=3` 奇核心走廊有系统补偿；
4. `p=499` 已出现 `max omega=6`，所以五阶下界与精确幸存数差 `1`，真正高重惩罚仍很小。

新的最窄尾项命题因此更新为：

```text
SignedTail-Balance:
odd-core corridor mass cannot exceed even-core corridor mass by the BK threshold.
```

如果该平衡失败，则由 `ETC-SignedBucket` 必有一个奇数阶 dyadic/anchor 桶显著过量；
该桶再进入 Tail-anchor 或 Distributed corridor saturation，并最终回流 `PDEC/SAE`。
