# 第P列锚点层叠轮筛审计

**状态：** `pcolumn_anchor_wheel_field_audit_not_a_proof`

## 参数

- `p_list`: `[101, 499, 997, 2003, 5003]`
- `wheels`: `[30, 210, 2310, 30030]`
- `include_square_plus`: `True`
- `max_sieve`: `25035012`

## 总表

| P | W | rows | shift failures | min skeleton | min prime holes | max filler ratio | max anchor primes |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 101 | 30 | 101 | 0 | 26 | 7 | 0.730769 | 3 |
| 101 | 210 | 101 | 0 | 21 | 7 | 0.681818 | 3 |
| 101 | 2310 | 101 | 0 | 18 | 7 | 0.631579 | 3 |
| 101 | 30030 | 101 | 0 | 16 | 7 | 0.588235 | 3 |
| 499 | 30 | 499 | 0 | 132 | 29 | 0.781955 | 3 |
| 499 | 210 | 499 | 0 | 112 | 29 | 0.745614 | 4 |
| 499 | 2310 | 499 | 0 | 101 | 29 | 0.721154 | 4 |
| 499 | 30030 | 499 | 0 | 92 | 29 | 0.691489 | 4 |
| 997 | 30 | 997 | 0 | 265 | 54 | 0.796226 | 3 |
| 997 | 210 | 997 | 0 | 226 | 54 | 0.763158 | 4 |
| 997 | 2310 | 997 | 0 | 204 | 54 | 0.740385 | 4 |
| 997 | 30030 | 997 | 0 | 187 | 54 | 0.720207 | 4 |
| 2003 | 30 | 2003 | 0 | 533 | 113 | 0.788785 | 3 |
| 2003 | 210 | 2003 | 0 | 456 | 113 | 0.753813 | 4 |
| 2003 | 2310 | 2003 | 0 | 413 | 113 | 0.728365 | 4 |
| 2003 | 30030 | 2003 | 0 | 379 | 113 | 0.706494 | 4 |
| 5003 | 30 | 5003 | 0 | 1333 | 260 | 0.805097 | 3 |
| 5003 | 210 | 5003 | 0 | 1141 | 260 | 0.772727 | 4 |
| 5003 | 2310 | 5003 | 0 | 1037 | 260 | 0.750000 | 5 |
| 5003 | 30030 | 5003 | 0 | 955 | 260 | 0.729448 | 5 |

## P=101 W=30

- `wheel_prime_factors`: `[2, 3, 5]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `26`
- `min_prime_holes`: `7`
- `max_filler_ratio`: `0.730769`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=73, y=74, S=26, primes=7, fill=19, ratio=0.730769, anchor=[2]`

最高补洞比例行：

- `x=73, y=74, S=26, primes=7, fill=19, ratio=0.730769, anchor=[2]`

最大第P列锚因子行：

- `x=29, y=30, S=26, primes=11, fill=15, ratio=0.576923, anchor=[2, 3, 5]`
- `x=59, y=60, S=26, primes=9, fill=17, ratio=0.653846, anchor=[2, 3, 5]`
- `x=89, y=90, S=26, primes=11, fill=15, ratio=0.576923, anchor=[2, 3, 5]`

## P=101 W=210

- `wheel_prime_factors`: `[2, 3, 5, 7]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `21`
- `min_prime_holes`: `7`
- `max_filler_ratio`: `0.681818`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=73, y=74, S=22, primes=7, fill=15, ratio=0.681818, anchor=[2]`

最高补洞比例行：

- `x=73, y=74, S=22, primes=7, fill=15, ratio=0.681818, anchor=[2]`

最大第P列锚因子行：

- `x=29, y=30, S=22, primes=11, fill=11, ratio=0.500000, anchor=[2, 3, 5]`
- `x=41, y=42, S=23, primes=11, fill=12, ratio=0.521739, anchor=[2, 3, 7]`
- `x=59, y=60, S=22, primes=9, fill=13, ratio=0.590909, anchor=[2, 3, 5]`
- `x=69, y=70, S=23, primes=13, fill=10, ratio=0.434783, anchor=[2, 5, 7]`
- `x=83, y=84, S=23, primes=10, fill=13, ratio=0.565217, anchor=[2, 3, 7]`
- `x=89, y=90, S=23, primes=11, fill=12, ratio=0.521739, anchor=[2, 3, 5]`

