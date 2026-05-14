# Prime Matrix square-phase low-alpha squarefree PDEC 符号取消路由

**状态：** `same_modulus_vertical_cancellation_blocked_cross_modulus_pairing_open`

本步把上一轮 concrete squarefree PDEC 包从 top16 抽样升级为全量阈值重算。样本中超过阈值的同一 `m` 纵向包一律同号且贡献值稳定，因此不能靠同一模数跨 `z` 自取消。实际小净余项来自同一 `z` 层内不同 `m` 的正负交叉配对。所以当前最窄点被压成：证明这种跨模数符号配对有统一纪律，或把未配对的同号持久模数族登记并排斥为 persistent squarefree PDEC。

```text
full_threshold_recomputation_done=true
same_modulus_vertical_cancellation_blocked_for_visible_repeated_packets=true
cross_modulus_signed_pairing_discipline_proved=false
persistent_squarefree_pdec_excluded=false
coefficient_cancellation_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全量阈值修正

| threshold | previous top16 packets | full packets | unique m | total abs |
| ---: | ---: | ---: | ---: | ---: |
| 20.000000 | 44 | 47 | 19 | 1663.929367 |

## 2. 同一 z 内的跨模数取消

| z | packets | positive abs | negative abs | signed | abs | signed/abs | cancellation ratio | threshold abs/all abs |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 4 | 68.321811 | 84.917915 | -16.596104 | 153.239725 | 0.108302 | 0.891698 | 0.584223 |
| 13 | 8 | 133.294909 | 162.932278 | -29.637369 | 296.227187 | 0.100049 | 0.899951 | 0.454747 |
| 31 | 16 | 286.326561 | 269.626432 | 16.700129 | 555.952993 | 0.030039 | 0.969961 | 0.297665 |
| 61 | 19 | 306.537365 | 351.972096 | -45.434731 | 658.509461 | 0.068996 | 0.931004 | 0.205031 |

## 3. 同一 m 的纵向持久包

| m | factors | z values | signs | signed | abs | self-cancel ratio | stable deviation |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 2 | `[2]` | `[7, 13, 31, 61]` | `----` | -253.422391 | 253.422391 | 1.000000 | 0.000000 |
| 3 | `[3]` | `[7, 13, 31, 61]` | `++++` | 161.151416 | 161.151416 | 1.000000 | 0.000000 |
| 17 | `[17]` | `[31, 61]` | `++` | 134.062925 | 134.062925 | 1.000000 | 0.000000 |
| 11 | `[11]` | `[13, 31, 61]` | `---` | -124.968975 | 124.968975 | 1.000000 | 0.000000 |
| 42 | `[2, 3, 7]` | `[7, 13, 31, 61]` | `++++` | 112.135826 | 112.135826 | 1.000000 | 0.000000 |
| 22 | `[2, 11]` | `[13, 31, 61]` | `---` | -109.074116 | 109.074116 | 1.000000 | 0.000000 |
| 13 | `[13]` | `[13, 31, 61]` | `+++` | 98.083364 | 98.083364 | 1.000000 | 0.000000 |
| 33 | `[3, 11]` | `[13, 31, 61]` | `+++` | 96.835931 | 96.835931 | 1.000000 | 0.000000 |
| 5 | `[5]` | `[7, 13, 31, 61]` | `----` | -86.249268 | 86.249268 | 1.000000 | 0.000000 |
| 38 | `[2, 19]` | `[31, 61]` | `++` | 64.489134 | 64.489134 | 1.000000 | 0.000000 |
| 34 | `[2, 17]` | `[31, 61]` | `--` | -62.933203 | 62.933203 | 1.000000 | 0.000000 |
| 29 | `[29]` | `[31, 61]` | `++` | 59.044776 | 59.044776 | 1.000000 | 0.000000 |
| 51 | `[3, 17]` | `[31, 61]` | `--` | -56.770107 | 56.770107 | 1.000000 | 0.000000 |
| 19 | `[19]` | `[31, 61]` | `--` | -48.754043 | 48.754043 | 1.000000 | 0.000000 |
| 23 | `[23]` | `[31, 61]` | `++` | 48.466469 | 48.466469 | 1.000000 | 0.000000 |
| 58 | `[2, 29]` | `[31, 61]` | `--` | -44.930954 | 44.930954 | 1.000000 | 0.000000 |
| 37 | `[37]` | `[61]` | `-` | -42.760355 | 42.760355 | 1.000000 | 0.000000 |
| 53 | `[53]` | `[61]` | `-` | -39.585309 | 39.585309 | 1.000000 | 0.000000 |
| 258 | `[2, 3, 43]` | `[61]` | `+` | 20.210804 | 20.210804 | 1.000000 | 0.000000 |

## 4. 已闭合的负结论与剩余硬点

- 已闭合/核验：全量阈值包为 `47` 个，而上一轮 top16 抽取只登记 `44` 个。
- 已闭合/核验：重复出现的可见 `m` 全部同号，且同一 `m` 的贡献在激活后稳定；同一模数纵向自取消不可用。
- 已观察：每个 `z` 层的总净值很小，取消来自不同 `m` 之间的正负配对。
- 未闭合：证明这种跨模数配对有结构性纪律，而不是样本巧合。
- 未闭合：若配对纪律失败，逐个排斥未配对的 same-sign persistent squarefree PDEC。
- 下一目标：`CrossModulusSignedPairingDisciplineOrPersistentSquarefreePDECExclusion`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.json` | `02307435c88ec3c3bf6ec5d6b27efaab05ef77f5a77ffbb0d731d7786c672bda` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_cancellation_router.py` | `1206bf36a587598914a06c4b424debd2b2304baf34203ee90c3bf4d218d50779` |
