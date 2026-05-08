# Prime Matrix beta-sieve 99% 主系数终端攻击路由器

**状态：** `main_coefficient_reduced_to_continuous_and_discrete_error_inputs_open`

本步直接攻击 99% 主系数终端。具体 B=3 word rule 的精确 checkpoint 审计非常强：P=100000 处 W^-/Vf≈1.694，审计到 10^7 的最小比值仍约 1.553。但这仍不能作为 P>=100000 全尾段证明。诚实的最窄闭合条件已经压成两个微输入：连续 beta 主项余量，以及离散素和到连续模型的统一误差账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
lower_weight_recursive_construction_closed=true
lower_weight_dominance_proved=true
beta_sieve_main_coefficient_atom_reduced=true
beta_sieve_main_coefficient_99pct_proved=false
standard_beta_sieve_import_accepted=false
external_short_interval_rough_lower_bound_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 精确 checkpoint 审计

这些数值只证明有限点通过，不替代全尾段证明。

| P | pi(z) | W^- | V(z)f(s) | ratio | ratio-0.99 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 100000 | 34 | 0.081446823200 | 0.048078387419 | 1.694042 | 0.704042 |
| 200000 | 42 | 0.077550615415 | 0.045785384931 | 1.693785 | 0.703785 |
| 500000 | 60 | 0.069867790983 | 0.042368382334 | 1.649055 | 0.659055 |
| 1000000 | 75 | 0.066199482276 | 0.040494518370 | 1.634776 | 0.644776 |
| 2000000 | 97 | 0.061653832838 | 0.038533344714 | 1.600012 | 0.610012 |
| 5000000 | 134 | 0.057294459027 | 0.036339905989 | 1.576627 | 0.586627 |
| 10000000 | 172 | 0.054062457487 | 0.034816654207 | 1.552776 | 0.562776 |

## 2. 审计结论

```text
all_checkpoints_pass_99pct=true
min_checkpoint_P=10000000
min_checkpoint_ratio=1.552775782694
sample_only_not_tail_proof=true
```

checkpoint exact computation gives strong positive evidence, but a finite set of P-values cannot imply the uniform all-P>=100000 inequality. The missing self-contained tail proof is exactly continuous beta coefficient surplus plus explicit discrete prime-sum error.

## 3. 替换

```text
BetaSieveMainCoefficientExplicit99PercentPGe100000
  =>
(B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000)
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MainCoefficientGateActive | `true` | `false` | 最新内部唯一点是 B=3 lower word rule 的 99% 主系数尾段证明。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内处理筛主项，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| LowerPackageAvailable | `true` | `true` | 递归构造和逐点 lower-bound 支配已经闭合，主系数对象现在良定义。 | 无 lower-weight 结构剩余。 |
| ExactCoefficientFunctionalPinned | `true` | `true` | 主系数精确定义为 W^-(P)=sum lambda_d^-/d，并以精确 V(z)f(1/0.43) 归一。 | 无归一化自由度。 |
| FiniteCheckpointAuditStrongPositive | `true` | `false` | P=1e5 到 1e7 的 checkpoint 精确审计全部大幅超过 99%，最小比值仍超过 1.55。 | 样本不是全尾段证明。 |
| SampleToTailPromotionBlocked | `true` | `true` | 有限 checkpoint 不能推出 P>=100000 全部整数尾段；还需连续主项和离散误差的统一控制。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000 |
| MainCoefficientAtomReducedToTwoMicroInputs | `true` | `false` | 99% 主系数原子被压成两个最小自足输入：连续 beta 主项余量与离散素和误差账本。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000 |
| B3ContinuousBetaSieveCoefficientSurplusAlpha043 | `false` | `false` | 需要证明 B=3 word rule 在 s=1/0.43 的连续 Buchstab/beta 主系数至少达到 0.99 f(s)，最好给出显式正余量。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043 |
| B3DiscretePrimeSumUniformErrorPGe100000 | `false` | `false` | 需要证明 P>=100000 下离散素数乘积和到连续积分模型的误差小于连续余量。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 若接受标准 Rosser-Iwaniec beta-sieve 定理，可外部关闭主系数；但这不是内部自足闭合。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (((B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

先攻 `B3ContinuousBetaSieveCoefficientSurplusAlpha043`，再攻 `B3DiscretePrimeSumUniformErrorPGe100000`。
