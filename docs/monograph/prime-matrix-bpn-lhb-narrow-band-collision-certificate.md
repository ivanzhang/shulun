# BPN LHB 窄带碰撞能量证书

十个窄带素数的固定升序碰撞梯全相位通过；碰撞能量余量 `duplicate_gain-required_gain` 均非负。

## 1. 总表

| P | phases | high # | max holes | max required | failures | min surplus | min margin | sha256 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 61 | 2310 | 12 | 15 | 3 | 0 | 0 | 0 | `e893620a08a8fcf2` |
| 67 | 2310 | 13 | 16 | 3 | 0 | 0 | 0 | `2965540884e51c34` |
| 71 | 2310 | 14 | 17 | 3 | 0 | 0 | 0 | `aadef8e7c1215626` |
| 73 | 2310 | 15 | 18 | 3 | 0 | 1 | 1 | `543e145cde7b077b` |
| 79 | 2310 | 16 | 19 | 3 | 0 | 1 | 1 | `3fcd7e852d860436` |
| 83 | 2310 | 17 | 20 | 3 | 0 | 2 | 2 | `9ac8405672c2ab87` |
| 89 | 2310 | 18 | 21 | 3 | 0 | 2 | 2 | `c07b861b221e96e7` |
| 97 | 2310 | 19 | 23 | 4 | 0 | 2 | 2 | `1d76474025de229c` |
| 101 | 2310 | 20 | 24 | 4 | 0 | 2 | 2 | `2eb2926f675c2586` |
| 103 | 2310 | 21 | 25 | 4 | 0 | 3 | 3 | `b8502cff44b54ba0` |

## 2. 紧相位样例

仅列出每个 `P` 最紧的前若干相位；完整摘要哈希在 JSON 中。

### P=61

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 22 | 13 | 12 | 0 | 0 | `[{'prime': 13, 'residue': 7, 'hit': [20, 46], 'gain': 2}]` |
| 77 | 15 | 12 | 0 | 0 | `[{'prime': 13, 'residue': 1, 'hit': [1, 27], 'gain': 2}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 7, 'hit': [7, 45], 'gain': 2}]` |
| 108 | 14 | 12 | 0 | 0 | `[{'prime': 13, 'residue': 2, 'hit': [2, 54], 'gain': 2}, {'prime': 19, 'residue': 6, 'hit': [6, 44], 'gain': 2}]` |
| 120 | 13 | 12 | 0 | 0 | `[{'prime': 13, 'residue': 2, 'hit': [2, 54], 'gain': 2}]` |
| 151 | 14 | 12 | 0 | 0 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 19, 'residue': 11, 'hit': [11, 49], 'gain': 2}]` |
| 169 | 13 | 12 | 0 | 0 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}]` |

### P=67

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 105 | 15 | 13 | 0 | 0 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29], 'gain': 2}, {'prime': 19, 'residue': 2, 'hit': [21, 59], 'gain': 2}]` |
| 172 | 15 | 13 | 0 | 0 | `[{'prime': 13, 'residue': 4, 'hit': [4, 56], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}]` |
| 208 | 16 | 13 | 0 | 0 | `[{'prime': 13, 'residue': 8, 'hit': [8, 34], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}]` |
| 213 | 16 | 13 | 0 | 0 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [5, 39], 'gain': 2}, {'prime': 19, 'residue': 9, 'hit': [9, 47], 'gain': 2}]` |
| 236 | 15 | 13 | 0 | 0 | `[{'prime': 13, 'residue': 6, 'hit': [6, 58], 'gain': 2}, {'prime': 19, 'residue': 9, 'hit': [28, 66], 'gain': 2}]` |
| 241 | 15 | 13 | 0 | 0 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 19, 'residue': 11, 'hit': [11, 49], 'gain': 2}]` |

### P=71

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 195 | 17 | 14 | 0 | 0 | `[{'prime': 13, 'residue': 3, 'hit': [3, 55], 'gain': 2}, {'prime': 17, 'residue': 15, 'hit': [15, 49], 'gain': 2}, {'prime': 19, 'residue': 7, 'hit': [7, 45], 'gain': 2}]` |
| 260 | 16 | 14 | 0 | 0 | `[{'prime': 13, 'residue': 2, 'hit': [2, 54], 'gain': 2}, {'prime': 19, 'residue': 12, 'hit': [12, 50], 'gain': 2}]` |
| 340 | 17 | 14 | 0 | 0 | `[{'prime': 13, 'residue': 2, 'hit': [2, 28], 'gain': 2}, {'prime': 17, 'residue': 0, 'hit': [34, 68], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}]` |
| 748 | 16 | 14 | 0 | 0 | `[{'prime': 13, 'residue': 4, 'hit': [4, 56], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}]` |
| 782 | 17 | 14 | 0 | 0 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32], 'gain': 2}, {'prime': 17, 'residue': 2, 'hit': [2, 36], 'gain': 2}, {'prime': 19, 'residue': 12, 'hit': [12, 50], 'gain': 2}]` |
| 1060 | 17 | 14 | 0 | 0 | `[{'prime': 13, 'residue': 2, 'hit': [2, 28], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}]` |

