# 第P列远尾付款常数扫描

**状态：** `tail_payment_constant_scan_not_a_proof`

## 参数

- `p_list`: `[5003, 10007, 20011, 50021, 100003, 200003]`
- `alpha`: `0.43`
- `y_factor`: `4.0`
- `tail_factor`: `10.0`
- `top_n`: `16`
- `c_tail`: `1.05`

## 总表

| P | cutoff | y_limit | min pay margin | min C allow | max actual/model | fails |
|---:|---:|---:|---:|---:|---:|---:|
| 5003 | 38 | 152 | 32.155 | 1.141288 | 1.020616 | 0 |
| 10007 | 52 | 208 | 73.566 | 1.157071 | 1.033097 | 0 |
| 20011 | 70 | 280 | 78.398 | 1.107340 | 1.027271 | 0 |
| 50021 | 104 | 416 | 299.951 | 1.141423 | 1.010889 | 0 |
| 100003 | 141 | 564 | 478.903 | 1.124231 | 1.013767 | 0 |
| 200003 | 190 | 760 | 760.506 | 1.110310 | 1.006172 | 0 |

## P=5003

付款余量最紧行：

- `y=41, S=741, T=695, tail=356, non_tail=339, T/S=0.937922, c_allow=1.141288, actual/model=1.010693, pay_margin=32.155`
- `y=37, S=746, T=689, tail=348, non_tail=341, T/S=0.923592, c_allow=1.173631, actual/model=1.008453, pay_margin=42.663`
- `y=39, S=747, T=687, tail=351, non_tail=336, T/S=0.919679, c_allow=1.176586, actual/model=1.004822, pay_margin=44.219`
- `y=40, S=746, T=675, tail=344, non_tail=331, T/S=0.904826, c_allow=1.183832, actual/model=0.981297, pay_margin=46.916`
- `y=34, S=745, T=687, tail=342, non_tail=345, T/S=0.922148, c_allow=1.189672, actual/model=1.017169, pay_margin=46.961`
- `y=47, S=741, T=671, tail=334, non_tail=337, T/S=0.905533, c_allow=1.204853, actual/model=0.996092, pay_margin=51.924`
- `y=58, S=739, T=665, tail=325, non_tail=340, T/S=0.899865, c_allow=1.210466, actual/model=0.985968, pay_margin=52.894`
- `y=43, S=742, T=672, tail=343, non_tail=329, T/S=0.905660, c_allow=1.216082, actual/model=1.009966, pay_margin=56.404`

## P=10007

付款余量最紧行：

- `y=51, S=1391, T=1285, tail=689, non_tail=596, T/S=0.923796, c_allow=1.157071, actual/model=1.002795, pay_margin=73.566`
- `y=46, S=1389, T=1291, tail=684, non_tail=607, T/S=0.929446, c_allow=1.160000, actual/model=1.014629, pay_margin=74.155`
- `y=57, S=1383, T=1275, tail=685, non_tail=590, T/S=0.921909, c_allow=1.162395, actual/model=1.004086, pay_margin=76.677`
- `y=55, S=1382, T=1258, tail=665, non_tail=593, T/S=0.910275, c_allow=1.164852, actual/model=0.981782, pay_margin=77.794`
- `y=54, S=1390, T=1282, tail=682, non_tail=600, T/S=0.922302, c_allow=1.168479, actual/model=1.008738, pay_margin=80.103`
- `y=53, S=1387, T=1250, tail=672, non_tail=578, T/S=0.901226, c_allow=1.168653, actual/model=0.970748, pay_margin=82.138`
- `y=49, S=1387, T=1256, tail=667, non_tail=589, T/S=0.905552, c_allow=1.173457, actual/model=0.980822, pay_margin=83.956`
- `y=41, S=1379, T=1264, tail=661, non_tail=603, T/S=0.916606, c_allow=1.178605, actual/model=1.003940, pay_margin=84.674`

## P=20011

付款余量最紧行：

- `y=71, S=2596, T=2484, tail=1402, non_tail=1082, T/S=0.956857, c_allow=1.107340, actual/model=1.025423, pay_margin=78.398`
- `y=66, S=2590, T=2400, tail=1347, non_tail=1053, T/S=0.926641, c_allow=1.139649, actual/model=0.998768, pay_margin=120.905`
- `y=68, S=2585, T=2386, tail=1347, non_tail=1039, T/S=0.923017, c_allow=1.140026, actual/model=0.993282, pay_margin=122.085`
- `y=73, S=2596, T=2378, tail=1320, non_tail=1058, T/S=0.916025, c_allow=1.144861, actual/model=0.982586, pay_margin=127.436`
- `y=70, S=2593, T=2353, tail=1320, non_tail=1033, T/S=0.907443, c_allow=1.147565, actual/model=0.971016, pay_margin=132.630`
- `y=62, S=2587, T=2396, tail=1350, non_tail=1046, T/S=0.926169, c_allow=1.152899, actual/model=1.010002, pay_margin=137.537`
- `y=77, S=2586, T=2380, tail=1330, non_tail=1050, T/S=0.920340, c_allow=1.155674, actual/model=1.000681, pay_margin=140.451`
- `y=79, S=2599, T=2386, tail=1333, non_tail=1053, T/S=0.918045, c_allow=1.159597, actual/model=0.999834, pay_margin=146.117`

