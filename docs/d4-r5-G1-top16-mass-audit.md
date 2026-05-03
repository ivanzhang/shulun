# D4/R5 G1 top16 半质量证书审计

**状态：** `top16_half_mass_verified_on_full_step100_scan`

O2 的 Neff<=64 可进一步压缩为 top16 半质量引理。扫描中最坏 top16_sum_share 正好出现在 Neff 最大点 x=1023400，约为 0.50305，刚过 1/2。因此最终解析硬点是证明非 ordinary 偏移权重不能有超过半数质量落在第 17 位之后的长尾中。

## 引理模板
- If the largest 16 nonordinary weights carry at least half of S, then S^2 <= 64 Q by Cauchy: Q >= T16^2/16 >= S^2/64.

## 最坏记录
- top16 半质量最坏：{'x': 1023400, 'count': 93, 'sum': 0.12864024379619862, 'square': 0.00037090008779737285, 'neff': 44.61663091594079, 'top16_sum': 0.06471268562456178, 'top16_sum_share': 0.5030516401001571, 'top16_square_share': 0.7754511745330431, 'cauchy_bound_from_top16_share': 63.225874379832945}
- Neff 最坏：{'x': 1023400, 'count': 93, 'sum': 0.12864024379619862, 'square': 0.00037090008779737285, 'neff': 44.61663091594079, 'top16_sum': 0.06471268562456178, 'top16_sum_share': 0.5030516401001571, 'top16_square_share': 0.7754511745330431, 'cauchy_bound_from_top16_share': 63.225874379832945}

## 下一义务
- 证明 top16_half_mass：最大的 16 个非 ordinary 偏移团贡献至少总非 ordinary 质量的一半
- 解析来源应结合 tau_sum<60、a<=sqrt(x)、偏移 h=(-x mod a) 的重叠限制与 kernel 衰减
- 若半质量常数太紧，可改为 top20：扫描最坏 top20_sum_share≈0.578，对应 Cauchy 常数约 59.8，仍小于 64
