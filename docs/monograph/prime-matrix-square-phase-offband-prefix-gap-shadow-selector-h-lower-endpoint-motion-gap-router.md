# Prime Matrix square-phase off-band prefix gap shadow selector H lower endpoint motion gap router

**状态：** `endpoint_motion_gap_fill_profile_closed_current_sweep_global_bound_open`

按首次激活顺序看，活跃 `ell` 带端点扩张只制造了 3 次内部素数缺口，缺口 `ell` 为 [31, 43, 59]，当前扫描内最大已知填充延迟为 80。所有千级 P 前缀快照均保持连续素数带。全局剩余因此可进一步表述为：证明端点扩张制造的内部缺口有统一填充界，或把持久缺口登记并排斥为 Gap-PDEC/SAE。

```text
activation_count=21
gap_snapshot_count=3
gap_ells=[31, 43, 59]
max_known_gap_fill_delay=80
all_activation_gaps_filled_in_current_sweep=true
all_1000_prefix_snapshots_exact_intervals=true
final_active_band=[23, 109]
row_column_unconditional_closed=false
```

## 1. 首次激活

| p | ell | side | residue | slot | margin |
| ---: | ---: | --- | ---: | --- | ---: |
| 2017 | 41 | `plus` | 8 | `['195:47:41']` | 17 |
| 2027 | 37 | `minus` | 29 | `['185:41:37']` | 13 |
| 2063 | 47 | `plus` | 42 | `['177:37:47']` | 13 |
| 2137 | 43 | `minus` | 30 | `['198:45:43']` | 16 |
| 2687 | 29 | `minus` | 19 | `['242:53:29']` | 15 |
| 2767 | 31 | `plus` | 8 | `['229:46:31']` | 27 |
| 3137 | 53 | `minus` | 10 | `['297:69:53']` | 27 |
| 3187 | 61 | `minus` | 15 | `['229:38:61']` | 21 |
| 3257 | 59 | `minus` | 12 | `['287:61:59']` | 29 |
| 3967 | 67 | `minus` | 14 | `['375:87:67']` | 34 |
| 4177 | 71 | `minus` | 59 | `['358:74:71']` | 38 |
| 4337 | 73 | `minus` | 30 | `['404:92:73']` | 32 |
| 4987 | 23 | `minus` | 19 | `['484:116:23']` | 45 |
| 5197 | 79 | `minus` | 62 | `['435:87:79']` | 54 |
| 5557 | 83 | `plus` | 79 | `['537:129:83']` | 45 |
| 7207 | 89 | `plus` | 87 | `['714:177:89']` | 46 |
| 7537 | 97 | `minus` | 68 | `['750:186:97']` | 75 |
| 8387 | 101 | `minus` | 4 | `['813:195:101']` | 46 |
| 8537 | 103 | `minus` | 91 | `['834:202:103']` | 68 |
| 9277 | 107 | `minus` | 75 | `['880:206:107']` | 64 |
| 9817 | 109 | `minus` | 7 | `['853:179:109']` | 74 |

## 2. 缺口快照

| p | activated ell | band | missing | fill delays |
| ---: | ---: | --- | --- | --- |
| 2063 | 47 | `37..47` | `[43]` | `{'43': 74}` |
| 2687 | 29 | `29..47` | `[31]` | `{'31': 80}` |
| 3187 | 61 | `29..61` | `[59]` | `{'59': 70}` |

## 3. 千级 P 前缀

| cutoff | active count | band | exact interval | missing |
| ---: | ---: | --- | ---: | --- |
| 3000 | 6 | `29..47` | `true` | `[]` |
| 4000 | 10 | `29..67` | `true` | `[]` |
| 5000 | 13 | `23..73` | `true` | `[]` |
| 6000 | 15 | `23..83` | `true` | `[]` |
| 7000 | 15 | `23..83` | `true` | `[]` |
| 8000 | 17 | `23..97` | `true` | `[]` |
| 9000 | 19 | `23..103` | `true` | `[]` |
| 10000 | 21 | `23..109` | `true` | `[]` |

## 4. 结构结论

- 当前端点扩张不是任意散乱激活，而是带短暂内部缺口的素数带运动。
- 缺口事件只有三类：`43`、`31`、`59`，并且当前扫描内都被后续首次激活填回。
- 全局闭合仍需要证明统一填充界，或证明持久缺口会形成可排斥的 Gap-PDEC/SAE。

## 5. 下一步

- 主攻：`EndpointMotionGapFillBoundOrGapPDECExclusion`。
- 将缺口填充延迟写成端点 CRT 相位宽度与新 `ell` 首次激活原子的比较不等式。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_endpoint_motion_gap_router.py` | `be5c18dc5191353ea5944c999405104ab550a6d9a9fdf6b031b85a4d9813b1cf` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json` | `60a85b991523e1af0bdb40c950945b3db3163d1132d1ff441e8ccbc46ade0ac6` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json` | `49723eba352f20363d6be36712caf088dbebab1a89f2ed5707d7c0ce76a228e9` |
