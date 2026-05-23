# Prime Matrix Phi-LPF q-support conductor-stratified Ramanujan spectrum 审计

**状态：** `conductor_stratified_full_spectrum_closed_low_conductor_truncation_rejected`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
frequency_conductor=q=W_P/gcd(a,W_P)
coefficient_by_conductor=c_W(a)/W = mu(q)*phi(W)/(W*phi(q))
primitive_frequency_count=there are phi(q) frequencies of exact conductor q
layer_l1=sum over exact conductor q of |c_W(a)|/W equals phi(W)/W
truncation_conclusion=dropping any conductor layer changes the exact selector and does not remove a small-mass tail
```

## 2. Conductor 分层审计

```text
max_prime=1009
P_value_count=165
max_conductor_layer_count=2048
max_full_additive_frequency_count=200560490130
max_sqrt_sieve_prime_count=11
bad_frequency_count_total=0
bad_layer_l1_equality_total=0
bad_total_l1_formula_total=0
bad_total_l2_parseval_total=0
all_conductor_strata_nonempty_and_equal_l1=true
proper_conductor_layer_truncation_exact_possible_for_any_P=false
previous_max_full_additive_frequency_count=200560490130
previous_bad_nonzero_frequency_total=0
```

代表 P：

| P | W_P | sqrt_sieve_prime_count | conductor_layer_count | full_additive_frequency_count | all_layer_l1_equal | common_layer_l1 | total_l1 | small_conductor_cut_sqrtW | small_conductor_layer_count | small_conductor_l1_fraction | sample_conductor_layers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 210 | 4 | 16 | 210 | true | 8/35 | 128/35 | 14 | 8 | 1/2 | {'conductor': 1, 'prime_count': 0, 'primitive_frequency_count': 1, 'coefficient': '8/35', 'coefficient_abs': '8/35', 'layer_l1': '8/35', 'layer_l2': '64/1225', 'signed_layer': 'positive'} / {'conductor': 2, 'prime_count': 1, 'primitive_frequency_count': 1, 'coefficient': '-8/35', 'coefficient_abs': '8/35', 'layer_l1': '8/35', 'layer_l2': '64/1225', 'signed_layer': 'negative'} / {'conductor': 3, 'prime_count': 1, 'primitive_frequency_count': 2, 'coefficient': '-4/35', 'coefficient_abs': '4/35', 'layer_l1': '8/35', 'layer_l2': '32/1225', 'signed_layer': 'negative'} / {'conductor': 5, 'prime_count': 1, 'primitive_frequency_count': 4, 'coefficient': '-2/35', 'coefficient_abs': '2/35', 'layer_l1': '8/35', 'layer_l2': '16/1225', 'signed_layer': 'negative'} / {'conductor': 6, 'prime_count': 2, 'primitive_frequency_count': 2, 'coefficient': '4/35', 'coefficient_abs': '4/35', 'layer_l1': '8/35', 'layer_l2': '32/1225', 'signed_layer': 'positive'} / {'conductor': 7, 'prime_count': 1, 'primitive_frequency_count': 6, 'coefficient': '-4/105', 'coefficient_abs': '4/105', 'layer_l1': '8/35', 'layer_l2': '32/3675', 'signed_layer': 'negative'} / {'conductor': 10, 'prime_count': 2, 'primitive_frequency_count': 4, 'coefficient': '2/35', 'coefficient_abs': '2/35', 'layer_l1': '8/35', 'layer_l2': '16/1225', 'signed_layer': 'positive'} / {'conductor': 14, 'prime_count': 2, 'primitive_frequency_count': 6, 'coefficient': '4/105', 'coefficient_abs': '4/105', 'layer_l1': '8/35', 'layer_l2': '32/3675', 'signed_layer': 'positive'} |
| 257 | 30030 | 6 | 64 | 30030 | true | 192/1001 | 12288/1001 | 173 | 32 | 1/2 | {'conductor': 1, 'prime_count': 0, 'primitive_frequency_count': 1, 'coefficient': '192/1001', 'coefficient_abs': '192/1001', 'layer_l1': '192/1001', 'layer_l2': '36864/1002001', 'signed_layer': 'positive'} / {'conductor': 2, 'prime_count': 1, 'primitive_frequency_count': 1, 'coefficient': '-192/1001', 'coefficient_abs': '192/1001', 'layer_l1': '192/1001', 'layer_l2': '36864/1002001', 'signed_layer': 'negative'} / {'conductor': 3, 'prime_count': 1, 'primitive_frequency_count': 2, 'coefficient': '-96/1001', 'coefficient_abs': '96/1001', 'layer_l1': '192/1001', 'layer_l2': '18432/1002001', 'signed_layer': 'negative'} / {'conductor': 5, 'prime_count': 1, 'primitive_frequency_count': 4, 'coefficient': '-48/1001', 'coefficient_abs': '48/1001', 'layer_l1': '192/1001', 'layer_l2': '9216/1002001', 'signed_layer': 'negative'} / {'conductor': 6, 'prime_count': 2, 'primitive_frequency_count': 2, 'coefficient': '96/1001', 'coefficient_abs': '96/1001', 'layer_l1': '192/1001', 'layer_l2': '18432/1002001', 'signed_layer': 'positive'} / {'conductor': 7, 'prime_count': 1, 'primitive_frequency_count': 6, 'coefficient': '-32/1001', 'coefficient_abs': '32/1001', 'layer_l1': '192/1001', 'layer_l2': '6144/1002001', 'signed_layer': 'negative'} / {'conductor': 10, 'prime_count': 2, 'primitive_frequency_count': 4, 'coefficient': '48/1001', 'coefficient_abs': '48/1001', 'layer_l1': '192/1001', 'layer_l2': '9216/1002001', 'signed_layer': 'positive'} / {'conductor': 11, 'prime_count': 1, 'primitive_frequency_count': 10, 'coefficient': '-96/5005', 'coefficient_abs': '96/5005', 'layer_l1': '192/1001', 'layer_l2': '18432/5010005', 'signed_layer': 'negative'} |
| 971 | 200560490130 | 11 | 2048 | 200560490130 | true | 13271040/86822723 | 27179089920/86822723 | 447839 | 1024 | 1/2 | {'conductor': 1, 'prime_count': 0, 'primitive_frequency_count': 1, 'coefficient': '13271040/86822723', 'coefficient_abs': '13271040/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '176120502681600/7538185229134729', 'signed_layer': 'positive'} / {'conductor': 2, 'prime_count': 1, 'primitive_frequency_count': 1, 'coefficient': '-13271040/86822723', 'coefficient_abs': '13271040/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '176120502681600/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 3, 'prime_count': 1, 'primitive_frequency_count': 2, 'coefficient': '-6635520/86822723', 'coefficient_abs': '6635520/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '88060251340800/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 5, 'prime_count': 1, 'primitive_frequency_count': 4, 'coefficient': '-3317760/86822723', 'coefficient_abs': '3317760/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '44030125670400/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 6, 'prime_count': 2, 'primitive_frequency_count': 2, 'coefficient': '6635520/86822723', 'coefficient_abs': '6635520/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '88060251340800/7538185229134729', 'signed_layer': 'positive'} / {'conductor': 7, 'prime_count': 1, 'primitive_frequency_count': 6, 'coefficient': '-2211840/86822723', 'coefficient_abs': '2211840/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '29353417113600/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 10, 'prime_count': 2, 'primitive_frequency_count': 4, 'coefficient': '3317760/86822723', 'coefficient_abs': '3317760/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '44030125670400/7538185229134729', 'signed_layer': 'positive'} / {'conductor': 11, 'prime_count': 1, 'primitive_frequency_count': 10, 'coefficient': '-1327104/86822723', 'coefficient_abs': '1327104/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '17612050268160/7538185229134729', 'signed_layer': 'negative'} |
| 1009 | 200560490130 | 11 | 2048 | 200560490130 | true | 13271040/86822723 | 27179089920/86822723 | 447839 | 1024 | 1/2 | {'conductor': 1, 'prime_count': 0, 'primitive_frequency_count': 1, 'coefficient': '13271040/86822723', 'coefficient_abs': '13271040/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '176120502681600/7538185229134729', 'signed_layer': 'positive'} / {'conductor': 2, 'prime_count': 1, 'primitive_frequency_count': 1, 'coefficient': '-13271040/86822723', 'coefficient_abs': '13271040/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '176120502681600/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 3, 'prime_count': 1, 'primitive_frequency_count': 2, 'coefficient': '-6635520/86822723', 'coefficient_abs': '6635520/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '88060251340800/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 5, 'prime_count': 1, 'primitive_frequency_count': 4, 'coefficient': '-3317760/86822723', 'coefficient_abs': '3317760/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '44030125670400/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 6, 'prime_count': 2, 'primitive_frequency_count': 2, 'coefficient': '6635520/86822723', 'coefficient_abs': '6635520/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '88060251340800/7538185229134729', 'signed_layer': 'positive'} / {'conductor': 7, 'prime_count': 1, 'primitive_frequency_count': 6, 'coefficient': '-2211840/86822723', 'coefficient_abs': '2211840/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '29353417113600/7538185229134729', 'signed_layer': 'negative'} / {'conductor': 10, 'prime_count': 2, 'primitive_frequency_count': 4, 'coefficient': '3317760/86822723', 'coefficient_abs': '3317760/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '44030125670400/7538185229134729', 'signed_layer': 'positive'} / {'conductor': 11, 'prime_count': 1, 'primitive_frequency_count': 10, 'coefficient': '-1327104/86822723', 'coefficient_abs': '1327104/86822723', 'layer_l1': '13271040/86822723', 'layer_l2': '17612050268160/7538185229134729', 'signed_layer': 'negative'} |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RamanujanSpectrumExactConductorStratification | true | true | Every frequency has exact conductor q=W_P/gcd(a,W_P), with coefficient mu(q)phi(W_P)/(W_P phi(q)). | none |
| EqualL1MassPerConductorLayer | true | true | Each conductor layer q\|W_P has total L1 mass phi(W_P)/W_P. | none |
| LowConductorExactTruncationRejected | true | true | Keeping only low conductor layers changes the exact selector and is not a negligible exact tail. | none |
| UniformCancellationAcrossAllPrimorialConductorLayers | false | false | Prove cancellation across all conductor layers of the dynamic primorial spectrum. | new conductor-uniform cancellation theorem |
| ConductorStratifiedSpectrumToKloostermanOrTraceFamilyBridge | false | false | Package the conductor layers into a same-object Kloosterman/trace-function/Type-II family. | new bridge theorem |
| RoughBetaSiegelWalfiszUniformityOrReplacement | false | false | Supply the equidistribution/SW factor or an object-specific replacement for rough beta weights. | rough beta uniformity input |

## 4. 外部 theorem 影响

```text
Wright_2026_arXiv_2604_25177=useful only after conductor layers become a completed unbalanced-convolution coefficient family
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459=trace-function bilinear bounds require sheaf/trace packaging of the conductor layers
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-q Kloosterman estimates still need admissible bilinear coefficient ranges
Pascadi_2025_arXiv_2511_08445=non-abelian amplification may apply after Type-II organisation over composite conductor layers
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=squarefree/smooth Kloosterman parameter sums are adjacent to the conductor set but not this pointwise P,k selector
```

结论：全谱可按 exact conductor 压成 2^omega(W_P) 层，但每一层总 L1 质量相同。低 conductor 层不是主质量，丢弃高 conductor 层不是精确同对象截断。

## 5. 最新最窄口

```text
ConductorStratifiedSpectrumToKloostermanOrTraceFamilyBridge
AND UniformCancellationAcrossAllPrimorialConductorLayers
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
conductor_stratification_closed=true
equal_l1_mass_per_conductor_layer_proved=true
low_conductor_exact_truncation_rejected=true
uniform_conductor_layer_cancellation_closed=false
usable_kloosterman_or_trace_family_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
