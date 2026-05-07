# 平方后端点一尾互补因子审计

**状态：** `experimental_postsquare_tail_cofactor_identity_support_not_a_proof`

## 参数

- `max_p`: `10000`
- `y_ratio`: `0.36787944117144233`

## 总结

- 检查奇素数个数：`1228`。
- y-rough 互补因子总数：`75031`。
- 复合 y-rough 互补因子数：`4`。
- 最后出现复合互补因子的 p：`13`。
- 最大互补因子区间长度：`3`。
- 最大区间样本：`{'p': 13, 'y': 4, 'ell': 5, 'cofactor_interval': [34, 36], 'interval_length': 3}`。
- 互补因子素性阈值失败次数：`5`。
- 最后一个阈值失败 p：`19`。
- floor offset 分布：`{'1': 47547, '2': 24213, '3': 3271}`。
- 单行最多互补因子记录：`{'p': 9887, 'y': 3637, 'tail_prime_count': 710, 'yrough_cofactors': 140, 'offset_counts': {2: 39, 3: 9, 1: 92}}`。

## 最大区间样本

| p | y | tail primes | yrough cofactors | composite | max interval | sample |
|---:|---:|---:|---:|---:|---:|---|
| 13 | 4 | 3 | 2 | 2 | 3 | [{'ell': 5, 'cofactor': 35, 'offset': 2, 'value': 175, 'column': 6, 'cofactor_is_prime': False}, {'ell': 7, 'cofactor': 25, 'offset': 1, 'value': 175, 'column': 6, 'cofactor_is_prime': False}] |
| 19 | 6 | 4 | 2 | 0 | 3 | [{'ell': 7, 'cofactor': 53, 'offset': 2, 'value': 371, 'column': 10, 'cofactor_is_prime': True}, {'ell': 13, 'cofactor': 29, 'offset': 2, 'value': 377, 'column': 16, 'cofactor_is_prime': True}] |
| 29 | 10 | 5 | 2 | 0 | 3 | [{'ell': 11, 'cofactor': 79, 'offset': 3, 'value': 869, 'column': 28, 'cofactor_is_prime': True}, {'ell': 23, 'cofactor': 37, 'offset': 1, 'value': 851, 'column': 10, 'cofactor_is_prime': True}] |
| 31 | 11 | 5 | 1 | 0 | 3 | [{'ell': 23, 'cofactor': 43, 'offset': 2, 'value': 989, 'column': 28, 'cofactor_is_prime': True}] |
| 41 | 15 | 6 | 3 | 0 | 3 | [{'ell': 17, 'cofactor': 101, 'offset': 3, 'value': 1717, 'column': 36, 'cofactor_is_prime': True}, {'ell': 19, 'cofactor': 89, 'offset': 1, 'value': 1691, 'column': 10, 'cofactor_is_prime': True}, {'ell': 29, 'cofactor': 59, 'offset': 2, 'value': 1711, 'column': 30, 'cofactor_is_prime': True}] |
| 43 | 15 | 7 | 2 | 0 | 3 | [{'ell': 17, 'cofactor': 109, 'offset': 1, 'value': 1853, 'column': 4, 'cofactor_is_prime': True}, {'ell': 31, 'cofactor': 61, 'offset': 2, 'value': 1891, 'column': 42, 'cofactor_is_prime': True}] |
| 61 | 22 | 9 | 3 | 0 | 3 | [{'ell': 23, 'cofactor': 163, 'offset': 2, 'value': 3749, 'column': 28, 'cofactor_is_prime': True}, {'ell': 37, 'cofactor': 101, 'offset': 1, 'value': 3737, 'column': 16, 'cofactor_is_prime': True}, {'ell': 53, 'cofactor': 71, 'offset': 1, 'value': 3763, 'column': 42, 'cofactor_is_prime': True}] |
| 67 | 24 | 9 | 1 | 0 | 3 | [{'ell': 29, 'cofactor': 157, 'offset': 3, 'value': 4553, 'column': 64, 'cofactor_is_prime': True}] |
| 71 | 26 | 10 | 3 | 0 | 3 | [{'ell': 31, 'cofactor': 163, 'offset': 1, 'value': 5053, 'column': 12, 'cofactor_is_prime': True}, {'ell': 37, 'cofactor': 137, 'offset': 1, 'value': 5069, 'column': 28, 'cofactor_is_prime': True}, {'ell': 61, 'cofactor': 83, 'offset': 1, 'value': 5063, 'column': 22, 'cofactor_is_prime': True}] |
| 73 | 26 | 11 | 3 | 0 | 3 | [{'ell': 31, 'cofactor': 173, 'offset': 2, 'value': 5363, 'column': 34, 'cofactor_is_prime': True}, {'ell': 41, 'cofactor': 131, 'offset': 2, 'value': 5371, 'column': 42, 'cofactor_is_prime': True}, {'ell': 53, 'cofactor': 101, 'offset': 1, 'value': 5353, 'column': 24, 'cofactor_is_prime': True}] |
| 97 | 35 | 13 | 1 | 0 | 3 | [{'ell': 53, 'cofactor': 179, 'offset': 2, 'value': 9487, 'column': 78, 'cofactor_is_prime': True}] |
| 101 | 37 | 13 | 4 | 0 | 3 | [{'ell': 41, 'cofactor': 251, 'offset': 3, 'value': 10291, 'column': 90, 'cofactor_is_prime': True}, {'ell': 43, 'cofactor': 239, 'offset': 2, 'value': 10277, 'column': 76, 'cofactor_is_prime': True}, {'ell': 53, 'cofactor': 193, 'offset': 1, 'value': 10229, 'column': 28, 'cofactor_is_prime': True}, {'ell': 59, 'cofactor': 173, 'offset': 1, 'value': 10207, 'column': 6, 'cofactor_is_prime': True}] |
| 103 | 37 | 14 | 2 | 0 | 3 | [{'ell': 47, 'cofactor': 227, 'offset': 2, 'value': 10669, 'column': 60, 'cofactor_is_prime': True}, {'ell': 59, 'cofactor': 181, 'offset': 2, 'value': 10679, 'column': 70, 'cofactor_is_prime': True}] |
| 109 | 40 | 16 | 3 | 0 | 3 | [{'ell': 43, 'cofactor': 277, 'offset': 1, 'value': 11911, 'column': 30, 'cofactor_is_prime': True}, {'ell': 73, 'cofactor': 163, 'offset': 1, 'value': 11899, 'column': 18, 'cofactor_is_prime': True}, {'ell': 79, 'cofactor': 151, 'offset': 1, 'value': 11929, 'column': 48, 'cofactor_is_prime': True}] |
| 113 | 41 | 16 | 6 | 0 | 3 | [{'ell': 53, 'cofactor': 241, 'offset': 1, 'value': 12773, 'column': 4, 'cofactor_is_prime': True}, {'ell': 61, 'cofactor': 211, 'offset': 2, 'value': 12871, 'column': 102, 'cofactor_is_prime': True}, {'ell': 67, 'cofactor': 191, 'offset': 1, 'value': 12797, 'column': 28, 'cofactor_is_prime': True}, {'ell': 71, 'cofactor': 181, 'offset': 2, 'value': 12851, 'column': 82, 'cofactor_is_prime': True}, {'ell': 79, 'cofactor': 163, 'offset': 2, 'value': 12877, 'column': 108, 'cofactor_is_prime': True}] |
| 131 | 48 | 16 | 5 | 0 | 3 | [{'ell': 59, 'cofactor': 293, 'offset': 3, 'value': 17287, 'column': 126, 'cofactor_is_prime': True}, {'ell': 61, 'cofactor': 283, 'offset': 2, 'value': 17263, 'column': 102, 'cofactor_is_prime': True}, {'ell': 67, 'cofactor': 257, 'offset': 1, 'value': 17219, 'column': 58, 'cofactor_is_prime': True}, {'ell': 89, 'cofactor': 193, 'offset': 1, 'value': 17177, 'column': 16, 'cofactor_is_prime': True}, {'ell': 103, 'cofactor': 167, 'offset': 1, 'value': 17201, 'column': 40, 'cofactor_is_prime': True}] |
| 139 | 51 | 18 | 4 | 0 | 3 | [{'ell': 53, 'cofactor': 367, 'offset': 3, 'value': 19451, 'column': 130, 'cofactor_is_prime': True}, {'ell': 61, 'cofactor': 317, 'offset': 1, 'value': 19337, 'column': 16, 'cofactor_is_prime': True}, {'ell': 83, 'cofactor': 233, 'offset': 1, 'value': 19339, 'column': 18, 'cofactor_is_prime': True}, {'ell': 107, 'cofactor': 181, 'offset': 1, 'value': 19367, 'column': 46, 'cofactor_is_prime': True}] |
| 149 | 54 | 18 | 6 | 0 | 3 | [{'ell': 71, 'cofactor': 313, 'offset': 1, 'value': 22223, 'column': 22, 'cofactor_is_prime': True}, {'ell': 83, 'cofactor': 269, 'offset': 2, 'value': 22327, 'column': 126, 'cofactor_is_prime': True}, {'ell': 89, 'cofactor': 251, 'offset': 2, 'value': 22339, 'column': 138, 'cofactor_is_prime': True}, {'ell': 97, 'cofactor': 229, 'offset': 1, 'value': 22213, 'column': 12, 'cofactor_is_prime': True}, {'ell': 113, 'cofactor': 197, 'offset': 1, 'value': 22261, 'column': 60, 'cofactor_is_prime': True}] |
| 151 | 55 | 19 | 5 | 0 | 3 | [{'ell': 59, 'cofactor': 389, 'offset': 3, 'value': 22951, 'column': 150, 'cofactor_is_prime': True}, {'ell': 73, 'cofactor': 313, 'offset': 1, 'value': 22849, 'column': 48, 'cofactor_is_prime': True}, {'ell': 89, 'cofactor': 257, 'offset': 1, 'value': 22873, 'column': 72, 'cofactor_is_prime': True}, {'ell': 101, 'cofactor': 227, 'offset': 2, 'value': 22927, 'column': 126, 'cofactor_is_prime': True}, {'ell': 137, 'cofactor': 167, 'offset': 1, 'value': 22879, 'column': 78, 'cofactor_is_prime': True}] |
| 157 | 57 | 20 | 6 | 0 | 3 | [{'ell': 59, 'cofactor': 419, 'offset': 2, 'value': 24721, 'column': 72, 'cofactor_is_prime': True}, {'ell': 71, 'cofactor': 349, 'offset': 2, 'value': 24779, 'column': 130, 'cofactor_is_prime': True}, {'ell': 79, 'cofactor': 313, 'offset': 1, 'value': 24727, 'column': 78, 'cofactor_is_prime': True}, {'ell': 89, 'cofactor': 277, 'offset': 1, 'value': 24653, 'column': 4, 'cofactor_is_prime': True}, {'ell': 109, 'cofactor': 227, 'offset': 1, 'value': 24743, 'column': 94, 'cofactor_is_prime': True}] |

## 审稿解释

一尾项精确等价于 `p^2+k=ell*m`，其中 `y<ell<p`，且 `m` 仍为 `y`-rough。互补因子区间长度至多 `1+p/ell<1+e`，本次样本实际最大为 `3`。若 `p^2+p-1<(y+1)^3`，则任何 `y`-rough 互补因子 `m` 必为素数；样本显示复合 `y`-rough 互补因子只出现在极小 `p`。
