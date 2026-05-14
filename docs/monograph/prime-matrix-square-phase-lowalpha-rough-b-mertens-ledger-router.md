# Prime Matrix square-phase low-alpha rough-b Mertens 账本路由

**状态：** `rough_b_dimension_one_mertens_ledger_materialized_selberg_pdec_open`

rough-b 幸存者账本与一维 Mertens 乘积高度对齐：对 cutoff y，模型为 `prime_a_fibers * prod_{ell<=y}(1-1/ell)`。默认样本中常数包覆盖聚合行与逐 P 行，说明该分支的自然筛维数是 1。当前仍未证明统一 Selberg 上界；若某 cutoff 的 rough-b 数量超过常数 Mertens 包络，则该 cutoff 直接给出低模粗数幸存者偏斜，进入 PDEC/SAE。

```text
rough_b_mertens_ledger_materialized=true
sample_constant_covers_aggregate_rows=true
sample_constant_covers_profile_rows=true
dimension_one_selberg_upper_proved=false
lowmod_rough_b_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 常数包

| constant | max aggregate ratio | aggregate failures | profile failures |
| ---: | ---: | ---: | ---: |
| 1.250000 | 1.058976 | 0 | 0 |

## 2. 聚合 Mertens 账本

| cutoff | rough | prime-a | Mertens product | model | rough/model | covered |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 7 | 9965 | 43666 | 0.228571 | 9980.800000 | 0.998417 | true |
| 13 | 8365 | 43666 | 0.191808 | 8375.496503 | 0.998747 | true |
| 31 | 6712 | 43666 | 0.152852 | 6674.442043 | 1.005627 | true |
| 61 | 5750 | 43666 | 0.131587 | 5745.893306 | 1.000715 | true |
| 99 | 99 | 777 | 0.120317 | 93.486535 | 1.058976 | true |
| 127 | 4740 | 42889 | 0.113866 | 4883.613496 | 0.970593 | true |
| 191 | 429 | 4013 | 0.105499 | 423.366431 | 1.013307 | true |
| 251 | 3764 | 38876 | 0.100353 | 3901.334745 | 0.964798 | true |
| 289 | 1025 | 10697 | 0.097792 | 1046.084356 | 0.979844 | true |
| 447 | 2620 | 28179 | 0.091337 | 2573.774300 | 1.017960 | true |

## 3. 每个 P 的最大比值

| P | prime-a | prime-b | max rough/model | failures |
| ---: | ---: | ---: | ---: | ---: |
| 10007 | 777 | 99 | 1.060909 | 0 |
| 36739 | 4013 | 429 | 1.018253 | 0 |
| 83561 | 10697 | 1025 | 0.988343 | 0 |
| 200003 | 28179 | 2620 | 1.017960 | 0 |

## 4. 证明边界

- 已物化：rough-b survivor 与一维 Mertens 乘积的聚合/逐 P 账本。
- 已闭合：给定常数包时，样本行自动分为 covered 或 LowMod-RoughB-PDEC。
- 未闭合：证明 reciprocal-floor b 多重序列满足统一维数一 Selberg 上界。
- 未闭合：排斥持久 LowMod-RoughB-PDEC/SAE。
- 下一目标：`DimensionOneRoughBReciprocalFloorSelbergUpperOrLowModPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-semiprime-incidence-router.json` | `074be8a7697fbbc1a38650c2b7296e0317915ba3cd4b1ec4ebedc79a45e265cc` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-prime-b-sieve-router.json` | `9d31214bd48757964376cf5d1255d145217506dde8481ca45530f8aa320eb482` |
| `experiments/prime_matrix_square_phase_lowalpha_rough_b_mertens_ledger_router.py` | `141d5e3cb7e7bd88cfb76a6fc3d083d3a544b92044afd263731e9f11ee50ff55` |
