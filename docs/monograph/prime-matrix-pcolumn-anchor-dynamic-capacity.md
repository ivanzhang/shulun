# 第P列锚点动态提升轮容量证书

**状态：** `reduction_plus_audit_not_a_proof`

本文把 `PColumn Anchor-Wheel Field` 从固定轮 `30/210/2310/...` 提升到动态轮

\[
Y=P^\alpha,\qquad \alpha=0.43.
\]

核心目标是把用户提出的“第 `P` 列也层叠轮筛，与第一行斜线覆盖形成全行全列夹击场”写成一个可审稿的不等式接口。

## 1. 动态锚点骨架

固定奇素数 `P`，令

\[
y=x+1,\qquad d=P-c,\qquad 1\le d<P.
\]

第 `x` 行的非平凡列为

\[
n_{x,c}=xP+c=Py-d.
\tag{PCD-1}
\]

令

\[
\mathcal P_Y=\prod_{\ell\le Y}\ell.
\]

第 `P` 列锚点 `Py` 诱导的动态低素骨架为

\[
S_Y(P,y)=\{1\le d<P:(Py-d,\mathcal P_Y)=1\}.
\tag{PCD-2}
\]

剩余高素斜线为

\[
\mathcal Q_Y(P)=\{q:\ q\ {\rm prime},\ Y<q<P\}.
\]

每条高素斜线在距离坐标中的命中集是

\[
C_q(P,y)=\{d\in S_Y(P,y):d\equiv Py\pmod q\}.
\tag{PCD-3}
\]

定义总命中

\[
T_Y(P,y)=\sum_{q\in\mathcal Q_Y(P)} |C_q(P,y)|.
\tag{PCD-4}
\]

## 2. 严格素数洞蕴含

若

\[
T_Y(P,y)<|S_Y(P,y)|,
\tag{PCD-5}
\]

则

\[
\left|\bigcup_{q\in\mathcal Q_Y(P)}C_q(P,y)\right|
\le T_Y(P,y)<|S_Y(P,y)|.
\]

所以存在 `d in S_Y(P,y)` 不被任何 `Y<q<P` 命中。该 `d` 同时避开所有 `q<=Y`，因此 `n=Py-d` 没有任何 `<P` 的素因子；且 `1<=d<P`，所以 `P\nmid n`。

对 `2<=y<=P+1`，

\[
P<n=Py-d<P^2+P.
\]

若 `n` 合成，则其最小素因子不超过 `sqrt(n)<P+1`，只能是 `<P` 的素数或 `P`。二者已排除。因此 `n` 必为素数。

这给出严格推论：

```text
PColumn Dynamic Capacity:
  对某一行 y，若 T_Y(P,y)<|S_Y(P,y)|，
  则该行存在素数洞，不能成为零行。
```

## 3. 与第一行圆柱平移的连接

把动态轮看成巨大模数 `\mathcal P_Y`。固定轮恒等式仍成立：

\[
S_Y(P,y)\equiv S_Y(P,2)+P(y-2)\pmod{\mathcal P_Y}.
\tag{PCD-6}
\]

因此第 `P` 列并不直接提供素数，它提供的是全体低素模下的锚相位向量

\[
(Py\bmod \ell)_{\ell\le Y}.
\]

第一行给出原始骨架，第 `P` 列给出平移参数；所有行都是同一个圆柱骨架在动态轮上的平移切片。这正是“方阵斜线覆盖”和“圆柱环绕覆盖”的共同方程。

## 4. 相对筛余量接口

令

\[
S=|S_Y(P,y)|,\qquad T=T_Y(P,y),\qquad
H=\sum_{Y<q<P}{1\over q}.
\]

有恒等式

\[
S-T=S(1-H)-(T-HS).
\tag{PCD-7}
\]

记

\[
D_+(P,y)=\max(0,T-HS).
\]

若

\[
D_+(P,y)<S(1-H),
\tag{PCD-8}
\]

则 `T<S`，行 `y-1` 不能成为零行。

这与平方端点 DPRC 是同一解析骨架，但第 `P` 列版本更强：它要求对所有 `2<=y<=P+1` 同时成立，而不只处理 `P^2-k` 与 `P^2+k` 两个端点切片。

## 5. 审计结果与新结构

脚本：

```text
experiments/prime_matrix_pcolumn_anchor_dynamic_capacity_audit.py
```

报告：

```text
docs/pcolumn_anchor_dynamic_capacity_audit_20260506.md
docs/pcolumn_anchor_dynamic_capacity_audit_p10007_20260506.md
docs/pcolumn_anchor_dynamic_capacity_audit_p20011_20260506.md
```

汇总：

| P | cutoff | H | min margin | max T/S | min model/sqrt | max D+/sqrt | C-window | min prime holes | cap fails |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 101 | 7 | 0.626627 | 1 | 0.954545 | 1.711011 | 1.538075 | 0.172936 | 7 | 0 |
| 499 | 14 | 0.750683 | 3 | 0.968085 | 2.391366 | 2.107793 | 0.283573 | 29 | 0 |
| 997 | 19 | 0.741599 | 20 | 0.883041 | 3.329259 | 1.849589 | 1.479671 | 54 | 0 |
| 2003 | 26 | 0.793492 | 20 | 0.939024 | 3.694119 | 2.635695 | 1.058424 | 113 | 0 |
| 5003 | 38 | 0.812465 | 46 | 0.937922 | 5.066922 | 3.415103 | 1.651820 | 260 | 0 |
| 10007 | 52 | 0.821413 | 98 | 0.929446 | 6.602875 | 4.026284 | 2.576591 | 498 | 0 |
| 20011 | 70 | 0.826152 | 112 | 0.956857 | 8.802969 | 6.659539 | 2.143430 | 929 | 0 |

