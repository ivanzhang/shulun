# SN-3 分散正带投影残余审计

**状态：** `sn3_projection_audit_not_a_proof`

## 参数

- `p_list`: `[5003, 10007, 20011, 50021, 100003, 200003]`
- `alpha`: `0.43`
- `y_factor`: `4.0`
- `tail_factor`: `10.0`
- `top_n`: `8`
- `q_window_scale`: `1.0`
- `qwindow_excess_share`: `0.5`
- `phase_share`: `0.35`
- `centered_return_share`: `0.75`
- `w_list`: `[30, 210]`

## 全局摘要

- `distributed_candidate_count`: `32`
- `sn3_centered_route_counts`: `{'true_distributed_dls_candidate': 24, 'centered_columncrt_return': 6, 'centered_pdec_return': 2}`
- `max_excess_over_required`: `0.132524`
- `max_excess_over_sqrt_model`: `1.310464`
- `max_projection_peak_share`: `1.018659`
- `total_distributed_excess`: `561.852711`
- `total_distributed_model`: `20707.147289`

## 按 P 汇总

| P | cutoff | y_limit | count | routes | total E | total M | E^2/M | max E/R | max E/sqrt(M) | max proj peak |
|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 5003 | 38 | 152 | 3 | `{'true_distributed_dls_candidate': 3}` | 25.524887 | 278.475113 | 2.339598 | 0.132524 | 0.970917 | 0.612405 |
| 10007 | 52 | 208 | 5 | `{'true_distributed_dls_candidate': 5}` | 60.739128 | 777.260872 | 4.746465 | 0.132150 | 1.310464 | 0.693169 |
| 20011 | 70 | 280 | 5 | `{'true_distributed_dls_candidate': 4, 'centered_columncrt_return': 1}` | 71.977430 | 1358.022570 | 3.814922 | 0.125358 | 1.090000 | 0.752736 |
| 50021 | 104 | 416 | 7 | `{'true_distributed_dls_candidate': 5, 'centered_columncrt_return': 2}` | 126.166441 | 4101.833559 | 3.880696 | 0.049704 | 0.992358 | 1.018659 |
| 100003 | 141 | 564 | 10 | `{'true_distributed_dls_candidate': 6, 'centered_columncrt_return': 2, 'centered_pdec_return': 2}` | 221.177643 | 10487.822357 | 4.664414 | 0.035861 | 1.024227 | 1.015309 |
| 200003 | 190 | 760 | 2 | `{'true_distributed_dls_candidate': 1, 'centered_columncrt_return': 1}` | 56.267182 | 3703.732818 | 0.854812 | 0.026300 | 0.941647 | 0.938755 |

## 最紧候选

