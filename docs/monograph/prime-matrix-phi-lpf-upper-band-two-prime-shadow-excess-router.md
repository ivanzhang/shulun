# Prime Matrix Phi-LPF upper-band two-prime shadow excess 证书

**状态：** `upper_band_two_prime_shadow_reduced_to_sparse_reciprocal_prime_pair_windows`

本层处理 strict-k half-rough shadow split 留下的 upper square band。设 `P` 为素数，
`1<k<P`，并处在

```text
4*((k+1)P-1)>P^2.
```

对每个高素数 `q in (P/2,P)`，定义倒数短窗

```text
I_q(P,k)=[max(q, floor(kP/q)+1), floor(((k+1)P-1)/q)] intersect Z.
```

则上一层的 two-prime shadow 精确为

```text
T_half(P,k)=sum_{P/2<q<P, q prime} #{m in I_q(P,k): m prime}.
```

并且 `|I_q(P,k)|<=2`。所以 upper-band 的真剩余不是完整 LPF 树，而是
一个每个 `q` 至多两个候选点的 reciprocal prime-pair 饱和问题。

## 1. 结构证明读法

由 `kP<qm<(k+1)P` 得

```text
floor(kP/q)+1 <= m <= floor(((k+1)P-1)/q).
```

唯一代表要求 `q<=m`，所以左端取 `max(q, floor(kP/q)+1)`。
窗口实长度小于 `P/q<2`，故每个高素数 `q` 最多给两个整数候选；再筛掉非素数 `m`
就是 actual shadow load。若 `R_half(P,k)-T_half(P,k)<=0`，失败必须是这些
短窗素数点真实饱和，而不是低筛容量的匿名波动。

## 2. 有限审计

```text
max_prime=1009
prime_base_count=165
all_reciprocal_window_identities_hold=true
identity_failure_count=0
finite_evidence_not_used_as_global_proof=true
```

upper-band 最小余量样本：

```text
P=11, k=10, R=2, T=1, direct=1, cand=2
```

BHP 剩余与 upper-band 交集最小余量：

```text
P=11, first_k=9, min_margin=1
```

最高实际 shadow 比例行：

```text
P=13, k=9, R=3, T=2, direct=1
```

最高整数候选包络比例行：

```text
P=19, k=15, R=3, int_candidates=5, T=2
```

## 3. 有限样本表

| P | k | R_half | T_shadow | int cand | R-T | active q | two-cand q | max cand/q |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 2 | 3 | 0 | 0 | 3 | 0 | 0 | 0 |
| 11 | 5 | 2 | 0 | 2 | 2 | 1 | 1 | 2 |
| 11 | 8 | 3 | 1 | 2 | 2 | 1 | 1 | 2 |
| 11 | 9 | 4 | 0 | 1 | 4 | 1 | 0 | 1 |
| 11 | 10 | 2 | 1 | 2 | 1 | 1 | 1 | 2 |
| 101 | 25 | 12 | 0 | 0 | 12 | 0 | 0 | 0 |
| 101 | 50 | 13 | 2 | 8 | 11 | 5 | 3 | 2 |
| 101 | 66 | 14 | 2 | 10 | 12 | 7 | 3 | 2 |
| 101 | 75 | 14 | 2 | 13 | 12 | 8 | 5 | 2 |
| 101 | 100 | 16 | 4 | 14 | 12 | 10 | 4 | 2 |
| 257 | 64 | 27 | 0 | 0 | 27 | 0 | 0 | 0 |
| 257 | 128 | 32 | 4 | 20 | 28 | 11 | 9 | 2 |
| 257 | 152 | 31 | 4 | 22 | 27 | 14 | 8 | 2 |
| 257 | 192 | 26 | 2 | 26 | 24 | 16 | 10 | 2 |
| 257 | 256 | 29 | 6 | 34 | 23 | 23 | 11 | 2 |
| 1009 | 252 | 85 | 0 | 0 | 85 | 0 | 0 | 0 |
| 1009 | 504 | 79 | 9 | 55 | 70 | 31 | 24 | 2 |
| 1009 | 523 | 80 | 9 | 54 | 71 | 33 | 21 | 2 |
| 1009 | 756 | 88 | 9 | 84 | 79 | 54 | 30 | 2 |
| 1009 | 1008 | 89 | 19 | 101 | 70 | 72 | 29 | 2 |

