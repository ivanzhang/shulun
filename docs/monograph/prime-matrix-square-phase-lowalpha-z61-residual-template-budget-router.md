# Prime Matrix square-phase low-alpha z=61 残量模板预算

**状态：** `z61_residual_cells_reduced_to_sign_word_template_budget_open`

7 个残量格原子已按 sign word 模板合并。`mid<=4` 只剩单一 `--++` 模板；`unbalanced<=8` 仍需四个模板合力。因此最终残量证明可集中到 unbalanced 的四模板相位不变量，或登记 Template-PDEC。

```text
fused_cell_atom_count=7
bucket_template_budget_materialized=true
sample_templates_cover_all_residuals=true
bucket_template_obligation_count=5
unbalanced_template_count=4
template_phase_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. bucket 模板覆盖

| bucket | residual need | templates | cover templates | cover credit | surplus |
| --- | ---: | ---: | ---: | ---: | ---: |
| `mid<=4` | 0.042281 | 1 | 1 | 0.045293 | 0.003012 |
| `unbalanced<=8` | 0.037200 | 4 | 4 | 0.038509 | 0.001310 |

## 2. 模板明细

| bucket | sign word | credit | cells | cell list |
| --- | --- | ---: | ---: | --- |
| `mid<=4` | `--++` | 0.045293 | 2 | `omega=3,(2D,4D]:0.023208, omega=4,(D,2D]:0.022085` |
| `unbalanced<=8` | `-++-` | 0.011492 | 1 | `omega=3,(2D,4D]:0.011492` |
| `unbalanced<=8` | `--++` | 0.011029 | 2 | `omega=3,(8D,16D]:0.005640, omega=4,(8D,16D]:0.005389` |
| `unbalanced<=8` | `-+--` | 0.008732 | 1 | `omega=5,(4D,8D]:0.008732` |
| `unbalanced<=8` | `+-++` | 0.007257 | 1 | `omega=5,(2D,4D]:0.007257` |

## 3. 全局模板贡献

| sign word | credit |
| --- | ---: |
| `--++` | 0.056322 |
| `-++-` | 0.011492 |
| `-+--` | 0.008732 |
| `+-++` | 0.007257 |

## 4. 证明边界

- 已闭合：7 个格原子到 sign-word 模板预算的合并账本。
- 剩余：证明 `unbalanced<=8` 四模板相位不变量，或登记 Template-PDEC。
- 下一目标：`UnbalancedFourTemplatePhaseInvariantOrTemplatePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-secondary-residual-cell-fusion-router.json` | `f67145d47b84b98c326dfe7b3031984483ab57306a50d51986459d2cf79d1565` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_residual_template_budget_router.py` | `a8c4545807e01e2d6e586d616c1c9785eba3e51718928992ef19de7acfa2f512` |
