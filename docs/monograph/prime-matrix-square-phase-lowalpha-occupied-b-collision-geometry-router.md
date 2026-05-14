# Prime Matrix square-phase low-alpha occupied-b 碰撞几何路由

**状态：** `occupied_b_collisions_reduced_to_short_semiprime_modulus_intervals_open`

同一 occupied-b 的跨 q 重复不再是二维纤维问题。固定 b 后，每条记录的半素数模数 n=q*a 都必须落入短区间 (P^2/b,(P^2+P-1)/b]；固定 (b,q) 后 a 的允许区间长度为 P/(bq)<1，所以每个 q 至多贡献一个 a。样本中该短区间恒等式、固定 (b,q) 单 a 纤维、以及同 q 碰撞排除均无失败；剩余被压成一维 q 扫描上的低重数/素性上筛，或素性尖峰 PDEC。

```text
short_semiprime_modulus_interval_identity_closed=true
fixed_bq_single_a_fiber_closed=true
same_q_collision_excluded_by_imported_injection=true
global_low_multiplicity_bound_proved=false
one_dimensional_selberg_prime_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 碰撞账本

| occupied fibers | distinct b | collision b | collision fibers | duplicate excess | max b mult | prime collision b | prime collision fibers | max prime mult |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 43666 | 42315 | 1328 | 2679 | 1351 | 3 | 119 | 241 | 3 |

## 2. 短区间几何

| interval failures | fixed (b,q) failures | same q failures | max n-capacity on collisions | max n-width | max a-width for fixed (b,q) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 18 | 18.353951 | 0.163942 |

## 3. 典型碰撞

| kind | data |
| --- | --- |
| top multiplicity | `{'p': 36739, 'b': 4533, 'multiplicity': 3, 'prime_b': False, 'n_interval': [297762, 297769], 'n_interval_capacity': 8, 'n_interval_width': 8.104787116699757, 'n_span': 6, 'min_adjacent_n_gap': 2, 'max_adjacent_n_gap': 4, 'q_values': [131, 73, 191], 'a_values': [2273, 4079, 1559], 'n_values': [297763, 297767, 297769], 'repeated_q_count': 0, 'sample_records': [{'q': 131, 'a': 2273, 'b': 4533, 'width': 0.12338336193549904, 'center': 4532.9813341482995, 'prime_b': False, 'prime_weight': 0.11877704588219272, 'n': 297763, 'n_interval': [297762, 297769], 'n_interval_capacity': 8, 'n_interval_width': 8.104787116699757, 'n_interval_hit_ok': True, 'a_interval_for_fixed_bq': [2273, 2273], 'a_interval_capacity_for_fixed_bq': 1, 'a_interval_width_for_fixed_bq': 0.06186860394427296, 'a_singleton_for_fixed_bq': True, 'qa_semiprime_modulus': 297763}, {'q': 73, 'a': 4079, 'b': 4533, 'width': 0.1233817044870654, 'center': 4532.920441150295, 'prime_b': False, 'prime_weight': 0.11877723540089558, 'n': 297767, 'n_interval': [297762, 297769], 'n_interval_capacity': 8, 'n_interval_width': 8.104787116699757, 'n_interval_hit_ok': True, 'a_interval_for_fixed_bq': [4079, 4079], 'a_interval_capacity_for_fixed_bq': 1, 'a_interval_width_for_fixed_bq': 0.1110244810506816, 'a_singleton_for_fixed_bq': True, 'qa_semiprime_modulus': 297767}, {'q': 191, 'a': 1559, 'b': 4533, 'width': 0.12338087577954723, 'center': 4532.889995264786, 'prime_b': False, 'prime_weight': 0.11877733015951908, 'n': 297769, 'n_interval': [297762, 297769], 'n_interval_capacity': 8, 'n_interval_width': 8.104787116699757, 'n_interval_hit_ok': True, 'a_interval_for_fixed_bq': [1559, 1559], 'a_interval_capacity_for_fixed_bq': 1, 'a_interval_width_for_fixed_bq': 0.04243344040156941, 'a_singleton_for_fixed_bq': True, 'qa_semiprime_modulus': 297769}]}` |
| densest interval | `{'p': 10007, 'b': 3151, 'multiplicity': 2, 'prime_b': False, 'n_interval': [31781, 31783], 'n_interval_capacity': 3, 'n_interval_width': 3.175817200888607, 'n_span': 2, 'min_adjacent_n_gap': 2, 'max_adjacent_n_gap': 2, 'q_values': [61, 37], 'a_values': [521, 859], 'n_values': [31781, 31783], 'repeated_q_count': 0, 'sample_records': [{'q': 61, 'a': 521, 'b': 3151, 'width': 0.3148736666561782, 'center': 3150.9407822283756, 'prime_b': False, 'prime_weight': 0.12413945986023728, 'n': 31781, 'n_interval': [31781, 31783], 'n_interval_capacity': 3, 'n_interval_width': 3.175817200888607, 'n_interval_hit_ok': True, 'a_interval_for_fixed_bq': [521, 521], 'a_interval_capacity_for_fixed_bq': 1, 'a_interval_width_for_fixed_bq': 0.05206257706374765, 'a_singleton_for_fixed_bq': True, 'qa_semiprime_modulus': 31781}, {'q': 37, 'a': 859, 'b': 3151, 'width': 0.3148538526885442, 'center': 3150.7425038542615, 'prime_b': False, 'prime_weight': 0.12414042963721085, 'n': 31783, 'n_interval': [31781, 31783], 'n_interval_capacity': 3, 'n_interval_width': 3.175817200888607, 'n_interval_hit_ok': True, 'a_interval_for_fixed_bq': [859, 859], 'a_interval_capacity_for_fixed_bq': 1, 'a_interval_width_for_fixed_bq': 0.0858328973213137, 'a_singleton_for_fixed_bq': True, 'qa_semiprime_modulus': 31783}]}` |

## 4. 每个 P 的总结

| P | collision b | dup excess | max mult | prime collision b | prime dup excess | max n-cap | max fixed-bq a-width |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 11 | 11 | 2 | 0 | 0 | 6 | 0.161180 |
| 36739 | 85 | 86 | 3 | 10 | 10 | 13 | 0.163609 |
| 83561 | 281 | 287 | 3 | 25 | 27 | 15 | 0.163843 |
| 200003 | 951 | 967 | 3 | 84 | 85 | 18 | 0.163942 |

## 5. 证明边界

- 已闭合：同一 `b` 的每个记录等价于 `q*a` 落入短区间 `(P^2/b,(P^2+P-1)/b]`。
- 已闭合：固定 `(b,q)` 时 `a` 的允许区间长度小于一，所以每个 `q` 至多一个 `a`。
- 已继承：固定 `q` 的 `a->b` 注入排除同 `q` 碰撞。
- 未闭合：固定 `b` 的全局低重数上界，即一维 `q` 扫描中有多少个 `q` 使唯一候选 `a_q` 为素数且相位非空。
- 未闭合：该稀疏 occupied-b 序列上的素性上筛，或持续素性尖峰的 PDEC 排除。
- 下一目标：`OccupiedBShortSemiprimeModulusMultiplicityBoundOrPrimeSpikePDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-occupied-b-sequence-router.json` | `8fe89eaab334cdee38f6b5d2b9a54e7f00082a7bdfbeaf460eb9b64ff03fa631` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.json` | `6f41d62e64c519dcede5d9341dbff6c628034cbdd3814b2cd1a8234b0f4e2ed8` |
| `experiments/prime_matrix_square_phase_lowalpha_occupied_b_collision_geometry_router.py` | `c70a87712407aef1ed8c24944aad41e5ff1b9f4d60e65474f7ed776061c14eea` |
