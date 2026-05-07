# SN-2 正二进带结构审计

**状态：** `sn2_band_structure_audit_not_a_proof`

## 参数

- `p_list`: `[5003, 10007, 20011, 50021, 100003, 200003]`
- `alpha`: `0.43`
- `y_factor`: `4.0`
- `tail_factor`: `10.0`
- `top_n`: `8`
- `q_window_scale`: `1.0`
- `qwindow_excess_share`: `0.5`
- `phase_share`: `0.35`

## 总路由

- `global_route_counts`: `{'sae_short_q_window_candidate': 131, 'distributed_band_large_sieve_candidate': 32}`

## 总表

| P | cutoff | y_limit | qwin width | routes | max band+/R | min band margin |
|---:|---:|---:|---:|---|---:|---:|
| 5003 | 38 | 152 | 71 | `{'sae_short_q_window_candidate': 10, 'distributed_band_large_sieve_candidate': 3}` | 0.176536 | 40.980801 |
| 10007 | 52 | 208 | 100 | `{'distributed_band_large_sieve_candidate': 5, 'sae_short_q_window_candidate': 22}` | 0.248700 | 87.798324 |
| 20011 | 70 | 280 | 141 | `{'distributed_band_large_sieve_candidate': 5, 'sae_short_q_window_candidate': 22}` | 0.244794 | 110.833866 |
| 50021 | 104 | 416 | 224 | `{'sae_short_q_window_candidate': 18, 'distributed_band_large_sieve_candidate': 7}` | 0.103856 | 438.862450 |
| 100003 | 141 | 564 | 316 | `{'sae_short_q_window_candidate': 30, 'distributed_band_large_sieve_candidate': 10}` | 0.117122 | 730.817646 |
| 200003 | 190 | 760 | 447 | `{'sae_short_q_window_candidate': 29, 'distributed_band_large_sieve_candidate': 2}` | 0.054697 | 1337.735998 |

## P=5003

- `y=41, margin=46, T/S=0.937922, band+/R=0.176536, band_margin=40.981`
  - `band=[2y,4y), E=5.410, A/M=1.059063, qwin_E_share=0.758715, qmod30=0.164948, dmod30=0.164948, labels=['sae_short_q_window_candidate']`
  - `band=[8y,16y), E=3.376, A/M=1.053061, qwin_E_share=1.211847, qmod30=0.179104, dmod30=0.194030, labels=['sae_short_q_window_candidate']`
- `y=37, margin=57, T/S=0.923592, band+/R=0.116725, band_margin=52.923`
  - `band=[4y,8y), E=6.994, A/M=1.070640, qwin_E_share=0.533310, qmod30=0.160377, dmod30=0.179245, labels=['sae_short_q_window_candidate']`
- `y=34, margin=58, T/S=0.922148, band+/R=0.132524, band_margin=55.321`
  - `band=[2y,4y), E=8.451, A/M=1.092316, qwin_E_share=0.293439, qmod30=0.140000, dmod30=0.150000, labels=['distributed_band_large_sieve_candidate']`
- `y=39, margin=60, T/S=0.919679, band+/R=0.109793, band_margin=54.912`
  - `band=[1y,2y), E=2.572, A/M=1.025614, qwin_E_share=1.242278, qmod30=0.155340, dmod30=0.165049, labels=['sae_short_q_window_candidate']`
  - `band=[2y,4y), E=2.444, A/M=1.026689, qwin_E_share=2.219776, qmod30=0.148936, dmod30=0.159574, labels=['sae_short_q_window_candidate']`
  - `band=[8y,16y), E=1.757, A/M=1.027343, qwin_E_share=1.549658, qmod30=0.181818, dmod30=0.242424, labels=['sae_short_q_window_candidate']`

## P=10007

- `y=46, margin=98, T/S=0.929446, band+/R=0.186012, band_margin=87.798`
  - `band=[4y,8y), E=14.254, A/M=1.090360, qwin_E_share=0.359951, qmod30=0.151163, dmod30=0.151163, labels=['distributed_band_large_sieve_candidate']`
  - `band=[2y,4y), E=3.726, A/M=1.022274, qwin_E_share=1.399085, qmod30=0.146199, dmod30=0.163743, labels=['sae_short_q_window_candidate']`
  - `band=[1y,2y), E=2.084, A/M=1.013992, qwin_E_share=1.344737, qmod30=0.145695, dmod30=0.158940, labels=['sae_short_q_window_candidate']`
