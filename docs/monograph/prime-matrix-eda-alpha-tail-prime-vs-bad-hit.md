# AlphaTail 精确分解：对角素数数 vs 坏高标签命中

**状态：** `alpha_tail_prime_vs_bad_hit_exact_reduction_open`

本文继续专攻 `AlphaTail(alpha=0.9)`。设

\[
\alpha=0.9,\qquad y=\lfloor \alpha p\rfloor.
\tag{ATB-1}
\]

核心结论：

```text
H_alpha(p)>C_alpha(p)
等价于
对角短区间素数数 > 坏高标签命中数。
```

这说明 AlphaTail 的真正尾项硬核不是半素数壳层本身；好半素数壳层会与高标签容量相互抵消。

## 1. 高标签唯一性

对 `alpha>1/sqrt(2)` 且充分大 `p`，任意

\[
n=p^2+k,\qquad 1\le k<p,
\tag{ATB-2}
\]

至多有一个素因子 `q` 满足

\[
\alpha p<q<p.
\tag{ATB-3}
\]

**证明。**  
若存在两个不同素因子 `q_1,q_2` 均在 `(alpha p,p)`，则 `q_1q_2<p^2<n`，所以
`n/(q_1q_2)` 是至少 `2` 的整数。于是

\[
n\ge2\alpha^2p^2.
\tag{ATB-4}
\]

当 `alpha>1/sqrt2` 且 `p` 足够大时，右侧大于 `p^2+p>n`，矛盾。证毕。

因此在 `alpha=0.9` 下，高标签容量 `C_alpha(p)` 实际是在数具体的整数命中，而非带大重数的
多重覆盖。

## 2. 三类分解

把 `[1,p-1]` 中的列分成：

1. `Prime`: `p^2+k` 是素数；
2. `GoodHigh`: `p^2+k=q r`，其中 `alpha p<q<p<r` 且 `r` 为素数，因此该列是低洞；
3. `BadHigh`: 存在 `alpha p<q<p` 使 `q|p^2+k`，但 `p^2+k` 不是低洞，即还有某个
   `<=alpha p` 的小素因子。

记三类数量为

\[
P_\alpha(p),\quad G_\alpha(p),\quad B_\alpha^{bad}(p).
\tag{ATB-5}
\]

由高标签唯一性：

\[
H_\alpha(p)=P_\alpha(p)+G_\alpha(p),
\tag{ATB-6}
\]

而

\[
C_\alpha(p)=G_\alpha(p)+B_\alpha^{bad}(p).
\tag{ATB-7}
\]

于是得到精确恒等式：

\[
H_\alpha(p)-C_\alpha(p)
=
P_\alpha(p)-B_\alpha^{bad}(p).
\tag{ATB-8}
\]

## 3. AlphaTail 等价硬核

由 `(ATB-8)`：

\[
H_\alpha(p)>C_\alpha(p)
\quad\Longleftrightarrow\quad
P_\alpha(p)>B_\alpha^{bad}(p).
\tag{ATB-9}
\]

这就是 AlphaTail 的真实硬核。好半素数壳层 `G_alpha` 同时出现在低洞数和高标签容量中，
完全抵消。

## 4. 坏高标签命中的结构

若 `q` 是高标签，写

\[
p^2+k=q m.
\tag{ATB-10}
\]

由于 `q>alpha p`，

\[
p<m<{p+1\over\alpha}+O(1).
\tag{ATB-11}
\]

当 `alpha=0.9` 时，

\[
p<m<1.112p+O(1).
\tag{ATB-12}
\]

`BadHigh` 正是这些短区间内的复合 `m` 产生的命中；若 `m` 为素数，则该列属于
`GoodHigh`，会被 `(ATB-8)` 抵消。

因此坏命中是一个双变量稀疏问题：

```text
q prime in (0.9p,p),
m composite in (p,1.112p),
qm in (p^2,p^2+p).
```

## 5. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_bad_audit.py
```

样本验证 `(ATB-8)`：

| p | alpha | prime count | good high | bad high | H-C = P-Bad |
|---:|---:|---:|---:|---:|---:|
| 499 | 0.9 | 40 | 1 | 6 | 34 |
| 997 | 0.9 | 78 | 2 | 13 | 65 |
| 5003 | 0.9 | 282 | 7 | 56 | 226 |
| 10007 | 0.9 | 530 | 12 | 104 | 426 |
| 50021 | 0.9 | 2329 | 44 | 436 | 1893 |

坏高标签命中远小于对角素数数。

## 6. 审稿边界

本文把 AlphaTail 精确化，但也暴露了硬核：

```text
需要证明 P_alpha(p)>B_bad_alpha(p)。
```

`B_bad` 可望由上筛给出 `O(p/log^2 p)` 级别；但 `P_alpha(p)` 是
`(p^2,p^2+p)` 中的素数数。若不用外部平方根长度短区间素数输入，就必须通过 PDEC/SAE
证明 `B_bad` 不可能覆盖全部素数缺口。

因此下一步最优是：

1. 对 `B_bad` 建立 Selberg/Brun 上界；
2. 明确剩余需要的对角素数下界或 PDEC 替代机制；
3. 避免把好半素数壳层当作净余量，因为它在 `(ATB-8)` 中抵消。
