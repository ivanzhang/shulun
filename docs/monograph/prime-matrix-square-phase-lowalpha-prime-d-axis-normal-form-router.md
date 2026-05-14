# Prime Matrix square-phase low-alpha prime-D 轴 normal form

**状态：** `quarter_gate_prime_d_axis_reduced_to_two_prime_strip_and_single_b_fibers_open`

在 `z>=P^(1/4)` 的 quarter-gate 内，semiprime predecessor 已退化为 `D_-=q`。于是 prime-u 分支就是双素数窄带 `P^2<q*u<=P^2+P-1`；semiprime-u 分支写成 `u=a*b` 且 `a>P/q`，固定 `(q,a)` 后 `b` 落在长度 `P/(q*a)<1` 的整数区间，因此是单点纤维。剩余不再是一般 Buchstab 分布，而是双素数窄带上界、半素数单纤维全局求和，以及 `z<P^(1/4)` ultra-low 复合尾项。

```text
prime_d_axis_normal_form_closed=true
prime_u_to_two_prime_strip_closed=true
semiprime_single_b_fiber_closed=true
prime_d_two_prime_strip_bound_proved=false
semiprime_single_fiber_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局分支容量

| quarter rows | ultra-low skipped | prime-u cap | semiprime-u cap | total cap | prime share | semiprime share |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 0 | 8298 | 4173 | 12471 | 0.665384 | 0.334616 |

## 2. 最坏 quarter-gate 块

| P | block | prime-u | semiprime-u | total | top q | top semiprime q |
| ---: | --- | ---: | ---: | ---: | --- | --- |
| 200003 | `(124,248]` | 1342 | 741 | 2083 | `{'q': 131, 'left_u': 305352672, 'right_u': 305354198, 'h': 1526.7404580152672, 'u_interval_capacity': 1527, 'prime_u_capacity': 74, 'semiprime_u_capacity': 53, 'total_capacity': 127, 'semiprime_a_count': 53, 'semiprime_a_fiber_capacity': 53, 'semiprime_single_b_fiber_closed': True, 'semiprime_width_failure_count': 0, 'semiprime_b_interval_failure_count': 0, 'top_semiprime_sample': {'u': 305353357, 'a': 1531, 'b': 199447, 'b_interval': [199447, 199447], 'b_width': 0.9972178040596128}}` | `{'q': 131, 'left_u': 305352672, 'right_u': 305354198, 'h': 1526.7404580152672, 'u_interval_capacity': 1527, 'prime_u_capacity': 74, 'semiprime_u_capacity': 53, 'total_capacity': 127, 'semiprime_a_count': 53, 'semiprime_a_fiber_capacity': 53, 'semiprime_single_b_fiber_closed': True, 'semiprime_width_failure_count': 0, 'semiprime_b_interval_failure_count': 0, 'top_semiprime_sample': {'u': 305353357, 'a': 1531, 'b': 199447, 'b_interval': [199447, 199447], 'b_width': 0.9972178040596128}}` |

## 3. 每个 P 的总结

| P | quarter rows | ultra-low skipped | prime-u | semiprime-u | total | semiprime a-fibers | worst block |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 0 | 168 | 99 | 267 | 99 | `(31,62]` |
| 36739 | 3 | 0 | 798 | 429 | 1227 | 429 | `(62,124]` |
| 83561 | 4 | 0 | 2141 | 1025 | 3166 | 1025 | `(124,248]` |
| 200003 | 4 | 0 | 5191 | 2620 | 7811 | 2620 | `(124,248]` |

## 4. 证明边界

- 已闭合：quarter-gate 内 `D_-=q` 轴的 normal form。
- 已闭合：prime-u 分支等价于双素数窄带点 `P^2<q*u<=P^2+P-1`。
- 已闭合：semiprime-u 分支固定 `(q,a)` 后 `b` 的整数区间长度小于一。
- 未闭合：双素数窄带的全局上筛常数与相位缺陷排除。
- 未闭合：半素数单纤维在所有 `(q,a)` 上的全局求和上界。
- 未闭合：`z<P^(1/4)` ultra-low 复合尾项。
- 下一目标：`PrimeDTwoPrimeStripBoundAndSemiprimeSingleFiberBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-predecessor-envelope-router.json` | `ef5019a7213b88a515692b4e2234c5be6c593552dfac7b856de5c8fa26c87e72` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-quarter-gate-router.json` | `1ee763007af6d4aa7f09b483e088b5bb35744c0f255e189bce7e07c9414e7ac6` |
| `experiments/prime_matrix_square_phase_lowalpha_prime_d_axis_normal_form_router.py` | `3ddf1878a5459c170f3ce4d07140c4e6669157923912ff3d107a781c48c8bf64` |