## P=50021

付款余量最紧行：

- `y=104, S=5884, T=5400, tail=3252, non_tail=2148, T/S=0.917743, c_allow=1.141660, actual/model=0.993758, pay_margin=299.951`
- `y=107, S=5895, T=5406, tail=3265, non_tail=2141, T/S=0.917048, c_allow=1.141423, actual/model=0.992740, pay_margin=300.680`
- `y=106, S=5886, T=5357, tail=3225, non_tail=2132, T/S=0.910126, c_allow=1.144194, actual/model=0.982958, pay_margin=309.042`
- `y=103, S=5901, T=5392, tail=3232, non_tail=2160, T/S=0.913743, c_allow=1.146167, actual/model=0.990219, pay_margin=313.881`
- `y=128, S=5898, T=5412, tail=3209, non_tail=2203, T/S=0.917599, c_allow=1.152786, actual/model=1.001162, pay_margin=329.459`
- `y=101, S=5888, T=5397, tail=3264, non_tail=2133, T/S=0.916610, c_allow=1.152321, actual/model=1.001644, pay_margin=333.426`
- `y=120, S=5902, T=5394, tail=3205, non_tail=2189, T/S=0.913927, c_allow=1.155443, actual/model=0.997359, pay_margin=338.840`
- `y=91, S=5890, T=5384, tail=3206, non_tail=2178, T/S=0.914092, c_allow=1.155821, actual/model=0.998266, pay_margin=339.852`

## P=100003

付款余量最紧行：

- `y=149, S=11122, T=10277, tail=6408, non_tail=3869, T/S=0.924024, c_allow=1.124231, actual/model=0.993254, pay_margin=478.903`
- `y=147, S=11128, T=10351, tail=6468, non_tail=3883, T/S=0.930176, c_allow=1.124777, actual/model=1.004149, pay_margin=481.662`
- `y=140, S=11106, T=10275, tail=6433, non_tail=3842, T/S=0.925176, c_allow=1.133814, actual/model=1.004106, pay_margin=536.970`
- `y=145, S=11134, T=10339, tail=6500, non_tail=3839, T/S=0.928597, c_allow=1.134174, actual/model=1.010573, pay_margin=541.406`
- `y=154, S=11112, T=10278, tail=6396, non_tail=3882, T/S=0.924946, c_allow=1.135989, actual/model=1.004949, pay_margin=547.275`
- `y=150, S=11140, T=10310, tail=6452, non_tail=3858, T/S=0.925494, c_allow=1.138149, actual/model=1.008423, pay_margin=563.985`
- `y=151, S=11147, T=10236, tail=6386, non_tail=3850, T/S=0.918274, c_allow=1.138875, actual/model=0.996691, pay_margin=569.440`
- `y=135, S=11135, T=10305, tail=6437, non_tail=3868, T/S=0.925460, c_allow=1.139312, actual/model=1.009185, pay_margin=569.668`

## P=200003

付款余量最紧行：

- `y=190, S=21168, T=19746, tail=12579, non_tail=7167, T/S=0.932823, c_allow=1.110310, actual/model=0.997542, pay_margin=760.506`
- `y=185, S=21189, T=19800, tail=12580, non_tail=7220, T/S=0.934447, c_allow=1.111598, actual/model=1.001067, pay_margin=774.074`
- `y=189, S=21220, T=19738, tail=12539, non_tail=7199, T/S=0.930160, c_allow=1.112606, actual/model=0.995005, pay_margin=788.955`
- `y=187, S=21197, T=19722, tail=12562, non_tail=7160, T/S=0.930415, c_allow=1.114802, actual/model=0.997659, pay_margin=815.947`
- `y=180, S=21211, T=19744, tail=12515, non_tail=7229, T/S=0.930838, c_allow=1.115155, actual/model=0.998152, pay_margin=816.927`
- `y=184, S=21202, T=19737, tail=12554, non_tail=7183, T/S=0.930903, c_allow=1.116059, actual/model=0.999429, pay_margin=829.775`
- `y=188, S=21187, T=19667, tail=12534, non_tail=7133, T/S=0.928258, c_allow=1.116153, actual/model=0.995437, pay_margin=832.969`
- `y=183, S=21228, T=19682, tail=12472, non_tail=7210, T/S=0.927172, c_allow=1.116549, actual/model=0.993408, pay_margin=835.504`

## 结构解释

该扫描检验一个条件付款命题：若远尾满足 `tail<=C_tail*model_tail`，则 top 风险行是否已推出 `T<S`。这里 `model_tail=sum |I_m|/log(q_min)`，`C_allow=(S-non_tail)/model_tail` 是该行允许的最大远尾常数。

若 `C_tail < min C_allow` 且实际 `actual/model_tail` 也明显低于 `C_tail`，则远尾分支可被压成证明统一短素数区间上界。若某行 `C_allow` 接近实际比例，则进入 `cofactor-anchor / SAE / PDEC / ColumnCRT`。
