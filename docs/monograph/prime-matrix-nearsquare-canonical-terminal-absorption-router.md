# Prime Matrix 近平方 canonical 终端吸收路由器

**状态：** `nearsquare_terminal_absorbed_beta_sieve_frontier_open`

本步把近平方条带终端门从当前链条中吸收掉。在 canonical-source 分支内，外层已经含有 NoFurtherCanonicalSourceTerminalPromotionGap，而 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve 已由当前终端晋级调和接回该边界；所以内层终端门不再是独立剩余。当前最窄点回到 beta-sieve lower weights 的自足构造与 99% 主系数账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
nearsquare_terminal_absorbed=true
self_contained_beta_sieve_appendix_proved=false
beta_sieve_main_coefficient_99pct_proved=false
standard_beta_sieve_import_accepted=false
external_short_interval_rough_lower_bound_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 吸收律

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
  =>
NoFurtherCanonicalSourceTerminalPromotionGap

A AND (((B AND T) OR C)) with T=>A and outer A compresses to A AND ((B OR C)) for the canonical branch.
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| NearSquareTerminalAbsorptionGateActive | `true` | `false` | 上一层已经把近平方条带终端准入全局 PDEC-CAP/internal-KLS 门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只整理假设早期零行反例链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| CanonicalTerminalPromotionImported | `true` | `true` | 既有当前终端晋级调和已证明 canonical-source 边界内 PDEC-CAP/internal-KLS 无新开门。 | NoFurtherCanonicalSourceTerminalPromotionGap |
| OuterCanonicalPromotionAlreadyPresent | `true` | `true` | 当前输入基外层已含 NoFurtherCanonicalSourceTerminalPromotionGap，可吸收内层同一终端门。 | 布尔吸收 A AND ((B AND A) OR C) => A AND (B OR C)。 |
| NearSquareTerminalAbsorbed | `true` | `false` | 近平方条带终端门被 canonical 终端晋级边界吸收，不再是独立剩余。 | SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 |
| SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix | `false` | `false` | 完全自足路线仍需逐行给出 Rosser-Iwaniec beta-sieve lower weights 构造。 | SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix |
| BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 | `false` | `false` | 仍需显式证明 P>=100000 下主系数达到保守 99% 模型主项。 | BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 若接受标准 beta-sieve 定理，可绕过自足权重构造，但不关闭 sawtooth 外部/generic 分支。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可直接替代整个内部筛权+sawtooth 路线。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 3. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

直接攻 `SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix`，随后攻 `BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000`。
