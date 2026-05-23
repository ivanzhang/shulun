# Prime Matrix Phi-LPF q-support dynamic Ramanujan unit expansion 审计

**状态：** `dynamic_ramanujan_unit_expansion_closed_usable_kloosterman_bridge_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
dynamic_primorial=W_P=product_{ell prime, ell<=sqrt(P-1)} ell
unit_selector=1_{gcd(Q_odd,W_P)=1}
ramanujan_expansion=1_{(n,W)=1}=phi(W)/W * sum_{d|W} mu(d)c_d(n)/phi(d)
local_factor=for ell|W, local factor is (ell-1)/ell*(1-c_ell(n)/(ell-1))
full_additive_opening=c_d(n)=sum_{a mod d, (a,d)=1} e(a*n/d), so total modes sum_{d|W}phi(d)=W
phase_after_expansion=e(h*kP/Q_odd) multiplied by dynamic Ramanujan modes e(a*Q_odd/d)
```

## 2. 有限 Ramanujan 审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_ramanujan_identity_row_count=56196
ramanujan_product_identity_checked_total=951378
ramanujan_product_identity_mismatch_total=0
ramanujan_divisor_sum_sample_checked_total=111
ramanujan_divisor_sum_sample_mismatch_total=0
primorial_unit_selected_total=299977
primorial_unit_rejected_total=651401
max_dynamic_primorial_modulus=200560490130
max_dynamic_primorial_prime_count=11
max_ramanujan_divisor_terms_per_candidate=2048
max_full_additive_character_modes_per_candidate=200560490130
max_full_additive_mode_l1=27179089920/86822723
```

代表行：

| P | k | ramanujan_product_identity_checked | ramanujan_product_identity_mismatch | ramanujan_divisor_sum_sample_checked | ramanujan_divisor_sum_sample_mismatch | dynamic_primorial_modulus | ramanujan_divisor_terms | full_additive_character_modes | sample_ramanujan_atoms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 3 | 0 | 3 | 0 | 210 | 16 | 210 | {'m': 119, 'r': 7, 'beta': 17, 'Q_odd': 85, 'gcd_Q_W': 5, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 143, 'r': 11, 'beta': 13, 'Q_odd': 71, 'gcd_Q_W': 1, 'expected_unit': 1, 'local_product': '1', 'divisor_sum': '1'} / {'m': 161, 'r': 7, 'beta': 23, 'Q_odd': 63, 'gcd_Q_W': 21, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} |
| 257 | 256 | 8 | 0 | 8 | 0 | 30030 | 64 | 30030 | {'m': 259, 'r': 7, 'beta': 37, 'Q_odd': 255, 'gcd_Q_W': 15, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 301, 'r': 7, 'beta': 43, 'Q_odd': 219, 'gcd_Q_W': 3, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 319, 'r': 11, 'beta': 29, 'Q_odd': 207, 'gcd_Q_W': 3, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 341, 'r': 11, 'beta': 31, 'Q_odd': 193, 'gcd_Q_W': 1, 'expected_unit': 1, 'local_product': '1', 'divisor_sum': '1'} / {'m': 377, 'r': 13, 'beta': 29, 'Q_odd': 175, 'gcd_Q_W': 35, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} |
| 971 | 936 | 49 | 0 | 49 | 0 | 200560490130 | 2048 | 200560490130 | {'m': 973, 'r': 7, 'beta': 139, 'Q_odd': 935, 'gcd_Q_W': 935, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 979, 'r': 11, 'beta': 89, 'Q_odd': 929, 'gcd_Q_W': 1, 'expected_unit': 1, 'local_product': '1', 'divisor_sum': '1'} / {'m': 989, 'r': 23, 'beta': 43, 'Q_odd': 919, 'gcd_Q_W': 1, 'expected_unit': 1, 'local_product': '1', 'divisor_sum': '1'} / {'m': 1003, 'r': 17, 'beta': 59, 'Q_odd': 907, 'gcd_Q_W': 1, 'expected_unit': 1, 'local_product': '1', 'divisor_sum': '1'} / {'m': 1007, 'r': 19, 'beta': 53, 'Q_odd': 903, 'gcd_Q_W': 21, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} |
| 1009 | 1008 | 51 | 0 | 51 | 0 | 200560490130 | 2048 | 200560490130 | {'m': 1027, 'r': 13, 'beta': 79, 'Q_odd': 991, 'gcd_Q_W': 1, 'expected_unit': 1, 'local_product': '1', 'divisor_sum': '1'} / {'m': 1037, 'r': 17, 'beta': 61, 'Q_odd': 981, 'gcd_Q_W': 3, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 1057, 'r': 7, 'beta': 151, 'Q_odd': 963, 'gcd_Q_W': 3, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 1079, 'r': 13, 'beta': 83, 'Q_odd': 943, 'gcd_Q_W': 23, 'expected_unit': 0, 'local_product': '0', 'divisor_sum': '0'} / {'m': 1081, 'r': 23, 'beta': 47, 'Q_odd': 941, 'gcd_Q_W': 1, 'expected_unit': 1, 'local_product': '1', 'divisor_sum': '1'} |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimorialUnitRamanujanExpansionIdentity | true | true | The W_P-unit selector has the exact Ramanujan divisor expansion. | none |
| RamanujanLocalProductFactorization | true | true | For squarefree W_P the expansion factors into prime-local tests and equals the gcd selector. | none |
| FullAdditiveOpeningModeCountLedger | true | true | Opening all Ramanujan sums gives exactly sum_{d\|W_P}phi(d)=W_P additive modes. | none |
| DynamicRamanujanUnitExpansionToUsableKloostermanCompletionBridge | false | false | Turn the dynamic Ramanujan-mode expansion into a same-object completed Kloosterman or Type-II family. | new bridge theorem |
| UniformRamanujanModeCancellationOrTruncation | false | false | Control or truncate the W_P dynamic additive modes without changing the selector. | mode cancellation/truncation theorem |
| RoughBetaSiegelWalfiszUniformityOrReplacement | false | false | Supply the equidistribution/SW factor or an object-specific replacement for rough beta weights. | rough beta uniformity input |

## 4. 外部 theorem 影响

```text
Wright_2026_arXiv_2604_25177=trilinear Kloosterman fractions do not provide the dynamic Ramanujan-mode completion for W_P unit classes
Milicevic_Qin_Wu_2025_arXiv_2511_07550=bilinear Kloosterman estimates still need admissible bilinear coefficient families after completion
Pascadi_2025_arXiv_2511_08445=composite-modulus amplification still needs Type-II organisation, not a raw W_P-mode expansion
Dong_Robles_Zeindler_2026_arXiv_2601_00292=withdrawn; not usable as an external input
```

结论：本层把动态 primorial CRT 单位类继续正规化为 Ramanujan 加性字符展开，并精确记录完全打开后的动态模式规模。它没有闭合外部 Kloosterman/Type-II 桥，因为模式数等于 W_P，且 W_P 随 P 增长。

## 5. 最新最窄口

```text
DynamicRamanujanUnitExpansionToUsableKloostermanCompletionBridge
AND UniformRamanujanModeCancellationOrTruncation
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
dynamic_ramanujan_unit_expansion_closed=true
ramanujan_product_identity_globally_proved=true
ramanujan_product_identity_finitely_audited=true
full_additive_mode_count_ledger_closed=true
usable_kloosterman_completion_bridge_closed=false
uniform_ramanujan_mode_cancellation_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
