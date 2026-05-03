# BPN low-hole bucket 固定小高素数碰撞梯审计

**状态：** `fixed_high_prime_collision_ladder_covers_after_turning_point`

固定小高素数碰撞梯按 `13,17,19,23,...` 顺序选择最大列残基块。`Q=2310` 样本中从 `P=61` 起全相位覆盖成功；这比动态贪心更接近符号证明。

## 1. 总表

| P | Q | high # | max holes | success | fail | min margin | top extra-gain primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 53 | 2310 | 10 | 14 | 2266 | 44 | 0 | `[(13, 2124), (17, 1684), (19, 640), (23, 92)]` |
| 59 | 2310 | 11 | 15 | 2274 | 36 | 0 | `[(13, 2254), (17, 1750), (19, 1406), (23, 182)]` |
| 61 | 2310 | 12 | 15 | 2310 | 0 | 0 | `[(13, 2306), (17, 1836), (19, 1664), (23, 240)]` |
| 67 | 2310 | 13 | 16 | 2310 | 0 | 0 | `[(13, 2310), (19, 2020), (17, 1906), (23, 594), (29, 24)]` |
| 71 | 2310 | 14 | 17 | 2310 | 0 | 0 | `[(13, 2310), (19, 2120), (17, 2032), (23, 916), (29, 80), (31, 18)]` |
| 73 | 2310 | 15 | 18 | 2310 | 0 | 1 | `[(13, 2310), (19, 2148), (17, 2084), (23, 1094), (29, 154), (31, 38)]` |
| 79 | 2310 | 16 | 19 | 2310 | 0 | 1 | `[(13, 2310), (17, 2212), (19, 2146), (23, 1490), (29, 394), (31, 134)]` |
| 83 | 2310 | 17 | 20 | 2310 | 0 | 2 | `[(13, 2822), (17, 2210), (19, 2150), (23, 1668), (29, 490), (31, 226)]` |
| 89 | 2310 | 18 | 21 | 2310 | 0 | 2 | `[(13, 3514), (17, 2276), (19, 2186), (23, 1830), (31, 686), (29, 574)]` |
| 97 | 2310 | 19 | 23 | 2310 | 0 | 2 | `[(13, 4042), (17, 2300), (19, 2258), (23, 1944), (31, 1320), (29, 966)]` |
| 101 | 2310 | 20 | 24 | 2310 | 0 | 2 | `[(13, 4242), (17, 2302), (19, 2282), (23, 2002), (31, 1492), (29, 1246)]` |
| 103 | 2310 | 21 | 25 | 2310 | 0 | 3 | `[(13, 4302), (17, 2304), (19, 2290), (23, 2040), (31, 1536), (29, 1356)]` |
| 107 | 2310 | 22 | 25 | 2310 | 0 | 4 | `[(13, 4470), (17, 2606), (19, 2304), (23, 2096), (31, 1686), (29, 1508)]` |
| 109 | 2310 | 23 | 25 | 2310 | 0 | 5 | `[(13, 4578), (17, 2732), (19, 2310), (23, 2156), (31, 1720), (29, 1564)]` |
| 127 | 2310 | 25 | 28 | 2310 | 0 | 5 | `[(13, 5078), (17, 3802), (19, 2690), (23, 2304), (31, 1998), (29, 1988)]` |
| 149 | 2310 | 29 | 34 | 2310 | 0 | 6 | `[(13, 5984), (17, 4410), (19, 3894), (23, 2574), (29, 2204), (31, 2158)]` |

## 2. 固定碰撞梯证书

固定顺序为所有高素数升序排列。第 `j` 步只允许使用第 `j` 个尚可用高素数，
并选择当前未覆盖洞中最大的一个列残基块。若固定顺序也能覆盖全部低洞，
则不需要依赖动态贪心的选择自由。

该证书把转折后目标压成：小高素数升序碰撞梯提供足够重复增益。

## 3. 最大洞数样例

