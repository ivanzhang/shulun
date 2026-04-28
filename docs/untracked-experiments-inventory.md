# 未提交实验文件分类与提交建议

日期：2026-04-28

## 总览

- 已修改但未提交文件：2 个
- 未跟踪文件：134 个
- 建议：先不要一次性全部提交；这些脚本多为探索性实验，宜按主题分批审查、补充说明后提交。
- 当前已推送的证明稿保持为条件归约稿；这些实验可作为后续研究佐证，但不应混入“最终证明”提交。

## 已修改但未提交

- `docs/rigid-patch-lemma-experiments.md`：已有跟踪文件被修改，建议先查看 diff，再决定是否单独提交。
- `experiments/rigid_patch_lemma_scan.py`：已有跟踪文件被修改，建议先查看 diff，再决定是否单独提交。

## 未跟踪文件分类

### CRT 投影实验

- 数量：3
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/k3_divisor_projection_fit.py`
  - `experiments/projection_min_prime_class.py`
  - `experiments/second_projection_kernel.py`

### R anchor 均匀性实验

- 数量：1
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/R_anchor_uniformity.py`

### S 条件残差/矩实验

- 数量：4
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/S_conditional_cumulants_by_H.py`
  - `experiments/S_conditional_residual_scan.py`
  - `experiments/S_residual_moments_by_H.py`
  - `experiments/S_variance_pair_decomposition.py`

### TR 上界模型实验

- 数量：1
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/TR_upper_bound_model.py`

### U 层/安全常数/半素数容量实验

- 数量：6
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/U_anchor_uniformity.py`
  - `experiments/U_integral_constant_convergence.py`
  - `experiments/U_integral_constant_model.py`
  - `experiments/U_layer_upper_sum.py`
  - `experiments/U_safety_dyadic_ratio.py`
  - `experiments/U_semiprime_2d_count.py`

### cumulant/connected 展开实验

- 数量：2
- 建议：中高优先级，建议补充脚本用途说明后分组提交。
  - `experiments/cumulant_projection_vanish.py`
  - `experiments/r_point_connected_cumulant_sample.py`

### 三点 cumulant/三阶矩实验

- 数量：2
- 建议：中高优先级，建议补充脚本用途说明后分组提交。
  - `experiments/three_point_cumulant_collision_classes.py`
  - `experiments/three_point_singular_cumulant.py`

### 三阶中心矩实验

- 数量：2
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/third_central_by_differences.py`
  - `experiments/third_moment_decomposition.py`

### 乘积压力实验

- 数量：4
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/product_pressure_bound_scan.py`
  - `experiments/product_pressure_independence.py`
  - `experiments/product_pressure_uniform_bound.py`
  - `experiments/product_valuation_pressure.py`

### 二点前缀/奇异平均实验

- 数量：3
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/two_point_prefix_decomposition.py`
  - `experiments/two_point_prefix_error.py`
  - `experiments/two_point_singular_average.py`

### 候选坏段/半素数实验

- 数量：2
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/candidate_semiprime_bad_segments.py`
  - `experiments/candidate_semiprime_ratio_scan.py`

### 其他探索实验

- 数量：28
- 建议：低优先级，先确认是否仍有保留价值。
  - `experiments/bad_segment_candidate_pattern.py`
  - `experiments/certificate_chain_profile.py`
  - `experiments/certificate_collision_graph_scan.py`
  - `experiments/column_sieve_moments.py`
  - `experiments/constraint_graph_rank_count.py`
  - `experiments/diagonal_full_certificate.py`
  - `experiments/gallagher_average_j.py`
  - `experiments/layered_sieve_loss_scan.py`
  - `experiments/layered_sieve_regression.py`
  - `experiments/multilayer_block_capacity.py`
  - `experiments/multiple_row_orbit_correlation.py`
  - `experiments/multiple_row_orbit_scan.py`
  - `experiments/multipoint_singular_series_sample.py`
  - `experiments/no_large_edge_mixed_moments.py`
  - `experiments/pair_corr_cyclic_model.py`
  - `experiments/pair_corr_singular_model.py`
  - `experiments/reusable_certificate_bound_scan.py`
  - `experiments/reusable_certificate_ratio.py`
  - `experiments/rough_candidate_category_rates.py`
  - `experiments/shared_cluster_singular_weight.py`
  - `experiments/single_hit_expected_ratio.py`
  - `experiments/single_hit_layer_profile.py`
  - `experiments/singleton_patch_summary.py`
  - `experiments/small_prime_blocking_family.py`
  - `experiments/sqrt_block_sieve_holes.py`
  - `experiments/truncated_divisor_features.py`
  - `experiments/truncated_mobius_predictor.py`
  - `experiments/truncation_parameter_balance.py`

### 刚性补洞实验

- 数量：1
- 建议：中高优先级，建议补充脚本用途说明后分组提交。
  - `experiments/rigid_patch_graph_profile.py`

### 半素数层实验

- 数量：1
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/semiprime_ratio_by_C.py`

### 危险列/低阶 character 谱实验

- 数量：3
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/danger_column_character_spectrum.py`
  - `experiments/danger_column_spectrum_energy.py`
  - `experiments/danger_low_order_characters.py`

### 同步/异步斜线实验

- 数量：2
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/sync_async_line_decomposition.py`
  - `experiments/sync_strength_correlation.py`

