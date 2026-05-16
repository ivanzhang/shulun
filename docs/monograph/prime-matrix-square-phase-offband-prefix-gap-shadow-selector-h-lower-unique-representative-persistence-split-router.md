# Prime Matrix square-phase off-band prefix gap shadow selector H lower unique-representative persistence split router

**状态：** `unique_representative_persistence_split_materialized_open`

本步把唯一代表正规形的持久性来源拆成三层：physical 事件、fixed-residue packet、fixed-slot packet。当前重放 raw 记录 462 条，物理去重后 324 条，删除模板重复 138 条；正规形 shape 为 80 个，固定残基包为 312 个。跨不同 P 复现的固定残基包 12 个，残基或槽漂移的 moving shape 37 个。它们分别进入 ColumnCRT/PDEC 与 SAE/Rankin，全局无条件闭合仍未完成。

```text
max_p=10000
p0=2001
raw_record_count=462
physical_record_count=324
duplicate_template_count=138
normal_shape_count=80
residue_packet_count=312
recurrent_shape_count=37
recurrent_fixed_residue_packet_count_distinct_p=12
moving_residue_shape_count=37
row_column_unconditional_closed=false
```

## 1. 去重与拆分口径

```text
physical_key = (P, side, rho, normal_shape, CRT residue, CRT modulus, slot_keys)
residue_packet = (normal_shape, CRT modulus, CRT residue)
slot_packet = (normal_shape, CRT modulus, CRT residue, slot_keys)
```

物理去重只合并模板索引重复，不合并不同 `rho`、不同槽或不同残基的真实事件。

## 2. 高频 shape 包

| shape | physical | distinct P | residues | slot packets | p range | min margin | min CRT-width |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| `size=1|side=minus|ells=71` | 22 | 22 | 22 | 22 | `4177..9257` | 25 | 14 |
| `size=1|side=minus|ells=53` | 17 | 17 | 14 | 17 | `2377..7127` | 17 | 9 |
| `size=1|side=minus|ells=43` | 16 | 16 | 14 | 16 | `2137..9397` | 0 | 1 |
| `size=1|side=minus|ells=61` | 13 | 13 | 13 | 13 | `3187..8237` | 15 | 19 |
| `size=1|side=minus|ells=89` | 13 | 13 | 12 | 13 | `7297..9967` | 26 | 49 |
| `size=1|side=plus|ells=79` | 13 | 13 | 12 | 13 | `5639..8887` | 36 | 20 |
| `size=1|side=minus|ells=59` | 12 | 12 | 11 | 12 | `3257..7877` | 17 | 21 |
| `size=1|side=minus|ells=101` | 12 | 12 | 12 | 12 | `8387..9857` | 44 | 15 |
| `size=1|side=minus|ells=97` | 11 | 11 | 11 | 11 | `7537..8737` | 27 | 32 |
| `size=1|side=minus|ells=67` | 10 | 10 | 10 | 10 | `3967..9127` | 23 | 18 |
| `size=1|side=minus|ells=79` | 10 | 10 | 10 | 10 | `5197..8887` | 36 | 32 |
| `size=1|side=minus|ells=83` | 10 | 10 | 10 | 10 | `5927..9787` | 37 | 30 |
| `size=1|side=minus|ells=37` | 9 | 9 | 8 | 9 | `2027..6967` | 13 | 1 |
| `size=1|side=minus|ells=73` | 9 | 9 | 9 | 9 | `4337..8597` | 29 | 36 |
| `size=1|side=plus|ells=61` | 8 | 8 | 8 | 8 | `3257..5227` | 12 | 5 |
| `size=1|side=minus|ells=41` | 8 | 8 | 8 | 8 | `2087..8837` | 17 | 2 |
| `size=1|side=minus|ells=47` | 7 | 7 | 7 | 7 | `2357..6857` | 12 | 9 |
| `size=1|side=plus|ells=47` | 6 | 6 | 6 | 6 | `2063..9473` | 12 | 11 |

## 3. 固定残基复现包

| residue packet | physical | distinct P | p values | min margin | min CRT-width |
| --- | ---: | ---: | --- | ---: | ---: |
| `size=1|side=minus|ells=43|mod=43|residue=16` | 2 | 2 | `[2467, 2897]` | 0 | 21 |
| `size=1|side=plus|ells=43|mod=43|residue=20` | 2 | 2 | `[2557, 3847]` | 16 | 12 |
| `size=1|side=minus|ells=53|mod=53|residue=45` | 2 | 2 | `[2377, 5557]` | 17 | 17 |
| `size=1|side=minus|ells=43|mod=43|residue=37` | 2 | 2 | `[2617, 6917]` | 20 | 1 |
| `size=1|side=minus|ells=53|mod=53|residue=25` | 2 | 2 | `[2887, 7127]` | 24 | 26 |
| `size=1|side=minus|ells=53|mod=53|residue=31` | 2 | 2 | `[3847, 5437]` | 25 | 29 |
| `size=1|side=minus|ells=37|mod=37|residue=14` | 2 | 2 | `[3307, 5527]` | 26 | 10 |
| `size=1|side=minus|ells=59|mod=59|residue=42` | 2 | 2 | `[5647, 7417]` | 34 | 23 |
| `size=1|side=minus|ells=89|mod=89|residue=88` | 2 | 2 | `[7297, 9967]` | 44 | 65 |
| `size=1|side=minus|ells=29|mod=29|residue=24` | 2 | 2 | `[6317, 7187]` | 56 | 7 |
| `size=1|side=plus|ells=79|mod=79|residue=39` | 2 | 2 | `[7307, 8887]` | 60 | 54 |
| `size=1|side=plus|ells=103|mod=103|residue=64` | 2 | 2 | `[8819, 9437]` | 67 | 70 |