### P=53

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[6, 10, 12, 16, 22, 24, 30, 34, 36, 40, 52]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 10, 'hit': [10, 36], 'gain': 2}, {'prime': 17, 'residue': 6, 'hit': [6, 40], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 4, 'hit': [17, 43], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}]` |
| 2 | `[6, 8, 14, 18, 20, 26, 30, 36, 44, 48, 50]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 5, 'hit': [18, 44], 'gain': 2}, {'prime': 17, 'residue': 14, 'hit': [14, 48], 'gain': 2}]` |
| 4 | `[4, 8, 10, 14, 20, 22, 32, 34, 38, 40, 52]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 8, 'hit': [8, 34], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}]` |

### P=59

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[6, 12, 16, 18, 22, 28, 30, 36, 40, 42, 46, 58]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 6, 'hit': [6, 58], 'gain': 2}, {'prime': 17, 'residue': 12, 'hit': [12, 46], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}]` |
| 2 | `[2, 8, 12, 14, 20, 24, 30, 38, 42, 44, 48, 50, 54]` | 3 | 2 | 1 | `[{'prime': 13, 'residue': 2, 'hit': [2, 54], 'gain': 2}, {'prime': 17, 'residue': 8, 'hit': [8, 42], 'gain': 2}, {'prime': 19, 'residue': 12, 'hit': [12, 50], 'gain': 2}]` |
| 5 | `[3, 5, 11, 15, 21, 27, 33, 35, 41, 45, 47, 53, 57]` | 3 | 2 | 1 | `[{'prime': 13, 'residue': 5, 'hit': [5, 57], 'gain': 2}, {'prime': 17, 'residue': 11, 'hit': [11, 45], 'gain': 2}, {'prime': 19, 'residue': 3, 'hit': [3, 41], 'gain': 2}]` |

### P=61

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[2, 8, 14, 18, 20, 24, 30, 32, 38, 42, 44, 48, 60]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 8, 'hit': [8, 60], 'gain': 2}, {'prime': 17, 'residue': 14, 'hit': [14, 48], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}]` |
| 3 | `[5, 9, 15, 17, 27, 29, 35, 41, 45, 47, 51, 57, 59]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 5, 'hit': [5, 57], 'gain': 2}, {'prime': 17, 'residue': 0, 'hit': [17, 51], 'gain': 2}, {'prime': 19, 'residue': 9, 'hit': [9, 47], 'gain': 2}]` |
| 7 | `[1, 7, 11, 13, 17, 23, 25, 31, 35, 37, 43, 53, 55]` | 2 | 1 | 1 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 19, 'residue': 17, 'hit': [17, 55], 'gain': 2}]` |

### P=67

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[6, 8, 14, 20, 24, 26, 30, 36, 38, 44, 48, 50, 54, 66]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [14, 66], 'gain': 2}, {'prime': 17, 'residue': 3, 'hit': [20, 54], 'gain': 2}, {'prime': 19, 'residue': 6, 'hit': [6, 44], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}]` |
| 3 | `[3, 5, 15, 17, 23, 29, 33, 35, 39, 45, 47, 57, 59, 63, 65]` | 3 | 2 | 1 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [5, 39], 'gain': 2}, {'prime': 23, 'residue': 17, 'hit': [17, 63], 'gain': 2}]` |
| 6 | `[2, 12, 14, 18, 24, 26, 32, 38, 42, 44, 48, 54, 56, 62, 66]` | 3 | 2 | 1 | `[{'prime': 13, 'residue': 2, 'hit': [2, 54], 'gain': 2}, {'prime': 17, 'residue': 14, 'hit': [14, 48], 'gain': 2}, {'prime': 19, 'residue': 18, 'hit': [18, 56], 'gain': 2}]` |

### P=71

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[4, 10, 12, 18, 24, 28, 30, 34, 40, 42, 48, 52, 54, 58, 70]` | 4 | 1 | 3 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30], 'gain': 2}, {'prime': 17, 'residue': 1, 'hit': [18, 52], 'gain': 2}, {'prime': 19, 'residue': 10, 'hit': [10, 48], 'gain': 2}, {'prime': 23, 'residue': 12, 'hit': [12, 58], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}]` |
| 4 | `[8, 10, 14, 16, 20, 26, 28, 34, 38, 44, 50, 56, 58, 64, 68, 70]` | 3 | 2 | 1 | `[{'prime': 13, 'residue': 8, 'hit': [8, 34], 'gain': 2}, {'prime': 17, 'residue': 10, 'hit': [10, 44], 'gain': 2}, {'prime': 19, 'residue': 1, 'hit': [20, 58], 'gain': 2}]` |
| 10 | `[2, 4, 8, 14, 20, 22, 28, 34, 38, 44, 50, 52, 58, 62, 64, 70]` | 4 | 2 | 2 | `[{'prime': 13, 'residue': 2, 'hit': [2, 28], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}, {'prime': 31, 'residue': 8, 'hit': [8, 70], 'gain': 2}]` |

### P=73

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[2, 6, 12, 14, 20, 26, 30, 32, 36, 42, 44, 50, 54, 56, 60, 72]` | 4 | 1 | 3 | `[{'prime': 13, 'residue': 2, 'hit': [2, 54], 'gain': 2}, {'prime': 17, 'residue': 9, 'hit': [26, 60], 'gain': 2}, {'prime': 19, 'residue': 6, 'hit': [6, 44], 'gain': 2}, {'prime': 29, 'residue': 14, 'hit': [14, 72], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}]` |
| 4 | `[2, 4, 8, 10, 14, 20, 22, 28, 32, 38, 44, 50, 52, 58, 62, 64, 70]` | 4 | 2 | 2 | `[{'prime': 13, 'residue': 2, 'hit': [2, 28], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}, {'prime': 31, 'residue': 8, 'hit': [8, 70], 'gain': 2}]` |
| 50 | `[4, 6, 10, 12, 16, 22, 24, 30, 34, 36, 40, 46, 52, 54, 60, 66, 72]` | 3 | 2 | 1 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30], 'gain': 2}, {'prime': 17, 'residue': 6, 'hit': [6, 40], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}]` |

