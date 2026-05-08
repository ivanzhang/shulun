# Prime Matrix anchor-collar 幸存者恒等分解路由器

**状态：** `anchor_collar_capacity_reduced_to_prime_survivor_or_named_defect`

本步把 anchor-collar 短纤维容量硬点做成无损恒等式：`R_x` 精确等于素数幸存列与 canonical 双素纤维的并。因此“短纤维不能覆盖全部 R_x”等价于“该 P 对齐短区间至少有一个素数幸存”。这不是终局证明，但它排除了继续把纤维容量当作更弱纯计数问题的退路；下一步必须证明变量行一维粗骨架和二维素对纤维的维数差，或把素数幸存为零送入 PDEC/SAE/ColumnCRT。

```text
anchor_collar_survivor_identity_closed=true
capacity_gap_equals_prime_survivors_closed=true
anchor_collar_short_fiber_capacity_closed=false
row_column_unconditional_closed=false
terminal_gap_after_router=PrimeSurvivorLowerBoundOrPDECSAEColumnReturn
```

## 1. 精确分解

固定奇素数 `P` 与 `sqrt(P)<=x<P`。令 `R_x` 为第 `x` 行中没有 `<=x` 素因子的列：

```text
R_x={1<=c<P: P^-(xP+c)>x or xP+c is prime}.
```

因为 `xP+c<(x+1)P<=P^2`，任一 `c in R_x` 只有两种可能：

```text
xP+c is prime;
xP+c=q m,  x<q<=m<P,  q,m prime.
```

第二种正是上一轮 canonical anchor collar 的短纤维支撑。因此有无损恒等式：

```text
R_x = PrimeSurvivors_x disjoint_union SemiprimeFibers_x
|R_x|-|SemiprimeFibers_x| = |PrimeSurvivors_x|.
```

所以在 `x>=sqrt(P)` 分支，早期零行等价于 `PrimeSurvivors_x=empty`。

## 2. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `AnchorCollarImported` | `true` | `true` | 上一轮已证明 x>=sqrt(P) 的高补洞只能来自 canonical anchor collar。 | `可对 R_x 做无损分解。` |
| `RoughPrimeSemiprimePartition` | `true` | `true` | 若 x>=sqrt(P)，n<xP+P<P^2 且没有 <=x 因子，则 n 只能是素数或两个 >x 素数的乘积。 | `R_x = PrimeSurvivors_x disjoint_union SemiprimeFibers_x。` |
| `FiberSupportEqualsSemiprimeSet` | `true` | `true` | canonical q-fiber 恰好枚举上述双素乘积列；q,m 互换只计一次。 | `短纤维容量不是外估计，而是 SemiprimeFibers_x 的精确支撑。` |
| `CapacityGapEqualsPrimeSurvivors` | `true` | `true` | \|R_x\|-\|canonical fibers\| = PrimeSurvivors_x。 | `AnchorCollarShortPrimeFiberUpperBound 等价于 PrimeSurvivors_x>0。` |
| `EarlyZeroEquivalentPrimeFreeIntervalLargeBranch` | `true` | `true` | 在 x>=sqrt(P) 分支，早期零行等价于该 P 对齐短区间没有素数幸存者。 | `不能再把短纤维容量当作比 EDA 更弱的纯计数问题。` |
| `EDABarrierCompatibility` | `true` | `true` | 该分解与已有 EDA-Gap Barrier 一致：自足闭合仍需要 CRT 对偶下界或缺陷回流。 | `AnchorCollarPrimeSurvivorLowerBoundOrDefectReturn。` |
| `DimensionGapRouteCompatibility` | `true` | `true` | 可用的非循环攻法是证明一维粗骨架下界大于二维素对纤维上界，或失败进入 PDEC/Tail-anchor。 | `VariableRowRoughSkeletonVsPrimePairFiberDimensionGap。` |
| `UnconditionalPrimeSurvivorLowerBound` | `false` | `false` | 尚未证明所有 sqrt(P)<=x<P 均有 PrimeSurvivors_x>0。 | `PrimeSurvivorLowerBoundOrPDECSAEColumnReturn。` |

## 3. 样本审计

样本只验证实现口径；上面的分解由唯一分解和 `x>=sqrt(P)` 直接证明。

```text
sample_status=anchor_collar_survivor_identity_sample_verified
all_identity_holds=true
all_sqrt_gate_clean=true
all_anchor_collar_clean=true
```

| P | rows | min prime survivors | max semiprime share | max fiber load | min rough logx/P | max semiprime logP/P |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 101 | 91 | 7 | 0.500000 | 2 | 0.339838 | 0.411248 |
| 499 | 477 | 29 | 0.420290 | 4 | 0.342400 | 0.410854 |
| 997 | 966 | 54 | 0.413333 | 5 | 0.376230 | 0.429383 |
| 1999 | 1955 | 110 | 0.401408 | 7 | 0.418655 | 0.433440 |

最弱素数幸存行示例：

| P | x | rough | semiprime fibers | prime survivors | semiprime share |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 101 | 73 | 8 | 1 | 7 | 0.125000 |
| 499 | 362 | 29 | 0 | 29 | 0.000000 |
| 997 | 916 | 55 | 1 | 54 | 0.018182 |
| 1999 | 1881 | 111 | 1 | 110 | 0.009009 |

## 4. 结构结论

本步说明：

```text
AnchorCollarShortPrimeFiberUpperBound
  <=> PrimeSurvivors_x>0 on every sqrt(P)<=x<P row.
```

因此继续直接数 q-fiber 总容量不会绕开短区间素数屏障。可继续硬攻的非循环方向是变量行维数差：

```text
G_x(P)=#R_x                       一维粗骨架
B_x(P)=#SemiprimeFibers_x          二维素对纤维
PrimeSurvivors_x=G_x(P)-B_x(P).
```

若能证明 `G_x(P)>B_x(P)`，则该行闭合；若失败，则失败必须表现为低模骨架亏损、素对纤维过密、
孤立幸存者逃逸或固定列位移复用，并分别回流 `PDEC/SAE/ColumnCRT`。

## 5. 新最窄剩余

```text
PrimeSurvivorLowerBoundOrPDECSAEColumnReturn
  = VariableRowRoughSkeletonLowerBound
    AND VariableRowPrimePairFiberUpperBound
    AND PrimeFreeIntervalLowModPDECDefectReturn
    AND SparsePrimeSurvivorOrLocalSAEExclusion
    AND ColumnDisplacementReusePDECReturn.
```

这一步不是终局闭合；它把 anchor-collar 的容量语言压成了精确的素数幸存/维数差语言。
