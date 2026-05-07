# 对角平方后端点素对维数差合同

**状态：** `reduced_to_explicit_dimension_gap_constants_not_a_proof`

本文把 `x=P` 对角端点的剩余硬点继续压缩。上一层已证明：`P>=23` 时，一尾项唯一等价于三条倒数地板素-素曲线。本文给出最终可审稿接口：

```text
低筛骨架是一维筛主量；
倒数地板素对覆盖是二维筛上界；
只要常数账本分离，平方后端点闭合。
```

## 1. 两个计数

令

\[
y=\max(2,\lfloor P/e\rfloor).
\]

定义低筛骨架

\[
G(P)=\#\{1\le k<P:\ P^-(P^2+k)>y\}.
\tag{DG-1}
\]

定义三曲线素对覆盖数

\[
B(P)=\#\left\{(\ell,m):
\begin{array}{l}
y<\ell<P<m,\\
\ell,m\in\mathbb P,\\
P^2<\ell m<P^2+P
\end{array}
\right\}.
\tag{DG-2}
\]

由唯一分解与 `m>P>ell`，不同素对给出不同列；且每个素对列自动属于低筛骨架。因此 `P>=23` 时

\[
G(P)-B(P)
\tag{DG-3}
\]

正是平方后端点中的无尾储备数。若 `(DG-3)>0`，则存在一个 `P^2+k` 没有 `<P` 素因子；因

\[
P^2<P^2+k<P^2+P<(P+1)^2,
\]

它必为素数。

## 2. 倒数地板三曲线

对任意 `(ell,m)`，写

\[
P^2=\ell a_\ell+r_\ell,\qquad 0\le r_\ell<\ell.
\]

由于 `ell>y`，互补因子区间长度小于 `4`，所以

\[
m=a_\ell+s,\qquad s\in\{1,2,3\}.
\tag{DG-4}
\]

于是

\[
B(P)=
\sum_{s=1}^3
\#\{y<\ell<P:\ \ell\in\mathbb P,\ \lfloor P^2/\ell\rfloor+s\in\mathbb P,\ 1\le \ell s-(P^2\bmod \ell)<P\}.
\tag{DG-5}
\]

这就是当前最窄的素对上界对象。

## 3. 显式常数闭合条件

若存在常数 `c_G,C_B>0` 与阈值 `P0`，使所有素数 `P>=P0` 满足

\[
G(P)\ge c_G {P\over \log P},
\tag{DG-6}
\]

和

\[
B(P)\le C_B {P\over (\log P)^2},
\tag{DG-7}
\]

且

\[
\log P>{C_B\over c_G},
\tag{DG-8}
\]

则 `(DG-3)>0`，平方后端点闭合。

审计到 `P<=100000` 支持一个非常紧凑的候选账本：

```text
c_G = 0.48；
C_B = 1.50；
C_B/c_G = 3.125；
log(23) = 3.135... > 3.125。
```

因此只要 `(DG-6)` 与 `(DG-7)` 以这组常数从 `P>=23` 起成立，端点硬点就完全闭合；小于 `23` 的有限例外已经由直接审计覆盖。

低范围有限证书进一步见：

```text
docs/diagonal_postsquare_lowband_finite_certificate_p2003_20260505.md
docs/diagonal_postsquare_lowband_finite_certificate_p2003_20260505.json
```

该证书直接检查 `P<=2003` 的 `303` 个奇素数：端点素数失败数为 `0`；其中 `P>=23` 的
`296` 条记录全部满足 `G(P)-B(P)>0`，最小 margin 为 `2`。因此解析常数证明可从
`P>=2003` 的尾段开始。

## 4. 审计证据

脚本：

```text
experiments/prime_matrix_diagonal_postsquare_primepair_excess_audit.py
```

输出：

```text
docs/diagonal_postsquare_primepair_excess_audit_p100000_20260505.md
docs/diagonal_postsquare_primepair_excess_audit_p100000_20260505.json
```

读数：

```text
p>=23 odd primes checked=9584；
bad low-column records=0；
duplicate records=0；
min margin=2；
max cover ratio=0.5；
min margin ratio=0.5；
global offset counts={1:2382769,2:1224063,3:163279}。
```

尺度常数读数：

```text
min_{P<=100000} G(P) log(P)/P = 0.4879618800870573 at P=37；
max_{P<=100000} B(P) log(P)^2/P = 1.4688379348569027 at P=461。
```

阈值后的最坏覆盖比例持续下降：

```text
P>=101:   0.400000；
P>=501:   0.311475；
P>=5003:  0.239401；
P>=10007: 0.208807；
P>=50021: 0.176814。
```

## 5. 剩余硬点

本文没有证明 `(DG-6)` 或 `(DG-7)`。它把端点硬点拆成两个可验收目标：

```text
LDG-Lower:
证明低筛骨架 G(P) >= 0.48 P/log P；
若失败，则失败是低模骨架持续亏损，路由到 PDEC。

RFP-Upper:
证明三条倒数地板素对曲线 B(P) <= 1.50 P/log^2 P；
若失败，则失败是短窗素数/尾锚异常集中，路由到 Tail-anchor/PDEC。
```

这比原始的短区间素数命题更窄：现在只需证明一维粗骨架下界与二维素对上界之间存在显式维数差，或者证明任何维数差失败都会触发已有的命名缺陷接口。

`RFP-Upper` 的进一步拆分见：

```text
docs/monograph/prime-matrix-diagonal-postsquare-rfp-selberg-route.md
```

该文把 `B(P)` 改写为双曲窄带 `R_P` 中两个坐标同为素数的二维上筛问题，并把剩余常数债务拆成
`RFP-Area`、`RFP-Selberg` 与 `RFP-Defect`。

`LDG-Lower` 的进一步拆分见：

```text
docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md
```

该文把低筛骨架下界改写为固定端点相位 `-P^2 mod r` 的低模 CRT 骨架亏损问题：若
`G(P)<0.48P/logP`，则必须出现 `LowSkeletonDeficit/PDEC` 或有限 `SAE`。
