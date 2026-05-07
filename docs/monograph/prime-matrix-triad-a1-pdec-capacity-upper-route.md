# Triad-A1：PDEC 同一坏窗容量上界路线

**状态：** `triad_a1_capacity_upper_route_not_closed`

本文承接 `prime-matrix-terminal-certificate-triad.md`，直接攻击三终端中的第一硬点：

```text
Triad-A1: 对同一坏窗集合建立 PDEC capacity upper U_CRT。
```

核心原则是：`PDEC` 下界 `L_PDEC` 与上界 `U_CRT` 必须作用在同一个坏窗推前计数向量 `g(t)` 上。
任何背景全集、完整 CRT 周期或方便替代集合的容量，都不能直接作为 `g(t)` 的上界，除非先证明当前
坏窗集合嵌入该允许全集。

## 1. A1 目标方程

固定一个已经同口径拆分的 persistent 分支：

```text
theta=(formal unit Omega, signature tau, bad-set S, test F, kappa, route source)。
```

令

\[
g(t)=\#\{x\in S:\tau(x)=t\}.
\]

PDEC 下界给出

\[
L_{\rm PDEC}
=
{\kappa |S|\over \sqrt{|G|-1}\|F\|_2}.
\tag{A1-1}
\]

容量上界定义为同一约束系统上的对偶最优值：

\[
U_{\rm CRT}(h,\zeta;\theta)
=
\sup_{g\in \mathcal P_\theta}
\Re\left\{\zeta\sum_{t\in G}g(t)e(ht)\right\},
\tag{A1-2}
\]

其中

```text
P_theta = {g>=0: A_theta g<=b_theta, E_theta g=e_theta}。
```

`Triad-A1(theta)` 闭合当且仅当对所有 `h!=0` 与所有方向 `zeta` 有

\[
U_{\rm CRT}(h,\zeta;\theta)<L_{\rm PDEC}.
\tag{A1-3}
\]

若 `(A1-3)` 失败，失败对象必须输出 `DualCap`、缺失容量行或命名出口路由，不能停在“上界不够强”。

## 2. 同一坏窗集合律

**Same-Set Law.** 任一容量行进入 `A_theta g<=b_theta` 前，必须满足三者之一：

```text
Tautology:
  对任意 S 都成立，如 g>=0、质量范围。

Attachment:
  已证明 S subset Z_theta，于是继承 Z_theta 的相位/块容量。

ConditionalRouting:
  已证明违反该行必进入某个已剥离出口 E，当前分支正在处理 non-E 剩余。
```

禁止使用：

```text
完整 CRT 周期均匀性 => 任意坏窗子集均匀；
有限样本相位表     => 无限族相位容量；
背景全集 mirror     => 子集 mirror equality；
不同 formal unit 的多重计数 => 当前 g(t) 上界。
```

这条律把 A1 从统计估计问题改写为集合嵌入与路由证明问题。

## 3. 容量行生成器

对每个 `theta`，容量上界系统按以下顺序生成。

### 3.1 恒真行

```text
g(t)>=0；
sum_t g(t)=|S|，若 |S| 精确登记；
S_min<=sum_t g(t)<=S_max，若只知范围。
```

### 3.2 附着行

若证明 `S subset Z_theta`，则加入：

```text
phase cap:
  g(t)<=C_Z(t)；

block cap:
  sum_{t in T}g(t)<=C_Z(T)；

mirror-pair cap:
  g(t)+g(rho(t))<=C_Z({t,rho(t)})；

low-hole bucket:
  sum_{h_Q(t)>=m}g(t)<=B_m。
```

强 `mirror equality` 只有在额外证明 `m(S)=S` 时才可加入；否则必须降级为 mirror-pair cap。

### 3.3 条件路由行

若当前分支已经剥离对应出口，可加入：

```text
tail-anchor nonreuse cap；
cofactor-anchor cap；
displacement/ColumnCRT cap；
endpoint seam cap；
core-overlap cap；
Rankin/H5 exit cap。
```

每一行必须带元数据：

```text
excluded_exit；
source theorem；
phase compatibility proof；
normalization of g；
threshold B。
```

若缺少相位兼容性，必须细化 `tau` 或改用点级计数；不能把点级事件硬投影到旧 `g(t)`。

## 4. A1 失败的强制输出

若对某个 `(h,zeta,theta)` 无法证明 `(A1-3)`，必须输出以下四类之一：