这里

```text
model/sqrt = S(1-H)/sqrt(S)
D+/sqrt    = max(0,T-HS)/sqrt(S)
C-window   = min model/sqrt - max D+/sqrt
```

所有样本均有 `cap fails=0` 与 `union fails=0`。

### 近截止锚峰

新发现是：第 `P` 列全行版本的最紧容量行经常不在底部，而在 `y` 接近动态 cutoff 后第一批高素的位置。

| P | cutoff | worst y | S | T | margin | T/S | D+/sqrt | prime holes |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 499 | 14 | 15 | 94 | 91 | 3 | 0.968085 | 2.107793 | 49 |
| 5003 | 38 | 41 | 741 | 695 | 46 | 0.937922 | 3.415103 | 397 |
| 10007 | 52 | 46 | 1389 | 1291 | 98 | 0.929446 | 4.026284 | 747 |
| 20011 | 70 | 71 | 2596 | 2484 | 112 | 0.956857 | 6.659539 | 1366 |

机制是：刚超过 `Y` 的第一批高素 `q` 仍有较长步长命中，且当 `Py mod q` 较小或 `q|y` 时，距离类落在短区间前端，形成高命中峰。`P=20011,y=71` 中 top labels 正是 `q=71,73,79`。

但这些峰同时带来大量重叠。`P=20011,y=71` 虽有 `T=2484`，实际未覆盖素数洞仍有 `1366` 个。这说明近截止锚峰不能直接形成零行；若要强行覆盖，必须让同一批近截止高素斜线极高效、低重叠地协调，这正是 `ColumnCRT/PDEC/SAE` 应捕获的异常结构。

### 最薄素数洞与容量峰分离

另一个结构信号是：最少素数洞行通常靠近底部，但这些行并不是 `T/S` 最大行。

`P=20011` 的最少素数洞行在 `y=19289`，仍有 `929` 个素数洞，且 `T/S=0.860331`，远低于最紧容量行的 `0.956857`。这给出一个可攻分裂：

```text
近截止行：容量最紧，但重叠极强；
底部行：素数洞较少，但容量余量明显更大。
```

要产生零行，必须同时打破这两个分裂，即既达到近截止行的容量饱和，又达到底部行的低洞密度。这会把反例压入更窄的异常相位族。

## 6. 近截止-远尾分裂

新增：

```text
docs/monograph/prime-matrix-pcolumn-nearcutoff-fartail-cofactor.md
experiments/prime_matrix_pcolumn_nearcutoff_spike_audit.py
experiments/prime_matrix_pcolumn_far_tail_cofactor_audit.py
```

专项审计显示：最强 `T/S` 行的 top labels 确实是 cutoff 后第一批高素，但相对正偏差 `D+` 的主来源是远尾 `q>10Y`。例如：

| P | best y | q>10Y hit share | q>10Y D+/sqrt |
|---:|---:|---:|---:|
| 20011 | 71 | 0.564412 | 6.727107 |
| 50021 | 104 | 0.602222 | 8.771821 |
| 100003 | 147 | 0.624867 | 12.725422 |

并且对远尾可做精确互补因子反演。写

\[
Py-d=qm,\qquad q>10Y.
\]

则命中等价于

\[
\left\lceil {Py-P+1\over m}\right\rceil
\le q\le
\left\lfloor {Py-1\over m}\right\rfloor,
\]

其中 `q` 为素数，`q<P`，且 `m` 避开所有 `ell<=Y`。审计样本中按 `q` 直接计数与按 `m` 反演计数全部 `identity_delta=0`。

这把当前硬点从“高素斜线总偏差”压成：

```text
FarTail-Cofactor Bound:
  q>10Y 的正偏差等价于 Y-rough m 上的短素数区间总计数；
  若该总量超预算，则必须存在 cofactor-anchor / SAE / ColumnCRT / PDEC。
```

新增 `prime-matrix-pcolumn-fartail-model-payment.md` 后，远尾分支又被压成常数付款接口。令

\[
Model_{tail}=\sum_m |I_m|/\log(q_m^-).
\]

样本 `P<=200003` 的 top 近截止风险行显示 `actual/model` 接近 `1`，而闭合允许常数均大于 `1.107`。取

```text
C_tail = 1.05
```

扫描每个样本的 top-16 风险行，全部满足

\[
T_{\le10Y}+1.05\,Model_{tail}<S.
\]

最紧样本 `P=20011,y=71` 仍有付款余量 `78.398`。

## 7. 当前最小硬点

新的最小硬点应写成：

```text
PColumn Dynamic Capacity:
  对所有奇素数 P 与 2<=y<=P+1，
  令 Y=P^0.43。
  证明 T_Y(P,y)<|S_Y(P,y)|；
  等价地，证明 D_+(P,y)<S(1-H)。
```

若直接不等式失败，则失败必须落入以下出口之一：

```text
1. NearCutoff Anchor Spike:
   刚超过 Y 的高素 q 在同一锚点行低重叠同步；

2. FarTail-Cofactor Bound:
   远尾 q>10Y 正偏差由 Y-rough m 短素数区间超额承担；
   当前目标是证明 tail <= 1.05*Model_tail；

3. PDEC:
   低模轮平移相位反复支撑正偏差；

4. SAE:
   单个短窗口或少数 q 桶承担异常命中；

5. ColumnCRT:
   第 P 列锚残基 Py mod q 产生持久列位移同步。
```

这一步不是行命题的最终无条件证明；它把用户提出的全行全列夹击模型压成了一个严格、统一、可继续攻击的相对筛容量方程。
