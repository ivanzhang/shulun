# Prime Matrix square-phase low-alpha z=61 positive lift carry-layer bridge

**状态：** `z61_positive_lift_signed_support_reduced_to_carry_layer_target_fiber_open`

MissingLift 的 signed CRT 支撑可进一步按 carry 分层。当前 32 个符号向量只落入 8 个 carry 层，所有目标投影命中都集中在 carry=6；该层虽然有 7 个符号，但目标纤维只有 `--++-:26951` 一个命中。剩余因此变成全局 carry-layer 目标纤维界，或 MissingLift-PDEC。

```text
carry_values=[-9, -8, -7, -6, 5, 6, 7, 8]
selected_carry=6
selected_sign_word=--++-
combined_target_hit_count=1
all_target_hits_are_selected=true
positive_lift_carry_layer_bridge_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. Carry 分层

| M | carry layers | selected carry | selected layer roots | selected layer sign count |
| ---: | --- | ---: | --- | ---: |
| 57684 | `[-9, -8, -7, -6, 5, 6, 7, 8]` | 6 | `[7457, 17071, 20833, 26951, 45913, 52031, 55793]` | 7 |

## 2. 非空目标层

| nonempty layers | q4/q2 hits | combined hits |
| --- | ---: | ---: |
| `[{'carry': 6, 'q4_or_q2_target_hit_count': 1, 'combined_target_hit_count': 1, 'target_hit_words': ['--++-:26951'], 'combined_hit_words': ['--++-:26951']}]` | 1 | 1 |

## 3. 证明边界

- 已闭合：当前 MissingLift signed support 与 carry-layer 目标纤维严格同一对象。
- 未闭合：全局 carry-layer 目标纤维界，或 MissingLift-PDEC 排斥。
- 下一目标：`CarryLayerTargetFiberGlobalBoundOrMissingLiftPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-carry-layer-projection-router.json` | `02ad727819419b59d9967acaff91084c2f0387eb6e6bc96881241e8506ee2ca2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json` | `ddccdcb319311d455f2c03fb85e7b1e55b8e9d401a88f1b72da9dc2f58868897` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_layer_bridge_router.py` | `8798dcf048329939ec78e921fe52b0a7731f222798c0066f4e73a36b18884321` |
