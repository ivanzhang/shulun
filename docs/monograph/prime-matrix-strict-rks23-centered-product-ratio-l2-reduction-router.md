# Prime Matrix strict RKS2/RKS3 中心化乘积比值 L2 归约证书

**状态：** `centered_product_ratio_joint_correlation_reduced_to_product_ratio_l2_energy`

当前中心化相关没有换题：把已闭合的 `L(lambda)` 低二阶账本代入 Cauchy，可把剩余压成 `C_*^circ` 的二阶能量节省。该二阶能量又精确展开为八变量非零乘积比值能量 `(a1*b1)(a4*b4)=(a2*b2)(a3*b3)` 相对均匀项 `M_*^4/(P-1)` 的偏差。因此下一真正自足硬点是证明这个八变量乘积比值能量具有 Cauchy 所需的固定幂节省。

```text
interval_ratio_l2_ledger_imported=true
cauchy_reduction_to_product_ratio_l2_closed=true
centered_product_ratio_l2_identity_closed=true
eight_variable_product_ratio_energy_expansion_closed=true
centered_nonzero_product_ratio_l2_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. Cauchy/L2 门

| field | value |
| --- | --- |
| `current_correlation` | S=sum_{lambda in F_P^*} C_*^circ(-lambda)*L(lambda) |
| `known_l2_l` | sum_lambda L(lambda)^2 <= \|T\|^2 P^o(1) |
| `cauchy_bound` | \|S\| <= (sum_rho \|C_*^circ(rho)\|^2)^(1/2) * (sum_lambda L(lambda)^2)^(1/2) |
| `sufficient_input` | prove sum_rho \|C_*^circ(rho)\|^2 is below the Cauchy-required scale by a fixed power |
| `why_no_theorem_switch` | this is the same centered nonzero product-ratio correlation, with the already proved L2(L) ledger inserted |
| `limitation` | Cauchy is sufficient but may be stronger than direct joint nonconcentration |

## 2. 八变量能量展开

| field | value |
| --- | --- |
| `nonzero_measure` | mu_*(z)=#{(a,b): a*b=z, z!=0} |
| `ratio_spectrum` | C_*(rho)=sum_{z!=0} mu_*(z)*mu_*(rho*z) |
| `centered_spectrum` | C_*^circ(rho)=C_*(rho)-M_*^2/(P-1) |
| `centered_l2_identity` | sum_rho \|C_*^circ(rho)\|^2=sum_rho C_*(rho)^2-M_*^4/(P-1) |
| `raw_l2_count` | sum_rho C_*(rho)^2 |
| `eight_variable_count` | #{z1/z2=z3/z4: zi=a_i*b_i!=0, all variables in the root product boxes} |
| `multiplicative_equation` | (a1*b1)*(a4*b4)=(a2*b2)*(a3*b3) mod P |
| `uniform_term` | M_*^4/(P-1) |
| `needed_dispersion` | the eight-variable product-ratio energy must equal the uniform term plus a fixed-power-saving error |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CenteredJointTargetActive` | `true` | `true` | 上一证书已把剩余固定为 `sum C_*^circ(-lambda)L(lambda)` 的中心化相关。 | CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving |
| `IntervalRatioL2LedgerImported` | `true` | `true` | 短区间比值谱已有 `sum L(lambda)^2<=\|T\|^2 P^o(1)` 账本。 | ledger |
| `CauchyReductionToProductRatioL2Closed` | `true` | `true` | 由 Cauchy，证明 `C_*^circ` 的足够强 L2 节省即可推出当前相关节省。 | CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale |
| `CenteredProductRatioL2IdentityClosed` | `true` | `true` | `sum \|C_*^circ\|^2=sum C_*^2-M_*^4/(P-1)`，均匀项口径已固定。 | EightVariableNonzeroProductRatioEnergyDispersionPowerSaving |
| `EightVariableProductRatioEnergyExpansionClosed` | `true` | `true` | `sum C_*^2` 精确等于八变量非零乘积比值能量。 | EightVariableNonzeroProductRatioEnergyDispersionPowerSaving |
| `CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale` | `false` | `false` | 仓库内尚未证明该八变量乘积比值能量相对均匀项有固定幂节省。 | EightVariableNonzeroProductRatioEnergyDispersionPowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是 L2 归约和八变量展开，不是八变量能量节省本身。 | CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale |

## 4. 下一最窄自足目标

```text
CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale
```
