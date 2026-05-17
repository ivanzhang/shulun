# Prime Matrix cycle-debt K13/K14 survivor rigidity router

**状态：** `k13_k14_survivors_are_tight_hall_crt_island_not_free_replacement`

K=13,14 不是自由的 support replacement。二者都含多个 zero-slack Hall cut，对应 supply set 必须整层进入匹配；任何单行容量损失都会破坏相应阈值。精确最小费用匹配显示，K=13 至少 20 行替换、至少 6 个 immediate-relief 行，K=14 至少 19 行替换、至少 6 个 immediate-relief 行。强制 tight 层的合数槽又给出横向 CRT 阻断模数，均超过本地周期。因此剩余不是普通容量自由度，而是 tight-Hall CRT island 的 PDEC 或 moving-support SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=K13K14SupportReplacementSurvivorPDECOrGlobalSAE
period_p=5680
survivor_shifts=[13, 14]
k13_zero_slack_thresholds=[1, 4, 7, 8]
k14_zero_slack_thresholds=[7, 8, 13, 15]
k13_minimum_replacement_count=20
k14_minimum_replacement_count=19
k13_minimum_immediate_relief_rows=6
k14_minimum_immediate_relief_rows=6
k13_minimum_overstretch_units=61
k14_minimum_overstretch_units=65
all_tight_layers_have_transverse_lcm_exceeding_period=true
survivor_island_has_adjacent_hall_failures=true
next_direct_attack_target=K13K14TightHallCRTIslandPDECOrMovingSupportSAE
```

## 1. tight Hall layers

| K | zero thresholds | min replacements | min immediate rows | min overstretch | same-support prime obstacles |
| ---: | --- | ---: | ---: | ---: | ---: |
| 13 | [1, 4, 7, 8] | 20 | 6 | 61 | 27 |
| 14 | [7, 8, 13, 15] | 19 | 6 | 65 | 28 |

## 2. forced shells

| K | shell | supply | demand | immediate supply | replacement lower bound |
| ---: | --- | ---: | ---: | ---: | ---: |
| 13 | `>=8` | 4 | 4 | 1 | 4 |
| 13 | `7..7` | 1 | 1 | 1 | 1 |
| 13 | `4..6` | 4 | 4 | 2 | 3 |
| 13 | `1..3` | 18 | 18 | 2 | 8 |
| 14 | `>=15` | 1 | 1 | 0 | 1 |
| 14 | `13..14` | 1 | 1 | 0 | 1 |
| 14 | `8..12` | 2 | 2 | 1 | 2 |
| 14 | `7..7` | 1 | 1 | 1 | 1 |

## 3. CRT pressure on tight layers

| K | threshold | slots | unique blockers | transverse blockers | log10 transverse lcm | exceeds period |
| ---: | ---: | ---: | ---: | ---: | ---: | :---: |
| 13 | 1 | 27 | 14 | 14 | 22.281 | true |
| 13 | 4 | 36 | 16 | 16 | 25.522 | true |
| 13 | 7 | 35 | 15 | 15 | 23.149 | true |
| 13 | 8 | 32 | 15 | 15 | 22.509 | true |
| 14 | 7 | 35 | 15 | 15 | 21.720 | true |
| 14 | 8 | 32 | 15 | 15 | 21.494 | true |
| 14 | 13 | 26 | 15 | 15 | 21.961 | true |
| 14 | 15 | 15 | 11 | 11 | 16.731 | true |

## 4. survivor island boundary

```text
left_neighbor_first_defect={'threshold': 1, 'supply_rows': 26, 'demand_rows': 27, 'slack': -1}
right_neighbor_first_defect={'threshold': 6, 'supply_rows': 5, 'demand_rows': 6, 'slack': -1}
adjacent_hall_failure_both_sides=true
```

## 5. 判定

- `K=13,14` 是一个两点 survivor island，不是可平滑移动的 replacement family。
- 每个 zero-slack 层都是精确 Hall cut；层内任一 supply 行的容量损失都会立刻破坏该阈值。
- 即便优化匹配，仍至少需要 `19/20` 个行替换与 `6` 个 immediate-relief 行。
- 强制合数槽的横向 CRT 模数均超过本地周期；若不是 PDEC，就只能作为 moving-support SAE 继续处理。
- 下一主攻点：`K13K14TightHallCRTIslandPDECOrMovingSupportSAE`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json` | `343ddce201b1f69189726670d132f957d7330d2724bb7c40dc9e80a9e8dd82a3` |