### P=73

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 50 | 17 | 14 | 1 | 1 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30], 'gain': 2}, {'prime': 17, 'residue': 6, 'hit': [6, 40], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}]` |
| 63 | 16 | 14 | 1 | 1 | `[{'prime': 13, 'residue': 5, 'hit': [5, 57], 'gain': 2}, {'prime': 19, 'residue': 15, 'hit': [15, 53], 'gain': 2}]` |
| 158 | 17 | 14 | 1 | 1 | `[{'prime': 13, 'residue': 6, 'hit': [6, 58], 'gain': 2}, {'prime': 17, 'residue': 1, 'hit': [18, 52], 'gain': 2}, {'prime': 19, 'residue': 10, 'hit': [10, 48], 'gain': 2}]` |
| 191 | 17 | 14 | 1 | 1 | `[{'prime': 13, 'residue': 7, 'hit': [7, 33], 'gain': 2}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}]` |
| 253 | 18 | 14 | 1 | 1 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 13, 'hit': [13, 47], 'gain': 2}, {'prime': 19, 'residue': 5, 'hit': [5, 43], 'gain': 2}, {'prime': 23, 'residue': 2, 'hit': [25, 71], 'gain': 2}]` |
| 338 | 13 | 12 | 1 | 3 | `[{'prime': 13, 'residue': 10, 'hit': [10, 36], 'gain': 2}]` |

### P=79

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 75 | 18 | 15 | 1 | 1 | `[{'prime': 13, 'residue': 5, 'hit': [5, 57], 'gain': 2}, {'prime': 17, 'residue': 3, 'hit': [3, 71], 'gain': 2}, {'prime': 19, 'residue': 15, 'hit': [15, 53], 'gain': 2}]` |
| 134 | 18 | 15 | 1 | 1 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30], 'gain': 2}, {'prime': 17, 'residue': 6, 'hit': [6, 40], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}]` |
| 146 | 18 | 15 | 1 | 1 | `[{'prime': 13, 'residue': 6, 'hit': [6, 58], 'gain': 2}, {'prime': 17, 'residue': 8, 'hit': [42, 76], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}]` |
| 175 | 19 | 15 | 1 | 1 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [5, 73], 'gain': 2}, {'prime': 19, 'residue': 17, 'hit': [17, 55], 'gain': 2}, {'prime': 23, 'residue': 2, 'hit': [25, 71], 'gain': 2}]` |
| 251 | 18 | 15 | 1 | 1 | `[{'prime': 13, 'residue': 1, 'hit': [1, 27], 'gain': 2}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}]` |
| 263 | 18 | 15 | 1 | 1 | `[{'prime': 13, 'residue': 3, 'hit': [3, 55], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [39, 73], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}]` |

