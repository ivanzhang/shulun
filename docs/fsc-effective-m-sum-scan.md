# FSC 有效 m 倒数和扫描

**状态：** `effective_m_inverse_sum_below_covering_threshold_in_samples`

对无锁定核心实际出现的有效 m 层计算倒数和。样本中最坏覆盖行的有效倒数和通常低于覆盖系统阈值 1，支持 FSC 的覆盖倒数和缺口；但理论可用 m 范围的倒数和可达 1，仍需证明有效素数层不能激活全部可用 m。

## 摘要
- P=5 worst row=1 share=0.000 U=1 holes=1 m_count=0 sum1/m=0.000 cap/U=0.000; maxInv row=1 sum1/m=0.000 share=0.000
- P=7 worst row=3 share=0.500 U=2 holes=1 m_count=1 sum1/m=0.200 cap/U=0.500; maxInv row=3 sum1/m=0.200 share=0.500
- P=11 worst row=4 share=0.333 U=3 holes=2 m_count=1 sum1/m=0.143 cap/U=0.333; maxInv row=4 sum1/m=0.143 share=0.333
- P=13 worst row=9 share=0.667 U=3 holes=1 m_count=2 sum1/m=0.131 cap/U=0.667; maxInv row=4 sum1/m=0.368 share=0.400
- P=17 worst row=12 share=0.833 U=6 holes=1 m_count=5 sum1/m=0.191 cap/U=0.833; maxInv row=3 sum1/m=0.368 share=0.333
- P=19 worst row=15 share=0.800 U=5 holes=1 m_count=4 sum1/m=0.150 cap/U=0.800; maxInv row=6 sum1/m=0.345 share=0.600
- P=23 worst row=14 share=0.714 U=7 holes=2 m_count=7 sum1/m=0.223 cap/U=1.000; maxInv row=3 sum1/m=0.479 share=0.286
- P=29 worst row=18 share=0.571 U=7 holes=3 m_count=4 sum1/m=0.135 cap/U=0.571; maxInv row=7 sum1/m=0.279 share=0.333
- P=31 worst row=25 share=0.750 U=8 holes=2 m_count=6 sum1/m=0.099 cap/U=0.750; maxInv row=6 sum1/m=0.412 share=0.444
- P=37 worst row=36 share=0.700 U=10 holes=3 m_count=7 sum1/m=0.094 cap/U=0.700; maxInv row=5 sum1/m=0.436 share=0.444
- P=41 worst row=32 share=0.667 U=9 holes=3 m_count=6 sum1/m=0.078 cap/U=0.667; maxInv row=9 sum1/m=0.364 share=0.364
- P=43 worst row=31 share=0.667 U=9 holes=3 m_count=6 sum1/m=0.102 cap/U=0.667; maxInv row=12 sum1/m=0.346 share=0.500
- P=47 worst row=46 share=0.692 U=13 holes=4 m_count=9 sum1/m=0.078 cap/U=0.692; maxInv row=4 sum1/m=0.489 share=0.308
- P=53 worst row=25 share=0.636 U=11 holes=4 m_count=9 sum1/m=0.190 cap/U=0.818; maxInv row=9 sum1/m=0.281 share=0.333
- P=59 worst row=42 share=0.786 U=14 holes=3 m_count=12 sum1/m=0.131 cap/U=0.857; maxInv row=6 sum1/m=0.382 share=0.308
- P=61 worst row=22 share=0.643 U=14 holes=5 m_count=11 sum1/m=0.217 cap/U=0.786; maxInv row=10 sum1/m=0.386 share=0.333
- P=67 worst row=20 share=0.583 U=12 holes=5 m_count=9 sum1/m=0.197 cap/U=0.833; maxInv row=10 sum1/m=0.251 share=0.250
- P=71 worst row=68 share=0.706 U=17 holes=5 m_count=12 sum1/m=0.080 cap/U=0.706; maxInv row=9 sum1/m=0.461 share=0.333
- P=73 worst row=66 share=0.688 U=16 holes=5 m_count=11 sum1/m=0.073 cap/U=0.688; maxInv row=7 sum1/m=0.477 share=0.438
- P=79 worst row=61 share=0.688 U=16 holes=5 m_count=12 sum1/m=0.092 cap/U=0.750; maxInv row=10 sum1/m=0.378 share=0.333
- P=83 worst row=16 share=0.684 U=19 holes=6 m_count=18 sum1/m=0.414 cap/U=1.053; maxInv row=10 sum1/m=0.496 share=0.421
- P=89 worst row=15 share=0.611 U=18 holes=7 m_count=15 sum1/m=0.352 cap/U=1.000; maxInv row=12 sum1/m=0.402 share=0.368
- P=97 worst row=82 share=0.739 U=23 holes=6 m_count=19 sum1/m=0.086 cap/U=0.826; maxInv row=8 sum1/m=0.525 share=0.435
- P=101 worst row=73 share=0.650 U=20 holes=7 m_count=15 sum1/m=0.072 cap/U=0.750; maxInv row=8 sum1/m=0.430 share=0.304
- P=103 worst row=71 share=0.579 U=19 holes=8 m_count=16 sum1/m=0.098 cap/U=0.842; maxInv row=8 sum1/m=0.327 share=0.300
- P=107 worst row=93 share=0.750 U=24 holes=6 m_count=24 sum1/m=0.099 cap/U=1.000; maxInv row=10 sum1/m=0.538 share=0.458
- P=109 worst row=54 share=0.680 U=25 holes=8 m_count=21 sum1/m=0.168 cap/U=0.840; maxInv row=12 sum1/m=0.494 share=0.591
- P=113 worst row=88 share=0.696 U=23 holes=7 m_count=19 sum1/m=0.088 cap/U=0.826; maxInv row=10 sum1/m=0.498 share=0.440
- P=127 worst row=91 share=0.630 U=27 holes=10 m_count=21 sum1/m=0.098 cap/U=0.778; maxInv row=10 sum1/m=0.496 share=0.429
- P=131 worst row=88 share=0.630 U=27 holes=10 m_count=18 sum1/m=0.082 cap/U=0.667; maxInv row=14 sum1/m=0.428 share=0.423
- P=137 worst row=137 share=0.625 U=24 holes=9 m_count=15 sum1/m=0.042 cap/U=0.625; maxInv row=9 sum1/m=0.351 share=0.370
- P=139 worst row=102 share=0.654 U=26 holes=9 m_count=19 sum1/m=0.063 cap/U=0.731; maxInv row=9 sum1/m=0.436 share=0.393
- P=149 worst row=127 share=0.621 U=29 holes=11 m_count=23 sum1/m=0.056 cap/U=0.793; maxInv row=11 sum1/m=0.476 share=0.419
- P=151 worst row=147 share=0.613 U=31 holes=12 m_count=23 sum1/m=0.060 cap/U=0.742; maxInv row=12 sum1/m=0.474 share=0.433
- P=157 worst row=118 share=0.633 U=30 holes=11 m_count=19 sum1/m=0.041 cap/U=0.633; maxInv row=12 sum1/m=0.418 share=0.333
- P=163 worst row=115 share=0.656 U=32 holes=11 m_count=23 sum1/m=0.060 cap/U=0.719; maxInv row=8 sum1/m=0.494 share=0.424
- P=167 worst row=140 share=0.676 U=34 holes=11 m_count=25 sum1/m=0.063 cap/U=0.735; maxInv row=10 sum1/m=0.517 share=0.441
- P=173 worst row=135 share=0.633 U=30 holes=11 m_count=20 sum1/m=0.057 cap/U=0.667; maxInv row=14 sum1/m=0.374 share=0.345
- P=179 worst row=167 share=0.618 U=34 holes=13 m_count=24 sum1/m=0.048 cap/U=0.706; maxInv row=10 sum1/m=0.467 share=0.424
- P=181 worst row=129 share=0.676 U=34 holes=11 m_count=25 sum1/m=0.070 cap/U=0.735; maxInv row=10 sum1/m=0.467 share=0.400
- P=191 worst row=122 share=0.600 U=35 holes=14 m_count=23 sum1/m=0.069 cap/U=0.657; maxInv row=16 sum1/m=0.434 share=0.412
- P=193 worst row=141 share=0.622 U=37 holes=14 m_count=27 sum1/m=0.071 cap/U=0.730; maxInv row=16 sum1/m=0.468 share=0.432
- P=197 worst row=138 share=0.610 U=41 holes=16 m_count=29 sum1/m=0.076 cap/U=0.707; maxInv row=15 sum1/m=0.486 share=0.432
- P=199 worst row=179 share=0.667 U=36 holes=12 m_count=25 sum1/m=0.050 cap/U=0.694; maxInv row=15 sum1/m=0.495 share=0.447
- P=211 worst row=210 share=0.619 U=42 holes=16 m_count=28 sum1/m=0.043 cap/U=0.667; maxInv row=13 sum1/m=0.463 share=0.375
- P=223 worst row=152 share=0.659 U=41 holes=14 m_count=28 sum1/m=0.055 cap/U=0.683; maxInv row=14 sum1/m=0.482 share=0.395
- P=227 worst row=177 share=0.651 U=43 holes=15 m_count=32 sum1/m=0.067 cap/U=0.744; maxInv row=13 sum1/m=0.430 share=0.375
- P=229 worst row=148 share=0.625 U=40 holes=15 m_count=26 sum1/m=0.058 cap/U=0.650; maxInv row=13 sum1/m=0.372 share=0.368
- P=233 worst row=186 share=0.625 U=40 holes=15 m_count=28 sum1/m=0.051 cap/U=0.700; maxInv row=13 sum1/m=0.465 share=0.372
- P=239 worst row=196 share=0.636 U=44 holes=16 m_count=32 sum1/m=0.058 cap/U=0.727; maxInv row=13 sum1/m=0.451 share=0.356
- P=241 worst row=217 share=0.646 U=48 holes=17 m_count=36 sum1/m=0.054 cap/U=0.750; maxInv row=10 sum1/m=0.505 share=0.422
- P=251 worst row=108 share=0.640 U=50 holes=18 m_count=39 sum1/m=0.107 cap/U=0.780; maxInv row=12 sum1/m=0.526 share=0.396
