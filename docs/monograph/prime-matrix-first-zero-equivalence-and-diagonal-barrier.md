# CRT 首个零行：证书等价命题与对角屏障

**状态：** `first_zero_reduced_to_certificate_minimum_and_prime-gap_barrier`

本文研究固定奇素数 `p` 的首个 CRT 零行出现规律。结论分三层：

1. 首个零行不是由简单密度单调律控制，而是一个 CRT 覆盖证书集合的最小正代表元问题；
2. “首个零行必在对角区段之后”等价于每个早期 `p` 对齐短区间 `(px,p(x+1))` 含素数；
3. 因此该目标触及平方根尺度短区间素数问题，完全自足证明必须利用特殊 CRT 对角结构，而不能
   只靠完整周期覆盖能力或连续光滑数下界。

## 1. 首个零行定义

令

\[
M_p=\prod_{q<p,\ q\ {\rm prime}}q.
\tag{FZ-1}
\]

定义乘数形式的零行集合

\[
Z_p=\left\{x\ge1:\ \forall 1\le k<p,\ \exists q<p,\ q\mid px+k\right\}.
\tag{FZ-2}
\]

首个零行乘数为

\[
X_0(p)=\min Z_p,
\tag{FZ-3}
\]

若 `Z_p` 为空则记为 `\infty`。旧一编号行号为

\[
R_0(p)=X_0(p)+1.
\tag{FZ-4}
\]

因为条件只依赖 `x mod M_p`，`Z_p` 是 `M_p` 周期集合。

## 2. 覆盖证书等价命题

对每个列 `k` 选择一个负责覆盖它的小素数：

\[
\tau(k)\in Q_p:=\{q:\ q<p,\ q\ {\rm prime}\}.
\tag{FZ-5}
\]

该选择称为一个覆盖证书，如果：

1. 每列被分配一个素数 `\tau(k)`；
2. 同一素数只能覆盖同余列，即
   \[
   \tau(a)=\tau(b)=q\quad\Longrightarrow\quad a\equiv b\pmod q.
   \tag{FZ-6}
   \]

对证书 `\tau`，令

\[
D_\tau=\prod_{q\in {\rm im}(\tau)}q.
\tag{FZ-7}
\]

若 `\tau(k)=q`，则 `q|px+k` 等价于

\[
x\equiv -k p^{-1}\pmod q.
\tag{FZ-8}
\]

由 `(FZ-6)`，这些同一 `q` 的条件相容；不同素数由 CRT 相容。因此每个证书给出唯一残基

\[
x\equiv r_\tau\pmod {D_\tau}.
\tag{FZ-9}
\]

于是有精确等价：

\[
Z_p=
\bigcup_{\tau\in\mathcal C_p}
\{x\ge1:\ x\equiv r_\tau\pmod {D_\tau}\},
\tag{FZ-10}
\]

其中 `\mathcal C_p` 是所有满足 `(FZ-6)` 的覆盖证书集合。特别地，

\[
X_0(p)
=
\min_{\tau\in\mathcal C_p} r_\tau^+,
\tag{FZ-11}
\]

其中 `r_\tau^+` 是 `(FZ-9)` 的最小正代表元。

这就是首个零行出现的本质：不是“有没有覆盖能力”，而是所有覆盖证书的 CRT 最小正代表元中
最小的一个何时出现。

## 3. 对角区段之后的等价命题

“首个零行必在对角区段之后”可写为

\[
X_0(p)>p.
\tag{FZ-12}
\]

由 `(FZ-10)`，它等价于：

\[
\forall \tau\in\mathcal C_p,\qquad r_\tau^+>p.
\tag{FZ-13}
\]

也等价于早期对角段避让：

\[
\forall 1\le x\le p,\quad
\exists 1\le k<p:\quad (px+k,M_p)=1.
\tag{FZ-14}
\]

上一文件 `prime-matrix-early-diagonal-avoidance-hardpoint.md` 已证明，在 `1<=x<=p` 时，`(px+k,M_p)=1`
等价于 `px+k` 是大于 `p` 的素数。因此 `(FZ-14)` 又等价于

\[
\forall 1\le x\le p,\qquad
\pi(px+p-1)-\pi(px)>0.
\tag{FZ-15}
\]

换言之：

```text
X0(p)>p
<=> every p-aligned interval (px,p(x+1)), 1<=x<=p, contains a prime.
```

这是首零行问题的最硬本质形态。

## 4. 样本规律：非单调、证书驱动

脚本

