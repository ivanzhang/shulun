# Prime Matrix cycle-debt K13 full-debt nine-lane tail router

**状态：** `k13_nine_lane_residual_tail_layer_invariant_and_crt_lower_bound`

K=13 九 lane 全债务分支中，27 个正容量行与 27 个需求行在第 1 层 Hall 完全贴边，所以所有正容量行都必须使用。总容量 119、总需求 101，残余 tail 恰为 18 槽，且层 slack 向量在阈值 1,4,7,8 为零。这说明 residual slack-tail 不是匹配伪影。在固定九 lane 的所有可行匹配中，tail 至少激活 8 个互素阻断素因子，最小 tail lcm 约为 10^11.488，已经超过本地周期 5680。因此剩余接口压成层不变量 tail-CRT PDEC，或真正移动族 SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE
period_p=5680
capacity_row_count=27
demand_row_count=27
all_capacity_rows_mandatory=true
total_capacity=119
total_demand_width=101
unavoidable_tail_slot_count=18
zero_slack_layers=[1, 4, 7, 8]
allowed_deltas=[0, 8, 22, 39, 54, 55, 58, 59, 66]
allowed_edge_count=71
min_tail_factor_count=8
min_tail_factors=[3, 7, 11, 13, 19, 127, 151, 281]
min_tail_lcm_log10=11.488
min_tail_lcm_exceeds_period=true
next_direct_attack_target=K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE
```

## 1. layer slack invariant

| threshold | supply rows | demand rows | slack | zero slack |
| ---: | ---: | ---: | ---: | :---: |
| 1 | 27 | 27 | 0 | true |
| 2 | 21 | 18 | 3 | false |
| 3 | 15 | 12 | 3 | false |
| 4 | 9 | 9 | 0 | true |
| 5 | 9 | 7 | 2 | false |
| 6 | 7 | 6 | 1 | false |
| 7 | 5 | 5 | 0 | true |
| 8 | 4 | 4 | 0 | true |
| 9 | 4 | 3 | 1 | false |
| 10 | 4 | 2 | 2 | false |
| 11 | 4 | 2 | 2 | false |
| 12 | 3 | 2 | 1 | false |
| 13 | 3 | 2 | 1 | false |
| 14 | 2 | 1 | 1 | false |
| 15 | 2 | 1 | 1 | false |

## 2. tail factor optimization

| objective | active factors | log10 tail lcm | tail slots | exceeds period |
| --- | ---: | ---: | ---: | :---: |
| `min_count` | 8 | 11.488 | 18 | true |
| `min_log` | 8 | 11.488 | 18 | true |
| `max_count` | 22 | 36.433 | 18 | true |
| `max_log` | 22 | 36.433 | 18 | true |

## 3. lane tail ranges

| delta | min tail slots | max tail slots |
| ---: | ---: | ---: |
| 0 | 0 | 2 |
| 8 | 0 | 2 |
| 22 | 2 | 2 |
| 39 | 9 | 9 |
| 54 | 0 | 0 |
| 55 | 0 | 0 |
| 58 | 2 | 2 |
| 59 | 2 | 2 |
| 66 | 1 | 1 |

## 4. current witness tail rows

| source | target | delta | capacity | width | tail slots | tail factors |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 49 | 49 | 0 | 3 | 1 | 2 | `[3, 19]` |
| 50 | 1 | 22 | 3 | 2 | 1 | `[11]` |
| 68 | 19 | 22 | 5 | 4 | 1 | `[7]` |
| 15 | 54 | 39 | 3 | 1 | 2 | `[3, 151]` |
| 19 | 58 | 39 | 15 | 8 | 7 | `[3, 7, 11, 13, 127]` |
| 30 | 17 | 58 | 11 | 9 | 2 | `[3, 281]` |
| 20 | 8 | 59 | 6 | 4 | 2 | `[3, 7]` |
| 57 | 52 | 66 | 2 | 1 | 1 | `[3]` |

## 5. 判定

- 第 1 层 Hall slack 为 `0`，所以没有备用容量行；任何 full-debt 匹配都必须使用全部 27 个正容量行。
- `sum layer_slack = total_capacity-total_demand = 18`，残余 tail 槽数是层账本不变量。
- 零 slack 层 `1,4,7,8` 是移动槽的刚性门；在这些层失去一行容量会立即破坏 Hall 条件，除非产生新的 arrival/PDEC。
- 在九 lane 约束内，即使优化 tail 因子，仍至少需要 8 个互素 blocker，tail lcm 约 `10^11.488`。
- 因此 residual slack-tail 出口被命名为层不变量 tail-CRT PDEC 或真正 moving-family SAE。
- 下一主攻点：`K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json` | `48c044e9957e2e14cb3f160b7c5fa6bd818fff5f55341fab9417753de39b6d49` |