### P=79

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[6, 8, 12, 18, 20, 26, 32, 36, 38, 42, 48, 50, 56, 60, 62, 66, 78]` | 4 | 1 | 3 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32], 'gain': 2}, {'prime': 17, 'residue': 8, 'hit': [8, 42], 'gain': 2}, {'prime': 19, 'residue': 12, 'hit': [12, 50], 'gain': 2}, {'prime': 23, 'residue': 20, 'hit': [20, 66], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}]` |
| 4 | `[2, 4, 10, 14, 20, 26, 32, 34, 40, 44, 46, 52, 56, 62, 70, 74, 76]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 4, 'hit': [4, 56], 'gain': 2}, {'prime': 17, 'residue': 2, 'hit': [2, 70], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}]` |
| 8 | `[4, 6, 10, 16, 18, 24, 34, 36, 40, 46, 48, 54, 58, 60, 64, 66, 76, 78]` | 4 | 2 | 2 | `[{'prime': 13, 'residue': 6, 'hit': [6, 58], 'gain': 2}, {'prime': 17, 'residue': 10, 'hit': [10, 78], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}, {'prime': 23, 'residue': 18, 'hit': [18, 64], 'gain': 2}]` |

### P=83

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[4, 10, 12, 16, 22, 24, 30, 36, 40, 42, 46, 52, 54, 60, 64, 66, 70, 82]` | 5 | 1 | 4 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30, 82], 'gain': 3}, {'prime': 17, 'residue': 12, 'hit': [12, 46], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}, {'prime': 23, 'residue': 1, 'hit': [24, 70], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]` | 4 | 1 | 3 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}]` |
| 3 | `[1, 3, 7, 13, 15, 25, 27, 31, 33, 45, 55, 57, 61, 63, 67, 73, 75, 81]` | 5 | 1 | 4 | `[{'prime': 13, 'residue': 3, 'hit': [3, 55, 81], 'gain': 3}, {'prime': 17, 'residue': 7, 'hit': [7, 75], 'gain': 2}, {'prime': 19, 'residue': 6, 'hit': [25, 63], 'gain': 2}, {'prime': 23, 'residue': 15, 'hit': [15, 61], 'gain': 2}]` |
| 8 | `[6, 8, 12, 18, 20, 26, 30, 32, 36, 38, 48, 50, 60, 62, 66, 72, 78, 80]` | 3 | 1 | 2 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32], 'gain': 2}, {'prime': 17, 'residue': 12, 'hit': [12, 80], 'gain': 2}, {'prime': 23, 'residue': 20, 'hit': [20, 66], 'gain': 2}]` |

