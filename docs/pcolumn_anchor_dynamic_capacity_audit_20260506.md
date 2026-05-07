# 第P列锚点动态容量审计

**状态：** `pcolumn_anchor_dynamic_capacity_audit_not_a_proof`

## 参数

- `p_list`: `[101, 499, 997, 2003, 5003]`
- `alpha`: `0.43`
- `include_square_plus`: `True`

## 总表

| P | cutoff | rows | low primes | high primes | H | min margin | max T/S | min model/sqrt | max D+/sqrt | C-window | min prime holes | cap fails | union fails |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 101 | 7 | 101 | 4 | 21 | 0.626627 | 1 | 0.954545 | 1.711011 | 1.538075 | 0.172936 | 7 | 0 | 0 |
| 499 | 14 | 499 | 6 | 88 | 0.750683 | 3 | 0.968085 | 2.391366 | 2.107793 | 0.283573 | 29 | 0 | 0 |
| 997 | 19 | 997 | 8 | 159 | 0.741599 | 20 | 0.883041 | 3.329259 | 1.849589 | 1.479671 | 54 | 0 | 0 |
| 2003 | 26 | 2003 | 9 | 294 | 0.793492 | 20 | 0.939024 | 3.694119 | 2.635695 | 1.058424 | 113 | 0 | 0 |
| 5003 | 38 | 5003 | 12 | 657 | 0.812465 | 46 | 0.937922 | 5.066922 | 3.415103 | 1.651820 | 260 | 0 | 0 |

## P=101

- `cutoff`: `7`
- `H=sum_{P^alpha<q<P}1/q`: `0.626627`
- `min_capacity_margin`: `1`
- `max_hit_ratio`: `0.954545`
- `min_model_over_sqrt`: `1.711011`
- `max_dplus_over_sqrt`: `1.538075`
- `sqrt_c_window`: `0.172936`
- `min_prime_holes`: `7`

最小容量余量行：

- `x=13, y=14, S=22, T=21, margin=1, ratio=0.954545, D+/sqrt=1.538075, prime_holes=9, top_q=[{'q': 11, 'hit_count': 2}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=24, y=25, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=9, top_q=[{'q': 11, 'hit_count': 4}, {'q': 13, 'hit_count': 3}, {'q': 23, 'hit_count': 2}]`
- `x=41, y=42, S=23, T=20, margin=3, ratio=0.869565, D+/sqrt=1.165092, prime_holes=11, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 19, 'hit_count': 2}]`
- `x=73, y=74, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=7, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=94, y=95, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=8, top_q=[{'q': 13, 'hit_count': 3}, {'q': 11, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=7, y=8, S=22, T=18, margin=4, ratio=0.818182, D+/sqrt=0.898473, prime_holes=13, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=11, y=12, S=21, T=17, margin=4, ratio=0.809524, D+/sqrt=0.838140, prime_holes=11, top_q=[{'q': 11, 'hit_count': 3}, {'q': 17, 'hit_count': 2}, {'q': 19, 'hit_count': 2}]`
- `x=70, y=71, S=23, T=19, margin=4, ratio=0.826087, D+/sqrt=0.956578, prime_holes=8, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`

最大 T/S 行：

- `x=13, y=14, S=22, T=21, margin=1, ratio=0.954545, D+/sqrt=1.538075, prime_holes=9, top_q=[{'q': 11, 'hit_count': 2}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=41, y=42, S=23, T=20, margin=3, ratio=0.869565, D+/sqrt=1.165092, prime_holes=11, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 19, 'hit_count': 2}]`
- `x=24, y=25, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=9, top_q=[{'q': 11, 'hit_count': 4}, {'q': 13, 'hit_count': 3}, {'q': 23, 'hit_count': 2}]`
- `x=73, y=74, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=7, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=94, y=95, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=8, top_q=[{'q': 13, 'hit_count': 3}, {'q': 11, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=70, y=71, S=23, T=19, margin=4, ratio=0.826087, D+/sqrt=0.956578, prime_holes=8, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=7, y=8, S=22, T=18, margin=4, ratio=0.818182, D+/sqrt=0.898473, prime_holes=13, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=11, y=12, S=21, T=17, margin=4, ratio=0.809524, D+/sqrt=0.838140, prime_holes=11, top_q=[{'q': 11, 'hit_count': 3}, {'q': 17, 'hit_count': 2}, {'q': 19, 'hit_count': 2}]`

最大相对正偏差行：

- `x=13, y=14, S=22, T=21, margin=1, ratio=0.954545, D+/sqrt=1.538075, prime_holes=9, top_q=[{'q': 11, 'hit_count': 2}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=41, y=42, S=23, T=20, margin=3, ratio=0.869565, D+/sqrt=1.165092, prime_holes=11, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 19, 'hit_count': 2}]`
- `x=24, y=25, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=9, top_q=[{'q': 11, 'hit_count': 4}, {'q': 13, 'hit_count': 3}, {'q': 23, 'hit_count': 2}]`
- `x=73, y=74, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=7, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=94, y=95, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=8, top_q=[{'q': 13, 'hit_count': 3}, {'q': 11, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=70, y=71, S=23, T=19, margin=4, ratio=0.826087, D+/sqrt=0.956578, prime_holes=8, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=7, y=8, S=22, T=18, margin=4, ratio=0.818182, D+/sqrt=0.898473, prime_holes=13, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=11, y=12, S=21, T=17, margin=4, ratio=0.809524, D+/sqrt=0.838140, prime_holes=11, top_q=[{'q': 11, 'hit_count': 3}, {'q': 17, 'hit_count': 2}, {'q': 19, 'hit_count': 2}]`

