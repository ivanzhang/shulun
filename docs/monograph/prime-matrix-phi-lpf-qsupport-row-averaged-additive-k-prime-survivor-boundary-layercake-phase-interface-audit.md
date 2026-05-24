# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary layer-cake phase-interface 审计

**状态：** `boundary_layercake_rectangles_split_by_phase_interface_short_shell_completion_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=6190 boundary layer-cake product rectangles
phase_interface=split into point, q-prefix line, m-shell line, and genuine q-m product layers
remaining=short prime-m shell completion, moving q-denominator trace family, and uniform summation over layers
```

## 2. 相位接口有限审计

```text
max_prime=1009
layercake_rectangle_count_total=6190
previous_layercake_rectangle_count_total=6190
edge_count_total=177515
previous_layercake_edge_count_total=177515
q_prefix_count_min=1
q_prefix_count_median=11.0
q_prefix_count_max=37
q_prefix_count_average=12.566720516963
m_shell_prime_count_min=1
m_shell_prime_count_median=2.0
m_shell_prime_count_max=12
m_shell_prime_count_average=2.494184168013
rectangle_edge_count_min=1
rectangle_edge_count_median=21.0
rectangle_edge_count_max=261
rectangle_edge_count_average=28.677705977383
sum_sqrt_rectangle_edges=30147.122529825978
sqrt_total_edges=421.325290007614
naive_layer_sqrt_loss_factor=71.553080825699
all_m_shells_le_12=true
no_large_balanced_typeii_layer_ge_16=true
phase_interface_shape_verified=true
direct_long_typeii_layer_closure_available=false
uniform_short_shell_completion_required=true
boundary_phase_saving_closed=false
```

相位接口分类：

| bucket | rectangle_count | edge_count |
| --- | --- | --- |
| genuine_qm_product_layer | 3880 | 147181 |
| m_shell_line_layer | 296 | 1103 |
| point_layer | 59 | 59 |
| q_prefix_line_layer | 1955 | 29172 |

strip x class 分类：

| strip | phase_class | rectangle_count | edge_count |
| --- | --- | --- | --- |
| lower_wing | genuine_qm_product_layer | 670 | 24514 |
| lower_wing | m_shell_line_layer | 37 | 128 |
| lower_wing | point_layer | 12 | 12 |
| lower_wing | q_prefix_line_layer | 313 | 4490 |
| right_tail | genuine_qm_product_layer | 1815 | 67906 |
| right_tail | m_shell_line_layer | 151 | 519 |
| right_tail | point_layer | 29 | 29 |
| right_tail | q_prefix_line_layer | 1196 | 18297 |
| upper_wing | genuine_qm_product_layer | 1395 | 54761 |
| upper_wing | m_shell_line_layer | 108 | 456 |
| upper_wing | point_layer | 18 | 18 |
| upper_wing | q_prefix_line_layer | 446 | 6385 |

q-prefix 分桶：

| bucket | rectangle_count | edge_count |
| --- | --- | --- |
| 17<=q<=37 | 1872 | 93081 |
| 2<=q<=4 | 886 | 7452 |
| 5<=q<=8 | 1220 | 20877 |
| 9<=q<=16 | 1857 | 54943 |
| q=1 | 355 | 1162 |

m-shell 分桶：

| bucket | rectangle_count | edge_count |
| --- | --- | --- |
| 3<=m<=4 | 1925 | 77832 |
| 5<=m<=8 | 449 | 20347 |
| 9<=m<=12 | 69 | 6485 |
| m=1 | 2014 | 29231 |
| m=2 | 1733 | 43620 |

双侧阈值：

| threshold | rectangle_count | edge_count |
| --- | --- | --- |
| both>=2 | 3880 | 147181 |
| both>=3 | 2084 | 102347 |
| both>=4 | 1084 | 64616 |
| both>=5 | 319 | 24004 |
| both>=8 | 42 | 6118 |
| both>=10 | 3 | 499 |
| both>=16 | 0 | 0 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BoundaryLayerCakeShapeImported | True | True | The previous exact 6190-rectangle layer-cake support identity is preserved. | none for support shape |
| PhaseInterfaceClassLedger | True | True | Every layer is classified by its q-prefix and m-shell side lengths. | none for finite classification |
| ThinPrimeShellObstructionLocated | True | True | The audited m-shell side has median 2 and maximum 12, so long-m Type-II input is not directly available layerwise. | prove short-shell completion or aggregate layers before applying external estimates |
| UniformShortShellPhaseSaving | False | False | Prove cancellation for q-long but m-short prime shells with moving prime q denominator. | new analytic estimate or completed trace family required |
| NoLossLayerSummation | False | False | Sum the 6190 layer estimates without a comparable Cauchy/endpoint loss. | uniform layer aggregation remains required |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | long bilinear trace input would need a completed family and uniform aggregation; thin m-shell layers are not supplied as a direct theorem instance |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman input is relevant only after the moving prime q denominator is completed layerwise |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | Type-II shape is present for many edges, but the m side is short and endpoint layer summation remains rate-bearing |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced estimates are a plausible interface for right-tail and q-long layers, still requiring the exact congruence model |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval theta=0.52 does not close the half-scale or short-shell phase interface |

```text
FKMS_trace_bilinear=genuine product layers are present, but the short m side and cross-layer aggregation are not automatic theorem hypotheses
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=useful only after layerwise moving q denominators are completed as Kloosterman variables
Pascadi_composite_Type_II=does not by itself absorb q-prefix line layers or short m-shell endpoint layers
Wright_unbalanced_Kloosterman=most relevant to q-long/m-short layers, still requiring the exact reciprocal phase model
Li_short_interval_x_052=does not imply the needed half-scale or layer endpoint positivity
```

结论：边界层包已经是 product rectangles，但逐层相位接口不是长双变量 Type-II 的直接输入。
`genuine_qm_product_layer` 承载多数边数；然而 `m_shell_prime_count` 的中位数为 `2`，最大为 `12`。
因此最新缺口从“曲边支撑”推进到短 prime-shell completion、移动 q 分母 completed trace family、以及 6190 层的无损求和。

## 5. 最新最窄口

```text
UniformShortPrimeShellCompletionAcrossLayerCakeRectangles
AND MovingPrimeQDenominatorCompletedTraceFamily
AND NoLossLayerAggregationFor6190ShortShellPackets
AND EndpointSummationByPartsForQPrefixLineLayers
AND DiagonalPGhostSubtractionDiscipline
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
phase_interface_shape_verified=true
direct_long_typeii_layer_closure_available=false
boundary_phase_saving_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
