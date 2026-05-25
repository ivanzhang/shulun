# Prime Matrix Phi-LPF LPF bucket inclusive survival formula 审计

**状态：** `prime_divisibility_class_is_one_over_p_not_one_minus_one_over_p`
**核验日期：** `2026-05-25`

## 1. 结论

修正版已经把小素数 `q<p` 的生存密度改为 `1-1/q`，这是正确方向。
但 `p` 本身不能继续乘 `1-1/p`。在 `LPF(n)=p` 的 bucket 中，
`n` 必须满足 `n=0 mod p`，所以 `p` 这一层的密度是 `1/p`。

精确公式仍是：

```text
C_p(N)=#{n<=N composite : LPF(n)=p}
      =Phi(floor(N/p); primes<p)-1.
```

正确的 n 轴连续主项是：

```text
(N-p^2)*(1/p)*prod_{q<p}(1-1/q).
```

用户修正版为：

```text
(N-p^2)*prod_{q<=p}(1-1/q),
```

二者相差因子 `p-1`。因此只在 `p=2` 偶然相同，从 `p=3` 起系统性高估。

## 2. 全局读数

```text
exact_lpf_bucket_identity_closed=true
inclusive_survival_formula_supported=false
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| N | exact total | composite count | correct total/exact | user total/exact | first wrong p |
| --- | --- | --- | --- | --- | --- |
| 100 | 74 | 74 | 0.947426 | 1.486358 | 3 |
| 1000 | 831 | 831 | 0.980306 | 2.398928 | 3 |
| 10000 | 8770 | 8770 | 0.985832 | 4.047312 | 3 |
| 100000 | 90407 | 90407 | 0.988315 | 7.385319 | 3 |

## 3. 样本 bucket

### N=100

| p | exact | correct density | correct main | user density | user main | user/correct |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 49 | 1/2 | 48.000000 | 1/2 | 48.000000 | 1.000000 |
| 3 | 16 | 1/6 | 15.166667 | 1/3 | 30.333333 | 2.000000 |
| 5 | 6 | 1/15 | 5.000000 | 4/15 | 20.000000 | 4.000000 |
| 7 | 3 | 4/105 | 1.942857 | 8/35 | 11.657143 | 6.000000 |

### N=1000

| p | exact | correct density | correct main | user density | user main | user/correct |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 499 | 1/2 | 498.000000 | 1/2 | 498.000000 | 1.000000 |
| 3 | 166 | 1/6 | 165.166667 | 1/3 | 330.333333 | 2.000000 |
| 5 | 66 | 1/15 | 65.000000 | 4/15 | 260.000000 | 4.000000 |
| 7 | 37 | 4/105 | 36.228571 | 8/35 | 217.371429 | 6.000000 |
| 11 | 20 | 8/385 | 18.264935 | 16/77 | 182.649351 | 10.000000 |
| 13 | 16 | 16/1001 | 13.282717 | 192/1001 | 159.392607 | 12.000000 |
| 17 | 10 | 192/17017 | 8.022096 | 3072/17017 | 128.353529 | 16.000000 |
| 19 | 8 | 3072/323323 | 6.071353 | 55296/323323 | 109.284350 | 18.000000 |
| 23 | 6 | 55296/7436429 | 3.502275 | 110592/676039 | 77.050040 | 22.000000 |
| 29 | 2 | 110592/19605131 | 0.896915 | 442368/2800733 | 25.113608 | 28.000000 |
| 31 | 1 | 442368/86822723 | 0.198708 | 13271040/86822723 | 5.961234 | 30.000000 |

### N=10000

| p | exact | correct density | correct main | user density | user main | user/correct |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 4999 | 1/2 | 4998.000000 | 1/2 | 4998.000000 | 1.000000 |
| 3 | 1666 | 1/6 | 1665.166667 | 1/3 | 3330.333333 | 2.000000 |
| 5 | 666 | 1/15 | 665.000000 | 4/15 | 2660.000000 | 4.000000 |
| 7 | 380 | 4/105 | 379.085714 | 8/35 | 2274.514286 | 6.000000 |
| 11 | 207 | 8/385 | 205.277922 | 16/77 | 2052.779221 | 10.000000 |
| 13 | 159 | 16/1001 | 157.138861 | 192/1001 | 1885.666334 | 12.000000 |
| 17 | 110 | 192/17017 | 109.567609 | 3072/17017 | 1753.081742 | 16.000000 |
| 19 | 94 | 3072/323323 | 91.583364 | 55296/323323 | 1648.500552 | 18.000000 |
| 23 | 76 | 55296/7436429 | 70.424718 | 110592/676039 | 1549.343798 | 22.000000 |
| 29 | 59 | 110592/19605131 | 51.665665 | 442368/2800733 | 1446.638616 | 28.000000 |
| 31 | 56 | 442368/86822723 | 46.054353 | 13271040/86822723 | 1381.630596 | 30.000000 |

### N=100000

| p | exact | correct density | correct main | user density | user main | user/correct |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 49999 | 1/2 | 49998.000000 | 1/2 | 49998.000000 | 1.000000 |
| 3 | 16666 | 1/6 | 16665.166667 | 1/3 | 33330.333333 | 2.000000 |
| 5 | 6666 | 1/15 | 6665.000000 | 4/15 | 26660.000000 | 4.000000 |
| 7 | 3808 | 4/105 | 3807.657143 | 8/35 | 22845.942857 | 6.000000 |
| 11 | 2077 | 8/385 | 2075.407792 | 16/77 | 20754.077922 | 10.000000 |
| 13 | 1597 | 16/1001 | 1595.700300 | 192/1001 | 19148.403596 | 12.000000 |
| 17 | 1127 | 192/17017 | 1125.022742 | 3072/17017 | 18000.363871 | 16.000000 |
| 19 | 949 | 3072/323323 | 946.703476 | 55296/323323 | 17040.662570 | 18.000000 |
| 23 | 741 | 55296/7436429 | 739.649154 | 110592/676039 | 16272.281380 | 22.000000 |
| 29 | 555 | 110592/19605131 | 559.353168 | 442368/2800733 | 15661.888696 | 28.000000 |
| 31 | 499 | 442368/86822723 | 504.610807 | 13271040/86822723 | 15138.324221 | 30.000000 |

## 4. 最新开放口

```text
PrimeDivisibilityClassIsOneOverPNotOneMinusOneOverP AND ExactLPFBucketCountIsLegendrePhiNotInclusiveSurvivalProduct AND UnsignedLPFBucketCountStillParityBlind AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_lpf_bucket_inclusive_survival_formula_audit.py` | `41f8575d06e22708ca73870d97e4412c28d49b9c3c2b6e16b52d36b6341eab42` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json` | `1e38c9ee2e7fd682eb787765eb9b5a7b9cf0b15992f1d013f75996bc01fe2bcf` |
| `docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json` | `f745ed6c597dfcceed10f50249df139235cac727fd8086737b81bb894bda3a4c` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `eac3c70ae4b07188e54640d3b27abdb499c581ae235c46f233bbe55595b5fc01` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `59aa6945ea8af6f9d9dc102fb4cf6c5cbd7745f8553f550650799b9ab16277dc` |
| `docs/monograph/external-theorem-index.md` | `a291f631ef5abb0156c1ad6046001065d48e868133324dcfa3e4c5eea4b6056f` |
