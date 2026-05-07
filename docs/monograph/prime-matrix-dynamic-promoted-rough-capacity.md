# 动态提升轮粗骨架容量证书

**状态：** `reduction_plus_large_finite_audit_not_a_proof`

本文把提升轮策略从固定小模 `6/30/210/...` 推到动态轮：

\[
Y=P^\alpha,\qquad e^{-1}<\alpha<1/2.
\]

把全部 `q<=Y` 的素因子斜线提升进轮底座。由轮提升不变性，最终幸存偏移集合不变；但剩余覆盖层只含 `Y<q<P` 的高素斜线。若这些剩余斜线的总命中数已经小于动态粗骨架本身，则全覆盖不可能。

## 1. 动态粗骨架

固定平方后行或平方前行：

```text
plus:  P^2+k,  1<=k<P；
minus: P^2-k,  1<=k<P。
```

令

\[
\mathcal P(Y)=\prod_{\ell\le Y}\ell.
\]

定义动态粗骨架

\[
S_Y^\pm(P)=
\{1\le k<P:(P^2\pm k,\mathcal P(Y))=1\}.
\tag{DPRC-1}
\]

剩余高素命中总量为

\[
T_Y^\pm(P)=
\sum_{Y<q<P}
\#\{k\in S_Y^\pm(P):q\mid P^2\pm k\}.
\tag{DPRC-2}
\]

若整行被剩余高素斜线覆盖，则必有

\[
|S_Y^\pm(P)|\le
\left|\bigcup_{Y<q<P}\{k\in S_Y^\pm(P):q\mid P^2\pm k\}\right|
\le T_Y^\pm(P).
\tag{DPRC-3}
\]

因此：

\[
T_Y^\pm(P)<|S_Y^\pm(P)|
\tag{DPRC-4}
\]

直接排除全覆盖。这是比强制重叠证书更强的一阶容量出口。

## 2. 与互补因子窗口的等价式

对固定 `q`，写

\[
P^2\pm k=q m.
\]

因为 `q>Y` 且 `q` 不在底座中，命中动态粗骨架当且仅当

\[
(m,\mathcal P(Y))=1.
\]

所以

\[
T_Y^\pm(P)=
\sum_{Y<q<P}
\#\{m\in I_q^\pm(P):(m,\mathcal P(Y))=1\},
\tag{DPRC-5}
\]

其中 `I_q^\pm(P)` 是平方前/后行的互补因子短窗口。

这把问题压成同一低筛权重下的相对不等式：

\[
\sum_{Y<q<P}
\#\{m\in I_q^\pm(P):(m,\mathcal P(Y))=1\}
<
\#\{1\le k<P:(P^2\pm k,\mathcal P(Y))=1\}.
\tag{DPRC-6}
\]

## 3. 为什么选择 alpha=0.43

启发式上，

\[
|S_Y^\pm(P)|\sim P V(Y),
\qquad
V(Y)=\prod_{\ell\le Y}\left(1-{1\over \ell}\right),
\]

而

\[
T_Y^\pm(P)\sim
P V(Y)\sum_{Y<q<P}{1\over q}.
\]

由 Mertens 型估计，

\[
\sum_{P^\alpha<q<P}{1\over q}
\sim
\log{\log P\over \log P^\alpha}
=\log {1\over \alpha}.
\tag{DPRC-7}
\]

若 `alpha>e^{-1}`，则 `log(1/alpha)<1`。同时取 `alpha<1/2`，筛层仍低于平方根水平，保留线性筛/同权筛的可攻空间。

本次固定

```text
alpha = 0.43
log(1/alpha) = 0.843970...
```

它位于

```text
e^{-1} < 0.43 < 1/2
```

的安全区间内。

## 4. 审计

脚本：

```text
experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py
```

报告：

```text
docs/dynamic_promoted_rough_capacity_audit_20260506.md
docs/dynamic_promoted_rough_capacity_audit_lowmid_20260506.md
docs/dynamic_promoted_rough_capacity_audit_alpha040_p20000_20260506.md
docs/dynamic_promoted_rough_capacity_audit_alpha043_p20000_20260506.md
docs/dynamic_promoted_rough_capacity_audit_alpha043_p50000_20260506.md
docs/dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.md
```

`alpha=0.43` 连续扫描：

```text
13<=P<=100000；
素数 P 个数 = 9587；
plus/minus 记录数 = 19174；
capacity_fail = 0；
forced_fail = 0；
min capacity margin = 1；
max T_Y/S_Y = 0.9473684210526315。
```