## P=101 W=2310

- `wheel_prime_factors`: `[2, 3, 5, 7, 11]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `18`
- `min_prime_holes`: `7`
- `max_filler_ratio`: `0.631579`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=73, y=74, S=19, primes=7, fill=12, ratio=0.631579, anchor=[2]`

最高补洞比例行：

- `x=73, y=74, S=19, primes=7, fill=12, ratio=0.631579, anchor=[2]`

最大第P列锚因子行：

- `x=29, y=30, S=20, primes=11, fill=9, ratio=0.450000, anchor=[2, 3, 5]`
- `x=41, y=42, S=20, primes=11, fill=9, ratio=0.450000, anchor=[2, 3, 7]`
- `x=59, y=60, S=21, primes=9, fill=12, ratio=0.571429, anchor=[2, 3, 5]`
- `x=65, y=66, S=20, primes=11, fill=9, ratio=0.450000, anchor=[2, 3, 11]`
- `x=69, y=70, S=22, primes=13, fill=9, ratio=0.409091, anchor=[2, 5, 7]`
- `x=83, y=84, S=21, primes=10, fill=11, ratio=0.523810, anchor=[2, 3, 7]`
- `x=89, y=90, S=21, primes=11, fill=10, ratio=0.476190, anchor=[2, 3, 5]`

## P=101 W=30030

- `wheel_prime_factors`: `[2, 3, 5, 7, 11, 13]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `16`
- `min_prime_holes`: `7`
- `max_filler_ratio`: `0.588235`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=73, y=74, S=17, primes=7, fill=10, ratio=0.588235, anchor=[2]`

最高补洞比例行：

- `x=73, y=74, S=17, primes=7, fill=10, ratio=0.588235, anchor=[2]`

最大第P列锚因子行：

- `x=29, y=30, S=17, primes=11, fill=6, ratio=0.352941, anchor=[2, 3, 5]`
- `x=41, y=42, S=19, primes=11, fill=8, ratio=0.421053, anchor=[2, 3, 7]`
- `x=59, y=60, S=19, primes=9, fill=10, ratio=0.526316, anchor=[2, 3, 5]`
- `x=65, y=66, S=19, primes=11, fill=8, ratio=0.421053, anchor=[2, 3, 11]`
- `x=69, y=70, S=21, primes=13, fill=8, ratio=0.380952, anchor=[2, 5, 7]`
- `x=77, y=78, S=20, primes=10, fill=10, ratio=0.500000, anchor=[2, 3, 13]`
- `x=83, y=84, S=20, primes=10, fill=10, ratio=0.500000, anchor=[2, 3, 7]`
- `x=89, y=90, S=20, primes=11, fill=9, ratio=0.450000, anchor=[2, 3, 5]`

## P=499 W=30

- `wheel_prime_factors`: `[2, 3, 5]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `132`
- `min_prime_holes`: `29`
- `max_filler_ratio`: `0.781955`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=362, y=363, S=133, primes=29, fill=104, ratio=0.781955, anchor=[3]`

最高补洞比例行：

- `x=362, y=363, S=133, primes=29, fill=104, ratio=0.781955, anchor=[3]`

最大第P列锚因子行：

- `x=29, y=30, S=133, primes=57, fill=76, ratio=0.571429, anchor=[2, 3, 5]`
- `x=59, y=60, S=133, primes=42, fill=91, ratio=0.684211, anchor=[2, 3, 5]`
- `x=89, y=90, S=133, primes=48, fill=85, ratio=0.639098, anchor=[2, 3, 5]`
- `x=119, y=120, S=133, primes=47, fill=86, ratio=0.646617, anchor=[2, 3, 5]`
- `x=149, y=150, S=133, primes=47, fill=86, ratio=0.646617, anchor=[2, 3, 5]`
- `x=179, y=180, S=133, primes=46, fill=87, ratio=0.654135, anchor=[2, 3, 5]`
- `x=209, y=210, S=133, primes=47, fill=86, ratio=0.646617, anchor=[2, 3, 5]`
- `x=239, y=240, S=133, primes=41, fill=92, ratio=0.691729, anchor=[2, 3, 5]`

