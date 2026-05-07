# 平方后端点倒数地板素对覆盖缺口审计

**状态：** `experimental_reciprocal_floor_prime_pair_excess_support_not_a_proof`

## 参数

- `max_p`: `10000`
- `y_ratio`: `0.36787944117144233`

## 总结

- 检查 `p>=23` 奇素数个数：`1221`。
- 非低骨架候选记录数：`0`。
- 重复覆盖记录数：`0`。
- 最小余量：`2`。
- 最大覆盖比例：`0.5`。
- 最小余量比例：`0.5`。
- 三曲线覆盖 offset 分布：`{'1': 47542, '2': 24208, '3': 3271}`。

## 阈值账本

| threshold | max cover record | min margin ratio record | min margin record |
|---:|---|---|---|
| 23 | {'p': 23, 'cover_ratio': 0.5, 'low_skeleton': 4, 'covered_columns': 2} | {'p': 23, 'margin_ratio': 0.5, 'margin': 2, 'low_skeleton': 4} | {'p': 23, 'margin': 2, 'low_skeleton': 4, 'covered_columns': 2} |
| 101 | {'p': 113, 'cover_ratio': 0.4, 'low_skeleton': 15, 'covered_columns': 6} | {'p': 113, 'margin_ratio': 0.6, 'margin': 9, 'low_skeleton': 15} | {'p': 113, 'margin': 9, 'low_skeleton': 15, 'covered_columns': 6} |
| 251 | {'p': 257, 'cover_ratio': 0.3793103448275862, 'low_skeleton': 29, 'covered_columns': 11} | {'p': 257, 'margin_ratio': 0.6206896551724138, 'margin': 18, 'low_skeleton': 29} | {'p': 251, 'margin': 18, 'low_skeleton': 26, 'covered_columns': 8} |
| 501 | {'p': 613, 'cover_ratio': 0.3114754098360656, 'low_skeleton': 61, 'covered_columns': 19} | {'p': 613, 'margin_ratio': 0.6885245901639344, 'margin': 42, 'low_skeleton': 61} | {'p': 503, 'margin': 34, 'low_skeleton': 48, 'covered_columns': 14} |
| 1009 | {'p': 2029, 'cover_ratio': 0.2909090909090909, 'low_skeleton': 165, 'covered_columns': 48} | {'p': 2029, 'margin_ratio': 0.7090909090909091, 'margin': 117, 'low_skeleton': 165} | {'p': 1021, 'margin': 65, 'low_skeleton': 88, 'covered_columns': 23} |
| 2003 | {'p': 2029, 'cover_ratio': 0.2909090909090909, 'low_skeleton': 165, 'covered_columns': 48} | {'p': 2029, 'margin_ratio': 0.7090909090909091, 'margin': 117, 'low_skeleton': 165} | {'p': 2029, 'margin': 117, 'low_skeleton': 165, 'covered_columns': 48} |
| 5003 | {'p': 5647, 'cover_ratio': 0.23940149625935161, 'low_skeleton': 401, 'covered_columns': 96} | {'p': 5647, 'margin_ratio': 0.7605985037406484, 'margin': 305, 'low_skeleton': 401} | {'p': 5023, 'margin': 276, 'low_skeleton': 336, 'covered_columns': 60} |

## 最大覆盖比例样本

