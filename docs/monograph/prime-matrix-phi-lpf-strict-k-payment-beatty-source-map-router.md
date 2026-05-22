# Prime Matrix Phi-LPF strict k payment Beatty source-map 证书

**状态：** `strict_k_low_carrier_payment_rewritten_as_unique_beatty_near_multiple_source_map`

low-carrier payment 的下半源注入可被完全规范成唯一 Beatty 近倍数映射：源素数 r>P 是否支付目标行，只取决于 kP mod r 是否落在 r-P+1 到 r-1 的尾段。因此零行反例必须由这张近倍数源像与 P-smooth 槽完美铺满；当前层未证明该Beatty/smooth 反铺满不等式。

## 1. 唯一近倍数源映射

对 strict 行 `1<k<P`，low-carrier payment 源素数满足：

```text
P<r<=floor(((k+1)P-1)/2), r prime
m=floor(kP/r)+1
a=m*r-kP=r-(kP mod r)
payment iff 1<=a<P
```

因为 `P/r<1`，固定 `r` 的 carrier 至多一个；因此 payment 源表不是可自由选择的多值关系，
而是一张由 `kP mod r` 决定的唯一近倍数表。

## 2. 与 H_m payment 的一致性

```text
sum_{2<=m<=k} H_m(k,P)
= #{prime r>P: a=r-(kP mod r) lies in [1,P-1]}
```

零行反设被改写为：

```text
all slots = image(Beatty near-multiple prime sources) union P-smooth slots
```

## 3. 有限审计

```text
max_prime=257
strict_row_count=6227
all_hm_counts_match_beatty_source_map=true
finite_evidence_not_used_as_global_proof=true
```

最大 payment 样本：

| value | cases |
| ---: | --- |
| 171 | P=257, k=244, pay=171, source_upper=31482, max_slot=255; P=257, k=248, pay=171, source_upper=31996, max_slot=256 |

样本行：

| P | k | H_m payment | Beatty count | source upper | sample sources |
| ---: | ---: | ---: | ---: | ---: | --- |
| 11 | 10 | 7 | 7 | 60 | r=13,m=9,a=7; r=17,m=7,a=9; r=19,m=6,a=4; r=23,m=5,a=5; r=29,m=4,a=6 |
| 101 | 50 | 56 | 56 | 2575 | r=103,m=50,a=100; r=107,m=48,a=86; r=109,m=47,a=73; r=113,m=45,a=35; r=127,m=40,a=30 |
| 101 | 100 | 60 | 60 | 5100 | r=103,m=99,a=97; r=107,m=95,a=65; r=109,m=93,a=37; r=113,m=90,a=70; r=127,m=80,a=60 |
| 571 | 438 | 382 | 382 | 125334 | r=577,m=434,a=320; r=587,m=427,a=551; r=593,m=422,a=148; r=599,m=418,a=284; r=601,m=417,a=519 |
| 1009 | 1008 | 670 | 670 | 509040 | r=1013,m=1005,a=993; r=1019,m=999,a=909; r=1021,m=997,a=865; r=1031,m=987,a=525; r=1033,m=985,a=433 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `UniqueCarrierForSourcePrimeClosed` | `true` | `true` | 固定源素数 r>P 时，区间 (kP/r,((k+1)P-1)/r] 长度小于 1，因此至多一个 carrier。 | unique carrier |
| `BeattyCarrierFormulaClosed` | `true` | `true` | 若存在 carrier，则必为 m=floor(kP/r)+1。 | canonical carrier |
| `NearMultipleResidueCriterionClosed` | `true` | `true` | payment 槽位为 a=r-(kP mod r)，且 payment 当且仅当 1<=a<P。 | near-multiple source criterion |
| `HmPaymentEqualsBeattySourceCountClosed` | `true` | `true` | sum_{2<=m<=k} H_m(k,P) 等于满足近倍数准则的下半源素数个数。 | exact source-table equality |
| `ZeroRowReducedToBeattySourcePlusSmoothTiling` | `true` | `true` | 零行反设等价于 Beatty 近倍数源像与 P-smooth 槽铺满全部行槽。 | Beatty-source image + smooth = all slots |
| `BeattySmoothAntiTilingProved` | `false` | `false` | 当前语料尚未证明 Beatty 近倍数源像不能与 P-smooth 槽完美铺满。 | Beatty smooth anti-tiling inequality |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层规范化 payment 源表，但不证明 strict 行正性。 | anti-tiling, rejection excess, or sqrt-scale input |

## 5. 结论

本层把 low-carrier payment 的源注入从抽象计数改写为显式近倍数判别。
这进一步排除 payment 选择自由：失败若存在，必须表现为 Beatty 尾段源像与
`P`-smooth 槽的完美铺满。剩余硬点为 `BeattySmoothAntiTilingInequality`，
或回到 raw/rejection strict excess，或提交真正的 sqrt-scale 输入。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_payment_beatty_source_map_router.py` | `cde49329bd1dfa224a189e670b72a659a349545b64822a02af5573ab46a5f03c` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.json` | `5b9dc9505da45b6bece3b4e96849a10a16ac232a1a4611ecfc6e8ad47858e903` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json` | `f4869e5f3736b22201d744255942b3cd84f317f7fdec6173c24dfcd987ba3a9f` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
