# Prime Matrix B=3 连续 beta-sieve 主项余量路由器

**状态：** `continuous_beta_surplus_closed_discrete_error_open`

连续主项余量已闭合。alpha=0.43 给 s=2.325581，位于线性下界筛 2<s<3 的显式公式区间；连续主项等于 f(s)=0.431717689229，因此相对 99% 目标保留 1% 的绝对归一误差预算 0.004317176892。当前唯一内部 beta-sieve 剩余变成离散素和统一误差。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
continuous_beta_sieve_surplus_proved=true
discrete_prime_sum_uniform_error_proved=false
beta_sieve_main_coefficient_99pct_proved=false
row_column_unconditional_closed=false
```

## 1. 连续账本

| item | value |
| --- | ---: |
| alpha | 0.430000 |
| s=1/alpha | 2.325581 |
| 2<s<3 | true |
| f(s) | 0.431717689229 |
| continuous coefficient | 0.431717689229 |
| 99% threshold | 0.427400512337 |
| absolute surplus | 0.004317176892 |
| relative surplus | 0.010000 |

## 2. 证明骨架

- The continuous linear lower sieve in dimension one is governed by the beta/Buchstab differential-difference system.
- On the interval 2<s<3, the lower function has the explicit solution f(s)=2e^gamma log(s-1)/s.
- For alpha=0.43, s=1/alpha=2.325581..., so this formula applies directly.
- The continuous main coefficient is therefore exactly f(s), while the project only needs 0.99 f(s).
- The remaining 0.01 f(s)=0.004317176892... is the entire budget for discrete prime-sum error.

## 3. 替换

```text
B3ContinuousBetaSieveCoefficientSurplusAlpha043
  =>
CONTINUOUS_LINEAR_SIEVE_F_ALPHA043_CLOSED
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ContinuousSurplusGateActive | `true` | `false` | 上一层把 99% 主系数原子压成连续 beta 主项余量与离散素和误差。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步只处理筛权连续主项函数，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| LowerPackageAvailable | `true` | `true` | lower weights 构造和逐点支配已闭合，连续主项对象有定义。 | 无 lower-weight 结构剩余。 |
| LinearLowerSieveRangeClosed | `true` | `true` | alpha=0.43 给 s=1/alpha=2.325581，处于 2<s<3 的显式公式区间。 | 无区间剩余。 |
| ContinuousLinearSieveFormulaClosed | `true` | `true` | 连续线性下界筛在 2<s<3 满足 f(s)=2e^gamma log(s-1)/s。 | 离散素和误差仍未处理。 |
| ContinuousSurplusAbove99PercentClosed | `true` | `true` | 连续主项等于 100% f(s)，因此相对 99% 目标留下 1% 误差余量。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| B3ContinuousBetaSieveCoefficientSurplusClosed | `true` | `true` | 连续层已经闭合；剩余唯一内部点是离散素和统一误差小于 1% f(s)。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| B3DiscretePrimeSumUniformErrorPGe100000 | `false` | `false` | 需要证明 P>=100000 下离散素数乘积和到连续模型的误差不超过 0.01 f(s)。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 若接受标准 Rosser-Iwaniec beta-sieve 定理，可外部关闭离散误差；但不是内部自足闭合。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((B3DiscretePrimeSumUniformErrorPGe100000 OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((B3DiscretePrimeSumUniformErrorPGe100000 OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((B3DiscretePrimeSumUniformErrorPGe100000 OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

直接攻 `B3DiscretePrimeSumUniformErrorPGe100000`。
