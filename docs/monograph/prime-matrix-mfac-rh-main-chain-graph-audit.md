# MFAC RH 主链依赖图审计

- 模块总数：`19`
- 最短阻断路径：`W1 → W2`
- `rh_chain_closed=false`
- `rh_proved=false`

## 义务节点

| 节点 | 状态 | 支持模块 | 阻断理由 |
| --- | --- | --- | --- |
| `W0` | `conditional` | `actual_lcm_gram_energy, actual_record_constructor, primitive_normalization_underdetermination, rough_cofactor_mobius_signed_transport, semiprime_local_naturality_factorization, semiprime_triad_dispatch, square_base_seed_binding` | `conditional_dependency_present` |
| `W1` | `conditional` | `actual_lcm_gram_energy, centered_divisibility_covariance, lcm_offconstant_projection_circularity, mertens_conditional_l2_upper, mobius_tail_l2, truncated_mobius_log_coercivity, uniform_offconstant_coercivity` | `conditional_dependency_present` |
| `W2` | `not_started` | `none` | `no_registered_support_module` |
| `W3` | `conditional` | `global_free_mellin_mode_no_go, mertens_randomness_contraction` | `conditional_dependency_present` |
| `W4` | `not_started` | `none` | `no_registered_support_module` |
| `W5` | `not_started` | `none` | `no_registered_support_module` |

## 主链边

| 边 | 状态 | 禁止输入 |
| --- | --- | --- |
| `W0 → W1` | `unproved` | `RH, zeta_zero, zero_free_region, Mellin` |
| `W1 → W2` | `unproved` | `RH, zeta_zero, zero_free_region, Mellin` |
| `W2 → W3` | `unproved` | `RH, zeta_zero, zero_free_region, Mellin` |
| `W3 → W4` | `unproved` | `RH, zeta_zero, zero_free_region, Mellin` |
| `W4 → W5` | `unproved` | `RH, zeta_zero, zero_free_region, Mellin` |
| `W5 → RH` | `unproved` | `RH, zeta_zero, zero_free_region, Mellin` |

## 循环与不足边

- `C1`：Chebyshev_error → W0/W2
- `C2`：Mellin_norm → W2
- `C3`：zero_free_region/zeta_zero → W3/W4
- `C4`：RH → W1--W5
- `C5`：finite_profile → W1/W3/W4
- `C6`：free_multiplicative_model → W3
- `C7`：Mertens/PNT cancellation → W1 tail L2

## 模块角色

| 模块 | 库存分类 | 预注册角色 |
| --- | --- | --- |
| `actual_lcm_gram_energy` | `open_or_unresolved` | `W0:forward_obligation, W1:forward_obligation` |
| `actual_record_constructor` | `open_or_unresolved` | `W0:forward_obligation, C1:cycle_detected` |
| `centered_divisibility_covariance` | `open_or_unresolved` | `W1:forward_obligation, C1:cycle_detected` |
| `colored_divisor_word_transport` | `open_or_unresolved` | `no_direct_rh_role:no_direct_rh_role` |
| `global_free_mellin_mode_no_go` | `open_or_unresolved` | `C6:insufficient_not_cycle, W3:forward_obligation` |
| `lcm_offconstant_projection_circularity` | `open_or_unresolved` | `C1:cycle_detected, W1:forward_obligation` |
| `mertens_conditional_l2_upper` | `conditional_or_external_dependency` | `W1:conditional_dependency, C7:conditional_dependency` |
| `mertens_randomness_contraction` | `open_or_unresolved` | `W3:conditional_dependency, C7:conditional_dependency` |
| `mobius_tail_l2` | `open_or_unresolved` | `W1:forward_obligation, C7:conditional_dependency` |
| `orientation_provenance_no_go` | `open_or_unresolved` | `C1:cycle_detected, no_direct_rh_role:no_direct_rh_role` |
| `primitive_normalization_underdetermination` | `open_or_unresolved` | `W0:forward_obligation, no_direct_rh_role:no_direct_rh_role` |
| `project_inventory` | `missing_or_unreadable_certificate` | `no_direct_rh_role:no_direct_rh_role` |
| `registration_hash` | `open_or_unresolved` | `no_direct_rh_role:no_direct_rh_role` |
| `rough_cofactor_mobius_signed_transport` | `open_or_unresolved` | `W0:forward_obligation, no_direct_rh_role:no_direct_rh_role` |
| `semiprime_local_naturality_factorization` | `conditional_or_external_dependency` | `W0:conditional_dependency, no_direct_rh_role:no_direct_rh_role` |
| `semiprime_triad_dispatch` | `open_or_unresolved` | `W0:forward_obligation, no_direct_rh_role:no_direct_rh_role` |
| `square_base_seed_binding` | `open_or_unresolved` | `W0:forward_obligation, no_direct_rh_role:no_direct_rh_role` |
| `truncated_mobius_log_coercivity` | `open_or_unresolved` | `W1:forward_obligation, C5:insufficient_not_cycle` |
| `uniform_offconstant_coercivity` | `open_or_unresolved` | `W1:forward_obligation, C5:insufficient_not_cycle` |

本图只组合阶段 1 库存与人工预注册角色，不运行模块；不构成 RH 证明。
