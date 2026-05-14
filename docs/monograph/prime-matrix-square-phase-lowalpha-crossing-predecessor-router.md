# Prime Matrix square-phase low-alpha crossing 前驱路由

**状态：** `crossing_prefix_distribution_reduced_to_predecessor_short_hyperbola_open`

crossing 前缀分布已改写为前驱 `D_-` 的短双曲区间：`P^2/D_- < r*t <= (P^2+P-1)/D_-`，长度为 `P/D_-`，其中 `r` 是跨越素因子，尾因子 `t` 为 `r`-rough。所以持续过载不能再隐藏在单个 crossing key 内，只能表现为前驱集合上的短区间分布过密或 PDEC。

```text
predecessor_short_hyperbola_formula_closed=true
crossing_bracket_checked=true
tail_roughness_checked=true
predecessor_distribution_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 最坏 low-alpha 块

| P | block | hits | active D_- | max hits/D_- | top D_- | width sum | hits/width | max width | top width bucket |
| ---: | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| 200003 | `(31,62]` | 4540 | 1173 | 362 | `37` | 44995.740721 | 0.100898 | 5405.486486 | `W7:>=128` |

## 2. 每个 P 的总结

| P | low blocks | total hits | worst block | worst D_- count | top width bucket |
| ---: | ---: | ---: | --- | ---: | --- |
| 10007 | 2 | 412 | `(31,62]` | 58 | `W7:>=128` |
| 36739 | 3 | 2040 | `(31,62]` | 267 | `W7:>=128` |
| 83561 | 4 | 5659 | `(31,62]` | 560 | `W7:>=128` |
| 200003 | 4 | 13393 | `(31,62]` | 1173 | `W7:>=128` |

## 3. 证明边界

- 已闭合：crossing 前驱短双曲区间公式。
- 已闭合：tail `t` 继承 `r`-rough 性质。
- 未闭合：`PredecessorShortHyperbolaDistributionBoundOrPDEC`，即对全部前驱 `D_-` 的短区间 rough-prime 对分布上界，或失败形成 PDEC。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-crossing-capacity-router.json` | `f041774be8b186cc7b89abf5a43c029d0fb27ca2b6eadb5077e5969d37e9813d` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-first-anchor-interval-router.json` | `c137e604c7b0d9a24ec7a9c15d77aecf2753760fdc7554398202948aed341bc7` |
| `experiments/prime_matrix_square_phase_lowalpha_crossing_predecessor_router.py` | `e33af62ee820906f21dad864de2f59245c29db53f3350fbc2e3da5aa70b66db0` |
