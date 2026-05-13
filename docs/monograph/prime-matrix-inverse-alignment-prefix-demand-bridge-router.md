# Prime Matrix 逆元对齐到 Prefix Demand 桥接路由器

**状态：** `inverse_alignment_zero_row_position_synced_to_prefix_demand_numeric_lower_bound_open`

逆元对齐系统可以直接并入当前前沿：假设早期零行存在时，行号 `x` 本身给出相位向量 `rho_q(x)=-xP mod q`；`R_{x,z}` 正是未被 `q<=z` 命中的列，`tau_z(c)` 是最小的 `q>z` 覆盖标签，`mu_q` 与现有容量乘子公式完全一致。因此你的同余方程组不是旁路，而是 `M#_{x,z}` 需求项的具体行号模型。但它仍不自动给出 `|R_{x,z}|` 的全局下界；若取自然 cutoff 试图证明 `min x>P`，硬点等价转为短区间素数输入。

```text
inverse_alignment_prefix_demand_bridge_closed=true
capacity_and_forced_load_compatibility_closed=true
normalized_prefix_potential_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 桥接结论

| name | statement | status |
| --- | --- | --- |
| `zero_row_position_equals_alignment_solution` | 行 x 是零行 iff every c in [1,P-1] is covered by some inverse class q<P. | `closed` |
| `phase_vector_source` | the vector rho_q(x)=-xP mod q gives the row-position source for all prefix labels. | `closed` |
| `prefix_atom_selector` | R_{x,z} is exactly the set of columns not hit by q<=z; tau_z(c) is the least q>z hitting c. | `closed` |
| `capacity_multiplier_match` | mu_q(x;P)=#{1<=c<P:c=rho_q(x) mod q}, matching the existing capacity discipline. | `closed` |
| `numeric_lower_bound_boundary` | the bridge does not prove \|R_{x,z}\| lower bounds; it routes them to sieve or short-prime-gap input. | `open_boundary` |

## 2. 样本 M# 字段

| P | x | z | zero row | |R_xz| | all labeled | M# exact |
| ---: | ---: | ---: | --- | ---: | --- | ---: |
| 13 | 168 | 3 | `true` | 4 | `true` | 2.666667 |
| 13 | 168 | 5 | `true` | 2 | `true` | 2.000000 |
| 13 | 168 | 7 | `true` | 1 | `true` | 1.000000 |
| 23 | 58 | 5 | `true` | 5 | `true` | 3.166667 |
| 23 | 58 | 7 | `true` | 3 | `true` | 2.500000 |
| 23 | 58 | 11 | `true` | 3 | `true` | 2.500000 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `InverseAlignmentImportedAsZeroRowPosition` | `true` | `true` | 零行 x 与全 r 逆元覆盖对齐严格等价，x 是实际行号源，不是后验抽象标签。 | none for row-position interface |
| `PrefixDemandBridgeClosed` | `true` | `true` | 逆元相位向量直接生成 R_{x,z}、tau_z(c)、mu_q 和 M# 字段。 | numeric lower bound still open |
| `CapacityAndForcedLoadCompatibilityClosed` | `true` | `true` | 新行号相位源与既有容量乘子、prefix 转移、强制负载守恒链条完全同字段匹配。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `MinXGreaterThanPClosedByAlignment` | `false` | `false` | 逆元系统本身仍不能证明全局 min x>P；该断言需要短区间素数输入。 | PrimeGapBelowP2ForAllPBlocks |
| `NormalizedPrefixPotentialProved` | `false` | `false` | R_{x,z} 的字段来源已更具体，但 \|R_{x,z}\| 统一下界仍需 beta-sieve/有限证书或短区间素数路线。 | NormalizedPrefixResidualPotentialLowerBound |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步加强了反例链源字段和非循环性，不产生最终无条件矛盾。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步

- 主攻：`NormalizedPrefixResidualPotentialLowerBound`。
- 备选闭合口：`PrimeGapBelowP2ForAllPBlocks`。
- 边界：本步只关闭逆元行号源到 M# 字段的桥接，不证明全局 |R_xz| 下界。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-prefix-demand-bridge-sample-ledger.json` | `eec72f9e3ef05087319a0ae53ce8fcf87638dd034adb488606096152d0c42055` |
| `docs/monograph/prime-matrix-inverse-alignment-covering-system-router.json` | `09be6a101dd2775a057577a1ef960270dbd88b03dd5e5cec4d1bddec67eb1acf` |
| `docs/monograph/prime-matrix-strict-normalized-prefix-potential-router.json` | `4f86ea29ee34a43e365527b3c6e030050418f872c893c8ba470d8997ed66d6da` |
| `docs/monograph/prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json` | `10d4d7aab7648367047e86acd7069d1986730a138b8c74e4d8a8269378119e65` |
| `docs/monograph/prime-matrix-strict-prefix-residual-transfer-router.json` | `e881be563d60841cab6d45ca64a55ee745691b9476ba79be3a3decab58038cad` |
| `docs/monograph/prime-matrix-strict-sparse-budget-after-unified-sync-router.json` | `70ca92ae2e350fdeba4eb1d386a9c31835da97f91a7252e3d0fee445a0e79f08` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json` | `3fabe3f3825c980842551045d9ca8714df0b3bb6fd1b92e39ba5e7e70daea1af` |
| `experiments/prime_matrix_inverse_alignment_prefix_demand_bridge_router.py` | `60f2fe44135706e0be6735c72514e3ac26a220fa7c7dc52edca728480a21510b` |
