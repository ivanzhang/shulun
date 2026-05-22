# Prime Matrix Phi-LPF punctured half-primorial forest phase 证书

**状态：** `shadow_free_and_upper_band_reduced_to_punctured_half_primorial_forest_phase`

本层把 shadow-free half-primorial special phase 与 upper-band forest saturation 合并。
设

```text
M_half(P)=prod_{q<=P/2, q prime} q,
F(P,k)={t: t=qm-kP, q,m prime, P/2<q<=m<2P, kP<qm<(k+1)P}.
```

则行内素数槽精确为

```text
{1<=t<P: gcd(kP+t,M_half(P))=1 and t not in F(P,k)}.
```

## 1. 结构证明读法

若 `t` 避开所有低素数且不在 forest hole set `F(P,k)` 中，则 `kP+t` 不可能合成。
因为任何合成 half-rough 槽都必须写成唯一的 high-prime product `qm`，从而正好落入 `F(P,k)`。
因此行失败等价于所有 half-primorial survivor 都被 forest holes 吃掉：

```text
{t: gcd(kP+t,M_half(P))=1} subset F(P,k).
```

shadow-free 子带就是 `F(P,k)=empty` 的零孔特例；upper-band 则是有序森林孔特例。

## 2. 有限审计

```text
max_prime=1009
prime_base_count=165
all_punctured_phase_identities_hold=true
punctured_phase_failure_count=0
saturation_row_count=0
finite_evidence_not_used_as_global_proof=true
```

最小 prime-slot 行：

```text
P=11, k=10, R=2, forest=1, prime_slots=1
```

最大 forest-hole 行：

```text
P=953, k=943, R=80, forest=24, prime_slots=56
```

## 3. 有限样本表

| P | k | R_half | forest holes | prime slots | covered outside holes | saturation |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 11 | 2 | 3 | 0 | 3 | 7 | `false` |
| 11 | 5 | 2 | 0 | 2 | 8 | `false` |
| 11 | 8 | 3 | 1 | 2 | 7 | `false` |
| 11 | 9 | 4 | 0 | 4 | 6 | `false` |
| 11 | 10 | 2 | 1 | 1 | 8 | `false` |
| 101 | 25 | 12 | 0 | 12 | 88 | `false` |
| 101 | 50 | 13 | 2 | 11 | 87 | `false` |
| 101 | 66 | 14 | 2 | 12 | 86 | `false` |
| 101 | 75 | 14 | 2 | 12 | 86 | `false` |
| 101 | 100 | 16 | 4 | 12 | 84 | `false` |
| 257 | 64 | 27 | 0 | 27 | 229 | `false` |
| 257 | 128 | 32 | 4 | 28 | 224 | `false` |
| 257 | 152 | 31 | 4 | 27 | 225 | `false` |
| 257 | 192 | 26 | 2 | 24 | 230 | `false` |
| 257 | 256 | 29 | 6 | 23 | 227 | `false` |
| 1009 | 252 | 85 | 0 | 85 | 923 | `false` |
| 1009 | 504 | 79 | 9 | 70 | 929 | `false` |
| 1009 | 523 | 80 | 9 | 71 | 928 | `false` |
| 1009 | 756 | 88 | 9 | 79 | 920 | `false` |
| 1009 | 1008 | 89 | 19 | 70 | 919 | `false` |

## 4. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sampled_forest_holes_are_half_rough=true
sample_saturation_row_count=0
minimum_sample_prime_slots=4385
large_samples_are_evidence_not_global_proof=true
```

| P | k | R_half | forest holes | prime slots | covered outside holes | saturation |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 100003 | 25000 | 4623 | 0 | 4623 |  | `false` |
| 100003 | 33406 | 4661 | 119 | 4542 |  | `false` |
| 100003 | 50001 | 4747 | 284 | 4463 |  | `false` |
| 100003 | 75002 | 4836 | 445 | 4391 |  | `false` |
| 100003 | 100002 | 4900 | 515 | 4385 |  | `false` |
| 300007 | 75001 | 12535 | 0 | 12535 |  | `false` |
| 300007 | 90261 | 12626 | 200 | 12426 |  | `false` |
| 300007 | 150003 | 12927 | 716 | 12211 |  | `false` |
| 300007 | 225005 | 13171 | 1061 | 12110 |  | `false` |
| 300007 | 300006 | 13238 | 1272 | 11966 |  | `false` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PuncturedHalfPrimorialIdentityClosed | `true` | `true` | 行素数槽精确等于 half-primorial survivor 去掉 upper-band forest holes 后的剩余。 | exact identity |
| ShadowFreeLaneIsZeroHoleSpecialCase | `true` | `true` | shadow-free 子带就是 forest hole set 为空的 punctured phase 特例。 | unifies previous lane |
| UpperBandFailureEqualsPuncturedCoveredBlock | `true` | `true` | upper-band 失败当且仅当所有 half-primorial survivors 都落在 forest holes 内。 | PuncturedHalfPrimorialForestCoveredBlock |
| FiniteSweepNoSaturationObserved | `true` | `true` | 有限审计未见 forest saturation，但这不是全局证明。 | finite audit only |
| PuncturedForestPhaseAvoidanceProved | `false` | `false` | 尚未证明特殊相位不能启动带 forest holes 的长覆盖块。 | PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC |
| UnifiedPositiveCoreProved | `false` | `false` | 本层统一两个剩余口，但不证明三目标命题。 | PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC |

## 6. 结论

shadow-free 与 upper-band 两个剩余口已经合并为同一个相位问题：特殊半 primorial 覆盖块允许被 reciprocal forest holes 打孔。若仍无素数，则全部 half-primorial survivor 必须落入这片 forest hole set；否则任意未被打孔的 survivor 自动就是素数。

当前统一最窄口为：

```text
PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC
```

本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它把两个剩余口合并成
一个 punctured half-primorial special phase 问题。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json` | `10da31e36ce24880aa1c9ae6014f8d9434a0b16d5217ea9105a7f3fe42585719` |
| `docs/monograph/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.json` | `55556f72402db91637fa98a903e4ee80c3fcb0ddabc81e334898523313d06d3f` |
| `docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json` | `6f2af1f27399871c3838a8a760f625bd16d18ac1e02e3740bdb2f903d3c27011` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json` | `9db4d90a17cdd1c8e1730e6b8d5d86caa454ea43951ddc4c3ce713a09acf373f` |
