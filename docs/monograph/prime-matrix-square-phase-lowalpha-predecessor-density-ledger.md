# Prime Matrix square-phase low-alpha 前驱密度账本

**状态：** `predecessor_u_capacity_multiplicity_density_open`

固定 crossing 前驱 `D_-` 后，`u=r*t` 落在整数短区间 `P^2/D_- < u <= (P^2+P-1)/D_-`。这给出 `u` 值容量，但一阶负载可因同一 `u` 被块内多个 `q` 命中而超过该容量。因此剩余必须同时控制 block-multiplicity 与 prime/rough Buchstab 密度，或把异常登记为 PDEC。

```text
predecessor_u_capacity_bound_closed=false
over_capacity_predecessor_count=73
u_capacity_alone_sufficient_for_first_moment_bound=false
block_multiplicity_bound_proved=false
buchstab_density_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 总体容量

| total hits | integer capacity | hits/capacity |
| ---: | ---: | ---: |
| 21504 | 203463 | 0.105690 |

## 2. 最坏 low-alpha 块

| P | block | hits | active D_- | capacity | hits/capacity | top-hit D_- | top-density D_- | large-cap density |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- | ---: |
| 200003 | `(31,62]` | 4540 | 1173 | 45038 | 0.100804 | `{'d_minus': 37, 'hits': 362, 'capacity': 5406, 'density': 0.06696263411024787}` | `{'d_minus': 147559, 'hits': 3, 'capacity': 1, 'density': 3.0}` | 0.068570 |

## 3. 每个 P 的总结

| P | low blocks | total hits | integer capacity | hits/capacity | worst block |
| ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 412 | 3025 | 0.136198 | `(31,62]` |
| 36739 | 3 | 2040 | 17279 | 0.118062 | `(31,62]` |
| 83561 | 4 | 5659 | 51541 | 0.109796 | `(31,62]` |
| 200003 | 4 | 13393 | 131618 | 0.101757 | `(31,62]` |

## 4. 证明边界

- 已闭合：逐前驱 `u` 短区间公式和整数容量账本。
- 未闭合：一阶负载允许同一 `u` 被多个块内 `q` 重复命中，故单纯 `u` 容量不能闭合。
- 未闭合：即使剥离 multiplicity，容量总和仍过宽，还需 Buchstab rough/prime 密度上界。
- 下一目标：`BlockMultiplicityAndBuchstabDensityOnPredecessorIntervalsOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.json` | `f041774be8b186cc7b89abf5a43c029d0fb27ca2b6eadb5077e5969d37e9813d` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-crossing-predecessor-router.json` | `0efba46c4858a88fed2f05dd6d6563563d1d04a4715edcd2904c9e35f2717522` |
| `experiments/prime_matrix_square_phase_lowalpha_predecessor_density_ledger.py` | `01f62569756dca9cb36fc7547886127870ff9ddd3d2081534cd5b58b21efffac` |
