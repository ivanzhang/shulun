# R1b 带权坏层吸收复核

**状态：** `R1b_reduced_to_existing_DBA_A3_A4_A5_budget_acceptance`

4.3.10f 给出坏层 singular factor 的逐点支配：分别由 Rankin/divisor、步长频率、低体积和 C_poly 标签预算控制。因此 R1b 不引入新坏层类型；剩余义务是接受既有 DBA-A3/A4/A5 加权预算在 singular-factor 口径下适用。

## 分层支配
### B1_denominator_reciprocity_ramification_jacobian_rank
- 坏层：分母、CRT/reciprocity、ramification、Jacobian、四点 rank
- 支配权：`sum_{q in Q_bad} 1/q`
- 预算：DBA Rankin/divisor + A2 fixed height + A5 B2/KS margins
- 状态：`covered_by_DBA_A1_A2_A5`

### B2_step_frequency_resonance
- 坏层：q|h,q|t,q|mU,q|mT,q|m,q|d,q|mdh
- 支配权：`1/q + 1/T`
- 预算：A3 step/frequency budget; 1/q enters Rankin, 1/T enters B4 margin
- 状态：`covered_by_A3_A5`

### B3_layering_endpoint_low_volume
- 坏层：短弧层化、dyadic 端点、低体积盒、coarea 切片端点
- 支配权：`1_low log^(C_L+C_KS) P`
- 预算：A4 low-volume/layering budget + C_star/KS margins
- 状态：`covered_by_A4_A5`

### B4_multi_skeleton_bad_prime_repetition
- 坏层：多 skeleton 坏素重复计数
- 支配权：`Rankin/divisor budget times C_poly label complexity`
- 预算：rankin_divisor_budget + C_poly absorption scan
- 状态：`covered_by_rankin_Cpoly`
