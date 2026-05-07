# Multiplicity-Stitching 吸收合同：口径不一致不是数学出口

**状态：** `multiplicity_stitching_absorbed_to_weighted_pdec_or_quotient_not_closed`

本文承接 `prime-matrix-newlayer-pdec-tower-entropy-contract.md`。当前终端列表中仍有
`Multiplicity-Stitching`。它不是新的覆盖机制，而是证书口径一致性义务：

```text
PDEC 下界、PDEC 上界、Column/SAE 约束必须作用于同一个 formal unit。
```

本文把该义务全局化：任何多重/拼接问题只有三类合法归宿。

```text
1. WeightedDualIndependence  => 加权 PDEC；
2. CoordinateQuotient        => primitive/physical PDEC 或 CleanKLS；
3. ReuseDefect               => ColumnCRT / SAE / TailAnchor。
```

因此 `Multiplicity-Stitching` 不能作为第五类终端出口保留。

## 1. Formal unit 原则

一个终端证书必须先固定 formal unit：

```text
Omega      : 坏窗索引域；
tau        : Omega -> G 的签名映射；
w(omega)  : 权重或重数；
g(a)       : sum_{omega:tau(omega)=a} w(omega)。
```

下界使用的 `g`、对偶上界约束 `Ag<=b, Eg=e`、以及 `SAE/ColumnCRT` 回流，都必须使用同一个
`Omega,tau,w`。若不能同时定义这三者，则该聚合只是诊断库信号，不能作为正式 PDEC 证书。

## 2. 三归宿

### 2.1 WeightedDualIndependence

若重复项来自不同 Hall 块、不同约束行或不同合法坏窗，则允许使用多重集合。但必须给出：

```text
w(omega) 的定义；
每个重复项对应的独立约束行；
对偶上界也按同一 w 计量；
不会把同一物理补洞能力重复使用。
```

此时 `Multiplicity-Stitching` 被吸收为：

```text
weighted PDEC-Cert。
```

### 2.2 CoordinateQuotient

若两个事件在正式坐标上相同，例如

```text
(q,row,candidate_row,column,offset,n,ell,rho)
```

完全一致，且没有加权对偶独立证明，则必须商掉重复标签。记 quotient map 为

```text
pi: Omega -> Omega_bar。
```

正式计数变成

```text
g_bar(a)=#{bar_omega: tau_bar(bar_omega)=a}。
```

此时强阈值可能下降，但口径合法。后续只有两种归宿：

```text
primitive/physical PDEC-Cert；
或 quotient 后低维峰消失，进入 CleanKLS/DLS。
```

### 2.3 ReuseDefect

若同一物理候选、同一列位移、同一端点 seam 或同一尾因子在多个层中复用，但这些层不能拼成同一
formal unit，则复用本身是结构缺陷：

```text
同一列位移多次出现      => ColumnCRT；
同一端点/短窗孤立复用    => SAE/Endpoint；
同一尾锚/互补因子复用    => TailAnchor / CofactorAnchor；
跨层持久复用             => PDEC on reuse signature。
```

因此无法拼接并不产生自由逃逸；它把重复项改写为复用缺陷。

## 3. 对 FO-PDEC 个案的抽象吸收

`FO-PDEC` 中 `ell=199,h=95` 的强信号来自：

```text
global_library_raw mass=4；
physical mass=2；
single formal unit best Fourier=1。
```

按本合同：

```text
嵌套同坐标重复
  => WeightedHallDualIndependence
     or CoordinateQuotient；

跨 q 同整数复用
  => Cross-q persistence weighted PDEC
     or ReuseDefect。
```

因此 `3.959...` 可以继续作为诊断信号，但只有在加权独立/拼接定理补齐后才能作为正式阈值。
若补不齐，就必须改用 quotient/primitive 口径，并把重复复用送入 `ColumnCRT/SAE/TailAnchor`。

## 4. 形式化无循环

定义口径势函数：

```text
Psi_MS=(
  formal_unit_status,
  duplicate_count,
  cross_layer_reuse_count,
  weight_rank,
  quotient_mass,
  reuse_defect_count
)。
```

每次处理 `Multiplicity-Stitching` 只能：

```text
证明新的独立权重行       => weight_rank 增加，进入 weighted PDEC；
商掉重复坐标             => duplicate_count 或 quotient_mass 下降；
抽取复用缺陷             => reuse_defect_count 增加并进入 ColumnCRT/SAE/TailAnchor/PDEC；
发现口径仍不一致         => 输出更小 formal unit 义务。
```

由于重复项和跨层复用项来自有限证书对象，固定层内该过程有限终止；若跨无限层复用，则回到
`new-layer PDEC tower entropy contract`，不是新的同层循环。

## 5. 结论

**Multiplicity-Stitching Absorption.**
任意终端证书中的口径不一致事件，有限步内必进入：

```text
weighted PDEC-Cert；
primitive/physical PDEC-Cert；
CleanKLS/DLS；
ColumnCRT；
SAE/Endpoint；
TailAnchor/CofactorAnchor；
new-layer tower entropy branch。
```

所以 `Multiplicity-Stitching` 从终端出口列表中删除；它只是证书对象规范化步骤。

## 6. 当前闭合边界

本文完成：

```text
Multiplicity-Stitching 不是独立数学出口；
它必须吸收到加权 PDEC、商后 PDEC/CleanKLS、或复用缺陷。
```

本文未完成：

```text
WeightedHallDualIndependence 的实际证明；
primitive/physical PDEC 的全部 U_CRT<L_PDEC；
ColumnCRT/SAE/TailAnchor 的终端排斥。
```

因此最终终端列表更新为：

```text
explicit/profinite/weighted/primitive PDEC；
ColumnCRT；
SAE；
CleanKLS/DLS；
TailAnchor/CofactorAnchor。
```

这仍是结构闭合推进，不是最终无条件行命题证明。

## 7. TailAnchor/CofactorAnchor 吸收

新增 `prime-matrix-tailanchor-cofactor-absorption-contract.md` 后，`TailAnchor/CofactorAnchor`
也不再作为终端列表保留。远尾互补因子反演给出签名：

```text
m/y band, m mod Q, q mod Q, d mod Q/P。
```

若某个锚签名持久承担正超额，则进入 `cofactor PDEC / low-mod PDEC / ColumnCRT`；
若锚只孤立出现，则进入 `SAE-anchor`；若无锚同步且总正部不足，则容量矛盾或 `CleanKLS/DLS`。
