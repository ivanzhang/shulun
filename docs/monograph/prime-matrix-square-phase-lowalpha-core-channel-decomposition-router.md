# Prime Matrix square-phase low-alpha core 通道分解

**状态：** `core_mobius_log_channel_decomposition_closed_channel_bounds_open`

核心系数公式可继续展开为通道恒等式 `core=S0-(log D)^(-2) sum_{q<=z} (log q)^2 S_q`，其中 `S0=sum_{m<=D} mu(m)R_m`，`S_q=sum_{m<=D,q|m} mu(m)R_m`。因此 core 角度失败不会是无名高维异常：它必须由 `S0` 或某些素数 log-square 通道承担，可登记为 PrimeChannel-VectorSquarefree-PDEC。

```text
core_channel_decomposition_identity_closed=true
prime_channel_pdec_route_materialized=true
S0_channel_bound_proved=false
prime_log_square_channel_bound_proved=false
core_mobius_log_residual_angle_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 通道恒等式

| z | S0 | log-square sum | core net | error | channel abs | |core|/channel abs | channel cancellation |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | -15.800000 | 1.569282 | -17.369282 | 0.000000 | 3.459136 | 5.021277 | 0.453663 |
| 13 | -12.517016 | 3.909590 | -16.426607 | -0.000000 | 11.703411 | 1.403574 | 0.334056 |
| 31 | 26.857515 | 12.233746 | 14.623769 | -0.000000 | 23.256973 | 0.628791 | 0.526025 |
| 61 | 31.728535 | 22.400745 | 9.327790 | -0.000000 | 69.684549 | 0.133857 | 0.321459 |

## 2. 最大素数通道

| z | q | S_q | weight | weighted term |
| ---: | ---: | ---: | ---: | ---: |
| 7 | 3 | 99.400000 | 0.025294 | 2.514209 |
| 7 | 5 | -8.800000 | 0.054284 | -0.477702 |
| 7 | 2 | -42.200000 | 0.010069 | -0.424903 |
| 7 | 7 | -0.533333 | 0.079355 | -0.042322 |
| 13 | 13 | 29.034499 | 0.137874 | 4.003115 |
| 13 | 11 | -23.465734 | 0.120500 | -2.827618 |
| 13 | 3 | 77.641026 | 0.025294 | 1.963841 |
| 13 | 7 | 23.181352 | 0.079355 | 1.839545 |
| 13 | 2 | -54.411655 | 0.010069 | -0.547859 |
| 13 | 5 | -9.605594 | 0.054284 | -0.521433 |
| 31 | 17 | 35.370315 | 0.168223 | 5.950091 |
| 31 | 13 | 30.210975 | 0.137874 | 4.165321 |
| 31 | 31 | -12.926592 | 0.247129 | -3.194534 |
| 31 | 19 | 12.918056 | 0.181690 | 2.347083 |
| 31 | 11 | -17.109381 | 0.120500 | -2.061678 |
| 31 | 29 | 7.376737 | 0.237623 | 1.752883 |
| 61 | 43 | -39.137870 | 0.296469 | -11.603157 |
| 61 | 47 | 26.122875 | 0.310657 | 8.115249 |
| 61 | 61 | 20.479353 | 0.354156 | 7.252883 |
| 61 | 59 | 18.953230 | 0.348435 | 6.603973 |
| 61 | 17 | 29.451166 | 0.168223 | 4.954355 |
| 61 | 53 | -14.421654 | 0.330347 | -4.764157 |

## 3. 证明边界

- 已闭合：core 通道恒等式。
- 已物化：若 core 角度失败，则必须落入 `S0` 或某个 `S_q` 素数通道。
- 未闭合：`S0` 通道统一界。
- 未闭合：逐素数 log-square 通道统一界或失败 PDEC 排斥。
- 下一目标：`CoreChannelS0AndPrimeLogSquareChannelBoundsOrVectorPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json` | `e9ae5080e5df364181f29c6acdff03bdb8259181f99065df89405a98be3fa2fd` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `experiments/prime_matrix_square_phase_lowalpha_core_channel_decomposition_router.py` | `a1db8b7b6c0691b63893c8f21045db2cb95ab0cc27b6a7f42b6e7a224c41a9cc` |
