# Prime Matrix Phi-LPF theta short-interval zero-density band 路由

**状态：** `fixed_theta_gt_half_short_intervals_close_only_zero_density_low_rows`
**核验日期：** `2026-05-26`

## 1. 一般嵌入律

对 strict row 取右端点短区间：

```text
I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P
X=(k+1)P and X^theta<P
k+1 < P^((1-theta)/theta), constants only change prefactors
for every fixed theta>1/2, P^((1-theta)/theta)/(P-1)->0
```

核心判定：

```text
all_fixed_theta_gt_half_close_only_zero_density_low_rows=true
theta_half_identified_as_short_interval_lane_threshold=true
density_one_top_band_remains_for_all_fixed_theta_gt_half=true
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 2. theta 对照表

| input | theta | covered exponent | zero-density low rows | source |
| --- | ---: | ---: | --- | --- |
| Baker-Harman-Pintz 2001 | 21/40 | 19/21 | true | classical pointwise short-interval exponent 0.525 |
| Runbo Li arXiv:2308.04458 v8 | 13/25 | 12/13 | true | https://arxiv.org/abs/2308.04458 |
| Guth-Maynard/Hieu scale representative | 17/30 | 13/17 | true | zero-density/AP short-interval PNT scale, still above 1/2 |
| Hypothetical theta=0.5001 | 5001/10000 | 4999/5001 | true | near-half fixed exponent stress test |

## 3. 尺度样本

| input | P | covered rows approx | covered fraction | top-band fraction |
| --- | ---: | ---: | ---: | ---: |
| Baker-Harman-Pintz 2001 | 1000000 | 268269.580 | 0.268269580 | 0.731730420 |
| Baker-Harman-Pintz 2001 | 1000000000000 | 71968567300.115 | 0.071968567 | 0.928031433 |
| Baker-Harman-Pintz 2001 | 1000000000000000000000000 | 5179474679231212945408.000 | 0.005179475 | 0.994820525 |
| Runbo Li arXiv:2308.04458 v8 | 1000000 | 345510.729 | 0.345510729 | 0.654489271 |
| Runbo Li arXiv:2308.04458 v8 | 1000000000000 | 119377664171.444 | 0.119377664 | 0.880622336 |
| Runbo Li arXiv:2308.04458 v8 | 1000000000000000000000000 | 14251026703030020997120.000 | 0.014251027 | 0.985748973 |
| Guth-Maynard/Hieu scale representative | 1000000 | 38746.751 | 0.038746751 | 0.961253249 |
| Guth-Maynard/Hieu scale representative | 1000000000000 | 1501310728.908 | 0.001501311 | 0.998498689 |
| Guth-Maynard/Hieu scale representative | 1000000000000000000000000 | 2253933904734784256.000 | 0.000002254 | 0.999997746 |
| Hypothetical theta=0.5001 | 1000000 | 994490.136 | 0.994490136 | 0.005509864 |
| Hypothetical theta=0.5001 | 1000000000000 | 989010630771.391 | 0.989010631 | 0.010989369 |
| Hypothetical theta=0.5001 | 1000000000000000000000000 | 978142027778824108769280.000 | 0.978142028 | 0.021857972 |

## 4. 最新开放口

```text
AllFixedThetaGreaterThanHalfShortIntervalInputsCloseOnlyZeroDensityLowRows AND DensityOneTopBandStillRequiresThetaHalfPointwisePsiOrStructuralParityBreak AND PrimePowerTailSublinearThresholdClosed AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_theta_short_interval_zero_density_band_router.py` | `ad8fc1a8191958faaab30dc92390d9577370df8dcac14db26f3dffa7eb8420c3` |
| `docs/monograph/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.json` | `03e3d0030f018ff25fab2cbb7c3aa1f15ec6f6aaa37c347e7ea7980f57302589` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json` | `9c8b4ae328fe2254bf81e16e4f058921efc6c3ea616a97f196a42482151dd028` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `5fc519f30a3992ecda8eda481ea128491fbb146253ae481a574bff119d2409f4` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `55b9bbfb44c1c29800dd5581e66d504fa910f790d0e45eb85251e9db45599660` |
| `docs/monograph/external-theorem-index.md` | `67e5172450a1dbc46eeee90e48e9757cdfb838569293248a674b09073d010687` |
