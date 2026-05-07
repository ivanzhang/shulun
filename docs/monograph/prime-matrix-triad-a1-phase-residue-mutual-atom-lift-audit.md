# Triad-A1 PhaseResidueMutual 原子提升审计

**状态：** `phase_residue_mutual_atoms_lifted_to_next_layer_routes`

当前所有已抽取互信息原子都满足提升层质量恒等式。已有下一层数据的原子分裂为 CleanFiberCandidate 与 RefinedPDECEntropy；没有出现无名第四路线。

## 1. 结构律

PhaseResidueMutual atom (t,b) maps exactly to new phase u=t+bQ mod Q'. Next layer either deletes u, leaves a refined KL peak on u's fiber, or flattens u toward CleanKLS.

```text
(old phase t, residue b)  <=>  new phase u=t+bQ mod Q'。
```

所以互信息峰不是新终端；它在提升层只是普通相位原子。下一层只能删除、继续偏斜、或趋平。

## 2. 参数

- `deletion_support_threshold=0.5`。
- `pdec_normalized_kl_threshold=0.2`。
- `clean_normalized_kl_threshold=0.05`。
- `threshold_meaning=阈值只用于有限审计分流；结构结论是 u=t+bQ 的原子提升恒等式。`。

## 3. 汇总

- `q_values_available=[2310, 30030, 510510]`。
- `atom_count=36`。
- `with_next_layer_count=12`。
- `all_lift_identities_hold=True`。
- `route_counts={'NoNextLayerDataProfiniteObligation': 24, 'NextLayerCleanFiberCandidate': 6, 'NextLayerRefinedPDECEntropy': 6}`。
- `min_next_normalized_kl=0`。
- `max_next_normalized_kl=0.309287`。

## 4. 原子明细

| layer | P | old phase | residue | new phase | mass | next Q | next support rate | next KL | route |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 17 | 13 | 1 | 2323 | 1 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 17 | 964 | 9 | 21754 | 1 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 17 | 1347 | 3 | 8277 | 1 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 17 | 2298 | 11 | 27708 | 1 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 17 | 260 | 5 | 11810 | 1 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 17 | 673 | 12 | 28393 | 1 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 19 | 111 | 10 | 23211 | 17 | 510510 | 1 | 0 | `NextLayerCleanFiberCandidate` |
| Q=2310->30030 | 19 | 2200 | 2 | 6820 | 17 | 510510 | 1 | 0 | `NextLayerCleanFiberCandidate` |
| Q=2310->30030 | 19 | 962 | 11 | 26372 | 17 | 510510 | 1 | 0 | `NextLayerCleanFiberCandidate` |
| Q=2310->30030 | 19 | 1349 | 1 | 3659 | 17 | 510510 | 1 | 0 | `NextLayerCleanFiberCandidate` |
| Q=2310->30030 | 19 | 741 | 4 | 9981 | 17 | 510510 | 1 | 0 | `NextLayerCleanFiberCandidate` |
| Q=2310->30030 | 19 | 1570 | 8 | 20050 | 17 | 510510 | 1 | 0 | `NextLayerCleanFiberCandidate` |
| Q=2310->30030 | 23 | 919 | 9 | 21709 | 35 | 510510 | 1 | 0.309287 | `NextLayerRefinedPDECEntropy` |
| Q=2310->30030 | 23 | 1392 | 3 | 8322 | 35 | 510510 | 1 | 0.309287 | `NextLayerRefinedPDECEntropy` |
| Q=2310->30030 | 23 | 152 | 7 | 16322 | 35 | 510510 | 1 | 0.309287 | `NextLayerRefinedPDECEntropy` |
| Q=2310->30030 | 23 | 689 | 5 | 12239 | 35 | 510510 | 1 | 0.309287 | `NextLayerRefinedPDECEntropy` |
| Q=2310->30030 | 23 | 1622 | 7 | 17792 | 35 | 510510 | 1 | 0.309287 | `NextLayerRefinedPDECEntropy` |
| Q=2310->30030 | 23 | 2159 | 5 | 13709 | 35 | 510510 | 1 | 0.309287 | `NextLayerRefinedPDECEntropy` |
| Q=2310->30030 | 29 | 1036 | 0 | 1036 | 112 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 29 | 1275 | 12 | 28995 | 112 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 29 | 228 | 5 | 11778 | 112 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 29 | 2083 | 7 | 18253 | 112 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 29 | 467 | 4 | 9707 | 112 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=2310->30030 | 29 | 1844 | 8 | 20324 | 112 | 510510 | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 19 | 111 | 8 | 240351 | 1 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 19 | 3051 | 8 | 243291 | 1 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 19 | 3239 | 8 | 243479 | 1 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 19 | 6913 | 8 | 247153 | 1 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 19 | 7251 | 8 | 247491 | 1 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 19 | 11367 | 8 | 251607 | 1 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 23 | 1602 | 15 | 452052 | 19 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 23 | 28429 | 1 | 58459 | 19 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 23 | 14664 | 5 | 164814 | 19 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 23 | 15367 | 11 | 345697 | 19 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 23 | 2621 | 2 | 62681 | 19 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |
| Q=30030->510510 | 23 | 10747 | 14 | 431167 | 19 | n/a | n/a | n/a | `NoNextLayerDataProfiniteObligation` |

## 5. 读法

`NextLayerCleanFiberCandidate` 表示该原子在下一层 fiber 上已接近均匀，若 NoDeletion 持续则可作为 CleanKLS 输入。
`NextLayerRefinedPDECEntropy` 表示该原子提升后仍有明显 fiber KL，必须作为 refined/profinite PDEC 或继续升层输入。
`NoNextLayerDataProfiniteObligation` 不是反例出口，只表示当前仓库尚无下一层 multiplicity 数据，需要在无限塔证明中按同一规则处理。
