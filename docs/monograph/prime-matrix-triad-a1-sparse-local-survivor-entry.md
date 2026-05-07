# Triad-A1 Sparse 到 LocalSurvivor 的入口合同

**状态：** `sparse_terminal_reduced_to_local_survivor_or_pdec`

本文承接 `Triad-A1 终端无循环账本`。当前已物化层仍在 `FiberDeletion`，若无限塔删除势发散，则支撑密度趋零。本文把这个终端从“Sparse”继续压缩为：

```text
Sparse
=> LocalSurvivorCert
   or persistent sparse pattern => PDEC
   or descent/seam => LocalSurvivor/PDEC。
```

所以 `Sparse` 不是第四类终端，而是 `LocalSurvivor/PDEC` 的入口。

## 1. 稀疏支撑对象

沿升层塔：

```text
Q_0 < Q_1 < Q_2 < ...
```

令 `A_n` 是第 `n` 层允许坏窗相位支撑，平均 fiber 幸存率为 `a_n`。已有删除势账本给出：

```text
density(A_N)=density(A_0)*prod_{n<N} a_n。
```

若：

```text
sum -log(a_n)=infinity，
```

则：

```text
density(A_N)->0。
```

这就是 Sparse 入口。

## 2. Sparse 二分

考虑一个最小早期零行反例族。如果 `A_N` 密度趋零，但仍要支撑坏窗覆盖，则只有两种结构形态：

```text
IsolatedSparse:
  坏窗只落在有限/短尺度孤立 cylinder 或局部窗口中；

PersistentSparse:
  虽然全局密度趋零，但某个签名、列位移、端点、尾锚或低模模式在无限反例族中重复出现。
```

第一种就是 `LocalSurvivorCert` 的输入。第二种由鸽巢抽取稳定签名，回到 `PDEC family`。

## 3. LocalSurvivorCert 输入格式

一个 Sparse 局部证书必须登记：

```text
window_id；
candidate set C(I)；
blocker families B_low, B_tail, B_col, B_endpoint, B_core；
projection rule blocker -> candidates；
cover_count(c)；
witness c0 with cover_count(c0)=0
or blocker deficit |union B_j|<|C(I)|。
```

若给出 witness，则该窗口存在未覆盖候选，早期零行失败。

若 blocker 覆盖全部候选，则取最小 blocker 族并分类：

```text
低模 blocker 持久       => low-mod PDEC；
尾锚/互补因子 blocker  => TailAnchor/Cofactor PDEC；
列位移 blocker          => ColumnCRT/PDEC；
端点或 seam blocker     => endpoint PDEC 或更小 SAE；
只在局部出现            => 缩小候选集，递归 LocalSurvivor。
```

固定窗口候选集有限，所以缩小候选集不能无限循环。若同类局部窗口沿反例族无限复现，则转为 persistent signature，回到 PDEC。

## 4. 与当前 A1 删除势的拼接

当前 A1 物化层给出：

```text
2310->30030 min density drop 3.19672；
30030->510510 min density drop 6.13889；
```

且 HRO/TCP/TUD 已证明中间逃逸只能转入 PDEC/CleanKLS。于是删除势分支的终端形态为：

```text
删除势继续发散:
  density(A_N)->0
  => SparseLocal；

SparseLocal 失败:
  blocker 持久 => PDEC；
  blocker 非持久 => 更小 LocalSurvivor；

删除势不发散:
  NoDeletion
  => KL/PDEC 或 CleanKLS。
```

这使 A1 的三终端进一步收紧为：

```text
PDEC；
CleanKLS/DLS；
LocalSurvivorCert。
```

## 5. 当前未闭合项

本文完成的是入口合同，不是所有局部窗口的 witness 证书。仍需提交：

```text
LS-1. 从具体 Sparse cylinder 抽取 C(I) 与 blocker families；
LS-2. 对每个窗口给出 witness 或 blocker deficit；
LS-3. 若 blocker 覆盖全局化，转成同一 formal unit 的 PDEC 证书。
```

当前最小可执行目标是：把 A1 删除势发散后出现的最小 sparse cylinder，转换为 `LocalSurvivorCert(I)` 的机器可读输入。