## 4. 移动残基 shape

| shape | physical | distinct P | residues | slot packets | p range | first residues |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `size=1|side=minus|ells=71` | 22 | 22 | 22 | 22 | `4177..9257` | `[3, 9, 10, 12, 18, 21, 22, 26, 27, 28, 34, 35, 36, 37, 39, 40, 44, 46, 53, 59]` |
| `size=1|side=minus|ells=53` | 17 | 17 | 14 | 17 | `2377..7127` | `[3, 4, 6, 8, 10, 14, 18, 25, 31, 35, 45, 46, 47, 51]` |
| `size=1|side=minus|ells=43` | 16 | 16 | 14 | 16 | `2137..9397` | `[1, 3, 9, 11, 12, 16, 19, 20, 23, 25, 26, 30, 37, 41]` |
| `size=1|side=minus|ells=61` | 13 | 13 | 13 | 13 | `3187..8237` | `[2, 3, 6, 9, 15, 17, 27, 34, 42, 50, 52, 54, 58]` |
| `size=1|side=minus|ells=89` | 13 | 13 | 12 | 13 | `7297..9967` | `[8, 9, 10, 18, 24, 31, 32, 33, 48, 73, 81, 88]` |
| `size=1|side=plus|ells=79` | 13 | 13 | 12 | 13 | `5639..8887` | `[6, 23, 24, 26, 29, 30, 38, 39, 42, 44, 49, 70]` |
| `size=1|side=minus|ells=59` | 12 | 12 | 11 | 12 | `3257..7877` | `[12, 13, 18, 30, 34, 35, 42, 43, 45, 46, 53]` |
| `size=1|side=minus|ells=101` | 12 | 12 | 12 | 12 | `8387..9857` | `[4, 18, 20, 43, 44, 47, 60, 61, 62, 67, 92, 93]` |
| `size=1|side=minus|ells=97` | 11 | 11 | 11 | 11 | `7537..8737` | `[7, 8, 10, 11, 28, 35, 54, 68, 72, 78, 91]` |
| `size=1|side=minus|ells=67` | 10 | 10 | 10 | 10 | `3967..9127` | `[13, 14, 15, 29, 37, 42, 45, 47, 60, 64]` |
| `size=1|side=minus|ells=79` | 10 | 10 | 10 | 10 | `5197..8887` | `[12, 15, 25, 26, 31, 35, 39, 45, 62, 67]` |
| `size=1|side=minus|ells=83` | 10 | 10 | 10 | 10 | `5927..9787` | `[16, 17, 26, 34, 52, 55, 61, 69, 76, 80]` |
| `size=1|side=minus|ells=37` | 9 | 9 | 8 | 9 | `2027..6967` | `[11, 14, 16, 17, 28, 29, 32, 35]` |
| `size=1|side=minus|ells=73` | 9 | 9 | 9 | 9 | `4337..8597` | `[1, 4, 6, 22, 27, 30, 45, 48, 56]` |
| `size=1|side=plus|ells=61` | 8 | 8 | 8 | 8 | `3257..5227` | `[16, 20, 24, 40, 42, 46, 53, 55]` |
| `size=1|side=minus|ells=41` | 8 | 8 | 8 | 8 | `2087..8837` | `[1, 4, 17, 22, 31, 32, 33, 37]` |
| `size=1|side=minus|ells=47` | 7 | 7 | 7 | 7 | `2357..6857` | `[7, 16, 25, 26, 32, 33, 42]` |
| `size=1|side=plus|ells=47` | 6 | 6 | 6 | 6 | `2063..9473` | `[19, 26, 37, 40, 42, 44]` |

## 5. 最紧物理事件

