# Prime Matrix square-phase low-alpha semiprime 单纤维相位/素性分解

**状态：** `semiprime_single_fiber_split_to_phase_and_occupied_prime_density_open`

semiprime 单 `b` 纤维进一步拆成两个独立输入：第一，`(q,a)` 对应的长度小于一的 `b` 区间是否非空，其总量由 reciprocal phase mass `sum P/(qa)` 控制；第二，在非空纤维中该唯一整数 `b` 是否为素数，其模型为 `sum_{nonempty} 1/log(P^2/(qa))`。样本显示非空纤维/相位质量几乎为 1，非空纤维内素性密度也近似模型；逐 q 最坏相位压力低于 1.25，逐 q 最坏素性压力低于 1.75。剩余是证明这两个常数，或把失败登记为 reciprocal-phase/PDEC 与 occupied-fiber prime spike。

```text
phase_occupancy_model_materialized=true
occupied_fiber_prime_density_model_materialized=true
sample_phase_constant_covers_all_q=true
sample_prime_constant_covers_all_q=true
reciprocal_fiber_phase_discrepancy_bound_proved=false
occupied_fiber_prime_density_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局分解

| q axes | semiprime actual | phase mass | nonempty | nonempty/phase | occupied model | actual/occupied model |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 171 | 4173 | 43652.759461 | 43666 | 1.000303 | 4134.665019 | 1.009272 |

## 2. 最热 q 轴

| type | record |
| --- | --- |
| phase | `{'q': 73, 'h': 137.08219178082192, 'semiprime_u_capacity': 5, 'phase_mass': 47.791289800447515, 'nonempty_fibers': 57, 'nonempty_over_phase': 1.1926859525659057, 'width_prime_model': 5.868707131953871, 'semiprime_over_width_model': 0.851976404270722, 'occupied_prime_model': 7.019193059939363, 'semiprime_over_occupied_model': 0.7123325939752957, 'max_width': 0.9862028185670642, 'top_width_sample': {'a': 139, 'b_interval': [9869, 9869], 'width': 0.9862028185670642, 'center': 9868.93160540061}}` |
| occupied-prime | `{'q': 181, 'h': 202.97790055248618, 'semiprime_u_capacity': 13, 'phase_mass': 77.90543100705356, 'nonempty_fibers': 72, 'nonempty_over_phase': 0.9241974412988115, 'width_prime_model': 8.45641927369529, 'semiprime_over_width_model': 1.5372936912480277, 'occupied_prime_model': 7.791627631052082, 'semiprime_over_occupied_model': 1.668457556697258, 'max_width': 0.9619805713387971, 'top_width_sample': {'a': 211, 'b_interval': [35343, 35343], 'width': 0.9619805713387971, 'center': 35342.204210416065}}` |

## 3. 每个 P 的总结

| P | semiprime | nonempty/phase | actual/occupied model | actual/width model |
| ---: | ---: | ---: | ---: | ---: |
| 10007 | 99 | 1.024436 | 1.047215 | 1.070196 |
| 36739 | 429 | 0.993755 | 1.005726 | 1.000083 |
| 83561 | 1025 | 1.002613 | 0.975818 | 0.977995 |
| 200003 | 2620 | 0.999718 | 1.022172 | 1.022006 |

## 4. 证明边界

- 已闭合：semiprime 单纤维分成相位非空问题与非空纤维素性问题。
- 已闭合：样本中相位常数 `1.25` 与素性常数 `1.75` 覆盖逐 q 压力。
- 未闭合：reciprocal phase discrepancy 的全局常数证明或 PDEC 排除。
- 未闭合：occupied-fiber prime density 的全局常数证明或素性尖峰排除。
- 未闭合：ultra-low 复合尾项 Rankin/Selberg 上界。
- 下一目标：`ReciprocalFiberPhaseDiscrepancyAndOccupiedFiberPrimeDensityBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-selberg-phase-router.json` | `33dfbaed09353024edee0ccc717a184111e0611f8cb4f4ff49cf802b2f83d526` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-u-brun-titchmarsh-router.json` | `efefb80cf3bc3f0c0ecc1bd6f46e9c5c3eab88e992e79b9025b19de8cecdf2ea` |
| `experiments/prime_matrix_square_phase_lowalpha_semiprime_fiber_phase_decomposition_router.py` | `98b87870a22c79c95ae793fbe18f1609a012c663649d9393e0c381c668c40ecc` |