最少素数洞行：

- `x=73, y=74, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=7, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=70, y=71, S=23, T=19, margin=4, ratio=0.826087, D+/sqrt=0.956578, prime_holes=8, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=79, y=80, S=22, T=17, margin=5, ratio=0.772727, D+/sqrt=0.685272, prime_holes=8, top_q=[{'q': 11, 'hit_count': 3}, {'q': 13, 'hit_count': 2}, {'q': 23, 'hit_count': 2}]`
- `x=94, y=95, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=8, top_q=[{'q': 13, 'hit_count': 3}, {'q': 11, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=13, y=14, S=22, T=21, margin=1, ratio=0.954545, D+/sqrt=1.538075, prime_holes=9, top_q=[{'q': 11, 'hit_count': 2}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`
- `x=24, y=25, S=22, T=19, margin=3, ratio=0.863636, D+/sqrt=1.111674, prime_holes=9, top_q=[{'q': 11, 'hit_count': 4}, {'q': 13, 'hit_count': 3}, {'q': 23, 'hit_count': 2}]`
- `x=59, y=60, S=22, T=15, margin=7, ratio=0.681818, D+/sqrt=0.258871, prime_holes=9, top_q=[{'q': 13, 'hit_count': 2}, {'q': 11, 'hit_count': 1}, {'q': 17, 'hit_count': 1}]`
- `x=63, y=64, S=22, T=16, margin=6, ratio=0.727273, D+/sqrt=0.472072, prime_holes=9, top_q=[{'q': 11, 'hit_count': 2}, {'q': 13, 'hit_count': 2}, {'q': 17, 'hit_count': 2}]`

## P=499

- `cutoff`: `14`
- `H=sum_{P^alpha<q<P}1/q`: `0.750683`
- `min_capacity_margin`: `3`
- `max_hit_ratio`: `0.968085`
- `min_model_over_sqrt`: `2.391366`
- `max_dplus_over_sqrt`: `2.107793`
- `sqrt_c_window`: `0.283573`
- `min_prime_holes`: `29`

最小容量余量行：

- `x=14, y=15, S=94, T=91, margin=3, ratio=0.968085, D+/sqrt=2.107793, prime_holes=49, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 5}]`
- `x=16, y=17, S=96, T=86, margin=10, ratio=0.895833, D+/sqrt=1.422178, prime_holes=53, top_q=[{'q': 19, 'hit_count': 6}, {'q': 23, 'hit_count': 5}, {'q': 17, 'hit_count': 4}]`
- `x=28, y=29, S=93, T=83, margin=10, ratio=0.892473, D+/sqrt=1.367375, prime_holes=46, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 4}]`
- `x=37, y=38, S=93, T=83, margin=10, ratio=0.892473, D+/sqrt=1.367375, prime_holes=40, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 5}]`
- `x=94, y=95, S=94, T=84, margin=10, ratio=0.893617, D+/sqrt=1.385798, prime_holes=41, top_q=[{'q': 19, 'hit_count': 5}, {'q': 17, 'hit_count': 4}, {'q': 29, 'hit_count': 4}]`
- `x=49, y=50, S=97, T=85, margin=12, ratio=0.876289, D+/sqrt=1.237073, prime_holes=42, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 29, 'hit_count': 4}]`
- `x=215, y=216, S=98, T=86, margin=12, ratio=0.877551, D+/sqrt=1.255930, prime_holes=34, top_q=[{'q': 17, 'hit_count': 7}, {'q': 19, 'hit_count': 7}, {'q': 31, 'hit_count': 5}]`
- `x=294, y=295, S=95, T=83, margin=12, ratio=0.873684, D+/sqrt=1.198868, prime_holes=39, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 41, 'hit_count': 4}]`

最大 T/S 行：

- `x=14, y=15, S=94, T=91, margin=3, ratio=0.968085, D+/sqrt=2.107793, prime_holes=49, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 5}]`
- `x=16, y=17, S=96, T=86, margin=10, ratio=0.895833, D+/sqrt=1.422178, prime_holes=53, top_q=[{'q': 19, 'hit_count': 6}, {'q': 23, 'hit_count': 5}, {'q': 17, 'hit_count': 4}]`
- `x=94, y=95, S=94, T=84, margin=10, ratio=0.893617, D+/sqrt=1.385798, prime_holes=41, top_q=[{'q': 19, 'hit_count': 5}, {'q': 17, 'hit_count': 4}, {'q': 29, 'hit_count': 4}]`
- `x=28, y=29, S=93, T=83, margin=10, ratio=0.892473, D+/sqrt=1.367375, prime_holes=46, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 4}]`
- `x=37, y=38, S=93, T=83, margin=10, ratio=0.892473, D+/sqrt=1.367375, prime_holes=40, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 5}]`
- `x=215, y=216, S=98, T=86, margin=12, ratio=0.877551, D+/sqrt=1.255930, prime_holes=34, top_q=[{'q': 17, 'hit_count': 7}, {'q': 19, 'hit_count': 7}, {'q': 31, 'hit_count': 5}]`
- `x=49, y=50, S=97, T=85, margin=12, ratio=0.876289, D+/sqrt=1.237073, prime_holes=42, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 29, 'hit_count': 4}]`
- `x=294, y=295, S=95, T=83, margin=12, ratio=0.873684, D+/sqrt=1.198868, prime_holes=39, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 41, 'hit_count': 4}]`

