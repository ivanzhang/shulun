# 行命题全局结构链路由审计

**状态：** `global_structural_chain_audit_not_a_proof`

## 参数

- `p_list`: `[5003, 10007, 20011, 50021, 100003, 200003]`
- `alpha`: `0.43`
- `y_factor`: `4.0`
- `tail_factor`: `10.0`
- `top_n`: `16`
- `near_hit_ratio`: `0.9`
- `m_anchor_share`: `0.1`
- `band_anchor_share`: `0.6`
- `phase_share`: `0.4`

## 总路由

- `global_route_counts`: `{'capacity_closed': 96}`
- `global_risk_flag_counts`: `{'near_capacity_boundary': 89, 'tail_positive_excess': 51}`
- `max_m_share=0.050898 at P=5003,y=33,margin=73,T/S=0.901351`
- `max_band_share=0.333333 at P=5003,y=59,margin=78,T/S=0.894879`
- `max_qmod30_share=0.150769 at P=5003,y=58,margin=74,T/S=0.899865`
- `max_dmod30_share=0.160000 at P=5003,y=58,margin=74,T/S=0.899865`
- `max_tail_actual_over_model=1.033097 at P=10007,y=63,margin=100,T/S=0.927693`
- `max_positive_m_excess_over_required=1.110155 at P=20011,y=71,margin=112,T/S=0.956857`
- `max_positive_band_excess_over_required=0.248700 at P=10007,y=75,margin=116,T/S=0.916185`
- `min_band_positive_absorption_margin=40.980801 at P=5003,y=41,margin=46,T/S=0.937922`

## 总表

| P | cutoff | y_limit | routes | risk flags | min margin | min margin/sqrt | min C_allow | max tail/model |
|---:|---:|---:|---|---|---:|---:|---:|---:|
| 5003 | 38 | 152 | `{'capacity_closed': 16}` | `{'near_capacity_boundary': 9, 'tail_positive_excess': 10}` | 46 | 1.689852 | 1.141288 | 1.020616 |
| 10007 | 52 | 208 | `{'capacity_closed': 16}` | `{'near_capacity_boundary': 16, 'tail_positive_excess': 10}` | 98 | 2.629511 | 1.157071 | 1.033097 |
| 20011 | 70 | 280 | `{'capacity_closed': 16}` | `{'near_capacity_boundary': 16, 'tail_positive_excess': 5}` | 112 | 2.198192 | 1.107340 | 1.027271 |
| 50021 | 104 | 416 | `{'capacity_closed': 16}` | `{'near_capacity_boundary': 16, 'tail_positive_excess': 6}` | 484 | 6.309705 | 1.141423 | 1.010889 |
| 100003 | 141 | 564 | `{'capacity_closed': 16}` | `{'near_capacity_boundary': 16, 'tail_positive_excess': 14}` | 777 | 7.365673 | 1.124231 | 1.013767 |
| 200003 | 190 | 760 | `{'capacity_closed': 16}` | `{'near_capacity_boundary': 16, 'tail_positive_excess': 6}` | 1389 | 9.542167 | 1.110310 | 1.006172 |

## 集中峰诊断

- `P=5003`: max_m_share=0.050898, max_band_share=0.333333, max_qmod30_share=0.150769, max_dmod30_share=0.160000
- `P=10007`: max_m_share=0.036309, max_band_share=0.284672, max_qmod30_share=0.146565, max_dmod30_share=0.148094
- `P=20011`: max_m_share=0.026178, max_band_share=0.238231, max_qmod30_share=0.140000, max_dmod30_share=0.142105
- `P=50021`: max_m_share=0.015284, max_band_share=0.198145, max_qmod30_share=0.138684, max_dmod30_share=0.137697
- `P=100003`: max_m_share=0.010348, max_band_share=0.188046, max_qmod30_share=0.132189, max_dmod30_share=0.132981
- `P=200003`: max_m_share=0.007967, max_band_share=0.164639, max_qmod30_share=0.130234, max_dmod30_share=0.130667

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

