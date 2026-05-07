# FO-PDEC fractional Weighted Hall dual 审计

**状态：** `weighted_hall_dual_full_duplicate_weight_blocked_not_global_proof`

当前 FO-PDEC 嵌套重复的分数加权对偶不能恢复完整第二单位质量。每个重复来自同一正式坐标，且大小 Hall 块是 laminar 嵌套；差层只增加同数目的半素数和素数，surplus 增量为 0，没有新的 Hall 压力。因此 raw 3.959... 必须降到坐标 cap 口径；若 cross-q persistence 不成立，还要继续降到 primitive/单分支口径。

## 1. 子门裁定

```text
closed_subgate: FractionalWeightedHallCannotRecoverFullNestedDuplicateMass
all_nested_full_extra_unit_weight_blocked: true
factor_199_full_extra_unit_weight_blocked: true
```

## 2. 口径比较

| mode | formal status | rows | best Fourier projection |
| --- | --- | ---: | --- |
| global_library_raw | diagnostic_only | 43 | ell=199, h=95, Fourier=3.959247567099, mass=4, support=3 |
| nested_coordinate_cap | allows_cross_q_but_rejects_same_coordinate_duplicate_unit_weight | 36 | ell=199, h=95, Fourier=2.969836690579, mass=3, support=3 |
| physical_candidate_cap | dedupes_cross_q_same_physical_candidate | 27 | ell=199, h=81, Fourier=1.999750779035, mass=2, support=2 |
| single_q_row_coordinate_cap | single_formal_branch | 9 | ell=19, h=1, Fourier=1.000000000000, mass=1, support=1 |
| single_block | single_hall_block | 13 | ell=19, h=1, Fourier=1.000000000000, mass=1, support=1 |

## 3. 嵌套差层审计

| key | blocks | delta semiprime | delta prime | delta surplus | conclusion |
| --- | --- | ---: | ---: | ---: | --- |
| [1993, 836, 835, 1915, -126, 1664077, 19, 18] | [1, 4] | 1 | 1 | 0 | blocked_by_laminar_zero_pressure_increment |
| [1993, 836, 835, 1919, -126, 1664081, 127, 73] | [1, 4] | 1 | 1 | 0 | blocked_by_laminar_zero_pressure_increment |
| [1993, 836, 836, 78, 30, 1664233, 83, 6] | [1, 4] | 1 | 1 | 0 | blocked_by_laminar_zero_pressure_increment |
| [1993, 836, 836, 82, 30, 1664237, 199, 40] | [1, 4] | 1 | 1 | 0 | blocked_by_laminar_zero_pressure_increment |
| [1993, 836, 836, 84, 30, 1664239, 193, 64] | [1, 4] | 1 | 1 | 0 | blocked_by_laminar_zero_pressure_increment |
| [1993, 836, 836, 126, 84, 1664281, 29, 24] | [1, 4] | 1 | 1 | 0 | blocked_by_laminar_zero_pressure_increment |
| [1993, 836, 836, 138, 84, 1664293, 79, 46] | [1, 4] | 1 | 1 | 0 | blocked_by_laminar_zero_pressure_increment |

## 4. 证明读法

加权 Hall 对偶若要把同一坐标重复计两次，必须证明第二个权重来自独立差层。但本审计中的嵌套差层不含这个重复坐标，并且只增加一个新半素数和一个新素数，Hall surplus 不下降。因此差层没有新的缺陷压力可支付重复坐标的第二单位质量。

这不是全局 PDEC 排斥。它只排除了当前最强 `global_library_raw` 信号中“嵌套重复靠分数加权恢复完整第二单位质量”的路线。

## 5. 剩余

- `coordinate-cap PDEC threshold using the 2.9698366905785227-level signal if cross-q persistence is proved`
- `physical-cap / primitive PDEC threshold using the 1.9997507790353146-level signal`
- `single-branch PDEC or SAE/Endpoint absorption when cross-q persistence is rejected`
- `independent non-laminar weighted dual proof, if a future branch supplies one`
