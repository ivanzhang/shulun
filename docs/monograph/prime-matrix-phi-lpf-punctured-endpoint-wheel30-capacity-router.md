# Prime Matrix Phi-LPF punctured endpoint 30-wheel capacity 证书

**状态：** `wheel6_capacity_tightened_to_euler_30_wheel_capacity`
**核验日期：** `2026-05-23`

## 1. 原子结论

- 上一层 6-wheel capacity 已扣除 `m>2` 偶数与 `m>3` 的 3 倍数。
- 本层加入 Euler `30`-wheel：若 `m>5` 且 `5|m`，则 `m` 也不能为素数。
- 因此 forest-hole 上界从 `C_6` 收紧为 `C_30=W_int-E_{2,3,5}`。
- 有限审计 `P<=1009` 中，`C_30` 严格闭合所有 strict-k 行；这只作为有限一致性证据。

## 2. 有限审计

```text
max_prime=1009
row_count=76789
closed_by_wheel6_ceiling_count=76789
closed_by_wheel30_ceiling_count=76789
wheel6_not_closed_count=0
wheel30_not_closed_count=0
wheel30_nonpositive_margin_count=0
all_holes_leq_wheel30_ceiling=true
finite_evidence_not_used_as_global_proof=true
```

上一层最小 6-wheel margin 行：

```text
P=11, k=10, Delta=2, C_6=1, margin=1, C_30=1, Delta-C_30=1
```

最小 30-wheel margin 行：

```text
P=11, k=10, Delta=2, C_30=1, Delta-C_30=1, holes=1, primes=1
```

最大 30-wheel 额外扣除行：

```text
P=997, k=952, extra_deletion=16, C_6=39, C_30=23
```

代表样本：

| P | k | Delta | W_int | C_6 | C_30 | Delta-C_30 | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 10 | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
| 19 | 15 | 3 | 5 | 2 | 2 | 1 | 2 | 1 |
| 101 | 100 | 16 | 14 | 5 | 5 | 11 | 4 | 12 |
| 257 | 256 | 29 | 34 | 12 | 9 | 20 | 6 | 23 |
| 1009 | 1008 | 89 | 101 | 34 | 28 | 61 | 19 | 70 |

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sampled_wheel30_margins_positive=true
minimum_sample_delta_minus_wheel30_ceiling=3215
large_samples_are_evidence_not_global_proof=true
```

| P | k | Delta | W_int | C_6 | C_30 | Delta-C_30 | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100003 | 2 | 8013 | 0 | 0 | 0 | 8013 | 0 |  |
| 100003 | 24999 | 4626 | 0 | 0 | 0 | 4626 | 0 |  |
| 100003 | 25000 | 4623 | 0 | 0 | 0 | 4623 | 0 |  |
| 100003 | 33406 | 4661 | 1342 | 449 | 366 | 4295 | 119 |  |
| 100003 | 100002 | 4900 | 6249 | 2119 | 1685 | 3215 | 515 |  |
| 300007 | 2 | 22178 | 0 | 0 | 0 | 22178 | 0 |  |
| 300007 | 75000 | 12614 | 0 | 0 | 0 | 12614 | 0 |  |
| 300007 | 75001 | 12535 | 0 | 0 | 0 | 12535 | 0 |  |
| 300007 | 90261 | 12626 | 2323 | 757 | 620 | 12006 | 200 |  |
| 300007 | 300006 | 13238 | 16876 | 5574 | 4485 | 8753 | 1272 |  |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Wheel6CapacityImported | `true` | `true` | 上一层已证明 \|F(P,k)\|<=W_int(P,k)-E_{2,3}(P,k)。 | 6-wheel capacity imported |
| Wheel30ForcedCompositeCeilingClosed | `true` | `true` | 若 m>5 且 5\|m，则 m 也不可能为素数；与 2,3 扣除合并得到 30-wheel ceiling。 | C_30(P,k)=W_int(P,k)-E_{2,3,5}(P,k) |
| FiniteAuditWheel30StrictClosure | `true` | `true` | P<=1009 审计中 30-wheel ceiling 严格闭合所有行；最小 margin 仍为正。 | finite audit only |
| GlobalWheel30EndpointCapacityInequalityProved | `false` | `false` | 尚未证明所有 P,k 都满足 DeltaPhi_half(P,k)>C_30(P,k)。 | PuncturedWheel30EndpointCapacityInequalityOrReciprocalPrimePairWheel30SaturationPDEC |
| PhiLPFParityBarrierBrokenGlobally | `false` | `false` | 本层是 6-wheel 到 30-wheel 的真实收紧，但不是全局 square-root-scale 正性或 signed dispersion 定理。 | sqrt-scale theorem OR structural signed/dispersion input |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 5. 当前最窄口

```text
PuncturedWheel30EndpointCapacityInequalityOrReciprocalPrimePairWheel30SaturationPDEC
```

本层不证明 Phi-LPF 奇偶障碍的全局突破；它把 `6`-wheel endpoint capacity 收紧到 `30`-wheel endpoint capacity 或相应 PDEC。

```text
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
