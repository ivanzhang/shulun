# Prime Matrix AffineTwin unused-target arrival audit

**状态：** `current_sweep_unused_target_arrivals_closed_global_open`

本审计继续下钻 `WindowEdgeCollision` 的 unused-target 分支：空窗 formal pair 若要落到当前未使用的 target pair，必须让 target pair 进入当前形式积，并支付 residue 位移对应的 CRT 相位跳跃。

```text
unused_target_arrival_candidate_count=9
unique_unused_target_pair_count=5
required_unique_side_residue_arrival_count=9
occurrence_new_side_residue_requirement_total=17
min_new_side_residues_per_candidate=1
max_new_side_residues_per_candidate=2
min_abs_crt_jump_to_unused_target=59
max_abs_crt_jump_to_unused_target=375
support_width_current=20
unused_target_arrival_closed_current_sweep=true
```

## 1. unused-target arrival 表

| source | target unused | target P | new g | new f | new count | L1 | CRT jump | jump-width | multiplicity |
| --- | --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| `13:8` | `16:5` | 2684 | `true` | `true` | 2 | 6 | 90 | 70 | 2 |
| `13:9` | `16:5` | 2684 | `true` | `true` | 2 | 7 | 345 | 325 | 2 |
| `13:12` | `18:7` | 2686 | `true` | `true` | 2 | 10 | 150 | 130 | 1 |
| `13:28` | `10:30` | 2678 | `true` | `true` | 2 | 5 | 374 | 354 | 3 |
| `15:8` | `17:6` | 2685 | `true` | `true` | 2 | 4 | 60 | 40 | 2 |
| `15:9` | `17:6` | 2685 | `true` | `true` | 2 | 5 | 375 | 355 | 2 |
| `15:28` | `10:30` | 2678 | `true` | `true` | 2 | 7 | 343 | 323 | 3 |
| `19:12` | `20:9` | 2688 | `true` | `false` | 1 | 4 | 59 | 39 | 1 |
| `19:28` | `10:30` | 2678 | `true` | `true` | 2 | 11 | 281 | 261 | 3 |

## 2. 当前读数

- 当前形式 generator residues 为 `[13, 15, 19]`，fill residues 为 `[8, 9, 12, 28]`。
- `9` 个 unused-target 候选压缩到 `5` 个唯一 target pairs：`{'10:30': 3, '16:5': 2, '17:6': 2, '18:7': 1, '20:9': 1}`。
- 这些 target 全部不在当前形式积中；唯一侧残基需求为 generator `[10, 16, 17, 18, 20]` 与 fill `[5, 6, 7, 30]`，合计 `9` 个新侧残基。
- 最窄 residue atom 是 `19:12 -> 20:9`，`L1=4`，但仍需 `1` 个新侧残基，CRT 跳跃 `59`。
- 最小 CRT 跳跃 atom 是 `19:12 -> 20:9`，跳跃 `59`，仍比窗口宽度多 `39`。

## 3. 结论边界

- 本步关闭当前 sweep 的 unused-target arrival 账本：所有 unused target 均在当前形式积外，均至少需要一个新侧残基，并且 CRT 跳跃均大于支撑宽度。
- 本步不证明全局 unused-target arrival 不发生；全局剩余是控制新 generator/fill residue 到达，或把失败路由到 `NewGeneratorResidueArrival-PDEC/SAE`、`NewFillResidueArrival-PDEC/SAE`、`SupportMotionEscape-PDEC/SAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-window-edge-collision-ledger.json` | `344885dd9ed7914d65f259e2b63626a2837703893cbf23623e034b34c6cfe334` |
| `data/prime-matrix-affine-twin-crt-window-gap-ledger.json` | `4822729687dfb1818e8d917ca278f2eeda8d167825456f1dc1dd0456e142f71f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
