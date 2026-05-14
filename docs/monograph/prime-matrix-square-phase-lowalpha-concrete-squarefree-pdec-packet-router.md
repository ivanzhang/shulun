# Prime Matrix square-phase low-alpha concrete squarefree PDEC 包路由

**状态：** `concrete_squarefree_pdec_packets_extracted_exclusion_open`

Selberg 余项若不能由统一系数 L1 预算吸收，失败不再是抽象余项：它必须落到具体的 squarefree 低模包 `ConcreteSquarefreeLowModPDEC(z,m)`。本路由从归因账本中抽取贡献量超过阈值的包，列出重复出现的模数和贡献方向。下一步可二选一：证明这些包的符号取消/系数预算，或逐个排斥具体 PDEC。

```text
concrete_squarefree_pdec_packets_materialized=true
coefficient_cancellation_bound_proved=false
concrete_squarefree_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 包总览

| threshold | packets | unique m | total abs contribution |
| ---: | ---: | ---: | ---: |
| 20.000000 | 44 | 18 | 1599.690769 |

## 2. 最大贡献包

| z | m | coefficient | actual | expected | remainder | contribution | actual/expected | label |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 17 | -0.831777 | 2488 | 2568.588235 | -80.588235 | 67.031463 | 0.968625 | `ConcreteSquarefreeLowModPDEC(z=31,m=17)` |
| 61 | 17 | -0.831777 | 2488 | 2568.588235 | -80.588235 | 67.031463 | 0.968625 | `ConcreteSquarefreeLowModPDEC(z=61,m=17)` |
| 7 | 2 | -0.989931 | 21897 | 21833.000000 | 64.000000 | -63.355598 | 1.002931 | `ConcreteSquarefreeLowModPDEC(z=7,m=2)` |
| 13 | 2 | -0.989931 | 21897 | 21833.000000 | 64.000000 | -63.355598 | 1.002931 | `ConcreteSquarefreeLowModPDEC(z=13,m=2)` |
| 31 | 2 | -0.989931 | 21897 | 21833.000000 | 64.000000 | -63.355598 | 1.002931 | `ConcreteSquarefreeLowModPDEC(z=31,m=2)` |
| 61 | 2 | -0.989931 | 21897 | 21833.000000 | 64.000000 | -63.355598 | 1.002931 | `ConcreteSquarefreeLowModPDEC(z=61,m=2)` |
| 61 | 37 | -0.726749 | 1239 | 1180.162162 | 58.837838 | -42.760355 | 1.049856 | `ConcreteSquarefreeLowModPDEC(z=61,m=37)` |
| 13 | 11 | -0.879500 | 4017 | 3969.636364 | 47.363636 | -41.656325 | 1.011931 | `ConcreteSquarefreeLowModPDEC(z=13,m=11)` |
| 31 | 11 | -0.879500 | 4017 | 3969.636364 | 47.363636 | -41.656325 | 1.011931 | `ConcreteSquarefreeLowModPDEC(z=31,m=11)` |
| 61 | 11 | -0.879500 | 4017 | 3969.636364 | 47.363636 | -41.656325 | 1.011931 | `ConcreteSquarefreeLowModPDEC(z=61,m=11)` |
| 7 | 3 | -0.974706 | 14514 | 14555.333333 | -41.333333 | 40.287854 | 0.997160 | `ConcreteSquarefreeLowModPDEC(z=7,m=3)` |
| 13 | 3 | -0.974706 | 14514 | 14555.333333 | -41.333333 | 40.287854 | 0.997160 | `ConcreteSquarefreeLowModPDEC(z=13,m=3)` |
| 31 | 3 | -0.974706 | 14514 | 14555.333333 | -41.333333 | 40.287854 | 0.997160 | `ConcreteSquarefreeLowModPDEC(z=31,m=3)` |
| 61 | 3 | -0.974706 | 14514 | 14555.333333 | -41.333333 | 40.287854 | 0.997160 | `ConcreteSquarefreeLowModPDEC(z=61,m=3)` |
| 61 | 53 | -0.669653 | 883 | 823.886792 | 59.113208 | -39.585309 | 1.071749 | `ConcreteSquarefreeLowModPDEC(z=61,m=53)` |
| 13 | 22 | 0.869431 | 1943 | 1984.818182 | -41.818182 | -36.358039 | 0.978931 | `ConcreteSquarefreeLowModPDEC(z=13,m=22)` |
| 31 | 22 | 0.869431 | 1943 | 1984.818182 | -41.818182 | -36.358039 | 0.978931 | `ConcreteSquarefreeLowModPDEC(z=31,m=22)` |
| 61 | 22 | 0.869431 | 1943 | 1984.818182 | -41.818182 | -36.358039 | 0.978931 | `ConcreteSquarefreeLowModPDEC(z=61,m=22)` |
| 13 | 13 | -0.862126 | 3321 | 3358.923077 | -37.923077 | 32.694455 | 0.988710 | `ConcreteSquarefreeLowModPDEC(z=13,m=13)` |
| 31 | 13 | -0.862126 | 3321 | 3358.923077 | -37.923077 | 32.694455 | 0.988710 | `ConcreteSquarefreeLowModPDEC(z=31,m=13)` |
| 61 | 13 | -0.862126 | 3321 | 3358.923077 | -37.923077 | 32.694455 | 0.988710 | `ConcreteSquarefreeLowModPDEC(z=61,m=13)` |
| 13 | 33 | 0.854206 | 1361 | 1323.212121 | 37.787879 | 32.278644 | 1.028558 | `ConcreteSquarefreeLowModPDEC(z=13,m=33)` |
| 31 | 33 | 0.854206 | 1361 | 1323.212121 | 37.787879 | 32.278644 | 1.028558 | `ConcreteSquarefreeLowModPDEC(z=31,m=33)` |
| 61 | 33 | 0.854206 | 1361 | 1323.212121 | 37.787879 | 32.278644 | 1.028558 | `ConcreteSquarefreeLowModPDEC(z=61,m=33)` |

## 3. 重复模数

| m | z values | packet count | total abs | max abs |
| ---: | --- | ---: | ---: | ---: |
| 2 | `[7, 13, 31, 61]` | 4 | 253.422391 | 63.355598 |
| 3 | `[7, 13, 31, 61]` | 4 | 161.151416 | 40.287854 |
| 17 | `[31, 61]` | 2 | 134.062925 | 67.031463 |
| 11 | `[13, 31, 61]` | 3 | 124.968975 | 41.656325 |
| 42 | `[7, 13, 31, 61]` | 4 | 112.135826 | 28.033957 |
| 22 | `[13, 31, 61]` | 3 | 109.074116 | 36.358039 |
| 13 | `[13, 31, 61]` | 3 | 98.083364 | 32.694455 |
| 33 | `[13, 31, 61]` | 3 | 96.835931 | 32.278644 |
| 5 | `[7, 13, 31]` | 3 | 64.686951 | 21.562317 |
| 38 | `[31, 61]` | 2 | 64.489134 | 32.244567 |
| 34 | `[31, 61]` | 2 | 62.933203 | 31.466602 |
| 29 | `[31, 61]` | 2 | 59.044776 | 29.522388 |
| 51 | `[31, 61]` | 2 | 56.770107 | 28.385054 |
| 19 | `[31, 61]` | 2 | 48.754043 | 24.377022 |
| 23 | `[31, 61]` | 2 | 48.466469 | 24.233234 |
| 37 | `[61]` | 1 | 42.760355 | 42.760355 |

## 4. 证明边界

- 已物化：Selberg 余项的具体 squarefree 低模 PDEC 包。
- 未闭合：证明这些包按系数符号取消，或证明总系数 L1 预算。
- 未闭合：逐个排斥持久 `ConcreteSquarefreeLowModPDEC(z,m)`。
- 下一目标：`ConcreteSquarefreePDECExclusionOrCoefficientCancellationBound`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json` | `e3fd8819110a576f1a5ea953b553ef1acb3493a6c7b8b8d6b2c7644d99b4b77c` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `experiments/prime_matrix_square_phase_lowalpha_concrete_squarefree_pdec_packet_router.py` | `821602cd1386344236f97492dd2fc2f4b61127924c9cc80e567c63eb96290b02` |
