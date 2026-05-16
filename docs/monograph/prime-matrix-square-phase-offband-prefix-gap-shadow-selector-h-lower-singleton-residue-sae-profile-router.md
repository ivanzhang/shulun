# Prime Matrix square-phase off-band prefix gap shadow selector H lower singleton-residue SAE profile router

**状态：** `singleton_residue_sae_profile_materialized_rankin_bound_open`

本步把 singleton residue 分支转成 SAE/Rankin 支撑剖面：当前 324 个物理事件中 300 个是 singleton residue packet，分布在 80 个 shape；样本 Rankin 质量 `sum 1/modulus` 为 4.328474。这只是剖面和账本，全局仍需证明该质量可求和，或排斥 transport reset-PDEC。

```text
physical_record_count=324
singleton_residue_packet_count=300
singleton_shape_count=80
singleton_certificate_size_histogram={'1': 257, '2': 43}
singleton_rankin_mass_total=4.328474445644
row_column_unconditional_closed=false
```

## 1. 高频 singleton shape

| shape | count | modulus | occupancy | Rankin mass | min margin |
| --- | ---: | --- | ---: | ---: | ---: |
| `size=1|side=minus|ells=71` | 22 | `[71]` | 0.309859 | 0.309859 | 25 |
| `size=1|side=minus|ells=61` | 13 | `[61]` | 0.213115 | 0.213115 | 15 |
| `size=1|side=minus|ells=43` | 12 | `[43]` | 0.279070 | 0.279070 | 16 |
| `size=1|side=minus|ells=101` | 12 | `[101]` | 0.118812 | 0.118812 | 44 |
| `size=1|side=minus|ells=53` | 11 | `[53]` | 0.207547 | 0.207547 | 21 |
| `size=1|side=plus|ells=79` | 11 | `[79]` | 0.139241 | 0.139241 | 36 |
| `size=1|side=minus|ells=89` | 11 | `[89]` | 0.123596 | 0.123596 | 26 |
| `size=1|side=minus|ells=97` | 11 | `[97]` | 0.113402 | 0.113402 | 27 |
| `size=1|side=minus|ells=59` | 10 | `[59]` | 0.169492 | 0.169492 | 17 |
| `size=1|side=minus|ells=67` | 10 | `[67]` | 0.149254 | 0.149254 | 23 |
| `size=1|side=minus|ells=79` | 10 | `[79]` | 0.126582 | 0.126582 | 36 |
| `size=1|side=minus|ells=83` | 10 | `[83]` | 0.120482 | 0.120482 | 37 |
| `size=1|side=minus|ells=73` | 9 | `[73]` | 0.123288 | 0.123288 | 29 |
| `size=1|side=minus|ells=41` | 8 | `[41]` | 0.195122 | 0.195122 | 17 |
| `size=1|side=plus|ells=61` | 8 | `[61]` | 0.131148 | 0.131148 | 12 |
| `size=1|side=minus|ells=37` | 7 | `[37]` | 0.189189 | 0.189189 | 13 |
| `size=1|side=minus|ells=47` | 7 | `[47]` | 0.148936 | 0.148936 | 12 |
| `size=1|side=plus|ells=37` | 6 | `[37]` | 0.162162 | 0.162162 | 26 |

## 2. 最大 Rankin 质量 shape

