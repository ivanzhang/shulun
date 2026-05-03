# RPZ 三路线闭合审计

**状态：** `rpz_three_route_closure_audit`

## 总结

- 路线数：`3`。
- 已全局闭合路线数：`0`。
- 当前推荐优先路线：`A_formal_family_avoidance`。
- 硬边界：`none_closed_yet`。

## 三路线表

| rank | route | status | next atomic target |
|---:|---|---|---|
| 1 | `A_formal_family_avoidance` | `current_ledger_avoids_all_grid_fail` | prove formal-family phase inequality delta<=p-r or formal-family avoids unit endpoint gate rows |
| 2 | `B_endpoint_PDEC` | `support_and_test_function_materialized_upper_bound_missing` | derive admissible U_CRT upper bound for the same unit endpoint bad-window family |
| 3 | `C_columnCRT_defect_exclusion` | `routes_to_defect_threshold_tuning_obstructed` | prove an independent ColumnCRTDefect exclusion theorem, not a smaller L_D threshold |

## 路线 A：formal-family avoidance

当前有限下降账本中，`20` 个实际转换节点全部避开 `grid_fail`，闭式判据无计数或相位不一致。这说明避开路线与已有证据一致。未闭合点是：还没有证明正式反例族必须落入这些已审计相位轨道，或必须满足 `delta<=p-r`。

因此路线 A 的最小目标是：证明 formal-family 的下降相位不命中 unit endpoint gate rows，或直接证明其每步满足 `delta<=p-r`。

## 路线 B：endpoint-PDEC

PDEC 输入已经具备：`12` 条单余类支持行、测试函数 `F=1_rho-1/r`、Fourier 支持频率。缺口是同一正式坏窗族上的 `U_CRT` 上界与合法线性约束来源。该路线可并行推进，但当前不能闭合。

## 路线 C：ColumnCRTDefect

固定非零位移入口已经具备；但阈值障碍证书显示，调小 `L_D` 只会触发 `ColumnCRTDefect`，不是排除。该路线必须升级为独立 `ColumnCRTDefect` 排斥定理，短期不应作为最快闭合路线。

## 执行结论

三选一并进后，当前应优先攻路线 A。路线 B 保留为备选上界路线；路线 C 已被压成独立深定理，不再尝试靠阈值调参闭合。
