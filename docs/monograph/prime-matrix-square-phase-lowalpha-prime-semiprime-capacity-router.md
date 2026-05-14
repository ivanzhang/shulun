# Prime Matrix square-phase low-alpha prime/semiprime 精确容量

**状态：** `semiprime_regime_reduced_to_exact_prime_semiprime_capacity_open`

semiprime regime 已从分布模型降为精确容量：对每个活跃前驱 `D_-`，直接枚举短区间内所有 prime-u 与 H-rough semiprime-u，再乘 `omega_B(D_-)`。实际 prime-u/semiprime-u 命中均被该精确容量覆盖。剩余不是单纤维结构，而是证明这些精确容量的全局上界，或把容量尖峰登记为 PDEC。

```text
exact_prime_semiprime_capacity_cover_closed=true
global_capacity_bound_proved=false
local_capacity_spike_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 全局容量

| actual hits | weighted prime capacity | weighted semiprime capacity | weighted total capacity | actual/total capacity | exact/integer capacity |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 12471 | 8298 | 4173 | 12471 | 1.000000 | 0.080266 |

## 2. 最坏 low-alpha 块

| P | block | actual | weighted total cap | actual/cap | top cap pressure | top prime pressure | top semiprime pressure |
| ---: | --- | ---: | ---: | ---: | --- | --- | --- |
| 200003 | `(124,248]` | 2083 | 2083 | 1.000000 | `{'d_minus': 127, 'omega_block': 1, 'actual_prime': 82, 'actual_semiprime': 34, 'prime_capacity': 82, 'semiprime_capacity': 34, 'weighted_prime_capacity': 82, 'weighted_semiprime_capacity': 34, 'pressure': 1.0, 'prime_pressure': 1.0, 'semiprime_pressure': 1.0, 'h': 1574.8267716535433}` | `{'d_minus': 127, 'omega_block': 1, 'actual_prime': 82, 'actual_semiprime': 34, 'prime_capacity': 82, 'semiprime_capacity': 34, 'weighted_prime_capacity': 82, 'weighted_semiprime_capacity': 34, 'pressure': 1.0, 'prime_pressure': 1.0, 'semiprime_pressure': 1.0, 'h': 1574.8267716535433}` | `{'d_minus': 127, 'omega_block': 1, 'actual_prime': 82, 'actual_semiprime': 34, 'prime_capacity': 82, 'semiprime_capacity': 34, 'weighted_prime_capacity': 82, 'weighted_semiprime_capacity': 34, 'pressure': 1.0, 'prime_pressure': 1.0, 'semiprime_pressure': 1.0, 'h': 1574.8267716535433}` |

## 3. 每个 P 的总结

| P | low blocks | actual | weighted cap | actual/cap | exact/integer | worst block |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 267 | 267 | 1.000000 | 0.112468 | `(31,62]` |
| 36739 | 3 | 1227 | 1227 | 1.000000 | 0.090721 | `(62,124]` |
| 83561 | 4 | 3166 | 3166 | 1.000000 | 0.085385 | `(124,248]` |
| 200003 | 4 | 7811 | 7811 | 1.000000 | 0.076285 | `(124,248]` |

## 4. 证明边界

- 已闭合：prime-u 与 H-rough semiprime-u 的精确容量覆盖。
- 未闭合：这些精确容量的全局上界。
- 未闭合：若某前驱容量尖峰持续出现，需证明其进入 PDEC。
- 下一目标：`WeightedPrimeSemiprimeIntervalCapacityGlobalBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.json` | `2a2d7d6b93538d7dc0d4165910449f43abb6f32381b2db3b50f865568e1b9675` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-fiber-router.json` | `6cd76b08c581610754ddeda2bac1fd3bb2dcab2a235fdd8d95a82f82c4ede858` |
| `experiments/prime_matrix_square_phase_lowalpha_prime_semiprime_capacity_router.py` | `2fe006241865fe7d2b7b4475fe4601a6aedd802c993f29b2492b8a3d6edbabc8` |