- `P=5003, y=34, band=[2y,4y), E=8.451, M=91.549, E/R=0.132524, E/sqrt(M)=0.883290, qwin_peak=0.293439, qmod30_peak=0.232226, dmod30_peak=0.348108, qmod210_peak=0.244008, dmod210_peak=0.244784, route=true_distributed_dls_candidate:d_mod_w/W=30/key=1/share=0.348108`
- `P=10007, y=46, band=[4y,8y), E=14.254, M=157.746, E/R=0.132150, E/sqrt(M)=1.134897, qwin_peak=0.359951, qmod30_peak=0.341961, dmod30_peak=0.375612, qmod210_peak=0.177197, dmod210_peak=0.203419, route=true_distributed_dls_candidate:d_mod_w/W=30/key=19/share=0.375612`
- `P=5003, y=53, band=[1y,2y), E=9.630, M=98.370, E/R=0.128723, E/sqrt(M)=0.970917, qwin_peak=0.293107, qmod30_peak=0.431044, dmod30_peak=0.371401, qmod210_peak=0.241796, dmod210_peak=0.232310, route=true_distributed_dls_candidate:q_mod_w/W=30/key=13/share=0.431044`
- `P=20011, y=71, band=[1y,2y), E=18.397, M=315.603, E/R=0.125358, E/sqrt(M)=1.035589, qwin_peak=0.255866, qmod30_peak=0.316906, dmod30_peak=0.511271, qmod210_peak=0.224983, dmod210_peak=0.281223, route=true_distributed_dls_candidate:d_mod_w/W=30/key=18/share=0.511271`
- `P=10007, y=75, band=[4y,8y), E=15.894, M=147.106, E/R=0.120145, E/sqrt(M)=1.310464, qwin_peak=0.450323, qmod30_peak=0.306791, dmod30_peak=0.304883, qmod210_peak=0.183154, dmod210_peak=0.116571, route=true_distributed_dls_candidate:q_window/W=None/key=16/share=0.450323`
- `P=5003, y=47, band=[4y,8y), E=7.444, M=88.556, E/R=0.108368, E/sqrt(M)=0.791011, qwin_peak=0.313716, qmod30_peak=0.456601, dmod30_peak=0.612405, qmod210_peak=0.245187, dmod210_peak=0.240358, route=true_distributed_dls_candidate:d_mod_w/W=30/key=24/share=0.612405`
- `P=10007, y=63, band=[1y,2y), E=10.899, M=153.101, E/R=0.089450, E/sqrt(M)=0.880876, qwin_peak=0.402142, qmod30_peak=0.378398, dmod30_peak=0.693169, qmod210_peak=0.233895, dmod210_peak=0.234085, route=true_distributed_dls_candidate:d_mod_w/W=30/key=14/share=0.693169`
- `P=10007, y=60, band=[1y,2y), E=10.822, M=172.178, E/R=0.086114, E/sqrt(M)=0.824761, qwin_peak=0.398027, qmod30_peak=0.409282, dmod30_peak=0.499675, qmod210_peak=0.279410, dmod210_peak=0.327784, route=true_distributed_dls_candidate:d_mod_w/W=30/key=23/share=0.499675`
- `P=20011, y=66, band=[2y,4y), E=12.845, M=285.155, E/R=0.068202, E/sqrt(M)=0.760669, qwin_peak=0.440785, qmod30_peak=0.408254, dmod30_peak=0.596269, qmod210_peak=0.313941, dmod210_peak=0.271382, route=true_distributed_dls_candidate:d_mod_w/W=30/key=29/share=0.596269`
- `P=10007, y=75, band=[1y,2y), E=8.869, M=147.131, E/R=0.067043, E/sqrt(M)=0.731201, qwin_peak=0.458424, qmod30_peak=0.570698, dmod30_peak=0.652723, qmod210_peak=0.231616, dmod210_peak=0.456294, route=true_distributed_dls_candidate:d_mod_w/W=30/key=22/share=0.652723`
- `P=20011, y=99, band=[16y,32y), E=16.090, M=217.910, E/R=0.064533, E/sqrt(M)=1.090000, qwin_peak=0.380603, qmod30_peak=0.380312, dmod30_peak=0.258202, qmod210_peak=0.242199, dmod210_peak=0.129612, route=true_distributed_dls_candidate:q_window/W=None/key=7/share=0.380603`
- `P=20011, y=80, band=[2y,4y), E=13.754, M=285.246, E/R=0.063319, E/sqrt(M)=0.814376, qwin_peak=0.290015, qmod30_peak=0.570892, dmod30_peak=0.383954, qmod210_peak=0.259608, dmod210_peak=0.442647, route=true_distributed_dls_candidate:q_mod_w/W=30/key=29/share=0.570892`

## 解释

该审计只处理 SN-2 中未触发短窗、`q mod 30`、`d mod 30` 峰的分散正带。这里进一步把模型量也投影到 `q mod W` 与 `d mod W`，因此峰值是中心化正桶峰，而不是单纯实际计数峰。

路由阈值 `centered_return_share` 只是诊断仪表：超过阈值的中心化低维峰回流到 `SAE/PDEC/ColumnCRT` 候选；低于阈值的才登记为 `true_distributed_dls_candidate`。

`max_projection_peak_share` 越小，说明低维结构越难解释该正带；剩余责任必须由 `SN3-DLS/KLS` 型分散估计吸收。若某个低维中心化峰持续升高，则它不是随机波动，而应路由到 `SAE/PDEC/ColumnCRT`。

这些数值不能替代证明；它们只给下一步可审稿输入的最紧参数和失败出口位置。
