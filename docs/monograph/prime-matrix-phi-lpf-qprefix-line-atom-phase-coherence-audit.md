# Prime Matrix Phi-LPF q-prefix line atom phase coherence 审计

**状态：** `qprefix_line_atom_phase_coherence_blocks_atomwise_saving_route`
**核验日期：** `2026-06-03`

## 1. 当前对象

```text
phase=S_A(h)=sum_{q in A} e(h*P*floor(q*m/P)/q)=sum_{q in A} e(-h*(q*m mod P)/q)
atom=fixed m and contiguous prime-q prefix from endpoint-flux atomization
tested_h_values=[1, 2, 3, 5]
```

## 2. 有限相干审计

```text
max_prime=1009
atom_count_total=15439
edge_count_total=177515
q_prefix_count_min=1
q_prefix_count_median=10
q_prefix_count_max=37
short_atom_count_q_le_4=3687
short_atom_ratio_q_le_4=0.238811
long_atom_count_q_ge_17=4052
long_atom_ratio_q_ge_17=0.262452
h1_ratio_ge_0_90=1561
h1_ratio_ge_0_75=2017
h1_ratio_ge_0_50=3515
h1_sqrt_ratio_ge_2=421
h1_sqrt_ratio_ge_3=78
```

q-prefix 长度分桶：

| q_prefix_bin | atom_count |
| --- | --- |
| 17<=q<=37 | 4052 |
| 2<=q<=4 | 2525 |
| 5<=q<=8 | 3220 |
| 9<=q<=16 | 4480 |
| q=1 | 1162 |

h 汇总：

| h | sum_abs | median_abs_over_length | max_abs_over_length | median_abs_over_sqrt_length | max_abs_over_sqrt_length | ratio_ge_0_90 | sqrt_ratio_ge_3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 45631.233117 | 0.277393 | 1.0 | 0.911531 | 4.528563 | 1561 | 78 |
| 2 | 42935.992317 | 0.265844 | 1.0 | 0.860048 | 3.893219 | 1544 | 48 |
| 3 | 41321.392852 | 0.256399 | 1.0 | 0.838395 | 4.082005 | 1575 | 39 |
| 5 | 41410.714011 | 0.260564 | 1.0 | 0.846647 | 3.976434 | 1534 | 21 |

h=1 近相干样例：

| P | m | strip | q_start | q_end | q_prefix_count | abs_sum | abs_over_length | abs_over_sqrt_length | phase_range_mod_1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 53 | 79 | upper_wing | 29 | 29 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 53 | 83 | upper_wing | 29 | 29 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 53 | 89 | upper_wing | 29 | 29 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 61 | 97 | upper_wing | 31 | 31 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 61 | 101 | upper_wing | 31 | 31 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 61 | 103 | upper_wing | 31 | 31 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 61 | 107 | upper_wing | 31 | 31 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 61 | 109 | upper_wing | 31 | 31 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 61 | 113 | upper_wing | 31 | 31 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |
| 67 | 97 | upper_wing | 37 | 37 | 1 | 1.0 | 1.0 | 1.0 | 0.0 |

## 3. 判定

逐 atom 相消不能作为独立闭合门：当前 atom family 含大量极短 prime-q prefix，
这些 atom 内部没有足够长度产生 cancellation；同时有限审计中存在多个 h=1
近相干 atom。故下一门应二分为短 atom 的带符号聚合/预算吸收，和长 atom
的 moving-prime-denominator completed trace/Kloosterman family。

## 4. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| QPrefixLineAtomPhaseIdentity | True | True | The fixed-m atom phase is exactly e(h*P*floor(q*m/P)/q). | none |
| AtomwiseQPrefixPhaseSavingRoute | False | False | Per-atom cancellation is not a valid standalone route for the current atom family. | short atoms and coherent atoms require aggregation or a stronger trace family |
| ShortAtomAggregationGate | False | False | Atoms with very short q-prefix cannot create internal cancellation. | aggregate short atoms with signed weights or absorb them by a separate budget |
| LongAtomMovingDenominatorTraceGate | False | False | Longer atoms still have moving prime denominator q and are not yet a completed trace/Kloosterman family. | construct completed moving-q denominator trace family |

## 5. 最新最窄口

```text
ShortQPrefixAtomSignedAggregationOrBudgetAbsorption
AND LongQPrefixMovingPrimeDenominatorTraceCompletion
AND NoLossAggregationAcrossQPrefixAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
atomwise_qprefix_phase_saving_closed=false
short_atom_aggregation_closed=false
long_atom_trace_completion_closed=false
no_loss_qprefix_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```