## P=499 W=210

- `wheel_prime_factors`: `[2, 3, 5, 7]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `112`
- `min_prime_holes`: `29`
- `max_filler_ratio`: `0.745614`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=362, y=363, S=114, primes=29, fill=85, ratio=0.745614, anchor=[3]`

最高补洞比例行：

- `x=362, y=363, S=114, primes=29, fill=85, ratio=0.745614, anchor=[3]`

最大第P列锚因子行：

- `x=209, y=210, S=114, primes=47, fill=67, ratio=0.587719, anchor=[2, 3, 5, 7]`
- `x=419, y=420, S=114, primes=46, fill=68, ratio=0.596491, anchor=[2, 3, 5, 7]`

## P=499 W=2310

- `wheel_prime_factors`: `[2, 3, 5, 7, 11]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `101`
- `min_prime_holes`: `29`
- `max_filler_ratio`: `0.721154`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=362, y=363, S=104, primes=29, fill=75, ratio=0.721154, anchor=[3, 11]`

最高补洞比例行：

- `x=362, y=363, S=104, primes=29, fill=75, ratio=0.721154, anchor=[3, 11]`

最大第P列锚因子行：

- `x=209, y=210, S=104, primes=47, fill=57, ratio=0.548077, anchor=[2, 3, 5, 7]`
- `x=329, y=330, S=104, primes=44, fill=60, ratio=0.576923, anchor=[2, 3, 5, 11]`
- `x=419, y=420, S=104, primes=46, fill=58, ratio=0.557692, anchor=[2, 3, 5, 7]`
- `x=461, y=462, S=103, primes=45, fill=58, ratio=0.563107, anchor=[2, 3, 7, 11]`

## P=499 W=30030

- `wheel_prime_factors`: `[2, 3, 5, 7, 11, 13]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `92`
- `min_prime_holes`: `29`
- `max_filler_ratio`: `0.691489`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=362, y=363, S=94, primes=29, fill=65, ratio=0.691489, anchor=[3, 11]`

最高补洞比例行：

- `x=362, y=363, S=94, primes=29, fill=65, ratio=0.691489, anchor=[3, 11]`

最大第P列锚因子行：

- `x=209, y=210, S=96, primes=47, fill=49, ratio=0.510417, anchor=[2, 3, 5, 7]`
- `x=329, y=330, S=96, primes=44, fill=52, ratio=0.541667, anchor=[2, 3, 5, 11]`
- `x=389, y=390, S=93, primes=31, fill=62, ratio=0.666667, anchor=[2, 3, 5, 13]`
- `x=419, y=420, S=96, primes=46, fill=50, ratio=0.520833, anchor=[2, 3, 5, 7]`
- `x=461, y=462, S=96, primes=45, fill=51, ratio=0.531250, anchor=[2, 3, 7, 11]`

## P=997 W=30

- `wheel_prime_factors`: `[2, 3, 5]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `265`
- `min_prime_holes`: `54`
- `max_filler_ratio`: `0.796226`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=916, y=917, S=265, primes=54, fill=211, ratio=0.796226, anchor=[]`

最高补洞比例行：

- `x=916, y=917, S=265, primes=54, fill=211, ratio=0.796226, anchor=[]`

最大第P列锚因子行：

- `x=29, y=30, S=265, primes=91, fill=174, ratio=0.656604, anchor=[2, 3, 5]`
- `x=59, y=60, S=265, primes=98, fill=167, ratio=0.630189, anchor=[2, 3, 5]`
- `x=89, y=90, S=265, primes=95, fill=170, ratio=0.641509, anchor=[2, 3, 5]`
- `x=119, y=120, S=265, primes=81, fill=184, ratio=0.694340, anchor=[2, 3, 5]`
- `x=149, y=150, S=265, primes=93, fill=172, ratio=0.649057, anchor=[2, 3, 5]`
- `x=179, y=180, S=265, primes=91, fill=174, ratio=0.656604, anchor=[2, 3, 5]`
- `x=209, y=210, S=265, primes=85, fill=180, ratio=0.679245, anchor=[2, 3, 5]`
- `x=239, y=240, S=265, primes=80, fill=185, ratio=0.698113, anchor=[2, 3, 5]`