## P=10007

最强风险行：

- `y=46, S=1389, T=1291, margin=98, T/S=0.929446, tail/model=1.014629, C_allow=1.160000, self_margin=98, E/R=9.862/107.862, band_pos/R=0.186, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=353, m/y=7.674, actual=8, model=4.055, excess=3.945`
  - top_band: `[4y,8y), share=0.251462, actual/model=1.090360`
- `y=63, S=1383, T=1283, margin=100, T/S=0.927693, tail/model=1.033097, C_allow=1.184577, self_margin=100, E/R=21.849/121.849, band_pos/R=0.248, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=83, m/y=1.317, actual=20, model=13.454, excess=6.546`
  - top_band: `[1y,2y), share=0.240469, actual/model=1.071191`
- `y=51, S=1391, T=1285, margin=106, T/S=0.923796, tail/model=1.002795, C_allow=1.157071, self_margin=106, E/R=1.920/107.920, band_pos/R=0.105, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=67, m/y=1.314, actual=22, model=16.819, excess=5.181`
  - top_band: `[1y,2y), share=0.258345, actual/model=1.040524`
- `y=54, S=1390, T=1282, margin=108, T/S=0.922302, tail/model=1.008738, C_allow=1.168479, self_margin=108, E/R=5.908/113.908, band_pos/R=0.090, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=71, m/y=1.315, actual=22, model=15.697, excess=6.303`
  - top_band: `[1y,2y), share=0.244868, actual/model=0.974485`
- `y=57, S=1383, T=1275, margin=108, T/S=0.921909, tail/model=1.004086, C_allow=1.162395, self_margin=108, E/R=2.788/110.788, band_pos/R=0.092, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=97, m/y=1.702, actual=17, model=11.891, excess=5.109`
  - top_band: `[1y,2y), share=0.284672, actual/model=1.018729`
- `y=41, S=1379, T=1264, margin=115, T/S=0.916606, tail/model=1.003940, C_allow=1.178605, self_margin=115, E/R=2.594/117.594, band_pos/R=0.088, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=149, m/y=3.634, actual=13, model=8.485, excess=4.515`
  - top_band: `[4y,8y), share=0.257186, actual/model=1.054445`
- `y=75, S=1384, T=1268, margin=116, T/S=0.916185, tail/model=1.025669, C_allow=1.208430, self_margin=116, E/R=16.292/132.292, band_pos/R=0.249, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=79, m/y=1.053, actual=18, model=13.886, excess=4.114`
  - top_band: `[4y,8y), share=0.250384, actual/model=1.108046`
- `y=60, S=1396, T=1276, margin=120, T/S=0.914040, tail/model=1.008439, C_allow=1.186923, self_margin=120, E/R=5.673/125.673, band_pos/R=0.132, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=79, m/y=1.317, actual=20, model=14.239, excess=5.761`
  - top_band: `[1y,2y), share=0.269912, actual/model=1.062855`

## P=20011

最强风险行：

- `y=71, S=2596, T=2484, margin=112, T/S=0.956857, tail/model=1.025423, C_allow=1.107340, self_margin=112, E/R=34.760/146.760, band_pos/R=0.245, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=241, m/y=3.394, actual=13, model=9.576, excess=3.424`
  - top_band: `[1y,2y), share=0.238231, actual/model=1.058293`
- `y=66, S=2590, T=2400, margin=190, T/S=0.926641, tail/model=0.998768, C_allow=1.139649, self_margin=190, E/R=-1.661/188.339, band_pos/R=0.077, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=89, m/y=1.348, actual=28, model=23.462, excess=4.538`
  - top_band: `[2y,4y), share=0.221232, actual/model=1.045046`
