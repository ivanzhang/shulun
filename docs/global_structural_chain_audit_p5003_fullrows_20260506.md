# 行命题全局结构链路由审计

**状态：** `global_structural_chain_audit_not_a_proof`

## 参数

- `p_list`: `[5003]`
- `alpha`: `0.43`
- `y_factor`: `999.0`
- `tail_factor`: `10.0`
- `top_n`: `16`
- `near_hit_ratio`: `0.9`
- `m_anchor_share`: `0.1`
- `band_anchor_share`: `0.6`
- `phase_share`: `0.4`

## 总路由

- `global_route_counts`: `{'capacity_closed': 16}`
- `global_risk_flag_counts`: `{'near_capacity_boundary': 9, 'tail_positive_excess': 10}`
- `max_m_share=0.050898 at P=5003,y=33,margin=73,T/S=0.901351`
- `max_band_share=0.333333 at P=5003,y=59,margin=78,T/S=0.894879`
- `max_qmod30_share=0.150769 at P=5003,y=58,margin=74,T/S=0.899865`
- `max_dmod30_share=0.160000 at P=5003,y=58,margin=74,T/S=0.899865`
- `max_tail_actual_over_model=1.020616 at P=5003,y=56,margin=77,T/S=0.896226`
- `max_positive_m_excess_over_required=0.732973 at P=5003,y=41,margin=46,T/S=0.937922`
- `max_positive_band_excess_over_required=0.176536 at P=5003,y=41,margin=46,T/S=0.937922`
- `min_band_positive_absorption_margin=40.980801 at P=5003,y=41,margin=46,T/S=0.937922`

## 总表

| P | cutoff | y_limit | routes | risk flags | min margin | min margin/sqrt | min C_allow | max tail/model |
|---:|---:|---:|---|---|---:|---:|---:|---:|
| 5003 | 38 | 5004 | `{'capacity_closed': 16}` | `{'near_capacity_boundary': 9, 'tail_positive_excess': 10}` | 46 | 1.689852 | 1.141288 | 1.020616 |

## 集中峰诊断

- `P=5003`: max_m_share=0.050898, max_band_share=0.333333, max_qmod30_share=0.150769, max_dmod30_share=0.160000

## P=5003

最强风险行：

- `y=41, S=741, T=695, margin=46, T/S=0.937922, tail/model=1.010693, C_allow=1.141288, self_margin=46, E/R=3.766/49.766, band_pos/R=0.177, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=157, m/y=3.829, actual=8, model=4.475, excess=3.525`
  - top_band: `[1y,2y), share=0.303371, actual/model=0.999266`
- `y=37, S=746, T=689, margin=57, T/S=0.923592, tail/model=1.008453, C_allow=1.173631, self_margin=57, E/R=2.917/59.917, band_pos/R=0.117, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=113, m/y=3.054, actual=9, model=6.103, excess=2.897`
  - top_band: `[4y,8y), share=0.304598, actual/model=1.070640`
- `y=34, S=745, T=687, margin=58, T/S=0.922148, tail/model=1.017169, C_allow=1.189672, self_margin=58, E/R=5.773/63.773, band_pos/R=0.133, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=71, m/y=2.088, actual=12, model=9.030, excess=2.970`
  - top_band: `[2y,4y), share=0.292398, actual/model=1.092316`
- `y=39, S=747, T=687, margin=60, T/S=0.919679, tail/model=1.004822, C_allow=1.176586, self_margin=60, E/R=1.684/61.684, band_pos/R=0.110, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=149, m/y=3.821, actual=9, model=4.754, excess=4.246`
  - top_band: `[1y,2y), share=0.293447, actual/model=1.025614`
- `y=53, S=748, T=679, margin=69, T/S=0.907754, tail/model=1.017384, C_allow=1.223853, self_margin=69, E/R=5.810/74.810, band_pos/R=0.156, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=97, m/y=1.830, actual=11, model=6.460, excess=4.540`
  - top_band: `[1y,2y), share=0.317647, actual/model=1.097893`
- `y=43, S=742, T=672, margin=70, T/S=0.905660, tail/model=1.009966, C_allow=1.216082, self_margin=70, E/R=3.385/73.385, band_pos/R=0.060, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=79, m/y=1.837, actual=12, model=8.116, excess=3.884`
  - top_band: `[1y,2y), share=0.306122, actual/model=1.044030`
- `y=47, S=741, T=671, margin=70, T/S=0.905533, tail/model=0.996092, C_allow=1.204853, self_margin=70, E/R=-1.311/68.689, band_pos/R=0.108, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=47, m/y=1.000, actual=15, model=12.476, excess=2.524`
  - top_band: `[4y,8y), share=0.287425, actual/model=1.084057`
- `y=40, S=746, T=675, margin=71, T/S=0.904826, tail/model=0.981297, C_allow=1.183832, self_margin=71, E/R=-6.557/64.443, band_pos/R=0.075, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=73, m/y=1.825, actual=13, model=8.744, excess=4.256`
  - top_band: `[1y,2y), share=0.316860, actual/model=1.009885`

## 解释

`capacity_closed` 是严格门：`T_Y<S_Y` 直接推出该行存在素数洞。

若未来样本出现 `T_Y>=S_Y`，脚本不会把它当成无名失败，而会按互补因子集中、二进 `m/y` 带集中、`mod 30` 相位峰、列残基峰和递归下降候选登记命名出口。

因此该审计服务于非固定常数路线：固定常数只作诊断，正式硬点是 `Self-Normalized Tail Dichotomy + NonHit-Phase Descent + No-Cycle Defect Ledger`。
