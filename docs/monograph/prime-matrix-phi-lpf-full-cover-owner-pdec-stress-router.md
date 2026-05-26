# Prime Matrix Phi-LPF full-cover owner PDEC stress 路由

**状态：** `owner_only_pdec_rejected_target_affine_pdec_still_open`
**核验日期：** `2026-05-26`

Full-cover owner PDEC 不能只依赖 LPF owner 分桶、纤维互不相交或一素数一同余类；普通零素数短区间已经满足这些性质并形成 full cover。因此 owner-only PDEC 被排除。剩余可行口必须使用目标行特有的 A=kP、P 为素数、k<P、长度 P-1 的全局仿射锚，并附带 owner minimality 与 signed/phase payload。有限目标行扫描继续未见 full cover，但仍只是证据，不是证明。

```text
full_cover_owner_pdec_stress_synced=true
owner_only_pdec_rejected=true
target_affine_owner_pdec_proved=false
target_scan_no_full_cover=true
row_column_unconditional_closed=false
```

## 1. owner-only PDEC 的反例压力

| interval | length | primes | full cover | owner buckets | one residue per prime |
| --- | ---: | ---: | --- | ---: | --- |
| `(90,96]` | 6 | 0 | `true` | 4 | `true` |
| `(114,126]` | 12 | 0 | `true` | 5 | `true` |
| `(200,210]` | 10 | 0 | `true` | 5 | `true` |

## 2. 目标行最小缺口有限扫描

| P | min-k | row | min primes | max primes | cover at min row | owner buckets | top owners |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 31 | 25 | `(775,805]` | 2 | 7 | 28 | 8 | `[{'p': 2, 'count': 15}, {'p': 3, 'count': 5}, {'p': 5, 'count': 2}, {'p': 11, 'count': 2}, {'p': 7, 'count': 1}, {'p': 13, 'count': 1}, {'p': 17, 'count': 1}, {'p': 19, 'count': 1}]` |
| 101 | 73 | `(7373,7473]` | 7 | 20 | 93 | 14 | `[{'p': 2, 'count': 50}, {'p': 3, 'count': 17}, {'p': 5, 'count': 7}, {'p': 7, 'count': 4}, {'p': 11, 'count': 3}, {'p': 13, 'count': 2}, {'p': 17, 'count': 2}, {'p': 31, 'count': 2}]` |
| 251 | 108 | `(27108,27358]` | 18 | 41 | 232 | 25 | `[{'p': 2, 'count': 125}, {'p': 3, 'count': 42}, {'p': 5, 'count': 17}, {'p': 7, 'count': 9}, {'p': 11, 'count': 5}, {'p': 17, 'count': 4}, {'p': 19, 'count': 4}, {'p': 13, 'count': 3}]` |
| 499 | 362 | `(180638,181136]` | 29 | 73 | 469 | 48 | `[{'p': 2, 'count': 249}, {'p': 3, 'count': 83}, {'p': 5, 'count': 33}, {'p': 7, 'count': 19}, {'p': 11, 'count': 10}, {'p': 13, 'count': 10}, {'p': 17, 'count': 6}, {'p': 19, 'count': 6}]` |
| 1009 | 905 | `(913145,914153]` | 52 | 137 | 956 | 80 | `[{'p': 2, 'count': 504}, {'p': 3, 'count': 168}, {'p': 5, 'count': 66}, {'p': 7, 'count': 39}, {'p': 11, 'count': 20}, {'p': 13, 'count': 17}, {'p': 17, 'count': 13}, {'p': 19, 'count': 10}]` |
| 2003 | 1256 | `(2515768,2517770]` | 113 | 248 | 1889 | 120 | `[{'p': 2, 'count': 1001}, {'p': 3, 'count': 333}, {'p': 5, 'count': 133}, {'p': 7, 'count': 76}, {'p': 11, 'count': 43}, {'p': 13, 'count': 31}, {'p': 17, 'count': 24}, {'p': 19, 'count': 17}]` |
| 5003 | 4980 | `(24914940,24919942]` | 260 | 559 | 4742 | 244 | `[{'p': 2, 'count': 2501}, {'p': 3, 'count': 834}, {'p': 5, 'count': 333}, {'p': 7, 'count': 190}, {'p': 11, 'count': 104}, {'p': 13, 'count': 79}, {'p': 17, 'count': 54}, {'p': 19, 'count': 46}]` |

