# Prime Matrix square-phase low-alpha 先验前驱 envelope

**状态：** `active_predecessors_replaced_by_prior_eligible_envelope_open`

semiprime 分支中的活跃前驱不再需要后验提取：固定 block `(z,Z]` 后，所有可能前驱先验等于 `D_-=qE<sqrt(P)`，其中 `q` 属于当前 block，`E` 没有不超过 `z` 的素因子。容量为正的先验 envelope 与真实活跃前驱完全一致，且加权 prime/semiprime 容量逐项等于真实命中。剩余被压成这个先验 envelope 上的全局容量上界，或容量尖峰的 PDEC 排除。

```text
prior_eligible_predecessor_envelope_closed=true
active_equals_capacity_positive_envelope=true
weighted_envelope_capacity_equals_actual_hits=true
global_capacity_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局 envelope 容量

| eligible D | cap-positive D | active D | actual hits | envelope cap | actual/cap | cap/integer |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 171 | 171 | 171 | 12471 | 12471 | 1.000000 | 0.080266 |

## 2. 最坏 low-alpha 块

| P | block | eligible D | cap-positive D | actual | envelope cap | top capacity record |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 200003 | `(124,248]` | 23 | 23 | 2083 | 2083 | `{'d_minus': 131, 'omega_block': 1, 'prime_capacity': 74, 'semiprime_capacity': 53, 'weighted_total_capacity': 127, 'h': 1526.7404580152672}` |

## 3. 每个 P 的总结

| P | low blocks | eligible D | cap-positive D | active D | actual | envelope cap | cap/integer | worst block |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 14 | 14 | 14 | 267 | 267 | 0.112468 | `(31,62]` |
| 36739 | 3 | 32 | 32 | 32 | 1227 | 1227 | 0.090721 | `(62,124]` |
| 83561 | 4 | 50 | 50 | 50 | 3166 | 3166 | 0.085385 | `(124,248]` |
| 200003 | 4 | 75 | 75 | 75 | 7811 | 7811 | 0.076285 | `(124,248]` |

## 4. 证明边界

- 已闭合：活跃前驱集合可由先验 envelope `D_-=qE<sqrt(P)` 替代。
- 已闭合：容量为正的 envelope 与真实活跃集合一致；加权容量等于真实命中。
- 未闭合：对该先验 envelope 的全局加权 prime/semiprime 容量上界。
- 未闭合：若 envelope 容量尖峰持续出现，需证明其形成 PDEC 并排除。
- 下一目标：`EligiblePredecessorEnvelopeWeightedCapacityGlobalBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-semiprime-capacity-router.json` | `88054fba3c7adeea2a5f3d834af2172b157af81f2be8b023c846a6843c5c1780` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-fiber-router.json` | `6cd76b08c581610754ddeda2bac1fd3bb2dcab2a235fdd8d95a82f82c4ede858` |
| `experiments/prime_matrix_square_phase_lowalpha_predecessor_envelope_router.py` | `b7e836b036a60fdc86e9b05a7462ced45b1a6d35714ec4d2f234a5b76ab2bce9` |
