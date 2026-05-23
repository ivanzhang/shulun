# Prime Matrix Phi-LPF weight extraction norm closure 审计

**状态：** `lpf_shell_weight_extracted_to_bounded_coefficients_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQLPFShellWeightedReciprocalPhaseSaving / AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII | LPFShellWeightBoundedCoefficientExtraction | true | pure support and coefficient-norm ledger after finite-H truncation; no new prime theorem required |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | still needs Buchstab transfer and denominator audit |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable algebraic coefficient gate |

finite-H 截断闭合后，本轮选择行/列 Phi-LPF 的 LPF 权重抽取子门。该子门是纯支撑与范数账本；二点筛与 RH 线没有同样可直接闭合的代数子门。

## 2. 有界系数抽取定理

```text
triple_package=R_30(P,k)=sum_{P/2<q<P prime} sum_{r>=7 prime} sum_{a>=r, P^-(a)>=r} beta(q,r,a) 1_{kP<qra<(k+1)P}, beta in {0,1}.
one_point_qr_fiber=Since q*r>P for r>=7 and q>P/2, each fixed (q,r) has at most one quotient a in a row.
q_projection=The q-projected LPF weight b(q)=# {m in I_q(P,k): m composite and LPF(m)>=7} satisfies 0<=b(q)<=#I_q(P,k)<=2.
total_mass=sum_q b(q)=R_30(P,k)<=W_int(P,k)<=2*pi(P)<2P.
norm_conclusion=LPF extraction causes no coefficient blow-up: linf(beta)<=1, linf(b)<=2, l1 total O(P).
rejected_route=Do not expand the rough condition by full Mobius inclusion-exclusion over all primes <r; that exact identity is true but has exponential l1 risk and is unnecessary for the coefficient package.
```

关键点是：LPF-shell 不需要展开成所有小素数的 Möbius 排斥和。保留 `r=LPF(m)` 与 `a` 为 `r`-rough 的三元图系数即可，系数为 `0/1`；再投影到每个 prime `q` 时，由 `#I_q(P,k)<=2` 直接得到 `b(q)<=2`。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_R30=299977
max_projected_q_weight_seen=1
max_qr_fiber_weight_seen=1
all_projected_q_weights_le_2=true
all_qr_fibers_le_1=true
all_total_masses_le_Wint_le_2piP=true
violation_count=0
```

有限审计只验证实现和账本一致性；全局闭合来自上面的符号 thin-fibre 论证。

代表行：

| P | k | q_count | W_int | R30 | max_projected_q_weight | max_qr_fiber_weight | coefficient_linf | shells |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 10 | 14 | 1 | 1 | 1 | 1 | 11:1 |
| 257 | 256 | 23 | 34 | 3 | 1 | 1 | 1 | 11:1, 13:1, 19:1 |
| 971 | 936 | 71 | 97 | 23 | 1 | 1 | 1 | 7:6, 11:4, 13:2, 17:6, 19:1, 23:2, 37:1, 41:1 |
| 1009 | 1008 | 72 | 101 | 9 | 1 | 1 | 1 | 7:1, 11:1, 13:2, 17:1, 23:1, 31:1, 37:1, 41:1 |

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_phase_saving | reason_not_direct |
| --- | --- | --- | --- | --- |
| Vaughan/Heath-Brown Type-I/II identity framework | accepts bounded coefficient sequences after an appropriate bilinear decomposition | true | false | the same-row reciprocal graph and prime-q phase still need their own Type-II/dispersion estimate |
| Duke-Friedlander-Iwaniec 1997 and Bettin--Chandee Kloosterman-fraction technology | bounded coefficients are compatible after inverse-fraction completion | true | false | the completion identity from real reciprocal/product window to inverse Kloosterman form is still missing |
| Milićević--Qin--Wu 2025, Pascadi 2025, Shao--Shparlinski--Wijaya 2024/2025 | frontier Kloosterman estimates for later bounded-coefficient phase work | false | false | they do not directly estimate fixed-row prime-q real reciprocal phases with LPF-shell coefficients |

Vaughan/Heath-Brown、DFI、Bettin--Chandee 与最新 Kloosterman 前沿都可在后续相位估计中利用 bounded coefficients；本层只关闭系数抽取与范数控制，不关闭 prime-q reciprocal phase saving。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LPFShellWeightBoundedCoefficientExtraction | true | true | The LPF-shell condition is absorbed into beta(q,r,a) in {0,1} and q-projected weights b(q)<=2. | none |
| NoMobiusL1ExplosionNeeded | true | true | The proof avoids full roughness inclusion-exclusion; all norms are controlled by thin reciprocal fibres. | none |
| PrimeQBoundedLPFCoefficientReciprocalPhaseSaving | false | false | For \|h\|<=polylog(P), prove cancellation for sum_{q prime} b_{P,k}(q)e(hkP/q) with 0<=b(q)<=2 coming from the LPF graph. | weighted bounded-coefficient prime-q reciprocal phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the same-row reciprocal/product-window form to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQBoundedLPFCoefficientReciprocalPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
lpf_weight_bounded_coefficient_extraction_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
