# Prime Matrix Phi-LPF strict k endpoint Beatty-smooth exact value 证书

**状态：** `strict_k_endpoint_difference_rewritten_as_beatty_smooth_exact_value`

本层把用户要求的 `[kP,kP+P]` 端点差计数同最新 Beatty payment 源表合并。结论是：

```text
N_P(k)=pi((k+1)P-1)-pi(kP)
      =(P-1)-sum_{p<=sqrt((k+1)P-1)}[Phi(floor(((k+1)P-1)/p),p)-Phi(floor(kP/p),p)]
      =(P-1)-B_P(k)-S_P(k).
```

其中 `B_P(k)` 是 Beatty 近倍数 high-prime payment 源像，`S_P(k)` 是行内 `P`-smooth 合数槽。
因此正性精确等价于：

```text
N_P(k)>=1  iff  B_P(k)+S_P(k)<=P-2.
```

这一步给出精确值坐标，但不自动证明该不等式；未证部分正是 Beatty/smooth 反铺满硬点。

## 1. 有限审计

```text
max_prime=257
strict_row_count=6227
all_endpoint_beatty_smooth_value_identities_hold=true
all_rows_positive_in_finite_sweep=true
minimum_prime_count=1
finite_evidence_not_used_as_global_proof=true
```

最接近铺满的有限样本：

```text
max_composite_fill=0.948276
P=59, k=42, prime=3, B=40, S=15, fill=0.948276
```

## 2. 样本行

| P | k | N_P(k) | B Beatty | S smooth | B+S | P-1 | formula ok | first prime slots |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 11 | 10 | 1 | 7 | 2 | 9 | 10 | `true` | 3 |
| 101 | 50 | 11 | 56 | 33 | 89 | 100 | `true` | 1, 9, 27, 31, 37, 49, 51, 57 |
| 101 | 100 | 12 | 60 | 28 | 88 | 100 | `true` | 3, 11, 33, 39, 41, 51, 59, 63 |
| 257 | 244 | 20 | 171 | 65 | 236 | 256 | `true` | 15, 23, 35, 45, 53, 65, 83, 93 |
| 571 | 438 | 27 | 382 | 161 | 543 | 570 | `true` | 11, 25, 49, 55, 71, 101, 155, 161 |
| 1009 | 1008 | 70 | 670 | 268 | 938 | 1008 | `true` | 5, 25, 47, 59, 67, 85, 101, 107 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EndpointDifferenceExactValueClosed | `true` | `true` | Phi-LPF 端点差分给出 N_P(k)=pi((k+1)P-1)-pi(kP) 的精确值。 | exact interval value |
| BeattySmoothCompositeSplitClosed | `true` | `true` | 在 1<k<P 时，每个合数槽唯一落入 P-smooth 槽或 Beatty high-prime payment 槽。 | composite split |
| ExactValueAsPMinusBeattyMinusSmoothClosed | `true` | `true` | N_P(k)=(P-1)-B_P(k)-S_P(k)，其中 B_P(k) 是 Beatty 源像，S_P(k) 是 P-smooth 槽。 | row prime count value |
| PositivityEquivalentToBeattySmoothAntiTilingClosed | `true` | `true` | N_P(k)>=1 等价于 B_P(k)+S_P(k)<=P-2。 | same positivity target |
| BeattySmoothAntiTilingInequalityProved | `false` | `false` | 当前层没有证明 B_P(k)+S_P(k)<=P-2 对所有 1<k<P 成立。 | global anti-tiling inequality |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层给出精确值坐标，不给出 strict 行正性的无条件证明。 | anti-tiling, rejection excess, or sqrt-scale input |

## 4. 结论

Phi-LPF 端点差分能给出 [kP,kP+P] 内部行素数个数的精确值；结合 Beatty 源表后，该值等于 (P-1)-B_P(k)-S_P(k)。正性剩余不是计数恒等式问题，而是 Beatty 源像与 P-smooth 槽不能铺满全部槽的全局不等式。

当前层关闭的是端点差精确值与 Beatty/smooth 分解，不是 strict 行正性的无条件证明。
下一步最窄接口仍是 `BeattySmoothAntiTilingInequality`、
`PositiveRejectionExcessForStrictKRawLPFIncidence` 或真正的 `SqrtGapInputAfterX`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json` | `fda512a55d40c2b2e3dbac432b0bcff1c47efd7bea9e5b96e9bb291804214316` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.json` | `070201d42be143cbddc67c573b9e4c82648687672b03396f3591b6ad953ae0ac` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json` | `f4869e5f3736b22201d744255942b3cd84f317f7fdec6173c24dfcd987ba3a9f` |
