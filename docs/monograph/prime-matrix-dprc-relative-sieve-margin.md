# DPRC 相对筛余量接口

**状态：** `reduction_plus_large_finite_audit_not_a_proof`

本文接续动态提升轮粗骨架容量证书，把

\[
T_Y^\pm(P)<|S_Y^\pm(P)|
\]

拆成一个更适合解析证明的相对筛偏差问题。

## 1. 余量恒等式

固定 `alpha=0.43`，令

\[
Y=P^\alpha,\qquad S=|S_Y^\pm(P)|,\qquad T=T_Y^\pm(P).
\]

再令

\[
H=\sum_{Y<q<P}{1\over q}.
\]

则有恒等式

\[
S-T=S(1-H)-(T-HS).
\tag{RSM-1}
\]

记正偏差

\[
D_+=\max(0,T-HS).
\]

因此若

\[
D_+<S(1-H),
\tag{RSM-2}
\]

就得到 `T<S`。

## 2. C-sqrt 充分条件

一个更标准的充分条件是存在常数 `C` 使

\[
D_+\le C\sqrt S,
\tag{RSM-3}
\]

同时

\[
S(1-H)>C\sqrt S.
\tag{RSM-4}
\]

这样 `(RSM-2)` 自动成立。

本次审计显示 `C=3` 是当前最干净的接口：

```text
P>=2003:
  min S(1-H)/sqrt(S) = 3.579479；
  max D_+/sqrt(S)   = 2.468627；
  capacity_fail     = 0。

P>=10007:
  min S(1-H)/sqrt(S) = 6.613726；
  max D_+/sqrt(S)   = 2.468627；
  min capacity margin = 213。
```

所以 `P>=2003` 可由 `C=3` 型相对筛偏差界闭合；`P<2003` 可保留为有限证书。

## 3. 审计

脚本：

```text
experiments/prime_matrix_dprc_relative_sieve_margin.py
```

报告：

```text
docs/dprc_relative_sieve_margin_alpha043_p100000_20260506.md
```

汇总：

| P threshold | records | cap fail | min margin | max T/S | min model/sqrt | max D+/sqrt | C=3 pass |
|---:|---:|---:|---:|---:|---:|---:|---|
| 13 | 19174 | 0 | 1 | 0.947368 | 0.867530 | 2.468627 | False |
| 2003 | 18578 | 0 | 48 | 0.883929 | 3.579479 | 2.468627 | True |
| 10007 | 16726 | 0 | 213 | 0.871142 | 6.613726 | 2.468627 | True |

最大正偏差样本：

| P | side | S | T | margin | H | D+/sqrt |
|---:|---|---:|---:|---:|---:|---:|
| 30137 | minus | 3708 | 3169 | 539 | 0.814098 | 2.468627 |
| 21149 | plus | 2703 | 2337 | 366 | 0.817612 | 2.442672 |
| 19997 | minus | 2592 | 2258 | 334 | 0.826102 | 2.293071 |
| 95581 | minus | 10721 | 9112 | 1609 | 0.828793 | 2.187611 |

## 4. 解析证明义务

`DPRC(alpha=0.43)` 现在可拆成三段：

```text
Finite:
  13<=P<2003 直接有限证书。

ModelGap:
  P>=2003 证明 S(1-H)>3 sqrt(S)。

RelativeDiscrepancy:
  P>=2003 证明 D_+<=3 sqrt(S)。
```

`ModelGap` 只需要显式 Mertens/prime harmonic 上界与低筛骨架下界。

`RelativeDiscrepancy` 是真正剩余硬点。它等价于证明在动态粗骨架上，剩余高素同余类命中总量相对其平均 `H S` 的正偏差只有平方根级：

\[
\sum_{Y<q<P}\left(
\#\{k\in S_Y^\pm(P):q\mid P^2\pm k\}
-{|S_Y^\pm(P)|\over q}
\right)
\le 3\sqrt{|S_Y^\pm(P)|}.
\tag{RSM-5}
\]

这应走同权相对筛、分散大筛或低模 Fourier/CRT 缺陷二分：

```text
RelativeDiscrepancy <= 3 sqrt(S)
or persistent endpoint CRT defect / sparse exceptional window.
```

## 5. 与 PDEC 的连接

若 `(RSM-5)` 失败，则许多剩余高素同余类在同一个动态粗骨架相位上正向偏斜。这不是随机误差，而是可抽取的低模/高模相干：

- 若偏差在许多 `q` 上分散，进入大筛型相位能量；
- 若偏差集中在少数 `q` 或短区间，进入 `SAE`；
- 若偏差由同一低模平移反复支撑，进入 `PDEC/ColumnCRT`。

因此当前最小硬点不再是原始行命题，而是：

```text
DPRC-RSM:
  对 alpha=0.43，证明 P>=2003 的 RelativeDiscrepancy <= 3sqrt(S)，
  或将失败路由到 PDEC/SAE/ColumnCRT；
  P<2003 用有限证书闭合。
```

这一步把动态小模连乘刚性从经验容量余量，压成了一个审稿员可以逐项检查的相对筛偏差接口。
