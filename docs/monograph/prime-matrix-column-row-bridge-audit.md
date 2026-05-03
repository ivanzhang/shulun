# 列输入到行命题桥接强度审计

**状态：** `experimental_column_input_bridge_strength_not_a_proof`

## 参数

- `max_q`: `1000`

## 总结

- 检查奇素数个数：`167`。
- 数据中列命题失败记录数：`0`。
- 全局最小行素数数：`1`。
- 最大列见证半径：`107`。

## 最薄行记录

- `q`: `3`
- `min_row_prime_count`: `1`
- `min_row_records`: `[{'row': 2, 'row_interval': [4, 6], 'row_prime_count': 1, 'column_witness_radius': 1, 'nontrivial_columns_with_witness_distance_le_1': 2, 'nontrivial_columns_with_witness_distance_le_2': 2, 'nontrivial_columns_with_witness_distance_le_5': 2, 'max_distance_columns': [1]}, {'row': 3, 'row_interval': [7, 9], 'row_prime_count': 1, 'column_witness_radius': 1, 'nontrivial_columns_with_witness_distance_le_1': 2, 'nontrivial_columns_with_witness_distance_le_2': 2, 'nontrivial_columns_with_witness_distance_le_5': 2, 'max_distance_columns': [2]}]`

## 最大列见证半径记录

- `q`: `929`
- `max_column_witness_radius`: `107`
- `max_radius_rows`: `[{'row': 929, 'row_interval': [862113, 863041], 'row_prime_count': 78, 'column_witness_radius': 107, 'nontrivial_columns_with_witness_distance_le_1': 142, 'nontrivial_columns_with_witness_distance_le_2': 214, 'nontrivial_columns_with_witness_distance_le_5': 372, 'max_distance_columns': [322]}]`

## 审稿解释

列命题若作为已证输入，只能保证每个非平凡列 `c<q` 某处有素数；第 `q` 列只有平凡见证 `q`，本审计已将其从桥接半径中剥离。要推出固定行非空，还需要把这些列素数见证拉回该行附近，或证明拉不回时产生端点/尾锚缺陷。

本审计量化了这个缺口：`D_col(r)` 是覆盖所有列所需的最小纵向半径。若 `D_col(r)` 无显式小上界，列命题不能直接推出行命题；若能证明坏行导致 `D_col(r)` 异常并触发 CRT 缺陷，则可形成行列闭锁桥接。
