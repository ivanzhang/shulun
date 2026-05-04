# EDA 对角分割的 Alpha-Lift：从 `2/3` 转向更优 `3/4`

**状态：** `diagonal_alpha_lift_route_promising_open`

前文 `DLS-13` 采用 `y=floor(2p/3)`。继续审计发现：`2/3` 不是最优分割。
取更高低骨架阈值，例如

\[
y=\lfloor 3p/4\rfloor,
\tag{ALP-1}
\]

低洞数只小幅下降，而高标签容量显著下降，分割容量余量更大。

## 1. 一般 alpha 分割

对任意 `1/2<alpha<1`，令

\[
y_\alpha=\lfloor \alpha p\rfloor.
\tag{ALP-2}
\]

低洞集合：

\[
H_\alpha(p)=\{1\le k<p:\forall q\le y_\alpha,\ q\nmid p^2+k\}.
\tag{ALP-3}
\]

高标签精确容量：

\[
C_\alpha(p)=
\sum_{y_\alpha<q<p}
\#\{1\le k<p:k\equiv -p^2\pmod q\}.
\tag{ALP-4}
\]

同 `DSC-1`，若

\[
|H_\alpha(p)|>C_\alpha(p),
\tag{ALP-5}
\]

则对角行必有素数。

## 2. 复合低洞壳层的一般形态

若 `k in H_alpha(p)` 且 `p^2+k` 合成，取最小素因子 `q`，则

\[
\alpha p<q<p,
\qquad
p<r={p^2+k\over q}< {p+1\over \alpha}+O(1).
\tag{ALP-6}
\]

当 `alpha>1/2` 且 `p` 足够大时，`r` 必为素数；否则 `r` 有素因子不超过
`sqrt((p+1)/alpha+O(1))<alpha p`，与低洞定义矛盾。

因此 `alpha=3/4` 时，复合低洞被压到更窄壳层：

\[
3p/4<q<p<r<4p/3+O(1).
\tag{ALP-7}
\]

这比 `2p/3<q<p<r<3p/2` 更强。

## 3. 为什么 `3/4` 更优

`alpha` 增大时：

1. `H_alpha(p)` 会减少，但主密度只从 `1/log(2p/3)` 变为 `1/log(3p/4)`，变化很小；
2. 高标签区间 `(alpha p,p)` 明显缩短；
3. 每个高标签仍只命中一列或两列；
4. 第二命中也随高标签区间缩短而减少。

样本审计：

| p | alpha | low holes | high capacity | margin |
|---:|---:|---:|---:|---:|
| 499 | 2/3 | 45 | 32 | 13 |
| 499 | 3/4 | 43 | 23 | 20 |
| 997 | 2/3 | 84 | 55 | 29 |
| 997 | 3/4 | 83 | 40 | 43 |
| 5003 | 2/3 | 307 | 246 | 61 |
| 5003 | 3/4 | 299 | 171 | 128 |
| 10007 | 2/3 | 585 | 455 | 130 |
| 10007 | 3/4 | 568 | 324 | 244 |
| 50021 | 2/3 | 2489 | 1907 | 582 |
| 50021 | 3/4 | 2444 | 1332 | 1112 |

因此，若目标是闭合对角分支，`alpha=3/4` 比 `2/3` 更适合硬攻。

## 4. 新主量间隙

定义

\[
V_\alpha(p)=\prod_{q\le y_\alpha}\left(1-{1\over q}\right),
\qquad
G_\alpha(p)=(p-1)V_\alpha(p)-C_\alpha(p).
\tag{ALP-8}
\]

样本中 `G_{3/4}(p)` 远大于 `G_{2/3}(p)`。因此固定低模自动排除条件

\[
G_\alpha(p)\ge c_\alpha {p\over\log p}
\tag{ALP-9}
\]

在 `alpha=3/4` 下更可能获得显式证明。

## 5. 当前最优替代硬点

原 `DLS-13` 可替换为更强、更有余量的目标：

```text
ALP-3/4:
prove |H_floor(3p/4)(p)| > C_floor(3p/4)(p).
```

这仍然推出对角分支闭合，但需要排斥的高标签容量更小，复合低洞壳层更窄。

## 6. 审稿边界

本文没有证明 `ALP-3/4`。它完成的是路线优化：当前最优不应继续死攻 `2/3` 常数，
而应把对角分支改写为 `alpha=3/4` 或更优 `alpha` 的分割容量不等式，再证明对应
`LowHole/PDEC`。
