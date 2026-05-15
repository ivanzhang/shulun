# Prime Matrix square-phase low-alpha z=61 nearest margin collision

**状态：** `z61_margin_pdec_reduced_to_nearest_offset55_collision_open`

Margin-PDEC 的最近塌缩并非分散随机：最小余量 55 的所有原子都是ResidueMarginCollapse，且有同一个有符号偏移 `candidate-target=-55`。三条最近原子分别在 step 1、2、3 出现。因此下一硬点可从任意 margin collapse 收窄为固定 offset-55 同余碰撞族，或登记 Offset-PDEC。

```text
minimum_margin=55
nearest_margin_collision_group_count=1
closest_offsets=[-55]
offset55_collision_pattern_closed_for_formal_unit=true
offset55_margin_collision_excluded=false
row_column_unconditional_closed=false
```

## 1. 最近 offset-55 原子

| step | branch sign | selected | candidate | sum mod | target | offset | margin |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `+` | true | `++--` | 972 | 1027 | -55 | 55 |
| 2 | `+` | true | `+--` | 1042 | 1097 | -55 | 55 |
| 3 | `+` | false | `--` | 2383 | 2438 | -55 | 55 |

## 2. 塌缩群组

| type | margin | offset | count | steps |
| --- | ---: | ---: | ---: | --- |
| `ResidueMarginCollapse` | 55 | -55 | 3 | `[1, 2, 3]` |
| `ResidueMarginCollapse` | 162 | -162 | 2 | `[1, 2]` |
| `ResidueMarginCollapse` | 224 | -224 | 2 | `[1, 2]` |
| `ResidueMarginCollapse` | 279 | -279 | 2 | `[1, 2]` |
| `ResidueMarginCollapse` | 364 | 364 | 5 | `[1, 2, 3, 4, 5]` |
| `ResidueMarginCollapse` | 403 | -403 | 2 | `[1, 2]` |
| `IntervalMarginCollapse` | 7723 |  | 1 | `[4]` |
| `IntervalMarginCollapse` | 645743 |  | 1 | `[1]` |

## 3. 自足小引理

若最小余量塌缩必须先发生，则当前 formal unit 中第一个可能塌缩的同余事件满足

```text
candidate_sum_mod = target - 55 (mod 2627).
```

所以全局排斥可优先针对 offset `-55` 的持久碰撞族；若该族出现，它就是比一般 Margin-PDEC 更窄的 Offset-PDEC。

## 4. 证明边界

- 已闭合：当前 z=61 formal unit 的最近塌缩全部归为同一 offset `-55` 同余碰撞。
- 未闭合：全局排斥 offset-55 碰撞族，或证明更宽 margin 塌缩也不能持久。
- 下一目标：`Offset55MarginCollisionExclusionOrOffsetPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json` | `a9b90b319ca2f4c0d0c5ebce61300e3fc565d402d702af55dd042d47939d17ca` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_nearest_margin_collision_router.py` | `265e6c50ec28863a65d152dc8663dccde6df24c533caafa3eac8fb159574cb98` |
