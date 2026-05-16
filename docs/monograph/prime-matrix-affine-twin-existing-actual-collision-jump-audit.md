# Prime Matrix AffineTwin existing-actual collision CRT jump audit

**状态：** `current_sweep_existing_actual_collision_jumps_closed_global_open`

本审计继续下钻 `WindowEdgeCollision` 中最窄的 existing-actual 分支：空窗 formal pair 若要撞向已经实现的 actual pair，必须支付 residue 位移对应的完整 CRT 相位跳跃。

```text
existing_actual_collision_candidate_count=2
existing_actual_target_pair_count=1
min_existing_actual_residue_l1=1
max_existing_actual_residue_l1=8
min_abs_crt_jump_to_existing_actual=120
max_abs_crt_jump_to_existing_actual=435
support_width_current=20
generator_unit_step_current=465
fill_unit_step_current=435
existing_actual_collision_jump_closed_current_sweep=true
```

## 1. existing-actual CRT 跳跃表

| source | target actual | delta g | delta f | L1 | source rep | target P | CRT jump | jump-width | closed |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `15:12` | `19:8` | 4 | -4 | 8 | 2567 | 2687 | 120 | 100 | `true` |
| `19:9` | `19:8` | 0 | -1 | 1 | 3122 | 2687 | 435 | 415 | `true` |

## 2. 当前读数

- 双模 CRT 单位步长为 `generator_unit=465`、`fill_unit=435`，共同窗口宽度为 `20`。
- 最窄 residue atom 是 `19:9 -> 19:8`，`L1=1`，但 CRT 跳跃为 `435`，比窗口宽度多 `415`。
- 最小 CRT 跳跃 atom 是 `15:12 -> 19:8`，跳跃 `120`，仍比窗口宽度多 `100`。
- 因此当前 existing-actual 碰撞不是窗口边缘的微小滑入；若要全局复现，必须移动支撑/残基结构并进入 repeated-residue、ColumnCRT、PDEC 或 SAE 出口。

## 3. 结论边界

- 本步关闭当前 sweep 的 existing-actual collision CRT 跳跃账本。
- 本步不证明全局 existing-actual collision 不复现；全局剩余是排斥持久复现，或把复现登记为 `RepeatedResidue-ColumnCRT-PDEC` / `SupportMotionEscape-PDEC/SAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-window-edge-collision-ledger.json` | `344885dd9ed7914d65f259e2b63626a2837703893cbf23623e034b34c6cfe334` |
| `data/prime-matrix-affine-twin-crt-window-gap-ledger.json` | `4822729687dfb1818e8d917ca278f2eeda8d167825456f1dc1dd0456e142f71f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
