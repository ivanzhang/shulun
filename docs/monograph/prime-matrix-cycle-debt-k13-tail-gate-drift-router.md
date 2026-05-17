# Prime Matrix cycle-debt K13 tail gate drift router

**状态：** `k13_layer_gate_profile_has_no_near_replay_except_base_shift`

在 support replacement 的 16 个 near-shift 中，K=13 的完整 slack 向量只有基准 shift=13 自身复现。唯一另一个 Hall survivor 是 K=14，但它把零 slack 门从 1,4,7,8 漂移到 7,8,13,15，tail balance 从 18 增至 31，slack 向量 L1 距离为 19。因此 K=13 层不变量 tail 不能近程无漂移重播；若反例链移动，必须进入 K14 high-gate drift SAE/PDEC。

```text
row_column_unconditional_closed=false
previous_hardpoint=K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE
period_p=5680
near_shift_limit_cycles=16
hall_pass_shifts=[13, 14]
same_slack_vector_shifts=[13]
same_zero_gate_set_shifts=[13]
passing_same_slack_vector_shifts=[13]
k13_tail_balance=18
k13_zero_slack_layers=[1, 4, 7, 8]
k13_min_tail_factor_count=8
k13_min_tail_lcm_log10=11.488
k14_tail_balance=31
k14_tail_increase_over_k13=13
k14_zero_slack_layers=[7, 8, 13, 15]
k14_slack_l1_distance_from_k13=19
k14_zero_gate_lost_from_k13=[1, 4]
k14_zero_gate_gained_over_k13=[13, 15]
next_direct_attack_target=K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE
```

## 1. near-shift gate comparison

| K | Hall pass | tail balance | zero gates | L1 from K13 | gate symmetric diff |
| ---: | :---: | ---: | --- | ---: | --- |
| 1 | false | -5 | `[2, 3, 4, 6, 10, 11, 12, 14]` | 23 | `[1, 2, 3, 6, 7, 8, 10, 11, 12, 14]` |
| 2 | false | -2 | `[1, 3, 9, 11]` | 24 | `[3, 4, 7, 8, 9, 11]` |
| 3 | false | -14 | `[9, 10]` | 34 | `[1, 4, 7, 8, 9, 10]` |
| 4 | false | -25 | `[2, 3]` | 43 | `[1, 2, 3, 4, 7, 8]` |
| 5 | false | 3 | `[]` | 33 | `[1, 4, 7, 8]` |
| 6 | false | -11 | `[]` | 35 | `[1, 4, 7, 8]` |
| 7 | false | -19 | `[]` | 37 | `[1, 4, 7, 8]` |
| 8 | false | -4 | `[6, 7]` | 28 | `[1, 4, 6, 8]` |
| 9 | false | -3 | `[2, 10, 14, 15]` | 25 | `[1, 2, 4, 7, 8, 10, 14, 15]` |
| 10 | false | 5 | `[9, 10, 11, 12, 13]` | 19 | `[1, 4, 7, 8, 9, 10, 11, 12, 13]` |
| 11 | false | 20 | `[7, 9]` | 14 | `[1, 4, 8, 9]` |
| 12 | false | 6 | `[7, 9, 13, 15]` | 14 | `[1, 4, 8, 9, 13, 15]` |
| 13 | true | 18 | `[1, 4, 7, 8]` | 0 | `[]` |
| 14 | true | 31 | `[7, 8, 13, 15]` | 19 | `[1, 4, 13, 15]` |
| 15 | false | 19 | `[8, 12, 13, 14, 15]` | 19 | `[1, 4, 7, 12, 13, 14, 15]` |
| 16 | false | 10 | `[5, 7, 11, 12, 14, 15]` | 18 | `[1, 4, 5, 8, 11, 12, 14, 15]` |

## 2. 判定

- `same_slack_vector_shifts=[13]`，说明 K=13 的层 slack 形状在 near-shift 窗口内没有第二个复本。
- `hall_pass_shifts=[13,14]`，所以唯一可动 survivor 是 K=14。
- K=14 只保留共同零门 `7,8`，丢失 K=13 的低门 `1,4`，新增高门 `13,15`。
- tail balance 从 `18` 增至 `31`，即 moving 分支必须支付额外 `13` 个 tail 槽。
- 因此 K=13 layer-tail 若要近程复现只能固定在原 shift；一旦移动就进入 K14 high-gate drift SAE/PDEC。
- 下一主攻点：`K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json` | `2cc8e902d04fdc3cca2c892030ddcb5d75786f207521c11b5bb43d3c23da8b9d` |
