# Prime Matrix square-phase low-alpha z=61 positive lift carry to signed-sum bridge

**状态：** `z61_positive_lift_carry_layer_reduced_to_five_term_signed_sum_residue_gate_open`

positive-lift/MissingLift 链上的 carry=6 目标纤维与已有五项 signed-sum 区间同余门是同一对象：唯一目标词都是 `--++-:26951`，对应 `S=373055`、`S mod 2627=21`。因此当前剩余从 `CarryLayerTargetFiberGlobalBoundOrMissingLiftPDEC` 正式压到 `FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC`。

```text
selected_carry=6
selected_sign_word=--++-
selected_residue=26951
selected_signed_sum=373055
selected_sum_mod_2627=21
positive_lift_carry_to_signed_sum_bridge_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. 对齐摘要

| M | coefficients | carry | sign | root r | S | S mod 2627 | target words |
| ---: | --- | ---: | --- | ---: | ---: | ---: | --- |
| 57684 | `[14421, 19228, 36708, 382536, 12540]` | 6 | `--++-` | 26951 | 373055 | 21 | `['--++-:26951']` |

## 2. 同一性检查

| check | value |
| --- | --- |
| carry values | `[-9, -8, -7, -6, 5, 6, 7, 8]` |
| selected layer sign count | 7 |
| positive-lift target words | `['--++-:26951']` |
| signed-sum target words | `['--++-:26951']` |
| selected layer q4 hits | 1 |
| selected layer q2 hits | 1 |
| selected layer combined hits | 1 |

## 3. 证明边界

- 已闭合：当前 positive-lift carry 纤维与五项 signed-sum 区间同余门严格接桥。
- 未闭合：五项 signed-sum 区间同余纤维的全局界，或 SumResidue/MissingLift-PDEC 排斥。
- 下一目标：`FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json` | `1bc52831b0aacaceb4e4e3979b91b5fe0563a7b62361d08d6b3ebf166befeb48` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json` | `000bb6e26dec4b78c4215118876df470f40659f120db560c9bee5cf6a80fd0c7` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_to_signed_sum_bridge_router.py` | `69bafad68d9203d99355ea4b61f3a92b030b4530f12020b9b26373a0d3cebe9a` |