最大相对正偏差行：

- `x=14, y=15, S=94, T=91, margin=3, ratio=0.968085, D+/sqrt=2.107793, prime_holes=49, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 5}]`
- `x=16, y=17, S=96, T=86, margin=10, ratio=0.895833, D+/sqrt=1.422178, prime_holes=53, top_q=[{'q': 19, 'hit_count': 6}, {'q': 23, 'hit_count': 5}, {'q': 17, 'hit_count': 4}]`
- `x=94, y=95, S=94, T=84, margin=10, ratio=0.893617, D+/sqrt=1.385798, prime_holes=41, top_q=[{'q': 19, 'hit_count': 5}, {'q': 17, 'hit_count': 4}, {'q': 29, 'hit_count': 4}]`
- `x=28, y=29, S=93, T=83, margin=10, ratio=0.892473, D+/sqrt=1.367375, prime_holes=46, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 4}]`
- `x=37, y=38, S=93, T=83, margin=10, ratio=0.892473, D+/sqrt=1.367375, prime_holes=40, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 5}]`
- `x=215, y=216, S=98, T=86, margin=12, ratio=0.877551, D+/sqrt=1.255930, prime_holes=34, top_q=[{'q': 17, 'hit_count': 7}, {'q': 19, 'hit_count': 7}, {'q': 31, 'hit_count': 5}]`
- `x=49, y=50, S=97, T=85, margin=12, ratio=0.876289, D+/sqrt=1.237073, prime_holes=42, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 29, 'hit_count': 4}]`
- `x=294, y=295, S=95, T=83, margin=12, ratio=0.873684, D+/sqrt=1.198868, prime_holes=39, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 41, 'hit_count': 4}]`

最少素数洞行：

- `x=362, y=363, S=94, T=80, margin=14, ratio=0.851064, D+/sqrt=0.973229, prime_holes=29, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 23, 'hit_count': 4}]`
- `x=351, y=352, S=96, T=74, margin=22, ratio=0.770833, D+/sqrt=0.197433, prime_holes=31, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 23, 'hit_count': 4}]`
- `x=389, y=390, S=93, T=76, margin=17, ratio=0.817204, D+/sqrt=0.641509, prime_holes=31, top_q=[{'q': 17, 'hit_count': 6}, {'q': 23, 'hit_count': 5}, {'q': 29, 'hit_count': 5}]`
- `x=330, y=331, S=96, T=79, margin=17, ratio=0.822917, D+/sqrt=0.707743, prime_holes=33, top_q=[{'q': 19, 'hit_count': 6}, {'q': 17, 'hit_count': 5}, {'q': 23, 'hit_count': 4}]`
- `x=215, y=216, S=98, T=86, margin=12, ratio=0.877551, D+/sqrt=1.255930, prime_holes=34, top_q=[{'q': 17, 'hit_count': 7}, {'q': 19, 'hit_count': 7}, {'q': 31, 'hit_count': 5}]`
- `x=254, y=255, S=97, T=82, margin=15, ratio=0.845361, D+/sqrt=0.932469, prime_holes=34, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 6}, {'q': 23, 'hit_count': 5}]`
- `x=355, y=356, S=96, T=76, margin=20, ratio=0.791667, D+/sqrt=0.401557, prime_holes=34, top_q=[{'q': 17, 'hit_count': 6}, {'q': 19, 'hit_count': 5}, {'q': 29, 'hit_count': 4}]`
- `x=436, y=437, S=95, T=78, margin=17, ratio=0.821053, D+/sqrt=0.685879, prime_holes=34, top_q=[{'q': 17, 'hit_count': 6}, {'q': 23, 'hit_count': 6}, {'q': 19, 'hit_count': 3}]`

## P=997

- `cutoff`: `19`
- `H=sum_{P^alpha<q<P}1/q`: `0.741599`
- `min_capacity_margin`: `20`
- `max_hit_ratio`: `0.883041`
- `min_model_over_sqrt`: `3.329259`
- `max_dplus_over_sqrt`: `1.849589`
- `sqrt_c_window`: `1.479671`
- `min_prime_holes`: `54`

最小容量余量行：

