# Prime Matrix Phi-LPF strict k sqrt gap equivalence 证书

**状态：** `strict_k_phi_lpf_ge_one_reduced_to_sqrt_gap_or_rejection_excess`

Phi-LPF 端点差分确实给出 strict 1<k<P 行的精确素数个数。要把该值证明为 >=1，等价于排除一个 P 网格对齐的平方根尺度素数荒漠，也等价于证明 raw/rejection 的严格正失衡。若未来给出 x 后 sqrt(x) 内必有素数的输入，则充分大部分立即闭合，剩余可有限验证；当前该 sqrt-gap 输入仍未证明。

## 1. >=1 的精确等价

```text
N_P(k)=pi((k+1)P-1)-pi(kP)
N_P(k)>=1 iff next_prime(kP)<(k+1)P
```

由于 `1<k<P`，闭区间两个端点 `kP` 与 `(k+1)P` 都是合数，
所以 `>=1` 完全等价于开行 `(kP,(k+1)P)` 中存在素数。

## 2. sqrt-gap 条件闭合模板

```text
If every x>=X0 has a prime in (x,x+sqrt(x)], then all strict rows with kP>=X0 have N_P(k)>=1 because sqrt(kP)<P.
The remaining rows under that hypothesis satisfy kP<X0; since k>=2, only P<X0/2 must be checked.
```

注意这里需要的是 `x` 后的平方根尺度间隙输入，而不是普通 `theta>1/2` 的短区间输入。

## 3. 样本审计

| P | k | x=kP | interval | row prime count | sqrt(x)<P | P-sqrt(x) |
| ---: | ---: | ---: | --- | ---: | --- | ---: |
| 5 | 4 | 20 | [21, 24] | 1 | `true` | 0.527864 |
| 11 | 10 | 110 | [111, 120] | 1 | `true` | 0.511912 |
| 17 | 16 | 272 | [273, 288] | 3 | `true` | 0.507577 |
| 101 | 50 | 5050 | [5051, 5150] | 11 | `true` | 29.936648 |
| 101 | 100 | 10100 | [10101, 10200] | 12 | `true` | 0.501244 |

## 4. 有限审计边界

```text
max_prime=499
case_count=21346
all_finite_rows_have_prime=true
zero_rows_found=[]
minimum_row_prime_count=1
finite_evidence_not_used_as_global_proof=true
```

最小行素数数样本：

| P | k | row prime count |
| ---: | ---: | ---: |
| 3 | 2 | 1 |
| 5 | 4 | 1 |
| 7 | 3 | 1 |
| 11 | 10 | 1 |
| 13 | 9 | 1 |
| 17 | 12 | 1 |
| 19 | 15 | 1 |

尾部 P 的最小值样本：

| P | min row prime count | sample k |
| ---: | ---: | --- |
| 443 | 27 | `[408]` |
| 449 | 27 | `[196]` |
| 457 | 28 | `[395, 425]` |
| 461 | 27 | `[392]` |
| 463 | 26 | `[390]` |
| 467 | 29 | `[375, 387]` |
| 479 | 28 | `[377]` |
| 487 | 29 | `[371]` |
| 491 | 28 | `[368]` |
| 499 | 29 | `[362]` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PhiLPFExactIntegerValueAvailable` | `true` | `true` | Phi-LPF 端点差分给出 strict 行素数数目的精确整数值。 | exact count only |
| `GEOneEquivalentToPositiveRejectionExcess` | `true` | `true` | 该整数 >=1 等价于 raw/rejection 严格失衡。 | PositiveRejectionExcessForStrictKRawLPFIncidence |
| `GEOneEquivalentToAlignedSqrtGapExclusion` | `true` | `true` | 行值 >=1 等价于没有完整 P 网格行被连续素数间隙覆盖。 | aligned sqrt-scale prime-gap exclusion |
| `SqrtGapInputWouldCloseLargeRows` | `true` | `true` | 若 x 后 sqrt(x) 内总有素数，则因 sqrt(kP)<P，所有充分大 strict 行闭合。 | finite verification below threshold |
| `FiniteVerificationTemplateIdentified` | `true` | `true` | 若 sqrt-gap 输入从 X0 起成立，则仅需有限验证 kP<X0 的行。 | depends on unproved sqrt-gap input |
| `SqrtGapInputProvedInCurrentCorpus` | `false` | `false` | 当前语料没有无条件证明 x 后 sqrt(x) 内总有素数。 | external/internal square-root prime-gap theorem |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层给出 >=1 的等价和条件闭合模板，不给出无条件正性。 | sqrt-gap input or structural rejection-excess proof |

## 6. 结论

Phi-LPF 可以计算出行素数个数这个整数，但 `>=1` 的证明不能从恒等式自身推出。
当前最清楚的闭合模板是：先证明平方根尺度 prime-gap 输入，再做有限验证。
在没有该输入时，非循环主攻仍应回到 `PositiveRejectionExcessForStrictKRawLPFIncidence`。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_sqrt_gap_equivalence_router.py` | `4b5dcda97a5e657276ff439b9bbd10432af1bdf9bb92ad54bbf2322ba1463113` |
| `docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json` | `fda512a55d40c2b2e3dbac432b0bcff1c47efd7bea9e5b96e9bb291804214316` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json` | `dbd0f06356306594afff56e4a199bdc4b27c7eb43688825b17cfd189ca8efa1c` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json` | `d0b1755f1ba90db1c954b73254aad74aef846825e80dc38b7a128638e7550b6c` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json` | `9c8b4ae328fe2254bf81e16e4f058921efc6c3ea616a97f196a42482151dd028` |