### P=83

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 8 | 18 | 15 | 2 | 2 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32], 'gain': 2}, {'prime': 17, 'residue': 12, 'hit': [12, 80], 'gain': 2}, {'prime': 23, 'residue': 20, 'hit': [20, 66], 'gain': 2}]` |
| 54 | 15 | 13 | 2 | 4 | `[{'prime': 13, 'residue': 9, 'hit': [22, 48], 'gain': 2}, {'prime': 17, 'residue': 7, 'hit': [24, 58], 'gain': 2}]` |
| 57 | 20 | 15 | 2 | 2 | `[{'prime': 13, 'residue': 3, 'hit': [3, 55, 81], 'gain': 3}, {'prime': 17, 'residue': 1, 'hit': [1, 69], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}, {'prime': 23, 'residue': 15, 'hit': [15, 61], 'gain': 2}]` |
| 59 | 16 | 14 | 2 | 3 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [5, 39], 'gain': 2}]` |
| 111 | 20 | 15 | 2 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 27, 79], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}, {'prime': 23, 'residue': 21, 'hit': [21, 67], 'gain': 2}]` |
| 139 | 18 | 15 | 2 | 2 | `[{'prime': 13, 'residue': 7, 'hit': [7, 59], 'gain': 2}, {'prime': 17, 'residue': 9, 'hit': [43, 77], 'gain': 2}, {'prime': 19, 'residue': 17, 'hit': [17, 55], 'gain': 2}]` |

### P=89

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 64 | 20 | 16 | 2 | 2 | `[{'prime': 13, 'residue': 4, 'hit': [4, 82], 'gain': 2}, {'prime': 17, 'residue': 10, 'hit': [10, 44], 'gain': 2}, {'prime': 19, 'residue': 2, 'hit': [2, 40], 'gain': 2}, {'prime': 23, 'residue': 16, 'hit': [16, 62], 'gain': 2}]` |
| 171 | 20 | 16 | 2 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 27, 79], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}]` |
| 183 | 21 | 16 | 2 | 2 | `[{'prime': 13, 'residue': 3, 'hit': [3, 55, 81], 'gain': 3}, {'prime': 17, 'residue': 1, 'hit': [1, 69], 'gain': 2}, {'prime': 19, 'residue': 9, 'hit': [9, 85], 'gain': 2}, {'prime': 23, 'residue': 15, 'hit': [15, 61], 'gain': 2}]` |
| 246 | 20 | 16 | 2 | 2 | `[{'prime': 13, 'residue': 4, 'hit': [4, 82], 'gain': 2}, {'prime': 17, 'residue': 12, 'hit': [12, 46], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}, {'prime': 23, 'residue': 18, 'hit': [18, 64], 'gain': 2}]` |
| 267 | 19 | 16 | 2 | 2 | `[{'prime': 13, 'residue': 3, 'hit': [3, 55], 'gain': 2}, {'prime': 17, 'residue': 2, 'hit': [19, 87], 'gain': 2}, {'prime': 23, 'residue': 4, 'hit': [27, 73], 'gain': 2}]` |
| 286 | 20 | 16 | 2 | 2 | `[{'prime': 13, 'residue': 2, 'hit': [2, 28], 'gain': 2}, {'prime': 17, 'residue': 8, 'hit': [8, 76], 'gain': 2}, {'prime': 19, 'residue': 7, 'hit': [26, 64], 'gain': 2}, {'prime': 23, 'residue': 16, 'hit': [16, 62], 'gain': 2}]` |

