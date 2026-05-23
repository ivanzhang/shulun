# Prime Square Half-Scale Specialization Audit

**状态**：`prime_square_endpoint_structure_is_attack_surface_not_halfscale_theorem`
**核验日期**：`2026-05-23`

## 1. 直接回答

把 `X=P^2` 代入通用短区间定理不会自动把指数从 `0.52` 降到 `1/2`。
`P` 为素数确实给出平方相位刚性，但当前已知外部定理没有把这种刚性转成每个素数平方端点的长度 `P` 素数存在定理。

## 2. 尺度换算

| input | after_x_equals_p_square | target_length | directly_sufficient |
| --- | --- | --- | --- |
| Baker-Harman-Pintz 0.525 | P^1.05 | P | false |
| Runbo Li arXiv:2308.04458 v8 0.52 | P^1.04 | P | false |
| needed prime-square half-scale theorem | P | P | true |

## 3. 右侧窗口与左侧窗口

```text
right_window_target=PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP
right_window_current_corpus_proved=false
left_window_target=PrimeIndexedOppermannLeftTopRow
left_window_current_corpus_proved=false
```

既有有限边界：

```text
finite_boundary_available=true
max_p=200000
prime_count=17984
failure_count=0
max_ratio_record={'p': 5, 'least_offset': 4, 'least_prime': 29, 'offset_ratio': 0.8}
```

## 4. 可证明结构收益

| structure | meaning | effect |
| --- | --- | --- |
| q=P is harmless | for 1<=r<P, P does not divide P^2+r or P^2-r | removes one trivial local obstruction only |
| square-phase CRT vector | for q<P, the forbidden residue is r≡-P^2 mod q on the right and r≡P^2 mod q on the left | turns the problem into a special square-phase long-block avoidance problem |
| survivor-to-prime gate | if P^2±r avoids all prime divisors q<P for 1<=r<P, then it is prime | converts a full low-prime-cover exclusion into a prime existence theorem |
| local wheel deletions | parity and 6-wheel factors delete some candidate cofactors | gives real finite/capacity tightening but not a global lower bound |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExternalTheta052SpecializedToPrimeSquare | true | true | substitution X=P^2 gives length P^1.04, still longer than P | theta<=1/2 or prime-square-specific theorem |
| PrimeFactorStructureAutomaticallyDropsExponent | false | false | the endpoint being a prime square gives CRT phase rigidity, not a known density theorem | SquarePhaseSpecialPhaseLongBlockPDECExclusion OR PrimeSquareEndpointNoExceptionalPhaseTheorem |
| RightFirstHalfPrimeSquareFiniteBoundary | true | false | finite scan has no failure but is not a proof | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| PhiLPFHalfScaleGlobalBreakthrough | false | false | 6-wheel and Phi-LPF identities tighten the residual but still need global square-phase positivity or signed dispersion | PuncturedWheel6EndpointCapacityInequality OR signed/dispersion input |
| RowColumnUnconditionalClosureReached | false | false | neither H_P nor the external/internal versions are unconditionally closed | row_column_unconditional_closed=false |

## 6. 新剩余基

```text
SquarePhaseSpecialPhaseLongBlockPDECExclusion
TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound
PrimeSquareEndpointNoExceptionalPhaseTheorem
PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP
PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC
ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch
NewAutomorphicDispersionProof
```

## 7. 边界声明

```text
prime_square_halfscale_auto_drop_closed=false
square_phase_attack_surface_identified=true
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
