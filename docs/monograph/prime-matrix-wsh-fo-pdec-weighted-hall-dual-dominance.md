# FO-PDEC 加权 Hall 对偶支配定理

**状态：** `weighted_hall_full_duplicate_mass_blocked_not_global_pdec`

本文承接：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.md
docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.md
```

目标是处理当前最窄硬点中的一个子问题：嵌套 Hall 块的同一正式坐标重复，能否通过
fractional Weighted Hall dual 恢复成完整第二单位 PDEC 质量。

结论是否定的：在当前 FO-PDEC 审计对象中，分数加权对偶不能把这些嵌套重复重新计成完整第二单位。
因此 `global_library_raw` 的 `3.959...` 强信号不能作为合法单分支下界使用；必须至少降到坐标
cap 口径。

## 1. Laminar block 记号

设一个 Hall 块 `B` 的候选半素数支撑为 `S(B)`，邻近可用素数集合为 `N(B)`，定义

\[
\sigma(B)=|N(B)|-|S(B)|
\]

为 surplus。若 `B_0 subset B_1`，则差层为

\[
\Delta S=S(B_1)\setminus S(B_0),\qquad
\Delta N=N(B_1)\setminus N(B_0),
\]

其增量 surplus 为

\[
\Delta\sigma=\sigma(B_1)-\sigma(B_0)
              =|\Delta N|-|\Delta S|.
\]

一个同坐标重复事件 `e` 若同时出现在 `B_0` 与 `B_1`，且 `e in S(B_0)`，则独立化后的差层
`B_1\setminus B_0` 并不包含 `e`。

## 2. 加权支配引理

**引理 WHD-1（laminar 零压力差层不能支付重复坐标）。**  
设 `B_0 subset B_1`，同一正式坐标事件 `e` 位于 `S(B_0)`。若

```text
Delta sigma >= 0
```

则任何只由 laminar 差层提供的 fractional Weighted Hall dual 不能给 `e` 增加第二个完整单位权重。

**证明。**  
对嵌套约束做标准 laminar 化：把大块行分解为小块行与差层行。小块行已经包含 `e`；差层行
`S(B_1)\setminus S(B_0)` 不包含 `e`。因此差层若要给 `e` 付款，只能通过非局部耦合约束，而不是
通过当前 Hall 块自身的独立坐标。

另一方面，`Delta sigma >= 0` 表示差层没有产生新的 Hall 缺陷压力；差层新增的可用素数不少于新增
的半素数候选。它至多解释“大块为何仍然安全”，不能提供一个新的负压约束来把 `e` 重复计算为第二
个独立 PDEC 事件。因此同一正式坐标的合法完整单位权最多来自包含它的最小块行；第二单位若要保留，
必须提交额外的非 laminar weighted dual 证书，并且同一多重 formal unit 的 `U_CRT` 上界也要按相同
权重重算。证毕。

## 3. 当前 FO-PDEC 的应用

审计给出 7 个 exact nested duplicates，全部满足：

```text
same formal coordinate: true
support relation:       smaller support subset larger support
Delta semiprime:        1
Delta prime:            1
Delta surplus:          0
```

所以它们全部落入 WHD-1。特别是 `ell=199,h=95` 的关键重复

```text
[1993, 836, 836, 82, 30, 1664237, 199, 40]
```

也不能通过 fractional Weighted Hall dual 恢复完整第二单位质量。

## 4. 数值口径后果

`prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.md` 记录了同一数据在不同合法口径下的变化：

```text
global_library_raw:       Fourier = 3.959247567099438
nested_coordinate_cap:    Fourier = 2.9698366905785227
physical_candidate_cap:   Fourier = 1.9997507790353146
single_q_row_coordinate:  Fourier = 1.0
single_block:             Fourier = 1.0
```

因此强阈值路线的当前真实分支是：

```text
若能证明 cross-q persistence:
    攻 coordinate-cap PDEC threshold, 即 U_CRT < 2.9698366905785227；
否则:
    进入 physical/primitive PDEC threshold 或 SAE/Endpoint absorption。
```

## 5. 边界

本文闭合的是一个子门：

```text
FractionalWeightedHallCannotRecoverFullNestedDuplicateMass
```

它不是完整 `PDEC exclusion`，也不是完整 Prime Matrix 行/列无条件定理。剩余仍是：

```text
cross-q persistence theorem；
coordinate-cap PDEC threshold；
physical/primitive PDEC threshold；
SAE/Endpoint absorption；
三终端证书全集与 D-structure/Tail-log4/Rankin 接口。
```
