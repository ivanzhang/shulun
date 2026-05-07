# FO-PDEC 嵌套重复支配审计

**状态：** `audited_nested_full_multiplicity_blocked_not_global_proof`

当前 FO-PDEC 有限审计中的 exact nested duplicates 全部是同一正式坐标上的嵌套支撑重复。因此它们不能按单位权作为两个独立 PDEC 事件计数；若要保留权重，必须提交同口径的 fractional Weighted Hall dual 证书，否则应坐标商掉或回流 SAE/Endpoint。

## 1. 子门裁定

```text
closed_subgate: NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC
raw_best_factor: 199
raw_best_frequency: 95
raw_best_fourier: 3.959247567099438
all_exact_nested_duplicates_unit_weight_blocked: true
factor_199_nested_duplicate_unit_weight_blocked: true
```

## 2. 逐重复审计

| key | blocks | multiplicity | support relation | sizes | unit status |
| --- | --- | ---: | --- | --- | --- |
| [1993, 836, 835, 1915, -126, 1664077, 19, 18] | [1, 4] | 2 | block_2_support_subset_block_1_support | [5, 4] | blocked_by_same_coordinate_nested_support |
| [1993, 836, 835, 1919, -126, 1664081, 127, 73] | [1, 4] | 2 | block_2_support_subset_block_1_support | [5, 4] | blocked_by_same_coordinate_nested_support |
| [1993, 836, 836, 78, 30, 1664233, 83, 6] | [1, 4] | 2 | block_2_support_subset_block_1_support | [5, 4] | blocked_by_same_coordinate_nested_support |
| [1993, 836, 836, 82, 30, 1664237, 199, 40] | [1, 4] | 2 | block_2_support_subset_block_1_support | [5, 4] | blocked_by_same_coordinate_nested_support |
| [1993, 836, 836, 84, 30, 1664239, 193, 64] | [1, 4] | 2 | block_2_support_subset_block_1_support | [5, 4] | blocked_by_same_coordinate_nested_support |
| [1993, 836, 836, 126, 84, 1664281, 29, 24] | [1, 4] | 2 | block_2_support_subset_block_1_support | [5, 4] | blocked_by_same_coordinate_nested_support |
| [1993, 836, 836, 138, 84, 1664293, 79, 46] | [1, 4] | 2 | block_2_support_subset_block_1_support | [5, 4] | blocked_by_same_coordinate_nested_support |

## 3. 证明含义

同一正式坐标给出的整数、解释因子、CRT 行相位和双线性方程完全相同。若两个 Hall 块的半素数支撑又是嵌套关系，则第二个块没有自动产生第二个算术事件。因此单位权重复计数不合法；合法选择只有三类：

1. 提交同一多重 formal unit 上的 fractional Weighted Hall dual，并保证每个坐标的对偶权重总和受控；
2. 对 exact duplicate 取坐标商，转入 primitive PDEC 阈值；
3. 把不能持久化的重复视作 SAE/Endpoint 局部逃逸并吸收。

## 4. 剩余

- `fractional Weighted Hall dual independence, if one wants to keep weighted multiplicity`
- `coordinate quotient / primitive PDEC threshold after removing duplicate unit mass`
- `exact duplicate SAE/Endpoint absorption`
- `cross-q persistence theorem for cross-level reuses`
