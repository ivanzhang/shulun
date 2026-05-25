# Prime Matrix Phi-LPF LPF bucket count formula 审计

**状态：** `exact_lpf_bucket_count_is_legendre_phi_not_reciprocal_density`
**核验日期：** `2026-05-25`

## 1. 结论

对 composite bucket，精确公式不是用户草式的全 reciprocal product，而是
Legendre-`Phi` 粗数计数：

```text
C_p(N) = #{n<=N composite : LPF(n)=p}
       = Phi(floor(N/p); primes < p) - 1
```

`-1` 去掉的是 `m=1`，即端点素数 `n=p`。连续主项应为：

```text
(N/p - p) * prod_{q<p}(1-1/q)
  = (N-p^2)/p * prod_{q<p}(1-1/q).
```

用户草式

```text
(N-p^2) * prod_{q<=p} 1/q
```

在 `p=2,3` 因低阶偶然相同；从 `p=5` 起把“避开 0 类”的生存密度
`1-1/q` 误写成了单类密度 `1/q`。

## 2. 全局读数

```text
exact_lpf_bucket_identity_closed=true
user_reciprocal_density_formula_supported=false
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| N | exact total | composite count | corrected total/exact | user total/exact | first wrong p |
| --- | --- | --- | --- | --- | --- |
| 100 | 74 | 74 | 0.947426 | 0.890669 | 5 |
| 1000 | 831 | 831 | 0.980306 | 0.843087 | 5 |
| 10000 | 8770 | 8770 | 0.985832 | 0.803612 | 5 |
| 100000 | 90407 | 90407 | 0.988315 | 0.780010 | 5 |

## 3. 样本 bucket

### N=100

| p | exact | correct density | corrected main | user density | user main |
| --- | --- | --- | --- | --- | --- |
| 2 | 49 | 1/2 | 48.000000 | 1/2 | 48.000000 |
| 3 | 16 | 1/6 | 15.166667 | 1/6 | 15.166667 |
| 5 | 6 | 1/15 | 5.000000 | 1/30 | 2.500000 |
| 7 | 3 | 4/105 | 1.942857 | 1/210 | 0.242857 |

### N=1000

| p | exact | correct density | corrected main | user density | user main |
| --- | --- | --- | --- | --- | --- |
| 2 | 499 | 1/2 | 498.000000 | 1/2 | 498.000000 |
| 3 | 166 | 1/6 | 165.166667 | 1/6 | 165.166667 |
| 5 | 66 | 1/15 | 65.000000 | 1/30 | 32.500000 |
| 7 | 37 | 4/105 | 36.228571 | 1/210 | 4.528571 |
| 11 | 20 | 8/385 | 18.264935 | 1/2310 | 0.380519 |
| 13 | 16 | 16/1001 | 13.282717 | 1/30030 | 0.027672 |
| 17 | 10 | 192/17017 | 8.022096 | 1/510510 | 0.001393 |
| 19 | 8 | 3072/323323 | 6.071353 | 1/9699690 | 0.000066 |
| 23 | 6 | 55296/7436429 | 3.502275 | 1/223092870 | 0.000002 |
| 29 | 2 | 110592/19605131 | 0.896915 | 1/6469693230 | 0.000000 |
| 31 | 1 | 442368/86822723 | 0.198708 | 1/200560490130 | 0.000000 |

### N=10000

| p | exact | correct density | corrected main | user density | user main |
| --- | --- | --- | --- | --- | --- |
| 2 | 4999 | 1/2 | 4998.000000 | 1/2 | 4998.000000 |
| 3 | 1666 | 1/6 | 1665.166667 | 1/6 | 1665.166667 |
| 5 | 666 | 1/15 | 665.000000 | 1/30 | 332.500000 |
| 7 | 380 | 4/105 | 379.085714 | 1/210 | 47.385714 |
| 11 | 207 | 8/385 | 205.277922 | 1/2310 | 4.276623 |
| 13 | 159 | 16/1001 | 157.138861 | 1/30030 | 0.327373 |
| 17 | 110 | 192/17017 | 109.567609 | 1/510510 | 0.019022 |
| 19 | 94 | 3072/323323 | 91.583364 | 1/9699690 | 0.000994 |
| 23 | 76 | 55296/7436429 | 70.424718 | 1/223092870 | 0.000042 |
| 29 | 59 | 110592/19605131 | 51.665665 | 1/6469693230 | 0.000001 |
| 31 | 56 | 442368/86822723 | 46.054353 | 1/200560490130 | 0.000000 |

### N=100000

| p | exact | correct density | corrected main | user density | user main |
| --- | --- | --- | --- | --- | --- |
| 2 | 49999 | 1/2 | 49998.000000 | 1/2 | 49998.000000 |
| 3 | 16666 | 1/6 | 16665.166667 | 1/6 | 16665.166667 |
| 5 | 6666 | 1/15 | 6665.000000 | 1/30 | 3332.500000 |
| 7 | 3808 | 4/105 | 3807.657143 | 1/210 | 475.957143 |
| 11 | 2077 | 8/385 | 2075.407792 | 1/2310 | 43.237662 |
| 13 | 1597 | 16/1001 | 1595.700300 | 1/30030 | 3.324376 |
| 17 | 1127 | 192/17017 | 1125.022742 | 1/510510 | 0.195316 |
| 19 | 949 | 3072/323323 | 946.703476 | 1/9699690 | 0.010272 |
| 23 | 741 | 55296/7436429 | 739.649154 | 1/223092870 | 0.000446 |
| 29 | 555 | 110592/19605131 | 559.353168 | 1/6469693230 | 0.000015 |
| 31 | 499 | 442368/86822723 | 504.610807 | 1/200560490130 | 0.000000 |

## 4. 最新开放口

```text
ExactLPFBucketCountIsLegendrePhiNotReciprocalDensity AND UnsignedLPFBucketCountStillParityBlind AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount AND PointwiseThetaAPPositivityAtP2OrAdmissibleSignedDivisorPayloadTypeIIFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_lpf_bucket_count_formula_audit.py` | `785b6e5bb93b05850244471f54e939764f04279c78feb5f1236e9979d5e69913` |
| `docs/monograph/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.json` | `984f9ab9a328383ff5f21275dcf054fae0ed8e4349170bf2c7f70d53a4e2c251` |
| `docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json` | `f745ed6c597dfcceed10f50249df139235cac727fd8086737b81bb894bda3a4c` |
| `docs/monograph/prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json` | `6f0a674fbf664cebc3a17c49a62fb8757a8ca3dd004403d023c0fc1746c23ecc` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `4f68a59e235fb0f7a9f39f9f4686d30a47d63d554b2aad4571510c188cd1aad5` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `d20df0ea7a6aedc816a135e2c5fc39c19fb085c17c339480977d47ffa6ccad79` |
