# Prime-Power Slope Sandwich Audit

**状态**：`prime_power_slope_sandwich_has_length_coincidence_but_misses_p2_location`
**核验日期**：`2026-05-23`

## 1. 直接回答

不能。`(P^(50/26))^0.52=P` 的确给出长度巧合，
但该短区间位于 `P^(25/13)` 附近，距离 `P^2` 仍为 `asymp P^2`。
`P^(50/24)` 位于 `P^2` 之上更远处，其 `0.52` 半径也只到 `P^(13/12)`，
同样无法触及 `P^2` 半窗。

## 2. 指数恒等式

```text
theta=13/25
lower_endpoint=P^(25/13)
center_endpoint=P^(2/1)=P^2
upper_endpoint=P^(25/12)
lower_radius_exponent=1/1
upper_radius_exponent=13/12
target_halfscale=P
```

## 3. 端点容器

| label | endpoint | guaranteed_radius | side | distance_to_p2_scale | radius_reaches_p2 |
| --- | --- | --- | --- | --- | --- |
| lower_X=P^(50/26)=P^(25/13) | P^(25/13) | P^1 | below_P2 | P^2 | false |
| center_X=P^(50/25)=P^2 | P^(2/1) | P^(26/25) | at_P2 | 0 | true |
| upper_X=P^(50/24)=P^(25/12) | P^(25/12) | P^(13/12) | above_P2 | P^(25/12) | false |

## 4. 位置-半径不相容

```text
lower_gap_to_center=P^2-P^(25/13)=P^2(1-P^(-1/13)) asymp P^2
lower_guaranteed_radius=P
lower_gap_over_radius=asymp P
upper_gap_to_center=P^(25/12)-P^2=P^2(P^(1/12)-1) asymp P^(25/12)
upper_guaranteed_radius=P^(13/12)
upper_gap_over_radius=asymp P
```

both guaranteed containers are a factor P too far from P^2 in the power scale

一般地，若 `X=P^a`，则通用 `X^theta` 定理给长度 `P^(a theta)`。
要中心在 `P^2` 必须 `a=2`；要长度为 `P` 必须 `a theta=1`。
二者同时成立等价于 `theta=1/2`。

```text
require_location=a=2 for X=P^2
require_radius_p=a*theta=1
simultaneous_solution_requires=theta=1/2
with_theta_13_over_25=a=25/13 gives radius P but not location P^2
closes_halfscale=false
```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExponentLengthCoincidenceRecognized | true | true | (P^(50/26))^(13/25)=P and (P^2)^(1/2)=P | location mismatch |
| LowerContainerTouchesP2 | false | false | the lower container has length P but lies around P^(25/13), far below P^2 | P2MinusLowerEndpointGapExclusion |
| UpperContainerTouchesP2 | false | false | the upper container lies around P^(25/12), far above P^2; radius P^(13/12) is too small | UpperEndpointGapToP2Bridge |
| SandwichForcesPrimeIntoP2HalfWindow | false | false | two far-away existence intervals do not imply existence in (P^2,P^2+P] or [P^2-P,P^2) | PrimeSquareEndpointLocalization |
| RowColumnUnconditionalClosureReached | false | false | external lemma and internal self-contained versions remain open | row_column_unconditional_closed=false |

## 6. 新剩余基

```text
PrimeSquareEndpointLocalizationNotExponentInterpolation
ThetaEqualsHalfOrPrimeSquareSpecificPointwiseTheorem
P2CenteredContainerPrimeLowerBound
OuterScaleGapBridgeBetweenP25Over13AndP2
SameObjectSignedDispersionOrAutomorphicEndpointProof
```

## 7. 边界声明

```text
prime_power_slope_sandwich_no_go_closed=true
exponent_length_coincidence_closed=true
lower_container_reaches_p2=false
upper_container_reaches_p2=false
prime_square_halfscale_closed=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