- `y=62, S=2587, T=2396, margin=191, T/S=0.926169, tail/model=1.010002, C_allow=1.152899, self_margin=191, E/R=13.369/204.369, band_pos/R=0.100, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=163, m/y=2.629, actual=19, model=13.787, excess=5.213`
  - top_band: `[2y,4y), share=0.223704, actual/model=1.028780`
- `y=80, S=2583, T=2385, margin=198, T/S=0.923345, tail/model=1.014676, C_allow=1.165846, self_margin=198, E/R=19.222/217.222, band_pos/R=0.088, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=251, m/y=3.138, actual=13, model=9.145, excess=3.855`
  - top_band: `[2y,4y), share=0.224981, actual/model=1.048219`
- `y=68, S=2585, T=2386, margin=199, T/S=0.923017, tail/model=0.993282, C_allow=1.140026, self_margin=199, E/R=-9.110/189.890, band_pos/R=0.028, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=193, m/y=2.838, actual=16, model=11.757, excess=4.243`
  - top_band: `[2y,4y), share=0.227171, actual/model=1.014291`
- `y=77, S=2586, T=2380, margin=206, T/S=0.920340, tail/model=1.000681, C_allow=1.155674, self_margin=206, E/R=0.906/206.906, band_pos/R=0.057, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=79, m/y=1.026, actual=30, model=25.645, excess=4.355`
  - top_band: `[2y,4y), share=0.216541, actual/model=1.035788`
- `y=79, S=2599, T=2386, margin=213, T/S=0.918045, tail/model=0.999834, C_allow=1.159597, self_margin=213, E/R=-0.222/212.778, band_pos/R=0.072, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=277, m/y=3.506, actual=12, model=8.452, excess=3.548`
  - top_band: `[1y,2y), share=0.215304, actual/model=0.959047`
- `y=99, S=2596, T=2382, margin=214, T/S=0.917565, tail/model=1.027271, C_allow=1.192437, self_margin=214, E/R=35.334/249.334, band_pos/R=0.144, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=101, m/y=1.020, actual=28, model=20.053, excess=7.947`
  - top_band: `[1y,2y), share=0.221638, actual/model=0.997727`

## P=50021

最强风险行：

- `y=104, S=5884, T=5400, margin=484, T/S=0.917743, tail/model=0.993758, C_allow=1.141660, self_margin=484, E/R=-20.428/463.572, band_pos/R=0.026, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=181, m/y=1.740, actual=33, model=27.007, excess=5.993`
  - top_band: `[4y,8y), share=0.186039, actual/model=1.004599`
- `y=128, S=5898, T=5412, margin=486, T/S=0.917599, tail/model=1.001162, C_allow=1.152786, self_margin=486, E/R=3.723/489.723, band_pos/R=0.104, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=223, m/y=1.742, actual=30, model=21.838, excess=8.162`
  - top_band: `[1y,2y), share=0.195076, actual/model=1.040457`
- `y=107, S=5895, T=5406, margin=489, T/S=0.917048, tail/model=0.992740, C_allow=1.141423, self_margin=489, E/R=-23.876/465.124, band_pos/R=0.031, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=199, m/y=1.860, actual=30, model=24.631, excess=5.369`
  - top_band: `[1y,2y), share=0.188055, actual/model=0.979282`
- `y=101, S=5888, T=5397, margin=491, T/S=0.916610, tail/model=1.001644, C_allow=1.152321, self_margin=491, E/R=5.359/496.359, band_pos/R=0.052, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=149, m/y=1.475, actual=37, model=32.145, excess=4.855`
  - top_band: `[8y,16y), share=0.186887, actual/model=1.020413`
- `y=116, S=5900, T=5398, margin=502, T/S=0.914915, tail/model=1.010889, C_allow=1.167999, self_margin=502, E/R=34.793/536.793, band_pos/R=0.095, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=131, m/y=1.129, actual=44, model=35.735, excess=8.265`
  - top_band: `[2y,4y), share=0.190402, actual/model=1.005953`