```text
experiments/prime_matrix_first_zero_pattern_audit.py
```

对 `x<=200000` 的扫描给出：

| p | first zero x | row r=x+1 | x/p |
|---:|---:|---:|---:|
| 13 | 168 | 169 | 12.92 |
| 17 | 1210 | 1211 | 71.18 |
| 19 | 3658 | 3659 | 192.53 |
| 23 | 58 | 59 | 2.52 |
| 29 | 5209 | 5210 | 179.62 |
| 31 | 60794 | 60795 | 1961.10 |
| 37 | 73916 | 73917 | 1997.73 |
| 41 | 170880 | 170881 | 4167.80 |
| 43 | 162932 | 162933 | 3789.12 |
| 47 | not found up to 200000 | not found | not found |

这组数据说明：

1. `X_0(p)/p` 不单调；
2. `p=23` 的首零行异常早，但仍在对角段之后；
3. 首零行受具体 CRT 覆盖证书的最小代表元控制，不受单一倒数和阈值控制；
4. 完整周期中零行很多，并不意味着早期对角段会命中零行。

## 5. 互质结构刚性

若同一素数 `q` 覆盖两列 `a<b`，则

\[
q\mid b-a.
\tag{FZ-16}
\]

所以高素数标签不能自由重复：

```text
q>p/2  =>  q 至多覆盖 1 列；
q>p/3  =>  q 至多覆盖 2 列；
q>p/m  =>  q 至多覆盖 m-1 列。
```

因此一个完整覆盖证书必须由：

1. 低素数给出粗骨架；
2. 中高素数以几乎单列标签补洞；
3. 所有标签共同满足一个 CRT 最小代表约束。

这解释了 `p=23` 的结构：低骨架可较早留下少数洞，高素数 `13,17,19` 的标签置换偶然在
`x=58` 补齐。但这种补齐仍需要最小代表超过 `p`。

## 6. 为什么这不是连续光滑数问题

零行只要求每个 `px+k` 有一个小素因子；它不要求 `px+k` 的所有素因子都小于 `p`。因此首零行
出现不能用 Størmer--Lehmer 或 Pell 型连续 `p`-光滑数下界解释。

真正的早期屏障来自 `(FZ-15)`：早期未覆盖列必为素数，而不是粗合数。

## 7. 与经典短区间素数问题的关系

`x=p` 的一行已经要求

\[
\pi(p^2+p-1)-\pi(p^2)>0.
\tag{FZ-17}
\]

这是 Oppermann 第一半区间

\[
(p^2,p(p+1))
\tag{FZ-18}
\]

在素数 `p` 子序列上的版本。完整 `(FZ-15)` 更强，因为它还要求所有

\[
(px,p(x+1)),\qquad 1\le x<p,
\tag{FZ-19}
\]

都含素数。

因此，若要无条件证明 `X_0(p)>p` 对所有奇素数成立，就必须证明一个平方根尺度的
`p` 对齐短区间素数定理，或利用 CRT 对角结构给出比普通短区间素数定理更强的专用证明。

## 8. 可推进的证明路径

当前最精确、非循环的目标是：

```text
Certificate-MinRep Barrier:
for every compatible full-cover certificate tau, its least CRT representative r_tau^+ exceeds p.
```

等价地：

```text
EDA-Dual:
for every 1<=x<=p, the exact inclusion-exclusion count U_p(x)>0.
```

建议下一步按以下顺序硬攻：

1. **证书分层。** 先固定低素数骨架，列出剩余洞集 `H_L(x)`；证明若 `|H_L(x)|` 太小，则低模端点
   缺陷进入 `PDEC/SAE`。
2. **高标签容量。** 用 `(FZ-16)` 证明高素数标签几乎只能单列补洞；若全补齐，则产生大量互不相容
   的 CRT 最小代表约束。
3. **最小代表下界。** 对每个分层证书证明 `r_\tau^+>p`，而不是只证明证书数量少。
4. **EDA-Dual 下界。** 从 Möbius 公式
   \[
   U_p(x)=\sum_{d\mid M_p}\mu(d)N_d(x)
   \tag{FZ-20}
   \]
   构造可变阶 Bonferroni/Selberg 对偶证书，证明 `U_p(x)>0`；失败时导出
   `Directed Endpoint CRTDefect` 或 `SAE`。

本步没有宣称闭合行命题；它把“首零行必在对角之后”的数学实质压缩为两个完全等价、可审稿的
硬接口：`Certificate-MinRep Barrier` 与 `EDA-Dual`。
