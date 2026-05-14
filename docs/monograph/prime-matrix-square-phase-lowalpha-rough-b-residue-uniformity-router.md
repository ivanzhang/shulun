# Prime Matrix square-phase low-alpha rough-b 低模残基均匀性路由

**状态：** `rough_b_lowmod_residue_uniformity_materialized_selberg_input_open`

维数一粗数筛的核心输入是 b 多重序列在低素模下的残基均匀性。本账本对 prime-a incidence 产生的 b 多重序列逐素数 ell 统计 `b=0 mod ell` 与全残基 L1 偏差；若某个 ell 出现持续大 z-score，则它就是 LowMod-RoughB-PDEC。默认样本聚合账本未越过 z-score 阈值，说明 Mertens 账本稳定来自真实低模均匀性，但统一低模差异界尚未证明。

```text
lowmod_residue_ledger_materialized=true
sample_aggregate_zscore_within_limit=true
sample_profile_zscore_within_limit=true
uniform_lowmod_discrepancy_bound_proved=false
lowmod_rough_b_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 聚合诊断

| ell limit | values | z limit | flagged | worst zero row | worst L1 row |
| ---: | ---: | ---: | ---: | --- | --- |
| 61 | 43666 | 3.500000 | 0 | `{'ell': 53, 'value_count': 43666, 'zero_count': 883, 'zero_expected': 823.8867924528302, 'zero_over_expected': 1.0717491870104887, 'zero_zscore': 2.0791557222540957, 'max_residue': 50, 'max_residue_count': 891, 'max_residue_over_expected': 1.0814592589199836, 'min_residue_count': 770, 'l1_discrepancy': 1340.7547169811317, 'l1_over_count': 0.03070477527094608}` | `{'ell': 53, 'value_count': 43666, 'zero_count': 883, 'zero_expected': 823.8867924528302, 'zero_over_expected': 1.0717491870104887, 'zero_zscore': 2.0791557222540957, 'max_residue': 50, 'max_residue_count': 891, 'max_residue_over_expected': 1.0814592589199836, 'min_residue_count': 770, 'l1_discrepancy': 1340.7547169811317, 'l1_over_count': 0.03070477527094608}` |

## 2. 聚合低模表

| ell | zero | expected | zero/expected | zscore | max residue | max/expected | L1/count |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 21897 | 21833.000000 | 1.002931 | 0.612545 | 0:21897 | 1.002931 | 0.002931 |
| 3 | 14514 | 14555.333333 | 0.997160 | -0.419600 | 1:14645 | 1.006160 | 0.004107 |
| 5 | 8756 | 8733.200000 | 1.002611 | 0.272774 | 0:8756 | 1.002611 | 0.002079 |
| 7 | 6255 | 6238.000000 | 1.002725 | 0.232488 | 4:6344 | 1.016993 | 0.012092 |
| 11 | 4017 | 3969.636364 | 1.011931 | 0.788435 | 10:4051 | 1.020496 | 0.012833 |
| 13 | 3321 | 3358.923077 | 0.988710 | -0.681059 | 7:3421 | 1.018481 | 0.009178 |
| 17 | 2488 | 2568.588235 | 0.968625 | -1.639037 | 15:2622 | 1.020794 | 0.013132 |
| 19 | 2328 | 2298.210526 | 1.012962 | 0.638423 | 11:2367 | 1.029932 | 0.013919 |
| 23 | 1868 | 1898.521739 | 0.983923 | -0.716233 | 15:1972 | 1.038703 | 0.014760 |
| 29 | 1467 | 1505.724138 | 0.974282 | -1.015615 | 10:1593 | 1.057963 | 0.020925 |
| 31 | 1435 | 1408.580645 | 1.018756 | 0.715569 | 7:1480 | 1.050703 | 0.018590 |
| 37 | 1239 | 1180.162162 | 1.049856 | 1.736343 | 0:1239 | 1.049856 | 0.016905 |
| 41 | 1090 | 1065.024390 | 1.023451 | 0.774815 | 20:1145 | 1.075093 | 0.026771 |
| 43 | 1032 | 1015.488372 | 1.016260 | 0.524278 | 22:1074 | 1.057619 | 0.022431 |
| 47 | 919 | 929.063830 | 0.989168 | -0.333742 | 6:1013 | 1.090345 | 0.023750 |
| 53 | 883 | 823.886792 | 1.071749 | 2.079156 | 50:891 | 1.081459 | 0.030705 |
| 59 | 748 | 740.101695 | 1.010672 | 0.292820 | 46:811 | 1.095795 | 0.027891 |
| 61 | 744 | 715.836066 | 1.039344 | 1.061392 | 40:769 | 1.074268 | 0.024981 |

## 3. 每个 P 的最坏行

| P | values | worst zero row | worst L1 row |
| ---: | ---: | --- | --- |
| 10007 | 777 | `{'ell': 19, 'value_count': 777, 'zero_count': 52, 'zero_expected': 40.89473684210526, 'zero_over_expected': 1.2715572715572716, 'zero_zscore': 1.7841677845019748, 'max_residue': 0, 'max_residue_count': 52, 'max_residue_over_expected': 1.2715572715572716, 'min_residue_count': 31, 'l1_discrepancy': 72.31578947368422, 'l1_over_count': 0.09307051412314571}` | `{'ell': 61, 'value_count': 777, 'zero_count': 11, 'zero_expected': 12.737704918032787, 'zero_over_expected': 0.8635778635778636, 'zero_zscore': -0.49093017936611, 'max_residue': 55, 'max_residue_count': 25, 'max_residue_over_expected': 1.9626769626769627, 'min_residue_count': 4, 'l1_discrepancy': 222.68852459016392, 'l1_over_count': 0.2866004177479587}` |
| 36739 | 4013 | `{'ell': 29, 'value_count': 4013, 'zero_count': 125, 'zero_expected': 138.3793103448276, 'zero_over_expected': 0.9033142287565412, 'zero_zscore': -1.1574923517560032, 'max_residue': 25, 'max_residue_count': 152, 'max_residue_over_expected': 1.0984301021679541, 'min_residue_count': 123, 'l1_discrepancy': 226.13793103448276, 'l1_over_count': 0.056351340900693436}` | `{'ell': 59, 'value_count': 4013, 'zero_count': 64, 'zero_expected': 68.01694915254237, 'zero_over_expected': 0.9409419386992276, 'zero_zscore': -0.4912468395666178, 'max_residue': 41, 'max_residue_count': 90, 'max_residue_over_expected': 1.3231996012957887, 'min_residue_count': 51, 'l1_discrepancy': 427.0508474576271, 'l1_over_count': 0.10641685707890036}` |
| 83561 | 10697 | `{'ell': 53, 'value_count': 10697, 'zero_count': 231, 'zero_expected': 201.83018867924528, 'zero_over_expected': 1.1445265027577827, 'zero_zscore': 2.072892689268252, 'max_residue': 27, 'max_residue_count': 240, 'max_residue_over_expected': 1.1891184444236702, 'min_residue_count': 175, 'l1_discrepancy': 586.4905660377358, 'l1_over_count': 0.054827574650625016}` | `{'ell': 59, 'value_count': 10697, 'zero_count': 196, 'zero_expected': 181.3050847457627, 'zero_over_expected': 1.0810507618958587, 'zero_zscore': 1.100713017843508, 'max_residue': 47, 'max_residue_count': 224, 'max_residue_over_expected': 1.2354865850238383, 'min_residue_count': 154, 'l1_discrepancy': 620.3050847457628, 'l1_over_count': 0.05798869633969924}` |
| 200003 | 28179 | `{'ell': 17, 'value_count': 28179, 'zero_count': 1576, 'zero_expected': 1657.5882352941176, 'zero_over_expected': 0.9507789488626283, 'zero_zscore': -2.0656354640814314, 'max_residue': 4, 'max_residue_count': 1736, 'max_residue_over_expected': 1.0473047304730474, 'min_residue_count': 1576, 'l1_discrepancy': 467.7647058823527, 'l1_over_count': 0.016599762443037465}` | `{'ell': 41, 'value_count': 28179, 'zero_count': 691, 'zero_expected': 687.2926829268292, 'zero_over_expected': 1.0053940877958765, 'zero_zscore': 0.14316959741624827, 'max_residue': 34, 'max_residue_count': 747, 'max_residue_over_expected': 1.0868732034493773, 'min_residue_count': 622, 'l1_discrepancy': 965.1219512195123, 'l1_over_count': 0.0342496877539839}` |

## 4. 证明边界

- 已物化：prime-a 生成的 `b` 多重序列在低素模下的零类与全残基偏差账本。
- 已闭合：任一越界低模行都可命名为 LowMod-RoughB-PDEC 候选。
- 未闭合：给出全局统一低模差异上界，并把它接入维数一 Selberg 上筛。
- 未闭合：排斥持久 LowMod-RoughB-PDEC/SAE。
- 下一目标：`LowModRoughBResidueDiscrepancySelbergInputOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-b-sieve-router.json` | `9d31214bd48757964376cf5d1255d145217506dde8481ca45530f8aa320eb482` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-mertens-ledger-router.json` | `74d26984ec6cb02e19f3f3d51f798d965b34bc9650451ab73d1bbb5fba081e3a` |
| `experiments/prime_matrix_square_phase_lowalpha_rough_b_residue_uniformity_router.py` | `d35c388e47185f7da8b555cb55d623a8bdf42f89fbd581ea9c4b1e4452d694fb` |
