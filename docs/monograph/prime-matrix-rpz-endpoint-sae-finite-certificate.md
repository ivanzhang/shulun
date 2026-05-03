# RPZ Endpoint SAE 有限证书

**状态：** `rpz_endpoint_sae_finite_certificate_current_ledger`

## 总结

- SAE 候选相位数：`2`。
- 当前账本 possible load：`2`。
- 当前账本 actual load：`0`。
- 当前有限账本闭合相位数：`2`。
- 全局出口是否闭合：`False`。

## 证书表

| phase key | possible load | actual load | current verdict | global status |
|---|---:|---:|---|---|
| `[11, 8, 2, 2]` | 1 | 0 | vacuous_current_ledger_closed | not_global_exclusion |
| `[11, 8, 3, 1]` | 1 | 0 | vacuous_current_ledger_closed | not_global_exclusion |

## 审稿解释

两个 endpoint 低负载候选相位在可能失败相位账本中各出现一次，但当前 BCB 审计的实际相位没有命中它们；因此当前有限账本中的 `candidate_windows` 为空，`RPZ-SAE-FIN` 在当前账本层面真空闭合。

这不是全局 `SAE` 排斥。若正式反例族在这些相位上产生实际窗口，必须逐窗给出 `survivor/lift/higher-defect`，或因同相持久进入 `PDEC/ColumnCRT`。

下一步最小硬点应转向三条 `lower_descent_grid_fail` 相位行：证明正式下降路径避开对应 `S_tau`，或填写 `U_CRT<L_PDEC` / `ColumnCRT` 证书。