- `x=804, y=805, S=171, T=151, margin=20, ratio=0.883041, D+/sqrt=1.849589, prime_holes=64, top_q=[{'q': 23, 'hit_count': 7}, {'q': 29, 'hit_count': 7}, {'q': 37, 'hit_count': 6}]`
- `x=40, y=41, S=169, T=148, margin=21, ratio=0.875740, D+/sqrt=1.743824, prime_holes=87, top_q=[{'q': 23, 'hit_count': 8}, {'q': 31, 'hit_count': 6}, {'q': 37, 'hit_count': 6}]`
- `x=35, y=36, S=168, T=146, margin=22, ratio=0.869048, D+/sqrt=1.651918, prime_holes=88, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 7}, {'q': 53, 'hit_count': 5}]`
- `x=956, y=957, S=170, T=148, margin=22, ratio=0.870588, D+/sqrt=1.681809, prime_holes=63, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 8}, {'q': 31, 'hit_count': 5}]`
- `x=24, y=25, S=169, T=146, margin=23, ratio=0.863905, D+/sqrt=1.589977, prime_holes=93, top_q=[{'q': 29, 'hit_count': 8}, {'q': 23, 'hit_count': 7}, {'q': 37, 'hit_count': 6}]`
- `x=27, y=28, S=169, T=146, margin=23, ratio=0.863905, D+/sqrt=1.589977, prime_holes=93, top_q=[{'q': 23, 'hit_count': 7}, {'q': 29, 'hit_count': 7}, {'q': 31, 'hit_count': 5}]`
- `x=916, y=917, S=171, T=148, margin=23, ratio=0.865497, D+/sqrt=1.620173, prime_holes=54, top_q=[{'q': 23, 'hit_count': 9}, {'q': 29, 'hit_count': 5}, {'q': 31, 'hit_count': 5}]`
- `x=64, y=65, S=169, T=145, margin=24, ratio=0.857988, D+/sqrt=1.513054, prime_holes=78, top_q=[{'q': 23, 'hit_count': 8}, {'q': 31, 'hit_count': 8}, {'q': 29, 'hit_count': 7}]`

最大 T/S 行：

- `x=804, y=805, S=171, T=151, margin=20, ratio=0.883041, D+/sqrt=1.849589, prime_holes=64, top_q=[{'q': 23, 'hit_count': 7}, {'q': 29, 'hit_count': 7}, {'q': 37, 'hit_count': 6}]`
- `x=40, y=41, S=169, T=148, margin=21, ratio=0.875740, D+/sqrt=1.743824, prime_holes=87, top_q=[{'q': 23, 'hit_count': 8}, {'q': 31, 'hit_count': 6}, {'q': 37, 'hit_count': 6}]`
- `x=956, y=957, S=170, T=148, margin=22, ratio=0.870588, D+/sqrt=1.681809, prime_holes=63, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 8}, {'q': 31, 'hit_count': 5}]`
- `x=35, y=36, S=168, T=146, margin=22, ratio=0.869048, D+/sqrt=1.651918, prime_holes=88, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 7}, {'q': 53, 'hit_count': 5}]`
- `x=916, y=917, S=171, T=148, margin=23, ratio=0.865497, D+/sqrt=1.620173, prime_holes=54, top_q=[{'q': 23, 'hit_count': 9}, {'q': 29, 'hit_count': 5}, {'q': 31, 'hit_count': 5}]`
- `x=24, y=25, S=169, T=146, margin=23, ratio=0.863905, D+/sqrt=1.589977, prime_holes=93, top_q=[{'q': 29, 'hit_count': 8}, {'q': 23, 'hit_count': 7}, {'q': 37, 'hit_count': 6}]`
- `x=27, y=28, S=169, T=146, margin=23, ratio=0.863905, D+/sqrt=1.589977, prime_holes=93, top_q=[{'q': 23, 'hit_count': 7}, {'q': 29, 'hit_count': 7}, {'q': 31, 'hit_count': 5}]`
- `x=545, y=546, S=173, T=149, margin=24, ratio=0.861272, D+/sqrt=1.574043, prime_holes=70, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 7}, {'q': 31, 'hit_count': 6}]`

最大相对正偏差行：

- `x=804, y=805, S=171, T=151, margin=20, ratio=0.883041, D+/sqrt=1.849589, prime_holes=64, top_q=[{'q': 23, 'hit_count': 7}, {'q': 29, 'hit_count': 7}, {'q': 37, 'hit_count': 6}]`
- `x=40, y=41, S=169, T=148, margin=21, ratio=0.875740, D+/sqrt=1.743824, prime_holes=87, top_q=[{'q': 23, 'hit_count': 8}, {'q': 31, 'hit_count': 6}, {'q': 37, 'hit_count': 6}]`
- `x=956, y=957, S=170, T=148, margin=22, ratio=0.870588, D+/sqrt=1.681809, prime_holes=63, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 8}, {'q': 31, 'hit_count': 5}]`
- `x=35, y=36, S=168, T=146, margin=22, ratio=0.869048, D+/sqrt=1.651918, prime_holes=88, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 7}, {'q': 53, 'hit_count': 5}]`
- `x=916, y=917, S=171, T=148, margin=23, ratio=0.865497, D+/sqrt=1.620173, prime_holes=54, top_q=[{'q': 23, 'hit_count': 9}, {'q': 29, 'hit_count': 5}, {'q': 31, 'hit_count': 5}]`
- `x=24, y=25, S=169, T=146, margin=23, ratio=0.863905, D+/sqrt=1.589977, prime_holes=93, top_q=[{'q': 29, 'hit_count': 8}, {'q': 23, 'hit_count': 7}, {'q': 37, 'hit_count': 6}]`
- `x=27, y=28, S=169, T=146, margin=23, ratio=0.863905, D+/sqrt=1.589977, prime_holes=93, top_q=[{'q': 23, 'hit_count': 7}, {'q': 29, 'hit_count': 7}, {'q': 31, 'hit_count': 5}]`
- `x=545, y=546, S=173, T=149, margin=24, ratio=0.861272, D+/sqrt=1.574043, prime_holes=70, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 7}, {'q': 31, 'hit_count': 6}]`

