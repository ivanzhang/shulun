# Prime Matrix square-phase low-alpha z=61 positive lift signed projection bridge

**状态：** `z61_positive_lift_projection_gate_reduced_to_signed_crt_support_open`

MissingLift 的 root projection gate 可展开为五维 CRT 符号支撑：`M=4*3*11*19*23` 的 32 个一级根正好对应 32 个符号向量。外部小模投影必须使用最小代表 carry 修正；修正后 q4/q2 以及合并模 `2627` 的目标纤维都只命中 `--++-`，即 `r=26951`。

```text
sign_vector_count=32
source_root_count=32
signed_support_matches_source_roots=true
selected_sign_word=--++-
selected_carry=6
combined_selected_singleton=true
positive_lift_signed_projection_bridge_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. 符号支撑

| M | local moduli | sign vectors | source roots | selected sign | carry | selected r |
| ---: | --- | ---: | ---: | --- | ---: | ---: |
| 57684 | `[4, 3, 11, 19, 23]` | 32 | 32 | `--++-` | 6 | 26951 |

## 2. 单投影目标纤维

| gate | ell | total target fiber | selected singleton | targets |
| --- | ---: | ---: | --- | --- |
| `q4_plain_root_projection` | 37 | 1 | true | `[{'target_residue': 15, 'fiber_size': 1, 'fiber': ['--++-:26951']}, {'target_residue': 16, 'fiber_size': 0, 'fiber': []}]` |
| `q2_shifted_root_projection` | 71 | 1 | true | `[{'target_residue': 42, 'fiber_size': 1, 'fiber': ['--++-:26951']}, {'target_residue': 50, 'fiber_size': 0, 'fiber': []}]` |

## 3. 合并投影

| classes | nonempty fibers | total fiber | singleton |
| --- | --- | ---: | --- |
| `[681, 1754, 1533, 2606]` | `[{'target_class': 681, 'fiber': ['--++-:26951'], 'fiber_size': 1}]` | 1 | true |

## 4. 证明边界

- 已闭合：当前 MissingLift root projection gate 与带 carry 的 signed CRT 支撑严格同一对象。
- 未闭合：全局 signed CRT carry 支撑界，或 MissingLift-PDEC 排斥。
- 下一目标：`SignedCRTSupportCarryBoundOrMissingLiftPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json` | `7038c8bfdfd00396f9e643e47812ce9d4d38279bc136faed20a5d1415f6f9525` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json` | `6f3e6110974e79d39e0a67c305741d1d06b4b21d1c8a1a4910ebaab92e52f9df` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_signed_projection_bridge_router.py` | `79a705cef6bc47f1b8311b6ad7bb26a6fcd29fa09f9b6f328d7bcdfcf010bf87` |
