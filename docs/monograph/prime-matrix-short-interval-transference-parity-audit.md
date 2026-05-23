# Short-Interval Transference Parity Audit

**状态**：`transference_and_prime_pattern_inputs_are_not_single_row_phi_lpf_parity_closure`
**核验日期**：`2026-05-23`

## 1. 直接回答

短区间 AP/Green--Tao 转移和 BDH 均方输入是真实有用的外部技术，
但它们给的是厚短区间中的素数模式或平均控制，不给每个 `P^2` 端点的长度 `P` 单行半窗素数。
因此它们不闭合 Phi-LPF 奇偶障碍。

## 2. 外部源

| name | verified_version | acceptance_status | claim_type | project_role | url |
| --- | --- | --- | --- | --- | --- |
| Le Duc Hieu, Arithmetic progressions of primes in short intervals beyond the 17/30 barrier | arXiv:2509.04883v1, 2025 | arxiv_preprint | k-term prime APs in intervals [x,x+x^theta] for theta>17/30 | prime-pattern abundance in thick short intervals; not endpoint-localized halfscale | https://arxiv.org/abs/2509.04883 |
| Guth--Maynard, New large value estimates for Dirichlet polynomials | Annals 203(2), 2026 | published | short-interval PNT at length x^(17/30+o(1)) | analytic input behind the 17/30 frontier; still gives thick rows at X=P^2 | https://annals.math.princeton.edu/2026/203-2/p06 |
| Matomaki--Shao, Vinogradov's theorem with almost equal summands | arXiv:1405.6592 | published_related_preprint | primes in short intervals/arithmetic progressions for most moduli or averaged settings | useful AP distribution technology; not all prime-square endpoints | https://arxiv.org/abs/1405.6592 |
| Matomaki--Merikoski--Teravainen, Primes in arithmetic progressions and short intervals without L-functions | arXiv:2401.17570v1, 2024 | arxiv_preprint | L-function-free short-interval/AP technology at much longer scales | methodological input; scale far above Prime Matrix halfscale | https://arxiv.org/abs/2401.17570 |
| Green--Tao, The primes contain arbitrarily long arithmetic progressions | Annals 167(2), 2008 | published | global transference theorem for prime AP patterns | transference architecture; not local pointwise prime existence | https://arxiv.org/abs/math/0404188 |

## 3. `X=P^2` 尺度换算

```text
input_variable=X
prime_square_specialization=X=P^2
target_interval=(P^2, P^2+P] or [P^2-P, P^2)
target_theta=0.5
```

| label | theta | length_after_x_equals_p_square | row_thickness_exponent | single_row_halfscale |
| --- | --- | --- | --- | --- |
| target_half_scale | 0.5 | P^1 | 0.0 | true |
| hieu_beyond_17_over_30_plus_0.001 | 0.567666666667 | P^1.13533333333 | 0.135333333333 | false |
| guth_maynard_17_over_30 | 0.566666666667 | P^1.13333333333 | 0.133333333333 | false |
| legacy_0.52_prime_gap_input | 0.52 | P^1.04 | 0.04 | false |
| l_function_free_39_over_40 | 0.975 | P^1.95 | 0.95 | false |

for theta>1/2 the container (P^2,P^2+P^(2theta)] has an outer tail of length P^(2theta)-P, asymptotically almost the whole container

## 4. 转移法缺口

```text
green_tao_or_w_trick_role=removes small prime biases and transfers dense-model pattern counts
missing_prime_matrix_property=anchoring every prime-square endpoint and every Phi-LPF row/column fiber
full_phi_lpf_sieve_needed=avoid all q<P residue covers, not only W with q up to logarithmic size
parity_breaking=false
closes_single_row_halfscale=false
```

## 5. 模式计数定位缺口

```text
whole_container_statement=there are prime APs or many primes in a short interval of length X^theta
required_statement=there is a prime inside the initial/final length-P subinterval for every prime P
outer_tail_can_absorb_patterns=true
closes_prime_square_halfscale=false
```

when theta>1/2, the outer tail length is comparable to the whole thick container, so pattern abundance need not intersect the first row

## 6. 均方到点态缺口

```text
bdh_or_average_role=controls many moduli/intervals on average
missing_pointwise_gate=no exceptional prime-square phase for all P and all relevant fibers
known_failure_mode=a sparse exceptional set can still contain all prime-square rows unless an object-sensitive endpoint theorem is added
closes_row_column_unconditional=false
```

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ShortIntervalAPTransferenceImported | true | false | registered Hieu/Green--Tao style prime-pattern transference as external input | EndpointLocalizationInsidePrimeSquareHalfWindow |
| ThetaGreater17Over30AtPrimeSquareScale | false | false | theta>17/30 gives P^(2/15+epsilon) row thickening after X=P^2 | ThetaLeHalfUniformShortIntervalPrimeTheorem |
| PrimePatternAbundanceForcesFirstRowPrime | false | false | outer tail can absorb the whole-pattern count at theta>1/2 | APPatternLocalizationInsidePrimeSquareHalfWindow |
| WTrickBreaksPhiLPFParity | false | false | W-trick handles small logarithmic primes and dense models, not all q<P Phi-LPF covers | WTrickToFullPhiLPFObjectSensitiveSieve |
| BDHMeanSquareGivesAllRows | false | false | mean-square/AP averages do not remove every prime-square endpoint exception | BDHNoExceptionalPrimeSquarePhaseTheorem |
| RowColumnUnconditionalClosureReached | false | false | external lemma and internal self-contained versions remain open | row_column_unconditional_closed=false |

## 8. 新剩余基

```text
ThetaLeHalfUniformShortIntervalPrimeTheorem
APPatternLocalizationInsidePrimeSquareHalfWindow
BDHNoExceptionalPrimeSquarePhaseTheorem
WTrickToFullPhiLPFObjectSensitiveSieve
MaynardClusterAnchoredAtEveryPrimeSquare
SameObjectSignedDispersionOrAutomorphicEndpointProof
```

## 9. 边界声明

```text
short_interval_transference_inputs_imported=true
prime_pattern_to_first_row_transfer_closed=false
w_trick_phi_lpf_parity_closed=false
bdh_pointwise_all_rows_closed=false
prime_square_halfscale_closed=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