高段 `P>=10007`：

```text
records = 16726；
min capacity margin = 213；
max T_Y/S_Y = 0.871141975308642。
```

最紧点都在低素数：

| P | side | S_Y | T_Y | margin | T/S | cutoff |
|---:|---|---:|---:|---:|---:|---:|
| 17 | plus | 5 | 4 | 1 | 0.800000 | 3 |
| 23 | plus | 7 | 6 | 1 | 0.857143 | 3 |
| 31 | minus | 10 | 9 | 1 | 0.900000 | 4 |
| 13 | plus | 4 | 2 | 2 | 0.500000 | 3 |
| 17 | minus | 5 | 3 | 2 | 0.600000 | 3 |

样本点：

| P | side | S_Y | T_Y | T/S | margin |
|---:|---|---:|---:|---:|---:|
| 10007 | minus | 1386 | 1093 | 0.788600 | 293 |
| 10007 | plus | 1385 | 1169 | 0.844043 | 216 |
| 36739 | minus | 4471 | 3686 | 0.824424 | 785 |
| 36739 | plus | 4465 | 3731 | 0.835610 | 734 |
| 99991 | minus | 11128 | 9280 | 0.833932 | 1848 |
| 99991 | plus | 11131 | 9127 | 0.819962 | 2004 |

## 5. 与强制重叠证书的关系

固定提升轮强制重叠证书证明：

\[
T-\left\lceil {2I_2\over M}\right\rceil<|S|.
\]

动态粗骨架容量证书更强：

\[
T_Y<|S_Y|.
\]

因此当前路线应分层：

```text
主出口：Dynamic-Promoted Rough Capacity，证明 T_Y<S_Y；
备出口：若一阶容量接近等号，用 Forced-Overlap 的 I2/M 扣除；
失败出口：若 T_Y>=S_Y 或筛估计超预算，抽取 PDEC/SAE/ColumnCRT。
```

`alpha=0.40` 在 `P<=20000` 只有两个等号点：

```text
P=113 minus: S=T=30；
P=293 plus:  S=T=67。
```

但强制重叠仍闭合。`alpha=0.43` 在 `P<=100000` 已无等号点。

## 6. 当前最小硬点

当前最小硬点可写成：

```text
DPRC(alpha=0.43):
  对所有奇素数 P 与 side in {plus,minus}，
  证明 T_Y^\pm(P)<|S_Y^\pm(P)|，
  其中 Y=P^0.43。
```

解析证明义务是同权相对筛不等式：

```text
低筛骨架下界:
  |S_Y^\pm(P)| >= P V(Y) - acceptable_error；

高素互补窗口总上界:
  T_Y^\pm(P) <= P V(Y)(log(1/alpha)+acceptable_error)；

余量:
  log(1/0.43)=0.843970...，高段实测最大 T/S≈0.871142。
```

注意这里不能把每个短窗口单独用粗莫比乌斯误差处理；短窗口太短，单窗误差会吞掉余量。必须使用聚合的同权筛、Selberg/Rosser-Iwaniec 平均，或把超预算相位送入 `PDEC/SAE/ColumnCRT`。

这一步把用户提出的“小模连乘同余刚性”推进到全局动态层：不再固定 `210` 或 `2310`，而是选择 `P^0.43` 以下的全部小素数作为刚性底座，使剩余高素斜线在总容量上已经不足以覆盖粗骨架。

## 7. 相对筛余量分解

后续细化见：

```text
docs/monograph/prime-matrix-dprc-relative-sieve-margin.md
docs/dprc_relative_sieve_margin_alpha043_p100000_20260506.md
```

令

\[
H=\sum_{P^{0.43}<q<P}{1\over q}.
\]

则

\[
S_Y^\pm(P)-T_Y^\pm(P)
=
S_Y^\pm(P)(1-H)
-
\left(T_Y^\pm(P)-H S_Y^\pm(P)\right).
\]

审计显示 `P>=2003` 时，

```text
min S(1-H)/sqrt(S) = 3.579479；
max positive discrepancy/sqrt(S) = 2.468627。
```

因此 `DPRC` 可由以下接口闭合：

```text
P<2003:
  finite certificate；

P>=2003:
  S(1-H)>3sqrt(S)；
  max(0,T-HS)<=3sqrt(S)。
```

后一项是当前最窄解析硬点：动态粗骨架上的剩余高素同余类正偏差只有平方根级；失败则进入 `PDEC/SAE/ColumnCRT`。