## P=997 W=210

- `wheel_prime_factors`: `[2, 3, 5, 7]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `226`
- `min_prime_holes`: `54`
- `max_filler_ratio`: `0.763158`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=916, y=917, S=228, primes=54, fill=174, ratio=0.763158, anchor=[7]`

最高补洞比例行：

- `x=916, y=917, S=228, primes=54, fill=174, ratio=0.763158, anchor=[7]`

最大第P列锚因子行：

- `x=209, y=210, S=227, primes=85, fill=142, ratio=0.625551, anchor=[2, 3, 5, 7]`
- `x=419, y=420, S=227, primes=77, fill=150, ratio=0.660793, anchor=[2, 3, 5, 7]`
- `x=629, y=630, S=227, primes=70, fill=157, ratio=0.691630, anchor=[2, 3, 5, 7]`
- `x=839, y=840, S=227, primes=70, fill=157, ratio=0.691630, anchor=[2, 3, 5, 7]`

## P=997 W=2310

- `wheel_prime_factors`: `[2, 3, 5, 7, 11]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `204`
- `min_prime_holes`: `54`
- `max_filler_ratio`: `0.740385`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=916, y=917, S=208, primes=54, fill=154, ratio=0.740385, anchor=[7]`

最高补洞比例行：

- `x=916, y=917, S=208, primes=54, fill=154, ratio=0.740385, anchor=[7]`

最大第P列锚因子行：

- `x=209, y=210, S=208, primes=85, fill=123, ratio=0.591346, anchor=[2, 3, 5, 7]`
- `x=329, y=330, S=206, primes=73, fill=133, ratio=0.645631, anchor=[2, 3, 5, 11]`
- `x=419, y=420, S=206, primes=77, fill=129, ratio=0.626214, anchor=[2, 3, 5, 7]`
- `x=461, y=462, S=208, primes=66, fill=142, ratio=0.682692, anchor=[2, 3, 7, 11]`
- `x=629, y=630, S=206, primes=70, fill=136, ratio=0.660194, anchor=[2, 3, 5, 7]`
- `x=659, y=660, S=208, primes=70, fill=138, ratio=0.663462, anchor=[2, 3, 5, 11]`
- `x=769, y=770, S=206, primes=71, fill=135, ratio=0.655340, anchor=[2, 5, 7, 11]`
- `x=839, y=840, S=206, primes=70, fill=136, ratio=0.660194, anchor=[2, 3, 5, 7]`

## P=997 W=30030

- `wheel_prime_factors`: `[2, 3, 5, 7, 11, 13]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `187`
- `min_prime_holes`: `54`
- `max_filler_ratio`: `0.720207`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=916, y=917, S=193, primes=54, fill=139, ratio=0.720207, anchor=[7]`

最高补洞比例行：

- `x=916, y=917, S=193, primes=54, fill=139, ratio=0.720207, anchor=[7]`

最大第P列锚因子行：

- `x=209, y=210, S=192, primes=85, fill=107, ratio=0.557292, anchor=[2, 3, 5, 7]`
- `x=329, y=330, S=191, primes=73, fill=118, ratio=0.617801, anchor=[2, 3, 5, 11]`
- `x=389, y=390, S=191, primes=73, fill=118, ratio=0.617801, anchor=[2, 3, 5, 13]`
- `x=419, y=420, S=190, primes=77, fill=113, ratio=0.594737, anchor=[2, 3, 5, 7]`
- `x=461, y=462, S=193, primes=66, fill=127, ratio=0.658031, anchor=[2, 3, 7, 11]`
- `x=545, y=546, S=191, primes=70, fill=121, ratio=0.633508, anchor=[2, 3, 7, 13]`
- `x=629, y=630, S=191, primes=70, fill=121, ratio=0.633508, anchor=[2, 3, 5, 7]`
- `x=659, y=660, S=193, primes=70, fill=123, ratio=0.637306, anchor=[2, 3, 5, 11]`

## P=2003 W=30

