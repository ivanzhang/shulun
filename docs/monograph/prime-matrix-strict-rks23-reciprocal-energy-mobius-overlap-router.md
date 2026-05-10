# Prime Matrix strict RKS2/RKS3 倒数能量 Möbius 重叠谱证书

**状态：** `reciprocal_interval_energy_rewritten_as_one_parameter_mobius_overlap_spectrum`

固定幂能量核心已改写成完全等价的一参数 Möbius 重叠谱问题：对每个和相位 `s`，解 `a^{-1}+b^{-1}=s` 得到 `b=a/(sa-1)`，因此 `E_+(J^{-1})=Σ_s |{a∈J: a/(sa-1)∈J}|^2`。下一真正最窄输入不是泛泛四元组能量，而是证明这些非仿射 Möbius 图不能在同一区间上形成高重叠 dyadic spectrum。

```text
mobius_overlap_identity_closed=true
dyadic_spectrum_criterion_closed=true
mobius_overlap_spectrum_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. Möbius 重叠等价式

| field | value |
| --- | --- |
| `pair_count` | r_J(s)=#{(a,b) in J^2: a^(-1)+b^(-1)=s} |
| `mobius_map` | phi_s(a)=a/(s*a-1), with s*a=1 giving no solution |
| `overlap_identity` | r_J(s)=#{a in J: phi_s(a) in J} |
| `energy_identity` | E_+(J^(-1))=sum_s r_J(s)^2 |
| `dyadic_spectrum` | Omega_tau={s: tau<=r_J(s)<2tau} |
| `sufficient_spectrum_bound` | for some delta>0, sum_tau \|Omega_tau\| tau^2 <= \|J\|^(3-delta) |
| `structural_reading` | many additive-energy quadruples mean many one-parameter Mobius maps repeatedly send J back into J |
| `next_attack_shape` | prove interval-overlap power saving for the non-affine family a -> a/(s*a-1) |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FixedPowerEnergyTargetActive` | `true` | `true` | 上一证书已把对数能量目标放松为固定幂节省能量目标。 | UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23 |
| `MobiusOverlapIdentityClosed` | `true` | `true` | `a^{-1}+b^{-1}=s` 等价于 `b=a/(sa-1)`，能量等于 Möbius 重叠平方和。 | OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving |
| `DyadicSpectrumCriterionClosed` | `true` | `true` | 固定幂能量节省等价于 dyadic overlap spectrum 的平方加权和节省。 | OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving |
| `IncidenceRouteStillMatches` | `true` | `true` | Rudnev/RNRS incidence 可以视作该 Möbius 图族的高重叠谱控制工具。 | RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving |
| `OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving` | `false` | `false` | 仓库内尚未证明一参数非仿射 Möbius 图族对区间的 dyadic overlap spectrum 有固定幂节省。 | RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是能量到 Möbius 重叠谱的等价改写，不是谱估计本身。 | OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving |

## 3. 下一最窄自足目标

```text
OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving
```
