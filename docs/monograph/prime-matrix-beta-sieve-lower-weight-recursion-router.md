# Prime Matrix beta-sieve lower weight 递归构造路由器

**状态：** `lower_weight_recursion_constructed_support_closed_dominance_open`

本步把 beta-sieve lower weight 构造原子闭成一个显式有限对象：固定 D=P、z=P^0.43，对 squarefree d 的降序素因子 word 使用偶数位 Rosser 门，并定义 lambda_d^- 为 mu(d) 或 0。这样 lambda_1、符号、squarefree、小素因子支撑与 d<P 都已经由有限递归和 B>=2 的代数检查闭合。真正剩余前移到逐点 lower-bound 支配证明，以及该具体权重的 99% 主系数显式误差。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
lower_weight_recursive_construction_closed=true
lower_weight_dominance_proved=false
beta_sieve_main_coefficient_99pct_proved=false
standard_beta_sieve_import_accepted=false
external_short_interval_rough_lower_bound_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 显式 word rule

```text
parameters: D=P, z=P^0.43, fixed integer word exponent B>=2
prime_word: for squarefree d|P(z), write d=p1...pr with p1>...>pr
lower_admissible: for every m with 1<=2m<=r, p1...p_{2m-1} * p_{2m}^B < D
weight: lambda_1^-=1; lambda_d^-=mu(d) if lower_admissible, else 0
recursive_generation: append smaller primes only; after each even-position append, test the new p1...p_{2m-1}p_{2m}^B<D gate
```

## 2. 支撑证明

- lambda_d^- is defined by mu(d) on squarefree words and 0 otherwise, hence lies in {-1,0,1}.
- All prime factors are drawn from primes <z by construction.
- If r is even, the final even gate gives p1...p_{r-1}p_r^B<D, hence d<D.
- If r is odd and r>=3, the previous even gate gives p1...p_{r-2}p_{r-1}^B<D; since p_r<=p_{r-1} and B>=2, d<D.
- If r=1, then d=p1<z<D because s=logD/logz=1/0.43>1.

## 3. P=100000 轻量审计

该审计只验证递归对象有限且支撑正常，不作为 99% 主系数证明。

| item | value |
| --- | ---: |
| audit P | 100000 |
| z | 141.253754 |
| floor z | 141 |
| word exponent for audit | 3 |
| small prime count | 34 |
| largest small prime | 139 |
| squarefree candidates under P | 7732 |
| accepted lower weights | 790 |
| positive weights | 395 |
| negative weights | 395 |
| max supported d | 22110 |
| signed harmonic weight sum | 0.081446823200 |

## 4. 替换

```text
BetaSieveLowerWeightRecursiveConstructionLedger
  =>
EXPLICIT_LOWER_WORD_RULE_DEFINITION_CLOSED
```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LowerWeightConstructionGateActive | `true` | `false` | 上一层最新最窄点正是 beta-sieve lower weights 的有限递归构造。 | BetaSieveLowerWeightRecursiveConstructionLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内固定筛权对象，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| DescendingPrimeWordRulePinned | `true` | `true` | 对 squarefree d\|P(z)，按降序素因子 p1>...>pr 定义 lower admissible word；lambda_d^- 为 mu(d) 或 0。 | 无定义自由度。 |
| FiniteRecursiveGenerationClosed | `true` | `true` | 每次只追加更小素数，并在偶数位置检查 p1...p_{2m-1} p_{2m}^B<D；小素数集有限，递归终止。 | 无算法性剩余。 |
| SupportSignAndLevelLedgerClosed | `true` | `true` | 由定义立即得到 lambda_1^-=1、lambda_d^- in {-1,0,1}、squarefree、小素因子支撑；B>=2 给 d<D<=P。 | 无支撑层剩余。 |
| LowerWeightRecursiveConstructionLedgerClosed | `true` | `false` | 构造原子已经降为显式有限对象，不再是黑箱输入。 | BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| BetaSieveLowerBoundDominanceProof | `false` | `false` | 下一步必须证明这些 lower weights 对筛剩余指示函数给出逐点下界。 | BetaSieveLowerBoundDominanceProof |
| BetaSieveMainCoefficientExplicit99PercentPGe100000 | `false` | `false` | 随后还要证明该构造的主系数在 P>=100000 尾段达到 99% 归一目标。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 若允许标准 Rosser-Iwaniec beta-sieve 定理导入，可直接替代支配与主系数两步；但不是自足闭合。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 6. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (((BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 下一步

直接攻 `BetaSieveLowerBoundDominanceProof`；随后攻 `BetaSieveMainCoefficientExplicit99PercentPGe100000`。
