# FO-PDEC 分支分离与拼接硬点定理

**状态：** `branch_separation_proved_stitching_theorem_open`

本文在 `FO-PDEC` 主线上继续硬攻 `FormalUnit-Stitching / NestedBlock-Independence`。结论不是全局闭合，
而是严格证明：当前 `3.959...` 强阈值不能在没有额外拼接定理时直接进入单个正式反例分支。

## 1. Formal event 与投影

记一条低模解释方程为

```text
e=(q,row,candidate_row,column,offset,n,ell,rho,block).
```

其中 `ell|n` 且

\[
  \rho\equiv row\equiv 1-column\cdot q^{-1}\pmod{\ell}.
\]

有三个自然投影：

```text
pi_coord(e)=(q,row,candidate_row,column,offset,n,ell,rho);
pi_layer(e)=(q,n,ell,rho);
pi_phys(e)=(n,ell).
```

`block` 只记录该事件来自哪个 Hall 块；它本身不是新的整数或新的 CRT 方程。

## 2. 分支分离引理

**引理 BS-1（不同 q 层不能自动拼接）。**  
若两条事件 `e1,e2` 满足 `q1!=q2`，则它们属于不同方阵宽度的 formal branch。除非另有
`cross-q persistence theorem` 证明同一假设反例链同时强制这两个层级事件，否则 `e1,e2`
不能放入同一个 `PDEC` 相位向量。

**证明。**  
单个 `PDEC` 证书的输入是一个坏窗集合 `S` 与一个相位映射 `tau:S->Z/QZ`。固定方阵宽度
`q` 后，行列坐标、固定偏移、Hall 块、端点镜像和列容量约束都以该 `q` 为参数。若把
`q1` 层和 `q2` 层事件合并，必须同时给出共同索引域和共同约束行；否则下界使用的是
`S1∪S2`，上界却没有同一套 `A,b,E,e` 约束。故无拼接定理时不能合并。证毕。

## 3. 坐标商引理

**引理 BS-2（同坐标嵌套重复必须商掉或加权证明）。**  
若 `pi_coord(e1)=pi_coord(e2)` 而 `block(e1)!=block(e2)`，则二者给出完全相同的整数、解释因子、
CRT 行相位和双线性方程。除非提供加权 Hall 对偶行证明这两个 block occurrence 是不同独立约束，
否则它们在 `PDEC` 向量中只能计为一个坐标事件。

**证明。**  
由 `pi_coord(e1)=pi_coord(e2)`，两条事件有同一

\[
  (q,row,candidate\_row,column,offset,n,\ell,\rho).
\]

所以它们满足同一条

\[
  row\equiv 1-column\cdot q^{-1}\pmod\ell
\]

以及同一条 `uv+offset=0 mod ell`。算术上没有第二个独立缺陷。若仍要计两次，唯一合法来源是
`S` 被定义为带 `block` 标签的多重集合，并且 Hall 对偶证明两个 block 标签分别对应独立约束行；
同时 `U_CRT` 上界也必须按同一多重集合计算。若没有这套加权对偶证明，`PDEC` 的同一集合原则迫使
通过 `pi_coord` 取商。证毕。

## 4. 对当前 `ell=199` 的应用

审计文件：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-stitching-feasibility-audit.md/json
```

给出：

```text
global library raw:        mass=4, Fourier=3.959247567099438
q-row coordinate dedup:    best Fourier=1.0
block-local best:          best Fourier=1.0
exact nested duplicates:   7
cross-level reuses:        9
```

其中最佳因子 `ell=199` 的两个关键重复为：

1. `1664237=199*8363` 在同一 `q=1993,row=836,column=82,offset=30` 中由 block `1`
   与 block `4` 重复出现，属于 BS-2；
2. `250541=199*1259` 在 `q=773,row=325` 与 `q=967,row=260` 中复用，属于 BS-1。

因此 `3.959...` 是库级诊断信号，不是当前已证的单分支下界。

## 5. 新的最窄闭合目标

全局证明若继续使用强阈值，必须补齐两个定理：

```text
Weighted Hall Dual Independence:
嵌套 block occurrence 可作为不同独立约束行计入同一个多重 PDEC 向量；

Cross-q Persistence Theorem:
同一正式反例链会强制出现当前跨 q 层复用事件，并给出统一相位映射与约束行。
```

若二者任一失败，则对应重复必须进入：

```text
coordinate quotient / primitive threshold / SAE-Endpoint absorption.
```

## 6. 审稿级结论

本轮闭合的是“不能误用库级聚合阈值”的逻辑缺口。当前仍未达到方阵行命题或全局主命题的
无条件证明。下一步最小可攻目标应是：

```text
先攻 Weighted Hall Dual Independence；
若失败，证明 exact nested duplicates 全部是 SAE/Endpoint 或坐标商事件。
```

这比继续直接优化 `U_CRT,199` 更优先，因为没有 BS-1/BS-2 的合法性，`U_CRT,199<3.959...`
本身不是同一 formal unit 上的命题。
