# Prime Matrix Phi-LPF finite-H truncation closure 审计

**状态：** `finite_h_truncation_closed_weighted_phase_and_lpf_extraction_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQLPFShellWeightedReciprocalPhaseSaving / AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII / AND UniformFiniteHTruncationWithHPolylog | UniformFiniteHTruncationWithHPolylog | true | deterministic Vaaler truncation plus thin-fibre absolute mass bound; no new prime theorem required |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | requires Buchstab transfer and denominator audit, not a one-gate bookkeeping closure |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package state; not the fastest mathematical hard-point closure |

本轮选择 Prime Matrix 行/列 Phi-LPF 链，因为 `UniformFiniteHTruncationWithHPolylog` 是纯截断账本，可完全闭合；二点筛和 RH 线仍分别卡在 Buchstab 转移和独立审稿包。

## 2. 截断定理

```text
mass_bound=For every strict row, total high-q reciprocal candidate mass W_int(P,k)<=2*pi(P)<2P; two endpoint sawtooth tails have absolute mass <=4P.
vaaler_tail_rule=With H>=1, endpoint truncation error is O(P/H) for nonnegative LPF-shell counting weights, after summing absolute weights.
polylog_choice=For any target A>0 choose H=ceil((log P)^(A+2)); then the tail is O(P/log^(A+2)P), hence O(P/log^A P).
finite_mode_reduction=Only |h|<=H weighted phases remain; coefficients have harmonic cost O(log H)=O(log log P).
```

关键点是：每个 `q` 的 reciprocal window 至多两个点，故总候选质量 `<=2*pi(P)<2P`；两个 endpoint sawtooth 的绝对尾质量 `<=4P/H`。选择 `H=(log P)^(A+2)` 后，截断尾项已带任意对数节省。

## 3. 代表尺度

| P | target_log_power_A | chosen_H | endpoint_tail_bound_le | tail_over_P_numeric | finite_mode_count_le |
| --- | --- | --- | --- | --- | --- |
| 101 | 4 | 9663 | 4P/log^6P | 0.000413950119 | 19326 |
| 101 | 8 | 4383596 | 4P/log^10P | 9.12493e-07 | 8767192 |
| 1009 | 4 | 109497 | 4P/log^6P | 3.6530681e-05 | 218994 |
| 1009 | 8 | 250610247 | 4P/log^10P | 1.5961e-08 | 501220494 |
| 100003 | 4 | 2328740 | 4P/log^6P | 1.717667e-06 | 4657480 |
| 100003 | 8 | 40913652002 | 4P/log^10P | 9.8e-11 | 81827304004 |
| 1000003 | 4 | 6953480 | 4P/log^6P | 5.75252e-07 | 13906960 |
| 1000003 | 8 | 253320498442 | 4P/log^10P | 1.6e-11 | 506640996884 |

这些数值只展示截断尺度；闭合本身来自上面的符号质量上界。

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_weighted_phase | reason_not_direct |
| --- | --- | --- | --- | --- |
| Vaaler finite Fourier approximation for sawtooth | closes deterministic polylog truncation once absolute thin-fibre mass is O(P) | true | false |  |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | power-saving bilinear forms with Kloosterman sums modulo arbitrary q | false | false | finite-field Kloosterman sums after completion, not the present real reciprocal phase with LPF-shell weights |
| Pascadi 2025 arXiv:2511.08445 | non-abelian amplification for composite-modulus Kloosterman sums | false | false | composite-modulus Kloosterman setting; present denominator q is prime and the missing step is LPF-weighted completion |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | Kloosterman sums over square-free and smooth parameters | false | false | useful only after finite-field Kloosterman completion and parameter transfer |

Milićević--Qin--Wu、Pascadi、Shao--Shparlinski--Wijaya 等 Kloosterman 前沿都继续作为 weighted phase 的候选技术源；它们不影响本层 finite-H 截断闭合，也不能直接替代 LPF 带权相位证明。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| UniformFiniteHTruncationWithHPolylog | true | true | Choose H=(log P)^(A+2); reciprocal thin-fibre total mass gives sawtooth tail O(P/log^A P). | none |
| PrimeQLPFShellWeightedReciprocalPhaseSaving | false | false | Finite modes still need cancellation with prime-q and LPF-shell/rough quotient weights. | weighted finite-mode phase saving |
| WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII | false | false | LPF condition must be converted without circularity into a Type-II/Kloosterman-compatible coefficient package. | LPF weight extraction identity/theorem |

## 6. 最新最窄口

```text
PrimeQLPFShellWeightedReciprocalPhaseSaving
AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII
```

状态边界：

```text
uniform_finite_h_truncation_closed=true
weighted_sawtooth_phi_lpf_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
