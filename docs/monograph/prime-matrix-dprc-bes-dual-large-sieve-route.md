# DPRC-BES 对偶大筛路线

**状态：** `proof_route_not_a_proof`

本文接续 `DPRC beta桶能量-同步性硬点`。目标是把 BES 的失败形态写成可审稿的结构出口，而不是停留在实验包络。

## 1. 中心化核

固定 `alpha=0.43`、`Y=P^alpha`，令

\[
S=S_Y^\pm(P),\qquad 1_S(k)=1_{k\in S}.
\]

对剩余高素 `Y<q<P` 定义覆盖相位

\[
\rho_q^\pm(P)\equiv
\begin{cases}
-P^2\pmod q,& plus,\\
 P^2\pmod q,& minus.
\end{cases}
\]

中心化单线核为

\[
\psi_q(k)=1_{k\equiv \rho_q^\pm(P)\pmod q}-{1\over q}.
\]

对 beta 桶 `B`，

\[
D_B=\sum_{k\in S}\sum_{q\in B}\psi_q(k)
=\langle 1_S,\Psi_B\rangle,
\qquad
\Psi_B(k)=\sum_{q\in B}\psi_q(k).
\tag{DLS-1}
\]

BES 的正偏差向量就是

\[
x_B={D_B^+\over \sqrt{|S|}}.
\]

## 2. 危险交集

当前足够闭合 DPRC-RSM 的目标可写为两个等价攻击口：

```text
BES-A:
  ||x||_1 >= 12/5  =>  ||x||_2 <= 6/5；

BES-B:
  ||x||_2 > 3/sqrt(6)  =>  ||x||_1 < 12/5。
```

两者都只需排除同一个危险交集：

\[
\|x\|_1\ge {12\over5}
\quad\text{and}\quad
\|x\|_2>{6\over5}
\tag{DLS-2}
\]

或更强地排除

\[
\|x\|_1\ge {12\over5}
\quad\text{and}\quad
\|x\|_2>{3\over\sqrt6}.
\tag{DLS-3}
\]

审计到 `P<=100000` 时 `(DLS-2)` 与 `(DLS-3)` 的记录数均为 `0`。

## 3. 失败的强制形态

若 `(DLS-2)` 失败，则正桶向量同时满足高总量和高能量。由

\[
d_{\rm eff}={\|x\|_1^2\over \|x\|_2^2}
\]

可知

\[
d_{\rm eff}<4
\]

当 `||x||_1>=12/5` 且 `||x||_2>6/5`。因此失败不是六桶均匀小涨，而是：

```text
少数 beta 桶贡献了大部分正偏差；
同时其余桶仍提供足够正和，使总 L1 达到 12/5。
```

用鸽巢可抽取至少一个尖峰桶 `B*`：

\[
D_{B^*}^+\ge {\|x\|_2^2\over \|x\|_1}\sqrt{|S|}
> {3\over5}\sqrt{|S|}.
\tag{DLS-4}
\]

并且存在额外正偏差总量

\[
\sum_{B\ne B^*}D_B^+
\ge \left({12\over5}-x_{B^*}\right)\sqrt{|S|}.
\tag{DLS-5}
\]

若单桶已经接近或超过 `12/5 sqrt(S)`，则进入单桶 SAE/PDEC；否则剩余正和必须由其他尺度桶共同承担，进入多尺度同步分析。

## 4. 二次能量展开

尖峰桶的平方可写为

\[
D_B^2
=
\sum_{k,\ell\in S}
\sum_{q,q'\in B}
\psi_q(k)\psi_{q'}(\ell).
\tag{DLS-6}
\]

把 `(q,k)` 看作命中边，正能量超过大筛基线时只有三种来源：

```text
PointLoad:
  同一个 k 被过多 q 命中；

ShortWindow:
  某个 q 子区间的互补因子窗口 m=(P^2±k)/q 过密；

LowPhase:
  多个 q 的相位 rho_q 在同一低模投影上同向偏斜。
```

这三类正好对应：

```text
PointLoad      -> ColumnCRT / tail-anchor；
ShortWindow    -> SAE；
LowPhase       -> PDEC。
```

## 5. 小模连乘刚性入口

因为 `S` 已经筛掉全部 `q<=Y`，每个剩余命中满足

\[
P^2\pm k=qm,\qquad (m,\prod_{\ell\le Y}\ell)=1.
\tag{DLS-7}
\]

所以 `D_B` 不是任意同余命中偏差，而是粗互补因子短窗的偏差：

\[
D_B=
\sum_{q\in B}
\left(
\#\{m\in I_q^\pm(P):(m,\prod_{\ell\le Y}\ell)=1\}
-{|S|\over q}
\right).
\tag{DLS-8}
\]

若多个 beta 桶同时正偏，意味着多个不同长度的 `m` 窗口在同一个动态轮底座上同向超密。
这正是小模连乘同余刚性可以发挥作用的地方：低模单位类不能在多个不同比例窗口内同时向同一端点相位倾斜，除非产生低模 Fourier 缺陷。

## 6. 下一步可证明接口

把 BES 失败排斥拆成三个可提交子命题：

```text
DLS-PointLoad:
  若某个 k 的剩余高素标签负载超过正常上界，则进入 ColumnCRT/tail-anchor。

DLS-ShortWindow:
  若某个 beta 桶的正偏差由短 q 子区间贡献固定比例，则进入 SAE。

DLS-LowPhase:
  若正偏差在 q 子区间分散，则中心化核的低模投影能量超过阈值，
  产生 PDEC 证书。
```

目标链更新为：

```text
BES danger intersection
=> PointLoad or ShortWindow or LowPhase
=> ColumnCRT or SAE or PDEC
=> DPRC-RSM closed after exits are excluded。
```

这把“高素斜线补洞过强”的剩余问题，转成了三个可以逐个给证书的结构出口。

## 7. 近危险审计后的优先级

新增 `docs/monograph/prime-matrix-dprc-bes-nearmiss-structure-audit.md` 后，10 个代表样本显示：

```text
PointLoad:
  max point load 全部为 4，暂未出现单点爆炸；

ShortWindow:
  最强短 q 子窗峰值约 0.25 到 0.38 sqrt(S)，局部但不够危险；

LowPhase:
  mod30 单位类内部偏斜最稳定，all/mod30 峰值最高到 0.902430 sqrt(S)。
```

所以当前优先级应调整为：

```text
1. DLS-LowPhase / WheelUnitPhaseBalance；
2. ShortWindow-SAE；
3. PointLoad-ColumnCRT。
```

特别地，`mod30` 顶峰全部落在 `P^2±k mod 30` 的单位类中。这说明异常不是小素数筛遗漏，
而是单位类内部的有向偏斜；它最适合用低模 Fourier/PDEC 证书处理。