- `wheel_prime_factors`: `[2, 3, 5]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `533`
- `min_prime_holes`: `113`
- `max_filler_ratio`: `0.788785`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=1256, y=1257, S=535, primes=113, fill=422, ratio=0.788785, anchor=[3]`
- `x=1411, y=1412, S=533, primes=113, fill=420, ratio=0.787992, anchor=[2]`
- `x=1673, y=1674, S=533, primes=113, fill=420, ratio=0.787992, anchor=[2, 3]`

最高补洞比例行：

- `x=1256, y=1257, S=535, primes=113, fill=422, ratio=0.788785, anchor=[3]`

最大第P列锚因子行：

- `x=29, y=30, S=534, primes=183, fill=351, ratio=0.657303, anchor=[2, 3, 5]`
- `x=59, y=60, S=534, primes=168, fill=366, ratio=0.685393, anchor=[2, 3, 5]`
- `x=89, y=90, S=534, primes=181, fill=353, ratio=0.661049, anchor=[2, 3, 5]`
- `x=119, y=120, S=534, primes=164, fill=370, ratio=0.692884, anchor=[2, 3, 5]`
- `x=149, y=150, S=534, primes=151, fill=383, ratio=0.717228, anchor=[2, 3, 5]`
- `x=179, y=180, S=534, primes=151, fill=383, ratio=0.717228, anchor=[2, 3, 5]`
- `x=209, y=210, S=534, primes=161, fill=373, ratio=0.698502, anchor=[2, 3, 5]`
- `x=239, y=240, S=534, primes=157, fill=377, ratio=0.705993, anchor=[2, 3, 5]`

## P=2003 W=210

- `wheel_prime_factors`: `[2, 3, 5, 7]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `456`
- `min_prime_holes`: `113`
- `max_filler_ratio`: `0.753813`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=1256, y=1257, S=459, primes=113, fill=346, ratio=0.753813, anchor=[3]`
- `x=1411, y=1412, S=456, primes=113, fill=343, ratio=0.752193, anchor=[2]`
- `x=1673, y=1674, S=456, primes=113, fill=343, ratio=0.752193, anchor=[2, 3]`

最高补洞比例行：

- `x=1256, y=1257, S=459, primes=113, fill=346, ratio=0.753813, anchor=[3]`

最大第P列锚因子行：

- `x=209, y=210, S=458, primes=161, fill=297, ratio=0.648472, anchor=[2, 3, 5, 7]`
- `x=419, y=420, S=458, primes=150, fill=308, ratio=0.672489, anchor=[2, 3, 5, 7]`
- `x=629, y=630, S=458, primes=138, fill=320, ratio=0.698690, anchor=[2, 3, 5, 7]`
- `x=839, y=840, S=458, primes=137, fill=321, ratio=0.700873, anchor=[2, 3, 5, 7]`
- `x=1049, y=1050, S=458, primes=143, fill=315, ratio=0.687773, anchor=[2, 3, 5, 7]`
- `x=1259, y=1260, S=458, primes=143, fill=315, ratio=0.687773, anchor=[2, 3, 5, 7]`
- `x=1469, y=1470, S=458, primes=126, fill=332, ratio=0.724891, anchor=[2, 3, 5, 7]`
- `x=1679, y=1680, S=458, primes=141, fill=317, ratio=0.692140, anchor=[2, 3, 5, 7]`

## P=2003 W=2310

- `wheel_prime_factors`: `[2, 3, 5, 7, 11]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `413`
- `min_prime_holes`: `113`
- `max_filler_ratio`: `0.728365`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=1256, y=1257, S=416, primes=113, fill=303, ratio=0.728365, anchor=[3]`
- `x=1411, y=1412, S=413, primes=113, fill=300, ratio=0.726392, anchor=[2]`
- `x=1673, y=1674, S=413, primes=113, fill=300, ratio=0.726392, anchor=[2, 3]`

最高补洞比例行：

- `x=1256, y=1257, S=416, primes=113, fill=303, ratio=0.728365, anchor=[3]`

最大第P列锚因子行：

