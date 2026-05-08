# Prime Matrix B=3 离散素和误差边界路由器

**状态：** `discrete_error_reduced_to_stieltjes_and_boundary_remainder_inputs_open`

最后内部离散误差不能由有限 checkpoint 直接闭合。现有精确审计余量很大，但要覆盖所有 P>=100000，必须证明两个明确输入：所有 B=3 admissible words 的素数倒数迭代和 到连续 Stieltjes 积分的统一下界，以及交错边界/跳变余项的一百分点预算。这就是标准 beta-sieve 基本引理的内部化核心。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
continuous_beta_sieve_surplus_proved=true
discrete_prime_sum_uniform_error_reduced=true
discrete_prime_sum_uniform_error_proved=false
beta_sieve_main_coefficient_99pct_proved=false
row_column_unconditional_closed=false
```

## 1. checkpoint 余量摘要

```text
checkpoint_count=7
all_checkpoints_pass_99pct=true
min_checkpoint_P=10000000
min_checkpoint_ratio=1.5527757826943358
min_surplus_to_99pct=0.5627757826943358
```

## 2. 自足替换

```text
B3DiscretePrimeSumUniformErrorPGe100000
  =>
(B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger)
```

Accepting the standard Rosser-Iwaniec beta-sieve fundamental lemma closes the discrete Stieltjes and boundary remainder package externally, but it is not a self-contained internal closure.

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DiscreteErrorGateActive | `true` | `false` | 上一层已经把 beta-sieve 内部点压到离散素和统一误差。 | B3DiscretePrimeSumUniformErrorPGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内处理筛权主系数误差，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ContinuousSurplusAvailable | `true` | `true` | 连续层给出 1% f(s) 的误差预算。 | 离散统一误差必须小于该预算，或利用更强的正向离散余量。 |
| CheckpointAuditHasLargePositiveMargin | `true` | `false` | 有限 checkpoint 全部通过，最小 W^-/Vf 约 1.553，远高于 0.99。 | 有限审计不能推出全尾段。 |
| FiniteCheckpointCannotCloseUniformTail | `true` | `true` | P>=100000 有无限多个素数阈值跳变；有限样本不能替代统一 Stieltjes/边界余项证明。 | B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger |
| DiscreteErrorReducedToTwoSelfContainedInputs | `true` | `false` | 离散误差已压成两个不可混淆的最小义务：素和到积分的统一账本，以及交错边界余项的一百分点预算。 | B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger |
| B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 | `false` | `false` | 需要对所有 B=3 admissible prime words 建立从素数倒数迭代和到连续 Stieltjes 积分的统一显式下界。 | B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 |
| B3AlternatingBoundaryRemainderOnePercentLedger | `false` | `false` | 需要控制交错截断边界、跳变端点和符号余项，总损失小于 0.01 f(s)，或证明其实际正向。 | B3AlternatingBoundaryRemainderOnePercentLedger |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 标准 Rosser-Iwaniec beta-sieve 基本引理可外部关闭这两个输入，但这不是内部自足闭合。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (((B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

先攻 `B3PrimeWordStieltjesIntegralUniformLedgerPGe100000`，再攻 `B3AlternatingBoundaryRemainderOnePercentLedger`。