### 四点 cumulant/四阶矩实验

- 数量：5
- 建议：中高优先级，建议补充脚本用途说明后分组提交。
  - `experiments/four_point_connected_cumulant_grid.py`
  - `experiments/four_point_cumulant_sample.py`
  - `experiments/four_point_gallagher_cancellation.py`
  - `experiments/four_point_local_cumulant.py`
  - `experiments/four_point_partition_mobius.py`

### 四阶矩/核投影实验

- 数量：7
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/fourth_easy_patterns.py`
  - `experiments/fourth_hard_patterns_sample.py`
  - `experiments/fourth_kernel_projection.py`
  - `experiments/fourth_kernel_projection_exact.py`
  - `experiments/fourth_moment_pattern_decomp.py`
  - `experiments/fourth_moment_pattern_sample.py`
  - `experiments/fourth_pairing_decomposition.py`

### 因子层/大因子实验

- 数量：7
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/bad_segment_factor_shell.py`
  - `experiments/fixed_large_factor_small_sieve_uniformity.py`
  - `experiments/large_factor_block_capacity.py`
  - `experiments/large_factor_exclusion.py`
  - `experiments/large_factor_reuse_graph.py`
  - `experiments/multifactor_chain_graph_scan.py`
  - `experiments/singleton_patch_factor_profile.py`

### 安全间隙实验

- 数量：4
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/safety_gap_by_H_bucket.py`
  - `experiments/safety_gap_component_by_H.py`
  - `experiments/safety_gap_component_ratios.py`
  - `experiments/safety_gap_ratio_scan.py`

### 尾部相关实验

- 数量：2
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/tail_correlation_ratio_scan.py`
  - `experiments/tail_ratio_fit_summary.py`

### 局部窗口/局部矩/局部振荡实验

- 数量：16
- 建议：中高优先级，建议补充脚本用途说明后分组提交。
  - `experiments/local_D_cov_decomposition.py`
  - `experiments/local_D_high_moments.py`
  - `experiments/local_H_high_moments.py`
  - `experiments/local_RU_high_moments.py`
  - `experiments/local_S_RS_variance.py`
  - `experiments/local_S_pair_contribution.py`
  - `experiments/local_S_pair_structure.py`
  - `experiments/local_T_high_moments.py`
  - `experiments/local_cross_cumulant_scan.py`
  - `experiments/local_factor_rank_decay.py`
  - `experiments/local_high_threshold_margin.py`
  - `experiments/local_oscillation_lemma_scan.py`
  - `experiments/local_partition_connected_factor.py`
  - `experiments/local_prime_candidate_moments.py`
  - `experiments/local_semiprime_gap_moments.py`
  - `experiments/local_variance_pair_model.py`

### 方差分解/奇异级数实验

- 数量：2
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/variance_by_difference_contrib.py`
  - `experiments/variance_singular_series_check.py`

### 有限周期/有限形状验证

- 数量：3
- 建议：优先审查，可作为验证工具提交。
  - `experiments/finite_period_projection_identity.py`
  - `experiments/finite_shape_blocking_enum.py`
  - `experiments/verify_finite_p_grid.py`

### 筛余分布/谱/矩实验

- 数量：12
- 建议：中高优先级，建议补充脚本用途说明后分组提交。
  - `experiments/sieve_pair_corr_factor_profile.py`
  - `experiments/sieve_remainder_additive_spectrum.py`
  - `experiments/sieve_remainder_constant_scan.py`
  - `experiments/sieve_remainder_distribution.py`
  - `experiments/sieve_remainder_fourth_moment.py`
  - `experiments/sieve_remainder_high_moments.py`
  - `experiments/sieve_remainder_moment_margin.py`
  - `experiments/sieve_remainder_multiplicative_spectrum.py`
  - `experiments/sieve_remainder_pair_correlation.py`
  - `experiments/sieve_remainder_pair_moment.py`
  - `experiments/sieve_remainder_spectrum_energy.py`
  - `experiments/sieve_remainder_tail_fit.py`

### 纯同余/折链实验

- 数量：3
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/pure_congruence_hall.py`
  - `experiments/pure_s2_fold_chain_rate.py`
  - `experiments/pure_s2_fold_chain_scan.py`

### 补洞/Hall 实验

- 数量：2
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/patch_hall_bipartite.py`
  - `experiments/patch_hall_summary.py`

### 骨架/rank 实验

- 数量：1
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/skeleton_rank_check.py`

### 高阈值列场/边际实验

- 数量：5
- 建议：中优先级，建议按对应论文小节整理后提交。
  - `experiments/high_threshold_count_bound.py`
  - `experiments/high_threshold_margin_fast.py`
  - `experiments/high_threshold_margin_multi.py`
  - `experiments/high_threshold_margin_scan.py`
  - `experiments/high_threshold_semiprime_tail.py`

## 建议提交策略

1. 先提交可复现实验入口，例如 `experiments/verify_finite_p_grid.py` 与有限周期验证类。
2. 再按主题分批提交：局部矩/筛余谱/cumulant/半素数层/补洞实验。
3. 对探索性脚本补充顶部中文注释：实验目的、输入参数、输出解释。
4. 暂不提交用途不清或重复脚本，避免仓库膨胀。
