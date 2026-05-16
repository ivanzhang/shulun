# Prime Matrix square-phase off-band prefix gap shadow selector H lower fixed-residue transport-cell router

**状态：** `fixed_residue_slot_drift_reduced_to_transport_cells_open`

本步把 12 个固定残基换槽复现对压成 transport cell。固定残基给出两个严格整数条件：`P2-P1=k*ell` 且 `(b2+u2)-(b1+u1)=a*ell`。当前扫描中 12 个 transport cell 全部互异，没有 exact phase translate；所有相位边界缺陷的绝对值都小于对应 `ell`。这说明当前复现不是稳定同相位复现，而是带小边界缺陷的槽漂移；全局仍需排斥 transport cell 持久复现，或把它送入 SAE/Rankin。

```text
transport_cell_count=12
unique_transport_cell_count=12
transport_cell_recurrence_count=0
all_slot_sum_lifts_integral=true
all_residue_steps_sum_zero=true
exact_phase_translate_count=0
all_edge_defects_strictly_below_ell=true
max_abs_edge_defect=30
row_column_unconditional_closed=false
```

## 1. transport cell

```text
P2-P1 = p_lift * ell
(b2+u2)-(b1+u1) = slot_sum_lift * ell
b_step + u_step == 0 mod ell
phase_edge_2 = phase_edge_1 + (P2-P1) + edge_defect
```

## 2. transport cell 明细

| ell | residue | side | p values | p lift | sum lift | b/u step | edge defect | active edges | exact translate |
| ---: | ---: | --- | --- | ---: | ---: | --- | --- | --- | ---: |
| 43 | 16 | `minus` | `[2467, 2897]` | 10 | 1 | `36/7` | `1/1` | `['lo_diag'] / ['hi_diag']` | `false` |
| 43 | 20 | `plus` | `[2557, 3847]` | 30 | 2 | `35/8` | `-14/-7` | `['lo_diag', 'lo_div_u'] / ['hi_diag']` | `false` |
| 53 | 45 | `minus` | `[2377, 5557]` | 60 | 9 | `1/52` | `15/-1` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 43 | 37 | `minus` | `[2617, 6917]` | 100 | 14 | `3/40` | `15/-5` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 53 | 25 | `minus` | `[2887, 7127]` | 80 | 8 | `36/17` | `12/16` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 53 | 31 | `minus` | `[3847, 5437]` | 30 | 4 | `9/44` | `9/7` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 37 | 14 | `minus` | `[3307, 5527]` | 60 | 6 | `0/0` | `-10/-8` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 59 | 42 | `minus` | `[5647, 7417]` | 30 | 3 | `30/29` | `30/28` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 89 | 88 | `minus` | `[7297, 9967]` | 30 | 3 | `45/44` | `-3/-2` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 29 | 24 | `minus` | `[6317, 7187]` | 30 | 3 | `15/14` | `5/6` | `['lo_diag'] / ['hi_diag', 'hi_div_u']` | `false` |
| 79 | 39 | `plus` | `[7307, 8887]` | 20 | 3 | `26/53` | `-18/-21` | `['lo_diag', 'lo_div_u'] / ['hi_diag']` | `false` |
| 103 | 64 | `plus` | `[8819, 9437]` | 6 | -2 | `77/26` | `-23/-10` | `['lo_diag', 'lo_div_u'] / ['hi_diag']` | `false` |

## 3. 结构判断

- 固定残基复现的核心不是固定槽，而是 `P` lift 与槽和 lift 的同步。
- 当前 12 个 cell 没有重复，也没有零边界缺陷的 exact phase translate。
- 若全局出现持久 cell，必须同时固定 lift、槽残差步长和边界缺陷；这就是下一步 ColumnCRT/PDEC 的精确输入。

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_residue_transport_identity` | `closed` | For one-slot fixed-residue recurrence, P2-P1 and (b2+u2)-(b1+u1) are both integral ell-lifts. |
| `current_sweep_transport_cells_unique` | `closed_on_current_sweep` | The current fixed-residue slot-drift recurrences have distinct transport-cell signatures and no exact phase translate. |
| `transport_cell_persistence_exclusion_open` | `open` | A global proof must exclude persistent transport cells by ColumnCRT/PDEC or route nonpersistent cells to SAE/Rankin. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedResidueTransportIdentityClosed` | `true` | `true` | 固定残基复现严格推出 `P` 与 `b+u` 的两个 `ell`-lift 条件。 | closed |
| `ActiveEdgeModeIntersects` | `true` | `false` | 当前 12 对的左右槽共享相位边界主导公式，可压成同类 transport cell。 | finite evidence only |
| `ExactPhaseTranslateAbsent` | `true` | `false` | 当前没有边界缺陷为零的同相位平移复现。 | finite evidence only |
| `TransportCellPersistenceExcluded` | `false` | `false` | 仍需证明同一 transport cell 不能全局持久复现。 | TransportCellPDEC/ColumnCRT |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只压缩固定残基槽漂移，不关闭全局命题。 | FixedResidueTransportCellPDECOrMovingResidueShapeSAE |

## 6. 下一步

- 主攻：`FixedResidueTransportCellPDECOrMovingResidueShapeSAE`。
- 固定残基分支：排斥同一 transport cell 的全局持久复现。
- 移动残基分支：继续建立 SAE/Rankin 可求和账本。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_residue_transport_cell_router.py` | `186617d305f412d177c448ef8bc96e77a8dd6df0534d365e44a81000bcbb33c5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json` | `bde88833f32da0c028cd0ed8d8a55701e2b0289d20485eac5ced6bd5befb197b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json` | `7a6af4c73819b3e86322f0b0e40032dc0e98a3f114eab5b163284c85e2b6f23b` |