```text
AttachmentFail:
  不能证明 S subset Z_theta。
  => 当前坏窗没有合法容量背景，必须回流 LocalSurvivor 或生成新 PDEC 分支。

PhaseCompatFail:
  某容量事件不由 tau(t) 决定。
  => 细化 signature，进入 refined/weighted/primitive PDEC；若只孤立发生，进 LocalSurvivor。

CapacityInsufficient:
  合法行全部加入后仍有 U_CRT>=L_PDEC。
  => 输出 LP/对偶极值支持相位块，按 PDEC dual-failure 形成 DualCap。

RoutingGap:
  需要某条件行，但对应出口尚未剥离。
  => 先攻该出口的 LocalSurvivor/PDEC/CleanKLS 证书。
```

因此 A1 失败不会生成第四出口；它只会指出缺少哪条集合嵌入、哪条相位兼容、哪个 cap 聚簇或哪个未剥离
命名出口。

## 5. 递归剥离协议

对最小反例族执行：

```text
Step 1. Homogeneous split:
  按 formal unit、tau、F、kappa、window-shape 无损拆分坏窗集合。

Step 2. Attach:
  对每个 theta 证明 S_theta subset Z_theta；失败进入 AttachmentFail。

Step 3. Generate:
  只加入 Tautology、Attachment、ConditionalRouting 三类合法容量行。

Step 4. Dual solve:
  对全部 h!=0 和外向方向弧计算 U_CRT。

Step 5. Compare:
  若 U_CRT<L_PDEC，theta 分支排除；
  否则输出 DualCap 或缺失行，并按第 4 节回流。
```

这是一套持续可迭代方法：每次失败都会增加签名、缩小支撑、剥离出口或提交局部 witness。固定签名层
由有限原子数终止；无限升层由塔熵二分终止。

## 6. 与现有 H4 文件的接口

当前可直接接入的已有结果：

```text
h4-pdec-certificate-template.md:
  给出 L_PDEC 与 U_CRT 对偶证书格式。

h4-pdec-constraint-source-lemmas.md:
  给出 mass、phase cap、mirror-pair cap、bucket cap、routing row 来源规则。

h4-pdec-admissible-constraint-table.md:
  标出 Tautology / FiniteCert / SymbolicReady / ConditionalRouting / Rejected。

h4-pdec-homogeneous-splitting-lemma.md:
  处理口径混合。

h4-pdec-column-defect-routing-contract.md:
  给出 displacement/ColumnCRT 条件行的相位兼容与路由合同。
```

还不能直接接入为全局无条件行的是：

```text
有限 phase block 直接推广到无限 P；
未证明 S subset Z 的背景容量；
未剥离出口上的 ConditionalRouting；
未给相位兼容权重的列/尾/核心事件。
```

## 7. 当前最小硬点

A1 的下一步不应继续发散为新常数，而应选择一个 `theta` 家族，补齐以下三项：

```text
A1.1 Attachment:
  证明该 persistent 坏窗族 S_theta subset Z_theta。

A1.2 Phase-compatible rows:
  物化 tau-compatible 的 phase/block/column/tail 权重。

A1.3 Dual comparison:
  对全部非零频率与方向弧证明 U_CRT<L_PDEC，或输出 DualCap。
```

优先级上，最适合先攻的是已经有 `LHB attachment`、`multiplicity cap` 与 `ColumnDefect routing`
元数据的分支；它离正式 `A_theta,b_theta,E_theta,e_theta` 最近。

新增 `prime-matrix-triad-a1-lhb-branch-capacity-skeleton.md` 后，这个优先分支已被单独物化：

```text
Q=2310 LHB-typed branch；
S subset Z_LHB；
g(t)<=M(t)；
WHOLEDEF/BRIDGED zero-cap rows；
general LP/dual U_CRT<L_PDEC still open。
```

这把 A1 的下一步从“找容量上界”进一步压成“对 Q=2310 LHB 分支生成 theta 级 LP/对偶证书”。

## 8. 结论

`Triad-A1` 已被压成一个确定协议：

```text
同口径拆分
=> Same-Set Law
=> 合法容量行生成
=> LP/对偶上界 U_CRT
=> 与 L_PDEC 比较
=> 失败输出 AttachmentFail / PhaseCompatFail / DualCap / RoutingGap。
```

本文完成的是 A1 的证明路线和失败回流合同。它仍未提交任何全局 `U_CRT<L_PDEC` 证书。
