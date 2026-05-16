# Prime Matrix AffineTwin CRT window gap audit

**状态：** `current_sweep_crt_window_gap_distances_closed_global_open`

本审计把 `CRTWindowEmpty` 从布尔空窗推进为带距离的相位间隙证书：每个通过 source gate 的 formal residue pair 都合成为一个 CRT 类；只有该类在共同 pair support 中有代表时才是 actual packet。

```text
source_gate_pass_q_values=[31]
formal_pair_total_with_exact_source=12
supported_actual_packet_total_current=1
crt_window_gap_pair_total_current=11
expected_crt_window_empty_pair_total=11
min_empty_window_distance=40
max_empty_window_distance=434
modulus_minus_support_width_current=879
crt_window_gap_closed_current_sweep=true
```

## 1. CRT window 表

| gen residue | fill residue | shifted fill | CRT residue | nearest P | distance | side | route |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 13 | 8 | 21 | 796 | 2594 | 75 | `below` | `CRTWindowGap` |
| 13 | 9 | 22 | 332 | 3029 | 341 | `above` | `CRTWindowGap` |
| 13 | 12 | 25 | 738 | 2536 | 133 | `below` | `CRTWindowGap` |
| 13 | 28 | 10 | 506 | 2304 | 365 | `below` | `CRTWindowGap` |
| 15 | 8 | 21 | 827 | 2625 | 44 | `below` | `CRTWindowGap` |
| 15 | 9 | 22 | 363 | 3060 | 372 | `above` | `CRTWindowGap` |
| 15 | 12 | 25 | 769 | 2567 | 102 | `below` | `CRTWindowGap` |
| 15 | 28 | 10 | 537 | 2335 | 334 | `below` | `CRTWindowGap` |
| 19 | 8 | 21 | 889 | 2687 | 0 | `inside` | `SupportedActualPacket` |
| 19 | 9 | 22 | 425 | 3122 | 434 | `above` | `CRTWindowGap` |
| 19 | 12 | 25 | 831 | 2629 | 40 | `below` | `CRTWindowGap` |
| 19 | 28 | 10 | 599 | 2397 | 272 | `below` | `CRTWindowGap` |

## 2. 当前结构读数

- `q=31` 的共同 pair support 为 `[2669,2688]`，宽度 `20`。
- 合成模数为 `29*31=899`，模数-窗口宽度为 `879`。
- 唯一 supported actual packet 是 `(19,8)`，CRT 代表为 `2687`。
- 其余 `11` 个 formal pairs 的最近 CRT 代表距离窗口至少 `40`，因此是严格正间隙，不是边界等号。

## 3. 结论边界

- 当前 sweep 的 `CRTWindowEmpty=11` 已全部转成正距离 `CRTWindowGap`。
- 这仍不是全局行/列证明；全局需要证明窗口随参数移动时，空窗失败只能进入 `WindowEdgeCollision-PDEC` 或 `SupportMotionEscape-PDEC/SAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/prime-matrix-affine-twin-source-materialization-gate-ledger.json` | `aaaee80eaba6130fa016758509513449beff23eaefa41fcc79a174e183c5e385` |
| `data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json` | `ed8532ade7e13ad9fe14068c545d961ba90a47895b395673cf69169c0967ac38` |
