# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor bulk-rectangle Type-II 审计

**状态：** `bulk_product_rectangle_extracted_boundary_typeii_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
edge_graph=prime-survivor edges (P,q,m) after rough-envelope cap
bulk_rectangle=maximal complete prime q x prime m rectangle inside each fixed-P support row
boundary=actual support minus the extracted complete bulk rectangle
remaining=prove phase saving for the comparable boundary, or complete the staircase into trace/Type-II packets without losing the main term
```

## 2. bulk rectangle 有限审计

```text
max_prime=1009
active_P_count=155
actual_prime_edge_count_total=355919
previous_actual_prime_edge_count_total=355919
bulk_rectangle_edge_count_total=178404
boundary_edge_count_total=177515
bulk_fraction_total=0.501248879661
boundary_fraction_total=0.498751120339
row_full_rectangle_count_total=795159
row_completion_extra_count_total=439240
row_completion_ratio_total=2.234101017366
row_completion_extra_to_actual_ratio_total=1.234101017366
bulk_fraction_min=0.485227517792
bulk_fraction_median=0.511806375443
bulk_fraction_max=1.000000000000
bulk_fraction_ge_half_rows=99
bulk_fraction_ge_45pct_rows=155
bulk_missing_count_total=0
bulk_rectangle_bad_row_count=0
total_bad_bulk_rectangle_typeii_count=0
bulk_product_rectangle_verified=true
bulk_is_large_but_not_dominating_boundary=true
direct_bulk_only_typeii_closure_available=false
boundary_phase_saving_or_staircase_completion_required=true
```

代表 bulk rectangle：

| P | q_start | q_end | m_start | m_end | q_count | m_count | bulk_edge_count | actual_edge_count | boundary_edge_count | bulk_fraction | bulk_missing_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 23 | 23 | 53 | 73 | 1 | 6 | 6 | 6 | 0 | 1.0 | 0 |
| 53 | 29 | 31 | 59 | 73 | 2 | 5 | 10 | 13 | 3 | 0.7692307692307693 | 0 |
| 59 | 31 | 43 | 53 | 73 | 4 | 5 | 20 | 26 | 6 | 0.7692307692307693 | 0 |
| 61 | 31 | 47 | 53 | 73 | 5 | 5 | 25 | 37 | 12 | 0.6756756756756757 | 0 |
| 67 | 37 | 47 | 53 | 89 | 4 | 8 | 32 | 38 | 6 | 0.8421052631578947 | 0 |
| 71 | 37 | 47 | 53 | 89 | 4 | 8 | 32 | 49 | 17 | 0.6530612244897959 | 0 |
| 73 | 37 | 43 | 53 | 113 | 3 | 14 | 42 | 57 | 15 | 0.7368421052631579 | 0 |
| 79 | 41 | 47 | 53 | 113 | 3 | 14 | 42 | 58 | 16 | 0.7241379310344828 | 0 |
| 101 | 53 | 71 | 79 | 139 | 5 | 12 | 60 | 96 | 36 | 0.625 | 0 |
| 257 | 131 | 181 | 191 | 359 | 11 | 29 | 319 | 591 | 272 | 0.5397631133671743 | 0 |
| 971 | 487 | 701 | 709 | 1327 | 34 | 90 | 3060 | 6206 | 3146 | 0.49307122139864645 | 0 |
| 1009 | 509 | 761 | 769 | 1327 | 39 | 81 | 3159 | 6414 | 3255 | 0.49251637043966323 | 0 |

粗 dyadic 密度：