- `y=63, margin=100, T/S=0.927693, band+/R=0.247862, band_margin=91.647`
  - `band=[1y,2y), E=10.899, A/M=1.071191, qwin_E_share=0.402142, qmod30=0.146341, dmod30=0.164634, labels=['distributed_band_large_sieve_candidate']`
  - `band=[8y,16y), E=10.116, A/M=1.068871, qwin_E_share=0.730027, qmod30=0.152866, dmod30=0.203822, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=8.020, A/M=1.195714, qwin_E_share=0.702217, qmod30=0.204082, dmod30=0.183673, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=1.166, A/M=1.007530, qwin_E_share=5.784101, qmod30=0.160256, dmod30=0.160256, labels=['sae_short_q_window_candidate']`
- `y=51, margin=106, T/S=0.923796, band+/R=0.104950, band_margin=96.594`
  - `band=[1y,2y), E=6.932, A/M=1.040524, qwin_E_share=0.546310, qmod30=0.134831, dmod30=0.162921, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=2.931, A/M=1.073156, qwin_E_share=1.346159, qmod30=0.209302, dmod30=0.162791, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=1.463, A/M=1.009716, qwin_E_share=2.398938, qmod30=0.164474, dmod30=0.144737, labels=['sae_short_q_window_candidate']`
- `y=54, margin=108, T/S=0.922302, band+/R=0.090249, band_margin=103.627`
  - `band=[2y,4y), E=5.136, A/M=1.034273, qwin_E_share=0.790471, qmod30=0.148387, dmod30=0.167742, labels=['sae_short_q_window_candidate']`
  - `band=[8y,16y), E=2.773, A/M=1.017308, qwin_E_share=1.657581, qmod30=0.159509, dmod30=0.171779, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=1.309, A/M=1.008353, qwin_E_share=3.396906, qmod30=0.139241, dmod30=0.151899, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=1.062, A/M=1.027987, qwin_E_share=1.059639, qmod30=0.205128, dmod30=0.179487, labels=['sae_short_q_window_candidate']`

## P=20011

- `y=71, margin=112, T/S=0.956857, band+/R=0.244794, band_margin=110.834`
  - `band=[1y,2y), E=18.397, A/M=1.058293, qwin_E_share=0.255866, qmod30=0.137725, dmod30=0.146707, labels=['distributed_band_large_sieve_candidate']`
  - `band=[4y,8y), E=10.770, A/M=1.042868, qwin_E_share=0.594198, qmod30=0.141221, dmod30=0.152672, labels=['sae_short_q_window_candidate']`
  - `band=[2y,4y), E=6.759, A/M=1.022970, qwin_E_share=0.546964, qmod30=0.139535, dmod30=0.146179, labels=['sae_short_q_window_candidate']`
- `y=66, margin=190, T/S=0.926641, band+/R=0.076870, band_margin=173.861`
  - `band=[2y,4y), E=12.845, A/M=1.045046, qwin_E_share=0.440785, qmod30=0.134228, dmod30=0.140940, labels=['distributed_band_large_sieve_candidate']`
  - `band=[1y,2y), E=1.632, A/M=1.005701, qwin_E_share=1.589399, qmod30=0.159722, dmod30=0.131944, labels=['sae_short_q_window_candidate']`
- `y=62, margin=191, T/S=0.926169, band+/R=0.100492, band_margin=183.831`
  - `band=[2y,4y), E=8.449, A/M=1.028780, qwin_E_share=0.616985, qmod30=0.132450, dmod30=0.152318, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=5.654, A/M=1.024336, qwin_E_share=1.783526, qmod30=0.151261, dmod30=0.168067, labels=['sae_short_q_window_candidate']`
  - `band=[1y,2y), E=3.567, A/M=1.014021, qwin_E_share=1.061702, qmod30=0.151163, dmod30=0.139535, labels=['sae_short_q_window_candidate']`
  - `band=[8y,16y), E=2.867, A/M=1.010460, qwin_E_share=3.058312, qmod30=0.158845, dmod30=0.148014, labels=['sae_short_q_window_candidate']`
- `y=80, margin=198, T/S=0.923345, band+/R=0.088489, band_margin=198.000`
  - `band=[2y,4y), E=13.754, A/M=1.048219, qwin_E_share=0.290015, qmod30=0.143813, dmod30=0.133779, labels=['distributed_band_large_sieve_candidate']`
  - `band=[16y,32y), E=2.552, A/M=1.011522, qwin_E_share=3.322421, qmod30=0.142857, dmod30=0.142857, labels=['sae_short_q_window_candidate']`
  - `band=[1y,2y), E=1.794, A/M=1.006567, qwin_E_share=2.074446, qmod30=0.145455, dmod30=0.145455, labels=['sae_short_q_window_candidate']`
  - `band=[8y,16y), E=0.778, A/M=1.002888, qwin_E_share=7.189217, qmod30=0.144444, dmod30=0.140741, labels=['sae_short_q_window_candidate']`

## P=50021

