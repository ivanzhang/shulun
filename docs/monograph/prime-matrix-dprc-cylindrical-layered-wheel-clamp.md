# 圆柱斜线与层叠轮筛的夹击矛盾场

**状态：** `reduction_framework_not_a_proof`

本文把两个方向合并：

```text
方阵斜线 / 圆柱螺旋覆盖：
  研究高素斜线能否补掉动态粗骨架上的所有洞；

P^2±k mod 30/210/2310/... 层叠轮筛：
  研究这些补洞命中能否在小模单位类中同步偏斜。
```

目标是把“`P x P` 方阵内不出现零行”压成一个夹击矛盾场：

```text
若零行存在，
  几何上必须有足够多高素斜线补洞；
  相位上这些补洞必须在层叠轮单位类中同步；
但容量、能量、低模相位三者不能同时满足。
```

## 1. 几何侧：圆柱斜线容量

固定平方前/后端点：

```text
plus:  P^2+k,  1<=k<P；
minus: P^2-k,  1<=k<P。
```

取动态提升轮

\[
Y=P^{0.43}.
\]

低素数 `q<=Y` 已经提升到底座，剩余粗骨架为

\[
S_Y^\pm(P)=
\{1\le k<P:(P^2\pm k,\prod_{\ell\le Y}\ell)=1\}.
\]

剩余高素斜线命中总量为

\[
T_Y^\pm(P)=
\sum_{Y<q<P}
\#\{k\in S_Y^\pm(P):q\mid P^2\pm k\}.
\]

若整行被覆盖，必须有

\[
|S_Y^\pm(P)|\le T_Y^\pm(P).
\tag{CLW-1}
\]

因此 `T_Y<S_Y` 直接排除零行。这是圆柱斜线模型的一阶容量夹击。

## 2. 相位侧：层叠轮单位类

对任意小模连乘轮

\[
W=30,210,2310,30030,\ldots
\]

素数只能落在单位类 `U_W`。平方端点行中，真实数值残基为

\[
n_k^\pm=P^2\pm k\pmod W.
\]

动态粗骨架已经排除 `q<=Y`，但剩余高素 `q>Y` 的补洞命中仍会在 `U_W` 内出现偏斜。定义中心化单位类偏差：

\[
E_a(W)=
\sum_{\substack{k\in S_Y^\pm(P)\\ n_k^\pm\equiv a\pmod W}}
\sum_{Y<q<P}
\left(1_{q\mid P^2\pm k}-{1\over q}\right),
\qquad a\in U_W.
\tag{CLW-2}
\]

若某个 `E_a(W)` 很大，则出现 `W-unit PDEC`：高素斜线补洞在小模单位类中有有向偏斜。

## 3. 中间接口：BES 能量同步性

把剩余高素 `q` 按 `beta=log q/log P` 分成六个尺度桶，令

\[
x_B={D_B^+\over \sqrt{|S_Y^\pm(P)|}},
\]

其中 `D_B` 是该 beta 桶的中心化偏差。已建立的充分接口为：

```text
BES-A:
  ||x||_1 >= 12/5  =>  ||x||_2 <= 6/5；

BES-B:
  ||x||_2 > 3/sqrt(6)  =>  ||x||_1 < 12/5。
```

这两个接口都在排除同一个危险交集：

\[
\|x\|_1\ge {12\over5}
\quad\text{且}\quad
\|x\|_2>{6\over5}
\tag{CLW-3}
\]

或更强的 `||x||_2>3/sqrt(6)`。危险交集若存在，意味着高素斜线既有多尺度正偏差总量，又有能量尖峰。

## 4. 夹击逻辑

零行若存在，则必须穿过三道门：

```text
Gate 1: Geometry Capacity
  T_Y >= S_Y；

Gate 2: BES Synchronization
  D_+ 足够大，且 beta 桶正偏差不能被 Cauchy/能量界吸收；

Gate 3: Layered Wheel Phase
  补洞偏差要在 30/210/2310/... 的单位类中保持同步，
  否则低模偏斜分散，不能形成整行覆盖。
```

因此夹击矛盾场可写为：

```text
Zero row inside P x P
=> Geometry capacity pressure
=> BES danger intersection
=> PointLoad or ShortWindow or LowPhase
=> ColumnCRT or SAE or W-unit PDEC
=> 出口排斥后矛盾。
```

这不是单一固定规律，而是“逐层提升、逐层排斥”的极限筛法。

## 5. 当前审计证据

### DPRC-BES 全范围

`P<=100000, alpha=0.43`：

```text
P>=2003:
  records = 18578；
  max D_+/sqrt(S) = 2.468627；
  max ||x||_2 = 1.233496；
  danger intersections = 0。
```

### W=30 全范围

报告：

```text
docs/dprc_wheel_unit_phase_balance_w30_p100000_20260506.md
```

`P>=2003`：

```text
max unit30 peak = 1.076781；
对应 BES L1=0.493686, L2=0.281040；

high L1 count = 2；
high L1 max unit30 peak = 0.902430；

high L2 count = 1；
high L2 max L1 = 2.078474 < 12/5。
```

结论：`mod30` 单位类偏斜真实存在，但不同步。

### 30/210/2310 三层全范围扫描

报告：

```text
docs/dprc_layered_wheel_phase_scan_p100000_20260506.md
```

`P>=10007`：

| W | max unit peak | high L1 max unit peak | max L1 when peak>=0.8 |
|---:|---:|---:|---:|
| `30` | `1.076781` | `0.902430` | `2.442672` |
| `210` | `0.617936` | `0.331095` | `0.000000` |
| `2310` | `0.293727` | `0.175276` | `0.000000` |

轮层提升后，单单位类峰明显下降；正偏差被分散到更多单位类中。高 `BES L1` 样本在 `2310` 层没有单相位尖峰。

## 6. 结构解释

`P^2±k mod 30/210/2310/...` 的确构成一种新筛法视角：

```text
每一层 W 给出素数禁止类的刚性坐标；
补洞只能发生在 U_W；
但随着 W 提升，单位类数量增加，单类峰值被稀释；
若某层仍出现同步尖峰，它就是 PDEC 证书；
若所有层都不出现同步尖峰，则高素补洞只剩分散能量，由大筛控制。
```

这与圆柱斜线模型互补：

```text
圆柱斜线告诉我们“补洞需要多少容量”；
层叠轮筛告诉我们“补洞能否相位同步”。
```

二者夹击的核心不是证明某个固定轮 `W` 解决一切，而是证明：

```text
随着 W 逐层提升，
任何试图形成零行的补洞同步要么在某层显化为 PDEC/SAE/ColumnCRT，
要么被分散成大筛可控的平方根偏差。
```

## 7. 下一最小硬点

当前最小硬点建议改写为：

```text
LayeredClamp:
  对动态提升轮 Y=P^0.43，
  若 BES 危险交集发生，
  则存在有限小模轮 W<=2310 或短 q 窗口或点负载，
  产生 W-unit PDEC / SAE / ColumnCRT；
  否则 D_+<=3sqrt(S)，DPRC 闭合。
```

后续应继续两路推进：

```text
1. 计算证书：
   把 W=30/210/2310 的层叠扫描扩到 P<=100000；

2. 解析证书：
   证明单类峰随 phi(W) 增长被稀释，
   或证明未稀释的峰自动给出低模 Fourier/PDEC 证书。
```

这就是当前最贴近“无穷迭代、无穷层叠、无穷缠绕”直觉的严谨接口。
