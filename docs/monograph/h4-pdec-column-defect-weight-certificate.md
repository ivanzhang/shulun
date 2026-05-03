# H4-PDEC ColumnDefect 有限权重证书

**状态：** `finite_column_defect_weight_certificate_not_global_exclusion`

## 参数

- `max_p`: `1000`
- `y_ratio`: `0.36787944117144233`
- `keep_rows`: `5`
- `radius_threshold`: `81`
- `displacement_threshold`: `2`

## 复现来源

- 生成脚本：`experiments/prime_matrix_h4_pdec_column_defect_weight_certificate.py`
- 生成脚本 SHA256：`04339c15c6b4fbaf01cb7449150830be7980fa9d2a7932c0c8caad2a210820a8`
- 审计模块：`experiments/prime_matrix_rci_cdb_joint_audit.py`
- 审计模块 SHA256：`75573eefc620f06e4faf5e5819fecbe6607d92290c53d4da0fd002156e81f0f8`

## 有限相位域

- `tau`: `tau_fin=(p,q,row)`
- `phase_count`: `835`
- `prime_count`: `167`
- 相位兼容性：权重只依赖 `tau_fin=(p,q,row)`，因此在本有限域中相位兼容。

## 证书结论

- 全部证书行通过：`true`。
- 观测最大列见证半径：`81`。
- 观测最大位移余类负载：`2`。
- 非空异常块：`[]`。

## 证书行

| row_id | event | threshold | observed_max | phase_block_size | bound | pass |
|---|---|---:|---:|---:|---:|---|
| CC-FIN-TIGHT-RADIUS-WEIGHT | `max_column_witness_radius > radius_threshold` | 81 | 81 | 0 | 0 | `true` |
| CC-FIN-DISPLOAD-WEIGHT | `max_displacement_residue_load > displacement_threshold` | 2 | 2 | 0 | 0 | `true` |

## 审稿边界

本证书只闭合 `p<=1000` 且每个 `p` 只取 `5` 条最紧 RCI 行的有限相位兼容权重物化。
它不能直接排除全局 `ColumnRadiusDefect` 或 `ColumnCRTDefect`，也不能替代全局阈值 `D_0,L_D` 的解析证明。

若要进入全局 `PDEC-Dual-Cert`，还需证明正式坏窗抽取过程落在同一有限相位域，或把 `tau_fin` 的权重结构提升为全局相位兼容定理。