最少素数洞行：

- `x=916, y=917, S=171, T=148, margin=23, ratio=0.865497, D+/sqrt=1.620173, prime_holes=54, top_q=[{'q': 23, 'hit_count': 9}, {'q': 29, 'hit_count': 5}, {'q': 31, 'hit_count': 5}]`
- `x=640, y=641, S=171, T=144, margin=27, ratio=0.842105, D+/sqrt=1.314285, prime_holes=59, top_q=[{'q': 23, 'hit_count': 8}, {'q': 29, 'hit_count': 7}, {'q': 31, 'hit_count': 6}]`
- `x=486, y=487, S=170, T=135, margin=35, ratio=0.794118, D+/sqrt=0.684755, prime_holes=60, top_q=[{'q': 23, 'hit_count': 6}, {'q': 29, 'hit_count': 6}, {'q': 41, 'hit_count': 6}]`
- `x=563, y=564, S=170, T=134, margin=36, ratio=0.788235, D+/sqrt=0.608058, prime_holes=61, top_q=[{'q': 23, 'hit_count': 7}, {'q': 31, 'hit_count': 6}, {'q': 41, 'hit_count': 6}]`
- `x=976, y=977, S=171, T=129, margin=42, ratio=0.754386, D+/sqrt=0.167206, prime_holes=61, top_q=[{'q': 29, 'hit_count': 8}, {'q': 23, 'hit_count': 6}, {'q': 31, 'hit_count': 6}]`
- `x=652, y=653, S=171, T=145, margin=26, ratio=0.847953, D+/sqrt=1.390757, prime_holes=62, top_q=[{'q': 23, 'hit_count': 6}, {'q': 31, 'hit_count': 6}, {'q': 37, 'hit_count': 6}]`
- `x=836, y=837, S=167, T=130, margin=37, ratio=0.778443, D+/sqrt=0.476126, prime_holes=62, top_q=[{'q': 23, 'hit_count': 7}, {'q': 29, 'hit_count': 5}, {'q': 31, 'hit_count': 5}]`
- `x=959, y=960, S=171, T=128, margin=43, ratio=0.748538, D+/sqrt=0.090735, prime_holes=62, top_q=[{'q': 23, 'hit_count': 7}, {'q': 31, 'hit_count': 7}, {'q': 29, 'hit_count': 6}]`

## P=2003

- `cutoff`: `26`
- `H=sum_{P^alpha<q<P}1/q`: `0.793492`
- `min_capacity_margin`: `20`
- `max_hit_ratio`: `0.939024`
- `min_model_over_sqrt`: `3.694119`
- `max_dplus_over_sqrt`: `2.635695`
- `sqrt_c_window`: `1.058424`
- `min_prime_holes`: `113`

最小容量余量行：

- `x=34, y=35, S=328, T=308, margin=20, ratio=0.939024, D+/sqrt=2.635695, prime_holes=164, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 10}]`
- `x=26, y=27, S=325, T=291, margin=34, ratio=0.895385, D+/sqrt=1.836887, prime_holes=180, top_q=[{'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 11}, {'q': 41, 'hit_count': 11}]`
- `x=22, y=23, S=326, T=291, margin=35, ratio=0.892638, D+/sqrt=1.790120, prime_holes=180, top_q=[{'q': 31, 'hit_count': 13}, {'q': 29, 'hit_count': 11}, {'q': 37, 'hit_count': 8}]`
- `x=27, y=28, S=329, T=294, margin=35, ratio=0.893617, D+/sqrt=1.816095, prime_holes=183, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 43, 'hit_count': 10}]`
- `x=36, y=37, S=326, T=291, margin=35, ratio=0.892638, D+/sqrt=1.790120, prime_holes=172, top_q=[{'q': 31, 'hit_count': 11}, {'q': 29, 'hit_count': 10}, {'q': 37, 'hit_count': 9}]`
- `x=23, y=24, S=329, T=293, margin=36, ratio=0.890578, D+/sqrt=1.760963, prime_holes=184, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 10}]`
- `x=30, y=31, S=325, T=289, margin=36, ratio=0.889231, D+/sqrt=1.725947, prime_holes=176, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 47, 'hit_count': 10}]`
- `x=1546, y=1547, S=329, T=292, margin=37, ratio=0.887538, D+/sqrt=1.705831, prime_holes=116, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 12}, {'q': 37, 'hit_count': 10}]`

最大 T/S 行：

