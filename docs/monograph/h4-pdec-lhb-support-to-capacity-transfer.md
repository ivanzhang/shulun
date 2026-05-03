# H4-PDEC LHB 支撑相位到容量行转移引理

**状态：** `lhb_support_to_capacity_transfer_conditions_proved`

本文处理 `h4-pdec-lhb-column-phase-blocks.json` 中 `WHOLEDEF/BRIDGED` 诊断支撑行的关键缺口：相位支撑集合 `C` 的大小不能自动成为

\[
\sum_{t\in C}g(t)
\]

的容量界，因为 `g(t)` 是 persistent 坏窗集合在相位 `t` 上的计数，可能有多重度。本文给出把支撑行升级为 `A g<=b` 行的精确条件。

## 1. 支撑行与容量行的区别

设 `C\subset Z/QZ` 是相位块。机器证书中常见两种不同语义：

```text
support row:
  C 是某类相位的支撑集合；

capacity row:
  sum_{t in C} g(t) <= B。
```

`support row` 只说明哪些相位属于某结构类型；它不控制同一相位中出现多少个坏窗。若没有额外多重度界，不能把

\[
B=|C|
\]

写入正式 `PDEC-Dual-Cert`。

## 2. 空异常块转移

**Lemma H4-LHB-T1（空相位块容量）。**
若 `C=emptyset`，则对任意 `g(t)>=0`，

\[
\sum_{t\in C}g(t)=0.
\]

因此 `AFFINE/NEGDELTA/UNBRIDGED` 这类已物化为空的异常块可以作为有限 `A` 行

\[
\sum_{t\in C}g(t)\le0.
\]

**证明。**
空和为 `0`。该结论不依赖 `S` 的多重度。证毕。

## 3. 相位指示型转移

**Lemma H4-LHB-T2（相位指示型容量）。**
若当前证书对象不是一般计数向量，而是相位指示向量

\[
g(t)\in\{0,1\},
\]

则任意相位块 `C` 满足

\[
\sum_{t\in C}g(t)\le |C|.
\]

**证明。**
每个相位最多贡献 `1`，求和即得。证毕。

**审稿边界。**
PDEC 默认对象是坏窗计数向量，不是相位指示向量。因此 `WHOLEDEF/BRIDGED` 的 `bound=|C|`
只能在明确把证书降为“相位级存在性证书”时使用，不能自动用于 persistent 多重集合。

## 4. 有界多重度转移

**Lemma H4-LHB-T3（有界多重度容量）。**
设存在函数 `M(t)` 使正式坏窗集合 `S` 满足

\[
g(t)\le M(t),\qquad t\bmod Q.
\]

则任意相位块 `C` 满足

\[
\sum_{t\in C}g(t)\le \sum_{t\in C}M(t).
\]

特别地，若 `M(t)<=M_0`，则

\[
\sum_{t\in C}g(t)\le M_0|C|.
\]

**证明。**
逐相位相加即可。证毕。

**可用来源。**
`M(t)` 可以来自：

```text
有限 CRT 周期内完整计数；
phase_cap_t；
窗口互斥；
尾锚不可复用；
已证路由后剩余分支的 multiplicity cap。
```

没有 `M(t)` 时，`|C|` 只是支撑大小，不是容量。

## 5. 允许全集转移

**Lemma H4-LHB-T4（允许全集投影容量）。**
若已证明正式坏窗集合 `S` 是某个允许全集 `Z` 的子集，且

\[
C_Z(C)=\#\{x\in Z:\tau(x)\in C\}
\]

可计算或可上界，则

\[
\sum_{t\in C}g(t)\le C_Z(C).
\]

**证明。**
这是 `H4-PDEC-S2` 对相位块 `C` 的直接应用。证毕。

**审稿边界。**
要把 `WHOLEDEF/BRIDGED` 变成正式 `A` 行，最稳妥路径不是使用 `|C|`，而是证明

```text
S subset Z_LHB
```

并计算 `Z_LHB` 在这些相位块上的投影计数。

## 6. 对 WHOLEDEF/BRIDGED 的准入结论

`h4-pdec-lhb-column-phase-blocks.json` 中：

```text
WHOLEDEF: whole_deficit_phases；
BRIDGED : bridged_critical_phases。
```

两者当前是 `diagnostic-phase-support`。它们升级为容量行有三条合法路线：

1. **相位级证书路线：** 证明当前 `g` 是相位指示向量，用 `|C|` 作为界；
2. **多重度路线：** 证明 `g(t)<=M(t)`，用 `sum_C M(t)` 作为界；
3. **允许全集路线：** 证明 `S subset Z_LHB`，用 `# {x in Z_LHB: tau(x) in C}` 作为界。

当前尚未完成的是第 2 或第 3 条路线所需的 `M(t)` 或 `Z_LHB`。因此：

```text
WHOLEDEF/BRIDGED phase_block 已物化；
WHOLEDEF/BRIDGED capacity bound 尚未物化。
```

## 7. 下一步最小任务

下一步不应再把 `bound=phase_block_size` 当作容量界，而应选择以下更具体目标之一：

```text
T3-multiplicity:
  从 phase_cap_t 或窗口互斥推出 M(t)，生成 bound=sum_C M(t)；

T4-allowed-set:
  定义 Z_LHB，并证明 S subset Z_LHB，再枚举 C_Z(C)；

phase-indicator fork:
  明确切换到相位级证书，声明该证书只验证相位集合，不验证 persistent 多重坏窗。
```

对 H4-PDEC 最有价值的是 `T3-multiplicity`：它能直接与已有 `phase_cap_t` 和尾锚不可复用约束合并，形成真正可审计的 `A,b,E,e` 行。

## 8. T3 路线的正式化

新增 `h4-pdec-lhb-multiplicity-cap-route.md` 后，`T3-multiplicity` 已被精确化为：

```text
输入：同一 (p,Q,S,tau) 下的 M(t)；
证明：逐相位 g(t)<=M(t)；
输出：sum_{t in C} g(t)<=sum_{t in C} M(t)。
```

该文件同时固定了 `M(t)` 的三类合法来源：

```text
有限全集投影；
资源不可复用单射；
条件路由后的剩余分支上界。
```

因此当前剩余不再是“支撑能否当容量”的逻辑问题，而是更窄的机器与证明义务：
物化 `Q=2310`、同一正式坏窗集合 `S` 下的 `M(t)` 数组或公式，并逐项给出来源证明。
