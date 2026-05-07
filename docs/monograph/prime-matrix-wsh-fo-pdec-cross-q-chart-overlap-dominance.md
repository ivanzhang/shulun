# FO-PDEC cross-q 坐标图重叠支配定理

**状态：** `cross_q_coordinate_persistence_rejected_for_audited_fo_pdec`

本文承接：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.md
docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-dominance.md
```

目标是处理上一轮留下的最窄硬点：

```text
cross-q persistence theorem
```

结论是：当前 FO-PDEC 有限前沿中的 cross-q 复用不是一个可用的独立持久化定理入口；它们全部是同一
物理候选在两个重叠 `q` 行坐标图中的表示。因此 coordinate-cap 的 `2.9698366905785227` 仍不能作为
单个正式反例分支的 PDEC 下界。当前必须降到 physical/primitive 口径，或把这些复用送入
SAE/Endpoint。

## 1. 坐标图恒等式

同一整数 `n` 在宽度 `q_1,q_2` 的两张方阵坐标图中写成

\[
n=(r_1-1)q_1+c_1=(r_2-1)q_2+c_2.
\]

若

\[
(r_2-1)q_2-(r_1-1)q_1=-(c_2-c_1),
\tag{CQ-1}
\]

则两个事件只是同一个物理整数的坐标变换。此时行残基

\[
r_i \bmod \ell
\]

可以随坐标图改变，但物理解释因子、半素数核心和 offset 并没有产生第二个独立缺陷。

## 2. 支配引理

**引理 CQ-1（坐标图重叠不产生独立 PDEC 质量）。**  
设两个低模方程事件满足：

```text
same candidate n；
same semiprime core b；
same offset d；
same explaining factor ell；
same physical identity n=b+d；
and coordinate identity (CQ-1)。
```

则它们不能仅因 `q` 层不同而作为同一 PDEC 向量中的两个独立单位质量。合法选择只有：

```text
物理候选去重；
或提交新的非坐标图 cross-q persistence theorem；
或把稀疏复用送入 SAE/Endpoint。
```

**证明。**  
PDEC 的下界与上界必须作用在同一个 formal unit 上。若两个事件只是同一物理整数 `n` 的不同
坐标图表示，则把它们都计入下界等价于给同一个物理缺失候选赋予 coordinate multiplicity。
但上界侧若没有同一多重 formal unit 和独立约束行，就只能约束物理候选一次。行残基变化
`r_1 mod ell` 到 `r_2 mod ell` 来自坐标图起点变化，不是新的合数解释，也不是新的补洞压力。
因此无额外 cross-q persistence theorem 时必须物理去重。证毕。

## 3. 当前 FO-PDEC 的应用

审计得到 9 个 cross-q reuses，全部满足：

```text
q layers:        [773, 967]
base_gap:        1
column_gap:     -1
candidate_gap:   0
same physical candidate / semiprime / offset / factor: true
```

尤其关键 `factor=199` 复用为：

```text
candidate=250541=199*1259；
q=773,row=325,column=89,residue=126；
q=967,row=260,column=88,residue=61；
row bases: 250452 and 250453。
```

它只是同一整数 `250541` 的两个重叠坐标图，不能作为两个独立 PDEC 事件。

## 4. 前沿后果

结合 weighted-Hall 子门，本轮得到：

```text
raw library signal 3.959247567099438:
  blocked by nested duplicate dominance；

coordinate-cap signal 2.9698366905785227:
  blocked for current sample by cross-q chart overlap；

remaining physical/primitive signal:
  1.9997507790353146。
```

因此当前最窄剩余变成：

```text
physical/primitive PDEC threshold U_CRT < 1.9997507790353146；
或 SAE/Endpoint absorption for physical cross-chart reuses。
```

## 5. 边界

本文只排斥当前已审计 FO-PDEC 有限前沿中的 cross-q 坐标图持久化误用。它不排斥未来可能出现的
非重叠 cross-q persistence theorem，也不闭合完整 `PDEC family`。完整行/列无条件定理仍需三终端
证书全集。
