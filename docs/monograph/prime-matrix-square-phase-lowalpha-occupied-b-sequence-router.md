# Prime Matrix square-phase low-alpha occupied-b 序列路由

**状态：** `occupied_b_prime_density_reduced_to_low_multiplicity_sparse_sequence_open`

非空纤维上的素性问题被压成 occupied-b 稀疏序列。固定 `q` 时，若两个不同素数 `a_1<a_2` 产生同一个 `b`，则两个乘积 `q*a_i*b` 都落在长度小于 `P` 的区间 `(P^2,P^2+P)`，但 `q*b*(a_2-a_1)>P`，矛盾；所以固定 `q` 内 `a->b` 注入。样本中局部注入零失败；跨 `q` 重数低，最大 occupied-b 重数为 3，最大 prime-b 重数也为 3。剩余是证明全局低重数包络与 occupied-b 序列的一维 Selberg 上筛，或把素性尖峰登记为 PDEC。

```text
fixed_q_a_to_b_injection_proved=true
fixed_q_injection_failure_count=0
occupied_b_sequence_materialized=true
global_b_multiplicity_bound_proved=false
occupied_b_selberg_prime_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局 occupied-b 账本

| q axes | occupied fibers | distinct b | duplicate ratio | max b mult | prime fibers | distinct prime b | prime dup ratio | max prime mult |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 171 | 43666 | 42315 | 1.031927 | 3 | 4173 | 4051 | 1.030116 | 3 |

## 2. 素性模型

| occupied prime model | prime/model | top collision |
| ---: | ---: | --- |
| 4134.665019 | 1.009272 | `{'b': 4533, 'multiplicity': 3, 'records': [{'q': 73, 'a': 4079, 'b': 4533, 'width': 0.1233817044870654, 'center': 4532.920441150295, 'prime_b': False, 'prime_weight': 0.11877723540089558}, {'q': 131, 'a': 2273, 'b': 4533, 'width': 0.12338336193549904, 'center': 4532.9813341482995, 'prime_b': False, 'prime_weight': 0.11877704588219272}, {'q': 191, 'a': 1559, 'b': 4533, 'width': 0.12338087577954723, 'center': 4532.889995264786, 'prime_b': False, 'prime_weight': 0.11877733015951908}]}` |

## 3. 每个 P 的总结

| P | occupied | distinct b | max b mult | prime fibers | distinct prime b | max prime mult | prime/model |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 777 | 766 | 2 | 99 | 99 | 1 | 1.047215 |
| 36739 | 4013 | 3927 | 3 | 429 | 419 | 2 | 1.005726 |
| 83561 | 10697 | 10410 | 3 | 1025 | 998 | 3 | 0.975818 |
| 200003 | 28179 | 27212 | 3 | 2620 | 2535 | 3 | 1.022172 |

## 4. 证明边界

- 已闭合：固定 `q` 内 `a->b` 注入。
- 已物化：跨 `q` occupied-b 与 prime-b 重数账本。
- 未闭合：跨 `q` 全局低重数包络证明。
- 未闭合：occupied-b 稀疏序列的一维 Selberg 上筛素性上界。
- 未闭合：若素性尖峰持续出现，对应 PDEC 的排除。
- 下一目标：`LowMultiplicityOccupiedBOneDimensionalSelbergBoundOrPrimeSpikePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-fiber-phase-decomposition-router.json` | `1543e8024672a1bd3afa5e41611c42418553241740fc69accf21f8de233af990` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-carry-router.json` | `41173d466644115c697765fc1c37912bb1dcc183620107f7439da7ab11b179a7` |
| `experiments/prime_matrix_square_phase_lowalpha_occupied_b_sequence_router.py` | `82b0e23ea17cc2d882727ebb97b51974897d15c27e54d0283ed90232360cd876` |
