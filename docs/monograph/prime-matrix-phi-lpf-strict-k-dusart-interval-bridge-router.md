# Prime Matrix Phi-LPF strict k Dusart interval bridge 证书

**状态：** `dusart_2010_closes_log_square_low_k_band_not_all_strict_rows`

Dusart 2010 的显式区间定理可以严格闭合 kP>=396738 且 k<=25 log^2(kP) 的 strict 行；kP<396738 由有限桥验证。但是该外部输入的长度尺度是 x/log^2 x，在 k 接近 P 时约为 P^2/log^2(P^2)，大于行长 P，因此不能替代 sqrt-scale 输入，也不能单独推出全部 1<k<P 行正性。

## 1. 外部输入

```text
Dusart 2010 / arXiv:1002.0442
for x>=396738, [x, x+x/(25 log^2 x)] contains at least one prime
pi(x)>=x/log x*(1+1/log x) for x>=599
pi(x)<=x/log x*(1+1.2762/log x) for x>1
```

该输入作为外部定理使用；本证书不声称已经在仓库内重证 Dusart 的零点自由区和显式表。

## 2. strict 行桥接

```text
x=kP; if x>=396738 and k<=25 log^2(kP), then x/(25 log^2 x)<=P and the Dusart prime lies inside (kP,(k+1)P)
dusart_low_k_condition: k <= 25 log^2(kP)
```

因此 Dusart 输入闭合的是低 k 对数平方带，而不是整个 `1<k<P`。

## 3. 阈值以下有限桥

```text
finite_threshold_x0=396738
sieve_max_n=595107
checked_rows=257198
max_prime_in_bridge=198349
max_k_in_bridge=628
finite_bridge_verified=true
```

## 4. 覆盖审计

```text
max_prime=10007
strict_row_count=5743942
finite_threshold_closed_rows=170482
direct_pi_endpoint_bound_closed_rows=49117
dusart_interval_closed_rows=5394954
union_closed_rows=5565436
union_closed_ratio=0.968923
uncovered_rows_in_sample=178506
first_prime_with_uncovered_row=8101
last_prime_all_rows_closed_in_sample=8093
finite_evidence_not_used_as_global_proof=true
```

样本未覆盖行：

| P | k | x=kP | Dusart margin P-x/(25log^2x) | direct pi margin |
| ---: | ---: | ---: | ---: | ---: |
| 8101 | 8100 | 65618100 | -0.574184 | -55495.133380 |
| 8111 | 8101 | 65707211 | -0.353127 | -55562.138180 |
| 8111 | 8102 | 65715322 | -1.243151 | -55568.286825 |
| 8111 | 8103 | 65723433 | -2.133163 | -55574.435391 |
| 8111 | 8104 | 65731544 | -3.023164 | -55580.583877 |
| 8111 | 8105 | 65739655 | -3.913153 | -55586.732284 |
| 8111 | 8106 | 65747766 | -4.803131 | -55592.880612 |
| 8111 | 8107 | 65755877 | -5.693097 | -55599.028860 |
| 8111 | 8108 | 65763988 | -6.583052 | -55605.177028 |
| 8111 | 8109 | 65772099 | -7.472996 | -55611.325118 |
| 8111 | 8110 | 65780210 | -8.362928 | -55617.473128 |
| 8117 | 8102 | 65763934 | -0.577127 | -55604.804852 |
| 8117 | 8103 | 65772051 | -1.467729 | -55610.957492 |
| 8117 | 8104 | 65780168 | -2.358320 | -55617.110052 |
| 8117 | 8105 | 65788285 | -3.248899 | -55623.262533 |
| 8117 | 8106 | 65796402 | -4.139467 | -55629.414935 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `Dusart2010IntervalInputImported` | `true` | `true` | 外部 Dusart 2010 给出 x>=396738 后长度 x/(25 log^2 x) 的素数存在输入。 | external theorem accepted, not self-contained |
| `StrictRowDusartLowKBridgeClosed` | `true` | `true` | 若 kP>=396738 且 k<=25 log^2(kP)，则 Dusart 素数落在 strict 行内。 | low-k logarithmic band |
| `FiniteBelowThresholdBridgeVerified` | `true` | `true` | kP<396738 的 strict 行已作有限桥验证。 | finite computation only |
| `DusartCoversAllStrictRows` | `false` | `false` | Dusart 长度为 x/log^2 x；在 k 接近 P 时远大于行长 P，不能覆盖全部 strict 行。 | sqrt-scale or anti-co-saturation still needed |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只用外部显式 PNT 闭合低 k/有限桥，不关闭全局行命题。 | high-k rows remain |

## 6. 结论

Dusart 2010 给出了有用的外部显式低 k 桥，但尺度仍是 `x/log^2 x`。
对顶端 `k~P`，这比行长 `P` 大一个约 `P/log^2 P` 的因子。
所以最新剩余仍是 `GlobalPaymentSmoothAntiCoSaturationInequality`、
`PositiveRejectionExcessForStrictKRawLPFIncidence` 或真正的 `SqrtGapInputAfterX`。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_dusart_interval_bridge_router.py` | `fd7f9644f0c4f126dadd807be2f0c1333bba74c0d299747f9970ee0609848495` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json` | `f4869e5f3736b22201d744255942b3cd84f317f7fdec6173c24dfcd987ba3a9f` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json` | `09509fd9e17e7dedd36e836dc8f91933c63935f56e8927d15a8bd2a1f3e9e481` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json` | `f825d0e5df9740a53392e3dc0821ca50208291280e33fe9e9ab04e878a70ab3b` |
