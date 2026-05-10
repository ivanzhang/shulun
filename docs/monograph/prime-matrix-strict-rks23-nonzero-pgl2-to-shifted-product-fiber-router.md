# Prime Matrix strict RKS2/RKS3 非零 PGL2 到 shifted product fiber 证书

**状态：** `nonzero_pgl2_high_spectrum_rewritten_as_shifted_interval_modular_product_fiber_spectrum`

非零相位剩余继续算术化：对 `s!=0` 取 `c=s^{-1}`，`a^{-1}+b^{-1}=s` 精确等价于 shifted product fiber `(a-c)(b-c)=c^2 mod P`。因此当前最窄剩余不是一般 PGL2 语言，而是平方根颈部区间 `J` 上的 shifted modular hyperbola 纤维高谱。若能证明统一点态界 `r_c<=N^(1-eta)`，非零高谱会直接消失。

```text
shifted_product_fiber_identity_closed=true
shifted_product_fiber_high_spectrum_proved=false
uniform_shifted_product_fiber_pointwise_bound_proved=false
row_column_unconditional_closed=false
```

## 1. shifted product fiber 改写

| field | value |
| --- | --- |
| `nonzero_phase` | s != 0 |
| `change_of_variable` | c=s^(-1) |
| `original_equation` | a^(-1)+b^(-1)=s with a,b in J |
| `shifted_product_equation` | (a-c)(b-c)=c^2 mod P |
| `fiber_count` | r_J(s)=#{(a,b) in J^2: (a-c)(b-c)=c^2} |
| `high_spectrum_form` | control c with r_c>N^(1-eta), where c runs over F_P^* |
| `pointwise_sufficient_bound` | r_c<=N^(1-eta) for all c would kill the whole nonzero high spectrum |
| `if_pointwise_fails` | a failing c is a concrete shifted modular hyperbola with too many points in J x J |
| `remaining_tools` | finite-field incidence, modular hyperbola in shifted intervals, or PGL2 almost-stabilizer expansion |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NonzeroPGL2TargetActive` | `true` | `true` | 上一证书已吸收 `s=0`，剩余只含 `s!=0` 的非仿射 PGL2 高谱。 | NonzeroAffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23 |
| `ShiftedProductFiberIdentityClosed` | `true` | `true` | 对 `s!=0`，令 `c=s^{-1}`，高谱纤维等价于 shifted interval 模乘积方程。 | ShiftedIntervalModularProductFiberHighSpectrumPowerSavingForSquareRootCollar |
| `PointwiseFiberBoundWouldCloseSpectrum` | `true` | `true` | 若每个 shifted modular hyperbola 在 `J x J` 中只有 `N^(1-eta)` 个点，非零高谱立即为空。 | UniformShiftedIntervalModularProductFiberSublinearBound |
| `ShiftedIntervalModularProductFiberHighSpectrumPowerSavingForSquareRootCollar` | `false` | `false` | 仓库内尚未证明 shifted product fiber 的高谱固定幂节省。 | RudnevRNRSShiftedProductFiberIncidenceEstimate OR SelfContainedModularHyperbolaInShiftedIntervalsPointwiseBound |
| `UniformShiftedIntervalModularProductFiberSublinearBound` | `false` | `false` | 更强的点态纤维上界尚未证明；它是当前最直接的硬攻版本。 | SelfContainedModularHyperbolaInShiftedIntervalsPointwiseBound |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合等价变换，未证明 shifted product fiber 上界。 | ShiftedIntervalModularProductFiberHighSpectrumPowerSavingForSquareRootCollar |

## 3. 下一最窄自足目标

```text
ShiftedIntervalModularProductFiberHighSpectrumPowerSavingForSquareRootCollar
```
