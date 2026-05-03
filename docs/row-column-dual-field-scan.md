# 行列双缺陷场扫描

**状态：** `row_and_column_defects_are_dual_marginals_of_the_same_prime_position_field`

行命题与列命题可视为同一个 P×P 素数位置场的两个边际缺陷。行残洞场 H_P(x) 给出类素数候选；列计数是这些候选在列方向的投影。统一证明应控制二维缺陷流，而不只是一维行转移。

## 摘要
- P=5 min_row_prime=1 min_col_prime_exclP=1 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=1 sample={1: [1], 2: [2], 5: [3]}
- P=7 min_row_prime=1 min_col_prime_exclP=1 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=1 sample={1: [1], 4: [2]}
- P=11 min_row_prime=1 min_col_prime_exclP=2 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=1 sample={1: [1], 11: [3]}
- P=13 min_row_prime=1 min_col_prime_exclP=1 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=1 sample={1: [1], 10: [10]}
- P=17 min_row_prime=1 min_col_prime_exclP=2 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=2 sample={1: [1], 13: [7]}
- P=19 min_row_prime=1 min_col_prime_exclP=2 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=2 sample={1: [1], 16: [8]}
- P=23 min_row_prime=2 min_col_prime_exclP=3 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=3 sample={1: [1]}
- P=29 min_row_prime=3 min_col_prime_exclP=4 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=3 sample={1: [1]}
- P=31 min_row_prime=2 min_col_prime_exclP=3 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=3 sample={1: [1]}
- P=37 min_row_prime=2 min_col_prime_exclP=4 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=4 sample={1: [1]}
- P=41 min_row_prime=3 min_col_prime_exclP=4 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=4 sample={1: [1]}
- P=43 min_row_prime=3 min_col_prime_exclP=3 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=3 sample={1: [1]}
- P=47 min_row_prime=3 min_col_prime_exclP=4 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=4 sample={1: [1]}
- P=53 min_row_prime=4 min_col_prime_exclP=5 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=5 sample={1: [1]}
- P=59 min_row_prime=3 min_col_prime_exclP=6 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=6 sample={1: [1]}
- P=61 min_row_prime=5 min_col_prime_exclP=6 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=5 sample={1: [1]}
- P=67 min_row_prime=5 min_col_prime_exclP=6 zero_rows=[] zero_cols=[] min_row_hole=1 min_col_hole=6 sample={1: [1]}

## 下一证明义务
- 定义二维缺陷矩阵 Z_{r,c}=1_{(r,c) 为类素数/素数候选}。
- 把行反例和列反例写成 Z 的零边际。
- 将 Barrier 的列支撑接入二维边际守恒。
