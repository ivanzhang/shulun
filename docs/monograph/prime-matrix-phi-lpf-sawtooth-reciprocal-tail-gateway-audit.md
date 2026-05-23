# Prime Matrix Phi-LPF sawtooth reciprocal tail gateway 审计

**状态：** `sawtooth_reciprocal_tail_split_unweighted_closed_weighted_open`
**核验日期：** `2026-05-23`

## 1. 选择最快子门

三原子门中，本轮选择先攻：

```text
SawtoothTailLogSavingForThinReciprocalFibres
```

原因是 endpoint floor/sawtooth 已给出明确倒数相位，至少无权模型可以用经典二阶导数估计推进。

## 2. 无权解析基准

```text
phase=e(h*k*P/u)
model_sum=S(A;N)=sum_{N<n<=2N} e(A/n), A=h*k*P, N=P
classical_second_derivative_bound=S(A;N) << sqrt(A/N)+sqrt(N^3/A)
row_scale_substitution=S << sqrt(h*k)+P/sqrt(h*k)
active_row_comparability=if the high-q reciprocal graph is nonempty, then q,m>P/2 forces k+1>P/4, so k is P-scale away from finitely many edge rows
active_row_polylog_h_consequence=for active rows and h<=H=(log P)^B, finite unweighted sawtooth modes contribute O(P^(1/2)H^(1/2)) and truncation tail O(P/H)
unweighted_log_saving_conclusion=unweighted endpoint benchmark gives arbitrary log saving versus P for sufficiently large P
```

这是真推进：`SawtoothTailLogSavingForThinReciprocalFibres` 中的无权倒数相位障碍已经不是主硬点。
但它还不是 Phi-LPF 闭合，因为真实权重来自 prime `q`、`r=LPF(m)` 与 `r`-rough quotient。

## 3. 有限无权 prime-q 诊断

| P | k | h | actual_abs_sum | trivial_q_count | actual_over_trivial | vdc_surrogate |
| --- | --- | --- | --- | --- | --- | --- |
| 101 | 50 | 4 | 2.503802 | 10 | 0.25038 | 21.283914 |
| 101 | 97 | 5 | 6.877629 | 10 | 0.687763 | 26.608889 |
| 101 | 100 | 8 | 3.290356 | 10 | 0.329036 | 31.85516 |
| 257 | 128 | 6 | 5.707668 | 23 | 0.248159 | 36.986502 |
| 257 | 245 | 3 | 8.317348 | 23 | 0.361624 | 36.590471 |
| 257 | 256 | 3 | 5.707668 | 23 | 0.248159 | 36.986502 |
| 509 | 254 | 6 | 11.601397 | 42 | 0.276224 | 52.076873 |
| 509 | 485 | 5 | 11.800893 | 42 | 0.280974 | 59.580513 |
| 509 | 508 | 3 | 11.601397 | 42 | 0.276224 | 52.076873 |
| 1009 | 504 | 7 | 8.543936 | 72 | 0.118666 | 76.384368 |
| 1009 | 961 | 4 | 10.125208 | 72 | 0.140628 | 78.274194 |
| 1009 | 1008 | 6 | 14.440694 | 72 | 0.200565 | 90.743228 |

该表只说明实际无权高 `q` 素数相位并不呈现结构性灾难；它不替代全局证明，也没有包含 LPF 权重。

## 4. 外部定理匹配

| source | useful_part | matched_to_unweighted_benchmark | matched_to_phi_lpf_weighted_object | remaining |
| --- | --- | --- | --- | --- |
| classical van der Corput/Kusmin-Landau second derivative estimate | handles the unweighted real reciprocal phase e(A/u) | true | false | PrimeQLPFShellWeightedReciprocalPhaseSaving |
| Duke-Friedlander-Iwaniec 1997 | bilinear Kloosterman fractions after inverse-modulus completion | false | false | ReciprocalGraphToKloostermanCompletionIdentity |
| Bettin-Chandee 2015/2018 and Wright 2026 | trilinear Kloosterman fractions and partially fixed-moduli dispersion | false | false | CompletedKloostermanMeanForPrimeQAndLPFShellWeights |
| Shao-Shparlinski-Wijaya 2025/2026, sums of Kloosterman sums over square-free and smooth integers | power savings for finite-field Kloosterman sums with square-free or smooth parameters | false | false | finite-field Kloosterman completion plus prime-q/LPF-shell transfer |

Shao--Shparlinski--Wijaya 的 square-free/smooth Kloosterman sum 结果是有用的新外部参考，
但它工作在固定有限域 Kloosterman sum参数上；本文当前 sawtooth 相位仍是实倒数相位 `e(A/q)`，
并且还带有逐行 LPF-shell 权重。因此它不能直接关闭本门。

## 5. 新门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DeterministicSawtoothEndpointIdentity | true | true | floor endpoint 产生 psi(kP/u) 与有限 Fourier 相位 e(h*kP/u)。 | identity closed; cancellation not included |
| VaalerTruncationTailWithThinTotalWeight | true | true | 若总权重为 O(P)，取 H=(log P)^B 时，截断尾项为 O(P/(log P)^B)。 | tail bookkeeping closed after choosing B |
| ActiveHighQRowsHavePScaleK | true | true | 若 high-q reciprocal window 非空，则 q,m>P/2 迫使 qm>P^2/4，从而 k+1>P/4。 | active sawtooth rows are P-scale |
| UnweightedReciprocalPhaseVanDerCorputBenchmark | true | true | 对 sum_{n≈P} e(h*kP/n)，二阶导数估计给 O(sqrt(hk)+P/sqrt(hk))；active rows 与 h≤log^B P 时给幂节省。 | only an unweighted interval benchmark |
| PrimeQLPFShellWeightedReciprocalPhaseSaving | false | false | 真实对象是 prime q 与 LPF-shell/rough cofactor 权重，不是无权连续区间。 | need weighted reciprocal phase saving uniformly in P,k,h |
| SawtoothTailLogSavingForThinReciprocalFibres | false | false | 无权 benchmark 已闭合，但带权 finite-h 相位和仍未闭合。 | PrimeQLPFShellWeightedReciprocalPhaseSaving |

## 6. 最新最窄口

```text
PrimeQLPFShellWeightedReciprocalPhaseSaving
AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII
AND UniformFiniteHTruncationWithHPolylog
```

状态边界：

```text
unweighted_sawtooth_benchmark_closed=true
weighted_sawtooth_phi_lpf_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
