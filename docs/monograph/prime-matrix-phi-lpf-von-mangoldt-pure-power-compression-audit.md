# Prime Matrix Phi-LPF von Mangoldt pure-power compression 审计

**状态：** `lpf_pure_power_von_mangoldt_compression_closed_but_not_distribution_family`
**核验日期：** `2026-05-26`

## 1. 修正后的 lift 口径

全局 Mobius 除子和式仍是可线性平均的标准形式：

```text
Lambda(m)=sum_{d|m} mu(d) log(m/d)
```

但点态恒等式可以被 LPF 剥离压缩为：

```text
Lambda(m)=log(LPF(m)) if m is a power of LPF(m), else 0
```

也就是说，令 `p=LPF(m)`，把 `p` 的全部幂从 `m` 中剥掉；若剩余为 `1`，
则 `m=p^a` 且 `Lambda(m)=log p`，否则 `Lambda(m)=0`。

这修正了“点态 lift 必须保持完整全局 divisor cube”的过强表述；真正不能省略的是
可平均的 signed distribution family。LPF 纯素幂选择器是非线性因子分解谓词，不是
Type-II/trace/AP 平均可直接调用的加性有符号族。

## 2. 全局读数

```text
lpf_pure_power_compression_closed=true
lambda_mass_reconstructed_from_endpoint_plus_prime_power_tail=true
mixed_composites_cancel_to_zero_pointwise=true
prime_power_tail_separated=true
pure_power_selector_supplies_additive_signed_distribution_family=false
pointwise_ap_theta_lower_bound_proved=false
admissible_typeii_or_trace_family_constructed=false
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| X | M=2X+1 | endpoint primes | composite prime powers | mixed composites | prime-power Lambda fraction |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 100 | 201 | 45 | 8 | 47 | 0.066686 |
| 1000 | 2001 | 302 | 21 | 677 | 0.024339 |
| 10000 | 20001 | 2261 | 53 | 7686 | 0.008123 |
| 100000 | 200001 | 17983 | 120 | 81897 | 0.002484 |

## 3. 最大样本局部结构

`X=100000` 的 composite prime-power owner：

```text
3:10, 5:6, 7:5, 11:4, 13:3, 17:3, 19:3, 23:2, other:84
```

对应 exponent 分布：

```text
2:85, 3:15, 4:7, 5:4, 6:3, 7:2, 8:1, 9:1, other:2
```

mixed composite 的主要 owner bucket：

```text
3:33323, 5:13326, 7:7613, 11:4151, 13:3194, 17:2252, 19:1897, 23:1484, other:14657
```

## 4. 外部前沿重新定位

| input | direct close | role after this audit |
| --- | --- | --- |
| [Milicevic-Qin-Wu arbitrary-modulus Kloosterman bilinear forms](https://arxiv.org/abs/2511.07550) | `false` | power-saving bilinear Kloosterman input; it becomes relevant only after the LPF layer supplies an actual bilinear trace family |
| [Zheng simultaneous arithmetic progressions](https://arxiv.org/abs/2512.22798) | `false` | mean-value input for two simultaneous AP constraints only after the LPF pure-power selector has been replaced by an admissible signed family |
| [Runbo Li large-modulus AP primes and Harman sieve refinements](https://arxiv.org/abs/2602.20917) | `false` | average-modulus prime distribution input; does not give pointwise every-row theta positivity at the P^2 scale |
| [Wright trilinear Kloosterman fractions](https://arxiv.org/abs/2604.25177) | `false` | usable only after a trilinear convolution with equidistributed coefficients is constructed |
| [Pascadi non-abelian composite-modulus Kloosterman Type-II](https://arxiv.org/abs/2511.08445) | `false` | requires a genuine Type-II Kloosterman family over composite moduli, not a nonlinear pure-power selector |
| [Becker-Breuillard spectral gaps and anti-concentration](https://arxiv.org/abs/2512.15364) | `false` | requires a finite-group orbit or random-walk model before spectral gap anti-concentration can be applied |
| [Matomaki-Radziwill-Shao-Tao-Teravainen almost-all short-interval uniformity](https://link.springer.com/article/10.1007/s00222-026-01408-6) | `false` | almost-all short-interval Lambda uniformity; not a pointwise AP positivity theorem for each prime-matrix row |

## 5. 最新开放口

```text
LPFPurePowerVonMangoldtCompressionClosed AND PrimePowerTailSeparated AND PurePowerSelectorNotAnAdditiveSignedDistributionFamily AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_von_mangoldt_pure_power_compression_audit.py` | `12e1b9cb43eac5f15cd3cf772e38d8cd97e9f71b4e3ce7f8142ecba8452d99fd` |
| `docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json` | `f745ed6c597dfcceed10f50249df139235cac727fd8086737b81bb894bda3a4c` |
| `docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json` | `bee6ba7d14330a7a2cf52547f8b37902314ba8ffa9b10186ae5d1e71efe4a534` |
| `docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json` | `92468974eceab624e5a553bb3a24e20a85b9e3f5424b674bb9f00057a53ccfc5` |
| `docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json` | `975aa118af686bd729414f291af1efd9fa60082d622ac687d7f87772246acd6e` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `2af578241a1c4fbe7078a25ef713f5651277a1d93674107cba35c6d3e9a45432` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `17248e6687643db9a713e4925423c0507feb614cb73b4c3d74876a5de261de4a` |
| `docs/monograph/external-theorem-index.md` | `8cd9f842581be6c8c05b966285e6c943faa782dead1f63bc50814bcdf5119089` |
