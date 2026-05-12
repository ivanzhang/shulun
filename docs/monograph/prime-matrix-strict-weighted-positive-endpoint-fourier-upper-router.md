# Prime Matrix strict 正权端点 Fourier 上界分裂路由器

**状态：** `weighted_positive_endpoint_fourier_upper_split_to_low_effective_decay_bohrcap_open`

正权端点 PDEC 的 Fourier 上界被压成三部分：低有效模共振、非共振几何衰减、以及衰减失败后的 Bohr-cap 大谱。端点弧单模 Fourier 系数由几何级数严格控制；若一个全局频率在许多 d 上同时低有效分母共振，则这本身就是 LowEffectiveMod PDEC/ColumnCRT。若没有低有效模共振，则需用几何衰减和正权支撑预算给出上界；预算失败则回流 Bohr-cap/PDEC/ColumnCRT。当前仍未排斥这些出口。

```text
fourier_coefficient_formula_closed=true
low_effective_mod_route_closed=true
large_effective_mod_decay_template_closed=true
bohrcap_large_spectrum_route_registered=true
weighted_positive_endpoint_fourier_upper_bound_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. Fourier 上界三分

单个模数 `d` 的端点弧函数有标准几何级数界。全局频率 `h` 对 `d` 的有效残基为

```text
r_h(d)=h P^{-1} mod d.
```

若 `r_h(d)` 在很多 `d` 上有小有效分母，就是低有效模 PDEC/ColumnCRT；否则端点弧系数按有效分母衰减。

## 2. 分裂表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `single_mod_endpoint_coefficient` | \|hat phi_d(r)\| <= min(H/d, 1/(2d\|\|r/d\|\|)) for r not 0 mod d. | `closed_classical` | 端点弧的非零 Fourier 系数由几何级数精确控制。 |
| `lifted_frequency_support` | A global frequency h only sees d through r_h(d)=h P^{-1} mod d. | `closed` | 大系数要求 h 与许多 d 同时低有效分母共振。 |
| `low_effective_mod_split` | If many active d have small d/gcd(r_h(d),d), then the frequency is a low-effective-mod PDEC/ColumnCRT. | `closed_route` | 低有效模大谱不是随机误差，而是命名相位缺陷。 |
| `large_effective_mod_decay` | On d/gcd(r_h(d),d)>R, each active d contributes O(w_d^+/R) after endpoint centering. | `closed_template` | 远离共振的频率可由几何衰减和权重 l1/l2 预算控制。 |
| `bohrcap_large_spectrum_route` | If high frequencies still exceed the decay budget, active d lie in a Bohr-cap large spectrum set. | `registered_route` | 这接入既有 Bohr-cap/PDEC/ColumnCRT 分支。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的正权亏损 PDEC 内部。 | 保持 row_column_unconditional_closed=false。 |
| `FourierCoefficientFormulaClosed` | `true` | `true` | 端点弧 Fourier 系数由有限几何级数给出。 | WeightedPositiveEndpointFourierPDECUpperBound |
| `LowEffectiveModRouteClosed` | `true` | `false` | 低有效模大谱已命名为 PDEC/ColumnCRT，但尚未排斥。 | LowEffectiveModEndpointPDECOrColumnCRT |
| `LargeEffectiveModDecayTemplateClosed` | `true` | `false` | 非共振部分有几何衰减模板，但还需要正权支撑的 l1/l2/复杂度预算。 | EndpointArcGeometricDecayLargeEffectiveModBudget |
| `LargeSpectrumFallbackRegistered` | `true` | `false` | 若衰减预算失败，回流 Bohr-cap/PDEC/ColumnCRT。 | PositiveWeightSupportLargeSpectrumBohrCapExclusion |
| `WeightedPositiveEndpointFourierUpperCurrentCorpusProved` | `false` | `false` | 三出口尚未全部排斥，也未给出统一数值预算。 | LowEffectiveModEndpointPDECOrColumnCRT AND EndpointArcGeometricDecayLargeEffectiveModBudget AND PositiveWeightSupportLargeSpectrumBohrCapExclusion AND DeficitPersistenceOrSAEClassification |

## 4. 最新最窄输入

```text
LowEffectiveModEndpointPDECOrColumnCRT
```

并行保留：

```text
EndpointArcGeometricDecayLargeEffectiveModBudget AND PositiveWeightSupportLargeSpectrumBohrCapExclusion AND DeficitPersistenceOrSAEClassification
```

审稿边界：本步只把 Fourier 上界拆成可攻的三出口；没有证明三出口都被排斥。
