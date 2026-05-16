# Prime Matrix square-phase off-band prefix gap shadow selector H lower gap repair corridor router

**状态：** `gap_repair_corridor_closed_current_sweep_global_bound_open`

本步把 immediate gap repair 转成短 P 走廊不等式：当前三次填充均满足 `fill_p-generator_p <= 3*gap_ell`，最大归一化延迟为 2.580645，最小 `3*gap_ell` 余量为 13。全局剩余是证明短走廊填充界，或把走廊失效登记并排斥为 Corridor-PDEC/SAE。

```text
corridor_row_count=3
all_repairs_within_3_gap_ell_current_sweep=true
all_repairs_within_3_min_local_ell_current_sweep=true
all_repairs_within_2_gap_ell_current_sweep=false
max_ceil_delay_over_gap_ell=3
max_p_delay_over_gap_ell=2.580645161290
min_corridor_defect_against_3_gap_ell=13
row_column_unconditional_closed=false
```

## 1. 短走廊行

| gap ell | generator ell | P delay | delay/gap | ceil | within 3*gap | 3*gap defect | pair key |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | 47 | 74 | 1.720930 | 2 | `true` | 55 | `dir=upper|gen=47|gap=43|fill=43|sides=plus->minus|dp=74|db=21|du=8|dr=-12` |
| 31 | 29 | 80 | 2.580645 | 3 | `true` | 13 | `dir=lower|gen=29|gap=31|fill=31|sides=minus->plus|dp=80|db=-13|du=-7|dr=-11` |
| 59 | 61 | 70 | 1.186441 | 2 | `true` | 107 | `dir=upper|gen=61|gap=59|fill=59|sides=minus->minus|dp=70|db=58|du=23|dr=-3` |

## 2. 结构结论

- 当前 immediate repair 不只是激活序列相邻，也落在 `3*gap_ell` 的短 P 走廊内。
- `2*gap_ell` 走廊失败只发生在 `gap_ell=31`，因此 `3*gap_ell` 是当前最小整数倍统一包络。
- 全局闭合仍需证明这个短走廊包络，或证明违反包络会产生 Corridor-PDEC/SAE。

## 3. 下一步

- 主攻：`ShortGapRepairCorridorBoundOrCorridorPDECExclusion`。
- 将 `3*gap_ell` 包络与端点 CRT 相位宽度、slot 位移和 residue 位移对齐，寻找可排斥的走廊失效原子。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_gap_repair_corridor_router.py` | `28b92ece6ec79ba3b38eae4b1cf0a6e8103d4753da2d80f8fdc91a6c69fe2cfa` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json` | `8af116227ee290b0341711947c640d3bceb05b32be2ca833c322aa61900a69bf` |