### P=89

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[6, 10, 16, 18, 22, 28, 30, 36, 42, 46, 48, 52, 58, 60, 66, 70, 72, 76, 88]` | 5 | 1 | 4 | `[{'prime': 13, 'residue': 10, 'hit': [10, 36, 88], 'gain': 3}, {'prime': 17, 'residue': 1, 'hit': [18, 52], 'gain': 2}, {'prime': 19, 'residue': 3, 'hit': [22, 60], 'gain': 2}, {'prime': 23, 'residue': 7, 'hit': [30, 76], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]` | 5 | 1 | 4 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}, {'prime': 23, 'residue': 14, 'hit': [37, 83], 'gain': 2}]` |
| 5 | `[3, 5, 11, 17, 21, 23, 27, 33, 35, 41, 45, 47, 53, 63, 65, 75, 77, 81, 83, 87]` | 5 | 2 | 3 | `[{'prime': 13, 'residue': 3, 'hit': [3, 81], 'gain': 2}, {'prime': 17, 'residue': 11, 'hit': [11, 45], 'gain': 2}, {'prime': 19, 'residue': 8, 'hit': [27, 65], 'gain': 2}, {'prime': 23, 'residue': 17, 'hit': [17, 63], 'gain': 2}, {'prime': 31, 'residue': 21, 'hit': [21, 83], 'gain': 2}]` |
| 15 | `[1, 3, 13, 15, 25, 27, 31, 33, 37, 43, 45, 51, 55, 57, 61, 67, 73, 75, 81, 87]` | 6 | 2 | 4 | `[{'prime': 13, 'residue': 3, 'hit': [3, 55, 81], 'gain': 3}, {'prime': 17, 'residue': 10, 'hit': [27, 61], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}, {'prime': 29, 'residue': 15, 'hit': [15, 73], 'gain': 2}, {'prime': 31, 'residue': 25, 'hit': [25, 87], 'gain': 2}]` |

### P=97

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[8, 14, 18, 24, 26, 30, 36, 38, 44, 50, 54, 56, 60, 66, 68, 74, 78, 80, 84, 96]` | 4 | 1 | 3 | `[{'prime': 13, 'residue': 5, 'hit': [18, 44, 96], 'gain': 3}, {'prime': 17, 'residue': 9, 'hit': [26, 60], 'gain': 2}, {'prime': 19, 'residue': 8, 'hit': [8, 84], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]` | 6 | 1 | 5 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}, {'prime': 23, 'residue': 14, 'hit': [37, 83], 'gain': 2}, {'prime': 29, 'residue': 2, 'hit': [31, 89], 'gain': 2}]` |
| 2 | `[4, 6, 10, 12, 16, 30, 34, 40, 42, 52, 54, 60, 66, 70, 72, 76, 82, 84, 94, 96]` | 6 | 1 | 5 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30, 82], 'gain': 3}, {'prime': 17, 'residue': 6, 'hit': [6, 40], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}, {'prime': 29, 'residue': 12, 'hit': [12, 70], 'gain': 2}, {'prime': 31, 'residue': 10, 'hit': [10, 72], 'gain': 2}]` |
| 3 | `[3, 5, 17, 27, 29, 33, 35, 39, 45, 47, 53, 57, 63, 69, 75, 77, 83, 87, 89, 95]` | 6 | 1 | 5 | `[{'prime': 13, 'residue': 5, 'hit': [5, 57, 83], 'gain': 3}, {'prime': 17, 'residue': 10, 'hit': [27, 95], 'gain': 2}, {'prime': 19, 'residue': 1, 'hit': [39, 77], 'gain': 2}, {'prime': 23, 'residue': 17, 'hit': [17, 63], 'gain': 2}, {'prime': 29, 'residue': 0, 'hit': [29, 87], 'gain': 2}]` |

### P=101

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[4, 12, 18, 22, 28, 30, 34, 40, 42, 48, 54, 58, 60, 64, 70, 72, 78, 82, 84, 88, 100]` | 6 | 1 | 5 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30, 82], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [54, 88], 'gain': 2}, {'prime': 19, 'residue': 3, 'hit': [22, 60], 'gain': 2}, {'prime': 23, 'residue': 12, 'hit': [12, 58], 'gain': 2}, {'prime': 29, 'residue': 13, 'hit': [42, 100], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]` | 6 | 1 | 5 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}, {'prime': 23, 'residue': 14, 'hit': [37, 83], 'gain': 2}, {'prime': 29, 'residue': 2, 'hit': [31, 89], 'gain': 2}]` |
| 2 | `[2, 6, 8, 12, 26, 30, 36, 38, 48, 50, 56, 62, 66, 68, 72, 78, 80, 90, 92, 96, 98]` | 6 | 1 | 5 | `[{'prime': 13, 'residue': 12, 'hit': [12, 38, 90], 'gain': 3}, {'prime': 17, 'residue': 2, 'hit': [2, 36], 'gain': 2}, {'prime': 19, 'residue': 11, 'hit': [30, 68], 'gain': 2}, {'prime': 23, 'residue': 6, 'hit': [6, 98], 'gain': 2}, {'prime': 29, 'residue': 8, 'hit': [8, 66], 'gain': 2}]` |
| 4 | `[4, 8, 10, 14, 20, 28, 34, 44, 46, 50, 56, 58, 64, 70, 74, 76, 80, 86, 88, 94, 98, 100]` | 6 | 2 | 4 | `[{'prime': 13, 'residue': 8, 'hit': [8, 34, 86], 'gain': 3}, {'prime': 17, 'residue': 10, 'hit': [10, 44], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [4, 80], 'gain': 2}, {'prime': 23, 'residue': 5, 'hit': [28, 74], 'gain': 2}, {'prime': 37, 'residue': 20, 'hit': [20, 94], 'gain': 2}]` |

