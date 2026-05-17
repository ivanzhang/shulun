# Prime Matrix formal-to-actual cutset completeness lemma

**状态：** `deterministic_cutset_partition_closed_exit_exclusion_open`

本文把 `GlobalFormalToActualCutsetPromotion` 中不依赖有限扫描的部分单独闭合：任意 AffineTwin formal pair 一旦按 actual-load 管道解释，必然落入一个命名出口。剩余不是分类问题，而是这些出口的全局排斥或可求和吸收。

## 1. 对象

固定 AffineTwin 候选 `q>=13`。令

```text
F_q = G_q x H_q
```

为形式侧 generator/fill residue 笛卡尔积。对 `a=(g,h) in F_q` 依次检查：

1. `Source_q(a)`: 是否存在 matching gap-fill source，满足 `gap=q`、`generator=q-2`、`fill=q`、方向、`p_delay=(11q-21)/4` 与 slot-lock key。
2. `CRT_q(a)`: source 物化后，合成 CRT class modulo `q(q-2)` 是否在 primitive pair support 中有代表。
3. `Primitive_q(a)`: CRT 命中后，是否保持 primitive depth identities、非复用投影、非 repeated-residue/reset、非 ColumnCRT/PDEC。

## 2. 完备分割

定义四个互斥集合：

```text
S_q = {a in F_q : Source_q(a) fails}
C_q = {a in F_q : Source_q(a) holds and CRT_q(a) fails}
P_q = {a in F_q : Source_q(a), CRT_q(a), Primitive_q(a) all hold}
E_q = F_q \ (S_q union C_q union P_q)
```

则

```text
F_q = S_q disjoint_union C_q disjoint_union P_q disjoint_union E_q.
```

解释为：

```text
S_q -> SourceMaterializationFailure-PDEC/SAE
C_q -> CRTWindowEmpty / WindowEdgeCollision / SupportMotion exits
P_q -> actual primitive-supported packet
E_q -> ProjectionCollision/ColumnCRT/PDEC or PrimitiveTwinSlotSupportEscape-PDEC/SAE
```

因此全局 product accounting 的确定性恒等式是

\[
M_q^{form}=|F_q|=|S_q|+|C_q|+|P_q|+|E_q|,
\qquad
N_q=|P_q|.
\]

`M_q^{form}-N_q` 不能作为隐藏 actual load 使用；它必须由 `S_q`、`C_q`、`E_q` 三类命名出口承担。

## 3. 证明

对任意 `a in F_q` 作有序门控：

1. 若 `Source_q(a)` 失败，则 `a in S_q`。
2. 若 source 通过但 `CRT_q(a)` 失败，则 `a in C_q`。
3. 若 source 与 CRT 都通过且 `Primitive_q(a)` 通过，则 `a in P_q`。
4. 剩余情形必然是 source 与 CRT 均通过但 primitive actual 条件失败，所以 `a in E_q`。

四步由第一个失败门确定，故互斥；四步覆盖全部 `F_q`，故完备。

## 4. 与 current sweep 的连接

当前 cutset 证书只是该完备分割在当前数据上的实例：

```text
|F|=40
|P|=1
|C|=11
|S|=28
|E|=0 current unresolved
```

其中 `C` 的当前最小相位距离为 `40`，主 CRT 模数为 `899`，支撑宽度为 `20`。

## 5. 剩余硬点

本引理关闭的是分类完备性，不关闭行/列命题。全局剩余变成：

```text
SourceMaterializationFailure-PDEC/SAE exclusion or summability
CRTWindowEmptyGlobalSupportBound / WindowEdgeCollision / SupportMotion exits
ProjectionCollision/ColumnCRT/PDEC exclusion
PrimitiveTwinSlotSupportEscape-PDEC/SAE exclusion or summability
Endpoint/reset, transport reset, epoch-pair multiplicity, moving-residue SAE/Rankin
```

下一主攻点：

```text
NamedExitExclusionOrSummabilityAfterCutsetCompleteness
```
