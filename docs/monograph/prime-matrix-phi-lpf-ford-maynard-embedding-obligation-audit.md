# Prime Matrix Phi-LPF Ford--Maynard embedding obligation 审计

**状态：** `hp_embedded_in_ford_maynard_typeii_framework_but_hypotheses_open`
**核验日期：** `2026-05-23`

## 1. 选择方向

本轮选择 `SameRowReciprocalWindowTypeIIDispersionForLPFTail` 作为三条非循环路线中最可操作的主线。

理由：

- directly attacks the LPF-tail parity obstruction rather than a renamed equivalent form
- matches the balanced q*m scale x^(1/2) in the strict top band x≈P^2
- Ford--Maynard supplies an explicit theorem-match checklist for Type I/II inputs

## 2. Ford--Maynard 精读摘要

论文：Kevin Ford and James Maynard, On the theory of prime-producing sieves，arXiv `2407.14368v1`。

核心框架不是直接给 H_P 的黑箱定理，而是：对任意非负序列 `a_n`，若
`w_n=a_n-b_n` 满足 Type I 与 Type II 估计，则可用常数
`C^-(gamma,theta,nu)` 给出 prime-producing lower bound。

精读项：

- Type I estimate (I) for w_n=a_n-b_n in divisor-sliced intervals
- Type II estimate (II) for arbitrary divisor-bounded bilinear coefficients
- constants C^-(gamma,theta,nu), C^+(gamma,theta,nu)
- Theorem 2.1: a positive amount of Type II information is necessary
- Theorem 2.2: asymptotic region characterized by A1/A2
- Theorem 2.4/2.5: the gamma=1/2 boundary is delicate and needs extra boundedness

## 3. H_P 嵌入

```text
x_scale=x≈P^2 in the top strict band k≈P
row_window=I_{P,k}=(kP,(k+1)P), length H=P=x^(1/2)
normalized_sequence_candidate=a_{P,k}(n)=(x/H) 1_{kP<n<(k+1)P} times optional wheel/unit filters
comparison_sequence_candidate=b_{P,k}(n)=smooth local-density model with same row mass and wheel density
prime_sum_target=sum_p a_{P,k}(p)>0 is equivalent, after normalization, to pi((k+1)P-1)-pi(kP)>0
lpf_tail_typeii_scale=q,m≈P≈x^(1/2), with q in (P/2,P) and m in I_q(P,k)
reciprocal_graph=I_q(P,k)=[max(q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]
```

## 4. 既有证书读数

LPF-tail Type-II：

```text
status=lpf_tail_reduced_to_same_row_reciprocal_graph_typeii_obligation
max_prime=1009
row_count=76789
active_residual_row_count=52697
total_R30=299977
total_direct_prime_count=4172483
total_prime_count_minus_R30=3872506
thin_q_fiber=true
thin_reverse_fiber=true
one_point_qr_fiber=true
sparsest_finite_graph={'P': 1009, 'W_int': 87, 'k': 965, 'm_span': 924, 'q_count': 72, 'rectangle_hull_area': 66528, 'support_density_den': 66528, 'support_density_float': 0.0013077200577200577, 'support_density_num': 87}
```

CRT signed projection gate：

```text
status=fixed_crt_unit_class_dominance_rejected_signed_character_dispersion_required
fixed_crt_classwise_dominance_proved=false
character_averaged_dispersion_required=true
negative_rows_by_layer={'210-wheel': {'modulus': 210, 'stable_rows_with_negative_unit_cell_surplus': 37115, 'stable_negative_unit_cell_count': 67547, 'fixed_crt_classwise_dominance_holds_on_stable_rows': False}, '2310-wheel': {'modulus': 2310, 'stable_rows_with_negative_unit_cell_surplus': 45472, 'stable_negative_unit_cell_count': 151197, 'fixed_crt_classwise_dominance_holds_on_stable_rows': False}, '30-wheel': {'modulus': 30, 'stable_rows_with_negative_unit_cell_surplus': 976, 'stable_negative_unit_cell_count': 998, 'fixed_crt_classwise_dominance_holds_on_stable_rows': False}, '30030-wheel': {'modulus': 30030, 'stable_rows_with_negative_unit_cell_surplus': 39964, 'stable_negative_unit_cell_count': 107093, 'fixed_crt_classwise_dominance_holds_on_stable_rows': False}}
```

## 5. Theorem-match 判定表

| field | closed | proved | hp_embedding_status | remaining |
| --- | --- | --- | --- | --- |
| Nonnegative target sequence | true | true | formal after row normalization by x/H≈P | normalization itself gives no prime lower bound |
| Prime sum target | true | true | sum_p a_{P,k}(p)>0 exactly matches one row of H_P | requires C^->0 and verified hypotheses for every row |
| Type-I short-row divisor estimate | false | false | not proved for the length sqrt(x) moving row sequence | FMTypeIShortRowDivisorSwitchEstimate |
| Type-II bilinear estimate | false | false | scale matches q,m≈x^(1/2), but support is a thin reciprocal graph, not a rectangular box | FMTypeIISameRowReciprocalGraphBilinearDispersion |
| Local density model | false | false | wheel/local density can be written formally, but row-specific comparison error is unproved | FMLocalDensityForWheelRowComparisonSequence |
| Pointwise all-row upgrade | false | false | H_P needs every prime P and every strict row k, not an averaged exceptional-set statement | FMPointwiseUniformAllRowsUpgrade |
| Fixed CRT unit-cell route | true | true | existing CRT audit rejects cellwise dominance; character-averaged dispersion remains possible | CharacterAveragedSameRowCRTDispersionForLPFTail |
| Unconditional H_P closure | false | false | not reached | row_column_unconditional_closed=false |

## 6. 条件外部引理版

```text
closed_as_schema=true
proved_unconditionally=false
statement=If for every sufficiently large prime P and every strict row k the normalized row sequence satisfies Ford--Maynard Type I, Type II, local-density, and positive-C^- hypotheses uniformly, then H_P follows for those rows.
```

未证明输入：

```text
FMTypeIShortRowDivisorSwitchEstimate
FMTypeIISameRowReciprocalGraphBilinearDispersion
FMLocalDensityForWheelRowComparisonSequence
FMPointwiseUniformAllRowsUpgrade
```

## 7. 新剩余基

```text
FMTypeIShortRowDivisorSwitchEstimate
FMTypeIISameRowReciprocalGraphBilinearDispersion
FMLocalDensityForWheelRowComparisonSequence
FMPointwiseUniformAllRowsUpgrade
CharacterAveragedSameRowCRTDispersionForLPFTail
SquarePhaseEndpointLowerBound
```

## 8. 边界声明

```text
ford_maynard_embedding_complete=true
ford_maynard_hypotheses_verified_for_hp=false
same_row_reciprocal_typeii_still_main_attack=true
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
