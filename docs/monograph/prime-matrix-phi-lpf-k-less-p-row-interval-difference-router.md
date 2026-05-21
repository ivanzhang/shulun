# Prime Matrix Phi-LPF 1<k<P row interval difference 证书

**状态：** `k_less_p_phi_lpf_row_interval_difference_closed_but_row_positivity_open`

对 1<k<P，Phi-LPF 端点差分能直接用于闭区间 [kP,kP+P]。由于两个端点 kP 与 (k+1)P 都是合数倍，闭区间素数数目恰等于内部行 I_k={kP+a:1<=a<P} 的素数数目。它给出逐行素数个数的精确值。但要证明该值为正，必须证明 LPF 合数桶端点增量和小于 P-1；在 1<k<P 时这等价于 full-root 未覆盖槽存在，也就是行内已有素数。因此本层是精确计数闭合和循环边界定位，不是行/列命题的无条件闭合。

## 1. 两个端点公式

闭区间 `[kP,kP+P]`，其中 `1<k<P`：

```text
pi(kP+P)-pi(kP-1)=P+1-sum_{p<=sqrt(kP+P)}[Phi(floor((kP+P)/p),p)-Phi(floor((kP-1)/p),p)]
```

内部行 `I_k={kP+a:1<=a<P}`：

```text
pi(kP+P-1)-pi(kP)=(P-1)-sum_{p<=sqrt(kP+P-1)}[Phi(floor((kP+P-1)/p),p)-Phi(floor(kP/p),p)]
```

正性需要证明：

```text
sum_{p<=sqrt(kP+P-1)}[Phi(floor((kP+P-1)/p),p)-Phi(floor(kP/p),p)] < P-1
```

Phi 递推读法：

```text
Phi(x,p_j)=Phi(x,p_{j+1})+Phi(floor(x/p_j),p_j)
```

因为 `kP` 与 `(k+1)P` 在 `1<k<P` 时都是合数，闭区间计数与内部行计数相同：

```text
pi(kP+P)-pi(kP-1)=pi(kP+P-1)-pi(kP)
```

## 2. k<P 的额外等价

当 `1<k<P` 且 `1<=a<P` 时，`kP+a<P^2`。因此若 `kP+a` 没有任何
`q<=sqrt(kP+P-1)` 的素因子覆盖，它不可能是合数，只能是素数。反过来素数槽当然未被这些
根内素数覆盖。所以 full-root uncovered slots 与 row prime slots 完全相同。

上一层 CRT 样本 `P=5,k=8166` 的确说明一般 `[kP,kP+P]` 全称命题为假；但该样本
满足 `k>P`，不能用于否定本层 `k<P` 行区间目标。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `KLessPEndpointDifferenceIdentityClosed` | `true` | `true` | 端点差分恒等式对任意 2<=A<=B 成立，因此也适用于 1<k<P 的 [kP,kP+P]。 | exact identity |
| `StrictKClosedEqualsInternalRow` | `true` | `true` | 当 1<k<P 时，kP 与 kP+P=(k+1)P 都是合数端点，闭区间素数数目等于内部行素数数目。 | endpoints contribute zero primes |
| `InternalRowFormulaClosed` | `true` | `true` | 对 I_k={kP+a:1<=a<P}，素数数目等于 P-1 减去 full-root LPF 桶端点增量和。 | pi(kP+P-1)-pi(kP) |
| `PhiRecurrenceComputesBucketDeltas` | `true` | `true` | Phi 递推可机械计算每个桶端点值，样本与 LPF 直接计数一致。 | recurrence, not asymptotic |
| `InsidePSquarePrimeUncoveredEquivalence` | `true` | `true` | 因为 1<k<P 且 1<=a<P，所以 kP+a<P^2；full-root 未覆盖槽等价于素数槽。 | uncovered iff prime |
| `PreviousCRTPrimeFreeBlockApplicableToKLessP` | `false` | `false` | 上一层 P=5,k=8166 的全合数闭区间样本满足 k>P，不能否定 k<P 行区间目标。 | need k<P-specific argument |
| `IntervalPositivityFromIdentityAlone` | `false` | `false` | 要推出行内有素数，仍需证明 LPF 合数桶增量和小于 P-1。 | composite bucket delta < row length |
| `FullRootUncoveredSlotPositiveProved` | `false` | `false` | 正性就是 full-root 未覆盖槽存在；这与 row-prime 目标等价，不能作为内部黑箱。 | noncircular short-interval input still missing |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把 1<k<P 的 Phi-LPF 行差分完全规范化；未证明行/列命题无条件闭合。 | Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure |

## 4. 内部行样本

| P | k | interval | length | LPF composite delta | endpoint prime count | direct prime count | uncovered=prime |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 5 | 4 | [21,24] | 4 | 3 | 1 | 1 | `true` |
| 11 | 10 | [111,120] | 10 | 9 | 1 | 1 | `true` |
| 101 | 100 | [10101,10200] | 100 | 88 | 12 | 12 | `true` |

## 5. 闭区间端点样本

| P | k | interval | length | endpoint prime count | internal prime count | closed=internal |
| ---: | ---: | --- | ---: | ---: | ---: | --- |
| 5 | 4 | [20,25] | 6 | 1 | 1 | `true` |
| 11 | 10 | [110,121] | 12 | 1 | 1 | `true` |

## 6. Phi 递推样本

`P=17, k=16, interval=[273, 288]`

`all_bucket_recurrence_matches_lpf_count=true`

| p | left x | right x | delta | recurrence ok |
| ---: | ---: | ---: | ---: | --- |
| 2 | 136 | 144 | 8 | `true` |
| 3 | 90 | 96 | 3 | `true` |
| 5 | 54 | 57 | 1 | `true` |
| 7 | 38 | 41 | 1 | `true` |
| 11 | 24 | 26 | 0 | `true` |
| 13 | 20 | 22 | 0 | `true` |

## 7. 有限审计边界

```text
max_prime=97
case_count=1010
all_internal_rows_positive_in_finite_sweep=true
all_full_root_uncovered_equals_prime_slots=true
minimum_prime_count=1
finite_evidence_not_used_as_global_proof=true
```

最小样本行：

| P | k | interval | prime count |
| ---: | ---: | --- | ---: |
| 3 | 2 | [7,8] | 1 |
| 5 | 4 | [21,24] | 1 |
| 7 | 3 | [22,27] | 1 |
| 11 | 10 | [111,120] | 1 |
| 13 | 9 | [118,129] | 1 |
| 17 | 12 | [205,220] | 1 |
| 19 | 15 | [286,303] | 1 |

## 8. 结论

Phi-LPF 端点差分在 `1<k<P` 行内已经完全可用：它给出精确素数个数值，并可由 Phi 递推机械计算。
剩余硬点被压成一个清晰不等式：LPF 合数桶端点增量和必须小于 `P-1`。
但这个不等式在 `1<k<P` 行内等价于 full-root 未覆盖槽存在，也等价于行内有素数。
因此它不能作为非循环内部黑箱；下一步仍需从 Q1/Q2 传输、seed/PDEC 作用域、signed table 或外部短区间输入中突破。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_k_less_p_row_interval_difference_router.py` | `f5cad0501648497c364ca49d4348123149f51e22213de208e197205b020da261` |
| `docs/monograph/prime-matrix-phi-lpf-endpoint-interval-difference-router.json` | `e0b7301c85ca5828aca8fc99ab225cbccc166f860ad2a62dfcbf7bfcda350e65` |
| `docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.json` | `6b5c87084ccd8da64c98664cffddfec39cb616129b00181d3694d998510f184f` |
| `docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json` | `80ae10c28cd1700bb3e5fb1280198a2332468800f9ea8e306dd8d699a22716f6` |
| `docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json` | `29531aaae09ccded34fee1864cffa649834298d947fd7ba74637a85fd88c9b40` |
