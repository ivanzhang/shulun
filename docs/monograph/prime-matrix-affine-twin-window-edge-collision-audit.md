# Prime Matrix AffineTwin window edge-collision audit

**状态：** `current_sweep_window_edge_collision_displacements_closed_global_open`

本审计把 `CRTWindowGap` 的下一失败形态写成 residue 网格位移：共同窗口给出有限个可命中的目标 residue pairs；空窗 formal pair 若要变成 actual packet，必须移动到其中一个目标点。

```text
target_window_pair_count=20
formal_pair_total_with_exact_source=12
supported_actual_packet_total_current=1
edge_collision_candidate_count_current=11
min_empty_l1_residue_displacement=1
max_empty_l1_residue_displacement=11
empty_pairs_target_existing_actual_count=2
empty_pairs_target_unused_residue_arrival_count=9
window_edge_collision_displacement_closed_current_sweep=true
```

## 1. edge-collision 位移表

| pair | CRT gap | nearest target | target P | delta g | delta f | L1 | route |
| --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| `(13,8)` | 75 | `(16,5)` | 2684 | 3 | -3 | 6 | `UnusedTargetResidueArrivalNeeded` |
| `(13,9)` | 341 | `(16,5)` | 2684 | 3 | -4 | 7 | `UnusedTargetResidueArrivalNeeded` |
| `(13,12)` | 133 | `(18,7)` | 2686 | 5 | -5 | 10 | `UnusedTargetResidueArrivalNeeded` |
| `(13,28)` | 365 | `(10,30)` | 2678 | -3 | 2 | 5 | `UnusedTargetResidueArrivalNeeded` |
| `(15,8)` | 44 | `(17,6)` | 2685 | 2 | -2 | 4 | `UnusedTargetResidueArrivalNeeded` |
| `(15,9)` | 372 | `(17,6)` | 2685 | 2 | -3 | 5 | `UnusedTargetResidueArrivalNeeded` |
| `(15,12)` | 102 | `(19,8)` | 2687 | 4 | -4 | 8 | `ExistingActualResidueCollisionNeeded` |
| `(15,28)` | 334 | `(10,30)` | 2678 | -5 | 2 | 7 | `UnusedTargetResidueArrivalNeeded` |
| `(19,9)` | 434 | `(19,8)` | 2687 | 0 | -1 | 1 | `ExistingActualResidueCollisionNeeded` |
| `(19,12)` | 40 | `(20,9)` | 2688 | 1 | -3 | 4 | `UnusedTargetResidueArrivalNeeded` |
| `(19,28)` | 272 | `(10,30)` | 2678 | -9 | 2 | 11 | `UnusedTargetResidueArrivalNeeded` |

## 2. 当前读数

- `q=31` 的窗口 `[2669,2688]` 给出 `20` 个 target residue pairs。
- 当前 `11` 个空窗 formal pairs 到最近 target 的 L1 residue 位移最小为 `1`，最大为 `11`。
- 其中 `2` 个空窗最近目标是已有 actual pair `(19,8)`，因此若复现会变成 existing-actual residue collision。
- 其余 `9` 个空窗最近目标需要未使用 target residue arrival，进入 arrival/PDEC/SAE 接口。

## 3. 结论边界

- 本步关闭当前 sweep 的 edge-collision 位移账本，不证明全局不发生碰撞。
- 全局剩余是证明这些位移需求不能持续由反例链供给，或把失败路由到 `ExistingActualResidueCollision-PDEC`、`UnusedTargetResidueArrival-PDEC/SAE`、`SupportMotionEscape-PDEC/SAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-crt-window-gap-ledger.json` | `4822729687dfb1818e8d917ca278f2eeda8d167825456f1dc1dd0456e142f71f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
