# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary layer-cake rectangles 审计

**状态：** `boundary_monotone_strips_decomposed_into_layercake_product_rectangles_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=three monotone prime-interval boundary strips
layercake_decomposition=each strip is a disjoint union of strip-local q-prefix x prime m-shell rectangles
remaining=uniform phase saving or completed trace/Kloosterman estimates over the 6190 rectangle layers
```

## 2. layer-cake rectangle 有限审计

```text
max_prime=1009
active_P_count=155
boundary_edge_count_total=177515
previous_boundary_edge_count_total=177515
layercake_rectangle_count_total=6190
layercake_edge_count_total=177515
lower_wing_rectangle_count_total=1032
upper_wing_rectangle_count_total=1967
right_tail_rectangle_count_total=3191
lower_wing_edge_count_total=29144
upper_wing_edge_count_total=61620
right_tail_edge_count_total=86751
row_rectangle_count_min=1
row_rectangle_count_median=38.5
row_rectangle_count_max=81
row_rectangle_count_average=40.194805194805
max_rectangle_edge_count=261
nested_bad_steps_total=0
missing_count_total=0
extra_count_total=0
bad_layercake_row_count=0
total_bad_boundary_layercake_rectangle_count=0
boundary_layercake_rectangle_identity_verified=true
all_layers_are_complete_product_rectangles=true
layer_count_requires_uniform_summation_control=true
boundary_phase_saving_closed=false
```

代表行：

| P | boundary_edge_count | layercake_rectangle_count | layercake_edge_count | lower_wing_rectangle_count | upper_wing_rectangle_count | right_tail_rectangle_count | max_rectangle_edge_count | missing_count | extra_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 53 | 3 | 1 | 3 | 0 | 1 | 0 | 3 | 0 | 0 |
| 59 | 6 | 1 | 6 | 0 | 1 | 0 | 6 | 0 | 0 |
| 61 | 12 | 2 | 12 | 0 | 2 | 0 | 6 | 0 | 0 |
| 67 | 6 | 1 | 6 | 0 | 1 | 0 | 6 | 0 | 0 |
| 71 | 17 | 3 | 17 | 0 | 2 | 1 | 12 | 0 | 0 |
| 73 | 15 | 3 | 15 | 0 | 1 | 2 | 6 | 0 | 0 |
| 79 | 16 | 2 | 16 | 0 | 1 | 1 | 8 | 0 | 0 |
| 101 | 36 | 7 | 36 | 0 | 3 | 4 | 12 | 0 | 0 |
| 257 | 272 | 19 | 272 | 4 | 8 | 7 | 48 | 0 | 0 |
| 971 | 3146 | 78 | 3146 | 15 | 25 | 38 | 154 | 0 | 0 |
| 1009 | 3255 | 77 | 3255 | 20 | 22 | 35 | 162 | 0 | 0 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BoundaryLayerCakeRectangleIdentity | True | True | The three monotone strips decompose exactly into disjoint q-prefix by m-shell product rectangles. | none for the support identity |
| NoLayerOverlapOrLeak | True | True | Expanded layer rectangles match the boundary edge set with no missing and no extra edge. | none for the finite ledger |
| LayerCountAndLoadLedger | True | True | The boundary load is carried by 6190 rectangle layers, with row layer counts recorded. | uniform summation control over layers remains required |
| LayerUniformPhaseSaving | False | False | Apply trace/Kloosterman/Type-II estimates uniformly across all layer rectangles. | new analytic estimate and completed family still required |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | the boundary is now a finite family of product rectangles, but uniform trace-family hypotheses and summation over layers remain open |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | rectangle layers still require a completed Kloosterman variable for the moving q denominator |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | layer rectangles are Type-II shaped, but the number of layers and endpoint weights must be absorbed |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | right-tail layers are unbalanced candidates only after their congruence model is completed |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval theta=0.52 still does not close the half-scale layer endpoint problem |

```text
FKMS_trace_function_bilinear=layer rectangles fit the product-shape interface better, but a trace-family sheaf and uniform layer summation are not supplied
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=moving q denominators still need completed Kloosterman variables on every layer
Pascadi_composite_Type_II=Type-II shape is present layerwise, but endpoint weights and layer count remain rate-bearing
Wright_unbalanced_convolution=right-tail layers suggest an unbalanced route, still conditional on a congruence model
Li_short_interval_x_052=does not provide the missing half-scale layer endpoint estimate
```

结论：三条 monotone boundary strips 已精确分解成互不重叠的 q-prefix x m-shell product rectangles。
这进一步贴近 Type-II/trace 输入形状；但共有 `6190` 个层矩形，仍必须证明跨层统一相消或完成求和。

## 5. 最新最窄口

```text
UniformPhaseSavingAcrossBoundaryLayerCakeRectangles
AND CompletedTraceFamilyForPrimePrimeBulkRectangle
AND CompletedKloostermanVariableForMovingPrimeDenominatorOnLayers
AND StripEndpointSummationByPartsWithoutComparableLoss
AND DiagonalPGhostSubtractionDiscipline
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
boundary_layercake_rectangle_identity_verified=true
all_layers_are_complete_product_rectangles=true
boundary_phase_saving_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