- `x=34, y=35, S=328, T=308, margin=20, ratio=0.939024, D+/sqrt=2.635695, prime_holes=164, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 10}]`
- `x=26, y=27, S=325, T=291, margin=34, ratio=0.895385, D+/sqrt=1.836887, prime_holes=180, top_q=[{'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 11}, {'q': 41, 'hit_count': 11}]`
- `x=27, y=28, S=329, T=294, margin=35, ratio=0.893617, D+/sqrt=1.816095, prime_holes=183, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 43, 'hit_count': 10}]`
- `x=22, y=23, S=326, T=291, margin=35, ratio=0.892638, D+/sqrt=1.790120, prime_holes=180, top_q=[{'q': 31, 'hit_count': 13}, {'q': 29, 'hit_count': 11}, {'q': 37, 'hit_count': 8}]`
- `x=36, y=37, S=326, T=291, margin=35, ratio=0.892638, D+/sqrt=1.790120, prime_holes=172, top_q=[{'q': 31, 'hit_count': 11}, {'q': 29, 'hit_count': 10}, {'q': 37, 'hit_count': 9}]`
- `x=23, y=24, S=329, T=293, margin=36, ratio=0.890578, D+/sqrt=1.760963, prime_holes=184, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 10}]`
- `x=30, y=31, S=325, T=289, margin=36, ratio=0.889231, D+/sqrt=1.725947, prime_holes=176, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 47, 'hit_count': 10}]`
- `x=1546, y=1547, S=329, T=292, margin=37, ratio=0.887538, D+/sqrt=1.705831, prime_holes=116, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 12}, {'q': 37, 'hit_count': 10}]`

最大相对正偏差行：

- `x=34, y=35, S=328, T=308, margin=20, ratio=0.939024, D+/sqrt=2.635695, prime_holes=164, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 10}]`
- `x=26, y=27, S=325, T=291, margin=34, ratio=0.895385, D+/sqrt=1.836887, prime_holes=180, top_q=[{'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 11}, {'q': 41, 'hit_count': 11}]`
- `x=27, y=28, S=329, T=294, margin=35, ratio=0.893617, D+/sqrt=1.816095, prime_holes=183, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 43, 'hit_count': 10}]`
- `x=22, y=23, S=326, T=291, margin=35, ratio=0.892638, D+/sqrt=1.790120, prime_holes=180, top_q=[{'q': 31, 'hit_count': 13}, {'q': 29, 'hit_count': 11}, {'q': 37, 'hit_count': 8}]`
- `x=36, y=37, S=326, T=291, margin=35, ratio=0.892638, D+/sqrt=1.790120, prime_holes=172, top_q=[{'q': 31, 'hit_count': 11}, {'q': 29, 'hit_count': 10}, {'q': 37, 'hit_count': 9}]`
- `x=23, y=24, S=329, T=293, margin=36, ratio=0.890578, D+/sqrt=1.760963, prime_holes=184, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 11}, {'q': 37, 'hit_count': 10}]`
- `x=30, y=31, S=325, T=289, margin=36, ratio=0.889231, D+/sqrt=1.725947, prime_holes=176, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 47, 'hit_count': 10}]`
- `x=1546, y=1547, S=329, T=292, margin=37, ratio=0.887538, D+/sqrt=1.705831, prime_holes=116, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 12}, {'q': 37, 'hit_count': 10}]`

最少素数洞行：

- `x=1256, y=1257, S=330, T=286, margin=44, ratio=0.866667, D+/sqrt=1.329275, prime_holes=113, top_q=[{'q': 29, 'hit_count': 13}, {'q': 43, 'hit_count': 10}, {'q': 31, 'hit_count': 9}]`
- `x=1411, y=1412, S=325, T=278, margin=47, ratio=0.855385, D+/sqrt=1.115776, prime_holes=113, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 9}, {'q': 37, 'hit_count': 8}]`
- `x=1673, y=1674, S=320, T=273, margin=47, ratio=0.853125, D+/sqrt=1.066739, prime_holes=113, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 37, 'hit_count': 9}]`
- `x=1647, y=1648, S=325, T=273, margin=52, ratio=0.840000, D+/sqrt=0.838426, prime_holes=114, top_q=[{'q': 29, 'hit_count': 13}, {'q': 31, 'hit_count': 10}, {'q': 37, 'hit_count': 10}]`
- `x=1877, y=1878, S=329, T=291, margin=38, ratio=0.884498, D+/sqrt=1.650699, prime_holes=114, top_q=[{'q': 31, 'hit_count': 12}, {'q': 29, 'hit_count': 10}, {'q': 37, 'hit_count': 9}]`
- `x=1910, y=1911, S=325, T=277, margin=48, ratio=0.852308, D+/sqrt=1.060306, prime_holes=114, top_q=[{'q': 29, 'hit_count': 12}, {'q': 31, 'hit_count': 12}, {'q': 37, 'hit_count': 9}]`
- `x=1995, y=1996, S=331, T=280, margin=51, ratio=0.845921, D+/sqrt=0.953862, prime_holes=114, top_q=[{'q': 31, 'hit_count': 11}, {'q': 29, 'hit_count': 10}, {'q': 37, 'hit_count': 10}]`
- `x=1988, y=1989, S=325, T=273, margin=52, ratio=0.840000, D+/sqrt=0.838426, prime_holes=115, top_q=[{'q': 29, 'hit_count': 12}, {'q': 37, 'hit_count': 10}, {'q': 53, 'hit_count': 9}]`