## 4. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sampled_upper_rows_have_positive_margin=true
large_samples_are_evidence_not_global_proof=true
```

| P | k | R_half | T_shadow | int cand | R-T | active q | two-cand q | max cand/q |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100003 | 25000 | 4623 | 0 | 0 | 4623 | 0 | 0 | 0 |
| 100003 | 33406 | 4661 | 119 | 1342 | 4542 | 723 | 619 | 2 |
| 100003 | 50001 | 4747 | 284 | 3134 | 4463 | 1871 | 1263 | 2 |
| 100003 | 75002 | 4836 | 445 | 4964 | 4391 | 3288 | 1676 | 2 |
| 100003 | 100002 | 4900 | 515 | 6249 | 4385 | 4459 | 1790 | 2 |
| 300007 | 75001 | 12535 | 0 | 0 | 12535 | 0 | 0 | 0 |
| 300007 | 90261 | 12626 | 200 | 2323 | 12426 | 1213 | 1110 | 2 |
| 300007 | 150003 | 12927 | 716 | 8603 | 12211 | 5136 | 3467 | 2 |
| 300007 | 225005 | 13171 | 1061 | 13440 | 12110 | 8975 | 4465 | 2 |
| 300007 | 300006 | 13238 | 1272 | 16876 | 11966 | 12148 | 4728 | 2 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| UpperBandReciprocalWindowFormulaClosed | `true` | `true` | upper-band two-prime shadow 精确等于高素数 q 的 reciprocal m 短窗中素数点数之和。 | exact formula |
| EachHighQHasAtMostTwoMValues | `true` | `true` | 因窗口长度 P/q<2，每个 q in (P/2,P) 至多贡献两个整数候选 m。 | prime filtering remains actual load |
| UpperBandFailureIsSparsePrimePairSaturation | `true` | `true` | 若 upper-band 行失败，则 at-most-two 候选的 reciprocal prime-pair shadow 必须吃掉全部 half-rough survivor。 | UpperBandReciprocalPrimePairShadowSaturatesHalfRoughSurvivors |
| FiniteSweepSupportsPositiveMargin | `true` | `true` | 有限审计中 exact identity、短窗公式和正余量均正常，但不作为全局证明。 | finite audit only |
| MertensHalfRoughFloorAndSelbergShadowCeilingProved | `false` | `false` | 尚未证明同一 row convention 下 R_half 的下界和 T_shadow 的 Selberg/Brun 上界之间存在统一正间隔。 | UpperBandHalfRoughFloorOrReciprocalPrimePairCeiling |
| UpperBandPositivityProved | `false` | `false` | 本层只把 high-k upper band 压成稀疏 reciprocal prime-pair 饱和问题，不证明全局正性。 | UpperBandReciprocalPrimePairShadowSaturationOrPDEC |
| UnifiedPositiveCoreProved | `false` | `false` | 本层不是三目标命题闭合；shadow-free special phase 与 upper-band sparse shadow 两口仍需继续攻。 | HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC AND UpperBandReciprocalPrimePairShadowSaturationOrPDEC |

## 6. 结论

upper-band 的 two-prime shadow 不再是抽象合数树，而是高素数 q 上的 reciprocal 短窗 prime-pair 图。每个 q 至多两个 m 候选；若行正性失败，必须是这些稀疏短窗中的素数点 真实饱和并覆盖全部 half-rough survivor，或者表现为 half-rough floor / reciprocal shadow ceiling 的命名 PDEC。

当前 upper-band 最窄直接主攻口是：

```text
UpperBandReciprocalPrimePairShadowSaturationOrPDEC AND UpperBandHalfRoughFloorOrReciprocalPrimePairCeiling
```

本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把 upper-band
硬点压成 reciprocal prime-pair 短窗饱和与相应 PDEC/ceiling/floor 接口。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json` | `9db4d90a17cdd1c8e1730e6b8d5d86caa454ea43951ddc4c3ce713a09acf373f` |
| `docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json` | `6f2af1f27399871c3838a8a760f625bd16d18ac1e02e3740bdb2f903d3c27011` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.json` | `f3f48c40a68ca892665fdc763803d616619ac104127aebb783f7f921c6fcbf54` |
| `docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json` | `c5ca8b97bf9f6dc2c5abaec3dd7f4ba612a3996df98696b3b01167e2b076f936` |
