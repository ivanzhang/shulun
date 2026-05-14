# Prime Matrix square-phase low-alpha z=61 奇深度核心与偶高壳补项

**状态：** `z61_core_exit_five_cells_reduced_to_odd_core_even_booster_open`

五个核心出口覆盖格可压成奇深度核心加偶高壳补项。`omega=3,5` 的奇深度核心几乎覆盖全部 residual；剩余缺口由一个 `omega=4,(8D,16D],--++` 偶高壳补项补齐。下一步只需证明该奇偶深度组合的不变量，或登记 Parity-PDEC。

```text
unbalanced_residual_needed_ratio=0.037200
odd_core_credit_ratio=0.033120
deficit_after_odd_core_ratio=0.004079
selected_even_booster_credit_ratio=0.005389
odd_core_plus_booster_credit_ratio=0.038509
odd_core_plus_booster_surplus_ratio=0.001310
sample_odd_core_plus_booster_covers_residual=true
odd_core_even_booster_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 奇深度核心

| omega | shell | signs | credit | pairs |
| ---: | --- | --- | ---: | --- |
| 3 | `(2D,4D]` | `-++-` | 0.011492 | `36739->200003:0.011492` |
| 5 | `(4D,8D]` | `-+--` | 0.008732 | `36739->200003:0.008732` |
| 5 | `(2D,4D]` | `+-++` | 0.007257 | `200003->36739:0.007257` |
| 3 | `(8D,16D]` | `--++` | 0.005640 | `200003->10007:0.002379, 200003->36739:0.003260` |

## 2. 偶高壳补项

| omega | shell | signs | credit | selected | pairs |
| ---: | --- | --- | ---: | --- | --- |
| 4 | `(8D,16D]` | `--++` | 0.005389 | true | `200003->10007:0.002385, 200003->36739:0.003004` |

## 3. 证明边界

- 已闭合：五格核心出口支撑压成奇深度核心加偶高壳补项。
- 未闭合：证明该奇偶深度组合下界，或登记 Parity-PDEC。
- 下一目标：`OddOmegaCorePlusEvenHighShellBoosterInvariantOrParityPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json` | `0912930626796d5c415b381e8bd837ffb4dca6d5380e77c6b816cd3377120336` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_odd_core_even_booster_router.py` | `8fd4ff54d3e0a9c9892ecd33fc55261dc69a6afcf4653d11e963b9dd91e4319a` |
