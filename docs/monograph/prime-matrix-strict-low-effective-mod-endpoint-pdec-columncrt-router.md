# Prime Matrix strict 低有效模 endpoint PDEC/ColumnCRT 路由器

**状态：** `low_effective_mod_reduced_to_reciprocal_common_divisor_envelope_and_columncrt_open`

低有效模共振已经被严格压成共同因子结构。因为 P 与所有筛模 d 互素，gcd(hP^{-1},d)=gcd(h,d)。若有效分母 s=d/gcd(h,d) 小，则 d=s g 且 g|h。其中 s=1 的零频已经被中心化端点函数完全删除；真正剩余的 s>=2 项有 1/g 的共同因子衰减。因此低有效模上界等价于加权共同因子倒数和。若该倒数和仍过大，就必须登记为 hot frequency common divisor 或低商模 ColumnCRT/PDEC。

```text
effective_gcd_identity_closed=true
zero_mode_cancellation_closed=true
reciprocal_common_divisor_reduction_closed=true
pdec_columncrt_route_registered=true
low_effective_mod_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 共同因子压缩

全局频率 `h` 在模 `d` 上看到的有效残基是 `hP^{-1} mod d`。因为 `P` 与 `d` 互素，

```text
gcd(hP^{-1},d)=gcd(h,d).
```

若有效分母 `s=d/gcd(h,d)<=R`，则

```text
d=s g,  g|h.
```

中心化端点函数删掉 `s=1` 的零频；对 `s>=2`，单模 Fourier 系数有

```text
|hat phi_d(h)| <= s/(2d)=1/(2g).
```

所以低有效模贡献不再是自由大谱，而是共同因子倒数和。

## 2. 精确律

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `invertible_phase_gcd` | gcd(hP^{-1} mod d,d)=gcd(h,d), because gcd(P,d)=1. | `closed` | 低有效模完全由 h 与 d 的共同因子控制。 |
| `effective_denominator_factorization` | s=d/gcd(h,d); if s<=R, then d=s g with g\|h. | `closed` | 低有效模支撑落在少数 small-quotient times divisor-of-h 线上。 |
| `zero_mode_cancellation` | If s=1, then hP^{-1}=0 mod d and the centered endpoint coefficient is 0. | `closed` | 最危险的 d\|h 情况实际被中心化删除。 |
| `reciprocal_common_divisor_decay` | For s>=2, \|hat phi_d(h)\| <= s/(2d)=1/(2g), d=sg. | `closed` | 低有效模不是免费大谱；每条共同因子线有 1/g 衰减。 |
| `low_effective_mass_bound` | LowEff_R(h)<=1/2 sum_{2<=s<=R} sum_{g\|h, sg in D_+} w_{sg}^+/g. | `closed_reduction` | 低有效模上界压成加权共同因子倒数和。 |
| `hot_divisor_or_columncrt` | If the reciprocal divisor envelope is too large, then some quotient s has abnormal mass on divisors of h; persistent cases are PDEC/ColumnCRT, isolated cases SAE. | `registered_route` | 大低有效模不能作为无名误差保留。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的正权端点 Fourier 上界内部。 | 保持 row_column_unconditional_closed=false。 |
| `EffectiveGCDIdentityClosed` | `true` | `true` | 低有效分母等于 d/gcd(h,d)，与 P 的逆元选择无关。 | LowEffectiveModEndpointPDECOrColumnCRT |
| `ZeroModeCancellationClosed` | `true` | `true` | d\|h 的零频贡献被中心化端点函数删除。 | 无。 |
| `ReciprocalDivisorReductionClosed` | `true` | `true` | 低有效模贡献被压到 small quotient 线上的 1/g 加权倒数和。 | WeightedReciprocalCommonDivisorEnvelopeForLowEffectiveSpectrum |
| `PDECColumnCRTRouteRegistered` | `true` | `false` | 倒数和若过大，必须表现为 hot common divisor 或低商模相位集中。 | HotFrequencyCommonDivisorSupportBudget OR LowQuotientColumnCRTOrPDECRoute |
| `LowEffectiveModExcludedCurrentCorpus` | `false` | `false` | 尚未证明 reciprocal divisor envelope 小于 PDEC 下界，也未排斥 hot divisor/ColumnCRT 出口。 | WeightedReciprocalCommonDivisorEnvelopeForLowEffectiveSpectrum AND HotFrequencyCommonDivisorSupportBudget AND LowQuotientColumnCRTOrPDECRoute |

## 4. 最新最窄输入

```text
WeightedReciprocalCommonDivisorEnvelopeForLowEffectiveSpectrum
```

并行保留：

```text
HotFrequencyCommonDivisorSupportBudget AND LowQuotientColumnCRTOrPDECRoute AND EndpointArcGeometricDecayLargeEffectiveModBudget
```

审稿边界：本步闭合低有效模的共同因子结构和零频删除；尚未证明共同因子倒数和足够小，也未排斥 hot divisor/ColumnCRT 出口。
