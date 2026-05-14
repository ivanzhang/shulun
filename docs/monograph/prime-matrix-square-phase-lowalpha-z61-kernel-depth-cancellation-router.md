# Prime Matrix square-phase low-alpha z=61 kernel 深度抵消路由

**状态：** `z61_kernel_depth_shell_absolute_budget_open`

一维核余项已进一步分解为 `omega(m)` 与 dyadic shell 深度格。样本中逐格内部偏斜率有时很高，但每个格占 bucket 总质量的比例很小；因此按深度格绝对线性余项求和的 crude budget 已足以推出 `0.221522` 合同。下一步不需要依赖跨深度偶然抵消，而是证明所有命名深度格的绝对预算，若某格长期超预算则直接形成 DepthCell-PDEC。

```text
depth_shell_ledger_materialized=true
kernel_source_ratio_identity_closed=true
independent_omega_cell_contract_sufficient_for_all_buckets=true
independent_shell_cell_contract_sufficient_for_all_buckets=true
same_parity_cross_depth_cancellation_needed=false
depth_shell_absolute_budget_proved=false
row_column_unconditional_closed=false
```

## 1. bucket 总览

| bucket | actual slice | omega crude | shell crude | omega needed credit | shell needed credit |
| --- | ---: | ---: | ---: | ---: | ---: |
| `balanced<=2` | 0.087145 | 0.126958 | 0.177263 | 0.000000 | 0.000000 |
| `mid<=4` | 0.049512 | 0.121293 | 0.182229 | 0.000000 | 0.000000 |
| `unbalanced<=8` | 0.032026 | 0.032026 | 0.204937 | 0.000000 | 0.000000 |
| `far>8` | 0.058366 | 0.101564 | 0.115186 | 0.000000 | 0.000000 |

## 2. 同片跨深度抵消

| bucket | parity | abs | crude depth | net | credit | net ratio | credit ratio |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `balanced<=2` | `mu_plus` | 257.399579 | 27.968495 | 27.968495 | 0.000000 | 0.108658 | 0.000000 |
| `balanced<=2` | `mu_minus` | 213.185295 | 31.776061 | 13.040829 | 18.735232 | 0.061171 | 0.087882 |
| `mid<=4` | `mu_plus` | 210.318752 | 14.546952 | 5.745777 | 8.801176 | 0.027319 | 0.041847 |
| `mid<=4` | `mu_minus` | 194.101962 | 34.506373 | 14.277959 | 20.228414 | 0.073559 | 0.104215 |
| `unbalanced<=8` | `mu_plus` | 180.602472 | 0.544680 | 0.544680 | 0.000000 | 0.003016 | 0.000000 |
| `unbalanced<=8` | `mu_minus` | 153.571646 | 10.157547 | 10.157547 | 0.000000 | 0.066142 | 0.000000 |
| `far>8` | `mu_plus` | 384.765798 | 4.753997 | 4.753997 | 0.000000 | 0.012356 | 0.000000 |
| `far>8` | `mu_minus` | 293.612214 | 64.144692 | 34.840029 | 29.304662 | 0.118660 | 0.099807 |

## 3. omega 深度行

| bucket | omega | mu | abs | linear | cell ratio | bucket contribution |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `balanced<=2` | 2 | 1 | 53.108268 | 25.730063 | 0.484483 | 0.054677 |
| `balanced<=2` | 3 | -1 | 184.533700 | 22.408445 | 0.121433 | 0.047618 |
| `balanced<=2` | 4 | 1 | 204.291310 | 2.238431 | 0.010957 | 0.004757 |
| `balanced<=2` | 5 | -1 | 28.651595 | -9.367616 | 0.326949 | 0.019906 |
| `mid<=4` | 2 | 1 | 25.603634 | 10.146364 | 0.396286 | 0.025089 |
| `mid<=4` | 3 | -1 | 161.367705 | 24.392166 | 0.151159 | 0.060314 |
| `mid<=4` | 4 | 1 | 184.715118 | -4.400588 | 0.023824 | 0.010881 |
| `mid<=4` | 5 | -1 | 32.734257 | -10.114207 | 0.308979 | 0.025009 |
| `unbalanced<=8` | 3 | -1 | 129.622148 | -2.557702 | 0.019732 | 0.007654 |
| `unbalanced<=8` | 4 | 1 | 180.602472 | -0.544680 | 0.003016 | 0.001630 |
| `unbalanced<=8` | 5 | -1 | 23.949498 | -7.599845 | 0.317328 | 0.022742 |
| `far>8` | 3 | -1 | 242.576687 | 49.492360 | 0.204028 | 0.072957 |
| `far>8` | 4 | 1 | 384.765798 | 4.753997 | 0.012356 | 0.007008 |
| `far>8` | 5 | -1 | 51.035528 | -14.652331 | 0.287101 | 0.021599 |

