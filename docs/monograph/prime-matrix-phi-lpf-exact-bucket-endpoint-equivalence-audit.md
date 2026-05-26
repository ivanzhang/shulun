# Prime Matrix Phi-LPF exact bucket endpoint equivalence 审计

**状态：** `exact_lpf_bucket_endpoint_singleton_and_floor_boundary_fixed`
**核验日期：** `2026-05-25`

## 1. 修正后的精确公式层级

两种精确写法完全等价：

```text
C_p(N)=Phi(floor(N/p); primes<p)-1
      =Phi(floor(N/p); primes<p)-Phi(p-1; primes<p),
Phi(p-1; primes<p)=1.
```

真正需要修正的是：不能把连续欧拉乘积主项当作精确计数。下面只是连续主项：

```text
(N-p^2)*(1/p)*prod_{q<p}(1-1/q).
```

精确计算必须保留 `floor(N/p)`、端点 singleton，以及上一轮证书中的 primorial 周期边界项。

## 2. 全局读数

```text
exact_endpoint_singleton_fixed=true
minus_one_and_endpoint_forms_equivalent=true
exact_lpf_bucket_identity_closed=true
continuous_euler_main_is_exact_count=false
floor_endpoint_and_periodic_boundary_required=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| N | exact total | composite count | endpoint singleton | endpoint formula | first continuous mismatch p |
| --- | --- | --- | --- | --- | --- |
| 30 | 19 | 19 | `true` | `true` | 2 |
| 100 | 74 | 74 | `true` | `true` | 2 |
| 1000 | 831 | 831 | `true` | `true` | 2 |
| 10000 | 8770 | 8770 | `true` | `true` | 2 |
| 100000 | 90407 | 90407 | `true` | `true` | 2 |

## 3. 样本 bucket

### N=30

| p | scan exact | Phi(X)-1 | Phi(X)-Phi(p-1) | Phi(p-1) | continuous main | continuous error |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 14 | 14 | 14 | 1 | 13.000000 | 1.000000 |
| 3 | 4 | 4 | 4 | 1 | 3.500000 | 0.500000 |
| 5 | 1 | 1 | 1 | 1 | 0.333333 | 0.666667 |

### N=100

| p | scan exact | Phi(X)-1 | Phi(X)-Phi(p-1) | Phi(p-1) | continuous main | continuous error |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 49 | 49 | 49 | 1 | 48.000000 | 1.000000 |
| 3 | 16 | 16 | 16 | 1 | 15.166667 | 0.833333 |
| 5 | 6 | 6 | 6 | 1 | 5.000000 | 1.000000 |
| 7 | 3 | 3 | 3 | 1 | 1.942857 | 1.057143 |

### N=1000

| p | scan exact | Phi(X)-1 | Phi(X)-Phi(p-1) | Phi(p-1) | continuous main | continuous error |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 499 | 499 | 499 | 1 | 498.000000 | 1.000000 |
| 3 | 166 | 166 | 166 | 1 | 165.166667 | 0.833333 |
| 5 | 66 | 66 | 66 | 1 | 65.000000 | 1.000000 |
| 7 | 37 | 37 | 37 | 1 | 36.228571 | 0.771429 |
| 11 | 20 | 20 | 20 | 1 | 18.264935 | 1.735065 |
| 13 | 16 | 16 | 16 | 1 | 13.282717 | 2.717283 |
| 17 | 10 | 10 | 10 | 1 | 8.022096 | 1.977904 |
| 19 | 8 | 8 | 8 | 1 | 6.071353 | 1.928647 |
| 23 | 6 | 6 | 6 | 1 | 3.502275 | 2.497725 |
| 29 | 2 | 2 | 2 | 1 | 0.896915 | 1.103085 |
| 31 | 1 | 1 | 1 | 1 | 0.198708 | 0.801292 |

### N=10000

| p | scan exact | Phi(X)-1 | Phi(X)-Phi(p-1) | Phi(p-1) | continuous main | continuous error |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 4999 | 4999 | 4999 | 1 | 4998.000000 | 1.000000 |
| 3 | 1666 | 1666 | 1666 | 1 | 1665.166667 | 0.833333 |
| 5 | 666 | 666 | 666 | 1 | 665.000000 | 1.000000 |
| 7 | 380 | 380 | 380 | 1 | 379.085714 | 0.914286 |
| 11 | 207 | 207 | 207 | 1 | 205.277922 | 1.722078 |
| 13 | 159 | 159 | 159 | 1 | 157.138861 | 1.861139 |
| 17 | 110 | 110 | 110 | 1 | 109.567609 | 0.432391 |
| 19 | 94 | 94 | 94 | 1 | 91.583364 | 2.416636 |
| 23 | 76 | 76 | 76 | 1 | 70.424718 | 5.575282 |
| 29 | 59 | 59 | 59 | 1 | 51.665665 | 7.334335 |
| 31 | 56 | 56 | 56 | 1 | 46.054353 | 9.945647 |

### N=100000

| p | scan exact | Phi(X)-1 | Phi(X)-Phi(p-1) | Phi(p-1) | continuous main | continuous error |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 49999 | 49999 | 49999 | 1 | 49998.000000 | 1.000000 |
| 3 | 16666 | 16666 | 16666 | 1 | 16665.166667 | 0.833333 |
| 5 | 6666 | 6666 | 6666 | 1 | 6665.000000 | 1.000000 |
| 7 | 3808 | 3808 | 3808 | 1 | 3807.657143 | 0.342857 |
| 11 | 2077 | 2077 | 2077 | 1 | 2075.407792 | 1.592208 |
| 13 | 1597 | 1597 | 1597 | 1 | 1595.700300 | 1.299700 |
| 17 | 1127 | 1127 | 1127 | 1 | 1125.022742 | 1.977258 |
| 19 | 949 | 949 | 949 | 1 | 946.703476 | 2.296524 |
| 23 | 741 | 741 | 741 | 1 | 739.649154 | 1.350846 |
| 29 | 555 | 555 | 555 | 1 | 559.353168 | -4.353168 |
| 31 | 499 | 499 | 499 | 1 | 504.610807 | -5.610807 |

## 4. 最新开放口

```text
ExactLPFBucketEndpointSingletonFixed AND FloorEndpointAndPeriodicBoundaryRetained AND ContinuousEulerMainNotExactCount AND UnsignedLPFBucketCountStillParityBlind AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_exact_bucket_endpoint_equivalence_audit.py` | `a648a00877c672995be692ee2f87ff80f3be494cc81177288c12a310db4968d0` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json` | `1e38c9ee2e7fd682eb787765eb9b5a7b9cf0b15992f1d013f75996bc01fe2bcf` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.json` | `c823b4fd173f4ae1fcda94ed70585bad15d0ddbc90819886325307beff6313d8` |
| `docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json` | `975aa118af686bd729414f291af1efd9fa60082d622ac687d7f87772246acd6e` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `c6a7d99f076be632ab2065cd790461a3da67ef605e10a93fdd087aeda3ebb893` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `80b0e5d12072b810ccf52d7a0b54e5ecaa73c504e05e320b34aafe001629c58e` |
| `docs/monograph/external-theorem-index.md` | `c149325eb6e493afa223a2e50ece2fc489fa06dc58316e4788e61fff1cc46ac1` |
