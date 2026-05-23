# Prime Matrix Phi-LPF q-support full Ramanujan spectrum obstruction 审计

**状态：** `full_ramanujan_spectrum_obstruction_closed_exact_truncation_rejected`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
unit_selector=f_W(n)=1_{gcd(n,W_P)=1} on Z/W_PZ
additive_fourier_coefficient=fhat(a)=c_{W_P}(a)/W_P
squarefree_coefficient=c_W(a)=prod_{ell|W, ell|a}(ell-1) prod_{ell|W, ell not|a}(-1)
full_support=c_{W_P}(a)!=0 for every a mod W_P
exact_truncation_conclusion=any proper additive-mode truncation changes the selector
```

## 2. 满谱审计

```text
max_prime=1009
P_value_count=165
max_full_additive_frequency_count=200560490130
max_ramanujan_divisor_terms=2048
max_sqrt_sieve_prime_count=11
max_l1_norm=27179089920/86822723
bad_frequency_count_total=0
bad_nonzero_frequency_total=0
bad_l1_formula_total=0
bad_l2_parseval_total=0
all_exact_fourier_supports_full=true
proper_exact_mode_truncation_possible_for_any_P=false
previous_ramanujan_identity_checked_total=951378
previous_ramanujan_identity_mismatch_total=0
```

代表 P：

| P | W_P | sqrt_sieve_prime_count | phi_W | unit_density | ramanujan_divisor_terms | full_additive_frequency_count | all_frequencies_nonzero | minimum_exact_modes_for_exact_fourier_selector | l1_norm | l2_norm_squared | sample_gcd_buckets |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 210 | 4 | 48 | 8/35 | 16 | 210 | true | 210 | 128/35 | 8/35 | {'g': 1, 'frequency_count': 48, 'abs_cW': 1} / {'g': 2, 'frequency_count': 48, 'abs_cW': 1} / {'g': 3, 'frequency_count': 24, 'abs_cW': 2} / {'g': 5, 'frequency_count': 12, 'abs_cW': 4} / {'g': 6, 'frequency_count': 24, 'abs_cW': 2} / {'g': 7, 'frequency_count': 8, 'abs_cW': 6} / {'g': 10, 'frequency_count': 12, 'abs_cW': 4} / {'g': 14, 'frequency_count': 8, 'abs_cW': 6} |
| 257 | 30030 | 6 | 5760 | 192/1001 | 64 | 30030 | true | 30030 | 12288/1001 | 192/1001 | {'g': 1, 'frequency_count': 5760, 'abs_cW': 1} / {'g': 2, 'frequency_count': 5760, 'abs_cW': 1} / {'g': 3, 'frequency_count': 2880, 'abs_cW': 2} / {'g': 5, 'frequency_count': 1440, 'abs_cW': 4} / {'g': 6, 'frequency_count': 2880, 'abs_cW': 2} / {'g': 7, 'frequency_count': 960, 'abs_cW': 6} / {'g': 10, 'frequency_count': 1440, 'abs_cW': 4} / {'g': 11, 'frequency_count': 576, 'abs_cW': 10} |
| 971 | 200560490130 | 11 | 30656102400 | 13271040/86822723 | 2048 | 200560490130 | true | 200560490130 | 27179089920/86822723 | 13271040/86822723 | {'g': 1, 'frequency_count': 30656102400, 'abs_cW': 1} / {'g': 2, 'frequency_count': 30656102400, 'abs_cW': 1} / {'g': 3, 'frequency_count': 15328051200, 'abs_cW': 2} / {'g': 5, 'frequency_count': 7664025600, 'abs_cW': 4} / {'g': 6, 'frequency_count': 15328051200, 'abs_cW': 2} / {'g': 7, 'frequency_count': 5109350400, 'abs_cW': 6} / {'g': 10, 'frequency_count': 7664025600, 'abs_cW': 4} / {'g': 11, 'frequency_count': 3065610240, 'abs_cW': 10} |
| 1009 | 200560490130 | 11 | 30656102400 | 13271040/86822723 | 2048 | 200560490130 | true | 200560490130 | 27179089920/86822723 | 13271040/86822723 | {'g': 1, 'frequency_count': 30656102400, 'abs_cW': 1} / {'g': 2, 'frequency_count': 30656102400, 'abs_cW': 1} / {'g': 3, 'frequency_count': 15328051200, 'abs_cW': 2} / {'g': 5, 'frequency_count': 7664025600, 'abs_cW': 4} / {'g': 6, 'frequency_count': 15328051200, 'abs_cW': 2} / {'g': 7, 'frequency_count': 5109350400, 'abs_cW': 6} / {'g': 10, 'frequency_count': 7664025600, 'abs_cW': 4} / {'g': 11, 'frequency_count': 3065610240, 'abs_cW': 10} |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AdditiveFourierFullSupportForPrimorialUnitSelector | true | true | For squarefree W_P every additive Fourier coefficient c_{W_P}(a)/W_P is nonzero. | none |
| ExactRamanujanModeTruncationRejected | true | true | No proper subset of additive modes can reproduce the exact W_P-unit selector. | none |
| RamanujanSpectrumL1L2Ledger | true | true | The full-spectrum L1 and Parseval L2 ledgers are explicit and match product formulas. | none |
| UniformCancellationAcrossFullDynamicRamanujanSpectrum | false | false | Prove cancellation after keeping the full W_P dynamic frequency spectrum. | new full-spectrum cancellation theorem |
| DynamicFullRamanujanSpectrumToUsableKloostermanCompletionBridge | false | false | Organise the full dynamic spectrum into a same-object completed Kloosterman or Type-II family. | new completion bridge |
| RoughBetaSiegelWalfiszUniformityOrReplacement | false | false | Supply the equidistribution/SW factor or an object-specific replacement for rough beta weights. | rough beta uniformity input |

## 4. 外部 theorem 影响

```text
Wright_2026_arXiv_2604_25177=trilinear Kloosterman fractions still need a completed coefficient family; full W_P spectrum is not already organised
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459=bilinear trace-function technology is relevant after sheaf/trace-family packaging, but the current full W_P spectrum lacks that packaging
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-q bilinear Kloosterman estimates still require admissible bilinear ranges and coefficients
Pascadi_2025_arXiv_2511_08445=composite-modulus amplification still needs Type-II organisation beyond raw dynamic Fourier support
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree Kloosterman parameter sums are adjacent but do not estimate this pointwise P,k full-spectrum selector
Dong_Robles_Zeindler_2026_arXiv_2601_00292=withdrawn; not usable as an external input
```

结论：精确加性 Fourier 支撑是满的。Ramanujan 展开不能靠丢弃大多数模式成为 completed Kloosterman 输入；若要继续，必须对完整动态谱建立同对象 completion 与抵消。

## 5. 最新最窄口

```text
DynamicFullRamanujanSpectrumToUsableKloostermanCompletionBridge
AND UniformCancellationAcrossFullDynamicRamanujanSpectrum
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
full_ramanujan_spectrum_obstruction_closed=true
additive_fourier_full_support_proved=true
exact_mode_truncation_rejected=true
full_spectrum_cancellation_closed=false
usable_kloosterman_completion_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
