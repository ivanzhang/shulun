# FO-PDEC Formal Unit 一致性审计

**状态：** `finite_fo_pdec_formal_unit_audit_not_global_proof`

本文档审计当前 `ell=199` 强阈值是否可作为正式 `PDEC` 向量使用。核心规则是：`PDEC` 的 `g(t)` 必须来自同一个坏窗集合或多重集合；跨 `q` 层、嵌套块或物理重复若要合并，必须先给出独立性或持久拼接引理。

## 口径摘要

| mode | status | units | best unit | mass | ell | h | Fourier | support |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| global_library_raw | `diagnostic_only_requires_persistent_stitching` | 1 | `['global']` | 4 | 199 | 95 | 3.959248 | 3 |
| global_layer_dedup | `diagnostic_only_requires_cross_level_stitching` | 1 | `['global']` | 3 | 199 | 95 | 2.969837 | 3 |
| global_physical_dedup | `diagnostic_only_physical_projection` | 1 | `['global']` | 2 | 199 | 81 | 1.999751 | 2 |
| q_row_raw | `single_matrix_row_raw_nested_duplicates_allowed_only_with_block_independence` | 3 | `[1993, 836]` | 2 | 199 | 1 | 2.000000 | 1 |
| q_row_coordinate_dedup | `single_matrix_row_coordinate_dedup` | 3 | `[1993, 836]` | 1 | 1013 | 1 | 1.000000 | 1 |
| block_local_raw | `single_hall_block` | 4 | `[1]` | 1 | 439 | 1 | 1.000000 | 1 |
| offset_row_raw | `single_fixed_offset_row` | 11 | `[2]` | 1 | 439 | 1 | 1.000000 | 1 |

## 最佳因子重复来源

| type | multiplicity | key | sources | proof obligation |
| --- | ---: | --- | --- | --- |
| `nested_same_formal_coordinate` | 2 | `[1993, 836, 836, 82, 30, 1664237, 199, 40]` | `[{'block_index': 1, 'offset_row_index': 2, 'p': 1987, 'q': 1993, 'source_row': 836, 'candidate': 1664237, 'factor': 199, 'target_residue': 40}, {'block_index': 4, 'offset_row_index': 9, 'p': 1987, 'q': 1993, 'source_row': 836, 'candidate': 1664237, 'factor': 199, 'target_residue': 40}]` | 需要 NestedBlock-Independence；否则只能按一个正式坐标计数。 |
| `cross_level_same_physical_candidate` | 2 | `[250541, 199]` | `[{'block_index': 2, 'offset_row_index': 5, 'p': 769, 'q': 773, 'source_row': 325, 'candidate': 250541, 'factor': 199, 'target_residue': 126}, {'block_index': 3, 'offset_row_index': 7, 'p': 953, 'q': 967, 'source_row': 260, 'candidate': 250541, 'factor': 199, 'target_residue': 61}]` | 需要 CrossLevel-Stitching；否则不能把不同 q 层拼成同一 PDEC 向量。 |

## 审稿结论

当前 `global_library_raw` 的强阈值 `3.959247567099438` 来自有限证书库的聚合：它同时使用了不同 `q` 层的方程，并且包含嵌套块的同一正式坐标重复。因此它不能直接作为单个正式反例分支的 `PDEC` 下界，除非补上以下至少一项：

1. `FormalUnit-Stitching`：证明这些跨 `q` 层事件属于同一个持久坏窗族，并给出统一相位映射与计数向量；
2. `NestedBlock-Independence`：证明嵌套块重复在 Hall/PDEC 对偶中代表不同独立约束行，且 `U_CRT` 上界也按同一多重集合计算；
3. `SAE/Endpoint absorption`：若无法拼接或独立化，则把重复事件视为孤立端点/非持久样本并回流到 SAE/Endpoint，而不能计入强阈值。

在上述接口未闭合前，`ell=199` 的强阈值只能作为硬点定位工具，不能升级为全局无条件证明。
