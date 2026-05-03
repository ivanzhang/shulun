# 前 P 行高度受限最小因子链扫描

**状态：** `front_window_has_prime_gaps_in_every_sampled_row_and_height_limited_factor_chain`

前 P 行的高度受限最小因子链与 CRT 远处零行不同：采样行均有素数洞，且大最小因子标签数量受高度约束。下一步应将“若 prime_count=0”时最小因子链必须异常密集这一点不等式化。

## 摘要
- P=23
  - r=1 primes=9 comp=13 big_min=0 max_factor=3 gaps=[(2, 6), (1, 6)]
  - r=2 primes=5 comp=17 big_min=2 max_factor=5 gaps=[(1, 11), (2, 5)]
  - r=5 primes=6 comp=16 big_min=1 max_factor=5 gaps=[(1, 9), (2, 6)]
  - r=11 primes=4 comp=18 big_min=3 max_factor=13 gaps=[(1, 13), (2, 4)]
  - r=17 primes=4 comp=18 big_min=3 max_factor=13 gaps=[(1, 13), (2, 4)]
  - r=23 primes=3 comp=19 big_min=4 max_factor=17 gaps=[(1, 15), (2, 3)]
- P=101
  - r=1 primes=26 comp=74 big_min=0 max_factor=7 gaps=[(1, 50), (2, 23)]
  - r=2 primes=20 comp=80 big_min=4 max_factor=13 gaps=[(1, 59), (2, 20)]
  - r=25 primes=9 comp=91 big_min=13 max_factor=47 gaps=[(1, 81), (2, 9)]
  - r=50 primes=14 comp=86 big_min=8 max_factor=71 gaps=[(1, 71), (2, 14)]
  - r=75 primes=16 comp=84 big_min=7 max_factor=73 gaps=[(1, 67), (2, 16)]
  - r=101 primes=12 comp=88 big_min=10 max_factor=73 gaps=[(1, 75), (2, 12)]
- P=211
  - r=1 primes=47 comp=163 big_min=0 max_factor=13 gaps=[(1, 118), (2, 44)]
  - r=2 primes=35 comp=175 big_min=4 max_factor=19 gaps=[(1, 140), (2, 34)]
  - r=52 primes=20 comp=190 big_min=20 max_factor=101 gaps=[(1, 169), (2, 20)]
  - r=105 primes=24 comp=186 big_min=15 max_factor=127 gaps=[(1, 161), (2, 24)]
  - r=158 primes=18 comp=192 big_min=22 max_factor=167 gaps=[(1, 173), (2, 18)]
  - r=211 primes=15 comp=195 big_min=27 max_factor=199 gaps=[(1, 179), (2, 15)]
- P=401
  - r=1 primes=79 comp=321 big_min=0 max_factor=19 gaps=[(1, 244), (2, 76)]
  - r=2 primes=60 comp=340 big_min=3 max_factor=23 gaps=[(1, 279), (2, 60)]
  - r=100 primes=40 comp=360 big_min=33 max_factor=179 gaps=[(1, 320), (2, 39)]
  - r=200 primes=39 comp=361 big_min=31 max_factor=283 gaps=[(1, 321), (2, 39)]
  - r=300 primes=35 comp=365 big_min=33 max_factor=317 gaps=[(1, 330), (2, 34)]
  - r=401 primes=36 comp=364 big_min=35 max_factor=383 gaps=[(1, 327), (2, 36)]
- P=809
  - r=1 primes=140 comp=668 big_min=0 max_factor=23 gaps=[(1, 530), (2, 137)]
  - r=2 primes=115 comp=693 big_min=15 max_factor=37 gaps=[(1, 577), (2, 115)]
  - r=202 primes=73 comp=735 big_min=63 max_factor=389 gaps=[(1, 662), (2, 72)]
  - r=404 primes=58 comp=750 big_min=74 max_factor=571 gaps=[(1, 691), (2, 58)]
  - r=606 primes=65 comp=743 big_min=66 max_factor=691 gaps=[(1, 677), (2, 65)]
  - r=809 primes=63 comp=745 big_min=67 max_factor=797 gaps=[(1, 681), (2, 63)]

## 下一证明义务
- 假设 prime_count=0，估计最小因子标签链的必要覆盖密度。
- 利用 p_c<=sqrt(n)<P 和商 m_c<n/p_c 建立递归高度约束。
- 比较前窗口链与 P=23,r=59 这类远处零行链的差异。