### P=97

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 25 | 23 | 17 | 2 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 53, 79], 'gain': 3}, {'prime': 17, 'residue': 6, 'hit': [23, 91], 'gain': 2}, {'prime': 19, 'residue': 5, 'hit': [5, 43], 'gain': 2}, {'prime': 23, 'residue': 19, 'hit': [19, 65], 'gain': 2}, {'prime': 29, 'residue': 13, 'hit': [13, 71], 'gain': 2}]` |
| 106 | 22 | 17 | 2 | 2 | `[{'prime': 13, 'residue': 3, 'hit': [16, 68, 94], 'gain': 3}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 8, 'hit': [8, 46], 'gain': 2}, {'prime': 31, 'residue': 26, 'hit': [26, 88], 'gain': 2}]` |
| 206 | 22 | 17 | 2 | 2 | `[{'prime': 13, 'residue': 4, 'hit': [4, 82], 'gain': 2}, {'prime': 17, 'residue': 12, 'hit': [12, 46], 'gain': 2}, {'prime': 19, 'residue': 18, 'hit': [18, 94], 'gain': 2}, {'prime': 23, 'residue': 6, 'hit': [6, 52], 'gain': 2}, {'prime': 31, 'residue': 22, 'hit': [22, 84], 'gain': 2}]` |
| 487 | 22 | 17 | 2 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 79], 'gain': 2}, {'prime': 17, 'residue': 7, 'hit': [7, 41], 'gain': 2}, {'prime': 19, 'residue': 11, 'hit': [11, 49], 'gain': 2}, {'prime': 23, 'residue': 19, 'hit': [19, 65], 'gain': 2}, {'prime': 31, 'residue': 29, 'hit': [29, 91], 'gain': 2}]` |
| 551 | 22 | 17 | 2 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 27, 79], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}, {'prime': 31, 'residue': 7, 'hit': [7, 69], 'gain': 2}]` |
| 749 | 22 | 17 | 2 | 2 | `[{'prime': 13, 'residue': 2, 'hit': [15, 67, 93], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 7, 'hit': [7, 45], 'gain': 2}, {'prime': 31, 'residue': 25, 'hit': [25, 87], 'gain': 2}]` |

### P=101

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 209 | 23 | 18 | 2 | 2 | `[{'prime': 13, 'residue': 3, 'hit': [3, 29, 81], 'gain': 3}, {'prime': 17, 'residue': 5, 'hit': [5, 39], 'gain': 2}, {'prime': 19, 'residue': 15, 'hit': [15, 53], 'gain': 2}, {'prime': 31, 'residue': 9, 'hit': [9, 71], 'gain': 2}]` |
| 918 | 23 | 18 | 2 | 2 | `[{'prime': 13, 'residue': 4, 'hit': [4, 30, 82], 'gain': 3}, {'prime': 17, 'residue': 6, 'hit': [6, 40], 'gain': 2}, {'prime': 19, 'residue': 16, 'hit': [16, 54], 'gain': 2}, {'prime': 31, 'residue': 10, 'hit': [10, 72], 'gain': 2}]` |
| 1101 | 23 | 18 | 2 | 2 | `[{'prime': 13, 'residue': 1, 'hit': [1, 27, 79], 'gain': 3}, {'prime': 17, 'residue': 3, 'hit': [3, 37], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [13, 51], 'gain': 2}, {'prime': 31, 'residue': 7, 'hit': [7, 69], 'gain': 2}]` |
| 1810 | 23 | 18 | 2 | 2 | `[{'prime': 13, 'residue': 2, 'hit': [2, 28, 80], 'gain': 3}, {'prime': 17, 'residue': 4, 'hit': [4, 38], 'gain': 2}, {'prime': 19, 'residue': 14, 'hit': [14, 52], 'gain': 2}, {'prime': 31, 'residue': 8, 'hit': [8, 70], 'gain': 2}]` |

### P=103

| phase | holes | choices | surplus | margin | multi-gain choices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 111 | 18 | 15 | 3 | 6 | `[{'prime': 13, 'residue': 8, 'hit': [21, 47], 'gain': 2}, {'prime': 17, 'residue': 6, 'hit': [23, 57], 'gain': 2}, {'prime': 19, 'residue': 13, 'hit': [51, 89], 'gain': 2}]` |
| 268 | 18 | 15 | 3 | 6 | `[{'prime': 13, 'residue': 7, 'hit': [20, 46], 'gain': 2}, {'prime': 17, 'residue': 5, 'hit': [22, 56], 'gain': 2}, {'prime': 19, 'residue': 12, 'hit': [50, 88], 'gain': 2}]` |
| 425 | 18 | 15 | 3 | 6 | `[{'prime': 13, 'residue': 6, 'hit': [19, 45], 'gain': 2}, {'prime': 17, 'residue': 4, 'hit': [21, 55], 'gain': 2}, {'prime': 19, 'residue': 11, 'hit': [49, 87], 'gain': 2}]` |
| 426 | 25 | 18 | 3 | 3 | `[{'prime': 13, 'residue': 6, 'hit': [6, 32, 84], 'gain': 3}, {'prime': 17, 'residue': 2, 'hit': [2, 36], 'gain': 2}, {'prime': 19, 'residue': 18, 'hit': [18, 56], 'gain': 2}, {'prime': 23, 'residue': 8, 'hit': [8, 54], 'gain': 2}, {'prime': 29, 'residue': 14, 'hit': [14, 72], 'gain': 2}, {'prime': 31, 'residue': 12, 'hit': [12, 74], 'gain': 2}]` |
| 582 | 18 | 15 | 3 | 6 | `[{'prime': 13, 'residue': 5, 'hit': [18, 44], 'gain': 2}, {'prime': 17, 'residue': 3, 'hit': [20, 54], 'gain': 2}, {'prime': 19, 'residue': 10, 'hit': [48, 86], 'gain': 2}]` |
| 583 | 25 | 18 | 3 | 3 | `[{'prime': 13, 'residue': 5, 'hit': [5, 31, 83], 'gain': 3}, {'prime': 17, 'residue': 1, 'hit': [1, 35], 'gain': 2}, {'prime': 19, 'residue': 17, 'hit': [17, 55], 'gain': 2}, {'prime': 23, 'residue': 7, 'hit': [7, 53], 'gain': 2}, {'prime': 29, 'residue': 13, 'hit': [13, 71], 'gain': 2}, {'prime': 31, 'residue': 11, 'hit': [11, 73], 'gain': 2}]` |

## 3. 审稿结论

该证书闭合 `61<=P<=103` 的窄带碰撞能量义务。
结合低范围最终证书后，low-hole 主线只剩 `P>=13208` 的显式常数引用核验。
