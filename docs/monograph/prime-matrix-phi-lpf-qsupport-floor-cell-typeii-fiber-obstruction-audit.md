# Prime Matrix Phi-LPF q-support floor-cell Type-II fiber obstruction 审计

**状态：** `direct_floor_cell_typeii_completion_rejected_same_object_trace_embedding_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
floor_cell=I_{P,k}(q)=[max(P/2+1,q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]
factor_split=m=r*beta with r>=7 prime and beta r-rough
same_object_fibers_checked=q->m, m->q, q->(r,beta), (q,r)->beta, (q,beta)->r, (r,beta)->q
phase=e(h*k*P/q), equivalently e(-h*(qm-kP)/q) on the graph
obstruction=all same-object fibers are singleton, so floor cells do not directly form a long Type-II/Kloosterman family
```

## 2. Fiber 审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_floor_cell_residual_atoms=951378
total_floor_cell_selected_terms=299977
q_floor_cells_checked_total=12532624
bad_product_cell_window_size_total=0
bad_product_cell_odd_count_total=0
max_product_cell_window_size=2
max_product_cell_odd_count=1
max_q_to_m_fiber=1
max_m_to_q_fiber=1
max_q_to_factor_pair_fiber=1
max_qr_to_beta_fiber=1
max_qbeta_to_r_fiber=1
max_rbeta_to_q_fiber=1
max_selected_q_to_m_fiber=1
max_selected_qr_to_beta_fiber=1
rows_with_long_same_object_fiber=0
same_object_long_fiber_available_for_any_row=false
direct_typeii_bilinear_fiber_available=false
direct_kloosterman_variable_available=false
phase_is_denominator_graph_phase_not_inverse_variable=true
```

代表 P：

| P | k | floor_cell_residual_atoms | floor_cell_selected_terms | max_q_to_m_fiber | max_m_to_q_fiber | max_qr_to_beta_fiber | max_qbeta_to_r_fiber | max_rbeta_to_q_fiber | same_object_long_fiber_available | sample_floor_cells |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | false | q=71,m=143,r=11,beta=13,I_q=[143,143],phase=e(h*100*101/71) |
| 257 | 256 | 8 | 3 | 1 | 1 | 1 | 1 | 1 | false | q=137,m=481,r=13,beta=37,I_q=[481,482],phase=e(h*256*257/137); q=151,m=437,r=19,beta=23,I_q=[436,437],phase=e(h*256*257/151); q=193,m=341,r=11,beta=31,I_q=[341,342],phase=e(h*256*257/193) |
| 971 | 936 | 49 | 23 | 1 | 1 | 1 | 1 | 1 | false | q=491,m=1853,r=17,beta=109,I_q=[1852,1853],phase=e(h*936*971/491); q=503,m=1807,r=13,beta=139,I_q=[1807,1808],phase=e(h*936*971/503); q=523,m=1739,r=37,beta=47,I_q=[1738,1739],phase=e(h*936*971/523); q=541,m=1681,r=41,beta=41,I_q=[1680,1681],phase=e(h*936*971/541); q=557,m=1633,r=23,beta=71,I_q=[1632,1633],phase=e(h*936*971/557); q=601,m=1513,r=17,beta=89,I_q=[1513,1513],phase=e(h*936*971/601); q=619,m=1469,r=13,beta=113,I_q=[1469,1469],phase=e(h*936*971/619); q=631,m=1441,r=11,beta=131,I_q=[1441,1441],phase=e(h*936*971/631) |
| 1009 | 1008 | 51 | 9 | 1 | 1 | 1 | 1 | 1 | false | q=563,m=1807,r=13,beta=139,I_q=[1807,1808],phase=e(h*1008*1009/563); q=577,m=1763,r=41,beta=43,I_q=[1763,1764],phase=e(h*1008*1009/577); q=617,m=1649,r=17,beta=97,I_q=[1649,1650],phase=e(h*1008*1009/617); q=647,m=1573,r=11,beta=143,I_q=[1572,1573],phase=e(h*1008*1009/647); q=743,m=1369,r=37,beta=37,I_q=[1369,1370],phase=e(h*1008*1009/743); q=761,m=1337,r=7,beta=191,I_q=[1337,1337],phase=e(h*1008*1009/761); q=887,m=1147,r=31,beta=37,I_q=[1147,1147],phase=e(h*1008*1009/887); q=941,m=1081,r=23,beta=47,I_q=[1081,1081],phase=e(h*1008*1009/941) |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FloorCellSameObjectFiberSingletonLedger | true | true | The q-cell support and all immediate factor fibers are singleton fibers in the same object. | none |
| DirectFloorCellTypeIICompletionRejected | true | true | The exact floor-cell graph does not itself supply the long bilinear/trilinear variables required by Type-II Kloosterman inputs. | none |
| DirectKloostermanVariableFromFloorCellRejected | true | true | The phase remains a denominator graph phase e(hkP/q), not a completed inverse-variable Kloosterman sum. | none |
| SameObjectAveragedGraphDispersionOrTraceEmbedding | false | false | Build a new embedding that averages the sparse denominator graph into a legitimate trace/Kloosterman or dispersion family without changing the object. | new same-object completion theorem |
| UniformCancellationAcrossGraphSupportedRadialKernels | false | false | Prove cancellation after such an embedding, uniformly across the radial pair kernels and q-support graph. | new phase-saving theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459=requires a genuine trace-function family and bilinear variables; singleton floor-cell fibers do not provide it directly
Milicevic_Qin_Wu_2025_arXiv_2511_07550=power-saving bilinear Kloosterman sums need actual Kloosterman variables modulo q; the present phase is still a q-graph denominator phase
Pascadi_2025_arXiv_2511_08445=composite-modulus Type-II amplification remains relevant only after a nontrivial same-object embedding creates long variables
Wright_2026_arXiv_2604_25177=unbalanced convolution hypotheses require a congruence/convolution family with a nontrivial inner variable; direct floor-cell fibers are singleton
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree parameter inputs remain adjacent to W_P but do not overcome the missing trace embedding
```

结论：floor-cell 支撑虽然已精确闭合，但直接 Type-II/Kloosterman 完成出口被排除。下一步必须构造新的 same-object averaged graph dispersion 或 trace embedding，而不能把单点纤维误认为长双线性变量。

## 5. 最新最窄口

```text
SameObjectAveragedGraphDispersionOrTraceEmbedding
AND UniformCancellationAcrossGraphSupportedRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
floor_cell_same_object_fiber_singleton_ledger_closed=true
direct_floor_cell_typeii_completion_rejected=true
direct_kloosterman_variable_from_floor_cell_rejected=true
same_object_averaged_graph_dispersion_or_trace_embedding_closed=false
uniform_cancellation_across_graph_supported_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
