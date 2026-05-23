# Almost-All Short Interval Exceptional-Spine Audit

**状态**：`almost_all_short_interval_inputs_are_scale_strong_but_spine_pointwise_open`
**核验日期**：`2026-05-23`

## 1. 直接回答

almost-all 短区间素数和高阶一致性结果在尺度上非常强；代入 `X=P^2` 后，
它们的窗口长度都短于目标半窗 `P`。但这些结果允许例外集，而素数平方端点
`{P^2}` 本身就是密度为零的稀疏脊线。因此它们不能自动闭合每个 `P^2` 半窗。

## 2. 外部源

| name | verified_version | acceptance_status | claim_type | project_role | url |
| --- | --- | --- | --- | --- | --- |
| Runbo Li, Primes in almost all short intervals | arXiv:2407.05651v6, 2025-09-25 | arxiv_preprint | almost all intervals [n,n+n^(1/21.5+epsilon)] contain primes | scale-overkill if pointwise; still almost-all only | https://arxiv.org/abs/2407.05651 |
| Runbo Li, Primes in almost all short intervals II | Cambridge Open Engage working paper v1, 2025-10-17 | working_paper_not_peer_reviewed_at_posting | almost all intervals [n-n^(1/22+epsilon),n] contain primes | newest almost-all scale indicator; not a citable unconditional pointwise closure | https://www.cambridge.org/engage/coe/article-details/68f12b20bc2ac3a0e0635f11 |
| Gafni--Tao, On the number of exceptional intervals to the PNT in short intervals | arXiv:2505.24017v1, 2025-05-29 | arxiv_preprint | exceptional-set bounds; PNT in short intervals all x for theta>17/30 and almost all x for theta>2/15 | best exceptional-set framework; still permits structured sparse spines without extra exclusion | https://arxiv.org/abs/2505.24017 |
| Matomaki--Radziwill--Shao--Tao--Teravainen, Higher uniformity II | arXiv:2411.05770v2, 2026; Invent. Math. 2026 | published_inventiones_2026 | almost all short intervals higher uniformity for Lambda, mu and divisor functions | deep almost-all transference/uniformity input; not pointwise on prime-square spine | https://arxiv.org/abs/2411.05770 |

## 3. `X=P^2` 尺度换算

```text
prime_matrix_specialization=X=P^2
target_halfwindow=length P = X^(1/2)
```

| label | theta_as_fraction | theta_decimal | length_after_x_equals_p_square | p_exponent_decimal | shorter_than_halfscale_P | status |
| --- | --- | --- | --- | --- | --- | --- |
| runbo_li_almost_all_1_over_21_5 | 2/43 | 0.046511627907 | P^(4/43) | 0.093023255814 | true | almost_all |
| runbo_li_ii_working_paper_1_over_22 | 1/22 | 0.045454545455 | P^(1/11) | 0.090909090909 | true | almost_all_working_paper |
| gafni_tao_almost_all_2_over_15 | 2/15 | 0.133333333333 | P^(4/15) | 0.266666666667 | true | almost_all_pnt |
| higher_uniformity_lambda_1_over_3 | 1/3 | 0.333333333333 | P^(2/3) | 0.666666666667 | true | almost_all_uniformity |
| target_halfscale | 1/2 | 0.5 | P^(1/1) | 1.0 | false | pointwise_target |

the almost-all inputs are shorter than P after X=P^2; if they were pointwise they would be stronger than needed

## 4. 例外脊线缺口

```text
dyadic_block=X <= n <= 2X
prime_square_spine={P^2: P prime, sqrt(X) <= P <= sqrt(2X)}
spine_size_asymptotic=asymp X^(1/2)/log X
spine_density=asymp 1/(X^(1/2) log X)
required_upgrade=ExceptionalSetIntersectPrimeSquareSpineIsEmptyEventually
```

an o(X) exceptional set, or even a sparse structured exceptional set, may still contain every prime-square endpoint unless a spine-disjointness theorem is proved

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AlmostAllPrimeInputImported | true | false | registered newest almost-all prime interval scales | PrimeSquareSpinePointwiseExclusion |
| ScaleWouldBeatHalfWindowIfPointwise | true | true | all listed almost-all exponents are below 1/2 in X, hence below P at X=P^2 | not a pointwise theorem |
| ExceptionalSetCannotContainPrimeSquares | false | false | almost-all statements do not identify the exceptional set arithmetically | ExceptionalPrimeSquareSpineDisjointness |
| HigherUniformityImpliesEndpointPrime | false | false | almost-all Lambda uniformity gives powerful averages but permits exceptional intervals | PointwiseEndpointUniformityAtEveryP2 |
| PhiLPFParityBrokenByAlmostAll | false | false | Phi-LPF needs every row/column fiber, not density-one rows | AllRowsNoExceptionOrObjectSensitiveSignedSieve |
| RowColumnUnconditionalClosureReached | false | false | external lemma and internal self-contained versions remain open | row_column_unconditional_closed=false |

## 6. 新剩余基

```text
ExceptionalPrimeSquareSpineDisjointness
PointwiseEndpointUniformityAtEveryPrimeSquare
AlmostAllToAllRowsUpgradeWithArithmeticSpineRepulsion
NoPrimeSquareExceptionalPhaseForGafniTaoBounds
PhiLPFObjectSensitiveSignedSieveOnSparseSpine
ThetaLeHalfPointwiseShortIntervalPrimeTheorem
```

## 7. 边界声明

```text
almost_all_short_interval_inputs_imported=true
scale_stronger_than_halfwindow_if_pointwise=true
exceptional_prime_square_spine_excluded=false
pointwise_every_prime_square_endpoint_closed=false
phi_lpf_parity_closed=false
prime_square_halfscale_closed=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
