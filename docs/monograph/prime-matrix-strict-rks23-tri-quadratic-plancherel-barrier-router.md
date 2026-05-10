# Prime Matrix strict RKS2/RKS3 三短二次 Plancherel 边界证书

**状态：** `tri_quadratic_fourier_packet_reduced_to_correlated_energy_overlap_saving_beyond_plancherel`

三短二次 Fourier 包经固定斜率 Cauchy/Plancherel 后，精确压成 `sum_lambda sqrt(M_A(lambda)L(lambda))` 的相关节省问题。这里 `M_A(lambda)` 是短二次和 `A` 的乘法自相关能量，`L(lambda)` 是根盒斜率重叠。普通 Plancherel 只给 `|Dev|<=P^(1/2)N^2=N^3 log^O(P)`，正好卡在自然三次尺度，不能给固定幂节省。因此当前唯一剩余是证明 `M_A(lambda)` 不能集中在大重叠斜率上。

```text
per_slope_cauchy_plancherel_envelope_closed=true
natural_scale_barrier_quantified=true
correlated_energy_overlap_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. Plancherel 后剩余

| field | value |
| --- | --- |
| `quadratic_sum` | A(s)=sum_{d in Delta} e_P(s*d^2) |
| `slope_overlap` | L(lambda)=\|X_lambda\| with X_lambda=T cap lambda^(-1)T |
| `energy_autocorrelation` | M_A(lambda)=sum_{r!=0}\|A(r)\|^2\|A(r*lambda)\|^2 |
| `per_slope_cauchy` | \|packet_lambda\|/P <= P^(-1/2)*sqrt(M_A(lambda)*L(lambda)) |
| `plancherel_inputs` | sum_s \|A(s)\|^2 <= 2P\|Delta\| and sum_h \|B_lambda(h)\|^2 <= 2P L(lambda) |
| `global_l2_sums` | sum_lambda M_A(lambda) <= (sum_s \|A(s)\|^2)^2 and sum_lambda L(lambda)=\|T\|^2 |
| `natural_bound` | \|Dev\| <= P^(1/2) N^2 = N^3 log^O(P) in the square-root collar |
| `barrier` | Cauchy/Plancherel reaches the natural cubic scale but gives no fixed power saving |
| `needed_saving` | sum_lambda sqrt(M_A(lambda)L(lambda)) <= P*N^2*N^(-delta) for some fixed delta>0 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TriQuadraticFourierTargetActive` | `true` | `true` | 上一证书已把剩余压成三短二次 Fourier 相关包。 | TriShortQuadraticFourierCorrelationPowerSaving |
| `PerSlopeCauchyPlancherelEnvelopeClosed` | `true` | `true` | 对固定斜率，Cauchy 与 Plancherel 给出 `P^{-1/2}sqrt(M_A(lambda)L(lambda))` 包络。 | CorrelatedQuadraticFourierEnergyOverlapPowerSaving |
| `NaturalScaleBarrierQuantified` | `true` | `true` | 全局 L2 只能推出 `N^3 log^O(P)` 自然尺度，不能给固定幂节省。 | CorrelatedQuadraticFourierEnergyOverlapPowerSaving |
| `PlainPlancherelRouteInsufficient` | `true` | `true` | 若不证明 `M_A(lambda)` 与 `L(lambda)` 的相关节省，链条不能闭合。 | CorrelatedQuadraticFourierEnergyOverlapPowerSaving |
| `CorrelatedQuadraticFourierEnergyOverlapPowerSaving` | `false` | `false` | 仓库内尚未证明二次 Fourier 能量自相关与斜率重叠之间有固定幂相关节省。 | BeyondPlancherelSlopeOverlapQuadraticEnergySaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只定位 Plancherel 后的唯一缺口，未证明相关节省。 | CorrelatedQuadraticFourierEnergyOverlapPowerSaving |

## 3. 下一最窄自足目标

```text
CorrelatedQuadraticFourierEnergyOverlapPowerSaving
```