- `y=104, margin=484, T/S=0.917743, band+/R=0.026450, band_margin=451.311`
  - `band=[8y,16y), E=9.492, A/M=1.016493, qwin_E_share=0.770415, qmod30=0.133333, dmod30=0.136752, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=2.770, A/M=1.004599, qwin_E_share=1.604183, qmod30=0.148760, dmod30=0.140496, labels=['sae_short_q_window_candidate']`
- `y=128, margin=486, T/S=0.917599, band+/R=0.103856, band_margin=438.862`
  - `band=[1y,2y), E=24.341, A/M=1.040457, qwin_E_share=0.331184, qmod30=0.148562, dmod30=0.148562, labels=['distributed_band_large_sieve_candidate']`
  - `band=[2y,4y), E=16.112, A/M=1.026903, qwin_E_share=0.380586, qmod30=0.134959, dmod30=0.149593, labels=['distributed_band_large_sieve_candidate']`
  - `band=[4y,8y), E=10.407, A/M=1.018632, qwin_E_share=0.399582, qmod30=0.133568, dmod30=0.133568, labels=['distributed_band_large_sieve_candidate']`
- `y=107, margin=489, T/S=0.917048, band+/R=0.031273, band_margin=450.578`
  - `band=[16y,32y), E=8.391, A/M=1.014888, qwin_E_share=1.731653, qmod30=0.143357, dmod30=0.141608, labels=['sae_short_q_window_candidate']`
  - `band=[8y,16y), E=6.155, A/M=1.010560, qwin_E_share=1.131728, qmod30=0.140917, dmod30=0.132428, labels=['sae_short_q_window_candidate']`
- `y=101, margin=491, T/S=0.916610, band+/R=0.051700, band_margin=470.697`
  - `band=[8y,16y), E=12.203, A/M=1.020413, qwin_E_share=0.794888, qmod30=0.145902, dmod30=0.140984, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=8.581, A/M=1.015177, qwin_E_share=1.340004, qmod30=0.141115, dmod30=0.149826, labels=['sae_short_q_window_candidate']`
  - `band=[32y,64y), E=2.883, A/M=1.008501, qwin_E_share=1.994934, qmod30=0.154971, dmod30=0.140351, labels=['sae_short_q_window_candidate']`
  - `band=[2y,4y), E=1.995, A/M=1.003470, qwin_E_share=2.649243, qmod30=0.136915, dmod30=0.135182, labels=['sae_short_q_window_candidate']`

## P=100003

- `y=147, margin=777, T/S=0.930176, band+/R=0.090712, band_margin=730.818`
  - `band=[64y,128y), E=24.883, A/M=1.164662, qwin_E_share=1.000000, qmod30=0.187500, dmod30=0.142045, labels=['sae_short_q_window_candidate']`
  - `band=[1y,2y), E=18.986, A/M=1.015928, qwin_E_share=0.355882, qmod30=0.130471, dmod30=0.132122, labels=['distributed_band_large_sieve_candidate']`
  - `band=[2y,4y), E=12.105, A/M=1.011962, qwin_E_share=0.492161, qmod30=0.134766, dmod30=0.137695, labels=['distributed_band_large_sieve_candidate']`
  - `band=[4y,8y), E=9.280, A/M=1.008857, qwin_E_share=0.819678, qmod30=0.136235, dmod30=0.136235, labels=['sae_short_q_window_candidate']`
- `y=145, margin=795, T/S=0.928597, band+/R=0.117122, band_margin=761.929`
  - `band=[8y,16y), E=30.948, A/M=1.030550, qwin_E_share=0.335579, qmod30=0.135057, dmod30=0.133142, labels=['distributed_band_large_sieve_candidate']`
  - `band=[32y,64y), E=29.448, A/M=1.028940, qwin_E_share=1.013748, qmod30=0.140401, dmod30=0.133715, labels=['sae_short_q_window_candidate']`
  - `band=[64y,128y), E=17.348, A/M=1.114390, qwin_E_share=1.000000, qmod30=0.189349, dmod30=0.153846, labels=['sae_short_q_window_candidate']`
  - `band=[2y,4y), E=15.024, A/M=1.014615, qwin_E_share=0.467871, qmod30=0.135187, dmod30=0.133269, labels=['distributed_band_large_sieve_candidate']`
- `y=131, margin=818, T/S=0.926591, band+/R=0.096566, band_margin=810.647`
  - `band=[4y,8y), E=23.087, A/M=1.022461, qwin_E_share=0.412771, qmod30=0.139867, dmod30=0.134158, labels=['distributed_band_large_sieve_candidate']`
  - `band=[1y,2y), E=23.079, A/M=1.023819, qwin_E_share=0.281580, qmod30=0.134073, dmod30=0.140121, labels=['distributed_band_large_sieve_candidate']`
  - `band=[64y,128y), E=19.254, A/M=1.127725, qwin_E_share=1.000000, qmod30=0.182353, dmod30=0.152941, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=18.487, A/M=1.018098, qwin_E_share=1.071678, qmod30=0.139423, dmod30=0.131731, labels=['sae_short_q_window_candidate']`
