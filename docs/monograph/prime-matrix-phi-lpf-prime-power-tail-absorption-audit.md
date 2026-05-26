# Prime Matrix Phi-LPF prime-power tail absorption 审计

**状态：** `prime_power_tail_absorption_threshold_reduces_theta_to_pointwise_psi`
**核验日期：** `2026-05-26`

## 1. 严格分解

对 strict row

```text
I_{P,k}=(kP,(k+1)P), integers kP<n<(k+1)P
```

有精确分解：

```text
psi(I_{P,k})=theta(I_{P,k})+sum_{p^a in I_{P,k}, a>=2} log p
```

因此素数存在性可改写为素幂尾巴吸收阈值：

```text
theta(I_{P,k})>0 iff psi(I_{P,k})>prime_power_tail(I_{P,k})
```

尾巴有确定性整数根上界：

```text
prime_power_tail(I_{P,k}) <= log(P) * sum_{a>=2} (floor(((k+1)P-1)^(1/a))-floor((kP)^(1/a)))
```

## 2. 全局读数

```text
psi_theta_tail_identity_all_samples=true
prime_power_tail_bound_all_samples=true
psi_tail_absorption_equivalent_to_prime_presence_all_samples=true
prime_power_tail_absorption_threshold_closed=true
pointwise_psi_row_lower_bound_beyond_tail_proved=false
pointwise_theta_ap_lower_bound_proved=false
admissible_signed_typeii_or_trace_family_constructed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

| P | rows | rows with prime | empty rows | max tail row k | max tail mass | max tail bound | min positive theta row k |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 30 | 30 | 0 | 11 | 4.890349 | 17.169936 | 25 |
| 101 | 100 | 100 | 0 | 21 | 7.513709 | 32.305844 | 73 |
| 251 | 250 | 250 | 0 | 1 | 8.416710 | 55.254529 | 108 |
| 1009 | 1008 | 1008 | 0 | 1 | 14.176733 | 124.500870 | 905 |

## 3. 最大样本尾巴行

`P=1009` 的最大素幂尾巴出现在 `k=1`：

```text
integer_interval=[1010, 2017]
prime_count=137
theta_mass=999.495375
prime_power_tail_count=5
prime_power_tail_mass=14.176733
psi_mass=1013.672108
tail_bound_logP=124.500870
tail_items_sample=1024=2^10, 1331=11^3, 1369=37^2, 1681=41^2, 1849=43^2
```

## 4. 最新开放口

```text
LPFPurePowerVonMangoldtCompressionClosed AND PrimePowerTailAbsorptionThresholdClosed AND NeedPointwisePsiRowLowerBoundBeyondPrimePowerTail AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_prime_power_tail_absorption_audit.py` | `61c308749fce12c7400d9fe3b3d2ed863bf60bc50cf21334d0c890ed6b80b446` |
| `docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json` | `09d96abf6eb42659f55a40043b65eb521de0da1a706878bd169bde499488ac4f` |
| `docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json` | `f745ed6c597dfcceed10f50249df139235cac727fd8086737b81bb894bda3a4c` |
| `docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json` | `92468974eceab624e5a553bb3a24e20a85b9e3f5424b674bb9f00057a53ccfc5` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `b09da8a0889ca1973f35e9311c14e456d24b0a0ac0ba74d41c5203c78a3b75e8` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `da6fec5dfdfafb4df075c42804e9c58c255e17e19ca5dc01be775a5b90a48ebd` |
| `docs/monograph/external-theorem-index.md` | `5322981bfcd77ef9d016809a2e6f742e82da6cec9118806e2be5bd981528c501` |
