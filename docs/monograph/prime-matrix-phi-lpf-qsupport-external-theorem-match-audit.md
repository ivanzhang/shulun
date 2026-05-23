# Prime Matrix Phi-LPF q-support external theorem match 审计

**状态：** `external_theorem_match_completed_direct_closure_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQSupportSetReciprocalPhaseSavingBeyondParity / AND CompletionToExternalKloostermanOrVaughanTypeII | QSupportExternalTheoremMatchAndBridgeObligation | true | after leaf phase collapse, the only realistic non-cyclic advance is to theorem-match the q-support phase against current Kloosterman/Type-II inputs |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | no faster external theorem-match than the current q-support phase interface |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | not a Kloosterman/Type-II q-support interface |

本轮继续选择行/列 Phi-LPF。叶子相位塌缩后，继续分解 LPF 已无相位收益；最快非循环推进是把当前 q-support phase 与最新外部 Kloosterman/Type-II 定理逐项 theorem-match。

## 2. 当前对象

```text
phase_sum=sum_{q in S(P,k)} e(h*kP/q)
denominator=prime q in (P/2,P)
support=S(P,k) is the actual Phi-LPF residual q-support after complete leaf phase collapse
not_a_completed_external_form=No current ledger gives mn≡a mod q bilinear/trilinear convolution with a Siegel-Walfisz factor.
```

## 3. 有限接口审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_qsupport_row_count=52697
total_prime_q_instances=3874554
total_qsupport_instances=299977
max_prime_q_count=73
max_support_q_count=23
support_is_prime_denominator_dyadic_family=true
completed_mn_congruence_representation_available=false
siegel_walfisz_factor_certificate_available=false
type_ii_dyadic_ranges_certificate_available=false
missing_completed_mn_congruence_rows=76954
missing_siegel_walfisz_factor_rows=76954
missing_type_ii_dyadic_range_rows=76954
```

代表行：

| P | k | prime_q_count | support_q_count | support_q_min | support_q_max | phase_denominator_family | hk_mod_samples |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 10 | 1 | 71 | 71 | prime q in (P/2,P) | q=71,kPmodq=18,phase=e(h*kP/q) |
| 257 | 256 | 23 | 3 | 137 | 193 | prime q in (P/2,P) | q=137,kPmodq=32,phase=e(h*kP/q); q=151,kPmodq=107,phase=e(h*kP/q); q=193,kPmodq=172,phase=e(h*kP/q) |
| 971 | 936 | 71 | 23 | 491 | 929 | prime q in (P/2,P) | q=491,kPmodq=15,phase=e(h*kP/q); q=503,kPmodq=438,phase=e(h*kP/q); q=523,kPmodq=405,phase=e(h*kP/q); q=541,kPmodq=517,phase=e(h*kP/q); q=557,kPmodq=389,phase=e(h*kP/q); q=601,kPmodq=144,phase=e(h*kP/q) |
| 1009 | 1008 | 72 | 9 | 563 | 991 | prime q in (P/2,P) | q=563,kPmodq=294,phase=e(h*kP/q); q=577,kPmodq=398,phase=e(h*kP/q); q=617,kPmodq=256,phase=e(h*kP/q); q=647,kPmodq=635,phase=e(h*kP/q); q=743,kPmodq=648,phase=e(h*kP/q); q=761,kPmodq=376,phase=e(h*kP/q) |

## 4. 外部 theorem-match 表

| source | source_url | input_shape | requires | current_object | directly_closes | missing_bridge |
| --- | --- | --- | --- | --- | --- | --- |
| Wright 2026 arXiv:2604.25177 | https://arxiv.org/abs/2604.25177 | trilinear Kloosterman fractions / unbalanced convolution, including partially fixed moduli | completed mn≡a mod q convolution, dyadic M,N,Q ranges, and an equidistributed/Siegel-Walfisz factor | prime-q support reciprocal phase sum_{q in S(P,k)} e(h*kP/q) | false | QSupportToCompletedTrilinearKloostermanFractionWithSWFactor |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | https://arxiv.org/abs/2511.07550 | general bilinear forms with Kloosterman sums modulo arbitrary q | bilinear Kloosterman form with admissible coefficient norms | 0/1 q-support predicate times e(h*kP/q) | false | QSupportToBilinearKloostermanFormWithAdmissibleCoefficients |
| Pascadi 2025 arXiv:2511.08445 | https://arxiv.org/abs/2511.08445 | Type-II Kloosterman sums with composite moduli | Type-II organisation over composite moduli and non-abelian amplification input | prime denominator q with object-specific support predicate | false | PrimeQSupportToCompositeModulusTypeIIOrganisation |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | https://arxiv.org/abs/2411.12113 | Kloosterman sums parametrised by square-free and smooth integers | completed square-free/smooth parameter family | floor-defined LPF q-support, not a completed smooth/square-free parameter sum | false | QSupportLPFPredicateToCompletedSmoothSquarefreeParameterFamily |
| Ford--Maynard 2024 arXiv:2407.14368 | https://arxiv.org/abs/2407.14368 | prime-producing sieve framework with Type-I/II hypotheses | object-specific Type-I and Type-II information before the sieve conclusion | q-support phase after parity-class linear sieve reductions | false | ObjectSpecificQSupportTypeITypeIIInputLedger |

结论：这些定理都是有用候选，但没有一个可以按名称直接闭合当前 q-support phase。必须先提交同对象 completion bridge。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| QSupportExternalFrontierInventoryUpdatedThroughWright2026 | true | true | The current external candidates now include Wright 2026 partially fixed-modulus trilinear Kloosterman fractions. | none |
| DirectNameCitationToKloostermanTypeIIRejected | true | true | None of the external names directly estimates the present q-support reciprocal phase. | none |
| CompletionObligationSharpenedToConvolutionBridge | true | true | The vague completion gate is refined to a bilinear/trilinear convolution bridge with external hypotheses. | none |
| QSupportToCompletedBilinearOrTrilinearKloostermanConvolutionWithSWFactor | false | false | Construct the same-object convolution representation and verify the equidistribution/Siegel-Walfisz factor. | new bridge theorem |
| PointwisePKUniformTransferFromExternalAverageEstimate | false | false | Transfer an external averaged Kloosterman/Type-II theorem to every fixed P,k row without zero-exception leakage. | uniform transfer ledger |

## 6. 最新最窄口

```text
QSupportToCompletedBilinearOrTrilinearKloostermanConvolutionWithSWFactor
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
external_theorem_match_completed=true
direct_external_closure_available=false
q_support_convolution_bridge_closed=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
