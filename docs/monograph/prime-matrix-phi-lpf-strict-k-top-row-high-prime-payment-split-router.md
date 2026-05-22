# Prime Matrix Phi-LPF strict k top row high-prime payment split 证书

**状态：** `strict_k_top_row_high_prime_leak_split_into_prime_slot_or_low_carrier_payment`

顶行的 high-prime 泄出分成三块：m=1 是真正的素数槽，2<=m<P 是低载体高素数 payment，剩余是所有素因子 <=P 的 smooth 合数槽。目标正性就是证明 m=1 非空。Sylvester-Schur 在 m=1 为空的反设下只推出低载体 payment 非空，不能直接推出矛盾；要闭合还必须证明低载体 payment 加 smooth 槽不能铺满全部 P-1 个槽位。

## 1. high-prime 分裂恒等式

```text
T_P={n:P^2-P<n<P^2}
P-1 = H_1(P)+sum_{2<=m<P}H_m(P)+S_P(P)
H_1(P)=pi(P^2-1)-pi(P^2-P)
H_m(P)=pi(floor((P^2-1)/m))-pi(floor((P^2-P)/m)), 2<=m<P
S_P(P)=# top-row composite slots with all prime factors <=P
H_1(P)>=1
```

这里 `m=1` 正是顶行素数本身；`2<=m<P` 是一个大素数因子被小载体支付，
不是未铺满槽位。

## 2. Sylvester-Schur 的实际强度

```text
若 H_1(P)=0，Sylvester-Schur 只给出 sum_{2<=m<P}H_m(P)>=1，而不是 H_1(P)>=1。
```

因此经典连续乘积输入只定位一笔低载体 payment；它缺少把该 payment 放大成
`H_1(P)>=1` 的机制。

## 3. 有限审计边界

```text
max_prime=5003
case_count=669
all_split_identities_hold=true
minimum_prime_slots_m_equals_1=1
maximum_low_carrier_payment_ratio=0.722222
maximum_p_smooth_composite_ratio=0.500000
finite_evidence_not_used_as_global_proof=true
```

最小 `m=1` 素数槽样本：

| P | H_1(P) |
| ---: | ---: |
| 3 | 1 |
| 5 | 1 |
| 11 | 1 |

低载体 payment 比例最大样本：

| P | low-carrier payment | slot count | ratio | H_1(P) |
| ---: | ---: | ---: | ---: | ---: |
| 37 | 26 | 36 | 0.722222 | 2 |

P-smooth 合数比例最大样本：

| P | P-smooth composite | slot count | ratio | H_1(P) |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 1 | 2 | 0.500000 | 1 |

## 4. 样本分裂

| P | H_1 prime slots | low-carrier payment | P-smooth composite | slot count |
| ---: | ---: | ---: | ---: | ---: |
| 5 | 1 | 2 | 1 | 4 |
| 11 | 1 | 7 | 2 | 10 |
| 17 | 3 | 8 | 5 | 16 |
| 101 | 12 | 60 | 28 | 100 |
| 499 | 44 | 318 | 136 | 498 |
| 5003 | 281 | 3365 | 1356 | 5002 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `HighPrimePaymentSplitIdentityClosed` | `true` | `true` | 顶行槽位精确分裂为 m=1 素数槽、2<=m<P 低载体高素数 payment、以及 P-smooth 合数槽。 | exact split only |
| `PrimeSlotEqualsMOneClosed` | `true` | `true` | 目标正性正是 m=1 high-prime slot 非空。 | prove H_1(P)>=1 |
| `SylvesterSchurLeakLocated` | `true` | `true` | 若 m=1 为空，连续乘积输入只强制 2<=m<P 的低载体 payment 非空。 | single leak is not positivity |
| `LowCarrierPaymentCapacityExceeded` | `false` | `false` | 当前语料没有证明低载体 payment 与 P-smooth 槽的合计容量小于 P-1。 | capacity deficit or positive rejection excess |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只定位 high-prime leak 的真实落点。 | strict row positivity still open |

## 6. 结论

这一层排除了一个常见误读：大素因子泄出不等于顶行有素数。
只有 `m=1` 泄出才是目标正性；`2<=m<P` 泄出是低载体 payment。
剩余硬点是证明低载体 payment 与 P-smooth 合数槽不能合计铺满全部顶行。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_top_row_high_prime_payment_split_router.py` | `31c21d722ca45578c59fd4bf08337c301d97fe3b2246dd278dc7cd028c9b605b` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json` | `d1a4c61c54b866038f6263dd795dad16f3d486faf53a9fcbaa45e0ae2228f058` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json` | `6180246c2e8eae53ef5b16c3731190746c95a781e528a85d08188efbc328ee6c` |