- `y=111, S=5902, T=5399, margin=503, T/S=0.914775, tail/model=1.006634, C_allow=1.163153, self_margin=503, E/R=21.321/524.321, band_pos/R=0.081, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=193, m/y=1.739, actual=33, model=25.249, excess=7.751`
  - top_band: `[2y,4y), share=0.198145, actual/model=1.012966`
- `y=91, S=5890, T=5384, margin=506, T/S=0.914092, tail/model=0.998266, C_allow=1.155821, self_margin=506, E/R=-5.569/500.431, band_pos/R=0.053, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=107, m/y=1.176, actual=49, model=43.955, excess=5.045`
  - top_band: `[4y,8y), share=0.194011, actual/model=1.032012`
- `y=125, S=5905, T=5397, margin=508, T/S=0.913971, tail/model=1.002606, C_allow=1.159854, self_margin=508, E/R=8.420/516.420, band_pos/R=0.061, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=1063, m/y=8.504, actual=10, model=5.535, excess=4.465`
  - top_band: `[1y,2y), share=0.197592, actual/model=1.032802`

## P=100003

最强风险行：

- `y=147, S=11128, T=10351, margin=777, T/S=0.930176, tail/model=1.004149, C_allow=1.124777, self_margin=777, E/R=26.725/803.725, band_pos/R=0.091, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=181, m/y=1.231, actual=57, model=48.858, excess=8.142`
  - top_band: `[1y,2y), share=0.187229, actual/model=1.015928`
- `y=145, S=11134, T=10339, margin=795, T/S=0.928597, tail/model=1.010573, C_allow=1.134174, self_margin=795, E/R=68.006/863.006, band_pos/R=0.117, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=227, m/y=1.566, actual=49, model=39.791, excess=9.209`
  - top_band: `[1y,2y), share=0.175077, actual/model=0.979798`
- `y=131, S=11143, T=10325, margin=818, T/S=0.926591, tail/model=1.012492, C_allow=1.141357, self_margin=818, E/R=79.295/897.295, band_pos/R=0.097, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=229, m/y=1.748, actual=47, model=39.829, excess=7.171`
  - top_band: `[2y,4y), share=0.173642, actual/model=0.998460`
- `y=150, S=11140, T=10310, margin=830, T/S=0.925494, tail/model=1.008423, C_allow=1.138149, self_margin=830, E/R=53.891/883.891, band_pos/R=0.078, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=193, m/y=1.287, actual=55, model=46.027, excess=8.973`
  - top_band: `[1y,2y), share=0.177619, actual/model=1.012684`
- `y=135, S=11135, T=10305, margin=830, T/S=0.925460, tail/model=1.009185, C_allow=1.139312, self_margin=830, E/R=58.589/888.589, band_pos/R=0.082, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=241, m/y=1.785, actual=45, model=37.983, excess=7.017`
  - top_band: `[4y,8y), share=0.169178, actual/model=1.012252`
- `y=140, S=11106, T=10275, margin=831, T/S=0.925176, tail/model=1.004106, C_allow=1.133814, self_margin=831, E/R=26.305/857.305, band_pos/R=0.052, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=151, m/y=1.079, actual=65, model=58.004, excess=6.996`
  - top_band: `[1y,2y), share=0.170061, actual/model=0.994720`
- `y=154, S=11112, T=10278, margin=834, T/S=0.924946, tail/model=1.004949, C_allow=1.135989, self_margin=834, E/R=31.500/865.500, band_pos/R=0.061, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=241, m/y=1.565, actual=44, model=37.527, excess=6.473`
  - top_band: `[1y,2y), share=0.171357, actual/model=0.995182`
- `y=172, S=11091, T=10251, margin=840, T/S=0.924263, tail/model=1.013767, C_allow=1.147472, self_margin=840, E/R=86.491/926.491, band_pos/R=0.098, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=883, m/y=5.134, actual=19, model=11.447, excess=7.553`
  - top_band: `[2y,4y), share=0.174753, actual/model=1.024667`

