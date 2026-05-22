# Prime Matrix Phi-LPF strict k row load phase tradeoff 证书

**状态：** `strict_k_capacity_deficit_reduced_to_payment_smooth_anti_cosaturation`

strict 行正性现在被压成两股负载的反同相问题：低载体 high-prime payment 负载 lambda 与 P-smooth 合数负载 sigma 满足 lambda+sigma+eta=1，其中 eta 是目标素数槽比例。要证明正性，必须证明 lambda 与 sigma 不能同相饱和到 1。有限审计显示两股峰值出现在不同 k/P 相位，但当前语料尚无全局反同相不等式。

## 1. 归一化负载恒等式

```text
lambda(k,P)=sum_{2<=m<=k}H_m(k,P)/(P-1), sigma(k,P)=S_k(P)/(P-1), eta(k,P)=H_1(k,P)/(P-1)
lambda(k,P)+sigma(k,P)+eta(k,P)=1
H_1(k,P)>=1 iff lambda(k,P)+sigma(k,P)<=1-1/(P-1)
```

因此正性不再是计数公式问题，而是 `lambda` 与 `sigma` 不能同时把总质量推到 1 的问题。

## 2. 有限审计边界

```text
max_prime=1009
prime_count=167
strict_row_count=76797
all_split_identities_hold=true
all_rows_positive_in_finite_sweep=true
minimum_prime_slots=1
no_payment_smooth_both_ge_070_in_sweep=true
finite_evidence_not_used_as_global_proof=true
```

全局峰值样本：

| load | value | cases |
| --- | ---: | --- |
| lambda payment | 0.722222 | P=37, k=36, k/P=0.9730, pay=0.722222, smooth=0.222222, prime=2 |
| sigma smooth | 0.806265 | P=863, k=2, k/P=0.0023, pay=0.069606, smooth=0.806265, prime=107 |
| lambda+sigma | 0.952632 | P=571, k=438, k/P=0.7671, pay=0.670175, smooth=0.282456, prime=27 |
| eta prime | 0.500000 | P=5, k=2, k/P=0.4000, pay=0.250000, smooth=0.250000, prime=2; P=5, k=3, k/P=0.6000, pay=0.000000, smooth=0.500000, prime=2 |

最小素数槽样本：

| P | k | H_1(k,P) |
| ---: | ---: | ---: |
| 5 | 4 | 1 |
| 7 | 3 | 1 |
| 11 | 10 | 1 |
| 13 | 9 | 1 |
| 17 | 12 | 1 |
| 19 | 15 | 1 |

## 3. k/P 相位分箱

| phase k/P | rows | max payment | max smooth | max composite | min H_1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `[0.0,0.1)` | 7464 | 0.487395 | 0.806265 | 0.927579 | 5 |
| `[0.1,0.2)` | 7713 | 0.552577 | 0.722222 | 0.933432 | 3 |
| `[0.2,0.3)` | 7714 | 0.588333 | 0.666667 | 0.938567 | 2 |
| `[0.3,0.4)` | 7709 | 0.611369 | 0.500000 | 0.943992 | 2 |
| `[0.4,0.5)` | 7715 | 0.627273 | 0.500000 | 0.943376 | 1 |
| `[0.5,0.6)` | 7714 | 0.645683 | 0.437500 | 0.943434 | 2 |
| `[0.6,0.7)` | 7710 | 0.657658 | 0.500000 | 0.948845 | 1 |
| `[0.7,0.8)` | 7714 | 0.690476 | 0.366667 | 0.952632 | 1 |
| `[0.8,0.9)` | 7715 | 0.685252 | 0.375000 | 0.951439 | 1 |
| `[0.9,1.0)` | 7629 | 0.722222 | 0.333333 | 0.950000 | 1 |

## 4. 样本行

| P | k | payment ratio | smooth ratio | prime ratio | H_1 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 2 | 0.100000 | 0.600000 | 0.300000 | 3 |
| 101 | 2 | 0.100000 | 0.740000 | 0.160000 | 16 |
| 101 | 50 | 0.560000 | 0.330000 | 0.110000 | 11 |
| 101 | 100 | 0.600000 | 0.280000 | 0.120000 | 12 |
| 863 | 2 | 0.069606 | 0.806265 | 0.124130 | 107 |
| 1009 | 1008 | 0.664683 | 0.265873 | 0.069444 | 70 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NormalizedLoadIdentityClosed` | `true` | `true` | 每行满足 lambda_payment+sigma_smooth+eta_prime=1。 | exact normalized ledger |
| `PositivityEquivalentToAntiSaturationClosed` | `true` | `true` | H_1(k,P)>=1 等价于 lambda_payment+sigma_smooth <= 1-1/(P-1)。 | same target in load variables |
| `PhaseTradeoffIdentified` | `true` | `false` | 有限审计显示 payment 峰值与 smooth 峰值分处不同 k/P 相位。 | finite evidence only |
| `AntiCoSaturationInequalityProved` | `false` | `false` | 当前语料没有证明 payment 与 smooth 不能同相饱和。 | global anti-co-saturation inequality |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把容量缺口重写成两股负载反同相问题。 | strict row positivity still open |

## 6. 结论

这一层把剩余硬点改写成全局反同相不等式：
`lambda(k,P)+sigma(k,P)<=1-1/(P-1)`。有限审计支持 payment 与 smooth 峰值错相，
但没有证明全局错相。因此不能声称 strict 行正性已经无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_row_load_phase_tradeoff_router.py` | `0c7ac1b8c05c83dd472d9fbb265d7aea3ce556f90afb2183424242bd89d30fcd` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json` | `09509fd9e17e7dedd36e836dc8f91933c63935f56e8927d15a8bd2a1f3e9e481` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json` | `f825d0e5df9740a53392e3dc0821ca50208291280e33fe9e9ab04e878a70ab3b` |
