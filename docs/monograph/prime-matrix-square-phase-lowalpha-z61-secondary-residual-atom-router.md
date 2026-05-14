# Prime Matrix square-phase low-alpha z=61 次级残量原子路由

**状态：** `z61_secondary_residual_reduced_to_nine_depth_atoms_open`

主星形之后的两个残量 bucket 已压成有限残量原子：`mid<=4` 由 2 个深度格原子覆盖，`unbalanced<=8` 由 7 个深度格原子覆盖。因此下一步可逐原子证明相位不变量；若这些原子支撑无法强制存在，则输出 Atom-PDEC。

```text
secondary_residual_atom_support_materialized=true
sample_selected_atoms_cover_all_residuals=true
residual_bucket_count=2
selected_atom_count=9
residual_atom_phase_invariant_proved=false
atom_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 残量 bucket 原子覆盖

| bucket | residual need | selected atoms | selected credit | surplus | candidate atoms |
| --- | ---: | ---: | ---: | ---: | ---: |
| `mid<=4` | 0.042281 | 2 | 0.045293 | 0.003012 | 5 |
| `unbalanced<=8` | 0.037200 | 7 | 0.038509 | 0.001310 | 9 |

## 2. 选中残量原子

| bucket | pair | omega | shell | signs | credit/residual | bucket share | cumulative |
| --- | --- | ---: | --- | --- | ---: | ---: | ---: |
| `mid<=4` | `200003->36739` | 3 | `(2D,4D]` | `--++` | 0.548893 | 0.023208 | 0.023208 |
| `mid<=4` | `200003->36739` | 4 | `(D,2D]` | `--++` | 0.522352 | 0.022085 | 0.045293 |
| `unbalanced<=8` | `36739->200003` | 3 | `(2D,4D]` | `-++-` | 0.308923 | 0.011492 | 0.011492 |
| `unbalanced<=8` | `36739->200003` | 5 | `(4D,8D]` | `-+--` | 0.234743 | 0.008732 | 0.020224 |
| `unbalanced<=8` | `200003->36739` | 5 | `(2D,4D]` | `+-++` | 0.195073 | 0.007257 | 0.027481 |
| `unbalanced<=8` | `200003->36739` | 3 | `(8D,16D]` | `--++` | 0.087641 | 0.003260 | 0.030741 |
| `unbalanced<=8` | `200003->36739` | 4 | `(8D,16D]` | `--++` | 0.080751 | 0.003004 | 0.033745 |
| `unbalanced<=8` | `200003->10007` | 4 | `(8D,16D]` | `--++` | 0.064115 | 0.002385 | 0.036130 |
| `unbalanced<=8` | `200003->10007` | 3 | `(8D,16D]` | `--++` | 0.063962 | 0.002379 | 0.038509 |

## 3. 证明边界

- 已闭合：两个残量 bucket 的样本覆盖可由 9 个显式深度格原子承担。
- 未闭合：需要证明这些原子的相位/支撑不变量，或登记 Atom-PDEC。
- 下一目标：`ResidualAtomPhaseInvariantForMidUnbalancedOrAtomPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-principal-star-residual-router.json` | `3a969b773dd2ef0f972e6d2a2ada55824c255fc1c06044360394add4c67f35a0` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json` | `130434e1af6983603b965fc0185055ecd897f538e76e9e59d2d0e024d8955dc9` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_secondary_residual_atom_router.py` | `5d35c0d782dd8c17076199c47ff300ab33c22d7c827fe768166fe1c3c8e21bbc` |