有限扫描只显示目标行 full cover 未出现；它不替代证明。

## 3. 被排除的 naive PDEC

| predicate | reason rejected | surviving requirement |
| --- | --- | --- |
| `LPFOwnerFibersDisjointAndCoverRow` | generic full-cover intervals satisfy it with no contradiction | must use target anchor A=kP, P prime, k<P, length P-1 |
| `OneResidueClassPerPrimeFiber` | every ordinary interval has one divisibility residue class per prime after choosing offset from A | must exploit the special residues -kP mod p across all p, not one class locally |
| `LPFRoughCofactorOwnerPartition` | this is exactly the LPF definition and is true in zero-prime ordinary intervals | must add a non-tautological CRT/phase incompatibility |
| `EulerProductDensityOrWheelCapacityOnly` | full-cover witnesses show support capacity can saturate without signed information | must add Mobius/Von Mangoldt/trace cancellation or a named PDEC |

## 4. 仍可非循环的 PDEC 字段

| field | content | why needed |
| --- | --- | --- |
| `target_affine_anchor` | `A=kP, length=P-1, P prime, 1<=k<=P-1` | ordinary full-cover intervals lack this exact anchor |
| `global_residue_coupling` | `a_p=-kP mod p for all p<=sqrt((k+1)P-1)` | local one-residue-per-prime facts are generic and cannot produce PDEC |
| `owner_minimality` | `O_p=D_p minus union_{q<p}D_q with a named first-owner transition` | must distinguish owner buckets from coarse divisor support |
| `signed_or_phase_payload` | `Mobius/Von Mangoldt sign, trace phase, or CRT phase packet before pushforward` | pure support is parity-blind and already known insufficient |

## 5. 外部边界

| input | usable content | current gap | source |
| --- | --- | --- | --- |
| Jacobsthal / covering-system bounds | general bounds on long runs covered by residue classes of small primes | known general bounds are far above the one-row P scale needed here; no target-affine PDEC follows | https://doi.org/10.1007/BF02564232 |
| Short-interval prime theorems | zero-density driven primes in intervals thicker than x^(1/2) | at x=P^2 the theorem still covers many rows, not one target row | https://arxiv.org/abs/2405.20552 |
| Spectral/Kloosterman/Type-II methods | AP/trace technology indicates the right kind of signed family | the current LPF owner fibers have not been promoted to an admissible source-keyed trace family | https://arxiv.org/abs/2509.04883 |

## 6. 下一手

```text
selected_next_primary_gate=TargetAffineFullCoverOwnerResiduePDEC
selected_parallel_signed_gate=MobiusResidueCoverSignedTraceWithTargetAffineAnchor
selected_parallel_spectral_gate=SpectralKloostermanResidueLiftWithSourceKeys
```

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `7d8fcb401c9515bae493bed57eb5e6fa597a7d10d405676f8a5471dea8e44705` |
| `docs/monograph/external-theorem-index.md` | `cc8764f0b71685b315a4ee815e80ac349173f14705ccbe41691297bca037ff90` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `9e0b4444d5633c653edf9e5a72bbcd90ca0f6f0a9efc19466335575436a8f580` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json` | `74636f1bc6c8e7088a213b0df5440bf93aadb10482989dca7615eb4edaaf3f06` |
| `docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json` | `234ad3d23afb443ae53e5b0faf095f0621e38614b737de87b541a6b194da0cdd` |
| `docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json` | `93b9420810fe6a699bb79d3591e65e1e3f6077e3d0c94e37842649ed8a3bfb32` |
| `docs/monograph/prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.json` | `04b3e0b14d2f12b48232ea386ad31895d9a5b550a631bb8530539335f45b216b` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `a8dcf58155c3b8611ea9b4eaf095b159764de417f3e80ca6db378ff2a6bbeb85` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `5bd83b585553e8b0c51793c64d414e13de3d4790c2317d089b148e8be02ac96d` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `5ec1a1f30e082ef4b542e4a49b622d6391e4fab8b7e6b996bdfb5ddc003b15cf` |
| `experiments/prime_matrix_phi_lpf_full_cover_owner_pdec_stress_router.py` | `6994171369e63abd4d4fc0556e33e253ecd91f02363c502a48fab49b42df54bc` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `24173fec1dcaa935079b1405e74978583f893ec75a79654f093171f77858b857` |
