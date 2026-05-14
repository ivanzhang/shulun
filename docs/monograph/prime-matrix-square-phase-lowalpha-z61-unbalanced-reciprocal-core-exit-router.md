# Prime Matrix square-phase low-alpha z=61 unbalanced 互反核心出口

**状态：** `z61_unbalanced_two_source_reduced_to_reciprocal_core_plus_single_exit_open`

`unbalanced<=8` 的两来源残量已压成互反核心加单出口。`36739->200003` 与 `200003->36739` 的互反核心几乎覆盖全部需求；剩余缺口只需一个出口 pair，例如 `200003->10007`，即可补齐。下一步只需证明互反核心加单出口的不变量，或登记 Exit-PDEC。

```text
unbalanced_residual_needed_ratio=0.037200
reciprocal_core_credit_ratio=0.034188
deficit_after_reciprocal_core_ratio=0.003011
selected_exit_pair=200003->10007
selected_exit_credit_ratio=0.005191
sample_core_plus_exit_covers_unbalanced_residual=true
reciprocal_core_plus_exit_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 互反核心

| component | credit ratio |
| --- | ---: |
| `36739->200003` | 0.020224 |
| `200003->36739` | 0.013964 |
| reciprocal core total | 0.034188 |
| core deficit | 0.003011 |

## 2. 出口候选

| pair | credit | covers deficit | surplus after core |
| --- | ---: | --- | ---: |
| `200003->10007` | 0.005191 | true | 0.002179 |
| `36739->10007` | 0.004110 | true | 0.001098 |
| `36739->83561` | 0.002752 | false | -0.000259 |

## 3. 证明边界

- 已闭合：unbalanced 两来源预算压成互反核心加单出口的验收合同。
- 未闭合：证明互反核心与出口 pair 的下界，或登记 Exit-PDEC。
- 下一目标：`UnbalancedReciprocalCorePlusExitInvariantOrExitPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-source-budget-router.json` | `6edaba0b2526fda438f889227b5d41c7d11090a2f22371d3949be07bc64c1bef` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_unbalanced_reciprocal_core_exit_router.py` | `e5cb9bd84e9bf092fae334ade96679e4ad1ede7c3bb6837bdcbe59e258bdf133` |