## P=5003

- `cutoff`: `38`
- `H=sum_{P^alpha<q<P}1/q`: `0.812465`
- `min_capacity_margin`: `46`
- `max_hit_ratio`: `0.937922`
- `min_model_over_sqrt`: `5.066922`
- `max_dplus_over_sqrt`: `3.415103`
- `sqrt_c_window`: `1.651820`
- `min_prime_holes`: `260`

最小容量余量行：

- `x=40, y=41, S=741, T=695, margin=46, ratio=0.937922, D+/sqrt=3.415103, prime_holes=397, top_q=[{'q': 41, 'hit_count': 18}, {'q': 43, 'hit_count': 17}, {'q': 47, 'hit_count': 16}]`
- `x=36, y=37, S=746, T=689, margin=57, ratio=0.923592, D+/sqrt=3.035231, prime_holes=404, top_q=[{'q': 41, 'hit_count': 19}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 17}]`
- `x=33, y=34, S=745, T=687, margin=58, ratio=0.922148, D+/sqrt=2.993759, prime_holes=404, top_q=[{'q': 43, 'hit_count': 19}, {'q': 47, 'hit_count': 19}, {'q': 41, 'hit_count': 16}]`
- `x=38, y=39, S=747, T=687, margin=60, ratio=0.919679, D+/sqrt=2.930296, prime_holes=407, top_q=[{'q': 41, 'hit_count': 21}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 15}]`
- `x=52, y=53, S=748, T=679, margin=69, ratio=0.907754, D+/sqrt=2.606121, prime_holes=396, top_q=[{'q': 43, 'hit_count': 19}, {'q': 41, 'hit_count': 16}, {'q': 53, 'hit_count': 14}]`
- `x=42, y=43, S=742, T=672, margin=70, ratio=0.905660, D+/sqrt=2.538618, prime_holes=401, top_q=[{'q': 43, 'hit_count': 18}, {'q': 41, 'hit_count': 15}, {'q': 47, 'hit_count': 14}]`
- `x=46, y=47, S=741, T=671, margin=70, ratio=0.905533, D+/sqrt=2.533441, prime_holes=395, top_q=[{'q': 41, 'hit_count': 20}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 16}]`
- `x=39, y=40, S=746, T=675, margin=71, ratio=0.904826, D+/sqrt=2.522654, prime_holes=411, top_q=[{'q': 47, 'hit_count': 18}, {'q': 43, 'hit_count': 17}, {'q': 41, 'hit_count': 16}]`

最大 T/S 行：

- `x=40, y=41, S=741, T=695, margin=46, ratio=0.937922, D+/sqrt=3.415103, prime_holes=397, top_q=[{'q': 41, 'hit_count': 18}, {'q': 43, 'hit_count': 17}, {'q': 47, 'hit_count': 16}]`
- `x=36, y=37, S=746, T=689, margin=57, ratio=0.923592, D+/sqrt=3.035231, prime_holes=404, top_q=[{'q': 41, 'hit_count': 19}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 17}]`
- `x=33, y=34, S=745, T=687, margin=58, ratio=0.922148, D+/sqrt=2.993759, prime_holes=404, top_q=[{'q': 43, 'hit_count': 19}, {'q': 47, 'hit_count': 19}, {'q': 41, 'hit_count': 16}]`
- `x=38, y=39, S=747, T=687, margin=60, ratio=0.919679, D+/sqrt=2.930296, prime_holes=407, top_q=[{'q': 41, 'hit_count': 21}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 15}]`
- `x=52, y=53, S=748, T=679, margin=69, ratio=0.907754, D+/sqrt=2.606121, prime_holes=396, top_q=[{'q': 43, 'hit_count': 19}, {'q': 41, 'hit_count': 16}, {'q': 53, 'hit_count': 14}]`
- `x=42, y=43, S=742, T=672, margin=70, ratio=0.905660, D+/sqrt=2.538618, prime_holes=401, top_q=[{'q': 43, 'hit_count': 18}, {'q': 41, 'hit_count': 15}, {'q': 47, 'hit_count': 14}]`
- `x=46, y=47, S=741, T=671, margin=70, ratio=0.905533, D+/sqrt=2.533441, prime_holes=395, top_q=[{'q': 41, 'hit_count': 20}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 16}]`
- `x=39, y=40, S=746, T=675, margin=71, ratio=0.904826, D+/sqrt=2.522654, prime_holes=411, top_q=[{'q': 47, 'hit_count': 18}, {'q': 43, 'hit_count': 17}, {'q': 41, 'hit_count': 16}]`

最大相对正偏差行：

