# Prime Matrix Phi-LPF q-support row-averaged mixed-modulus graph 审计

**状态：** `row_averaged_graph_normal_form_closed_mixed_modulus_trace_embedding_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
row_averaged_edge=q odd, m=r*beta residual, k=floor(q*m/P), 1<=k<P
displacement=D=q*m-k*P=q*m mod P, 1<=D<P
phase=e(h*k*P/q)=e(-h*D/q)
long_fiber_gain=after averaging over k, fixed q can have many m and many k
mixed_modulus_obstruction=D is a mod-P residue while the phase denominator is q
```

## 2. 跨 k 图审计

```text
max_prime=1009
P_value_count=165
total_row_averaged_residual_edges=951378
total_row_averaged_selected_edges=299977
previous_single_row_selected_edge_total=299977
row_averaged_selected_edges_match_previous_total=true
floor_cell_membership_mismatch_total=0
floor_cell_odd_candidate_mismatch_total=0
bad_floor_cell_odd_count_total=0
bad_zero_displacement_total=0
max_q_to_m_fiber=193
max_m_to_q_fiber=252
max_q_to_k_fiber=193
max_k_to_q_fiber=59
max_selected_q_to_m_fiber=192
max_selected_m_to_q_fiber=73
max_selected_q_to_k_fiber=192
max_selected_k_to_q_fiber=23
P_values_with_long_selected_q_fibers=155
row_averaging_creates_long_selected_q_fibers_for_some_P=true
trace_mod_q_conflict_residue_count_total=2811
trace_mod_q_conflict_q_count_total=767
P_values_with_trace_mod_q_conflict=129
first_trace_mod_q_conflict=P=83,q=47,m_mod_q=2,D_mod_q_values=[15, 34]
phase_normal_form=for each edge k=floor(q*m/P), D=q*m-k*P=q*m mod P, e(h*k*P/q)=e(-h*D/q)
same_modulus_trace_family_available_directly=false
kloosterman_inverse_variable_available_directly=false
```

代表 P：

