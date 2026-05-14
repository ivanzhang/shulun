# Prime Matrix square-phase low-alpha z=61 common-core prefix gate

**状态：** `z61_common_core_window_selector_reduced_to_prefix_interval_gate_open`

common-core 窗口选择器已压成一维 prefix 区间门：对 core 分割 `small|large`，prefix `t` 入选当且仅当 `large/(8*small) <= t < large/(4*small)`。在当前 `t in {2,3}` 中，只有 `[19,253]` 接收 `2,3`，`[23,209]` 只接收 `2`。下一步最窄硬点是证明这种 prefix interval gate 的容量受控，或登记 PrefixGate-PDEC。

```text
split_count=4
selected_split_count=2
selected_prefix_total_count=3
selected_weight=0.555427
selected_weight_identity_error=0.000000
prefix_gate_identity_closed=true
row_column_unconditional_closed=false
```

## 1. Prefix 区间门

| core split | large/small | prefix interval | selected prefixes | selected weight |
| --- | ---: | --- | --- | ---: |
| `[23, 209]` | 9.086957 | `[1.135870, 2.271739)` | `[2]` | 0.202029 |
| `[19, 253]` | 13.315789 | `[1.664474, 3.328947)` | `[2, 3]` | 0.353398 |
| `[11, 437]` | 39.727273 | `[4.965909, 9.931818)` | `[]` | 0.000000 |
| `[1, 4807]` | 4807.000000 | `[600.875000, 1201.750000)` | `[]` | 0.000000 |

## 2. 证明边界

- 已闭合：ratio-window 选择到 prefix interval gate 的精确等价。
- 未闭合：prefix interval gate 容量界，或 PrefixGate-PDEC 排斥。
- 下一目标：`PrefixIntervalGateCapacityBoundOrPrefixGatePDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-window-selector-router.json` | `aa7bd238d68b507d20b993017c086649b36078cf9fec7edfa22700a81462b57e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_common_core_prefix_gate_router.py` | `e220bcf88156b6d4a92db9dd32a5f565178f035356d029c1adbebac95387ec31` |
