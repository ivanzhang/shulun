# Prime Matrix square-phase low-alpha fixed-b 半素数 incidence 路由

**状态：** `fixed_b_prime_a_reduced_to_short_interval_semiprime_incidence_open`

固定 b 后，prime-a 候选与短区间 J_b 中的活跃半素数点完全一致：n=q*a，q 为活跃小素轴，a 为大素补因子，且 a<=b。由于 q<sqrt(P)<a，每个半素数 n 至多给出一个 q，因此 prime-a 到 n 的投影是注入；prime-b 层只是再要求 b 本身为素数。样本中 q-scan 与直接短区间半素数枚举完全一致，无遗漏、无额外、无 n 碰撞。剩余被压成短区间活跃半素数 incidence 的 Selberg/Brun 上界，或 prime-b 尖峰 PDEC 排除。

```text
prime_a_semiprime_interval_identity_closed=true
prime_a_to_n_injection_closed=true
prime_a_interval_capacity_bound_closed=true
short_interval_semiprime_selberg_bound_proved=false
prime_b_spike_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 全局账本

| b with phase | n-capacity sum | phase | prime-a | prime-a/n-cap | prime-b | prime-b/n-cap | prime-b/prime-a |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 42315 | 170153 | 86844 | 43666 | 0.256628 | 4173 | 0.024525 | 0.095566 |

## 2. 精确性与容量

| missing | extra | n injection failures | max n-cap | max prime-a | max prime-b |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 21 | 3 | 3 |

## 3. 关键样本

| kind | data |
| --- | --- |
| top prime-a | `{'b': 4533, 'n_interval': [297762, 297769], 'n_interval_capacity': 8, 'phase_multiplicity': 3, 'prime_a_multiplicity': 3, 'prime_b_multiplicity': 0, 'prime_a_over_n_capacity': 0.375, 'prime_b_over_n_capacity': 0.0, 'prime_b_over_prime_a': 0.0, 'sample_prime_a': [{'q': 73, 'a': 4079, 'b': 4533, 'n': 297767, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [4079, 4079], 'raw_a_interval': [4079, 4079], 'singleton_ok': True, 'a_interval_width': 0.1110244810506816, 'n_interval': [297762, 297769]}, {'q': 131, 'a': 2273, 'b': 4533, 'n': 297763, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [2273, 2273], 'raw_a_interval': [2273, 2273], 'singleton_ok': True, 'a_interval_width': 0.06186860394427296, 'n_interval': [297762, 297769]}, {'q': 191, 'a': 1559, 'b': 4533, 'n': 297769, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [1559, 1559], 'raw_a_interval': [1559, 1559], 'singleton_ok': True, 'a_interval_width': 0.04243344040156941, 'n_interval': [297762, 297769]}], 'sample_prime_b': []}` |
| top prime-b | `{'b': 9733, 'n_interval': [717399, 717407], 'n_interval_capacity': 9, 'phase_multiplicity': 6, 'prime_a_multiplicity': 3, 'prime_b_multiplicity': 3, 'prime_a_over_n_capacity': 0.3333333333333333, 'prime_b_over_n_capacity': 0.3333333333333333, 'prime_b_over_prime_a': 1.0, 'sample_prime_a': [{'q': 101, 'a': 7103, 'b': 9733, 'n': 717403, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [7103, 7103], 'raw_a_interval': [7103, 7103], 'singleton_ok': True, 'a_interval_width': 0.08500325014521384, 'n_interval': [717399, 717407]}, {'q': 151, 'a': 4751, 'b': 9733, 'n': 717401, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [4751, 4751], 'raw_a_interval': [4751, 4751], 'singleton_ok': True, 'a_interval_width': 0.05685647857395098, 'n_interval': [717399, 717407]}, {'q': 233, 'a': 3079, 'b': 9733, 'n': 717407, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [3079, 3079], 'raw_a_interval': [3079, 3079], 'singleton_ok': True, 'a_interval_width': 0.036846902423461794, 'n_interval': [717399, 717407]}], 'sample_prime_b': [{'q': 101, 'a': 7103, 'b': 9733, 'n': 717403, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [7103, 7103], 'raw_a_interval': [7103, 7103], 'singleton_ok': True, 'a_interval_width': 0.08500325014521384, 'n_interval': [717399, 717407]}, {'q': 151, 'a': 4751, 'b': 9733, 'n': 717401, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [4751, 4751], 'raw_a_interval': [4751, 4751], 'singleton_ok': True, 'a_interval_width': 0.05685647857395098, 'n_interval': [717399, 717407]}, {'q': 233, 'a': 3079, 'b': 9733, 'n': 717407, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [3079, 3079], 'raw_a_interval': [3079, 3079], 'singleton_ok': True, 'a_interval_width': 0.036846902423461794, 'n_interval': [717399, 717407]}]}` |
| densest prime-a | `{'b': 5260, 'n_interval': [19039, 19039], 'n_interval_capacity': 1, 'phase_multiplicity': 1, 'prime_a_multiplicity': 1, 'prime_b_multiplicity': 0, 'prime_a_over_n_capacity': 1.0, 'prime_b_over_n_capacity': 0.0, 'prime_b_over_prime_a': 0.0, 'sample_prime_a': [{'q': 79, 'a': 241, 'b': 5260, 'n': 19039, 'prime_a': True, 'prime_b': False, 'valid_a_interval': [241, 241], 'raw_a_interval': [241, 241], 'singleton_ok': True, 'a_interval_width': 0.02408191750493334, 'n_interval': [19039, 19039]}], 'sample_prime_b': []}` |
| densest prime-b | `{'b': 5641, 'n_interval': [17753, 17753], 'n_interval_capacity': 1, 'phase_multiplicity': 1, 'prime_a_multiplicity': 1, 'prime_b_multiplicity': 1, 'prime_a_over_n_capacity': 1.0, 'prime_b_over_n_capacity': 1.0, 'prime_b_over_prime_a': 1.0, 'sample_prime_a': [{'q': 41, 'a': 433, 'b': 5641, 'n': 17753, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [433, 433], 'raw_a_interval': [433, 433], 'singleton_ok': True, 'a_interval_width': 0.043267713301135845, 'n_interval': [17753, 17753]}], 'sample_prime_b': [{'q': 41, 'a': 433, 'b': 5641, 'n': 17753, 'prime_a': True, 'prime_b': True, 'valid_a_interval': [433, 433], 'raw_a_interval': [433, 433], 'singleton_ok': True, 'a_interval_width': 0.043267713301135845, 'n_interval': [17753, 17753]}]}` |

## 4. 每个 P 的总结

| P | n-capacity | phase | prime-a | prime-b | prime-a/n-cap | prime-b/n-cap | max n-cap | failures |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 2389 | 1060 | 777 | 99 | 0.325241 | 0.041440 | 9 | 0 |
| 36739 | 14184 | 6760 | 4013 | 429 | 0.282924 | 0.030245 | 13 | 0 |
| 83561 | 39888 | 20015 | 10697 | 1025 | 0.268176 | 0.025697 | 17 | 0 |
| 200003 | 113692 | 59009 | 28179 | 2620 | 0.247854 | 0.023045 | 21 | 0 |

## 5. 证明边界

- 已闭合：prime-a 候选等价于 `J_b` 中的活跃半素数 `n=q*a`。
- 已闭合：由于 `q<sqrt(P)<a`，同一半素数 `n` 不会给出两个活跃 `q`。
- 已闭合：prime-a 重数受 `J_b` 整数容量控制；prime-b 是其子层。
- 未闭合：对所有 `b` 的短区间活跃半素数 incidence 建立全局 Selberg/Brun 上界。
- 未闭合：若 prime-b 在这些短区间持续尖峰，需形成并排斥 PDEC/SAE。
- 下一目标：`ShortIntervalActiveSemiprimeSelbergBoundOrPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-divisor-envelope-router.json` | `8c48526d7aee1e0ac16f6e881b136e18de29a6d7bcd39f34c993b6b8028447a3` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-qscan-router.json` | `85bbe9471bade90f3be449692f4272acf40637e1836c6d0e317082f0572e2a27` |
| `experiments/prime_matrix_square_phase_lowalpha_fixed_b_semiprime_incidence_router.py` | `c54c949d612d74fe310080ab9715cbbcae49f6a544f6e68701d7966c15ecc324` |
