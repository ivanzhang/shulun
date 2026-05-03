# R2 C_poly 吸收扫描

**状态：** `all_scanned_values_pass`

| C_poly | C_* | B1 | B2 | B4 | 最小余量 |
|---:|---:|---:|---:|---:|---:|
| 0 | 160 | 960 | 880 | 820 | 140 |
| 80 | 160 | 960 | 880 | 820 | 140 |
| 160 | 160 | 960 | 880 | 820 | 140 |
| 240 | 240 | 1280 | 1200 | 1140 | 380 |
| 320 | 320 | 1600 | 1520 | 1460 | 620 |
| 480 | 480 | 2240 | 2160 | 2100 | 1100 |

## 解释
C_poly can be absorbed by increasing C_star and recomputing B1,B2,B4. With the formula in 6.15.2, scanned values through 480 keep positive margins; this affects thresholds but not the local DBA closure logic.
