# Prime Matrix Phi-LPF punctured endpoint 6-wheel capacity 证书

**状态：** `parity_capacity_tightened_to_euler_6_wheel_capacity`
**核验日期：** `2026-05-23`

## 1. 原子结论

- 上一层 parity capacity 只扣除偶数 `m>2`。
- 本层加入 Euler `6`-wheel：若 `m>3` 且 `3|m`，则 `m` 也不能为素数。
- 因此 forest-hole 上界从 `C_par` 收紧为 `C_6=W_int-E_{2,3}`。
- 有限审计 `P<=1009` 中，`C_6` 严格闭合所有 strict-k 行；上一层唯一 parity 等号行 `P=19,k=15` 被删除。

## 2. 有限审计

```text
max_prime=1009
row_count=76789
closed_by_parity_ceiling_count=76788
closed_by_wheel6_ceiling_count=76789
parity_not_closed_count=1
wheel6_not_closed_count=0
wheel6_nonpositive_margin_count=0
all_holes_leq_wheel6_ceiling=true
finite_evidence_not_used_as_global_proof=true
```

上一层最小 parity margin 行：

```text
P=19, k=15, Delta=3, C_par=3, margin=0, C_6=2, Delta-C_6=1
```

最小 6-wheel margin 行：

```text
P=11, k=10, Delta=2, C_6=1, Delta-C_6=1, holes=1, primes=1
```

最大 6-wheel 额外扣除行：

```text
P=967, k=965, extra_deletion=28, C_par=50, C_6=22
```

代表样本：

| P | k | Delta | W_int | parity ceiling | wheel6 ceiling | Delta-wheel6 | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 10 | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
| 19 | 15 | 3 | 5 | 3 | 2 | 1 | 2 | 1 |
| 101 | 100 | 16 | 14 | 7 | 5 | 11 | 4 | 12 |
| 257 | 256 | 29 | 34 | 16 | 12 | 17 | 6 | 23 |
| 1009 | 1008 | 89 | 101 | 54 | 34 | 55 | 19 | 70 |

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sampled_wheel6_margins_positive=true
minimum_sample_delta_minus_wheel6_ceiling=2781
large_samples_are_evidence_not_global_proof=true
```

| P | k | Delta | W_int | parity ceiling | wheel6 ceiling | Delta-wheel6 | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100003 | 2 | 8013 | 0 | 0 | 0 | 8013 | 0 |  |
| 100003 | 24999 | 4626 | 0 | 0 | 0 | 4626 | 0 |  |
| 100003 | 25000 | 4623 | 0 | 0 | 0 | 4623 | 0 |  |
| 100003 | 33406 | 4661 | 1342 | 671 | 449 | 4212 | 119 |  |
| 100003 | 100002 | 4900 | 6249 | 3131 | 2119 | 2781 | 515 |  |
| 300007 | 2 | 22178 | 0 | 0 | 0 | 22178 | 0 |  |
| 300007 | 75000 | 12614 | 0 | 0 | 0 | 12614 | 0 |  |
| 300007 | 75001 | 12535 | 0 | 0 | 0 | 12535 | 0 |  |
| 300007 | 90261 | 12626 | 2323 | 1153 | 757 | 11869 | 200 |  |
| 300007 | 300006 | 13238 | 16876 | 8444 | 5574 | 7664 | 1272 |  |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ParityCapacityImported | `true` | `true` | 上一层已证明 \|F(P,k)\|<=W_int(P,k)-E_even(P,k)。 | parity capacity imported |
| Wheel6ForcedCompositeCeilingClosed | `true` | `true` | 若 m>3 且 3\|m，则 m 也不可能为素数；与偶数扣除合并得到 6-wheel ceiling。 | C_6(P,k)=W_int(P,k)-E_{2,3}(P,k) |
| FiniteAuditWheel6StrictClosureAfterParityTie | `true` | `true` | P<=1009 审计中 6-wheel ceiling 严格闭合所有行；上一层 P=19,k=15 的 parity 等号被 m=27 的 3-倍数扣除删除。 | finite audit only |
| GlobalWheel6EndpointCapacityInequalityProved | `false` | `false` | 尚未证明所有 P,k 都满足 DeltaPhi_half(P,k)>C_6(P,k)。 | PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC |
| PhiLPFParityBarrierBrokenGlobally | `false` | `false` | 本层是奇偶窗到 6-wheel 窗的真实收紧，但不是全局 square-root-scale 正性或 signed dispersion 定理。 | sqrt-scale theorem OR structural signed/dispersion input |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 5. 当前最窄口

```text
PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC
```

本层不证明 Phi-LPF 奇偶障碍的全局突破；它把 parity-only 剩余严格收紧到 `6`-wheel endpoint capacity 或相应 PDEC。

```text
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
