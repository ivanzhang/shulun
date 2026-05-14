# Prime Matrix square-phase low-alpha semiprime 单纤维路由

**状态：** `semiprime_predecessor_interval_reduced_to_prime_and_single_b_fibers_open`

semiprime regime `D_-<sqrt(P)` 已化为两个一维纤维：`u` 为素数的 prime-u 短区间，以及 `u=a*b` 时固定 `(D_-,a)` 后长度小于一的单 `b` 纤维。因此半素数分支不再需要完整 Buchstab 递归；剩余是 prime-u 与 prime-a/b 的分布上界，或失败形成前驱/纤维 PDEC。

```text
semiprime_gate_checked=true
semiprime_a_fiber_collision_free=true
prime_and_semiprime_distribution_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局 semiprime regime

| hits | prime u | semiprime u | weighted capacity | weighted density |
| ---: | ---: | ---: | ---: | ---: |
| 12471 | 8298 | 4173 | 155370 | 0.080266 |

## 2. 最坏 low-alpha 块

| P | block | hits | prime u | semiprime u | active D | prime fibers | semiprime a-fibers | top prime fiber | top semiprime fiber |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 200003 | `(124,248]` | 2083 | 1342 | 741 | 23 | 1342 | 741 | `{'d_minus': 127, 'u': 314970091, 'multiplicity': 1, 'q_values': [127]}` | `{'d_minus': 127, 'a': 3169, 'b_count': 1, 'b_values': [99391]}` |

## 3. 每个 P 的总结

| P | low blocks | hits | prime u | semiprime u | weighted density | worst block |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 2 | 267 | 168 | 99 | 0.112468 | `(31,62]` |
| 36739 | 3 | 1227 | 798 | 429 | 0.090721 | `(62,124]` |
| 83561 | 4 | 3166 | 2141 | 1025 | 0.085385 | `(124,248]` |
| 200003 | 4 | 7811 | 5191 | 2620 | 0.076285 | `(124,248]` |

## 4. 证明边界

- 已闭合：semiprime regime 中 `u` 只可能为素数或两个大素因子。
- 已闭合：固定 `(D_-,a)` 后 semiprime 的 `b` 纤维单点化。
- 未闭合：prime-u 与 prime-a/b 的短区间分布上界。
- 下一目标：`PrimeAndSemiprimeFiberDistributionBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-block-multiplicity-router.json` | `8d674312b227502b88a5e5c234c46f5f164a4e0cc7ac5d982c7d1f1336c61224` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-depth-gate-router.json` | `2a2d7d6b93538d7dc0d4165910449f43abb6f32381b2db3b50f865568e1b9675` |
| `experiments/prime_matrix_square_phase_lowalpha_semiprime_fiber_router.py` | `bcefbd4bd3e51c58df9616c8e0b577f4612e200972f7baea8cd75a418b9f9da1` |
