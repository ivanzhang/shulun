# Legendre Frontier External Theorem Audit

**状态**：`legendre_frontier_external_inputs_are_near_gates_not_prime_square_halfscale_closure`
**核验日期**：`2026-05-23`

## 1. 直接回答

2026 年 Legendre 相关外部结果确实有帮助，但都不是本文的无条件素数半窗闭合。
RH 条件 larger-powers 结果避开了 `delta=0`；P3 almost-prime 结果落在正确平方区间但对象不是素数；Guth--Maynard 的 `17/30` 仍高于 `1/2`。

## 2. 外部源

| name | verified_version | acceptance_status | claim_type | project_role | url |
| --- | --- | --- | --- | --- | --- |
| Chamberland-Straub, Weakening the Legendre Conjecture | v1, submitted 2026-02-26 | arxiv_preprint_and_RH_conditional | RH-conditional primes between consecutive larger powers x^(2+delta) | conditional near-gate; not delta=0 Legendre and not unconditional | https://arxiv.org/abs/2602.22502 |
| Campbell, On the Existence of Integers with at Most 3 Prime Factors Between Every Pair of Consecutive Squares | v2, 2026-05-19 | arxiv_preprint | unconditional P3 almost-prime in every square interval | parity diagnostic; correct location but wrong prime object | https://arxiv.org/abs/2603.10356 |
| Bordignon-Johnston-Starichkova, explicit Chen theorem and linear sieve | v6, 2025-06-25 | to_appear | explicit linear sieve / P2 additive Chen-type input | technology behind almost-prime results; linear-sieve parity remains | https://arxiv.org/abs/2207.09452 |
| Guth-Maynard, New large value estimates for Dirichlet polynomials | Annals 203(2), 2026 | published | zero-density estimate and short-interval PNT at length x^(17/30+o(1)) | deep pointwise PNT technology; exponent still above 1/2 | https://annals.math.princeton.edu/2026/203-2/p06 |
| Lee, Minimal zero-free regions for results on primes between consecutive perfect kth powers | arXiv:2602.14340v2, 2026 | arxiv_preprint | zero-free-region requirements for primes between consecutive kth powers | quantifies high-power progress toward Legendre; does not reach k=2 | https://arxiv.org/abs/2602.14340 |

## 3. RH larger-powers 尺度

```text
source=Chamberland-Straub under RH
statement_shape=primes between x^(2+delta) and (x+1)^(2+delta)
delta_zero_target=Legendre/PrimeSquareHalfscale with length exponent 1/2
unconditional=false
closes_prime_square_halfscale=false
```

| delta | interval_power | length_exponent_in_X | excess_over_half | matches_delta_zero_legendre |
| --- | --- | --- | --- | --- |
| 0.25 | 2+0.25 | 0.555555555556 | 0.055555555556 | false |
| 0.1 | 2+0.1 | 0.52380952381 | 0.02380952381 | false |
| 0.01 | 2+0.01 | 0.502487562189 | 0.002487562189 | false |
| 0.001 | 2+0.001 | 0.500249875062 | 0.000249875062 | false |

for every fixed delta>0 the length exponent is 1/2 + delta/(2(2+delta)); delta=0 is exactly the open square case and is not supplied

## 4. P3 almost-prime 诊断

```text
source=Campbell 2026 v2
statement_shape=every (n^2,(n+1)^2) contains an integer with at most 3 prime factors counted with multiplicity
location_matches_square_interval=true
object_is_prime=false
closes_prime_square_halfscale=false
```

linear sieve can force almost-prime objects in square intervals but not a prime object

## 5. Guth--Maynard 17/30 尺度

```text
theta=17/30
theta_decimal=0.566666666667
after_x_equals_p_square=P^(17/15)
row_thickness_exponent=0.133333333333
closes_each_p_row=false
```

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RHLargerPowersDeltaPositiveImported | true | false | registered as RH-conditional near-gate; delta=0 remains missing | DeltaZeroLegendreOrPrimeSquareHalfscale |
| P3AlmostPrimeBetweenSquaresImported | true | false | registered as arXiv preprint diagnostic: P3 object in square intervals, not a prime object | P3ToPrimeParityBreakingTransfer |
| LinearSieveParityBrokenByP3Result | false | false | P3 confirms location but not prime parity; it is a parity diagnostic, not a parity break | PrimeObjectExtractionFromP3OrSignedDispersion |
| GuthMaynard17Over30AtHalfscale | false | false | 17/30 gives P^(2/15) row thickening after X=P^2, not one row | ThetaLeHalfOrGridTransferAtHalfscale |
| HighPowerZeroFreeRegionProgressImported | true | false | latest kth-power zero-free-region work quantifies progress for large k, but not k=2 | SquarePowerKEqualsTwoCase |
| RowColumnUnconditionalClosureReached | false | false | neither H_P nor the external/internal versions are unconditionally closed | row_column_unconditional_closed=false |

## 7. 新剩余基

```text
DeltaZeroLegendreOrPrimeSquareHalfscaleTheorem
P3ToPrimeParityBreakingTransferOrObjectSensitiveSignedSieve
ThetaLeHalfPointwiseShortIntervalPrimeTheorem
GridTransferredThetaHalfSecondMoment
PrimeSquareSpecialPhaseNoOuterTailTheorem
NewSameObjectSignedDispersionOrAutomorphicProof
```

## 8. 边界声明

```text
legendre_frontier_external_inputs_imported=true
rh_larger_powers_delta_zero_closed=false
p3_to_prime_transfer_closed=false
prime_square_halfscale_closed=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
