# H4-PDEC LHB 多重度容量路线

**状态：** `t3_multiplicity_cap_route_formalized_not_materialized`

本文承接 `h4-pdec-lhb-support-to-capacity-transfer.md`。目标是把
`WHOLEDEF/BRIDGED` 这类相位支撑行升级为真正可进入 `PDEC-Dual-Cert` 的容量行。
核心点是：必须控制 persistent 坏窗计数向量

\[
g(t)=\#\{x\in S:\tau(x)=t\},\qquad t\in\mathbf Z/Q\mathbf Z,
\]

而不是只控制相位支撑集合的大小。

## 1. T3 输入对象

一个合法的 `T3-multiplicity` 输入包必须包含：

```text
Q；
phase map tau:S -> Z/QZ；
正式坏窗集合 S 的定义；
M(t) 数组或公式，0<=t<Q；
证明 g(t)<=M(t) 的来源；
需要升级的相位块 C_j；
容量界 B_j=sum_{t in C_j} M(t)。
```

若缺少 `M(t)` 或缺少 `g(t)<=M(t)` 的证明，则 `WHOLEDEF/BRIDGED` 只能保留为
`diagnostic-phase-support`。

## 2. 多重度容量引理

**Lemma H4-LHB-M1（逐相位多重度容量）。**
设 `S` 是当前分支的正式 persistent 坏窗集合，`tau:S->Z/QZ` 是证书使用的相位投影。
若存在非负函数 `M:Z/QZ->R_{\ge0}` 使得对每个相位 `t` 都有

\[
g(t)\le M(t),
\]

则任意相位块 `C` 满足

\[
\sum_{t\in C}g(t)\le \sum_{t\in C}M(t).
\]

**证明。**
对不等式 `g(t)<=M(t)` 在 `t in C` 上逐项求和。证毕。

## 3. `M(t)` 的三类合法来源

### 3.1 有限全集投影来源

**Lemma H4-LHB-M2（有限全集投影上界）。**
若已证明 `S subset Z`，且 `Z` 是可枚举有限全集，则

\[
M_Z(t)=\#\{z\in Z:\tau(z)=t\}
\]

满足 `g(t)<=M_Z(t)`。

**证明。**
每个 `S_t={x in S:tau(x)=t}` 都是 `{z in Z:tau(z)=t}` 的子集。证毕。

**审稿边界。**
`prime-matrix-bpn-pdec-real-constraint-rows.json` 的 `phase_cap_t` 属于该来源，但当前只覆盖
`P=23,Q=210` 的有限样本。它不能直接替代 `Q=2310` 的 `M(t)`。

### 3.2 资源不可复用来源

**Lemma H4-LHB-M3（资源注入上界）。**
若对每个相位 `t` 都构造了资源集合 `R_t` 和映射

\[
\iota_t:S_t\to R_t
\]

且 `iota_t` 单射，则

\[
g(t)=|S_t|\le |R_t|.
\]

**证明。**
单射不能增加基数。证毕。

该来源可以承载三种既有刚性：

```text
window non-reuse：同一短窗容量资源不可被多个坏窗重复占用；
tail-anchor non-reuse：同一尾锚或同一尾标签不能在剩余分支中无限复用；
column witness displacement：同列素数见证的非零位移资源不能被同一缺陷重复吞并。
```

只要资源单射被逐行证明，相应 `M(t)=|R_t|` 就是可审计容量界。

### 3.3 条件路由来源

**Lemma H4-LHB-M4（路由后剩余分支多重度界）。**
设当前证明树已经排除了出口 `E`。若已证明

\[
g(t)>M_E(t)\quad\Longrightarrow\quad E,
\]

则在“非 `E`”剩余分支中有

\[
g(t)\le M_E(t).
\]

**证明。**
反证即得：若非 `E` 分支中存在 `g(t)>M_E(t)`，则由路由定理推出 `E`，矛盾。证毕。

该来源适合把 `ColumnRadiusDefect`、`ColumnCRTDefect`、`TailAnchorDefect` 这类出口剥离后，
留下真正可进入当前分支的容量行。

## 4. 组合规则

若同一相位有多个同时有效的上界 `M_1(t),...,M_r(t)`，则可取

\[
M(t)=\min_i M_i(t).
\]

若 `S` 被互不相交地分解为 `S=S^{(1)}\sqcup\cdots\sqcup S^{(r)}`，且
`g_i(t)<=M_i(t)`，则

\[
g(t)=\sum_i g_i(t)\le \sum_i M_i(t).
\]

这两条规则分别对应“同一坏窗族的多重约束取最强界”和“分支拆分后容量相加”。

## 5. `WHOLEDEF/BRIDGED` 升级合同

对 `h4-pdec-lhb-column-phase-blocks.json` 中每一条 `WHOLEDEF/BRIDGED` 支撑行，若已经物化
同一 `p,Q,S,tau` 下的 `M(t)`，则生成正式容量行：

```text
row_id: CC-LHB-WHOLEDEF-MULT-Q2310-P{p}
phase_block: 原 WHOLEDEF phase_block
bound: sum(M[t] for t in phase_block)
inequality: sum_{t in phase_block} g(t) <= bound
source_type: MultiplicityCap
admissibility: A-ready-after-M-vector
proof_ref: h4-pdec-lhb-multiplicity-cap-route.md + M(t) 来源文件
```

`BRIDGED` 行同理。注意这里的 `bound` 是 `sum_C M(t)`，不是 `phase_block_size`。

## 6. 当前可审查结论

当前仓库已经完成：

```text
Q=2310 的 WHOLEDEF/BRIDGED 支撑相位块；
空异常块 AFFINE/NEGDELTA/UNBRIDGED 的 bound=0 容量行；
T3 多重度容量的正式引理与准入合同。
```

当前尚未完成：

```text
Q=2310 的 M(t) 数组；
每个 M(t) 的来源证明或有限全集投影证书；
把 WHOLEDEF/BRIDGED 输出为 A-ready-after-M-vector 行。
```

因此本轮推进把缺口从“支撑能否当容量”压缩为唯一可核验任务：

\[
\boxed{\text{物化并证明同一 }(p,Q,S,\tau)\text{ 下的 }M(t).}
}
\]

## 7. 下一步最小硬点

下一步应优先生成 `Q=2310` 的 `M(t)` 输入包。推荐顺序：

1. **有限全集路线。** 定义 `Z_LHB(p,Q)`，证明 `S subset Z_LHB`，并枚举 `M_Z(t)`；
2. **资源不可复用路线。** 对尾锚、列位移、短窗资源分别构造单射，取 `min` 或分支相加；
3. **条件路由路线。** 先剥离 `ColumnRadius/ColumnCRT/TailAnchor` 出口，再在剩余分支给出 `M_E(t)`。

只有上述任一路线完成后，`WHOLEDEF/BRIDGED` 才能从诊断支撑升级为正式容量行。
