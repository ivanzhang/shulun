# MFAC W2→W3 实际 Mellin 传递合同审计

## 已登记输入

- 声明来源：`actual_dyadic_chebyshev_energy_bound_lemma`, `dyadic_scale_partition_lemma`, `weighted_scale_summability_lemma`, `mellin_plancherel_transfer_lemma`
- 实际误差对象：`psi_minus_identity`
- dyadic 尺度变量：`X_to_2X`
- Mellin 测度：`dt_over_t_squared`
- 半平面参数：`0.75`
- 常数依赖：`fixed_test_function_and_half_plane_parameter`

## 外部解析引理

- `actual_dyadic_chebyshev_energy_bound`：外部证明包已登记。
- `dyadic_scale_partition`：外部证明包已登记。
- `weighted_scale_summability`：外部证明包已登记。
- `mellin_plancherel_transfer`：外部证明包已登记。

## 状态边界

```text
w2_to_w3_status=assumption_chain_registered
actual_mellin_half_plane_contraction_status=unproved
w3_spectral_contraction_status=unproved
rh_proved=false
```

本证书只登记实际 dyadic 能量至 Mellin 半平面范数的外部证明包；它不证明
Chebyshev 能量界、尺度可和性、Mellin/Plancherel 传递、半平面收缩、零自由区域或 RH。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py \
  --half-plane-parameter 0.75
```