- `y=150, margin=830, T/S=0.925494, band+/R=0.078405, band_margin=814.589`
  - `band=[64y,128y), E=19.332, A/M=1.130913, qwin_E_share=1.000000, qmod30=0.191617, dmod30=0.161677, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=16.030, A/M=1.016095, qwin_E_share=0.664006, qmod30=0.134387, dmod30=0.135375, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=14.402, A/M=1.013854, qwin_E_share=0.528597, qmod30=0.136622, dmod30=0.135674, labels=['sae_short_q_window_candidate']`
  - `band=[1y,2y), E=14.354, A/M=1.012684, qwin_E_share=0.423365, qmod30=0.132635, dmod30=0.136126, labels=['distributed_band_large_sieve_candidate']`

## P=200003

- `y=185, margin=1389, T/S=0.934447, band+/R=0.017032, band_margin=1378.518`
  - `band=[2y,4y), E=11.427, A/M=1.005829, qwin_E_share=0.631007, qmod30=0.129310, dmod30=0.130832, labels=['sae_short_q_window_candidate']`
  - `band=[16y,32y), E=5.946, A/M=1.003281, qwin_E_share=2.232445, qmod30=0.134763, dmod30=0.132013, labels=['sae_short_q_window_candidate']`
  - `band=[32y,64y), E=3.752, A/M=1.002078, qwin_E_share=3.087591, qmod30=0.132670, dmod30=0.135987, labels=['sae_short_q_window_candidate']`
  - `band=[8y,16y), E=2.146, A/M=1.001152, qwin_E_share=4.648522, qmod30=0.137265, dmod30=0.135121, labels=['sae_short_q_window_candidate']`
- `y=190, margin=1422, T/S=0.932823, band+/R=0.038296, band_margin=1337.736`
  - `band=[16y,32y), E=13.698, A/M=1.007583, qwin_E_share=1.340422, qmod30=0.132418, dmod30=0.137363, labels=['sae_short_q_window_candidate']`
  - `band=[2y,4y), E=12.705, A/M=1.006558, qwin_E_share=0.776037, qmod30=0.133846, dmod30=0.132821, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=12.365, A/M=1.006671, qwin_E_share=0.663871, qmod30=0.137728, dmod30=0.130225, labels=['sae_short_q_window_candidate']`
  - `band=[32y,64y), E=8.776, A/M=1.004853, qwin_E_share=3.333311, qmod30=0.141992, dmod30=0.137039, labels=['sae_short_q_window_candidate']`
- `y=171, margin=1456, T/S=0.931236, band+/R=0.054697, band_margin=1421.685`
  - `band=[16y,32y), E=26.788, A/M=1.014814, qwin_E_share=0.588270, qmod30=0.143869, dmod30=0.134605, labels=['sae_short_q_window_candidate']`
  - `band=[32y,64y), E=18.723, A/M=1.010152, qwin_E_share=1.087110, qmod30=0.140633, dmod30=0.139560, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=18.298, A/M=1.009941, qwin_E_share=0.725172, qmod30=0.136095, dmod30=0.132329, labels=['sae_short_q_window_candidate']`
  - `band=[2y,4y), E=11.954, A/M=1.005862, qwin_E_share=0.657840, qmod30=0.132618, dmod30=0.132131, labels=['sae_short_q_window_candidate']`
- `y=184, margin=1465, T/S=0.930903, band+/R=0.028328, band_margin=1416.535`
  - `band=[1y,2y), E=17.988, A/M=1.009094, qwin_E_share=0.510650, qmod30=0.130261, dmod30=0.129760, labels=['sae_short_q_window_candidate']`
  - `band=[4y,8y), E=11.680, A/M=1.006258, qwin_E_share=0.830421, qmod30=0.132588, dmod30=0.129925, labels=['sae_short_q_window_candidate']`
  - `band=[2y,4y), E=11.630, A/M=1.006003, qwin_E_share=0.590340, qmod30=0.130323, dmod30=0.132376, labels=['sae_short_q_window_candidate']`

## 解释

该审计只做结构定位：若正二进带的最大 q 短窗正超额承担比例过高，则进入 `SAE`；若 `q mod 30` 或 `d mod 30` 峰过高，则进入 `PDEC/ColumnCRT`；否则登记为 `DistributedBandLargeSieve` 候选。

正式证明目标不是这些阈值本身，而是证明分散候选可由带级大筛吸收；若吸收失败，则失败会被上述短窗或相位出口捕获。
