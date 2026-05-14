# Prime Matrix square-phase low-alpha VectorSquarefree-PDEC 统一义务

**状态：** `unified_vector_pdec_obligations_materialized_bounds_open`

core 的 `S0/S_q` 通道与 tail 的 low-overflow `(d,e)` 边界通道现在共用同一个 VectorSquarefree-PDEC 义务格式：每个义务都有 family、z、label、样本尺度与待证明界。这一步不证明排斥，但切断了继续分叉：剩余只需证明 Möbius divisor-sum 通道界、boundary lcm edge 界，或排斥统一的 VectorSquarefree-PDEC。

```text
unified_vector_pdec_obligation_schema_closed=true
core_channel_obligations_imported=true
low_overflow_edge_obligations_imported=true
mobius_divisor_sum_channel_bounds_proved=false
boundary_lcm_edge_bounds_proved=false
unified_vector_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 家族汇总

| family | obligations | total sample scale | max sample scale | sample labels |
| --- | ---: | ---: | ---: | --- |
| `CoprimeBoundaryLCMEdge` | 3 | 2851.857024 | 1887.557718 | `['coprime-boundary-edge(z=13)', 'coprime-boundary-edge(z=31)', 'coprime-boundary-edge(z=61)']` |
| `SmallGCDOverflowEdge` | 3 | 1957.033048 | 1192.425987 | `['small-gcd-overflow-edge(z=13)', 'small-gcd-overflow-edge(z=31)', 'small-gcd-overflow-edge(z=61)']` |
| `PrimeLogSquareChannel` | 26 | 89.033836 | 11.603157 | `['S_q(z=7,q=3)', 'S_q(z=7,q=5)', 'S_q(z=7,q=2)', 'S_q(z=7,q=7)', 'S_q(z=13,q=13)', 'S_q(z=13,q=11)', 'S_q(z=13,q=3)', 'S_q(z=13,q=7)']` |
| `CoreS0MobiusDivisorSum` | 4 | 86.903067 | 31.728535 | `['S0(z=7)', 'S0(z=13)', 'S0(z=31)', 'S0(z=61)']` |

## 2. 最大义务

| family | z | label | sample signed | sample scale | sample ratio |
| --- | ---: | --- | ---: | ---: | ---: |
| `CoprimeBoundaryLCMEdge` | 61 | `coprime-boundary-edge(z=61)` | -14.077683 | 1887.557718 | 0.612847 |
| `SmallGCDOverflowEdge` | 61 | `small-gcd-overflow-edge(z=61)` | 11.653945 | 1192.425987 | 0.387153 |
| `CoprimeBoundaryLCMEdge` | 31 | `coprime-boundary-edge(z=31)` | 19.219154 | 898.291025 | 0.563130 |
| `SmallGCDOverflowEdge` | 31 | `small-gcd-overflow-edge(z=31)` | -15.834942 | 696.883291 | 0.436870 |
| `SmallGCDOverflowEdge` | 13 | `small-gcd-overflow-edge(z=13)` | -4.250646 | 67.723770 | 0.506414 |
| `CoprimeBoundaryLCMEdge` | 13 | `coprime-boundary-edge(z=13)` | 5.950220 | 66.008281 | 0.493586 |
| `CoreS0MobiusDivisorSum` | 61 | `S0(z=61)` | 31.728535 | 31.728535 | 0.133857 |
| `CoreS0MobiusDivisorSum` | 31 | `S0(z=31)` | 26.857515 | 26.857515 | 0.628791 |
| `CoreS0MobiusDivisorSum` | 7 | `S0(z=7)` | -15.800000 | 15.800000 | 5.021277 |
| `CoreS0MobiusDivisorSum` | 13 | `S0(z=13)` | -12.517016 | 12.517016 | 1.403574 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=43)` | -39.137870 | 11.603157 | 0.166510 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=47)` | 26.122875 | 8.115249 | 0.116457 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=61)` | 20.479353 | 7.252883 | 0.104082 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=59)` | 18.953230 | 6.603973 | 0.094770 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=17)` | 35.370315 | 5.950091 | 0.255841 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=17)` | 29.451166 | 4.954355 | 0.071097 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=53)` | -14.421654 | 4.764157 | 0.068367 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=13)` | 30.210975 | 4.165321 | 0.179100 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=37)` | -14.931538 | 4.080054 | 0.058550 |
| `PrimeLogSquareChannel` | 13 | `S_q(z=13,q=13)` | 29.034499 | 4.003115 | 0.342047 |
| `PrimeLogSquareChannel` | 61 | `S_q(z=61,q=13)` | 27.943112 | 3.852640 | 0.055287 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=31)` | -12.926592 | 3.194534 | 0.137358 |
| `PrimeLogSquareChannel` | 13 | `S_q(z=13,q=11)` | -23.465734 | 2.827618 | 0.241606 |
| `PrimeLogSquareChannel` | 7 | `S_q(z=7,q=3)` | 99.400000 | 2.514209 | 0.726831 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=19)` | 12.918056 | 2.347083 | 0.100920 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=11)` | -17.109381 | 2.061678 | 0.088648 |
| `PrimeLogSquareChannel` | 13 | `S_q(z=13,q=3)` | 77.641026 | 1.963841 | 0.167801 |
| `PrimeLogSquareChannel` | 13 | `S_q(z=13,q=7)` | 23.181352 | 1.839545 | 0.157180 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=29)` | 7.376737 | 1.752883 | 0.075370 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=23)` | 8.495765 | 1.750413 | 0.075264 |
| `PrimeLogSquareChannel` | 31 | `S_q(z=31,q=7)` | 17.929895 | 1.422818 | 0.061178 |
| `PrimeLogSquareChannel` | 13 | `S_q(z=13,q=2)` | -54.411655 | 0.547859 | 0.046812 |

## 3. 证明边界

- 已闭合：统一 VectorSquarefree-PDEC 义务格式。
- 已导入：core channel 与 low-overflow edge 两类剩余。
- 未闭合：Möbius divisor-sum 通道界。
- 未闭合：boundary lcm edge 角度界。
- 未闭合：统一 VectorSquarefree-PDEC 排斥。
- 下一目标：`MöbiusDivisorSumChannelBoundsAndBoundaryLCMEdgeBoundsOrUnifiedVectorPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json` | `e9ae5080e5df364181f29c6acdff03bdb8259181f99065df89405a98be3fa2fd` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-core-channel-decomposition-router.json` | `4348332181b6fec385f3475caa9333f8521b56e2705bdc610dc87e908fa5e230` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-low-overflow-edge-profile-router.json` | `586cbd19ff15c98e5c81dc5b0448d76c781b47b7855dacd241c292150e7a94ae` |
| `experiments/prime_matrix_square_phase_lowalpha_vector_pdec_unified_obligation_router.py` | `3156c1e1aefa9124f5dbcbd39bf24634103dd67db9d9a47e5ff5635f9158ad9c` |
