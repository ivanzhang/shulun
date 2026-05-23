# Prime Matrix Phi-LPF q-support LPF bucket completion bridge 审计

**状态：** `lpf_bucket_normal_form_closed_completion_bridge_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
phase_sum=sum_{q in S(P,k)} e(h*kP/q)
support_predicate=q in S(P,k) iff the unique odd candidate omega_{P,k}(q) is composite with LPF(omega)>=7
lpf_bucket_formula=1_S(q)=sum_{7<=r<=sqrt(omega), r prime, r|omega} 1_{P^-(omega)>=r} 1_{omega/r>=r}
rough_mobius_inner_sum=1_{P^-(omega)>=r}=sum_{d|omega, P^+(d)<r} mu(d)
product_window_shape=kP < q*r*beta < (k+1)P with beta=omega/r and P^-(beta)>=r
```

## 2. 有限 LPF 桶审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_prime_q_instances=3874554
total_odd_candidate_instances=1266932
total_residual_support_instances=299977
total_lpf_bucket_terms=299977
actual_support_equals_lpf_bucket_terms=true
max_terms_per_candidate=1
max_reverse_prime_count_per_lpf_bucket=1
bad_candidate_count=0
bad_bucket_formula_total=0
bad_reverse_window_total=0
r_bucket_totals={7: 96700, 11: 52080, 13: 44104, 17: 34414, 19: 29723, 23: 22368, 29: 11815, 31: 6916, 37: 1559, 41: 262, 43: 36}
```

代表行：

| P | k | prime_q_count | odd_candidate_count | residual_support_count | lpf_bucket_terms_total | max_reverse_prime_count | r_bucket_totals | sample_terms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 10 | 7 | 1 | 1 | 1 | 11:1 | q=71,omega=143,r=11,beta=13,reverse_prime_count=1 |
| 257 | 256 | 23 | 16 | 3 | 3 | 1 | 11:1, 13:1, 19:1 | q=137,omega=481,r=13,beta=37,reverse_prime_count=1; q=151,omega=437,r=19,beta=23,reverse_prime_count=1; q=193,omega=341,r=11,beta=31,reverse_prime_count=1 |
| 971 | 936 | 71 | 49 | 23 | 23 | 1 | 7:6, 11:4, 13:2, 17:6, 19:1, 23:2, 37:1, 41:1 | q=491,omega=1853,r=17,beta=109,reverse_prime_count=1; q=503,omega=1807,r=13,beta=139,reverse_prime_count=1; q=523,omega=1739,r=37,beta=47,reverse_prime_count=1; q=541,omega=1681,r=41,beta=41,reverse_prime_count=1; q=557,omega=1633,r=23,beta=71,reverse_prime_count=1 |
| 1009 | 1008 | 72 | 54 | 9 | 9 | 1 | 7:1, 11:1, 13:2, 17:1, 23:1, 31:1, 37:1, 41:1 | q=563,omega=1807,r=13,beta=139,reverse_prime_count=1; q=577,omega=1763,r=41,beta=43,reverse_prime_count=1; q=617,omega=1649,r=17,beta=97,reverse_prime_count=1; q=647,omega=1573,r=11,beta=143,reverse_prime_count=1; q=743,omega=1369,r=37,beta=37,reverse_prime_count=1 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| QSupportUniqueOddCandidateLPFBucketNormalForm | true | true | The actual q-support predicate is exactly a unique LPF bucket over the odd candidate omega_{P,k}(q). | none |
| RoughMobiusLPFBucketIdentityForQSupport | true | true | The LPF bucket can be written as a rough-Mobius inner sum over primes below r. | none |
| SparseProductWindowGraphNormalForm | true | true | Every support term is a sparse product-window triple (q,r,beta) with max reverse prime multiplicity one. | none |
| NaiveDenseDyadicConvolutionCompletionRejected | true | true | The product-window graph is sparse and pointwise; treating it as a dense completed convolution would add non-object terms. | none |
| SparseLPFBucketProductWindowGraphToCompletedKloostermanConvolutionBridge | false | false | Construct a same-object bridge from sparse product-window triples to a completed bilinear/trilinear Kloosterman family. | new bridge theorem |
| RoughBetaSiegelWalfiszUniformityOrReplacement | false | false | Provide the SW/equidistribution factor required by external trilinear theorems, or replace it by an object-specific theorem. | rough beta uniformity input |

## 4. 外部 theorem 影响

```text
Wright_2026=still requires completed convolution plus equidistributed/SW factor
Milicevic_Qin_Wu_2025=still requires admissible bilinear Kloosterman coefficients
Pascadi_2025=still requires Type-II organisation over the target modulus family
Ford_Maynard_2024=still requires object-specific Type-I/II inputs before sieve positivity
```

结论：本层真推进是把 q-support 谓词压成唯一 LPF 桶和 sparse product-window graph；但这仍不是 completed Kloosterman convolution。直接把稀疏图填充成密集 dyadic convolution 会加入非同对象项。

## 5. 最新最窄口

```text
SparseLPFBucketProductWindowGraphToCompletedKloostermanConvolutionBridge
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
lpf_bucket_normal_form_closed=true
rough_mobius_identity_closed=true
sparse_product_window_normal_form_closed=true
dense_completed_convolution_available=false
siegel_walfisz_factor_extracted=false
same_object_kloosterman_bridge_closed=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
