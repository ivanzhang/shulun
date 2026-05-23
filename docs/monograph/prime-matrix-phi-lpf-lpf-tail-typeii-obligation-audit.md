# Prime Matrix Phi-LPF LPF tail Type-II obligation 审计

**状态：** `lpf_tail_reduced_to_same_row_reciprocal_graph_typeii_obligation`
**核验日期：** `2026-05-23`

## 1. 原子结论

`30-wheel` 后的 LPF tail residual 可精确写成三变量对象：

```text
R_30(P,k)=# {(q,r,a): P/2<q<P, q prime, m=r*a in I_q(P,k),
                 r=LPF(m)>=7, a>=r, a is r-rough }
```

但这个对象不是普通矩形 Type-II 盒。它是同一行 reciprocal graph：

```text
I_q(P,k)=[max(q, floor(kP/q)+1), min(2P-1, floor(((k+1)P-1)/q))]
# I_q(P,k) <= 2,             because P/q < 2
# {q: m in I_q(P,k)} <= 2,   because P/m < 2
# {a: kP<q*r*a<(k+1)P} <= 1, because P/(q*r)<1
```

所以 `q,m` 分解形状上接近平衡，但支撑是极稀疏图；`q,r,a` 分解中
固定 `(q,r)` 的 quotient 纤维只有一个点，不能在该纤维内部产生抵消。
真正需要的是跨越移动 reciprocal graph 的同对象 signed dispersion。

## 2. 有限审计

```text
max_prime=1009
row_count=76789
active_residual_row_count=52697
total_R30=299977
total_direct_prime_count=4172483
total_prime_count_minus_R30=3872506
all_q_m_windows_have_at_most_two_points=true
all_m_q_reverse_fibers_have_at_most_two_points=true
all_qr_a_fibers_have_at_most_one_point=true
all_residual_qr_steps_exceed_row_length=true
finite_evidence_not_used_as_global_proof=true
```

代表样本：

| P | k | N | W_int | R30 | N-R30 | q count | m span | support density | max m/q | max q/m | max a/(q,r) | min qr-P |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 29 | 28 | 5 | 5 | 1 | 4 | 3 | 14 | 0.119048 | 2 | 1 | 1 | 90 |
| 101 | 100 | 12 | 14 | 1 | 11 | 10 | 88 | 0.0159091 | 2 | 1 | 1 | 680 |
| 257 | 256 | 23 | 34 | 3 | 20 | 23 | 242 | 0.00610852 | 2 | 1 | 1 | 1524 |
| 971 | 936 | 80 | 97 | 23 | 57 | 71 | 915 | 0.00149311 | 2 | 1 | 1 | 3600 |
| 1009 | 1008 | 70 | 101 | 9 | 61 | 72 | 980 | 0.00143141 | 2 | 1 | 1 | 4318 |

最大 residual 行：

| P | k | N | W_int | R30 | N-R30 | q count | m span | support density | max m/q | max q/m | max a/(q,r) | min qr-P |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 971 | 936 | 80 | 97 | 23 | 57 | 71 | 915 | 0.00149311 | 2 | 1 | 1 | 3600 |

有限 active residual 最小 `N-R30` 行：

| P | k | N | W_int | R30 | N-R30 | q count | m span | support density | max m/q | max q/m | max a/(q,r) | min qr-P |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 37 | 30 | 3 | 5 | 1 | 2 | 4 | 25 | 0.05 | 2 | 1 | 1 | 124 |

最稀疏 reciprocal graph 行：

```text
P=1009, k=965
W_int=87
q_count=72
m_span=924
rectangle_hull_area=66528
support_density=0.0013077201
```

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
active_residual_row_count=6
total_R30=10782
all_q_m_windows_have_at_most_two_points=true
all_m_q_reverse_fibers_have_at_most_two_points=true
all_qr_a_fibers_have_at_most_one_point=true
all_residual_qr_steps_exceed_row_length=true
large_samples_are_evidence_not_global_proof=true
```

## 4. 外部定理验收边界

短区间素数的 `x^0.52` 点态输入在 `x=P^2` 上仍给 `P^1.04`，
未到本文行长 `P=x^1/2`。Ford--Maynard 型 prime-producing sieve
说明破奇偶通常需要 Type-I/Type-II 或双线性信息，但本层显示所需对象不是
普通矩形盒，而是同一行 reciprocal graph。因此必须新增：

```text
SameRowReciprocalWindowTypeIIDispersionForLPFTail
```

它要直接支付 `N(P,k)-R_30(P,k)>0` 或更强的 LPF tail shell 支配。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LPFTailTripleRepresentation | `true` | `true` | 30-wheel residual 精确写成 q*r*a，其中 r=LPF(m)>=7 且 a 为 r-rough。 | R30=sum_{q,r,a} 1_{kP<qra<(k+1)P} |
| ReciprocalGraphThinFibers | `true` | `true` | 同一行中固定 q 至多两个 m，固定 m 至多两个 q，固定 (q,r) 至多一个 a。 | graph-thin, not rectangular Type-II box |
| QuotientFiberCancellationAvailable | `false` | `false` | 固定 (q,r) 的 a 纤维只有一个点，不能在该纤维内部产生 Type-II 抵消。 | cancellation must run across the moving q-r graph |
| FordMaynardSieveAppliesDirectly | `false` | `false` | prime-producing sieve 需要目标序列的 Type-I/II 输入；本层只给出 exact object 与义务。 | same-row reciprocal-window Type-II theorem required |
| PrimeCountDominatesLPFTailShellSumProved | `false` | `false` | 有限审计中 N-R30 为正，但未证明所有 P,k 的点态支配。 | PrimeCountDominatesLPFTailShellSum |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 6. 当前最窄口

```text
SameRowReciprocalWindowTypeIIDispersionForLPFTail OR PrimeCountDominatesLPFTailShellSum OR SquarePhaseEndpointLowerBound
```

```text
lpf_tail_triple_representation_closed=true
reciprocal_graph_thin_fibers_closed=true
quotient_fiber_cancellation_available=false
external_prime_producing_sieve_applies_directly=false
prime_count_dominates_lpf_tail_shell_sum_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
