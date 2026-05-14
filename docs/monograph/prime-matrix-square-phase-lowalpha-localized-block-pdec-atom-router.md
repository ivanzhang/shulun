# Prime Matrix square-phase low-alpha LocalizedBlock-PDEC 原子

**状态：** `localized_block_pdec_atoms_materialized_exclusion_open`

双线性块 signed budget 的剩余现在原子化为具体 `LocalizedBlockPDEC(z,bucket)`。balanced/mid 原子进入 BilinearDispersion 证明路线，unbalanced/far 原子进入 EndpointPDEC 路线。因此下一步不再需要处理整块总和，只需给出这些原子的 signed ratio 预算表，或逐个排斥局部块 PDEC。

```text
localized_block_pdec_atoms_materialized=true
bilinear_dispersion_atoms_routed=true
endpoint_pdec_atoms_routed=true
signed_ratio_budget_table_proved=false
localized_block_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 路线汇总

| route | atoms | total weighted budget | max weighted budget | sample atoms |
| --- | ---: | ---: | ---: | --- |
| `BilinearDispersion` | 6 | 0.083048 | 0.063104 | `['LocalizedBlockPDEC(z=13,bucket=balanced<=2)', 'LocalizedBlockPDEC(z=13,bucket=mid<=4)', 'LocalizedBlockPDEC(z=31,bucket=balanced<=2)', 'LocalizedBlockPDEC(z=31,bucket=mid<=4)', 'LocalizedBlockPDEC(z=61,bucket=balanced<=2)', 'LocalizedBlockPDEC(z=61,bucket=mid<=4)']` |
| `EndpointPDEC` | 6 | 0.061982 | 0.024870 | `['LocalizedBlockPDEC(z=13,bucket=unbalanced<=8)', 'LocalizedBlockPDEC(z=13,bucket=far>8)', 'LocalizedBlockPDEC(z=31,bucket=unbalanced<=8)', 'LocalizedBlockPDEC(z=31,bucket=far>8)', 'LocalizedBlockPDEC(z=61,bucket=unbalanced<=8)', 'LocalizedBlockPDEC(z=61,bucket=far>8)']` |

## 2. 最大原子

| atom | route | signed/abs | weighted budget | abs share |
| --- | --- | ---: | ---: | ---: |
| `LocalizedBlockPDEC(z=13,bucket=balanced<=2)` | `BilinearDispersion` | 0.400790 | 0.063104 | 0.157450 |
| `LocalizedBlockPDEC(z=13,bucket=far>8)` | `EndpointPDEC` | 0.047438 | 0.024870 | 0.524272 |
| `LocalizedBlockPDEC(z=31,bucket=unbalanced<=8)` | `EndpointPDEC` | 0.080038 | 0.016034 | 0.200323 |
| `LocalizedBlockPDEC(z=61,bucket=far>8)` | `EndpointPDEC` | 0.044350 | 0.015939 | 0.359395 |
| `LocalizedBlockPDEC(z=61,bucket=balanced<=2)` | `BilinearDispersion` | 0.031722 | 0.007908 | 0.249309 |
| `LocalizedBlockPDEC(z=61,bucket=unbalanced<=8)` | `EndpointPDEC` | 0.028766 | 0.005093 | 0.177040 |
| `LocalizedBlockPDEC(z=31,bucket=balanced<=2)` | `BilinearDispersion` | 0.027417 | 0.004911 | 0.179123 |
| `LocalizedBlockPDEC(z=61,bucket=mid<=4)` | `BilinearDispersion` | 0.021097 | 0.004520 | 0.214256 |
| `LocalizedBlockPDEC(z=13,bucket=mid<=4)` | `BilinearDispersion` | 0.012484 | 0.002184 | 0.174940 |
| `LocalizedBlockPDEC(z=31,bucket=mid<=4)` | `BilinearDispersion` | 0.002149 | 0.000420 | 0.195326 |
| `LocalizedBlockPDEC(z=31,bucket=far>8)` | `EndpointPDEC` | 0.000073 | 0.000031 | 0.425227 |
| `LocalizedBlockPDEC(z=13,bucket=unbalanced<=8)` | `EndpointPDEC` | 0.000106 | 0.000015 | 0.143338 |

## 3. 证明边界

- 已物化：所有局部块 PDEC 原子。
- 未闭合：BilinearDispersion 原子的 signed ratio 预算。
- 未闭合：EndpointPDEC 原子的排斥或吸收。
- 未闭合：统一 signed ratio budget 表。
- 下一目标：`LocalizedBlockPDECAtomExclusionOrSignedRatioBudgetTable`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json` | `f90e12d06a383f59ee4da84f5aa83c61f47d3c7de2b2a86f3946f8d5b31fefd9` |
| `experiments/prime_matrix_square_phase_lowalpha_localized_block_pdec_atom_router.py` | `366706a2d2b080e820295e96a78b04625e5d9a64fa946da3db6a3a63b78f6e34` |