- `x=209, y=210, S=417, primes=161, fill=256, ratio=0.613909, anchor=[2, 3, 5, 7]`
- `x=329, y=330, S=416, primes=158, fill=258, ratio=0.620192, anchor=[2, 3, 5, 11]`
- `x=419, y=420, S=416, primes=150, fill=266, ratio=0.639423, anchor=[2, 3, 5, 7]`
- `x=461, y=462, S=416, primes=162, fill=254, ratio=0.610577, anchor=[2, 3, 7, 11]`
- `x=629, y=630, S=417, primes=138, fill=279, ratio=0.669065, anchor=[2, 3, 5, 7]`
- `x=659, y=660, S=416, primes=143, fill=273, ratio=0.656250, anchor=[2, 3, 5, 11]`
- `x=769, y=770, S=416, primes=140, fill=276, ratio=0.663462, anchor=[2, 5, 7, 11]`
- `x=839, y=840, S=416, primes=137, fill=279, ratio=0.670673, anchor=[2, 3, 5, 7]`

## P=2003 W=30030

- `wheel_prime_factors`: `[2, 3, 5, 7, 11, 13]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `379`
- `min_prime_holes`: `113`
- `max_filler_ratio`: `0.706494`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=1256, y=1257, S=385, primes=113, fill=272, ratio=0.706494, anchor=[3]`
- `x=1411, y=1412, S=381, primes=113, fill=268, ratio=0.703412, anchor=[2]`
- `x=1673, y=1674, S=379, primes=113, fill=266, ratio=0.701847, anchor=[2, 3]`

最高补洞比例行：

- `x=1256, y=1257, S=385, primes=113, fill=272, ratio=0.706494, anchor=[3]`

最大第P列锚因子行：

- `x=209, y=210, S=386, primes=161, fill=225, ratio=0.582902, anchor=[2, 3, 5, 7]`
- `x=329, y=330, S=384, primes=158, fill=226, ratio=0.588542, anchor=[2, 3, 5, 11]`
- `x=389, y=390, S=384, primes=143, fill=241, ratio=0.627604, anchor=[2, 3, 5, 13]`
- `x=419, y=420, S=383, primes=150, fill=233, ratio=0.608355, anchor=[2, 3, 5, 7]`
- `x=461, y=462, S=384, primes=162, fill=222, ratio=0.578125, anchor=[2, 3, 7, 11]`
- `x=545, y=546, S=383, primes=146, fill=237, ratio=0.618799, anchor=[2, 3, 7, 13]`
- `x=629, y=630, S=383, primes=138, fill=245, ratio=0.639687, anchor=[2, 3, 5, 7]`
- `x=659, y=660, S=382, primes=143, fill=239, ratio=0.625654, anchor=[2, 3, 5, 11]`

## P=5003 W=30

- `wheel_prime_factors`: `[2, 3, 5]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `1333`
- `min_prime_holes`: `260`
- `max_filler_ratio`: `0.805097`
- `max_anchor_zero_prime_count`: `3`

最小素数洞行：

- `x=4980, y=4981, S=1334, primes=260, fill=1074, ratio=0.805097, anchor=[]`

最高补洞比例行：

- `x=4980, y=4981, S=1334, primes=260, fill=1074, ratio=0.805097, anchor=[]`

最大第P列锚因子行：

- `x=29, y=30, S=1334, primes=427, fill=907, ratio=0.679910, anchor=[2, 3, 5]`
- `x=59, y=60, S=1334, primes=381, fill=953, ratio=0.714393, anchor=[2, 3, 5]`
- `x=89, y=90, S=1334, primes=365, fill=969, ratio=0.726387, anchor=[2, 3, 5]`
- `x=119, y=120, S=1334, primes=365, fill=969, ratio=0.726387, anchor=[2, 3, 5]`
- `x=149, y=150, S=1334, primes=363, fill=971, ratio=0.727886, anchor=[2, 3, 5]`
- `x=179, y=180, S=1334, primes=350, fill=984, ratio=0.737631, anchor=[2, 3, 5]`
- `x=209, y=210, S=1334, primes=350, fill=984, ratio=0.737631, anchor=[2, 3, 5]`
- `x=239, y=240, S=1334, primes=350, fill=984, ratio=0.737631, anchor=[2, 3, 5]`

## P=5003 W=210

- `wheel_prime_factors`: `[2, 3, 5, 7]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `1141`
- `min_prime_holes`: `260`
- `max_filler_ratio`: `0.772727`
- `max_anchor_zero_prime_count`: `4`