### P=103

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[2, 6, 14, 20, 24, 30, 32, 36, 42, 44, 50, 56, 60, 62, 66, 72, 74, 80, 84, 86, 90, 102]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32, 84], 'gain': 3}, {'prime': 17, 'residue': 2, 'hit': [2, 36], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 90], 'gain': 2}, {'prime': 23, 'residue': 20, 'hit': [20, 66], 'gain': 2}, {'prime': 29, 'residue': 15, 'hit': [44, 102], 'gain': 2}, {'prime': 31, 'residue': 24, 'hit': [24, 86], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]` | 6 | 1 | 5 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}, {'prime': 23, 'residue': 14, 'hit': [37, 83], 'gain': 2}, {'prime': 29, 'residue': 2, 'hit': [31, 89], 'gain': 2}]` |
| 4 | `[2, 4, 8, 14, 22, 28, 38, 40, 44, 50, 52, 58, 64, 68, 70, 74, 80, 82, 88, 92, 94, 100]` | 5 | 1 | 4 | `[{'prime': 13, 'residue': 2, 'hit': [2, 28, 80], 'gain': 3}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}, {'prime': 23, 'residue': 8, 'hit': [8, 100], 'gain': 2}]` |
| 6 | `[6, 8, 12, 14, 18, 26, 32, 36, 42, 44, 48, 54, 56, 62, 72, 74, 78, 84, 86, 92, 96, 98, 102]` | 8 | 2 | 6 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32, 84], 'gain': 3}, {'prime': 17, 'residue': 8, 'hit': [8, 42], 'gain': 2}, {'prime': 19, 'residue': 18, 'hit': [18, 56], 'gain': 2}, {'prime': 23, 'residue': 3, 'hit': [26, 72], 'gain': 2}, {'prime': 29, 'residue': 15, 'hit': [44, 102], 'gain': 2}, {'prime': 31, 'residue': 12, 'hit': [12, 74], 'gain': 2}, {'prime': 41, 'residue': 14, 'hit': [14, 96], 'gain': 2}]` |

### P=107

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[4, 6, 10, 18, 24, 28, 34, 36, 40, 46, 48, 54, 60, 64, 66, 70, 76, 78, 84, 88, 90, 94, 106]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 10, 'hit': [10, 36, 88], 'gain': 3}, {'prime': 17, 'residue': 4, 'hit': [4, 106], 'gain': 2}, {'prime': 19, 'residue': 18, 'hit': [18, 94], 'gain': 2}, {'prime': 23, 'residue': 1, 'hit': [24, 70], 'gain': 2}, {'prime': 29, 'residue': 6, 'hit': [6, 64], 'gain': 2}, {'prime': 31, 'residue': 28, 'hit': [28, 90], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]` | 8 | 1 | 7 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}, {'prime': 23, 'residue': 14, 'hit': [37, 83], 'gain': 2}, {'prime': 29, 'residue': 2, 'hit': [31, 89], 'gain': 2}, {'prime': 31, 'residue': 10, 'hit': [41, 103], 'gain': 2}, {'prime': 41, 'residue': 19, 'hit': [19, 101], 'gain': 2}]` |
| 3 | `[7, 9, 13, 15, 19, 25, 27, 33, 37, 43, 49, 55, 57, 63, 67, 69, 75, 79, 85, 93, 97, 99, 103]` | 5 | 1 | 4 | `[{'prime': 13, 'residue': 7, 'hit': [7, 33, 85], 'gain': 3}, {'prime': 17, 'residue': 9, 'hit': [9, 43], 'gain': 2}, {'prime': 19, 'residue': 0, 'hit': [19, 57], 'gain': 2}, {'prime': 31, 'residue': 13, 'hit': [13, 75], 'gain': 2}]` |
| 5 | `[3, 5, 9, 11, 15, 21, 29, 33, 35, 39, 51, 53, 59, 63, 65, 71, 75, 81, 93, 95, 99, 101, 105]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29, 81], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [71, 105], 'gain': 2}, {'prime': 19, 'residue': 15, 'hit': [15, 53], 'gain': 2}, {'prime': 23, 'residue': 5, 'hit': [5, 51], 'gain': 2}, {'prime': 29, 'residue': 6, 'hit': [35, 93], 'gain': 2}, {'prime': 31, 'residue': 2, 'hit': [33, 95], 'gain': 2}]` |

### P=109

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[2, 6, 8, 12, 20, 26, 30, 36, 38, 42, 48, 50, 56, 62, 66, 68, 72, 78, 80, 86, 90, 92, 96, 108]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 12, 'hit': [12, 38, 90], 'gain': 3}, {'prime': 17, 'residue': 2, 'hit': [2, 36], 'gain': 2}, {'prime': 19, 'residue': 1, 'hit': [20, 96], 'gain': 2}, {'prime': 23, 'residue': 3, 'hit': [26, 72], 'gain': 2}, {'prime': 29, 'residue': 8, 'hit': [8, 66], 'gain': 2}, {'prime': 31, 'residue': 6, 'hit': [6, 68], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107]` | 8 | 1 | 7 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}, {'prime': 23, 'residue': 14, 'hit': [37, 83], 'gain': 2}, {'prime': 29, 'residue': 2, 'hit': [31, 89], 'gain': 2}, {'prime': 31, 'residue': 10, 'hit': [41, 103], 'gain': 2}, {'prime': 41, 'residue': 19, 'hit': [19, 101], 'gain': 2}]` |
| 3 | `[3, 5, 9, 11, 15, 21, 23, 29, 33, 39, 45, 51, 53, 59, 63, 65, 71, 75, 81, 89, 93, 95, 99, 105]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29, 81], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [71, 105], 'gain': 2}, {'prime': 19, 'residue': 15, 'hit': [15, 53], 'gain': 2}, {'prime': 23, 'residue': 5, 'hit': [5, 51], 'gain': 2}, {'prime': 31, 'residue': 2, 'hit': [33, 95], 'gain': 2}, {'prime': 41, 'residue': 11, 'hit': [11, 93], 'gain': 2}]` |
| 6 | `[2, 6, 12, 14, 18, 24, 26, 32, 42, 44, 48, 54, 56, 62, 66, 68, 72, 74, 84, 86, 96, 98, 102, 108]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32, 84], 'gain': 3}, {'prime': 17, 'residue': 6, 'hit': [74, 108], 'gain': 2}, {'prime': 19, 'residue': 18, 'hit': [18, 56], 'gain': 2}, {'prime': 23, 'residue': 2, 'hit': [2, 48], 'gain': 2}, {'prime': 29, 'residue': 14, 'hit': [14, 72], 'gain': 2}, {'prime': 31, 'residue': 24, 'hit': [24, 86], 'gain': 2}]` |

### P=127

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[14, 18, 20, 24, 26, 30, 38, 44, 48, 54, 56, 60, 66, 68, 74, 80, 84, 86, 90, 96, 98, 104, 108, 110, 114, 126]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 5, 'hit': [18, 44, 96], 'gain': 3}, {'prime': 17, 'residue': 14, 'hit': [14, 48], 'gain': 2}, {'prime': 19, 'residue': 11, 'hit': [30, 68], 'gain': 2}, {'prime': 23, 'residue': 20, 'hit': [20, 66], 'gain': 2}, {'prime': 29, 'residue': 26, 'hit': [26, 84], 'gain': 2}, {'prime': 31, 'residue': 24, 'hit': [24, 86], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]` | 7 | 1 | 6 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 4, 'hit': [23, 61], 'gain': 2}, {'prime': 23, 'residue': 17, 'hit': [17, 109], 'gain': 2}, {'prime': 29, 'residue': 2, 'hit': [31, 89], 'gain': 2}, {'prime': 31, 'residue': 10, 'hit': [41, 103], 'gain': 2}]` |
| 2 | `[4, 10, 12, 22, 24, 30, 36, 40, 42, 46, 52, 54, 64, 66, 70, 72, 84, 94, 96, 100, 102, 106, 112, 114, 120, 124]` | 10 | 1 | 9 | `[{'prime': 13, 'residue': 10, 'hit': [10, 36, 114], 'gain': 3}, {'prime': 17, 'residue': 4, 'hit': [4, 72, 106], 'gain': 3}, {'prime': 19, 'residue': 5, 'hit': [24, 100], 'gain': 2}, {'prime': 23, 'residue': 20, 'hit': [66, 112], 'gain': 2}, {'prime': 29, 'residue': 12, 'hit': [12, 70], 'gain': 2}, {'prime': 31, 'residue': 22, 'hit': [22, 84], 'gain': 2}, {'prime': 37, 'residue': 9, 'hit': [46, 120], 'gain': 2}, {'prime': 41, 'residue': 1, 'hit': [42, 124], 'gain': 2}]` |
| 3 | `[3, 9, 15, 17, 23, 27, 29, 35, 39, 45, 53, 57, 59, 63, 69, 77, 83, 93, 95, 99, 105, 107, 113, 119, 123, 125]` | 9 | 1 | 8 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29, 107], 'gain': 3}, {'prime': 17, 'residue': 6, 'hit': [23, 57, 125], 'gain': 3}, {'prime': 19, 'residue': 9, 'hit': [9, 123], 'gain': 2}, {'prime': 23, 'residue': 17, 'hit': [17, 63], 'gain': 2}, {'prime': 29, 'residue': 6, 'hit': [35, 93], 'gain': 2}, {'prime': 31, 'residue': 15, 'hit': [15, 77], 'gain': 2}, {'prime': 37, 'residue': 2, 'hit': [39, 113], 'gain': 2}]` |

