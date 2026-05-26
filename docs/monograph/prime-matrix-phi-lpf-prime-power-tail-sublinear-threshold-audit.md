# Prime Matrix Phi-LPF prime-power tail sublinear threshold 审计

**状态：** `prime_power_tail_is_sublinear_but_pointwise_psi_sqrt_window_still_open`
**核验日期：** `2026-05-26`

## 1. 解析压缩

对 strict row

```text
I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P
```

上一层已证明：

```text
theta(I_{P,k})>0 iff psi(I_{P,k})>prime_power_tail(I_{P,k})
```

本层把尾巴进一步压成统一次线性阈值：

```text
prime_power_tail(I_{P,k}) <= log(P)*((sqrt(2)-1)*sqrt(P)+1+(floor(log2(P^2-1))-2)*((2^(1/3)-1)*P^(1/3)+1))
prime_power_tail(I_{P,k}) = O(sqrt(P)*log(P)+P^(1/3)*log(P)^2)=o(P)
```

因此新的闭合合同是：

```text
Any rowwise lower bound psi(I_{P,k}) >= eta*P for fixed eta>0 would exceed the prime-power tail for all sufficiently large P.
```

## 2. 样本审计

```text
actual_tail_bound_all_samples=true
sublinear_tail_bound_all_samples=true
prime_power_tail_sublinear_threshold_closed=true
positive_proportion_psi_would_close_rows_eventually=true
known_short_interval_input_reaches_sqrt_window=false
pointwise_psi_row_positive_proportion_proved=false
admissible_signed_typeii_or_trace_family_constructed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| P | rows | max tail k | max actual tail | actual tail / P | global sublinear bound / P | max root-bound k |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 30 | 11 | 4.890349 | 0.157753 | 1.774798 | 2 |
| 101 | 100 | 21 | 7.513709 | 0.074393 | 1.346966 | 2 |
| 251 | 250 | 1 | 8.416710 | 0.033533 | 0.921868 | 1 |
| 1009 | 1008 | 1 | 14.176733 | 0.014050 | 0.517390 | 1 |
| 3001 | 3000 | 1 | 26.082042 | 0.008691 | 0.329294 | 1 |
| 10007 | 10006 | 1 | 53.795750 | 0.005376 | 0.184886 | 1 |

最大样本行快照：

```text
P=10007, k=1
prime_power_tail_count=15
prime_power_tail_mass=53.795750
integer_root_mass_bound=488.185127
global_sublinear_mass_bound=1850.158123
prime_power_items_sample=16384=2^14, 19683=3^9, 15625=5^6, 16807=7^5, 14641=11^4, 12167=23^3
```

## 3. 解析阈值趋势

| P | sublinear mass bound | bound / P |
| ---: | ---: | ---: |
| 1000 | 520.051471 | 0.520051471 |
| 10000 | 1849.595304 | 0.184959530 |
| 1000000 | 19534.046679 | 0.019534047 |
| 100000000 | 190599.032375 | 0.001905990 |
| 1000000000000 | 16977349.602034 | 0.000016977 |

## 4. 外部前沿阈值

| 外部输入 | 源 | strict-row 结论 |
| --- | --- | --- |
| Runbo Li short intervals | https://arxiv.org/abs/2308.04458 | closes_strict_row=false; exponent 0.52 remains above the square-root row exponent 0.5 |
| Runbo Li large-modulus AP/Harman | https://arxiv.org/abs/2602.20917 | closes_strict_row=false; average large-modulus information is not a zero-exception rowwise psi lower bound |
| Milicevic-Qin-Wu bilinear Kloosterman | https://arxiv.org/abs/2511.07550 | closes_strict_row=false; the project still lacks an admissible signed Type-II/trace family |
| Pascadi composite-modulus Type-II Kloosterman | https://arxiv.org/abs/2511.08445 | closes_strict_row=false; coefficient family and return-to-row load are not constructed |
| Wright trilinear Kloosterman fractions | https://arxiv.org/abs/2604.25177 | closes_strict_row=false; requires a trilinear convolution with the paper's distribution hypotheses |

## 5. 最新开放口

```text
LPFPurePowerVonMangoldtCompressionClosed AND PrimePowerTailAbsorptionThresholdClosed AND PrimePowerTailSublinearThresholdClosed AND NeedPointwisePsiRowPositiveProportionAtSqrtScale AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_prime_power_tail_sublinear_threshold_audit.py` | `82128cd2600dfe024ac3b353ba660e70dc098fab1496d951e5c76e84f1113ad2` |
| `docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json` | `1e885c90848019792545d7e406ae517658a47e8f65b40a94a376b676956c7f5f` |
| `docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json` | `09d96abf6eb42659f55a40043b65eb521de0da1a706878bd169bde499488ac4f` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json` | `1e38c9ee2e7fd682eb787765eb9b5a7b9cf0b15992f1d013f75996bc01fe2bcf` |
| `docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json` | `975aa118af686bd729414f291af1efd9fa60082d622ac687d7f87772246acd6e` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `296457ce86c166f6f44ca8456c47bf6855f31a39440e04866b84ee084eefdaa5` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `0e9c5555a786c4194f6575a75904061cd44933480773e650c333e12bb5328ff2` |
| `docs/monograph/external-theorem-index.md` | `e72847eea37564fd8a8a19ddd196ea529ed0b9e4f9c537a0fc73dd137758b082` |
