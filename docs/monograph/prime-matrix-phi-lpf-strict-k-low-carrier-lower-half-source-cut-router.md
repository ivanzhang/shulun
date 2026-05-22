# Prime Matrix Phi-LPF strict k low-carrier lower-half source-cut 证书

**状态：** `strict_k_low_carrier_payment_reduced_to_acyclic_lower_half_source_injection`

low-carrier high-prime payment 不是当前行的自反馈来源：每个支付素数 r>P 都落在当前行左侧并且最多位于 floor(k/2) 行。于是零行反例必须表现为早期下半源 prime injection 与 P-smooth 槽的完美铺满。当前层关闭来源环，但尚未证明该下半源 payment/smooth 反铺满不等式。

## 1. 下半源切断

```text
n=mr, 2<=m<=k, r>P prime, kP<n<(k+1)P
kP/m < r <= ((k+1)P-1)/m
m>=2 => r < ((k+1)P)/2 < kP
therefore floor(r/P) <= floor(k/2)
```

这说明 low-carrier payment 不能由当前行或未来行反向生成；它只能从严格更早的下半行源进入。

## 2. 源素数注入

固定目标行 `(P,k)` 与源素数 `r>P`。若两个不同 carrier `m1<m2` 同时命中该行，
则 `(m2-m1)r>=r>P`，超过行宽 `P-1`。因此每个源素数至多支付一个槽。

零行反设因此变成：

```text
all slots = image(lower-half prime source injection) union P-smooth slots
```

## 3. 有限审计

```text
max_prime=1009
strict_row_count=76797
rows_with_low_carrier_payment=76795
all_payment_sources_in_lower_half=true
finite_evidence_not_used_as_global_proof=true
```

最大 payment 样本：

| value | cases |
| ---: | --- |
| 685 | P=1009, k=968, pay=685, j_max=484, floor(k/2)=484, lanes=m=2:H=38:j<=484 |

最大源行比例样本：

| value | cases |
| ---: | --- |
| 0.500000 | P=5, k=2, pay=1, j_max=1, floor(k/2)=1, lanes=m=2:H=1:j<=1; P=5, k=4, pay=2, j_max=2, floor(k/2)=2, lanes=m=2:H=1:j<=2; P=7, k=4, pay=2, j_max=2, floor(k/2)=2, lanes=m=2:H=1:j<=2; P=7, k=6, pay=2, j_max=3, floor(k/2)=3, lanes=m=2:H=1:j<=3; P=11, k=2, pay=1, j_max=1, floor(k/2)=1, lanes=m=2:H=1:j<=1; P=11, k=4, pay=3, j_max=2, floor(k/2)=2, lanes=m=2:H=1:j<=2; P=11, k=6, pay=4, j_max=3, floor(k/2)=3, lanes=m=2:H=1:j<=3; P=11, k=8, pay=5, j_max=4, floor(k/2)=4, lanes=m=2:H=1:j<=4 |

样本行：

| P | k | payment | max source row | floor(k/2) | bound |
| ---: | ---: | ---: | ---: | ---: | --- |
| 11 | 10 | 7 | 5 | 5 | `true` |
| 101 | 50 | 56 | 25 | 25 | `true` |
| 101 | 100 | 60 | 50 | 50 | `true` |
| 571 | 438 | 382 | 219 | 219 | `true` |
| 1009 | 1008 | 670 | 504 | 504 | `true` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LowCarrierPaymentSourceIntervalClosed` | `true` | `true` | 若 n=mr 落在 strict 行且 r>P 为素数、m>=2，则 r 位于 (kP/m,((k+1)P-1)/m]。 | exact source interval |
| `PaymentSourceLowerHalfCutClosed` | `true` | `true` | 因 m>=2，所有 payment prime r 都满足 r<((k+1)P)/2<kP。 | source row <= floor(k/2) |
| `SameRowAndFuturePaymentLoopExcluded` | `true` | `true` | low-carrier payment 不能来自当前行、近顶端行或未来行。 | acyclic lower-half source only |
| `PaymentInjectionPerSourcePrimeClosed` | `true` | `true` | 固定目标行内，一个源素数 r>P 至多对应一个 carrier m，因为相邻 m 的乘积差为 r>P。 | injective source-to-slot map |
| `ZeroRowReducedToLowerHalfPaymentPlusSmoothTiling` | `true` | `true` | 若 strict 行为零素数行，则所有槽必须由下半源 payment 注入像与 P-smooth 槽铺满。 | lower-half payment image + smooth = all slots |
| `LowerHalfPaymentSmoothAntiTilingProved` | `false` | `false` | 当前语料尚未证明下半源 payment 像与 P-smooth 槽不能完美铺满全部行槽。 | global lower-half payment/smooth anti-tiling inequality |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层排除 payment 来源环并压窄剩余，但不证明 strict 行正性。 | anti-tiling, rejection excess, or sqrt-scale input |

## 5. 结论

本层把 `lambda` payment 负载改写为一个无环下半源注入像。
若 strict 零行存在，它不能再解释为当前行自反馈支付；它必须是下半源 prime injection
与 `P`-smooth 槽的完美铺满。剩余硬点相应压成
`LowerHalfPaymentSmoothAntiTilingInequality`，或回到 raw/rejection strict excess，
或提交真正的 sqrt-scale 短区间输入。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_low_carrier_lower_half_source_cut_router.py` | `cba0ded920358c9c7f0f5708b7941281a0346df312c87830300089d293b13c86` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json` | `09509fd9e17e7dedd36e836dc8f91933c63935f56e8927d15a8bd2a1f3e9e481` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json` | `f4869e5f3736b22201d744255942b3cd84f317f7fdec6173c24dfcd987ba3a9f` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-router.json` | `76620c1c89ec3e690da8d3a4e8b62b3fe82ea12f671da61a4b27e053b35b6a65` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
