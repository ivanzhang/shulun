# Prime Matrix Phi-LPF punctured endpoint difference 证书

**状态：** `strict_k_prime_count_equals_phi_half_endpoint_difference_minus_forest_holes`

本层把 punctured half-primorial phase 改写为用户强调的 Phi-LPF 两端点差。
令 `p_half(P)` 为大于 `P/2` 的第一个素数，定义

```text
DeltaPhi_half(P,k)=Phi((k+1)P-1,p_half(P))-Phi(kP,p_half(P)).
```

再令 `F(P,k)` 为 upper-band reciprocal forest hole set。则

```text
pi((k+1)P-1)-pi(kP)=DeltaPhi_half(P,k)-|F(P,k)|.
```

## 1. 结构证明读法

`DeltaPhi_half(P,k)` 数的正是该行中避开所有 `q<=P/2` 的 half-primorial survivors。
这些 survivor 若合成，就唯一落入 high-prime semiprime forest holes；去掉 holes 后只能是素数。
因此反例等价于端点差不超过 forest holes：

```text
DeltaPhi_half(P,k)<=|F(P,k)|.
```

shadow-free lane 是 `|F(P,k)|=0` 的特例；upper-band 是有 forest holes 的同一公式。

## 2. 有限审计

```text
max_prime=1009
prime_base_count=165
all_endpoint_difference_identities_hold=true
endpoint_difference_failure_count=0
finite_evidence_not_used_as_global_proof=true
```

最小端点差余量行：

```text
P=11, k=10, DeltaPhi=2, forest=1, margin=1
```

最大 forest-hole 行：

```text
P=953, k=943, DeltaPhi=80, forest=24, margin=56
```

## 3. 有限样本表

| P | k | Delta Phi half | forest holes | Delta-hole | direct primes | shadow-free | upper |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 11 | 2 | 3 | 0 | 3 | 3 | `false` | `true` |
| 11 | 9 | 4 | 0 | 4 | 4 | `false` | `true` |
| 11 | 10 | 2 | 1 | 1 | 1 | `false` | `true` |
| 101 | 2 | 16 | 0 | 16 | 16 | `true` | `false` |
| 101 | 24 | 9 | 0 | 9 | 9 | `true` | `false` |
| 101 | 25 | 12 | 0 | 12 | 12 | `false` | `true` |
| 101 | 66 | 14 | 2 | 12 | 12 | `false` | `true` |
| 101 | 100 | 16 | 4 | 12 | 12 | `false` | `true` |
| 257 | 2 | 39 | 0 | 39 | 39 | `true` | `false` |
| 257 | 63 | 24 | 0 | 24 | 24 | `true` | `false` |
| 257 | 64 | 27 | 0 | 27 | 27 | `false` | `true` |
| 257 | 152 | 31 | 4 | 27 | 27 | `false` | `true` |
| 257 | 256 | 29 | 6 | 23 | 23 | `false` | `true` |
| 1009 | 2 | 128 | 0 | 128 | 128 | `true` | `false` |
| 1009 | 251 | 87 | 0 | 87 | 87 | `true` | `false` |
| 1009 | 252 | 85 | 0 | 85 | 85 | `false` | `true` |
| 1009 | 523 | 80 | 9 | 71 | 71 | `false` | `true` |
| 1009 | 1008 | 89 | 19 | 70 | 70 | `false` | `true` |

## 4. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sampled_endpoint_margins_positive=true
minimum_sample_endpoint_margin=4385
large_samples_are_evidence_not_global_proof=true
```

| P | k | Delta Phi half | forest holes | Delta-hole | direct primes | shadow-free | upper |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 100003 | 2 | 8013 | 0 | 8013 |  | `true` | `false` |
| 100003 | 24999 | 4626 | 0 | 4626 |  | `true` | `false` |
| 100003 | 25000 | 4623 | 0 | 4623 |  | `false` | `true` |
| 100003 | 33406 | 4661 | 119 | 4542 |  | `false` | `true` |
| 100003 | 100002 | 4900 | 515 | 4385 |  | `false` | `true` |
| 300007 | 2 | 22178 | 0 | 22178 |  | `true` | `false` |
| 300007 | 75000 | 12614 | 0 | 12614 |  | `true` | `false` |
| 300007 | 75001 | 12535 | 0 | 12535 |  | `false` | `true` |
| 300007 | 90261 | 12626 | 200 | 12426 |  | `false` | `true` |
| 300007 | 300006 | 13238 | 1272 | 11966 |  | `false` | `true` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PhiHalfEndpointDifferenceIdentityClosed | `true` | `true` | Delta Phi_half 精确等于 half-primorial survivor 数。 | exact Phi-LPF endpoint count |
| ForestHoleSubtractionIdentityClosed | `true` | `true` | strict 行素数数精确等于 Delta Phi_half 减去 reciprocal forest holes。 | exact punctured endpoint identity |
| ShadowFreeAndUpperBandUnifiedByEndpointDifference | `true` | `true` | shadow-free 是 forest_holes=0；upper-band 是 forest_holes>0 的同一端点差公式。 | unified endpoint formulation |
| FiniteSweepEndpointIdentityMatchesPrimeCount | `true` | `true` | 有限审计确认端点差等式与直接素数计数一致，但不作为全局证明。 | finite audit only |
| EndpointDifferenceDominatesForestHolesProved | `false` | `false` | 尚未证明所有剩余特殊相位都有 Delta Phi_half>forest_holes。 | PuncturedPhiEndpointDifferencePositiveOrPDEC |
| UnifiedPositiveCoreProved | `false` | `false` | 本层只把剩余口写成 Phi-LPF 两端点差正性，不证明三目标命题。 | PuncturedPhiEndpointDifferencePositiveOrPDEC |

## 6. 结论

当前 strict-k 剩余被写成单一 Phi-LPF 端点差：行素数数等于半筛 Phi 两端点差 减去 reciprocal forest holes。反例必须满足 DeltaPhi_half(P,k)<=|F(P,k)|；这就是 punctured phase 的端点计数正性版本。

当前端点差最窄口为：

```text
PuncturedPhiEndpointDifferencePositiveOrPDEC
```

本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只把统一剩余写成
Phi-LPF 端点差正性。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.json` | `8a608720597fccf43d673d046fecabc255493974f2a8441d4b3b14a3bb759e4e` |
| `docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json` | `10da31e36ce24880aa1c9ae6014f8d9434a0b16d5217ea9105a7f3fe42585719` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json` | `9db4d90a17cdd1c8e1730e6b8d5d86caa454ea43951ddc4c3ce713a09acf373f` |
