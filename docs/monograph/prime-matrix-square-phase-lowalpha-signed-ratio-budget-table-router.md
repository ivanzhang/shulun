# Prime Matrix square-phase low-alpha signed-ratio 预算表

**状态：** `signed_ratio_budget_table_materialized_nontrivial_z31_z61_caps_open`

块级 signed-ratio 预算表进一步压缩了 LocalizedBlock-PDEC：`z=13` 的目标角度大于 `1`，而任何块天然满足 `|signed|/abs<=1`，所以 `z=13` 四个原子由平凡界闭合。真正非平凡剩余只有 `z=31` 与 `z=61` 的 8 个局部块 cap：`z=31` 需 `signed/abs<=0.591273`，`z=61` 需 `signed/abs<=0.221522`。若这些 cap 失败，失败块就是明确的 LocalizedBlock-PDEC。

```text
signed_ratio_budget_table_materialized=true
z13_atoms_closed_by_trivial_signed_ratio=true
z31_z61_nontrivial_caps_materialized=true
signed_ratio_budget_table_proved=false
localized_block_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 原子预算表

| atom | route | target | required cap | observed | slack | proof class |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `LocalizedBlockPDEC(z=31,bucket=balanced<=2)` | `BilinearDispersion` | 0.591273 | 0.591273 | 0.027417 | 0.563856 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=31,bucket=far>8)` | `EndpointPDEC` | 0.591273 | 0.591273 | 0.000073 | 0.591201 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=31,bucket=mid<=4)` | `BilinearDispersion` | 0.591273 | 0.591273 | 0.002149 | 0.589124 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=31,bucket=unbalanced<=8)` | `EndpointPDEC` | 0.591273 | 0.591273 | 0.080038 | 0.511235 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=61,bucket=balanced<=2)` | `BilinearDispersion` | 0.221522 | 0.221522 | 0.031722 | 0.189800 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=61,bucket=far>8)` | `EndpointPDEC` | 0.221522 | 0.221522 | 0.044350 | 0.177172 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=61,bucket=mid<=4)` | `BilinearDispersion` | 0.221522 | 0.221522 | 0.021097 | 0.200425 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=61,bucket=unbalanced<=8)` | `EndpointPDEC` | 0.221522 | 0.221522 | 0.028766 | 0.192756 | `nontrivial-localized-cap` |
| `LocalizedBlockPDEC(z=13,bucket=balanced<=2)` | `BilinearDispersion` | 2.715323 | 1.000000 | 0.400790 | 0.599210 | `trivial-signed-ratio` |
| `LocalizedBlockPDEC(z=13,bucket=far>8)` | `EndpointPDEC` | 2.715323 | 1.000000 | 0.047438 | 0.952562 | `trivial-signed-ratio` |
| `LocalizedBlockPDEC(z=13,bucket=mid<=4)` | `BilinearDispersion` | 2.715323 | 1.000000 | 0.012484 | 0.987516 | `trivial-signed-ratio` |
| `LocalizedBlockPDEC(z=13,bucket=unbalanced<=8)` | `EndpointPDEC` | 2.715323 | 1.000000 | 0.000106 | 0.999894 | `trivial-signed-ratio` |

## 2. 非平凡剩余

| atom | cap | observed | route |
| --- | ---: | ---: | --- |
| `LocalizedBlockPDEC(z=31,bucket=unbalanced<=8)` | 0.591273 | 0.080038 | `EndpointPDEC` |
| `LocalizedBlockPDEC(z=61,bucket=far>8)` | 0.221522 | 0.044350 | `EndpointPDEC` |
| `LocalizedBlockPDEC(z=61,bucket=balanced<=2)` | 0.221522 | 0.031722 | `BilinearDispersion` |
| `LocalizedBlockPDEC(z=61,bucket=unbalanced<=8)` | 0.221522 | 0.028766 | `EndpointPDEC` |
| `LocalizedBlockPDEC(z=31,bucket=balanced<=2)` | 0.591273 | 0.027417 | `BilinearDispersion` |
| `LocalizedBlockPDEC(z=61,bucket=mid<=4)` | 0.221522 | 0.021097 | `BilinearDispersion` |
| `LocalizedBlockPDEC(z=31,bucket=mid<=4)` | 0.591273 | 0.002149 | `BilinearDispersion` |
| `LocalizedBlockPDEC(z=31,bucket=far>8)` | 0.591273 | 0.000073 | `EndpointPDEC` |

## 3. 证明边界

- 已闭合：`z=13` 原子由 `signed/abs<=1` 平凡界通过。
- 已物化：`z=31,z=61` 的 8 个非平凡 signed-ratio cap。
- 未闭合：证明这些 cap，或排斥相应 LocalizedBlock-PDEC。
- 下一目标：`Z31Z61LocalizedBlockSignedRatioCapsOrPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-bilinear-block-budget-contract-router.json` | `f90e12d06a383f59ee4da84f5aa83c61f47d3c7de2b2a86f3946f8d5b31fefd9` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-localized-block-pdec-atom-router.json` | `896681b6eb105bca425c3ba0714e3dd1156c456d237dd5c4a72696b60f6c938f` |
| `experiments/prime_matrix_square_phase_lowalpha_signed_ratio_budget_table_router.py` | `5947dabcab4cc8611bc53e1264c042bd54b544c59e3c431b20baf95688204836` |
