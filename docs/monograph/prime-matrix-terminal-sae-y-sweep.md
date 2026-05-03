# Terminal-SAE 分层参数 y 扫描

**状态：** `experimental_y_parameter_stability_scan_not_a_proof`

## 参数

- `max_p`: `1000`
- `ratios`: `[0.2, 0.25, 0.3, 0.3333333333333333, 0.36787944117144233, 0.4, 0.45, 0.5, 0.6, 0.7]`

## 汇总

- 安全 ratio 个数：`8`。
- 首个安全 ratio：`0.3`。
- 末个安全 ratio：`0.7`。

## 扫描表

| y_ratio | certified | min margin p>=7 | unresolved p>=7 | worst record |
| ---: | --- | ---: | ---: | --- |
| 0.200000000000 | False | -1 | 6 | {'p': 13, 'q_next': 17, 'y': 2, 'min_margin': -1, 'min_data': {'h': 1, 'skeleton': 8, 'tail_incidence': 9, 'margin': -1}, 'bad_margin_row_count': 2} |
| 0.250000000000 | False | 0 | 2 | {'p': 17, 'q_next': 19, 'y': 4, 'min_margin': 0, 'min_data': {'h': 15, 'skeleton': 7, 'tail_incidence': 7, 'margin': 0}, 'bad_margin_row_count': 1} |
| 0.300000000000 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |
| 0.333333333333 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |
| 0.367879441171 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |
| 0.400000000000 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |
| 0.450000000000 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |
| 0.500000000000 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |
| 0.600000000000 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |
| 0.700000000000 | True | 1 | 0 | {'p': 3, 'q_next': 5, 'y': 2, 'min_margin': 1, 'min_data': {'h': 1, 'skeleton': 2, 'tail_incidence': 1, 'margin': 1}, 'bad_margin_row_count': 0} |

## 审稿解释

扫描显示 `y≈p/e` 位于一个稳定安全区间内，而不是孤立调参点。过小的 `y` 会保留太大的骨架并给尾素数过多命中机会；中等 `y` 后，尾素数带变短，`G_y(h)>T_y(h)` 在样本中稳定成立。
