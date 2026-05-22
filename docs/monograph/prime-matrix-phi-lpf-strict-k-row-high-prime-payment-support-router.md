# Prime Matrix Phi-LPF strict k row high-prime payment support 证书

**状态：** `strict_k_row_high_prime_payment_support_bound_identified_capacity_deficit_open`

对任意 strict 行，high-prime 泄出的低载体支撑不是 2<=m<P，而是精确缩到 2<=m<=k。顶行 k=P-1 因此仍是最大支撑硬核。Phi-LPF 端点差分的正性等价于证明低载体 high-prime payment 与 P-smooth 合数槽不能合计铺满 P-1 个槽位；当前语料尚未无条件证明这个 strict-k 容量缺口。

## 1. 一般 strict 行支撑界

```text
I_{k,P}={kP+a:1<=a<P}, 1<k<P
If n=mr in I_{k,P} and r>P, then m<n/P<k+1, hence m<=k.
```

因此低载体 payment 的支撑随 k 增长；顶行 `k=P-1` 是最大支撑情形。

## 2. 行级 high-prime 分裂

```text
P-1=H_1(k,P)+sum_{2<=m<=k}H_m(k,P)+S_k(P)
H_1(k,P)=pi((k+1)P-1)-pi(kP)
H_m(k,P)=pi(floor(((k+1)P-1)/m))-pi(floor(kP/m)), 2<=m<=k
S_k(P)=# row slots with all prime factors <=P
H_1(k,P)>=1
sum_{2<=m<=k}H_m(k,P)+S_k(P)<=P-2
```

这说明端点差分正性正是 `m=1` 非空；`2<=m<=k` 只是低载体支付。

## 3. 有限审计边界

```text
max_prime=1009
prime_count=167
strict_row_count=76797
all_split_identities_hold=true
all_rows_positive_in_finite_sweep=true
minimum_prime_slots_m_equals_1=1
maximum_low_carrier_payment_ratio=0.722222
maximum_p_smooth_composite_ratio=0.806265
top_row_low_payment_ratio_wins_for_each_prime_in_sweep=false
finite_evidence_not_used_as_global_proof=true
```

最小 `m=1` 素数槽样本：

| P | k | H_1(k,P) |
| ---: | ---: | ---: |
| 5 | 4 | 1 |
| 7 | 3 | 1 |
| 11 | 10 | 1 |
| 13 | 9 | 1 |
| 17 | 12 | 1 |
| 19 | 15 | 1 |

低载体 payment 比例最大样本：

| P | k | low-carrier payment | slot count | ratio | H_1(k,P) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 37 | 36 | 26 | 36 | 0.722222 | 2 |

P-smooth 合数比例最大样本：

| P | k | P-smooth composite | slot count | ratio | H_1(k,P) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 863 | 2 | 695 | 862 | 0.806265 | 107 |

## 4. 样本分裂

| P | k | H_1 prime slots | low-carrier payment | P-smooth composite | support |
| ---: | ---: | ---: | ---: | ---: | --- |
| 5 | 2 | 2 | 1 | 1 | `2<=m<=2` |
| 11 | 2 | 3 | 1 | 6 | `2<=m<=2` |
| 11 | 10 | 1 | 7 | 2 | `2<=m<=10` |
| 101 | 50 | 11 | 56 | 33 | `2<=m<=50` |
| 101 | 100 | 12 | 60 | 28 | `2<=m<=100` |
| 1009 | 1008 | 70 | 670 | 268 | `2<=m<=1008` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictRowCarrierSupportBoundClosed` | `true` | `true` | 若 strict 行槽位有素因子 r>P 且不是素数槽，则其低载体满足 2<=m<=k。 | exact support bound |
| `StrictRowHighPrimeSplitClosed` | `true` | `true` | 每行精确分裂为 m=1 素数槽、2<=m<=k 的低载体 high-prime payment、以及 P-smooth 合数槽。 | exact split only |
| `TopRowMaximalCarrierSupportClosed` | `true` | `true` | k=P-1 顶行拥有最大低载体支撑 2<=m<P。 | top row remains necessary hard core |
| `GeneralCapacityDeficitProved` | `false` | `false` | 当前语料没有证明每个 strict 行的低载体 payment 与 P-smooth 槽合计小于 P-1。 | strict-k capacity deficit |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只统一了一般 strict 行的 high-prime payment 支撑。 | strict row positivity still open |

## 6. 结论

一般 strict 行的 high-prime payment 已经被压到最窄支撑 `2<=m<=k`。
这强化了顶行是最大支撑硬核的判断，但仍没有给出无条件正性。
剩余需要一个真正的容量缺口：低载体 payment 与 P-smooth 合数槽不能铺满全部行槽。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_row_high_prime_payment_support_router.py` | `61d72e5d3c66a73810ee9972b91ca83d45c05249a5f14dde005ffcb6082a345b` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-router.json` | `bb71af306ed22cfe27321277790cc929b6d2424336d6f0b2b9cc13263481acb9` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json` | `6180246c2e8eae53ef5b16c3731190746c95a781e528a85d08188efbc328ee6c` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json` | `f825d0e5df9740a53392e3dc0821ca50208291280e33fe9e9ab04e878a70ab3b` |