| P | row_averaged_residual_edges | row_averaged_selected_edges | max_selected_q_to_m_fiber | max_selected_m_to_q_fiber | max_selected_q_to_k_fiber | max_selected_k_to_q_fiber | trace_mod_q_conflict_residue_count | first_trace_mod_q_conflict | sample_edges |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 108 | 48 | 9 | 9 | 9 | 3 | 0 | none | q=53,m=77,r=7,beta=11,k=40,D=41,phase=e(-h*41/53),qmodW=53; q=53,m=91,r=7,beta=13,k=47,D=76,phase=e(-h*76/53),qmodW=53; q=53,m=119,r=7,beta=17,k=62,D=45,phase=e(-h*45/53),qmodW=53; q=53,m=121,r=11,beta=11,k=63,D=50,phase=e(-h*50/53),qmodW=53; q=53,m=133,r=7,beta=19,k=69,D=80,phase=e(-h*80/53),qmodW=53; q=53,m=143,r=11,beta=13,k=75,D=4,phase=e(-h*4/53),qmodW=53; q=53,m=161,r=7,beta=23,k=84,D=49,phase=e(-h*49/53),qmodW=53; q=53,m=169,r=13,beta=13,k=88,D=69,phase=e(-h*69/53),qmodW=53 |
| 257 | 1013 | 377 | 36 | 23 | 36 | 7 | 0 | none | q=131,m=133,r=7,beta=19,k=67,D=204,phase=e(-h*204/131),qmodW=131; q=131,m=143,r=11,beta=13,k=72,D=229,phase=e(-h*229/131),qmodW=131; q=131,m=161,r=7,beta=23,k=82,D=17,phase=e(-h*17/131),qmodW=131; q=131,m=169,r=13,beta=13,k=86,D=37,phase=e(-h*37/131),qmodW=131; q=131,m=187,r=11,beta=17,k=95,D=82,phase=e(-h*82/131),qmodW=131; q=131,m=203,r=7,beta=29,k=103,D=122,phase=e(-h*122/131),qmodW=131; q=131,m=209,r=11,beta=19,k=106,D=137,phase=e(-h*137/131),qmodW=131; q=131,m=217,r=7,beta=31,k=110,D=157,phase=e(-h*157/131),qmodW=131 |
| 971 | 18708 | 5672 | 184 | 71 | 184 | 23 | 55 | q=487,m_mod_q=40,D_mod_q_values=[305, 308] | q=487,m=493,r=17,beta=29,k=247,D=254,phase=e(-h*254/487),qmodW=487; q=487,m=497,r=7,beta=71,k=249,D=260,phase=e(-h*260/487),qmodW=487; q=487,m=511,r=7,beta=73,k=256,D=281,phase=e(-h*281/487),qmodW=487; q=487,m=517,r=11,beta=47,k=259,D=290,phase=e(-h*290/487),qmodW=487; q=487,m=527,r=17,beta=31,k=264,D=305,phase=e(-h*305/487),qmodW=487; q=487,m=529,r=23,beta=23,k=265,D=308,phase=e(-h*308/487),qmodW=487; q=487,m=533,r=13,beta=41,k=267,D=314,phase=e(-h*314/487),qmodW=487; q=487,m=539,r=7,beta=77,k=270,D=323,phase=e(-h*323/487),qmodW=487 |
| 1009 | 20401 | 5901 | 192 | 72 | 192 | 21 | 48 | q=509,m_mod_q=2,D_mod_q_values=[277, 322] | q=509,m=511,r=7,beta=73,k=257,D=786,phase=e(-h*786/509),qmodW=509; q=509,m=517,r=11,beta=47,k=260,D=813,phase=e(-h*813/509),qmodW=509; q=509,m=527,r=17,beta=31,k=265,D=858,phase=e(-h*858/509),qmodW=509; q=509,m=529,r=23,beta=23,k=266,D=867,phase=e(-h*867/509),qmodW=509; q=509,m=533,r=13,beta=41,k=268,D=885,phase=e(-h*885/509),qmodW=509; q=509,m=539,r=7,beta=77,k=271,D=912,phase=e(-h*912/509),qmodW=509; q=509,m=551,r=19,beta=29,k=277,D=966,phase=e(-h*966/509),qmodW=509; q=509,m=553,r=7,beta=79,k=278,D=975,phase=e(-h*975/509),qmodW=509 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RowAveragedQSupportGraphNormalForm | true | true | Averaging over k identifies each edge by k=floor(qm/P) and D=qm mod P. | none |
| RowAveragingLongFiberGainLedger | true | true | Unlike one row, the all-k graph has long q-to-m and q-to-k fibers. | none |
| MixedModulusPhaseLedger | true | true | The row-averaged phase is e(-h(qm mod P)/q), coupling mod-P residue with denominator q. | none |
| DirectSameModulusTraceEmbeddingFromRowAverage | false | false | Identify the mixed-modulus graph phase as a same-modulus trace/Kloosterman family without changing the object. | new mixed-modulus embedding theorem |
| UniformCancellationAcrossRowAveragedMixedModulusRadialGraph | false | false | Prove phase saving over the row-averaged mixed-modulus graph and radial kernels. | new phase-saving theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459=row averaging supplies long fibers, but still lacks a same-modulus ell-adic trace-function family
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-q Kloosterman bilinear estimates still require Kloosterman variables modulo q, not a mod-P numerator divided by q
Pascadi_2025_arXiv_2511_08445=composite-modulus Type-II amplification is relevant only after the mixed-modulus graph is embedded into a genuine Kloosterman family
Wright_2026_arXiv_2604_25177=unbalanced convolution estimates require congruence/convolution structure; the present graph has k=floor(qm/P) and D=qm mod P
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree parameters remain adjacent to W_P but do not by themselves remove the mixed-modulus obstruction
```

结论：跨 k 平均确实恢复长纤维，但相位是 mixed-modulus graph phase。下一步不是再证明有长纤维，而是把 `D=qm mod P` 与分母 `q` 的混合模数结构嵌入同模 trace/Kloosterman/dispersion 对象。

## 5. 最新最窄口

```text
MixedModulusRowAveragedGraphToTraceOrKloostermanEmbedding
AND UniformCancellationAcrossRowAveragedMixedModulusRadialGraph
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
row_averaged_qsupport_graph_normal_form_closed=true
row_averaging_long_fiber_gain_ledger_closed=true
mixed_modulus_phase_ledger_closed=true
direct_same_modulus_trace_embedding_from_row_average_closed=false
uniform_cancellation_across_row_averaged_mixed_modulus_radial_graph_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