## P=200003

最强风险行：

- `y=185, S=21189, T=19800, margin=1389, T/S=0.934447, tail/model=1.001067, C_allow=1.111598, self_margin=1389, E/R=13.404/1402.404, band_pos/R=0.017, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=199, m/y=1.076, actual=91, model=82.868, excess=8.132`
  - top_band: `[1y,2y), share=0.156995, actual/model=0.998892`
- `y=190, S=21168, T=19746, margin=1422, T/S=0.932823, tail/model=0.997542, C_allow=1.110310, self_margin=1422, E/R=-30.994/1391.006, band_pos/R=0.038, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=211, m/y=1.111, actual=90, model=78.373, excess=11.627`
  - top_band: `[1y,2y), share=0.164639, actual/model=1.002772`
- `y=171, S=21174, T=19718, margin=1456, T/S=0.931236, tail/model=1.003845, C_allow=1.120595, self_margin=1456, E/R=47.946/1503.946, band_pos/R=0.055, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=191, m/y=1.117, actual=94, model=86.603, excess=7.397`
  - top_band: `[2y,4y), share=0.163831, actual/model=1.005862`
- `y=184, S=21202, T=19737, margin=1465, T/S=0.930903, tail/model=0.999429, C_allow=1.116059, self_margin=1465, E/R=-7.167/1457.833, band_pos/R=0.028, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=269, m/y=1.462, actual=71, model=62.940, excess=8.060`
  - top_band: `[1y,2y), share=0.158993, actual/model=1.009094`
- `y=180, S=21211, T=19744, margin=1467, T/S=0.930838, tail/model=0.998152, C_allow=1.115155, self_margin=1467, E/R=-23.165/1443.835, band_pos/R=0.020, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=263, m/y=1.461, actual=74, model=64.375, excess=9.625`
  - top_band: `[2y,4y), share=0.154854, actual/model=1.000326`
- `y=187, S=21197, T=19722, margin=1475, T/S=0.930415, tail/model=0.997659, C_allow=1.114802, self_margin=1475, E/R=-29.479/1445.521, band_pos/R=0.006, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=587, m/y=3.139, actual=39, model=30.750, excess=8.250`
  - top_band: `[1y,2y), share=0.160962, actual/model=1.000105`
- `y=172, S=21178, T=19704, margin=1474, T/S=0.930399, tail/model=1.001692, C_allow=1.119840, self_margin=1474, E/R=21.111/1495.111, band_pos/R=0.051, route=capacity_closed, flags=['near_capacity_boundary', 'tail_positive_excess']`
  - top_m_excess: `m=191, m/y=1.110, actual=97, model=86.561, excess=10.439`
  - top_band: `[2y,4y), share=0.162839, actual/model=0.998574`
- `y=189, S=21220, T=19738, margin=1482, T/S=0.930160, tail/model=0.995005, C_allow=1.112606, self_margin=1482, E/R=-62.947/1419.053, band_pos/R=0.013, route=capacity_closed, flags=['near_capacity_boundary']`
  - top_m_excess: `m=593, m/y=3.138, actual=39, model=30.477, excess=8.523`
  - top_band: `[1y,2y), share=0.159981, actual/model=0.992959`

## 解释

`capacity_closed` 是严格门：`T_Y<S_Y` 直接推出该行存在素数洞。

若未来样本出现 `T_Y>=S_Y`，脚本不会把它当成无名失败，而会按互补因子集中、二进 `m/y` 带集中、`mod 30` 相位峰、列残基峰和递归下降候选登记命名出口。

因此该审计服务于非固定常数路线：固定常数只作诊断，正式硬点是 `Self-Normalized Tail Dichotomy + NonHit-Phase Descent + No-Cycle Defect Ledger`。