| q_bin | m_bin | actual | full | density |
| --- | --- | --- | --- | --- |
| [0.5, 0.625)P | [0.5, 0.75)P | 27651 | 36795 | 0.7514879739094986 |
| [0.5, 0.625)P | [0.75, 1.0)P | 37575 | 37578 | 0.9999201660546064 |
| [0.5, 0.625)P | [1.0, 1.25)P | 36521 | 36521 | 1.0 |
| [0.5, 0.625)P | [1.25, 1.5)P | 36107 | 36112 | 0.9998615418697386 |
| [0.5, 0.625)P | [1.5, 1.75)P | 30106 | 35661 | 0.8442275875606404 |
| [0.5, 0.625)P | [1.75, 2.01)P | 8799 | 29988 | 0.2934173669467787 |
| [0.625, 0.75)P | [0.5, 0.75)P | 7962 | 36712 | 0.21687731531924168 |
| [0.625, 0.75)P | [0.75, 1.0)P | 36958 | 37170 | 0.9942964756524079 |
| [0.625, 0.75)P | [1.0, 1.25)P | 36418 | 36429 | 0.9996980427681244 |
| [0.625, 0.75)P | [1.25, 1.5)P | 26397 | 35655 | 0.7403449726546066 |
| [0.625, 0.75)P | [1.5, 1.75)P | 1829 | 35617 | 0.051351882528006286 |
| [0.625, 0.75)P | [1.75, 2.01)P | 0 | 29786 | 0.0 |
| [0.75, 0.875)P | [0.5, 0.75)P | 0 | 34953 | 0.0 |
| [0.75, 0.875)P | [0.75, 1.0)P | 24361 | 35745 | 0.6815218911735907 |
| [0.75, 0.875)P | [1.0, 1.25)P | 29219 | 34777 | 0.8401817293038503 |
| [0.75, 0.875)P | [1.25, 1.5)P | 1802 | 34286 | 0.052557895350872075 |
| [0.75, 0.875)P | [1.5, 1.75)P | 0 | 33874 | 0.0 |
| [0.75, 0.875)P | [1.75, 2.01)P | 0 | 28448 | 0.0 |
| [0.875, 1.000001)P | [0.5, 0.75)P | 0 | 29444 | 0.0 |
| [0.875, 1.000001)P | [0.75, 1.0)P | 6476 | 29763 | 0.2175855928501831 |
| [0.875, 1.000001)P | [1.0, 1.25)P | 7738 | 28995 | 0.2668735988963614 |
| [0.875, 1.000001)P | [1.25, 1.5)P | 0 | 28511 | 0.0 |
| [0.875, 1.000001)P | [1.5, 1.75)P | 0 | 28403 | 0.0 |
| [0.875, 1.000001)P | [1.75, 2.01)P | 0 | 23936 | 0.0 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LargestPrimePrimeBulkRectangleExtraction | True | True | Each active P row contains a verified complete prime q x prime m bulk rectangle inside the survivor graph. | none for the finite structural extraction |
| NaiveRowRectangleCompletionCostQuantified | True | True | Completing the row support to the full q x m row rectangle costs more than the actual support. | none for the cost ledger |
| BulkBoundaryComparableObstruction | True | True | The extracted bulk is large, but the remaining boundary is comparable and cannot be discarded. | boundary phase saving or staircase completion remains required |
| DirectBulkOnlyTypeIIClosure | False | False | Apply external Type-II/trace estimates only to the extracted bulk and close the full survivor layer. | does not handle the comparable boundary |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | the extracted bulk is closer to a trace bilinear input, but the comparable boundary remains outside the theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | bulk rectangles still need a completed Kloosterman variable; boundary is not absorbed |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | bulk rectangles are Type-II shaped, but boundary cancellation or completion is still missing |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | the split suggests an unbalanced convolution route only after boundary tails are completed |
| Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | additional smooth/squarefree matching remains absent for the prime-prime rectangle and boundary |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval theta=0.52 is not a replacement for boundary phase saving at the half-scale |

```text
FKMS_trace_function_bilinear=the bulk rectangle is a closer local shape, but the comparable boundary and completed trace family are not supplied
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=no completed Kloosterman variable has been constructed for bulk plus boundary
Pascadi_composite_Type_II=bulk rectangles are Type-II shaped, yet the boundary remains rate-bearing
Wright_unbalanced_convolution=a future unbalanced decomposition must include the staircase boundary
Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman=prime-prime and boundary weights still do not match the theorem hypotheses directly
Li_short_interval_x_052=does not replace the missing half-scale pointwise boundary estimate
```

结论：nested rough-envelope support 中确实存在可供 Type-II/trace 进一步研究的完整 bulk rectangle，
但最大 bulk 总量为 `178404` 条边，剩余 boundary 为 `177515` 条边，二者同阶。
因此不能只把 bulk 交给外部 Type-II 定理后丢弃边界；下一步必须证明 staircase boundary 的相消或无可比损失完成。

## 5. 最新最窄口

```text
BoundaryPhaseSavingForNestedRoughEnvelopeStaircase
AND CompletedTraceFamilyForPrimePrimeBulkRectangle
AND StaircaseBoundaryCompletionWithoutComparableLoss
AND DiagonalPGhostSubtractionDiscipline
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
bulk_product_rectangle_verified=true
bulk_boundary_comparable_obstruction_closed=true
direct_bulk_only_typeii_closure_available=false
boundary_phase_saving_or_staircase_completion_required=true
prefix_cap_trace_or_typeii_embedding_closed=false
completed_trace_or_kloosterman_variable_closed=false
prime_floor_span_trace_or_typeii_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
