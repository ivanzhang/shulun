# Prime Matrix square-phase low-alpha z=61 次级残量格融合

**状态：** `z61_secondary_residual_nine_pair_atoms_fused_to_seven_cell_atoms_open`

9 个残量 pair 原子中有两组共享同一深度格，因此可融合为 7 个残量格原子。这些格原子保留完整 profile 向量与 sign word；下一步可直接证明 7 个格模板的相位不变量，或登记 Cell-PDEC。

```text
selected_pair_atom_count=9
fused_cell_atom_count=7
sample_fused_cells_cover_all_residuals=true
residual_cell_phase_template_proved=false
cell_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 残量格融合

| bucket | residual need | fused cells | fused credit | surplus |
| --- | ---: | ---: | ---: | ---: |
| `mid<=4` | 0.042281 | 2 | 0.045293 | 0.003012 |
| `unbalanced<=8` | 0.037200 | 5 | 0.038509 | 0.001310 |

## 2. 7 个残量格原子

| bucket | omega | shell | signs | selected credit | pairs | profile vector |
| --- | ---: | --- | --- | ---: | --- | --- |
| `mid<=4` | 3 | `(2D,4D]` | `--++` | 0.023208 | `200003->36739:0.023208` | `10007:-1.749411, 36739:-8.007256, 83561:6.150322, 200003:8.708046` |
| `mid<=4` | 4 | `(D,2D]` | `--++` | 0.022085 | `200003->36739:0.022085` | `10007:-0.315393, 36739:-6.095123, 83561:2.683332, 200003:7.355355` |
| `unbalanced<=8` | 3 | `(2D,4D]` | `-++-` | 0.011492 | `36739->200003:0.011492` | `10007:-2.193242, 36739:2.714492, 83561:6.893740, 200003:-6.796502` |
| `unbalanced<=8` | 5 | `(4D,8D]` | `-+--` | 0.008732 | `36739->200003:0.008732` | `10007:-0.184853, 36739:1.985946, 83561:-1.267369, 200003:-4.021515` |
| `unbalanced<=8` | 5 | `(2D,4D]` | `+-++` | 0.007257 | `200003->36739:0.007257` | `10007:0.226569, 36739:-2.537867, 83561:1.807935, 200003:1.861220` |
| `unbalanced<=8` | 3 | `(8D,16D]` | `--++` | 0.005640 | `200003->36739:0.003260, 200003->10007:0.002379` | `10007:-0.750899, 36739:-1.028881, 83561:3.102292, 200003:3.490612` |
| `unbalanced<=8` | 4 | `(8D,16D]` | `--++` | 0.005389 | `200003->36739:0.003004, 200003->10007:0.002385` | `10007:-1.576550, 36739:-1.985602, 83561:7.257244, 200003:2.455029` |

## 3. sign word 贡献

| sign word | credit ratio |
| --- | ---: |
| `--++` | 0.056322 |
| `-++-` | 0.011492 |
| `-+--` | 0.008732 |
| `+-++` | 0.007257 |

## 4. 证明边界

- 已闭合：9 个 pair 原子融合成 7 个格原子的账本。
- 未闭合：需要证明 7 个格模板的相位不变量，或登记 Cell-PDEC。
- 下一目标：`SevenResidualCellPhaseTemplateInvariantOrCellPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json` | `f37d1d58c9c03c95badb956c102919ebd6a69db811139157393a1123f0a52d1b` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-atom-router.json` | `6bc6aa5518b22968175845b335d1c090746ae7d4d0e59b9fdf1520976828be5a` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_secondary_residual_cell_fusion_router.py` | `99c64cbd2e6aeba600144b9bcf60cce456c171faac449c446c9d1b8ee8177a75` |
