# RPZ 下层下降 grid_fail 避开证书

**状态：** `rpz_lower_grid_fail_avoidance_current_ledger`

## 精确判据

设 `p>r` 为相邻素数、`g=p-r`，`p` 对齐行号为 `a`。则

```text
delta = - (a-1) g mod r；
grid_success iff delta <= g；
grid_fail iff delta > g。
```

## 总结

- 转换行数：`5`。
- 存在可能 grid_fail 的转换行数：`3`。
- 实际下降转换节点数：`20`。
- 实际 grid_fail 节点数：`0`。
- 闭式计数与枚举不一致数：`0`。
- 实际节点 delta 与闭式不一致数：`0`。
- 全局避开是否闭合：`False`。

## 转换表

| p | r | Q | gap | fail residues mod r | source fail count | actual nodes | actual fails | min margin |
|---:|---:|---:|---:|---|---:|---:|---:|---:|
| 3 | 2 | 2 | 1 | `[]` | 0 | 6 | 0 | 0 |
| 5 | 3 | 6 | 2 | `[]` | 0 | 6 | 0 | 0 |
| 7 | 5 | 30 | 2 | `[2, 4]` | 12 | 5 | 0 | 0 |
| 11 | 7 | 210 | 4 | `[3, 5]` | 60 | 2 | 0 | 2 |
| 13 | 11 | 2310 | 2 | `[2, 3, 4, 5, 7, 8, 9, 10]` | 1680 | 1 | 0 | 1 |

## 审稿解释

三条待攻 `lower_descent_grid_fail` 行分别来自 `7->5`、`11->7`、`13->11`。本证书证明这些行的失败集合不是黑箱枚举，而是由一维余类不等式 `delta>p-r` 精确给出。

当前实际下降树中的 `20` 个转换节点全部满足 `delta<=p-r`，所以当前有限账本避开所有 `grid_fail` 相位。该结论只闭合当前账本，不证明全局正式反例下降路径必然避开。

下一步真正硬点是证明正式路径的行号相位始终落在 `delta<=p-r`，或在落入 `delta>p-r` 时把同相位族送入 `PDEC/ColumnCRT`。
