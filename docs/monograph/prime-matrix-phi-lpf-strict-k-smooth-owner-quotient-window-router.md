# Prime Matrix Phi-LPF strict k smooth owner quotient-window 证书

**状态：** `strict_k_smooth_slots_refined_to_lpf_owner_quotient_windows`

本层把 `P`-smooth 槽也写成 quotient-window。对 owner prime `p`，令 `n=pq` 落在 strict 行内。
`p` 是 LPF-owner 当且仅当 `q` 为 `p`-rough；该槽是 `P`-smooth 当且仅当 `q` 的最大素因子不超过 `P`。

```text
S_P(k)=sum_{p<=sqrt((k+1)P-1)} #{ q :
  floor(kP/p)<q<=floor(((k+1)P-1)/p),
  LPF(q)>=p, LPMax(q)<=P }.
```

结合前一层 high-prime Beatty/Euclidean source windows：

```text
N_P(k)=(P-1)-B_P(k)-S_P(k),
N_P(k)>=1 iff B_P(k)+S_P(k)<=P-2.
```

## 1. 有限审计

```text
max_prime=257
strict_row_count=6227
all_dual_quotient_window_identities_hold=true
minimum_prime_count=1
finite_evidence_not_used_as_global_proof=true
```

最大 smooth 样本：

```text
P=257, k=2, N=39, B=21, S=196, fill=0.847656
```

最接近双窗口铺满样本：

```text
P=59, k=42, N=3, B=40, S=15, fill=0.948276
```

## 2. 样本行

| P | k | N_P(k) | B high-prime | S smooth | dual formula | first owner rows |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 11 | 10 | 1 | 7 | 2 | 1 | 2:2 |
| 101 | 50 | 11 | 56 | 33 | 11 | 2:21, 3:5, 5:3, 7:1, 13:1, 53:1, 61:1 |
| 101 | 100 | 12 | 60 | 28 | 12 | 2:16, 3:6, 5:3, 7:1, 11:1, 13:1 |
| 257 | 244 | 20 | 171 | 65 | 20 | 2:39, 3:15, 5:2, 7:5, 11:2, 13:2 |
| 571 | 438 | 27 | 382 | 161 | 27 | 2:102, 3:29, 5:9, 7:3, 11:4, 13:2, 17:1, 19:1 |
| 1009 | 1008 | 70 | 670 | 268 | 70 | 2:159, 3:53, 5:17, 7:10, 11:5, 13:5, 17:5, 19:2 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SmoothOwnerQuotientWindowClosed | `true` | `true` | P-smooth 槽等于 LPF-owner p 的 p-rough 且 P-smooth cofactor q 窗口计数之和。 | smooth owner windows |
| HighPrimeBeattyWindowClosed | `true` | `true` | high-prime payment 槽等于 Beatty/Euclidean source-window prime 计数。 | high-prime source windows |
| DualWindowExactValueClosed | `true` | `true` | N_P(k)=(P-1)-B_P(k)-S_P(k)，其中 B 与 S 均为 quotient-window 计数。 | dual quotient-window value |
| DualWindowAntiTilingEquivalentClosed | `true` | `true` | 正性等价于 high-prime source windows 与 smooth owner windows 未铺满 P-1 个槽。 | same positivity target |
| DualWindowAntiTilingProved | `false` | `false` | 本层没有证明双窗口不能铺满。 | global dual-window anti-tiling inequality |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层只统一了两个 quotient-window 源域。 | anti-tiling, rejection excess, or sqrt-scale input |

## 4. 结论

strict 行的两个合数源域现在都已写成 quotient-window：最大素因子大于 P 的槽来自 Beatty/Euclidean high-prime source windows；最大素因子不超过 P 的槽来自 LPF-owner 的 rough cofactor windows。剩余硬点正是这两个窗口源域不能共同铺满目标行。

本层关闭的是 smooth 槽源域的 quotient-window 口径，不是双窗口反铺满不等式。
最新剩余仍为 `DualWindowAntiTilingProved`、
`PositiveRejectionExcessForStrictKRawLPFIncidence` 或真正的 `SqrtGapInputAfterX`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json` | `eed9e255475862b421b6591d3b431a111368cf67d9e75c52bf67ba600c7d9409` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.json` | `c6fbac529d47b04093d14185381cf071de813a9182a00fa03a8dcc92689bf2c6` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json` | `d0b1755f1ba90db1c954b73254aad74aef846825e80dc38b7a128638e7550b6c` |