| p | side | rho | templates | margin | shape | residue | slots |
| ---: | --- | ---: | --- | ---: | --- | ---: | --- |
| 2467 | `minus` | 7 | `[6]` | 0 | `size=1|side=minus|ells=43` | 16 | `['237:56:43']` |
| 2347 | `plus` | 7 | `[2, 3]` | 12 | `size=1|side=plus|ells=47` | 44 | `['180:33:47']` |
| 5297 | `minus` | 2 | `[0, 5]` | 12 | `size=1|side=minus|ells=47` | 33 | `['470:101:47']` |
| 3767 | `plus` | 2 | `[4]` | 12 | `size=1|side=plus|ells=61` | 46 | `['290:53:61']` |
| 2243 | `plus` | 2 | `[4]` | 12 | `size=2|side=plus|ells=17,19` | 305 | `['128:17:17', '155:25:19']` |
| 2027 | `minus` | 2 | `[5]` | 13 | `size=1|side=minus|ells=37` | 29 | `['185:41:37']` |
| 2063 | `plus` | 2 | `[4]` | 13 | `size=1|side=plus|ells=47` | 42 | `['177:37:47']` |
| 2927 | `minus` | 2 | `[0, 5]` | 13 | `size=2|side=minus|ells=37,43` | 1336 | `['69:3:37', '99:7:43']` |
| 2267 | `minus` | 2 | `[5]` | 14 | `size=2|side=minus|ells=47,31` | 810 | `['102:10:47', '135:18:31']` |
| 5407 | `minus` | 7 | `[6]` | 15 | `size=1|side=minus|ells=29` | 13 | `['483:105:29']` |
| 2687 | `minus` | 2 | `[5]` | 15 | `size=1|side=minus|ells=29` | 19 | `['242:53:29']` |
| 2837 | `minus` | 2 | `[5]` | 15 | `size=1|side=minus|ells=31` | 16 | `['270:63:31']` |
| 4007 | `minus` | 2 | `[5]` | 15 | `size=1|side=minus|ells=61` | 42 | `['338:68:61']` |
| 2207 | `minus` | 2 | `[0, 5]` | 15 | `size=2|side=minus|ells=43,23` | 229 | `['35:1:43', '114:13:23']` |
| 2297 | `minus` | 2 | `[5]` | 15 | `size=2|side=minus|ells=23,43` | 319 | `['77:5:23', '143:20:43']` |
| 2647 | `minus` | 7 | `[6]` | 15 | `size=2|side=minus|ells=37,31` | 353 | `['183:29:37', '205:37:31']` |
| 4567 | `minus` | 7 | `[6]` | 16 | `size=1|side=minus|ells=37` | 16 | `['417:93:37']` |
| 2137 | `minus` | 7 | `[1, 6]` | 16 | `size=1|side=minus|ells=43` | 30 | `['198:45:43']` |

## 6. 结构判断

- 固定残基复现包不是由模板索引重复造成；它们是下一步 `ColumnCRT/PDEC` 的候选输入。
- 同一正规形 shape 若残基或槽漂移，不能当作固定 CRT 图样排斥；它们应转入 `SAE/Rankin` 或全局增长界。
- 当前只是把前沿剩余拆成两个合法出口，没有证明全局无条件闭合。

## 7. 命题行

| name | status | statement |
| --- | --- | --- |
| `physical_deduplication_closed` | `closed` | Template-index multiplicity is quotiented by physical event keys before persistence is counted. |
| `fixed_residue_vs_moving_residue_split_closed` | `closed_on_current_sweep` | Every unique-representative event is assigned to shape, fixed-residue packet, and fixed-slot packet ledgers. |
| `persistent_packet_exclusion_open` | `open` | A global proof must exclude recurrent fixed-residue packets by ColumnCRT/PDEC or bound drifting residue shapes by SAE/Rankin. |

## 8. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PhysicalDeduplicationClosed` | `true` | `true` | 同一物理事件的模板索引重复已合并，不再把重复模板误判为复现。 | closed |
| `FixedResidueMovingResidueSplitMaterialized` | `true` | `false` | 当前重放已拆成固定残基包与移动残基 shape，但仍是有限扫描证据。 | finite evidence only |
| `FixedResiduePacketsExcluded` | `false` | `false` | 12 个固定残基包跨不同 P 复现，需要 ColumnCRT/PDEC 排斥。 | FixedResidueShapePDEC/ColumnCRT |
| `MovingResidueShapesBounded` | `false` | `false` | 37 个 shape 出现残基或槽漂移，需要 SAE/Rankin 或全局增长界。 | MovingResidueShapeSAE/Rankin |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只是持久性路由拆分，不关闭全局行/列命题。 | UniqueRepresentativePersistenceSplitToFixedResiduePDECOrMovingResidueSAE |

## 9. 下一步

- 主攻：`UniqueRepresentativePersistenceSplitToFixedResiduePDECOrMovingResidueSAE`。
- 固定残基包：证明 ColumnCRT/PDEC 上界，或登记明确的固定残基持久缺陷。
- 移动残基 shape：证明 residue drift 的 SAE/Rankin 可求和或增长界。

## 10. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_unique_representative_persistence_split_router.py` | `e52231333293c3b6993dda65d7f1e0d339752660fa8c84ba489efbc1b08ed210` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py` | `235a88162fc76a089f99156ebbc167cec3c3e43c7e00c2e99addcab467b88d09` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json` | `d1e5ac2f12b542edc86559cbbb8b75f862f1ee02df351a024bc302a4af01427b` |
