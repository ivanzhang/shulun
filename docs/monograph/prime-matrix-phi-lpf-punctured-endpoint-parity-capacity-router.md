# Prime Matrix Phi-LPF punctured endpoint parity capacity 证书

**状态：** `forest_holes_bounded_by_reciprocal_integer_windows_minus_forced_even_candidates`

本层继续攻击 `PuncturedPhiEndpointDifferencePositiveOrPDEC`。
上一层已有精确恒等式

```text
prime_count(P,k)=DeltaPhi_half(P,k)-|F(P,k)|.
```

对每个 `q` in `(P/2,P)`，reciprocal 窗 `I_q(P,k)` 的整数长度至多为 2。
把所有整数候选数为 `W_int(P,k)`；其中偶数 `m>2` 不可能为素数，记作
`E_even(P,k)`。于是有非循环上界

```text
|F(P,k)| <= C_par(P,k) := W_int(P,k)-E_even(P,k).
```

因此充分条件变为

```text
DeltaPhi_half(P,k) > C_par(P,k).
```

若该不等式失败，反例必须让 odd reciprocal candidates 近乎全部成为 prime-pair holes，
这就是新的更窄 saturated prime-pair 出口。

## 1. 有限审计

```text
max_prime=1009
row_count=76789
closed_by_integer_window_capacity_count=60813
closed_by_parity_ceiling_count=76788
parity_not_closed_count=1
parity_failure_count=0
parity_tie_count=1
parity_ties_have_direct_prime=true
all_holes_leq_parity_ceiling=true
finite_evidence_not_used_as_global_proof=true
```

最小 parity margin 行：

```text
P=19, k=15, Delta=3, C_par=3, margin=0, holes=2, primes=1
```

最大 parity ceiling 行：

```text
P=997, k=996, Delta=79, C_par=59, margin=20
```

未由 strict parity inequality 闭合的有限基例：

| P | k | Delta | W_int | E_even | parity ceiling | Delta-ceiling | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | 15 | 3 | 5 | 2 | 3 | 0 | 2 | 1 |

代表样本：

| P | k | Delta | W_int | E_even | parity ceiling | Delta-ceiling | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 10 | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
| 19 | 15 | 3 | 5 | 2 | 3 | 0 | 2 | 1 |
| 101 | 100 | 16 | 14 | 7 | 7 | 9 | 4 | 12 |
| 257 | 256 | 29 | 34 | 18 | 16 | 13 | 6 | 23 |
| 1009 | 1008 | 89 | 101 | 47 | 54 | 35 | 19 | 70 |

## 2. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sampled_parity_margins_positive=true
minimum_sample_delta_minus_parity_ceiling=1769
large_samples_are_evidence_not_global_proof=true
```

| P | k | Delta | W_int | E_even | parity ceiling | Delta-ceiling | holes | primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100003 | 2 | 8013 | 0 | 0 | 0 | 8013 | 0 |  |
| 100003 | 24999 | 4626 | 0 | 0 | 0 | 4626 | 0 |  |
| 100003 | 25000 | 4623 | 0 | 0 | 0 | 4623 | 0 |  |
| 100003 | 33406 | 4661 | 1342 | 671 | 671 | 3990 | 119 |  |
| 100003 | 100002 | 4900 | 6249 | 3118 | 3131 | 1769 | 515 |  |
| 300007 | 2 | 22178 | 0 | 0 | 0 | 22178 | 0 |  |
| 300007 | 75000 | 12614 | 0 | 0 | 0 | 12614 | 0 |  |
| 300007 | 75001 | 12535 | 0 | 0 | 0 | 12535 | 0 |  |
| 300007 | 90261 | 12626 | 2323 | 1170 | 1153 | 11473 | 200 |  |
| 300007 | 300006 | 13238 | 16876 | 8432 | 8444 | 4794 | 1272 |  |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EndpointDifferenceImported | `true` | `true` | 上一层已证明 prime count = DeltaPhi_half - forest holes。 | endpoint identity imported |
| ReciprocalIntegerWindowCeilingClosed | `true` | `true` | \|F(P,k)\| 不超过 high-q reciprocal 整数短窗总容量 W_int(P,k)。 | integer capacity ceiling |
| ParityForcedCompositeCeilingClosed | `true` | `true` | 每个偶 m>2 不能是 prime，故 \|F(P,k)\|<=W_int(P,k)-E_even(P,k)。 | parity capacity ceiling |
| FiniteAuditParityCapacityClosedAfterBaseTie | `true` | `true` | P<=1009 审计中 parity ceiling 只剩 P=19,k=15 的等号基例，且该行直接有素数。 | finite audit only |
| GlobalParityEndpointCapacityInequalityProved | `false` | `false` | 尚未证明所有 P,k 都满足 DeltaPhi_half(P,k)>W_int(P,k)-E_even(P,k) 或等号时存在额外合成候选。 | PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC |
| UnifiedPositiveCoreProved | `false` | `false` | 本层是更强的非循环容量上界，不证明三目标命题。 | PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC |

## 4. 结论

forest holes 已由 reciprocal 整数短窗容量进一步压到奇偶容量 C_par(P,k)=W_int(P,k)-E_even(P,k)。因此只要 DeltaPhi_half(P,k)>C_par(P,k)，该 strict 行立即有素数。有限审计到 P<=1009 只剩 P=19,k=15 的等号基例，且直接素数数为 1；全局仍需证明 parity endpoint capacity inequality，或把失败相位登记为 reciprocal prime-pair saturation PDEC。

当前最窄口为：

```text
PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC
```

本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只提供更强的
endpoint capacity 上界和新的非循环主攻接口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-difference-router.json` | `5a7b904f7e6feff82f6539fa8bb809178284793bfbd422663ebefa727bf60a5d` |
| `docs/monograph/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.json` | `8a608720597fccf43d673d046fecabc255493974f2a8441d4b3b14a3bb759e4e` |
| `docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json` | `10da31e36ce24880aa1c9ae6014f8d9434a0b16d5217ea9105a7f3fe42585719` |