| p | y | low | covered | ratio | margin | offsets | samples |
|---:|---:|---:|---:|---:|---:|---|---|
| 23 | 8 | 4 | 2 | 0.500000 | 2 | {'1': 1, '2': 1} | [{'ell': 13, 'm': 41, 'offset': 1, 'column': 4, 'value': 533, 'low_rough_column': True}, {'ell': 19, 'm': 29, 'offset': 2, 'column': 22, 'value': 551, 'low_rough_column': True}] |
| 37 | 13 | 5 | 2 | 0.400000 | 3 | {'1': 1, '2': 1} | [{'ell': 19, 'm': 73, 'offset': 1, 'column': 18, 'value': 1387, 'low_rough_column': True}, {'ell': 23, 'm': 61, 'offset': 2, 'column': 34, 'value': 1403, 'low_rough_column': True}] |
| 113 | 41 | 15 | 6 | 0.400000 | 9 | {'1': 3, '2': 3} | [{'ell': 53, 'm': 241, 'offset': 1, 'column': 4, 'value': 12773, 'low_rough_column': True}, {'ell': 61, 'm': 211, 'offset': 2, 'column': 102, 'value': 12871, 'low_rough_column': True}, {'ell': 67, 'm': 191, 'offset': 1, 'column': 28, 'value': 12797, 'low_rough_column': True}, {'ell': 71, 'm': 181, 'offset': 2, 'column': 82, 'value': 12851, 'low_rough_column': True}, {'ell': 79, 'm': 163, 'offset': 2, 'column': 108, 'value': 12877, 'low_rough_column': True}] |
| 137 | 50 | 15 | 6 | 0.400000 | 9 | {'1': 5, '2': 1} | [{'ell': 67, 'm': 281, 'offset': 1, 'column': 58, 'value': 18827, 'low_rough_column': True}, {'ell': 79, 'm': 239, 'offset': 2, 'column': 112, 'value': 18881, 'low_rough_column': True}, {'ell': 83, 'm': 227, 'offset': 1, 'column': 72, 'value': 18841, 'low_rough_column': True}, {'ell': 89, 'm': 211, 'offset': 1, 'column': 10, 'value': 18779, 'low_rough_column': True}, {'ell': 109, 'm': 173, 'offset': 1, 'column': 88, 'value': 18857, 'low_rough_column': True}] |
| 257 | 94 | 29 | 11 | 0.379310 | 18 | {'1': 3, '2': 7, '3': 1} | [{'ell': 97, 'm': 683, 'offset': 3, 'column': 202, 'value': 66251, 'low_rough_column': True}, {'ell': 103, 'm': 643, 'offset': 2, 'column': 180, 'value': 66229, 'low_rough_column': True}, {'ell': 107, 'm': 619, 'offset': 2, 'column': 184, 'value': 66233, 'low_rough_column': True}, {'ell': 109, 'm': 607, 'offset': 2, 'column': 114, 'value': 66163, 'low_rough_column': True}, {'ell': 127, 'm': 521, 'offset': 1, 'column': 118, 'value': 66167, 'low_rough_column': True}] |
| 41 | 15 | 8 | 3 | 0.375000 | 5 | {'1': 1, '2': 1, '3': 1} | [{'ell': 17, 'm': 101, 'offset': 3, 'column': 36, 'value': 1717, 'low_rough_column': True}, {'ell': 19, 'm': 89, 'offset': 1, 'column': 10, 'value': 1691, 'low_rough_column': True}, {'ell': 29, 'm': 59, 'offset': 2, 'column': 30, 'value': 1711, 'low_rough_column': True}] |
| 269 | 98 | 32 | 12 | 0.375000 | 20 | {'1': 7, '2': 4, '3': 1} | [{'ell': 101, 'm': 719, 'offset': 3, 'column': 258, 'value': 72619, 'low_rough_column': True}, {'ell': 107, 'm': 677, 'offset': 1, 'column': 78, 'value': 72439, 'low_rough_column': True}, {'ell': 113, 'm': 641, 'offset': 1, 'column': 72, 'value': 72433, 'low_rough_column': True}, {'ell': 127, 'm': 571, 'offset': 2, 'column': 156, 'value': 72517, 'low_rough_column': True}, {'ell': 139, 'm': 521, 'offset': 1, 'column': 58, 'value': 72419, 'low_rough_column': True}] |
| 421 | 154 | 44 | 16 | 0.363636 | 28 | {'1': 8, '2': 8} | [{'ell': 157, 'm': 1129, 'offset': 1, 'column': 12, 'value': 177253, 'low_rough_column': True}, {'ell': 167, 'm': 1063, 'offset': 2, 'column': 280, 'value': 177521, 'low_rough_column': True}, {'ell': 179, 'm': 991, 'offset': 1, 'column': 148, 'value': 177389, 'low_rough_column': True}, {'ell': 191, 'm': 929, 'offset': 2, 'column': 198, 'value': 177439, 'low_rough_column': True}, {'ell': 193, 'm': 919, 'offset': 1, 'column': 126, 'value': 177367, 'low_rough_column': True}] |
| 461 | 169 | 50 | 18 | 0.360000 | 32 | {'1': 12, '2': 5, '3': 1} | [{'ell': 173, 'm': 1229, 'offset': 1, 'column': 96, 'value': 212617, 'low_rough_column': True}, {'ell': 173, 'm': 1231, 'offset': 3, 'column': 442, 'value': 212963, 'low_rough_column': True}, {'ell': 193, 'm': 1103, 'offset': 2, 'column': 358, 'value': 212879, 'low_rough_column': True}, {'ell': 199, 'm': 1069, 'offset': 2, 'column': 210, 'value': 212731, 'low_rough_column': True}, {'ell': 211, 'm': 1009, 'offset': 2, 'column': 378, 'value': 212899, 'low_rough_column': True}] |
| 173 | 63 | 20 | 7 | 0.350000 | 13 | {'1': 5, '2': 1, '3': 1} | [{'ell': 67, 'm': 449, 'offset': 3, 'column': 154, 'value': 30083, 'low_rough_column': True}, {'ell': 79, 'm': 379, 'offset': 1, 'column': 12, 'value': 29941, 'low_rough_column': True}, {'ell': 89, 'm': 337, 'offset': 1, 'column': 64, 'value': 29993, 'low_rough_column': True}, {'ell': 107, 'm': 281, 'offset': 2, 'column': 138, 'value': 30067, 'low_rough_column': True}, {'ell': 131, 'm': 229, 'offset': 1, 'column': 70, 'value': 29999, 'low_rough_column': True}] |
| 383 | 140 | 44 | 15 | 0.340909 | 29 | {'1': 10, '2': 5} | [{'ell': 179, 'm': 821, 'offset': 2, 'column': 270, 'value': 146959, 'low_rough_column': True}, {'ell': 181, 'm': 811, 'offset': 1, 'column': 102, 'value': 146791, 'low_rough_column': True}, {'ell': 191, 'm': 769, 'offset': 1, 'column': 190, 'value': 146879, 'low_rough_column': True}, {'ell': 193, 'm': 761, 'offset': 1, 'column': 184, 'value': 146873, 'low_rough_column': True}, {'ell': 199, 'm': 739, 'offset': 2, 'column': 372, 'value': 147061, 'low_rough_column': True}] |
| 29 | 10 | 6 | 2 | 0.333333 | 4 | {'1': 1, '3': 1} | [{'ell': 11, 'm': 79, 'offset': 3, 'column': 28, 'value': 869, 'low_rough_column': True}, {'ell': 23, 'm': 37, 'offset': 1, 'column': 10, 'value': 851, 'low_rough_column': True}] |
| 89 | 32 | 12 | 4 | 0.333333 | 8 | {'1': 2, '2': 2} | [{'ell': 53, 'm': 151, 'offset': 2, 'column': 82, 'value': 8003, 'low_rough_column': True}, {'ell': 61, 'm': 131, 'offset': 2, 'column': 70, 'value': 7991, 'low_rough_column': True}, {'ell': 73, 'm': 109, 'offset': 1, 'column': 36, 'value': 7957, 'low_rough_column': True}, {'ell': 79, 'm': 101, 'offset': 1, 'column': 58, 'value': 7979, 'low_rough_column': True}] |
| 281 | 103 | 34 | 11 | 0.323529 | 23 | {'1': 8, '2': 2, '3': 1} | [{'ell': 107, 'm': 739, 'offset': 2, 'column': 112, 'value': 79073, 'low_rough_column': True}, {'ell': 113, 'm': 701, 'offset': 3, 'column': 252, 'value': 79213, 'low_rough_column': True}, {'ell': 137, 'm': 577, 'offset': 1, 'column': 88, 'value': 79049, 'low_rough_column': True}, {'ell': 139, 'm': 569, 'offset': 1, 'column': 130, 'value': 79091, 'low_rough_column': True}, {'ell': 151, 'm': 523, 'offset': 1, 'column': 12, 'value': 78973, 'low_rough_column': True}] |
| 149 | 54 | 19 | 6 | 0.315789 | 13 | {'1': 4, '2': 2} | [{'ell': 71, 'm': 313, 'offset': 1, 'column': 22, 'value': 22223, 'low_rough_column': True}, {'ell': 83, 'm': 269, 'offset': 2, 'column': 126, 'value': 22327, 'low_rough_column': True}, {'ell': 89, 'm': 251, 'offset': 2, 'column': 138, 'value': 22339, 'low_rough_column': True}, {'ell': 97, 'm': 229, 'offset': 1, 'column': 12, 'value': 22213, 'low_rough_column': True}, {'ell': 113, 'm': 197, 'offset': 1, 'column': 60, 'value': 22261, 'low_rough_column': True}] |
| 131 | 48 | 16 | 5 | 0.312500 | 11 | {'1': 3, '2': 1, '3': 1} | [{'ell': 59, 'm': 293, 'offset': 3, 'column': 126, 'value': 17287, 'low_rough_column': True}, {'ell': 61, 'm': 283, 'offset': 2, 'column': 102, 'value': 17263, 'low_rough_column': True}, {'ell': 67, 'm': 257, 'offset': 1, 'column': 58, 'value': 17219, 'low_rough_column': True}, {'ell': 89, 'm': 193, 'offset': 1, 'column': 16, 'value': 17177, 'low_rough_column': True}, {'ell': 103, 'm': 167, 'offset': 1, 'column': 40, 'value': 17201, 'low_rough_column': True}] |
| 613 | 225 | 61 | 19 | 0.311475 | 42 | {'1': 12, '2': 6, '3': 1} | [{'ell': 227, 'm': 1657, 'offset': 2, 'column': 370, 'value': 376139, 'low_rough_column': True}, {'ell': 233, 'm': 1613, 'offset': 1, 'column': 60, 'value': 375829, 'low_rough_column': True}, {'ell': 251, 'm': 1499, 'offset': 2, 'column': 480, 'value': 376249, 'low_rough_column': True}, {'ell': 263, 'm': 1429, 'offset': 1, 'column': 58, 'value': 375827, 'low_rough_column': True}, {'ell': 269, 'm': 1399, 'offset': 3, 'column': 562, 'value': 376331, 'low_rough_column': True}] |
| 251 | 92 | 26 | 8 | 0.307692 | 18 | {'1': 4, '2': 4} | [{'ell': 103, 'm': 613, 'offset': 2, 'column': 138, 'value': 63139, 'low_rough_column': True}, {'ell': 137, 'm': 461, 'offset': 2, 'column': 156, 'value': 63157, 'low_rough_column': True}, {'ell': 179, 'm': 353, 'offset': 2, 'column': 186, 'value': 63187, 'low_rough_column': True}, {'ell': 181, 'm': 349, 'offset': 1, 'column': 168, 'value': 63169, 'low_rough_column': True}, {'ell': 191, 'm': 331, 'offset': 2, 'column': 220, 'value': 63221, 'low_rough_column': True}] |
| 607 | 223 | 59 | 18 | 0.305085 | 41 | {'1': 10, '2': 7, '3': 1} | [{'ell': 229, 'm': 1609, 'offset': 1, 'column': 12, 'value': 368461, 'low_rough_column': True}, {'ell': 233, 'm': 1583, 'offset': 2, 'column': 390, 'value': 368839, 'low_rough_column': True}, {'ell': 239, 'm': 1543, 'offset': 2, 'column': 328, 'value': 368777, 'low_rough_column': True}, {'ell': 241, 'm': 1531, 'offset': 3, 'column': 522, 'value': 368971, 'low_rough_column': True}, {'ell': 271, 'm': 1361, 'offset': 2, 'column': 382, 'value': 368831, 'low_rough_column': True}] |
| 929 | 341 | 82 | 25 | 0.304878 | 57 | {'1': 17, '2': 6, '3': 2} | [{'ell': 349, 'm': 2473, 'offset': 1, 'column': 36, 'value': 863077, 'low_rough_column': True}, {'ell': 353, 'm': 2447, 'offset': 3, 'column': 750, 'value': 863791, 'low_rough_column': True}, {'ell': 389, 'm': 2221, 'offset': 3, 'column': 928, 'value': 863969, 'low_rough_column': True}, {'ell': 401, 'm': 2153, 'offset': 1, 'column': 312, 'value': 863353, 'low_rough_column': True}, {'ell': 409, 'm': 2111, 'offset': 1, 'column': 358, 'value': 863399, 'low_rough_column': True}] |

## 审稿解释

对 `p>=23`，尾碰撞已消失，且一尾互补因子必为素数。因此 `margin=low_skeleton-covered_columns` 正是平方后窗口中的无尾储备数；正余量直接给出素数。

该审计把剩余证明目标压成：三条倒数地板素对曲线的覆盖数必须始终小于低筛骨架数。若某族反例让覆盖比例逼近 `1`，则它必须表现为短窗素数异常集中或固定端点相位的 `PDEC/Tail-anchor` 缺陷。
