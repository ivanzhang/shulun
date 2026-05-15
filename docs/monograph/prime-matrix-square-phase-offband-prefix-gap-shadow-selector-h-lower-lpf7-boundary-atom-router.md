# Prime Matrix square-phase off-band prefix gap shadow selector H lower lpf7 boundary atom router

**状态：** `small_factor_loss_ladder_reduced_to_lpf7_main_layer_plus_boundary_atom_open`

本步把小因子损耗阶梯压成 `lpf(m)<=7` 主层加唯一边界补项。当前有限重放中，`lpf<=7` 只在 `P=2467, minus, rho=7` 一个贴边行不足；该行需要 28 个合数损耗，`lpf<=7` 支付 20 个，缺口 8 个，而 `11,13,17,23,43` 补项精确支付 8 个，最终余量仍为 0。这不是全局证明；严格闭合还需证明 lpf<=7 主层全局下界并排斥边界补项持久复现。

```text
max_p=10000
p0=2001
selected_hit_count_at_p0=462
lpf7_failure_count_at_p0=1
lpf7_failure_p_values_sample=[2467]
lpf43_failure_count_at_p0=0
boundary_supplement_exact_payment=true
row_column_unconditional_closed=false
```

## 1. 唯一边界原子

| p | side | rho | Bcrit | Good | cap | required loss | actual loss | lpf<=7 pay | deficit | supplement | loss surplus |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2467 | `minus` | 7 | 7 | 6 | 34 | 28 | 28 | 20 | 8 | 8 | 0 |

补项直方图：

```json
{"11": 2, "13": 1, "17": 2, "23": 2, "43": 1}
```

## 2. 结构判断

- 当前高段主层几乎完全由 `3,5,7` 三个小模支付。
- 唯一不足处是贴边行，且补项没有余量；这正是需要排斥持久复现的边界原子。
- 下一步不能把 `43` 当固定全局常数，而应证明 `lpf<=7` 主层的自适应 CRT 覆盖，并把边界补项作为 PDEC/SAE 守门项。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_lpf7_main_layer_all_but_one` | `closed_on_current_sweep` | On the current P>=2001 sweep, lpf(m)<=7 pays the required composite-loss floor for every selector row except the single boundary atom P=2467, minus, rho=7. |
| `boundary_supplement_exact_payment` | `closed_on_current_sweep` | For the boundary atom, the lpf 11,13,17,23,43 supplement contributes exactly eight extra composite losses and closes the floor with zero surplus. |
| `global_lpf7_main_plus_boundary_nonpersistence` | `open` | A global proof must establish the lpf<=7 main loss floor away from boundary atoms and prove boundary supplements cannot persist without PDEC/SAE. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CurrentLPF7MainLayerIsolated` | `true` | `false` | 有限重放中 lpf<=7 只剩一个边界原子。 | finite evidence only |
| `CurrentBoundarySupplementExact` | `true` | `false` | 唯一边界原子的 11..43 补项刚好补齐 8 个缺口。 | finite boundary atom |
| `GlobalLPF7MainFloorProved` | `false` | `false` | 仍需全局证明 lpf<=7 主层损耗下界。 | LPF7MainLossFloorPlusBoundarySupplementOrBoundaryAtomPDEC |
| `BoundaryAtomPDECExcluded` | `false` | `false` | 仍需证明类似贴边补项不能无限复现，或登记并排斥为 PDEC/SAE。 | LPF7MainLossFloorPlusBoundarySupplementOrBoundaryAtomPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把小因子阶梯压成主层加唯一边界原子。 | LPF7MainLossFloorPlusBoundarySupplementOrBoundaryAtomPDEC |

## 5. 下一步

- 主攻：`LPF7MainLossFloorPlusBoundarySupplementOrBoundaryAtomPDEC`。
- 具体目标：证明 `lpf<=7` 主层小模 CRT 覆盖下界；若存在贴边补项复现，则登记为 BoundaryAtom-PDEC/SAE 并排斥。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_boundary_atom_router.py` | `849e55c90717bdb0ea30b1ca2a4ab11399aa9ce12fa0f33585ae9ac782392538` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-ledger.json` | `ddaceee541d8f99a44cc1cebe474ff6daf11e13d8587f84295a64cdab68af3cd` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-ledger.json` | `2dd930d9965259e874fc0c98a8de210db35bc3cd250a406db3c26859933807c5` |
