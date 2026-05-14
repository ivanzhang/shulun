# Prime Matrix square-phase low-alpha 低超界 lcm 边画像

**状态：** `low_overflow_lcm_edge_profile_materialized_edge_bounds_open`

低超界 tail 可从 `m` 层进一步剥成 `(d,e)` 边：`sum_{D<lcm(d,e)<=16D} lambda_d lambda_e R_lcm(d,e)`。样本中主通道是 `gcd(d,e)=1` 的 coprime boundary lcm 边，其余为小 gcd overflow 通道。因此低超界角度失败可被命名为 coprime boundary edge 异常或 small-gcd overflow PDEC。

```text
low_overflow_edge_profile_materialized=true
coprime_boundary_edge_channel_identified=true
small_gcd_overflow_channel_identified=true
coprime_boundary_edge_angle_bound_proved=false
small_gcd_overflow_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. coprime vs small-gcd

| z | low edges | total abs | coprime abs share | coprime weight share | coprime angle | noncoprime angle |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 0 | 0.000000 | n/a | n/a | n/a | n/a |
| 13 | 976 | 133.732051 | 0.493586 | 0.461994 | 0.074118 | 0.044777 |
| 31 | 9836 | 1595.174316 | 0.563130 | 0.569652 | 0.016316 | 0.015179 |
| 61 | 19072 | 3079.983705 | 0.612847 | 0.616454 | 0.005551 | 0.006269 |

## 2. 主要 gcd 通道

| z | gcd | edges | abs contribution | signed/abs | angle |
| ---: | --- | ---: | ---: | ---: | ---: |
| 13 | `gcd=1` | 244 | 66.008281 | 0.090144 | 0.074118 |
| 13 | `gcd=3` | 78 | 12.319519 | 0.357218 | 0.279076 |
| 13 | `gcd=2` | 74 | 10.470079 | 0.164335 | 0.130129 |
| 13 | `gcd=5` | 80 | 9.289286 | 0.061816 | 0.049257 |
| 13 | `gcd=7` | 70 | 8.556203 | 0.078320 | 0.065124 |
| 13 | `gcd=11` | 72 | 8.093827 | 0.253211 | 0.213247 |
| 13 | `gcd=13` | 72 | 7.202677 | 0.128385 | 0.113013 |
| 13 | `gcd=15` | 18 | 1.692454 | 0.378722 | 0.321711 |
| 31 | `gcd=1` | 3304 | 898.291025 | 0.021395 | 0.016316 |
| 31 | `gcd=2` | 898 | 193.009239 | 0.056605 | 0.044059 |
| 31 | `gcd=3` | 766 | 119.470429 | 0.098683 | 0.072558 |
| 31 | `gcd=5` | 578 | 83.725966 | 0.012002 | 0.009516 |
| 31 | `gcd=7` | 512 | 66.365248 | 0.071067 | 0.054204 |
| 31 | `gcd=11` | 408 | 37.592039 | 0.053517 | 0.040141 |
| 31 | `gcd=13` | 368 | 29.886351 | 0.010853 | 0.008332 |
| 31 | `gcd=6` | 190 | 23.312239 | 0.149494 | 0.115348 |
| 61 | `gcd=1` | 7480 | 1887.557718 | 0.007458 | 0.005551 |
| 61 | `gcd=2` | 1882 | 380.051458 | 0.005757 | 0.004379 |
| 61 | `gcd=3` | 1546 | 236.304904 | 0.033313 | 0.024457 |
| 61 | `gcd=5` | 1208 | 147.851705 | 0.044722 | 0.034621 |
| 61 | `gcd=7` | 962 | 99.868895 | 0.053229 | 0.039598 |
| 61 | `gcd=11` | 664 | 53.468070 | 0.114971 | 0.082663 |
| 61 | `gcd=6` | 374 | 44.724678 | 0.054272 | 0.042155 |
| 61 | `gcd=13` | 572 | 38.071770 | 0.012632 | 0.009557 |

## 3. 证明边界

- 已物化：低超界 lcm shell 的 `(d,e)` 边画像。
- 已压缩：低超界失败二分为 coprime boundary edge 与 small-gcd overflow。
- 未闭合：coprime boundary edge 角度界。
- 未闭合：small-gcd overflow PDEC 排斥或吸收。
- 下一目标：`CoprimeBoundaryLCMEdgeAngleBoundOrSmallGCDOverflowPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-tail-lcm-shell-router.json` | `66e956f3263a3e300ed49a2d3ce2b18816b98738537199c107e98dbc74e3193d` |
| `experiments/prime_matrix_square_phase_lowalpha_low_overflow_edge_profile_router.py` | `195da297310d492a28c2408d22bd2e10e2be279523c8c9cdf8fac0b754128098` |