最小素数洞行：

- `x=4980, y=4981, S=1144, primes=260, fill=884, ratio=0.772727, anchor=[]`

最高补洞比例行：

- `x=4980, y=4981, S=1144, primes=260, fill=884, ratio=0.772727, anchor=[]`

最大第P列锚因子行：

- `x=209, y=210, S=1143, primes=350, fill=793, ratio=0.693788, anchor=[2, 3, 5, 7]`
- `x=419, y=420, S=1143, primes=348, fill=795, ratio=0.695538, anchor=[2, 3, 5, 7]`
- `x=629, y=630, S=1143, primes=340, fill=803, ratio=0.702537, anchor=[2, 3, 5, 7]`
- `x=839, y=840, S=1143, primes=332, fill=811, ratio=0.709536, anchor=[2, 3, 5, 7]`
- `x=1049, y=1050, S=1143, primes=346, fill=797, ratio=0.697288, anchor=[2, 3, 5, 7]`
- `x=1259, y=1260, S=1143, primes=333, fill=810, ratio=0.708661, anchor=[2, 3, 5, 7]`
- `x=1469, y=1470, S=1143, primes=317, fill=826, ratio=0.722660, anchor=[2, 3, 5, 7]`
- `x=1679, y=1680, S=1143, primes=307, fill=836, ratio=0.731409, anchor=[2, 3, 5, 7]`

## P=5003 W=2310

- `wheel_prime_factors`: `[2, 3, 5, 7, 11]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `1037`
- `min_prime_holes`: `260`
- `max_filler_ratio`: `0.750000`
- `max_anchor_zero_prime_count`: `5`

最小素数洞行：

- `x=4980, y=4981, S=1040, primes=260, fill=780, ratio=0.750000, anchor=[]`

最高补洞比例行：

- `x=4980, y=4981, S=1040, primes=260, fill=780, ratio=0.750000, anchor=[]`

最大第P列锚因子行：

- `x=2309, y=2310, S=1039, primes=299, fill=740, ratio=0.712223, anchor=[2, 3, 5, 7, 11]`
- `x=4619, y=4620, S=1039, primes=301, fill=738, ratio=0.710298, anchor=[2, 3, 5, 7, 11]`

## P=5003 W=30030

- `wheel_prime_factors`: `[2, 3, 5, 7, 11, 13]`
- `shift_identity_failures`: `0`
- `min_skeleton_count`: `955`
- `min_prime_holes`: `260`
- `max_filler_ratio`: `0.729448`
- `max_anchor_zero_prime_count`: `5`

最小素数洞行：

- `x=4980, y=4981, S=961, primes=260, fill=701, ratio=0.729448, anchor=[]`

最高补洞比例行：

- `x=4980, y=4981, S=961, primes=260, fill=701, ratio=0.729448, anchor=[]`

最大第P列锚因子行：

- `x=2309, y=2310, S=958, primes=299, fill=659, ratio=0.687891, anchor=[2, 3, 5, 7, 11]`
- `x=2729, y=2730, S=960, primes=303, fill=657, ratio=0.684375, anchor=[2, 3, 5, 7, 13]`
- `x=4289, y=4290, S=958, primes=297, fill=661, ratio=0.689979, anchor=[2, 3, 5, 11, 13]`
- `x=4619, y=4620, S=958, primes=301, fill=657, ratio=0.685804, anchor=[2, 3, 5, 7, 11]`

## 结构解释

第 `x` 行写成 `P(x+1)-d`，其中 `d=P-c`。所以第 `P` 列锚点 `P(x+1)` 的轮残基决定整行的距离筛：

```text
P(x+1)-d 避开 W 的全部素因子
<=> d mod W 属于 P(x+1)-U_W。
```

第一行是 `x=1,y=2`。任意行 `y=x+1` 的允许距离类，等于第一行允许距离类平移 `P(y-2)`。报告中的 `shift_identity_failures=0` 是这个圆柱平移恒等式的机器核验。

若某个 `q|W` 同时满足 `q|y`，则第 `P` 列锚点在 `mod q` 为零，该 q 在本行覆盖的距离类是 `d≡0 mod q`。这就是第 `P` 列的层叠轮筛如何接入整行斜线覆盖。