| shape | count | modulus | occupancy | Rankin mass | examples |
| --- | ---: | --- | ---: | ---: | --- |
| `size=1|side=minus|ells=71` | 22 | `[71]` | 0.309859 | 0.309859 | `[(4177, 59), (4217, 28), (4507, 34), (4517, 44)]` |
| `size=1|side=minus|ells=43` | 12 | `[43]` | 0.279070 | 0.279070 | `[(2137, 30), (2237, 1), (2417, 9), (2557, 20)]` |
| `size=1|side=minus|ells=61` | 13 | `[61]` | 0.213115 | 0.213115 | `[(3187, 15), (3677, 17), (3727, 6), (3877, 34)]` |
| `size=1|side=minus|ells=53` | 11 | `[53]` | 0.207547 | 0.207547 | `[(3137, 10), (3607, 3), (4297, 4), (4397, 51)]` |
| `size=1|side=minus|ells=41` | 8 | `[41]` | 0.195122 | 0.195122 | `[(2087, 37), (2657, 33), (3407, 4), (3517, 32)]` |
| `size=1|side=minus|ells=37` | 7 | `[37]` | 0.189189 | 0.189189 | `[(2027, 29), (2477, 35), (3347, 17), (4567, 16)]` |
| `size=1|side=minus|ells=59` | 10 | `[59]` | 0.169492 | 0.169492 | `[(3257, 12), (3527, 46), (3617, 18), (3947, 53)]` |
| `size=1|side=plus|ells=37` | 6 | `[37]` | 0.162162 | 0.162162 | `[(2917, 31), (3251, 32), (3359, 29), (3761, 24)]` |
| `size=1|side=minus|ells=31` | 5 | `[31]` | 0.161290 | 0.161290 | `[(2837, 16), (3467, 26), (3797, 15), (4327, 18)]` |
| `size=1|side=minus|ells=67` | 10 | `[67]` | 0.149254 | 0.149254 | `[(3967, 14), (5507, 13), (5657, 29), (5737, 42)]` |
| `size=1|side=minus|ells=47` | 7 | `[47]` | 0.148936 | 0.148936 | `[(2357, 7), (3457, 26), (3917, 16), (4967, 32)]` |
| `size=1|side=plus|ells=79` | 11 | `[79]` | 0.139241 | 0.139241 | `[(5639, 30), (5711, 23), (5717, 29), (6563, 6)]` |
| `size=1|side=plus|ells=61` | 8 | `[61]` | 0.131148 | 0.131148 | `[(3257, 24), (3347, 53), (3767, 46), (4229, 20)]` |
| `size=1|side=plus|ells=31` | 4 | `[31]` | 0.129032 | 0.129032 | `[(2767, 8), (4349, 9), (4817, 12), (6569, 28)]` |
| `size=1|side=plus|ells=47` | 6 | `[47]` | 0.127660 | 0.127660 | `[(2063, 42), (2347, 44), (3797, 37), (3967, 19)]` |
| `size=1|side=minus|ells=79` | 10 | `[79]` | 0.126582 | 0.126582 | `[(5197, 62), (5387, 15), (6197, 35), (6977, 25)]` |
| `size=1|side=minus|ells=89` | 11 | `[89]` | 0.123596 | 0.123596 | `[(7307, 9), (7507, 31), (7727, 73), (8117, 18)]` |
| `size=1|side=minus|ells=73` | 9 | `[73]` | 0.123288 | 0.123288 | `[(4337, 30), (4457, 4), (5867, 27), (5987, 1)]` |

## 3. 最紧 singleton 记录

