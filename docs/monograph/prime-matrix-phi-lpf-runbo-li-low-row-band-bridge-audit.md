# Prime Matrix Phi-LPF Runbo Li low-row band bridge 审计

**状态：** `runbo_li_short_interval_closes_low_row_band_but_not_top_band`
**核验日期：** `2026-05-26`

## 1. 外部定理嵌入

使用外部输入：

```text
name=Runbo Li primes in short intervals
source=https://arxiv.org/abs/2308.04458
exponent=13/25 = 0.52
form_used=for sufficiently large X, (X-X^(13/25), X] contains a prime
```

对 strict row 取右端点：

```text
I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P
X=(k+1)P
X^(13/25)<P iff (k+1)^13<P^12
```

因此低行带无条件外部闭合为：

```text
1<=k<=P^(12/13)-1, up to integer floor
```

但剩余 top band 为：

```text
k+1>=P^(12/13)
```

## 2. 样本审计

```text
runbo_li_low_row_band_closed=true
top_band_sqrt_scale_gap_remains=true
closes_all_strict_rows=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| P | rows | Li-closed k max | closed rows | closed fraction | top-band rows | next uncovered k |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 30 | 22 | 22 | 0.733333 | 8 | 23 |
| 101 | 100 | 69 | 69 | 0.690000 | 31 | 70 |
| 251 | 250 | 163 | 163 | 0.652000 | 87 | 164 |
| 1009 | 1008 | 591 | 591 | 0.586310 | 417 | 592 |
| 3001 | 3000 | 1620 | 1620 | 0.540000 | 1380 | 1621 |
| 10007 | 10006 | 4926 | 4926 | 0.492305 | 5080 | 4927 |
| 100003 | 100002 | 41246 | 41246 | 0.412452 | 58756 | 41247 |
| 1000003 | 1000002 | 345510 | 345510 | 0.345509 | 654492 | 345511 |

## 3. 渐近占比

| P | approx closed rows | approx closed fraction | approx top-band fraction |
| ---: | ---: | ---: | ---: |
| 1000 | 587.802 | 0.587801607 | 0.412198393 |
| 1000000 | 345510.729 | 0.345510729 | 0.654489271 |
| 1000000000 | 203091762.090 | 0.203091762 | 0.796908238 |
| 1000000000000 | 119377664171.444 | 0.119377664 | 0.880622336 |
| 1000000000000000000 | 41246263829013608.000 | 0.041246264 | 0.958753736 |

## 4. 最新开放口

```text
RunboLiLowRowBandClosedForKPlusOneLessThanPTo12Over13 AND TopBandKPlusOneAtLeastPTo12Over13StillRequiresSqrtScalePointwisePsi AND PrimePowerTailSublinearThresholdClosed AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_runbo_li_low_row_band_bridge_audit.py` | `b7ccff0fac45bcfd36d50777d2592c8afa5ef5344a06997f70a5bb3ebc7f4e47` |
| `docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json` | `22fec026bad79e0d8ec10bff215385c10fdee931213702bd67e4cebea47ec238` |
| `docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json` | `1e885c90848019792545d7e406ae517658a47e8f65b40a94a376b676956c7f5f` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `7f8914fce5f6eb059b0334ace59c163d964f6f16839d6ed3557cfea45625e741` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `910b07ccd3f299c985e6e72ce561206bdc25bafa157680e9831d1c0c411763a8` |
| `docs/monograph/external-theorem-index.md` | `0ae4594ba7b4c761c5cee883dfa04cf160d8147783805ca02fa6da424469f924` |
