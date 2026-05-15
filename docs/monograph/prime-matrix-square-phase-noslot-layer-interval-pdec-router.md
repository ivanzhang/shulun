# Prime Matrix square-phase no-slot layer interval PDEC router

**状态：** `noslot_floor_layer_bound_reduced_to_moving_layer_prime_load_open`

本步把 `NoSlotFloorLayerBandBoundOrLayerPDEC` 进一步原子化。固定 `P`、方向和 floor layer `k` 后，无槽支撑在 `b` 轴上是一个整数区间；无槽尾素数正是这些区间里线性型 `q=P-2b` 取素的 prime-load 总和。若无槽分支达到 `PrimeWindow/2`，则某个 moving layer interval 必有鸽巢强制的高 prime-load。这不是全局闭合；剩余是证明所有 moving layer prime-load 上界，或把持久高负载登记并排斥为 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
atom_decomposition_failure_count=0
monotone_failure_count=0
finite_large_branch_count=0
row_column_unconditional_closed=false
```

## 1. 层区间原子

固定 `P,side,k` 后，`b` 必须同时满足 floor-layer 条件和对应端带条件。由于相应二次函数在 `b>0` 上严格递增，支撑只能是一个整数区间：

```text
2b^2 = k(P-2b)+s, 0<=s<P-2b.
plus:  s < P-2b-(P-1)/2
minus: s > (P-1)/2.
```

无槽尾素数于是变成这些区间里 `P-2b` 为素数的负载和。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| plus PrimeWindow | 97145 |
| minus PrimeWindow | 97396 |
| plus no-slot load | 18299 |
| minus no-slot load | 15895 |
| plus atom count | 35777 |
| minus atom count | 35476 |
| max plus atom load | 11 |
| max minus atom load | 7 |

## 3. 最大原子

| side | P | k | b interval | length | prime load | sample q |
| --- | ---: | ---: | --- | ---: | ---: | --- |
| plus | 4273 | 0 | [1,32] | 32 | 11 | `[4271, 4261, 4259, 4253, 4243, 4241, 4231, 4229]` |
| minus | 4733 | 0 | [35,48] | 14 | 7 | `[4663, 4657, 4651, 4649, 4643, 4639, 4637]` |

## 4. 样本表

| P | plus prime | plus no-slot | plus atoms | plus max load | minus prime | minus no-slot | minus atoms | minus max load |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 3 | 1 | 1 | 1 | 3 | 0 | 0 | 0 |
| 17 | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 19 | 3 | 1 | 1 | 1 | 4 | 0 | 0 | 0 |
| 23 | 2 | 0 | 1 | 0 | 3 | 0 | 0 | 0 |
| 29 | 4 | 0 | 1 | 0 | 5 | 0 | 0 | 0 |
| 31 | 5 | 1 | 1 | 1 | 4 | 0 | 1 | 0 |
| 101 | 11 | 1 | 2 | 1 | 12 | 2 | 2 | 1 |
| 499 | 40 | 9 | 9 | 3 | 44 | 6 | 12 | 2 |
| 1009 | 72 | 17 | 25 | 3 | 70 | 9 | 20 | 3 |
| 2003 | 125 | 28 | 42 | 6 | 139 | 18 | 46 | 2 |
| 4999 | 300 | 58 | 117 | 11 | 289 | 46 | 117 | 3 |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `layer_interval_atomization` | `closed` | For fixed P, side, and floor layer k, the no-slot b-support is one integer interval. |
| `noslot_prime_load_identity` | `closed` | NoSlotTailPrime^side(P) is the sum of prime loads of q=P-2b over those layer intervals. |
| `large_branch_forces_layer_atom` | `closed` | If NoSlotTailPrime^side(P)>=PrimeWindow^side(P)/2, one layer interval atom has load at least the pigeonhole quotient. |
| `moving_layer_prime_load_bound` | `open` | A global proof needs a prime-load bound for q=P-2b in every moving layer interval, or a PDEC/SAE exclusion. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LayerIntervalAtomizationClosed` | `true` | `true` | 固定 k 的无槽支撑是单一区间原子。 | closed |
| `NoSlotPrimeLoadIdentityClosed` | `true` | `true` | 无槽尾素数等于层区间内 q=P-2b 取素的负载和。 | closed |
| `LargeBranchForcesAtomClosed` | `true` | `true` | 大无槽分支会强制至少一个层区间原子出现高 prime-load。 | closed |
| `FiniteNoLargeNoSlotBranch` | `true` | `false` | 有限扫描 P<=5000 没有大无槽分支。 | finite evidence only |
| `GlobalMovingLayerPrimeLoadBound` | `false` | `false` | 仍需全局排斥 moving layer interval 中 q=P-2b 的高素数负载。 | NoSlotLayerPrimeLoadBoundOrMovingLayerPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只登记层区间原子，不关闭全局行/列命题。 | NoSlotLayerPrimeLoadBoundOrMovingLayerPDEC |

## 7. 下一步

- 主攻：`NoSlotLayerPrimeLoadBoundOrMovingLayerPDEC`。
- 该目标必须处理 moving layer interval 中 `q=P-2b` 的素数负载；本步没有用有限样本替代全局证明。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-noslot-layer-interval-pdec-ledger.json` | `15ea7347eeae96fd2ac164f818274476b84449932c380a5f3fc719d21c3c989a` |
| `experiments/prime_matrix_square_phase_noslot_layer_interval_pdec_router.py` | `c0efd146c750223e5b5f5bfcd177f9cfe8fd61a19b8e50030eca50e2d71dee8f` |
