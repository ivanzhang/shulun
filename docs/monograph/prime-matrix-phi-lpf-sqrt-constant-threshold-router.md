# Prime Matrix Phi-LPF sqrt constant threshold 路由

**状态：** `sqrt_scale_constant_one_is_sharp_for_strict_rows`
**核验日期：** `2026-05-26`

## 1. 平方根常数门槛

```text
I_{P,k}=(kP,(k+1)P), 1<=k<P
x=kP and (x, x+C*sqrt(x)] lies in row if C^2*k<=P
X=(k+1)P and [X-C*sqrt(X), X] lies in row if C^2*(k+1)<=P
Equality at C=1 is harmless because kP and (k+1)P are composite row endpoints.
C<=1 would close all sufficiently large strict rows; every fixed C>1 leaves top-band density 1-1/C^2.
```

核心判定：

```text
sqrt_constant_one_pointwise_input_would_close_all_strict_rows=true
fixed_constant_greater_than_one_leaves_positive_density_top_band=true
known_unconditional_C_at_most_one_pointwise_input_available=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 2. 常数对照表

| input | C^2 | closes all if input available | top-band density | meaning |
| --- | ---: | --- | ---: | --- |
| C=1/2 | 1/4 | true | 0.000000000 | stronger than the sharp square-root row length |
| C=1 | 1/1 | true | 0.000000000 | sharp aligned square-root threshold |
| C=1.0001 | 100020001/100000000 | false | 0.000199970 | near-sharp but still larger than one |
| C=sqrt(2) | 2/1 | false | 0.500000000 | fixed constant above one |
| C=2 | 4/1 | false | 0.750000000 | wide square-root input with constant loss |

## 3. 尺度样本

| input | P | left closed fraction | right closed fraction | right top-band fraction |
| --- | ---: | ---: | ---: | ---: |
| C=1/2 | 1000003 | 1.000000000 | 1.000000000 | 0.000000000 |
| C=1/2 | 1000000000039 | 1.000000000 | 1.000000000 | 0.000000000 |
| C=1/2 | 1000000000000000000000039 | 1.000000000 | 1.000000000 | 0.000000000 |
| C=1 | 1000003 | 1.000000000 | 1.000000000 | 0.000000000 |
| C=1 | 1000000000039 | 1.000000000 | 1.000000000 | 0.000000000 |
| C=1 | 1000000000000000000000039 | 1.000000000 | 1.000000000 | 0.000000000 |
| C=1.0001 | 1000003 | 0.999801000 | 0.999800000 | 0.000200000 |
| C=1.0001 | 1000000000039 | 0.999800030 | 0.999800030 | 0.000199970 |
| C=1.0001 | 1000000000000000000000039 | 0.999800030 | 0.999800030 | 0.000199970 |
| C=sqrt(2) | 1000003 | 0.500000000 | 0.499999000 | 0.500001000 |
| C=sqrt(2) | 1000000000039 | 0.500000000 | 0.500000000 | 0.500000000 |
| C=sqrt(2) | 1000000000000000000000039 | 0.500000000 | 0.500000000 | 0.500000000 |
| C=2 | 1000003 | 0.249999500 | 0.249998500 | 0.750001500 |
| C=2 | 1000000000039 | 0.250000000 | 0.250000000 | 0.750000000 |
| C=2 | 1000000000000000000000039 | 0.250000000 | 0.250000000 | 0.750000000 |

## 4. 最新开放口

```text
SqrtScaleConstantAtMostOnePointwiseInputWouldCloseStrictRows AND AnyFixedSqrtConstantGreaterThanOneLeavesPositiveDensityTopBand AND PrimePowerTailSublinearThresholdClosed AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_sqrt_constant_threshold_router.py` | `1046a4360b3249fec6292f3cc3021b4159a2a65ad9f1e3cb165d9eb5d19c3f2a` |
| `docs/monograph/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.json` | `33ae5e4a006144f31f60066292586d3fe6da1ff13fe69a3d8dd2011920000978` |
| `docs/monograph/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.json` | `03e3d0030f018ff25fab2cbb7c3aa1f15ec6f6aaa37c347e7ea7980f57302589` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json` | `f825d0e5df9740a53392e3dc0821ca50208291280e33fe9e9ab04e878a70ab3b` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `7c207246b141a88abc5c0074c72d4bb3aa63c01d10c83bed6a2bc7e0a5f8d8e1` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `932824455cea45b45f147f5be739d81f62d4f930082aea00abc6c60885a965e0` |
| `docs/monograph/external-theorem-index.md` | `4b3e8e4309a99c4e12a7c708784a134f630798837fe4c6076841b812efb3d3f3` |
