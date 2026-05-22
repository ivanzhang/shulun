# Prime Matrix Phi-LPF strict k top row perfect tiling 证书

**状态：** `strict_k_top_row_positive_reduced_to_excluding_perfect_lpf_tiling`

Phi-LPF 端点差分给出的顶行正性不是一个新的免费正项；它等价于排除 LPF 合数桶对 P-1 个顶行槽位的完美铺满。递推式只把铺满负载继续拆成有序粗因子树。经典连续乘积输入最多强制大素因子出现；在无素数顶行假设下，该大素因子会被 2<=m<P 的小载体承载，正好回到低载体 payment injection/positive rejection excess 接口。

## 1. 精确铺满等价

```text
T_P={P^2-P+a:1<=a<P}
N_top(P)=pi(P^2-1)-pi(P^2-P)
B_q(P)=Phi(floor((P^2-1)/q),q)-Phi(floor((P^2-P)/q),q)
N_top(P)=0 iff sum_{q<P} B_q(P)=P-1
N_top(P)>=1 iff sum_{q<P} B_q(P)<=P-2
```

因此，顶行正性 `N_top(P)>=1` 的最窄形式不是继续展开 Phi 递推，
而是证明 LPF 合数桶负载不可能达到完整槽位数 `P-1`。

## 2. 端点差分递推读法

```text
Delta_j(A,B)=Delta_{j+1}(A,B)+[Phi(floor(B/p_j),p_j)-Phi(floor(A/p_j),p_j)]
```

这只是把同一批合数槽位继续按下一个粗因子层拆开；它保持精确，
但自身不产生正性余量。若要推出正性，必须在某层证明至少一个槽位未被合数桶覆盖。

## 3. Sylvester-Schur 输入的实际落点

对 P-1 个连续顶行槽位，Sylvester-Schur 定理给出一个素因子 r>P。如果顶行没有素数槽，那么 r 必被某个 2<=m<P 的小载体承载，于是该输入变成 low-carrier payment，而不是直接矛盾。

也就是说，经典连续乘积定理能证明大素因子泄出，但不能证明顶行中有一个槽位本身为素数。
它把问题转回低载体高素数 payment injection，而不是直接给出矛盾。

## 4. 有限审计边界

```text
max_prime=5003
case_count=669
perfect_lpf_tiling_found_in_finite_sweep=false
all_top_rows_have_untiled_prime_slot_in_finite_sweep=true
minimum_untiled_prime_slots=1
maximum_composite_tiling_ratio=0.948495
finite_evidence_not_used_as_global_proof=true
```

最小未铺满素数槽样本：

| P | prime count |
| ---: | ---: |
| 3 | 1 |
| 5 | 1 |
| 11 | 1 |

最高合数铺满比例样本：

| P | composite load | slot count | ratio | prime count |
| ---: | ---: | ---: | ---: | ---: |
| 4253 | 4033 | 4252 | 0.948495 | 219 |

## 5. 样本铺满表

### P=5

```text
interval=[21, 24]
slot_count=4
prime_count=1
composite_lpf_tiling_load=3
perfect_lpf_tiling=false
identity_slot_count_equals_prime_plus_composite=true
prime_slots_sample=[23]
```

| LPF bucket | count |
| ---: | ---: |
| 2 | 2 |
| 3 | 1 |

### P=11

```text
interval=[111, 120]
slot_count=10
prime_count=1
composite_lpf_tiling_load=9
perfect_lpf_tiling=false
identity_slot_count_equals_prime_plus_composite=true
prime_slots_sample=[113]
```

| LPF bucket | count |
| ---: | ---: |
| 2 | 5 |
| 3 | 2 |
| 5 | 1 |
| 7 | 1 |

### P=17

```text
interval=[273, 288]
slot_count=16
prime_count=3
composite_lpf_tiling_load=13
perfect_lpf_tiling=false
identity_slot_count_equals_prime_plus_composite=true
prime_slots_sample=[277, 281, 283]
```

| LPF bucket | count |
| ---: | ---: |
| 2 | 8 |
| 3 | 3 |
| 5 | 1 |
| 7 | 1 |

### P=101

```text
interval=[10101, 10200]
slot_count=100
prime_count=12
composite_lpf_tiling_load=88
perfect_lpf_tiling=false
identity_slot_count_equals_prime_plus_composite=true
prime_slots_sample=[10103, 10111, 10133, 10139, 10141, 10151, 10159, 10163, 10169, 10177, 10181, 10193]
```

| LPF bucket | count |
| ---: | ---: |
| 2 | 50 |
| 3 | 17 |
| 5 | 7 |
| 7 | 4 |
| 11 | 2 |
| 13 | 1 |
| 17 | 1 |
| 23 | 1 |
| 29 | 1 |
| 53 | 1 |
| 61 | 1 |
| 67 | 1 |
| 73 | 1 |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TopRowPerfectTilingEquivalenceClosed` | `true` | `true` | N_top(P)=0 等价于所有 P-1 个顶行内部槽位被 LPF 合数桶精确铺满。 | exclude perfect LPF tiling |
| `DeltaPhiLocalRecursionClosed` | `true` | `true` | 端点差分版 Phi 递推只把每个桶继续拆成较深的有序粗因子树。 | recursion enumerates load, does not create sign |
| `SylvesterSchurOnlyRoutesToLowCarrierPayment` | `true` | `true` | 连续乘积定理只强制出现大素因子；若顶行无素数，该大素因子必被小载体承载。 | low-carrier high-prime payment injection |
| `PerfectTilingExcludedGlobally` | `false` | `false` | 当前语料没有无条件排除所有素数 P 的顶行 LPF 完美铺满。 | PrimeSquareUpperCollarPrimeInput or PositiveRejectionExcess |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把正性硬点改写成 perfect-tiling 排除问题。 | strict row positivity still open |

## 7. 结论

顶行 square-collar 的正性现在被压成一个非常明确的全局排除命题：
`sum_{q<P} B_q(P)=P-1` 的 perfect LPF tiling 不能发生。
当前语料尚无该排除的无条件证明；剩余出口仍是
`PrimeSquareUpperCollarPrimeInput`、`SqrtGapInputAfterX` 或
`PositiveRejectionExcessForStrictKRawLPFIncidence`。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_top_row_perfect_tiling_router.py` | `03f51862bbf01fcfb1145494795ff78fe6a3173a9edcabed886b51a0d6bace93` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json` | `d1a4c61c54b866038f6263dd795dad16f3d486faf53a9fcbaa45e0ae2228f058` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json` | `f825d0e5df9740a53392e3dc0821ca50208291280e33fe9e9ab04e878a70ab3b` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
