# FO-PDEC 拼接可行性审计

**状态：** `finite_fo_pdec_stitching_feasibility_audit_not_global_proof`

本文档直接审计 `FormalUnit-Stitching` 与 `NestedBlock-Independence`。它区分“有限库聚合信号”和“单个正式反例分支可用的 PDEC 向量”。

## 总表

| object | mass | ell | h | Fourier | support |
| --- | ---: | ---: | ---: | ---: | ---: |
| global library raw | 4 | 199 | 95 | 3.959248 | 3 |
| q-row coordinate dedup best | 1 | 19 | 1 | 1.000000 | 1 |
| block-local best | 1 | 19 | 1 | 1.000000 | 1 |

结论：强阈值 `3.959...` 是有限库聚合信号；在单个 `q` 行坐标去重或单个 Hall 块口径下，当前最佳值只有 `1.0`。

## 嵌套同坐标重复

| key | multiplicity | blocks | status |
| --- | ---: | --- | --- |
| `[1993, 836, 835, 1915, -126, 1664077, 19, 18]` | 2 | `[1, 4]` | `not_independent_without_weighted_hall_dual_row` |
| `[1993, 836, 835, 1919, -126, 1664081, 127, 73]` | 2 | `[1, 4]` | `not_independent_without_weighted_hall_dual_row` |
| `[1993, 836, 836, 78, 30, 1664233, 83, 6]` | 2 | `[1, 4]` | `not_independent_without_weighted_hall_dual_row` |
| `[1993, 836, 836, 82, 30, 1664237, 199, 40]` | 2 | `[1, 4]` | `not_independent_without_weighted_hall_dual_row` |
| `[1993, 836, 836, 84, 30, 1664239, 193, 64]` | 2 | `[1, 4]` | `not_independent_without_weighted_hall_dual_row` |
| `[1993, 836, 836, 126, 84, 1664281, 29, 24]` | 2 | `[1, 4]` | `not_independent_without_weighted_hall_dual_row` |
| `[1993, 836, 836, 138, 84, 1664293, 79, 46]` | 2 | `[1, 4]` | `not_independent_without_weighted_hall_dual_row` |

嵌套同坐标重复的 CRT 方程完全相同。它只有在加权 Hall 对偶中被证明为两条独立约束行时才可重复计数；否则必须按同一正式坐标去重。

## 跨层同整数复用

| candidate | factorization | factor | q layers | row residues | status |
| ---: | --- | ---: | --- | --- | --- |
| 250477 | `[19, 13183]` | 19 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 2}, {'q': 967, 'row': 260, 'target_residue': 13}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250507 | `[397, 631]` | 397 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 325}, {'q': 967, 'row': 260, 'target_residue': 260}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250507 | `[397, 631]` | 631 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 325}, {'q': 967, 'row': 260, 'target_residue': 260}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250511 | `[31, 8081]` | 31 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 15}, {'q': 967, 'row': 260, 'target_residue': 12}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250513 | `[67, 3739]` | 67 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 57}, {'q': 967, 'row': 260, 'target_residue': 59}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250531 | `[29, 53, 163]` | 29 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 6}, {'q': 967, 'row': 260, 'target_residue': 28}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250531 | `[29, 53, 163]` | 53 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 7}, {'q': 967, 'row': 260, 'target_residue': 48}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250531 | `[29, 53, 163]` | 163 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 162}, {'q': 967, 'row': 260, 'target_residue': 97}]` | `not_same_formal_branch_without_persistence_theorem` |
| 250541 | `[199, 1259]` | 199 | `[773, 967]` | `[{'q': 773, 'row': 325, 'target_residue': 126}, {'q': 967, 'row': 260, 'target_residue': 61}]` | `not_same_formal_branch_without_persistence_theorem` |

跨层同整数复用说明同一个合数可在不同方阵宽度中持续被旧小因子解释。但这不是自动的单分支 `PDEC` 向量：必须证明同一个假设反例链会同时强制这些 `q` 层事件，且存在统一相位映射。否则它只是有限库中的相似样本。

## 硬攻结论

当前最严谨的结论是一个排除误用的二分：

```text
A. 证明 weighted Hall dual independence + cross-q persistence theorem，
   然后 global_library_raw 强阈值才可进入 PDEC；

B. 若不能证明 A，则重复项必须去重或回流 SAE/Endpoint，
   不能用 3.959... 直接闭合全局证明。
```

因此本轮没有完成全局无条件证明；但它把剩余硬点压缩为两个可审稿的具体定理，而不是继续停留在泛泛的 `U_CRT` 常数优化。
