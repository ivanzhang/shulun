# Prime Matrix square-phase low-alpha prime-D Selberg/相位接口

**状态：** `prime_d_axis_reduced_to_selberg_phase_constant_or_pdec_open`

`D_-=q` 轴现在有两个明确的常数账本：prime-u 分支按短区间素数上筛模型 `sum_q |I_q|/log(P^2/q)` 支付；semiprime-u 分支按单 `b` 纤维相位模型 `sum_{q,a} (P/(qa))/log(P^2/(qa))` 支付。样本中两个分支的全局实际/模型都接近 1，逐 q 压力也被常数 2 覆盖。该步只闭合接口与样本账本；全局仍需证明统一 Selberg/相位常数，或把失败登记为 reciprocal-phase/PDEC，并另处理 ultra-low 复合尾项。

```text
prime_u_selberg_model_materialized=true
semiprime_single_fiber_phase_model_materialized=true
sample_prime_u_C2_covers_all_q=true
sample_semiprime_C2_covers_all_q=true
prime_d_two_prime_selberg_bound_proved=false
semiprime_single_fiber_phase_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局模型压力

| q axes | prime actual | prime model | prime/model | semi actual | semi model | semi/model | total/model |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 171 | 8298 | 8229.927319 | 1.008271 | 4173 | 4133.119679 | 1.009649 | 1.008732 |

## 2. 相位栅格压力

| phase mass | nonempty fibers | nonempty/phase | max prime q/model | max semi q/model | max phase q/model |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 43652.759461 | 43666 | 1.000303 | 1.402074 | 1.537294 | 1.192686 |

## 3. 最热 q 轴

| type | record |
| --- | --- |
| prime-u | `{'q': 263, 'h': 317.72243346007605, 'u_interval_capacity': 317, 'prime_u_capacity': 26, 'prime_u_model': 18.54395843659127, 'prime_u_over_model': 1.4020738931713919, 'semiprime_u_capacity': 7, 'semiprime_phase_mass': 121.64511604184274, 'semiprime_nonempty_fibers': 113, 'semiprime_nonempty_over_phase': 0.9289316634884951, 'semiprime_prime_b_model': 12.227826418790631, 'semiprime_u_over_prime_b_model': 0.5724647832130677, 'semiprime_a_count': 620, 'semiprime_max_width': 0.9598865059216799, 'semiprime_top_width_sample': {'a': 331, 'b_interval': [80210, 80210], 'width': 0.9598865059216799, 'center': 80209.0763213215}}` |
| semiprime-u | `{'q': 181, 'h': 202.97790055248618, 'u_interval_capacity': 203, 'prime_u_capacity': 13, 'prime_u_model': 12.828043308848283, 'prime_u_over_model': 1.013404748254405, 'semiprime_u_capacity': 13, 'semiprime_phase_mass': 77.90543100705356, 'semiprime_nonempty_fibers': 72, 'semiprime_nonempty_over_phase': 0.9241974412988115, 'semiprime_prime_b_model': 8.45641927369529, 'semiprime_u_over_prime_b_model': 1.5372936912480277, 'semiprime_a_count': 352, 'semiprime_max_width': 0.9619805713387971, 'semiprime_top_width_sample': {'a': 211, 'b_interval': [35343, 35343], 'width': 0.9619805713387971, 'center': 35342.204210416065}}` |
| phase lattice | `{'q': 73, 'h': 137.08219178082192, 'u_interval_capacity': 137, 'prime_u_capacity': 9, 'prime_u_model': 9.694536647912884, 'prime_u_over_model': 0.9283579326029564, 'semiprime_u_capacity': 5, 'semiprime_phase_mass': 47.791289800447515, 'semiprime_nonempty_fibers': 57, 'semiprime_nonempty_over_phase': 1.1926859525659057, 'semiprime_prime_b_model': 5.868707131953871, 'semiprime_u_over_prime_b_model': 0.851976404270722, 'semiprime_a_count': 160, 'semiprime_max_width': 0.9862028185670642, 'semiprime_top_width_sample': {'a': 139, 'b_interval': [9869, 9869], 'width': 0.9862028185670642, 'center': 9868.93160540061}}` |

## 4. 每个 P 的总结

| P | q rows | prime/model | semi/model | phase nonempty/phase | total |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 14 | 1.017741 | 1.070196 | 1.024436 | 267 |
| 36739 | 32 | 0.983280 | 1.000083 | 0.993755 | 1227 |
| 83561 | 50 | 1.045759 | 0.977995 | 1.002613 | 3166 |
| 200003 | 75 | 0.997124 | 1.022006 | 0.999718 | 7811 |

## 5. 证明边界

- 已闭合：prime-u 与 semiprime 单纤维的同参数模型账本接口。
- 已闭合：样本中逐 q 压力均由常数 2 覆盖。
- 未闭合：统一的非对称双素数窄带 Selberg 上界。
- 未闭合：单 `b` 纤维相位栅格与素性模型的全局常数证明。
- 未闭合：若上述模型失败，对应 reciprocal-phase/PDEC 的排除。
- 未闭合：`z<P^(1/4)` ultra-low 复合尾项。
- 下一目标：`AsymmetricPrimeDTwoPrimeSelbergAndSingleFiberPhaseBoundOrPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-d-axis-normal-form-router.json` | `6727d8ab75e183541d62cecb47b31f87dc918e8afd51e6b21cd4736893f3129e` |
| `docs/monograph/prime-matrix-square-phase-rfp-upper-direct-attack-router.json` | `c8ecab3fdc5e787f3b7cef1d73d34868d48878e48a7b9c8b6cc88218ebcfed81` |
| `experiments/prime_matrix_square_phase_lowalpha_prime_d_selberg_phase_router.py` | `6a2457c291d39217345f5a43bfaf93fee5c119050862b4588cfccd22bfd14ff1` |