- `x=40, y=41, S=741, T=695, margin=46, ratio=0.937922, D+/sqrt=3.415103, prime_holes=397, top_q=[{'q': 41, 'hit_count': 18}, {'q': 43, 'hit_count': 17}, {'q': 47, 'hit_count': 16}]`
- `x=36, y=37, S=746, T=689, margin=57, ratio=0.923592, D+/sqrt=3.035231, prime_holes=404, top_q=[{'q': 41, 'hit_count': 19}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 17}]`
- `x=33, y=34, S=745, T=687, margin=58, ratio=0.922148, D+/sqrt=2.993759, prime_holes=404, top_q=[{'q': 43, 'hit_count': 19}, {'q': 47, 'hit_count': 19}, {'q': 41, 'hit_count': 16}]`
- `x=38, y=39, S=747, T=687, margin=60, ratio=0.919679, D+/sqrt=2.930296, prime_holes=407, top_q=[{'q': 41, 'hit_count': 21}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 15}]`
- `x=52, y=53, S=748, T=679, margin=69, ratio=0.907754, D+/sqrt=2.606121, prime_holes=396, top_q=[{'q': 43, 'hit_count': 19}, {'q': 41, 'hit_count': 16}, {'q': 53, 'hit_count': 14}]`
- `x=42, y=43, S=742, T=672, margin=70, ratio=0.905660, D+/sqrt=2.538618, prime_holes=401, top_q=[{'q': 43, 'hit_count': 18}, {'q': 41, 'hit_count': 15}, {'q': 47, 'hit_count': 14}]`
- `x=46, y=47, S=741, T=671, margin=70, ratio=0.905533, D+/sqrt=2.533441, prime_holes=395, top_q=[{'q': 41, 'hit_count': 20}, {'q': 43, 'hit_count': 18}, {'q': 47, 'hit_count': 16}]`
- `x=39, y=40, S=746, T=675, margin=71, ratio=0.904826, D+/sqrt=2.522654, prime_holes=411, top_q=[{'q': 47, 'hit_count': 18}, {'q': 43, 'hit_count': 17}, {'q': 41, 'hit_count': 16}]`

最少素数洞行：

- `x=4980, y=4981, S=740, T=628, margin=112, ratio=0.848649, D+/sqrt=0.984307, prime_holes=260, top_q=[{'q': 43, 'hit_count': 19}, {'q': 41, 'hit_count': 17}, {'q': 47, 'hit_count': 15}]`
- `x=3778, y=3779, S=740, T=645, margin=95, ratio=0.871622, D+/sqrt=1.609240, prime_holes=264, top_q=[{'q': 41, 'hit_count': 19}, {'q': 43, 'hit_count': 19}, {'q': 47, 'hit_count': 15}]`
- `x=3307, y=3308, S=740, T=639, margin=101, ratio=0.863514, D+/sqrt=1.388675, prime_holes=265, top_q=[{'q': 41, 'hit_count': 18}, {'q': 43, 'hit_count': 17}, {'q': 47, 'hit_count': 16}]`
- `x=4185, y=4186, S=747, T=627, margin=120, ratio=0.839357, D+/sqrt=0.735011, prime_holes=265, top_q=[{'q': 41, 'hit_count': 20}, {'q': 43, 'hit_count': 16}, {'q': 61, 'hit_count': 15}]`
- `x=4126, y=4127, S=742, T=626, margin=116, ratio=0.843666, D+/sqrt=0.849904, prime_holes=266, top_q=[{'q': 41, 'hit_count': 19}, {'q': 53, 'hit_count': 19}, {'q': 43, 'hit_count': 18}]`
- `x=4815, y=4816, S=748, T=635, margin=113, ratio=0.848930, D+/sqrt=0.997322, prime_holes=267, top_q=[{'q': 41, 'hit_count': 20}, {'q': 43, 'hit_count': 19}, {'q': 47, 'hit_count': 17}]`
- `x=4747, y=4748, S=739, T=622, margin=117, ratio=0.841678, D+/sqrt=0.794146, prime_holes=268, top_q=[{'q': 41, 'hit_count': 17}, {'q': 43, 'hit_count': 17}, {'q': 47, 'hit_count': 16}]`
- `x=4956, y=4957, S=743, T=601, margin=142, ratio=0.808883, D+/sqrt=0.000000, prime_holes=268, top_q=[{'q': 41, 'hit_count': 22}, {'q': 43, 'hit_count': 20}, {'q': 47, 'hit_count': 16}]`

## 结构解释

该审计是 `PColumn Anchor-Wheel Field` 的动态提升轮版本。对每个锚点行 `Py-d`，先提升全部 `q<=P^alpha`，得到动态粗骨架 `S_Y(P,y)`；再统计剩余 `P^alpha<q<P` 的总命中 `T_Y(P,y)`。若 `T_Y<S_Y`，则即使不利用重叠扣除，也不可能全覆盖该行骨架。

相对筛余量写成 `S-T=S(1-H)-(T-HS)`，其中 `H=sum_{P^alpha<q<P}1/q`。表中的 `min model/sqrt` 是 `S(1-H)/sqrt(S)` 的最小值，`max D+/sqrt` 是 `max(0,T-HS)/sqrt(S)` 的最大值。若存在常数 `C` 落在二者之间，即 `D+<=C sqrt(S)<S(1-H)`，则解析上推出 `T<S`。

因此若所有行均有正容量余量，说明第 `P` 列锚点场不仅有低模平移刚性，还满足一阶高素容量夹击。剩余证明任务是把 `T_Y<S_Y` 的样本余量升级为解析不等式，或把失败路由到 `PDEC/SAE/ColumnCRT`。
