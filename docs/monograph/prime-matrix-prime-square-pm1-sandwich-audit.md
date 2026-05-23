# Prime Square P^2±1 Sandwich Audit

**状态**：`pm1_sandwich_does_not_localize_theta052_to_halfscale`
**核验日期**：`2026-05-23`

## 1. 直接回答

`P^2-1` 与 `P^2+1` 的两侧夹击不能把 `0.52` 自动降到 `1/2`。
原因是短区间定理给出的仍是厚度 `P^1.04` 的容器；目标只允许厚度 `P`。
夹击若要成功，必须额外证明保证素数不落在外尾段，或证明容器内素数数目压过外尾段容量。

## 2. ±1 平移尺度

```text
formula=(P^2±1)^theta = P^(2theta) * (1 + O(P^-2))
theta=0.52
after_specialization=P^1.04 * (1 + O(P^-2))
target_halfscale=P
pm1_shift_absolute_change=O(P^(2theta-2)) = O(P^-0.96)
pm1_shift_changes_exponent=false
```

| P | (P^2+1)^0.52/P | (P^2-1)^0.52/P | right_outer_tail_estimate | left_outer_tail_estimate |
| --- | --- | --- | --- | --- |
| 101 | 1.202804 | 1.202682 | 20 | 20 |
| 1009 | 1.31873 | 1.318729 | 322 | 322 |
| 100003 | 1.584895 | 1.584895 | 58491 | 58491 |
| 1000003 | 1.737801 | 1.737801 | 737803 | 737803 |

## 3. 夹击窗口审计

| model | guaranteed_container | target_inner_window | open_outer_tail | localizes_to_inner_window |
| --- | --- | --- | --- | --- |
| right endpoint from P^2+1 | (P^2+1, P^2+1+(P^2+1)^0.52] | (P^2, P^2+P) | [P^2+P, P^2+P^1.04+O(1)] | false |
| left endpoint from P^2-1 | [P^2-1-(P^2-1)^0.52, P^2-1) | (P^2-P, P^2) | [P^2-P^1.04+O(1), P^2-P] | false |
| forward theorem at P^2-1 | (P^2-1, P^2-1+(P^2-1)^0.52] | (P^2, P^2+P) | [P^2+P, P^2+P^1.04+O(1)] | false |
| backward theorem at P^2+1 | [P^2+1-(P^2+1)^0.52, P^2+1) | (P^2-P, P^2) | [P^2-P^1.04+O(1), P^2-P] | false |

## 4. 计数障碍

```text
large_container_lower_bound_from_short_interval=at_least_one_prime
outer_tail_length=P^1.04-P
brun_titchmarsh_tail_capacity_order=P^1.04/log P
needed_count_dominance=container prime lower bound > outer-tail prime upper bound
available_now=false
```

one guaranteed prime in the thick container can all lie in the outer tail; available upper bounds do not make the outer tail empty

## 5. 因子结构诊断

| structure | effect | closes_halfscale |
| --- | --- | --- |
| P^2-1=(P-1)(P+1) | endpoint factorization does not constrain where the next or previous prime inside a P^1.04 container lies | false |
| P^2+1 square-adjacent phase | gives fixed quadratic/square phase residues already captured by the square-phase routers | false |
| P is coprime to P^2±r for 1<=r<P | removes the q=P local obstruction but leaves all q<P square-phase cover residues | false |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PM1ShiftChangesTheta052Scale | true | true | ±1 changes (P^2)^0.52 only by O(P^-0.96), not by a power of P | none |
| EndpointSandwichLocalizesPrimeIntoPWindow | false | false | the endpoint theorem gives thick containers, not inner P-window localization | PM1OuterTailExclusion OR count dominance |
| EndpointFactorStructureForcesHalfscale | false | false | factorization of P^2-1 and square adjacency of P^2+1 do not imply a prime in the first P slots | PrimeSquareSpecialPhaseNoOuterTailTheorem |
| FiniteBoundaryPromotedToProof | false | false | finite scans remain evidence only | global proof for all sufficiently large prime P |
| RowColumnUnconditionalClosureReached | false | false | neither H_P nor the external/internal versions are unconditionally closed | row_column_unconditional_closed=false |

## 7. 新剩余基

```text
PM1OuterTailExclusionForTheta052Containers
PrimeSquareNearestPrimeWithinPOnAtLeastOneSide
TwoSidedSquarePhaseInnerWindowLocalization
SquarePhaseSpecialPhaseLongBlockPDECExclusion
PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC
ExactExternalSqrtScaleOrGridTransferredThetaHalfSecondMoment
NewSameObjectSignedDispersionOrAutomorphicProof
```

## 8. 边界声明

```text
pm1_sandwich_halfscale_closed=false
pm1_sandwich_no_go_closed=true
prime_square_halfscale_auto_drop_closed=false
square_phase_attack_surface_identified=true
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
