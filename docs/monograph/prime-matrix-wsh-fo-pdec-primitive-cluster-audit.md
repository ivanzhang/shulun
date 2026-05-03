# FO-PDEC Primitive Cluster 去重审计

**状态：** `finite_fo_pdec_primitive_cluster_audit_not_global_proof`

本文档检查最佳投影中的短弧聚簇是否由独立坏窗方程构成，还是由嵌套块/跨层复用导致的多重计数。它防止把非独立重复误当成全局 `PDEC` 质量。

## 参数

- `ell`: `199`。
- `h`: `95`。

## 去重模式摘要

| mode | primitive | max mult | mass | support | Fourier | mass defect | dual arc |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| equation | 4 | 1 | 4 | 3 | 3.959248 | 0.040752 | 11 |
| block_local | 4 | 1 | 4 | 3 | 3.959248 | 0.040752 | 11 |
| layer_local | 3 | 2 | 3 | 3 | 2.969837 | 0.030163 | 11 |
| physical | 2 | 2 | 2 | 2 | 1.969919 | 0.030081 | 11 |

## 物理事件

| candidate | factor | residue | dual residue | multiplicity | sources |
| ---: | ---: | ---: | ---: | ---: | --- |
| 250541 | 199 | 126 | 30 | 2 | [{'block_index': 2, 'offset_row_index': 5, 'p': 769, 'q': 773, 'source_row': 325}, {'block_index': 3, 'offset_row_index': 7, 'p': 953, 'q': 967, 'source_row': 260}] |
| 1664237 | 199 | 40 | 19 | 2 | [{'block_index': 1, 'offset_row_index': 2, 'p': 1987, 'q': 1993, 'source_row': 836}, {'block_index': 4, 'offset_row_index': 9, 'p': 1987, 'q': 1993, 'source_row': 836}] |

## 审稿解释

若正式坏窗集合 `S` 是多重集合并且确实包含嵌套块/跨层复用，那么 equation 模式的阈值可以使用；若正式 `S` 必须按物理候选去重，则阈值应降到 physical 模式。当前最佳聚簇的质量差异正是最后证明义务：必须证明多重计数合法，或改用 primitive 事件并重新给出 `PDEC/SAE` 排斥。
