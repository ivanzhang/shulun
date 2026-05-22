# Prime Matrix Phi-LPF strict k Beatty Euclidean source-window 证书

**状态：** `strict_k_beatty_payment_refined_to_euclidean_quotient_source_windows`

本层把 Beatty payment 源表继续展开为欧几里得商源行窗口。若目标行为 `k`，carrier 为 `m`，
写：

```text
j=floor(k/m),  k=mj+t, 0<=t<m,  r=jP+b.
```

则 payment 条件等价于：

```text
tP < m b < (t+1)P
floor(tP/m)+1 <= b <= floor(((t+1)P-1)/m).
```

所以

```text
B_P(k)=sum_{2<=m<=k} #{ prime r=jP+b in the corresponding source window }.
```

这比“下半源”更精确：下半源界只是 `j=floor(k/m)<=floor(k/2)` 的推论。

## 1. 有限审计

```text
max_prime=1009
strict_row_count=76797
all_hm_counts_match_quotient_source_windows=true
all_source_rows_in_lower_half=true
finite_evidence_not_used_as_global_proof=true
```

最大 payment 样本：

```text
P=1009, k=968, payment=685, nonempty_windows=357, max_source_row=484
```

最大非空源窗口数样本：

```text
P=1009, k=1008, payment=670, nonempty_windows=368, max_source_row=504
```

## 2. 样本行

| P | k | H_m payment | quotient windows | nonempty windows | max source row | source histogram |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 11 | 10 | 7 | 7 | 7 | 5 | 1:3, 2:2, 3:1, 5:1 |
| 101 | 50 | 56 | 56 | 33 | 25 | 1:13, 2:9, 3:4, 4:4, 5:4, 6:2, 7:2, 8:2 |
| 101 | 100 | 60 | 60 | 39 | 50 | 1:14, 2:4, 3:5, 4:4, 5:3, 6:1, 7:1, 9:1 |
| 571 | 438 | 382 | 382 | 187 | 219 | 1:62, 2:28, 3:16, 4:17, 5:9, 6:11, 7:6, 8:13 |
| 1009 | 1008 | 670 | 670 | 368 | 504 | 1:95, 2:64, 3:40, 4:20, 5:27, 6:20, 7:13, 8:12 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EuclideanSourceRowLawClosed | `true` | `true` | 若 carrier 为 m，则源素数 r 必在源行 j=floor(k/m)。 | exact quotient source row |
| ResidueWindowLawClosed | `true` | `true` | 写 k=mj+t 后，源行余数 b 必满足 tP < mb < (t+1)P。 | rational residue window |
| BeattyPaymentEqualsQuotientWindowPrimeCountClosed | `true` | `true` | B_P(k) 等于所有欧几里得商源行窗口中的素数计数之和。 | source-window payment table |
| LowerHalfSourceCutRefined | `true` | `true` | j=floor(k/m)<=floor(k/2)，所以下半源切口是该商行定律的直接推论。 | lower-half source is quotient law |
| BeattySmoothAntiTilingProved | `false` | `false` | 本层没有证明这些源行窗口与 P-smooth 槽不能共同铺满目标行。 | source-window/smooth anti-tiling inequality |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本层细化 payment 来源，不证明 strict 行正性。 | anti-tiling, rejection excess, or sqrt-scale input |

## 4. 结论

Beatty payment 源表进一步等价于欧几里得商源行窗口表：每个 carrier m 只读取早期源行 floor(k/m) 的一个短有理窗口。这把反铺满硬点从抽象的 Beatty 源像改写为早期源行窗口供给与 P-smooth 槽的耦合不等式。

本层关闭的是 payment 源行与源窗口的选择自由；它没有证明这些源窗口供给与 `P`-smooth 槽不能铺满。
最新剩余仍是 `BeattySmoothAntiTilingInequality`、
`PositiveRejectionExcessForStrictKRawLPFIncidence` 或 `SqrtGapInputAfterX`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.json` | `070201d42be143cbddc67c573b9e4c82648687672b03396f3591b6ad953ae0ac` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json` | `eed9e255475862b421b6591d3b431a111368cf67d9e75c52bf67ba600c7d9409` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.json` | `5b9dc9505da45b6bece3b4e96849a10a16ac232a1a4611ecfc6e8ad47858e903` |
