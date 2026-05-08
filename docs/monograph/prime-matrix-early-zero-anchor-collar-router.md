# Prime Matrix 早期零行 canonical anchor collar 路由器

**状态：** `canonical_anchor_collar_closed_prime_fiber_capacity_open`

本步把真双素 carry-shell 再压窄：取最小高素因子后，anchor `q` 不在整个 `(x,P)`，而只能在 `x<q<sqrt((x+1)P)` 的 canonical collar 中；固定 q 后，cofactor `m` 只来自长度 `<P/q<=sqrt(P)` 的短素数纤维。剩余变成 anchor-collar 短素数纤维容量，或过载时的 PDEC/SAE/ColumnCRT 回流。

```text
canonical_anchor_collar_closed=true
fiber_short_interval_reduction_closed=true
anchor_collar_prime_fiber_capacity_closed=false
row_column_unconditional_closed=false
```

## 1. Canonical anchor collar

在 `x>=sqrt(P)` 分支，任一高补洞点都是

```text
xP+c = q m,   x<q,m<P,   q,m prime.
```

取 `q` 为最小高素因子，则 `q<=m`，所以

```text
q^2 <= xP+c < (x+1)P.
```

因此

```text
x < q < sqrt((x+1)P).
```

这把原先的高素选择区间 `(x,P)` 压成 canonical anchor collar。用 `q=P-a` 表示时，
它等价于在 carry-shell 中只取 `q<=m` 的半边，并且平方点只计一次。

## 2. q-fiber 短素数窗口

固定 collar 中的 `q` 后，`m` 必须满足

```text
ceil((xP+1)/q) <= m <= floor((xP+P-1)/q),
m prime,  q<=m<P.
```

该窗口长度严格小于 `P/q`，而 `q>x>=sqrt(P)`，故每条 q-fiber 长度 `<sqrt(P)`。
所以全覆盖不能再说成“高素很多”，而必须说成许多极短素数纤维同时满载。

## 3. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `PrimePairBranchImported` | `true` | `true` | 上一轮已把 x>=sqrt(P) 分支化为真双素 carry-shell 容量问题。 | `继续规范化 q anchor。` |
| `CarryShellIdentityImported` | `true` | `true` | 已有 h=a+b-floor(ab/P), c=ab mod P 的带进位壳恒等式。 | `可在壳上取 canonical anchor。` |
| `CanonicalLeastAnchorCollar` | `true` | `true` | 取 q 为 xP+c 的最小高素因子，则 q<=sqrt(xP+c)<sqrt((x+1)P)。 | `x<q<sqrt((x+1)P)，高素 anchor 只在窄 collar 内。` |
| `PairDuplicationQuotiented` | `true` | `true` | canonical q<=m 删除 q,m 互换重复；平方点只计一次。 | `primitive physical atom 口径更窄。` |
| `FiberShortPrimeInterval` | `true` | `true` | 固定 q 后，m 必须是长度 <P/q<=sqrt(P) 的短区间内素数。 | `q-fiber capacity replaces unconstrained high-prime coverage。` |
| `SampleAnchorAudit` | `true` | `false` | 样本中所有 canonical anchors 均落入 collar；审计只复核实现口径。 | `canonical_anchor_collar_sample_verified_capacity_open` |
| `NamedReturnCompatibility` | `true` | `true` | 若少数 q-fiber 持久过载则进入 PDEC；孤立短窗进入 SAE；固定列位移进入 ColumnCRT。 | `AnchorCollarPDECSAEColumnReturn。` |
| `AnchorCollarPrimeFiberCapacity` | `false` | `false` | 尚未证明所有 collar q-fiber 的短素数容量总和不能覆盖 R_x。 | `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn。` |

## 4. 样本审计

样本仅用于复核 canonical anchor 实现；collar 结论由 `q^2<=xP+c` 直接证明。

```text
sample_status=canonical_anchor_collar_sample_verified_capacity_open
all_anchor_hits_in_collar=true
```

| P | rows | max anchor width | max fiber load | max primepair share | min prime holes |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 101 | 91 | 26 | 2 | 0.500000 | 7 |
| 499 | 477 | 125 | 4 | 0.420290 | 29 |
| 997 | 966 | 250 | 5 | 0.413333 | 54 |

## 5. 新最窄剩余

本步把 `PrimePairCarryShellCapacityBoundOrPDECReturn` 压成：

```text
AnchorCollarPrimeFiberCapacityBoundOrPDECReturn
  = AnchorCollarShortPrimeFiberUpperBound
    AND NoPersistentAnchorFiberConcentrationPDEC
    AND NoSparseAnchorFiberSAE
    AND NoColumnDisplacementReuseInAnchorFibers.
```

真正未闭合的是第一项：需要证明 collar 中所有短素数纤维的容量总和不能吃掉整个 `R_x`；
若某些纤维承担异常大负载，则已经进入 PDEC/SAE/ColumnCRT 命名回流，而不是新的出口。
