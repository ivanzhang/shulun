# 完整覆盖方案必要素数分析

**状态：** `first_full_schemes_need_essential_medium_large_primes`

首个完整覆盖方案中，除小素数骨架外，总有若干必要中大素数负责唯一列。其乘积远超 P，这解释了完整方案 CRT 解被推出前窗口。

## 摘要
- P=13 x=168 essential_product/P=177.69 essential=[{'q': 2, 'unique_columns': [2, 4, 8, 10], 'unique_count': 4}, {'q': 3, 'unique_columns': [3, 9], 'unique_count': 2}, {'q': 5, 'unique_columns': [1, 11], 'unique_count': 2}, {'q': 7, 'unique_columns': [7], 'unique_count': 1}, {'q': 11, 'unique_columns': [5], 'unique_count': 1}]
- P=17 x=1210 essential_product/P=1766.47 essential=[{'q': 2, 'unique_columns': [2, 6, 8, 12, 14], 'unique_count': 5}, {'q': 3, 'unique_columns': [1, 7, 13], 'unique_count': 3}, {'q': 5, 'unique_columns': [5, 15], 'unique_count': 2}, {'q': 7, 'unique_columns': [3], 'unique_count': 1}, {'q': 11, 'unique_columns': [11], 'unique_count': 1}, {'q': 13, 'unique_columns': [9], 'unique_count': 1}]
- P=19 x=3658 essential_product/P=1580.53 essential=[{'q': 2, 'unique_columns': [4, 6, 10, 12, 16], 'unique_count': 5}, {'q': 3, 'unique_columns': [5, 17], 'unique_count': 2}, {'q': 5, 'unique_columns': [3, 13], 'unique_count': 2}, {'q': 7, 'unique_columns': [1, 15], 'unique_count': 2}, {'q': 11, 'unique_columns': [7], 'unique_count': 1}, {'q': 13, 'unique_columns': [9], 'unique_count': 1}]
- P=23 x=58 essential_product/P=38338.70 essential=[{'q': 2, 'unique_columns': [2, 12, 14, 20], 'unique_count': 4}, {'q': 3, 'unique_columns': [7, 13], 'unique_count': 2}, {'q': 5, 'unique_columns': [11, 21], 'unique_count': 2}, {'q': 7, 'unique_columns': [3, 17], 'unique_count': 2}, {'q': 13, 'unique_columns': [5], 'unique_count': 1}, {'q': 17, 'unique_columns': [9], 'unique_count': 1}, {'q': 19, 'unique_columns': [15], 'unique_count': 1}]
- P=29 x=5209 essential_product/P=7692857.59 essential=[{'q': 2, 'unique_columns': [5, 11, 15, 17, 21, 23], 'unique_count': 6}, {'q': 3, 'unique_columns': [10, 16, 22, 28], 'unique_count': 4}, {'q': 5, 'unique_columns': [14], 'unique_count': 1}, {'q': 7, 'unique_columns': [6, 20], 'unique_count': 2}, {'q': 11, 'unique_columns': [2], 'unique_count': 1}, {'q': 13, 'unique_columns': [12], 'unique_count': 1}, {'q': 17, 'unique_columns': [18], 'unique_count': 1}, {'q': 19, 'unique_columns': [8], 'unique_count': 1}, {'q': 23, 'unique_columns': [26], 'unique_count': 1}]
- P=31 x=60794 essential_product/P=553580.32 essential=[{'q': 2, 'unique_columns': [2, 8, 12, 14, 18, 20, 30], 'unique_count': 7}, {'q': 3, 'unique_columns': [7, 13, 19, 25], 'unique_count': 4}, {'q': 5, 'unique_columns': [11, 21], 'unique_count': 2}, {'q': 7, 'unique_columns': [3, 17], 'unique_count': 2}, {'q': 11, 'unique_columns': [5, 27], 'unique_count': 2}, {'q': 17, 'unique_columns': [23], 'unique_count': 1}, {'q': 19, 'unique_columns': [15], 'unique_count': 1}, {'q': 23, 'unique_columns': [29], 'unique_count': 1}]

## 下一证明义务
- 证明任意完整覆盖方案都含有必要素数集合 E，且 prod(E)>P。
- 证明这些必要素数的同余条件不能在 x<P 同时满足。
- 把必要列与相邻互斥/gap复杂度结合，给出 E 的下界。
