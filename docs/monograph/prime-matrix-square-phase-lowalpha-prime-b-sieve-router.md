# Prime Matrix square-phase low-alpha prime-b 粗数筛路由

**状态：** `prime_b_layer_reduced_to_rough_b_sieve_on_reciprocal_floor_sequence_open`

prime-b 层已经退化为 prime-a 半素数 incidence 多重序列上的粗数筛：对每条候选 `(q,a,b)`，是否贡献最终 semiprime-u 只取决于 b 是否为素数，而这等价于 b 没有不超过 sqrt(b) 的素因子。样本中 sqrt(b) 筛与直接素性判断完全一致。因此剩余不再是纤维几何，而是 reciprocal-floor 生成的 b 多重序列的粗数幸存者上界；若粗幸存者无法由 Selberg/Rankin 支付，则必须输出低模粗数偏斜 PDEC/SAE。

```text
sqrt_sieve_prime_b_identity_closed=true
rough_b_sieve_ledger_materialized=true
uniform_rough_b_selberg_rankin_bound_proved=false
rough_b_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 全局账本

| prime-a fibers | prime-b fibers | prime-b/prime-a | sqrt-sieve failures |
| ---: | ---: | ---: | ---: |
| 43666 | 4173 | 0.095566 | 0 |

## 2. 聚合粗数筛

| cutoff | rough count | covered prime-a | covered prime-b | rough/prime-a | prime-b/rough |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 9965 | 43666 | 4173 | 0.228210 | 0.418766 |
| 13 | 8365 | 43666 | 4173 | 0.191568 | 0.498864 |
| 31 | 6712 | 43666 | 4173 | 0.153712 | 0.621722 |
| 61 | 5750 | 43666 | 4173 | 0.131681 | 0.725739 |
| 99 | 99 | 777 | 99 | 0.127413 | 1.000000 |
| 127 | 4740 | 42889 | 4074 | 0.110518 | 0.859494 |
| 191 | 429 | 4013 | 429 | 0.106903 | 1.000000 |
| 251 | 3764 | 38876 | 3645 | 0.096821 | 0.968385 |
| 289 | 1025 | 10697 | 1025 | 0.095821 | 1.000000 |
| 447 | 2620 | 28179 | 2620 | 0.092977 | 1.000000 |

## 3. 每个 P 的总结

| P | prime-a | prime-b | max b | sqrt max b | sqrt rough | failures |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 777 | 99 | 9996 | 99 | 99 | 0 |
| 36739 | 4013 | 429 | 36716 | 191 | 429 | 0 |
| 83561 | 10697 | 1025 | 83554 | 289 | 1025 | 0 |
| 200003 | 28179 | 2620 | 199986 | 447 | 2620 | 0 |

## 4. 证明边界

- 已闭合：在 prime-a incidence 多重序列上，`b` 为素数等价于 `sqrt(b)` 粗。
- 已物化：多个低模 cutoff 下的 rough-b 幸存者账本。
- 未闭合：对 reciprocal-floor 生成的 b 序列给出统一 Selberg/Rankin 粗数幸存者上界。
- 未闭合：若低模粗数幸存者持续过多，需形成并排斥 PDEC/SAE。
- 下一目标：`RoughBReciprocalFloorSelbergRankinOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-fixed-b-semiprime-incidence-router.json` | `074be8a7697fbbc1a38650c2b7296e0317915ba3cd4b1ec4ebedc79a45e265cc` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-semiprime-phase-sawtooth-router.json` | `6f41d62e64c519dcede5d9341dbff6c628034cbdd3814b2cd1a8234b0f4e2ed8` |
| `experiments/prime_matrix_square_phase_lowalpha_prime_b_sieve_router.py` | `aa963b3aaf8e8c5d973d2cc527a87184933cdd782dc543691d52eefbd22b0de5` |
