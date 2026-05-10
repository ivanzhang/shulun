# Prime Matrix strict RKS2/RKS3 非零乘积比值谱中心化证书

**状态：** `nonzero_product_ratio_spectrum_centered_on_fstar_joint_saving_remains`

扣除零乘积同步对角层以后，非零乘积谱必须在 `F_P^*` 上重新中心化。令 `M_*=|Delta|^2-W0`，则正确均匀基线是 `M_*^2/(P-1)`，剩余相关精确写成 `sum_lambda C_*^circ(-lambda)L(lambda)`。这一步闭合了主项口径和非零核心的中心化接口；真正剩余变成证明该中心化乘积比值谱不会与短区间比值谱同位集中。

```text
nonzero_mass_ledger_closed=true
fstar_uniform_baseline_closed=true
centered_nonzero_product_ratio_correlation_identity_closed=true
centered_nonzero_product_ratio_joint_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. F_P^* 中心化账本

| field | value |
| --- | --- |
| `nonzero_measure` | mu_*(z)=#{(a,b): a*b=z, z!=0, with root-box/parity restrictions} |
| `nonzero_mass` | M_* = sum_{z!=0} mu_*(z)=\|Delta\|^2-W0 |
| `product_ratio_spectrum` | C_*(rho)=sum_{z!=0} mu_*(z)*mu_*(rho*z), rho in F_P^* |
| `first_moment` | sum_{rho in F_P^*} C_*(rho)=M_*^2 |
| `fstar_uniform_baseline` | C_unif=M_*^2/(P-1) |
| `centered_product_ratio_spectrum` | C_*^circ(rho)=C_*(rho)-M_*^2/(P-1) |
| `interval_ratio_spectrum` | L(lambda)=#{(x,u) in T^2: u=lambda*x} |
| `diagonal_main_subtracted_correlation` | sum_lambda C_*^circ(-lambda)*L(lambda) |
| `why_p_minus_1` | after zero-product peeling the support is F_P^*, so the correct uniform denominator is P-1 |
| `scale_audit` | plain first moment and L2(L) do not imply fixed power saving for the centered correlation |

## 2. 展开后的真正核心

| field | value |
| --- | --- |
| `four_box_ratio_equation` | a1*b1 = rho*a2*b2 mod P with all products nonzero |
| `six_variable_joint_equation` | u*a1*b1+x*a2*b2=0 mod P after setting rho=-u/x |
| `centered_failure_packet` | if the target fails, a dyadic set of interval ratios carries large C_*^circ mass |
| `sufficient_but_unproved_l2_route` | sum_{rho} \|C_*^circ(rho)\|^2 with fixed power saving would close by Cauchy and the existing L2(L) ledger |
| `direct_route` | prove joint nonconcentration of C_*^circ and L without requiring a global C_*^circ L2 theorem |
| `remaining_obstruction` | high product-ratio fibers may align with short interval ratios; this alignment is not ruled out by current ledgers |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DiagonalMainSubtractedTargetActive` | `true` | `true` | 上一证书已把零乘积同步对角层剥离，当前只剩非零乘积比值相关。 | DiagonalMainSubtractedNonzeroProductRatioSpectrumJointPowerSaving |
| `NonzeroMassLedgerClosed` | `true` | `true` | 非零质量为 `M_*=\|Delta\|^2-W0`，零层不会再混入非零谱。 | ledger |
| `FStarUniformBaselineClosed` | `true` | `true` | 非零谱定义在 `F_P^*`，均匀主项必须是 `M_*^2/(P-1)`。 | ledger |
| `CenteredNonzeroProductRatioCorrelationIdentityClosed` | `true` | `true` | 扣除对角主项和 `F_P^*` 均匀项后，剩余精确为 `sum C_*^circ(-lambda)L(lambda)`。 | CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving |
| `ExistingMarginalsDoNotCloseCenteredJointSaving` | `true` | `true` | 现有一阶账本与 `L` 的低二阶账本仍只到自然尺度，不能自动给固定幂节省。 | CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving |
| `CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving` | `false` | `false` | 仓库内尚未证明中心化非零乘积比值谱不能同位集中到短区间比值谱上。 | NonzeroFourBoxProductRatioCenteredL2OrJointNonconcentration |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是非零谱中心化和主项口径，不是最终联合节省。 | CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving |

## 4. 下一最窄自足目标

```text
CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving
```
