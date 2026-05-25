# Prime Matrix Phi-LPF Legendre-Phi periodic truncation error 审计

**状态：** `legendre_phi_truncation_error_is_periodic_boundary_not_half_main`
**核验日期：** `2026-05-25`

## 1. 严格公式

设

```text
W_<p = prod_{q<p} q.
```

则 Legendre-Phi 粗数计数有完整周期分解：

```text
Phi(x; primes<p) = floor(x/W_<p)*phi(W_<p) + R_p(x mod W_<p).
```

因此 composite LPF bucket 不是一个带固定半主项误差的欧拉乘积估计，而是：

```text
C_p(N)=Phi(floor(N/p); primes<p)-Phi(p-1; primes<p)
      =(floor(N/p)-p+1)*phi(W_<p)/W_<p
       + B_p(floor(N/p))-B_p(p-1),
|B_p(t)| <= phi(W_<p).
```

这说明截断误差是 primorial 周期余数边界项，不是普遍的 `1/2 main`。

## 2. 全局读数

```text
legendre_phi_periodic_truncation_error_closed=true
exact_lpf_bucket_identity_closed=true
half_main_truncation_error_claim_supported=false
truncation_error_is_periodic_residue_boundary=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| N | exact total | composite count | endpoint main/exact | n-axis main/exact | half-like buckets |
| --- | --- | --- | --- | --- | --- |
| 100 | 74 | 74 | 0.972523 | 0.947426 | 0 |
| 1000 | 831 | 831 | 0.982873 | 0.980306 | 0 |
| 10000 | 8770 | 8770 | 0.986211 | 0.985832 | 4 |
| 100000 | 90407 | 90407 | 0.988373 | 0.988315 | 10 |

## 3. 样本 bucket

### N=100

| p | exact | density | endpoint main | endpoint error | n-axis main | n-axis error | W_<p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 49 | 1 | 49.000000 | 0.000000 | 48.000000 | 1.000000 | 1 |
| 3 | 16 | 1/2 | 15.500000 | 0.500000 | 15.166667 | 0.833333 | 2 |
| 5 | 6 | 1/3 | 5.333333 | 0.666667 | 5.000000 | 1.000000 | 6 |
| 7 | 3 | 4/15 | 2.133333 | 0.866667 | 1.942857 | 1.057143 | 30 |

### N=1000

| p | exact | density | endpoint main | endpoint error | n-axis main | n-axis error | W_<p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 499 | 1 | 499.000000 | 0.000000 | 498.000000 | 1.000000 | 1 |
| 3 | 166 | 1/2 | 165.500000 | 0.500000 | 165.166667 | 0.833333 | 2 |
| 5 | 66 | 1/3 | 65.333333 | 0.666667 | 65.000000 | 1.000000 | 6 |
| 7 | 37 | 4/15 | 36.266667 | 0.733333 | 36.228571 | 0.771429 | 30 |
| 11 | 20 | 8/35 | 18.285714 | 1.714286 | 18.264935 | 1.735065 | 210 |
| 13 | 16 | 16/77 | 13.298701 | 2.701299 | 13.282717 | 2.717283 | 2310 |
| 17 | 10 | 192/1001 | 8.055944 | 1.944056 | 8.022096 | 1.977904 | 30030 |
| 19 | 8 | 3072/17017 | 6.137862 | 1.862138 | 6.071353 | 1.928647 | 510510 |
| 23 | 6 | 55296/323323 | 3.591504 | 2.408496 | 3.502275 | 2.497725 | 9699690 |
| 29 | 2 | 110592/676039 | 0.981529 | 1.018471 | 0.896915 | 1.103085 | 223092870 |
| 31 | 1 | 442368/2800733 | 0.315894 | 0.684106 | 0.198708 | 0.801292 | 6469693230 |

### N=10000

| p | exact | density | endpoint main | endpoint error | n-axis main | n-axis error | W_<p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4999 | 1 | 4999.000000 | 0.000000 | 4998.000000 | 1.000000 | 1 |
| 3 | 1666 | 1/2 | 1665.500000 | 0.500000 | 1665.166667 | 0.833333 | 2 |
| 5 | 666 | 1/3 | 665.333333 | 0.666667 | 665.000000 | 1.000000 | 6 |
| 7 | 380 | 4/15 | 379.200000 | 0.800000 | 379.085714 | 0.914286 | 30 |
| 11 | 207 | 8/35 | 205.485714 | 1.514286 | 205.277922 | 1.722078 | 210 |
| 13 | 159 | 16/77 | 157.298701 | 1.701299 | 157.138861 | 1.861139 | 2310 |
| 17 | 110 | 192/1001 | 109.714286 | 0.285714 | 109.567609 | 0.432391 | 30030 |
| 19 | 94 | 3072/17017 | 91.706881 | 2.293119 | 91.583364 | 2.416636 | 510510 |
| 23 | 76 | 55296/323323 | 70.461897 | 5.538103 | 70.424718 | 5.575282 | 9699690 |
| 29 | 59 | 110592/676039 | 51.693870 | 7.306130 | 51.665665 | 7.334335 | 223092870 |
| 31 | 56 | 442368/2800733 | 46.120589 | 9.879411 | 46.054353 | 9.945647 | 6469693230 |

### N=100000

| p | exact | density | endpoint main | endpoint error | n-axis main | n-axis error | W_<p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 49999 | 1 | 49999.000000 | 0.000000 | 49998.000000 | 1.000000 | 1 |
| 3 | 16666 | 1/2 | 16665.500000 | 0.500000 | 16665.166667 | 0.833333 | 2 |
| 5 | 6666 | 1/3 | 6665.333333 | 0.666667 | 6665.000000 | 1.000000 | 6 |
| 7 | 3808 | 4/15 | 3807.733333 | 0.266667 | 3807.657143 | 0.342857 | 30 |
| 11 | 2077 | 8/35 | 2075.428571 | 1.571429 | 2075.407792 | 1.592208 | 210 |
| 13 | 1597 | 16/77 | 1595.844156 | 1.155844 | 1595.700300 | 1.299700 | 2310 |
| 17 | 1127 | 192/1001 | 1125.146853 | 1.853147 | 1125.022742 | 1.977258 | 30030 |
| 19 | 949 | 3072/17017 | 946.855497 | 2.144503 | 946.703476 | 2.296524 | 510510 |
| 23 | 741 | 55296/323323 | 739.678897 | 1.321103 | 739.649154 | 1.350846 | 9699690 |
| 29 | 555 | 110592/676039 | 559.471628 | -4.471628 | 559.353168 | -4.353168 | 223092870 |
| 31 | 499 | 442368/2800733 | 504.641378 | -5.641378 | 504.610807 | -5.610807 | 6469693230 |

## 4. 外部前沿可用性

| input | url | current role | direct close |
| --- | --- | --- | --- |
| Milićević-Qin-Wu bilinear Kloosterman sums | https://arxiv.org/abs/2511.07550 | usable only after a genuine two-variable Kloosterman family is constructed | `false` |
| Zheng primes in simultaneous arithmetic progressions | https://arxiv.org/abs/2512.22798 | candidate only after the two AP constraints are matched to the same signed family | `false` |
| Runbo Li large-modulus AP primes and Harman sieve refinements | https://arxiv.org/abs/2602.20917 | average-modulus input, not pointwise row-column positivity at x=P^2 | `false` |
| Wright trilinear Kloosterman fractions | https://arxiv.org/abs/2604.25177 | requires a trilinear convolution and equidistributed coefficient sequence | `false` |
| Becker-Breuillard spectral gaps and anti-concentration | https://arxiv.org/abs/2512.15364 | requires a genuine finite-group orbit or thin-group sieve model | `false` |

## 5. 最新开放口

```text
LegendrePhiTruncationErrorIsPeriodicBoundaryNotHalfMain AND UnsignedLPFBucketCountStillParityBlind AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_legendre_phi_periodic_truncation_error_audit.py` | `3bbb00fcea2bbe1363786e7436afb7b3f4a07e7d913121183437119426d48905` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json` | `1e38c9ee2e7fd682eb787765eb9b5a7b9cf0b15992f1d013f75996bc01fe2bcf` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.json` | `c823b4fd173f4ae1fcda94ed70585bad15d0ddbc90819886325307beff6313d8` |
| `docs/monograph/prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json` | `6f0a674fbf664cebc3a17c49a62fb8757a8ca3dd004403d023c0fc1746c23ecc` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `9c76133d3704ae401b00da84d26103deda85332a352bd302b202baada1bac90b` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `12a209bdcd2bc4688a98e3c081d44756714b121b877c2696632c89cf4ab4c00a` |
| `docs/monograph/external-theorem-index.md` | `9ee5ffdc7251ae81634d346ee32385d9458d2e9c65ce5598c1d21d7c4d12d72b` |
