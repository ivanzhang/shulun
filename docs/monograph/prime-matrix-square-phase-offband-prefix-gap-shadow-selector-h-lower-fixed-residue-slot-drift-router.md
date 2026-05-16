# Prime Matrix square-phase off-band prefix gap shadow selector H lower fixed-residue slot-drift router

**状态：** `fixed_residue_recurrence_reduced_to_slot_drift_open`

本步检查固定残基复现包的槽位持久性：物理记录数等于 fixed-slot packet 数，因此当前扫描内没有 fixed-slot 复现。12 个跨不同 P 复现的固定残基包全部换槽，`p` 间距均为对应 `ell` 的整数倍，最小倍数 6，最大倍数 100。剩余硬点进一步压成固定残基但槽位漂移的 ColumnCRT/PDEC，外加移动残基 shape 的 SAE/Rankin 界。

```text
physical_record_count=324
slot_packet_count=324
fixed_slot_recurrence_count=0
fixed_residue_recurrent_packet_count=12
all_fixed_residue_recurrences_are_slot_drift=true
all_p_gaps_divisible_by_ell=true
p_gap_over_ell_histogram={'6': 1, '10': 1, '20': 1, '30': 5, '60': 2, '80': 1, '100': 1}
row_column_unconditional_closed=false
```

## 1. 复现对

| residue packet | ell | p values | gap/ell | rho | slots | b gap | u gap | depth | margin |
| --- | ---: | --- | ---: | --- | --- | ---: | ---: | --- | ---: |
| `size=1|side=minus|ells=43|mod=43|residue=16` | 43 | `[2467, 2897]` | 10 | `[7, 2]` | `237:56:43 -> 273:63:43` | 36 | 7 | `[8, 13] -> [7, 14]` | 0 |
| `size=1|side=plus|ells=43|mod=43|residue=20` | 43 | `[2557, 3847]` | 30 | `[7, 7]` | `237:54:43 -> 315:62:43` | 78 | 8 | `[2, 21] -> [16, 14]` | 16 |
| `size=1|side=minus|ells=53|mod=53|residue=45` | 53 | `[2377, 5557]` | 60 | `[7, 7]` | `183:33:53 -> 555:138:53` | 372 | 105 | `[17, 18] -> [2, 17]` | 17 |
| `size=1|side=minus|ells=43|mod=43|residue=37` | 43 | `[2617, 6917]` | 100 | `[7, 2]` | `187:31:43 -> 663:157:43` | 476 | 126 | `[28, 13] -> [13, 8]` | 20 |
| `size=1|side=minus|ells=53|mod=53|residue=25` | 53 | `[2887, 7127]` | 80 | `[7, 2]` | `270:62:53 -> 624:132:53` | 354 | 70 | `[18, 4] -> [6, 20]` | 24 |
| `size=1|side=minus|ells=53|mod=53|residue=31` | 53 | `[3847, 5437]` | 30 | `[7, 7]` | `355:80:53 -> 523:124:53` | 168 | 44 | `[10, 13] -> [1, 20]` | 25 |
| `size=1|side=minus|ells=37|mod=37|residue=14` | 37 | `[3307, 5527]` | 60 | `[7, 7]` | `298:65:37 -> 483:102:37` | 185 | 37 | `[3, 21] -> [13, 13]` | 26 |
| `size=1|side=minus|ells=59|mod=59|residue=42` | 59 | `[5647, 7417]` | 30 | `[7, 7]` | `432:78:59 -> 580:107:59` | 148 | 29 | `[33, 2] -> [3, 30]` | 34 |
| `size=1|side=minus|ells=89|mod=89|residue=88` | 89 | `[7297, 9967]` | 30 | `[7, 7]` | `687:159:89 -> 910:203:89` | 223 | 44 | `[9, 13] -> [12, 11]` | 44 |
| `size=1|side=minus|ells=29|mod=29|residue=24` | 29 | `[6317, 7187]` | 30 | `[2, 2]` | `620:151:29 -> 693:165:29` | 73 | 14 | `[6, 14] -> [1, 20]` | 56 |
| `size=1|side=plus|ells=79|mod=79|residue=39` | 79 | `[7307, 8887]` | 20 | `[2, 7]` | `663:147:79 -> 847:200:79` | 184 | 53 | `[0, 24] -> [18, 3]` | 60 |
| `size=1|side=plus|ells=103|mod=103|residue=64` | 103 | `[8819, 9437]` | 6 | `[2, 2]` | `881:220:103 -> 752:143:103` | -129 | -77 | `[0, 19] -> [23, 9]` | 67 |

## 2. 结构判断

- 固定残基复现不是 fixed-slot 复现；每一对都改变 `b:u:ell` 槽键。
- 固定残基只说明 `P` 落在同一个低模余类；真正需要排斥的是槽位随 `P` 漂移时的 ColumnCRT 兼容链。
- 当前没有获得终端矛盾，仍需全局证明 slot-drift 不能无限复现，或把失败形态登记为明确 PDEC。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_slot_persistence_empty_current_sweep` | `closed_on_current_sweep` | After physical deduplication every fixed-slot packet occurs once in the current selector sweep. |
| `fixed_residue_recurrence_is_slot_drift_current_sweep` | `closed_on_current_sweep` | Every recurrent fixed-residue packet changes its slot key, so recurrence is residue-fixed but slot-moving. |
| `slot_drift_columncrt_exclusion_open` | `open` | A global proof must exclude the slot-drift family by ColumnCRT/PDEC or transfer it to SAE/Rankin. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedSlotPersistenceEmpty` | `true` | `false` | 当前扫描内没有同一 fixed-slot packet 的物理复现。 | finite evidence only |
| `FixedResidueRecurrenceIsSlotDrift` | `true` | `false` | 12 个固定残基复现包全部换槽，不能作为固定槽图样处理。 | finite evidence only |
| `SlotDriftColumnCRTExcluded` | `false` | `false` | 仍需证明槽漂移族不能全局持久，或登记明确 ColumnCRT/PDEC。 | FixedResidueSlotDriftColumnCRT |
| `MovingResidueShapeSAEBounded` | `false` | `false` | 移动残基 shape 仍需 SAE/Rankin 全局界。 | MovingResidueShapeSAE/Rankin |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步仍是路由压缩，不关闭全局行/列命题。 | FixedResidueSlotDriftColumnCRTOrMovingResidueShapeSAE |

## 5. 下一步

- 主攻：`FixedResidueSlotDriftColumnCRTOrMovingResidueShapeSAE`。
- 对 12 个固定残基换槽对建立 ColumnCRT 相位宽度上界。
- 并行保留 37 个移动残基 shape 的 SAE/Rankin 汇总账本。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_residue_slot_drift_router.py` | `03d51182dd60dc18b457036c5c8a30854bf7549a29e396ddec68113659e8a0c3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json` | `d1e5ac2f12b542edc86559cbbb8b75f862f1ee02df351a024bc302a4af01427b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json` | `bde88833f32da0c028cd0ed8d8a55701e2b0289d20485eac5ced6bd5befb197b` |