| p | side | rho | shape | modulus | residue | margin | CRT-width | weight |
| ---: | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 2347 | `plus` | 7 | `size=1|side=plus|ells=47` | 47 | 44 | 12 | 11 | 0.021277 |
| 5297 | `minus` | 2 | `size=1|side=minus|ells=47` | 47 | 33 | 12 | 21 | 0.021277 |
| 3767 | `plus` | 2 | `size=1|side=plus|ells=61` | 61 | 46 | 12 | 25 | 0.016393 |
| 2243 | `plus` | 2 | `size=2|side=plus|ells=17,19` | 323 | 305 | 12 | 306 | 0.003096 |
| 2027 | `minus` | 2 | `size=1|side=minus|ells=37` | 37 | 29 | 13 | 12 | 0.027027 |
| 2063 | `plus` | 2 | `size=1|side=plus|ells=47` | 47 | 42 | 13 | 19 | 0.021277 |
| 2927 | `minus` | 2 | `size=2|side=minus|ells=37,43` | 1591 | 1336 | 13 | 1431 | 0.000629 |
| 2267 | `minus` | 2 | `size=2|side=minus|ells=47,31` | 1457 | 810 | 14 | 1405 | 0.000686 |
| 5407 | `minus` | 7 | `size=1|side=minus|ells=29` | 29 | 13 | 15 | 3 | 0.034483 |
| 2687 | `minus` | 2 | `size=1|side=minus|ells=29` | 29 | 19 | 15 | 4 | 0.034483 |
| 2837 | `minus` | 2 | `size=1|side=minus|ells=31` | 31 | 16 | 15 | 8 | 0.032258 |
| 4007 | `minus` | 2 | `size=1|side=minus|ells=61` | 61 | 42 | 15 | 31 | 0.016393 |
| 2207 | `minus` | 2 | `size=2|side=minus|ells=43,23` | 989 | 229 | 15 | 906 | 0.001011 |
| 2297 | `minus` | 2 | `size=2|side=minus|ells=23,43` | 989 | 319 | 15 | 955 | 0.001011 |
| 2647 | `minus` | 7 | `size=2|side=minus|ells=37,31` | 1147 | 353 | 15 | 1117 | 0.000872 |
| 4567 | `minus` | 7 | `size=1|side=minus|ells=37` | 37 | 16 | 16 | 13 | 0.027027 |
| 2137 | `minus` | 7 | `size=1|side=minus|ells=43` | 43 | 30 | 16 | 19 | 0.023256 |
| 2087 | `minus` | 2 | `size=1|side=minus|ells=41` | 41 | 37 | 17 | 11 | 0.024390 |

## 4. 结构判断

- singleton residue packet 当前没有复现，适合进入 SAE/Rankin 支撑求和。
- 低模一槽 shape 给出主要 Rankin 质量；二槽 shape 的模数较大，权重自然较小。
- 当前仍只是样本剖面，必须补全全局质量上界才可闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `singleton_residue_profile_materialized` | `closed` | All non-recurrent residue packets are materialized with CRT modulus, Rankin weight, shape, and margin data. |
| `current_sweep_singletons_are_residue_nonpersistent` | `closed_on_current_sweep` | Every singleton residue packet has multiplicity one in the current physical sweep. |
| `singleton_residue_rankin_summability_open` | `open` | A global proof must bound the singleton residue Rankin mass or route exceptional reset atoms to PDEC. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SingletonResidueProfileMaterialized` | `true` | `true` | singleton residue 事件已逐项带 CRT 模数和 Rankin 权重登记。 | closed |
| `CurrentSingletonNonPersistenceClosed` | `true` | `false` | 当前扫描中这些 residue packet 均未复现。 | finite evidence only |
| `RankinMassBoundProved` | `false` | `false` | Rankin 质量已物化但尚未给出全局上界。 | SingletonResidueRankinMassBound |
| `TransportResetPDECExcluded` | `false` | `false` | transport reset-PDEC 仍需全局排斥。 | TransportResetPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步是 SAE/Rankin 剖面，不关闭全局命题。 | SingletonResidueRankinMassBoundOrTransportResetPDECExclusion |

## 7. 下一步

- 主攻：`SingletonResidueRankinMassBoundOrTransportResetPDECExclusion`。
- 证明 singleton Rankin 质量全局可求和，或排斥 transport reset-PDEC。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py` | `b0c8c4981326d393ce93cd7256bb00ef2ee55eda8d87f8649bdad67cebcd12bd` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_two_slot_normal_form_router.py` | `235a88162fc76a089f99156ebbc167cec3c3e43c7e00c2e99addcab467b88d09` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json` | `2b7ba1295e2d498da7265aa73d7e39b6a5add3a31ae60f947b4fbc4cf212b373` |