## 4. 最大 shell 单元

| bucket | omega | shell | abs | linear | cell ratio | bucket contribution |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| `balanced<=2` | 3 | `(2D,4D]` | 77.584735 | 24.026580 | 0.309682 | 0.051057 |
| `balanced<=2` | 2 | `(D,2D]` | 39.083573 | 20.103586 | 0.514374 | 0.042720 |
| `unbalanced<=8` | 3 | `(D,2D]` | 44.978693 | -13.894007 | 0.308902 | 0.041577 |
| `unbalanced<=8` | 4 | `(D,2D]` | 42.273941 | -13.546811 | 0.320453 | 0.040538 |
| `far>8` | 3 | `(D,2D]` | 109.751618 | 24.112067 | 0.219697 | 0.035544 |
| `unbalanced<=8` | 4 | `(4D,8D]` | 46.877132 | 10.046878 | 0.214324 | 0.030065 |
| `far>8` | 3 | `(2D,4D]` | 73.386399 | 19.219395 | 0.261893 | 0.028331 |
| `mid<=4` | 3 | `(4D,8D]` | 39.535888 | 11.146348 | 0.281930 | 0.027561 |
| `mid<=4` | 4 | `(4D,8D]` | 54.118575 | -10.561041 | 0.195146 | 0.026114 |
| `mid<=4` | 2 | `(D,2D]` | 25.603634 | 10.146364 | 0.396286 | 0.025089 |
| `mid<=4` | 4 | `(8D,16D]` | 40.340320 | 8.693822 | 0.215512 | 0.021497 |
| `unbalanced<=8` | 4 | `(8D,16D]` | 41.385224 | 6.150121 | 0.148607 | 0.018404 |
| `balanced<=2` | 4 | `(2D,4D]` | 56.733435 | 8.476323 | 0.149406 | 0.018012 |
| `unbalanced<=8` | 3 | `(4D,8D]` | 27.494129 | 5.904693 | 0.214762 | 0.017670 |
| `unbalanced<=8` | 5 | `(8D,16D]` | 10.415603 | -5.469911 | 0.525165 | 0.016368 |
| `mid<=4` | 4 | `(2D,4D]` | 56.085309 | -6.161539 | 0.109860 | 0.015235 |

## 5. 证明边界

- 已闭合：深度层与 shell 层的精确分解账本，并与一维核 slice ratio 完全一致。
- 已闭合：样本中逐 `omega` 与逐 shell 的绝对线性余项 crude budget 均低于 cap。
- 重要边界：单个深度格的内部偏斜率可高于 cap，不能用格内比例界直接闭合。
- 当前真正剩余：证明所有深度格的绝对预算，或把超预算深度格登记为 DepthCell-PDEC。
- 下一目标：`DepthShellAbsoluteBudgetOrDepthCellPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json` | `eac8ba26aab932d189ae6a03e2e8ef9415f90c1746be4693ae0fb543a154d6ad` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-twocolor-balance-source-router.json` | `0986d2f09fe1b7834acf97e8f1dc7abc9fc91b1bb98673caa565f2c4a21e5505` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_kernel_depth_cancellation_router.py` | `83ec55f7152f2c174ee22eb4fc3513bb8f34078fc0862dc28812839752e87be2` |
