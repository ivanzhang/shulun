# Prime Matrix Phi-LPF reciprocal graph Kloosterman gateway 审计

**状态：** `reciprocal_graph_kloosterman_gateway_identified_not_closed`
**核验日期：** `2026-05-23`

## 1. 目标

本层继续下钻 `FMTypeIISameRowReciprocalGraphBilinearDispersion`，目标是判断 DFI、Bettin--Chandee、Wright 等外部 Kloosterman 定理是否能直接接入 Phi-LPF same-row reciprocal graph。

## 2. 上游读数

```text
ford_maynard_status=hp_embedded_in_ford_maynard_typeii_framework_but_hypotheses_open
selected_non_circular_direction=SameRowReciprocalWindowTypeIIDispersionForLPFTail
ford_maynard_hypotheses_verified_for_hp=false
lpf_tail_status=lpf_tail_reduced_to_same_row_reciprocal_graph_typeii_obligation
max_prime=1009
row_count=76789
active_residual_row_count=52697
total_R30=299977
thin_q_fiber=true
thin_reverse_fiber=true
one_point_qr_fiber=true
fixed_crt_classwise_dominance_proved=false
```

## 3. 同一行对象

```text
residual=R_30(P,k)=# {(q,r,a): P/2<q<P, q prime, m=r*a in I_q(P,k), r=LPF(m)>=7, a r-rough}
graph=I_q(P,k)=[max(q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]
#I_q(P,k)<=2
#{q:m in I_q(P,k)}<=2
#{a:kP<q*r*a<(k+1)P}<=1
```

## 4. 频率分解入口

| route | closed | proved | formal_phase | defect | remaining |
| --- | --- | --- | --- | --- | --- |
| floor_sawtooth_endpoint_route | true | true | psi(kP/u), psi(((k+1)P-1)/u) -> finite sums of e(h*kP/u) | produces reciprocal phases e(A/u), not modular-inverse Kloosterman fractions e(A*bar m/n) | ReciprocalSawtoothTailLogSavingForLPFShellWeights |
| product_window_fourier_route | true | true | smooth 1_{kP<uv<(k+1)P} -> additive bilinear phases e(t*u*v/Y) | not yet transformed into a DI/DFI/BC inverse-fraction phase without Cauchy/Poisson loss | ProductWindowToInverseKloostermanCompletionIdentity |
| crt_character_average_route | true | true | sum_a mu_S(a) chi(a) across unit classes | fixed cellwise dominance is false; character averaging still needs same-row dispersion | CharacterAveragedSameRowCRTDispersionForLPFTail |

## 5. 外部定理 theorem-match

| source | theorem_type | matched_to_current_object | reason_not_direct | remaining | accepted_as_external_input |
| --- | --- | --- | --- | --- | --- |
| Duke-Friedlander-Iwaniec 1997 | bilinear forms with Kloosterman fractions e(a*bar m/n) | false | current graph emits floor/reciprocal or product-window phases before any inverse-modulus completion | ProductWindowToInverseKloostermanCompletionIdentity | false |
| Bettin-Chandee 2015/2018 | trilinear Kloosterman fractions e(theta*a*bar m/n) | false | LPF tail has q prime and one-point m/a fibres, not an existing averaged numerator denominator package | LPFShellWeightsToBCKloostermanVariablesWithoutProjectionLoss | false |
| Wright 2026 arXiv:2604.25177 | partially fixed moduli and unbalanced convolution AP discrepancy | false | estimates average AP convolution over q~Q with Siegel-Walfisz beta; H_P is a pointwise product-window row | SameRowProductWindowToAPConvolutionAverageTransfer | false |
| Dong-Robles-Zeindler 2026 arXiv:2601.00292 | claimed improved bilinear Kloosterman fractions | false | paper is withdrawn and cannot be used as an accepted theorem | not_an_accepted_source | false |

## 6. 新原子门

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ReciprocalGraphToKloostermanCompletionIdentity | false | false | derive, without losing the pointwise row and LPF-shell weights, a DI/DFI/BC-compatible inverse-fraction bilinear or trilinear form | first missing gate before external Kloosterman theorems can be applied |
| CompletedKloostermanMeanForPrimeQAndLPFShellWeights | false | false | after completion, prove or cite a mean theorem with q prime, r=LPF(m), a r-rough and one-point fibres | object-sensitive spectral/dispersion theorem |
| SawtoothTailLogSavingForThinReciprocalFibres | false | false | control the Fourier truncation/tail from the floor endpoint representation with arbitrary log saving | thin reciprocal graph Fourier tail bound |
| ExternalKloostermanTheoremsApplyDirectly | false | false | DFI/BC/Wright do not directly match the present fixed-row reciprocal graph | must first close the completion identity |

## 7. 最新最窄口

```text
ReciprocalGraphToKloostermanCompletionIdentity
AND CompletedKloostermanMeanForPrimeQAndLPFShellWeights
AND SawtoothTailLogSavingForThinReciprocalFibres
```

## 8. 边界声明

```text
direct_external_closure_reached=false
same_row_reciprocal_typeii_still_main_attack=true
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
