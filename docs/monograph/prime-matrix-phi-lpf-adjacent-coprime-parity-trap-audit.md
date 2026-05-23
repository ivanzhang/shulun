# Prime Matrix Phi-LPF adjacent-coprime parity-trap 审计

**状态：** `adjacent_coprime_and_quotient_adjacent_routes_trapped_by_parity_after_30_wheel`
**核验日期：** `2026-05-23`

## 1. 原子结论

在 `30-wheel` residual 中，`m` 没有 `2,3,5` 因子且为合数，故 `r=LPF(m)>=7`。
于是 `q,m,r,a=m/r` 全为奇数。虽然相邻数总是互质：

```text
gcd(qm, qm±1)=1
gcd(m, m±1)=1
gcd(a, a±1)=1
```

但这些相邻数全部被奇偶性强迫为合数：

```text
qm±1, m±1, a±1 are even and >2
```

商相邻提升也不能留在同一行：

```text
q*r*(a±1)=q*r*a ± q*r
q*r > (P/2)*7 > P
```

因此相邻互质和商相邻互质是真刚性，但不是素数支付通道。

## 2. 有限审计

```text
max_prime=1009
row_count=76789
active_residual_row_count=52697
total_R30=299977
total_same_row_adjacent_slots=595083
total_same_row_adjacent_prime_shadows=0
total_cofactor_adjacent_prime_shadows=0
total_quotient_adjacent_prime_shadows=0
total_quotient_lift_inside_row=0
all_active_adjacent_coprime_but_even_composite=true
finite_evidence_not_used_as_global_proof=true
```

代表样本：

| P | k | R30 | same-row adjacent slots | adjacent prime shadows | cofactor checked | quotient checked | quotient lifts inside row |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 29 | 28 | 1 | 2 | 0 | 2 | 2 | 0 |
| 101 | 100 | 1 | 2 | 0 | 2 | 2 | 0 |
| 257 | 256 | 3 | 6 | 0 | 6 | 6 | 0 |
| 971 | 936 | 23 | 44 | 0 | 46 | 46 | 0 |
| 1009 | 1008 | 9 | 18 | 0 | 18 | 18 | 0 |

最大 residual 行：

| P | k | R30 | same-row adjacent slots | adjacent prime shadows | cofactor checked | quotient checked | quotient lifts inside row |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 971 | 936 | 23 | 44 | 0 | 46 | 46 | 0 |

## 3. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
active_residual_row_count=6
total_R30=10782
total_same_row_adjacent_prime_shadows=0
total_quotient_lift_inside_row=0
all_active_adjacent_coprime_but_even_composite=true
large_samples_are_evidence_not_global_proof=true
```

## 4. 外部定理验收边界

Ford--Maynard 型 prime-producing sieve 框架说明，若要从筛对象真正产出素数，
需要与对象匹配的 Type-I/Type-II 或双线性信息。当前相邻互质只给出
`gcd=1`，而在 30-wheel residual 上还立即落入偶合数陷阱；因此不能替代
`PrimeCountDominatesLPFTailShellSum`。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AdjacentCoprimeIdentityClosed | `true` | `true` | 对 n=qm、cofactor m 与 quotient a=m/LPF(m)，相邻数与原数互质。 | gcd(x,x±1)=1 |
| Post30WheelAdjacentParityTrapClosed | `true` | `true` | 30-wheel residual 中 q,m,r,a 全为奇数且 r>=7，所以 n±1、m±1、a±1 全是大于 2 的偶数合数。 | adjacent coprime does not imply prime |
| QuotientAdjacentLiftLeavesRow | `true` | `true` | 商相邻提升的步长为 q*LPF(m)>P，不能同时留在同一长度 P 行内。 | quotient-adjacent same-row transfer closed false |
| AdjacentCoprimePrimePaymentProved | `false` | `false` | 相邻互质路线在 30-wheel residual 上给出 0 个同排相邻素数影子。 | PrimeCountDominatesLPFTailShellSum still required |
| ExternalPrimeProducingSieveAppliesDirectly | `false` | `false` | Ford--Maynard 型 prime-producing sieve 需要 Type-I/II 输入；本文尚无 reciprocal-window 同对象 Type-II 包。 | same-object bilinear/dispersion theorem required |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层不证明 H_P、外部引理版或内部自足版无条件闭合。 | row_column_unconditional_closed=false |

## 6. 当前最窄口

```text
PrimeCountDominatesLPFTailShellSum OR same-object Type-II signed dispersion OR square-phase endpoint lower bound
```

```text
adjacent_coprime_identity_closed=true
post30_adjacent_parity_trap_closed=true
quotient_adjacent_lift_leaves_row_closed=true
adjacent_coprime_prime_payment_proved=false
external_prime_producing_sieve_applies_directly=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