### P=149

| phase | holes | duplicate gain | required gain | margin | multi-gain choices |
| ---: | --- | ---: | ---: | ---: | --- |
| 0 | `[10, 12, 18, 22, 36, 40, 42, 46, 48, 52, 60, 66, 70, 76, 78, 82, 88, 90, 96, 102, 106, 108, 112, 118, 120, 126, 130, 132, 136, 148]` | 12 | 1 | 11 | `[{'prime': 13, 'residue': 5, 'hit': [18, 70, 96, 148], 'gain': 4}, {'prime': 17, 'residue': 10, 'hit': [10, 78, 112], 'gain': 3}, {'prime': 19, 'residue': 12, 'hit': [12, 88, 126], 'gain': 3}, {'prime': 23, 'residue': 13, 'hit': [36, 82], 'gain': 2}, {'prime': 29, 'residue': 19, 'hit': [48, 106], 'gain': 2}, {'prime': 31, 'residue': 9, 'hit': [40, 102], 'gain': 2}, {'prime': 37, 'residue': 9, 'hit': [46, 120], 'gain': 2}, {'prime': 47, 'residue': 42, 'hit': [42, 136], 'gain': 2}]` |
| 1 | `[1, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]` | 12 | 1 | 11 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79, 131], 'gain': 4}, {'prime': 17, 'residue': 3, 'hit': [37, 71, 139], 'gain': 3}, {'prime': 19, 'residue': 13, 'hit': [13, 89, 127], 'gain': 3}, {'prime': 23, 'residue': 17, 'hit': [17, 109], 'gain': 2}, {'prime': 29, 'residue': 14, 'hit': [43, 101], 'gain': 2}, {'prime': 31, 'residue': 10, 'hit': [41, 103], 'gain': 2}, {'prime': 37, 'residue': 23, 'hit': [23, 97], 'gain': 2}, {'prime': 41, 'residue': 31, 'hit': [31, 113], 'gain': 2}]` |
| 2 | `[2, 8, 14, 18, 20, 24, 30, 32, 42, 44, 48, 50, 62, 72, 74, 78, 80, 84, 90, 92, 98, 102, 108, 114, 120, 122, 128, 132, 134, 140, 144]` | 10 | 2 | 8 | `[{'prime': 13, 'residue': 11, 'hit': [24, 50, 102, 128], 'gain': 4}, {'prime': 17, 'residue': 8, 'hit': [8, 42, 144], 'gain': 3}, {'prime': 19, 'residue': 2, 'hit': [2, 78], 'gain': 2}, {'prime': 23, 'residue': 2, 'hit': [48, 140], 'gain': 2}, {'prime': 29, 'residue': 14, 'hit': [14, 72], 'gain': 2}, {'prime': 31, 'residue': 18, 'hit': [18, 80], 'gain': 2}, {'prime': 41, 'residue': 32, 'hit': [32, 114], 'gain': 2}]` |
| 3 | `[1, 9, 13, 15, 19, 25, 33, 39, 49, 51, 55, 61, 63, 69, 75, 79, 81, 85, 91, 93, 99, 103, 105, 111, 121, 123, 133, 135, 139, 141, 145]` | 12 | 2 | 10 | `[{'prime': 13, 'residue': 1, 'hit': [1, 79, 105], 'gain': 3}, {'prime': 17, 'residue': 9, 'hit': [9, 111, 145], 'gain': 3}, {'prime': 19, 'residue': 6, 'hit': [25, 63, 139], 'gain': 3}, {'prime': 23, 'residue': 15, 'hit': [15, 61], 'gain': 2}, {'prime': 29, 'residue': 19, 'hit': [19, 135], 'gain': 2}, {'prime': 31, 'residue': 13, 'hit': [13, 75], 'gain': 2}, {'prime': 37, 'residue': 12, 'hit': [49, 123], 'gain': 2}, {'prime': 41, 'residue': 39, 'hit': [39, 121], 'gain': 2}, {'prime': 43, 'residue': 12, 'hit': [55, 141], 'gain': 2}]` |


## 4. 失败样例

### P=53

| phase | holes | uncovered | first choices |
| ---: | --- | --- | --- |
| 130 | `[4, 10, 14, 20, 22, 26, 32, 34, 40, 46, 50, 52]` | `[52]` | `[{'prime': 13, 'residue': 1, 'hit': [14, 40], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4], 'gain': 1}, {'prime': 19, 'residue': 10, 'hit': [10], 'gain': 1}, {'prime': 23, 'residue': 4, 'hit': [50], 'gain': 1}, {'prime': 29, 'residue': 20, 'hit': [20], 'gain': 1}, {'prime': 31, 'residue': 22, 'hit': [22], 'gain': 1}, {'prime': 37, 'residue': 26, 'hit': [26], 'gain': 1}, {'prime': 41, 'residue': 32, 'hit': [32], 'gain': 1}]` |
| 194 | `[2, 8, 14, 18, 20, 24, 30, 32, 38, 42, 44, 48, 50]` | `[50]` | `[{'prime': 13, 'residue': 5, 'hit': [18, 44], 'gain': 2}, {'prime': 17, 'residue': 8, 'hit': [8, 42], 'gain': 2}, {'prime': 19, 'residue': 2, 'hit': [2], 'gain': 1}, {'prime': 23, 'residue': 2, 'hit': [48], 'gain': 1}, {'prime': 29, 'residue': 14, 'hit': [14], 'gain': 1}, {'prime': 31, 'residue': 20, 'hit': [20], 'gain': 1}, {'prime': 37, 'residue': 24, 'hit': [24], 'gain': 1}, {'prime': 41, 'residue': 30, 'hit': [30], 'gain': 1}]` |
| 199 | `[5, 7, 17, 19, 23, 25, 29, 35, 37, 43, 47, 49]` | `[49]` | `[{'prime': 13, 'residue': 4, 'hit': [17, 43], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [5], 'gain': 1}, {'prime': 19, 'residue': 7, 'hit': [7], 'gain': 1}, {'prime': 23, 'residue': 19, 'hit': [19], 'gain': 1}, {'prime': 29, 'residue': 23, 'hit': [23], 'gain': 1}, {'prime': 31, 'residue': 25, 'hit': [25], 'gain': 1}, {'prime': 37, 'residue': 29, 'hit': [29], 'gain': 1}, {'prime': 41, 'residue': 35, 'hit': [35], 'gain': 1}]` |
| 207 | `[1, 3, 13, 15, 19, 21, 25, 31, 33, 39, 43, 45]` | `[45]` | `[{'prime': 13, 'residue': 0, 'hit': [13, 39], 'gain': 2}, {'prime': 17, 'residue': 1, 'hit': [1], 'gain': 1}, {'prime': 19, 'residue': 3, 'hit': [3], 'gain': 1}, {'prime': 23, 'residue': 15, 'hit': [15], 'gain': 1}, {'prime': 29, 'residue': 19, 'hit': [19], 'gain': 1}, {'prime': 31, 'residue': 21, 'hit': [21], 'gain': 1}, {'prime': 37, 'residue': 25, 'hit': [25], 'gain': 1}, {'prime': 41, 'residue': 31, 'hit': [31], 'gain': 1}]` |

### P=59

| phase | holes | uncovered | first choices |
| ---: | --- | --- | --- |
| 33 | `[1, 3, 13, 19, 21, 25, 31, 33, 39, 43, 45, 49, 55]` | `[45]` | `[{'prime': 13, 'residue': 3, 'hit': [3, 55], 'gain': 2}, {'prime': 17, 'residue': 1, 'hit': [1], 'gain': 1}, {'prime': 19, 'residue': 1, 'hit': [39], 'gain': 1}, {'prime': 23, 'residue': 3, 'hit': [49], 'gain': 1}, {'prime': 29, 'residue': 13, 'hit': [13], 'gain': 1}, {'prime': 31, 'residue': 19, 'hit': [19], 'gain': 1}, {'prime': 37, 'residue': 21, 'hit': [21], 'gain': 1}, {'prime': 41, 'residue': 25, 'hit': [25], 'gain': 1}]` |
| 46 | `[2, 4, 8, 14, 16, 22, 28, 32, 34, 38, 44, 46, 52, 56, 58]` | `[58]` | `[{'prime': 13, 'residue': 2, 'hit': [2, 28], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 8, 'hit': [8, 46], 'gain': 2}, {'prime': 23, 'residue': 14, 'hit': [14], 'gain': 1}, {'prime': 29, 'residue': 16, 'hit': [16], 'gain': 1}, {'prime': 31, 'residue': 22, 'hit': [22], 'gain': 1}, {'prime': 37, 'residue': 32, 'hit': [32], 'gain': 1}, {'prime': 41, 'residue': 34, 'hit': [34], 'gain': 1}]` |
| 186 | `[4, 6, 16, 18, 22, 24, 28, 34, 36, 42, 46, 48, 58]` | `[48]` | `[{'prime': 13, 'residue': 6, 'hit': [6, 58], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4], 'gain': 1}, {'prime': 19, 'residue': 4, 'hit': [42], 'gain': 1}, {'prime': 23, 'residue': 16, 'hit': [16], 'gain': 1}, {'prime': 29, 'residue': 18, 'hit': [18], 'gain': 1}, {'prime': 31, 'residue': 22, 'hit': [22], 'gain': 1}, {'prime': 37, 'residue': 24, 'hit': [24], 'gain': 1}, {'prime': 41, 'residue': 28, 'hit': [28], 'gain': 1}]` |
| 253 | `[1, 5, 11, 13, 19, 23, 25, 29, 31, 41, 43, 53, 55]` | `[55]` | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [5], 'gain': 1}, {'prime': 19, 'residue': 5, 'hit': [43], 'gain': 1}, {'prime': 23, 'residue': 11, 'hit': [11], 'gain': 1}, {'prime': 29, 'residue': 13, 'hit': [13], 'gain': 1}, {'prime': 31, 'residue': 19, 'hit': [19], 'gain': 1}, {'prime': 37, 'residue': 23, 'hit': [23], 'gain': 1}, {'prime': 41, 'residue': 25, 'hit': [25], 'gain': 1}]` |
