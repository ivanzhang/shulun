# RPZ 出口证书骨架包

**状态：** `rpz_certificate_skeleton_package`

## 总结

- Endpoint SAE 候选数：`2`。
- Endpoint PDEC 行数：`2`。
- Endpoint ColumnCRT 行数：`2`。
- LowerDescent 可能阻断相位数：`1752`。
- LowerDescent 阻断状态计数：`{'grid_fail': 1752}`。
- LowerDescent PDEC 行数：`3`。
- LowerDescent ColumnCRT 行数：`3`。

## RPZ-SAE-FIN 候选

| source | phase key | possible load | status |
|---|---|---:|---|
| bcb_endpoint_possible_failure | `[11, 8, 2, 2]` | 1 | candidate_not_closed |
| bcb_endpoint_possible_failure | `[11, 8, 3, 1]` | 1 | candidate_not_closed |

## RPZ-PDEC 相位行

| source | type | Q | support size | status |
|---|---|---:|---:|---|
| bcb_endpoint_possible_failure | endpoint_grid_failure | 11 | 1 | skeleton_not_closed |
| bcb_endpoint_possible_failure | endpoint_grid_failure | 11 | 1 | skeleton_not_closed |
| lower_descent_obstruction | grid_fail | 30 | 12 | skeleton_not_closed |
| lower_descent_obstruction | grid_fail | 210 | 60 | skeleton_not_closed |
| lower_descent_obstruction | grid_fail | 2310 | 1680 | skeleton_not_closed |

## 审稿边界

本包完成的是证书骨架材料化：所有已命名端点失败和下层下降阻断相位，都有明确的 `SAE/PDEC/ColumnCRT` 待填行。

本包没有完成 `U_CRT<L_PDEC`、`SAE` 局部逃逸排斥、或 `ColumnCRT` 位移阈值证明；因此不能把 Prime Matrix 行命题升级为无条件定理。

下一步最小硬点是：优先对 `endpoint` 的两个低负载相位填写 `RPZ-SAE-FIN`，同时对 `lower_descent_grid_fail` 三条 PDEC 行尝试证明正式下降路径避开其 `S_tau`。
