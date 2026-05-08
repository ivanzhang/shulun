# Prime Matrix beta-sieve lower-bound 支配证明路由器

**状态：** `lower_bound_dominance_closed_main_coefficient_open`

本步关闭 beta-sieve lower-bound 支配原子。证明是纯组合的 Buchstab 树截断：完整降序子集树给出 1_{A=empty}，lower word rule 只在奇层删除偶子树；这些偶子树完整贡献非负，而偶层的奇子节点全部保留，所以截断和不超过完整和。因此显式 lambda_d^- 确实逐点下界筛剩余指示函数。当前唯一内部 beta-sieve 剩余前移到 99% 主系数显式误差。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
lower_weight_recursive_construction_closed=true
lower_weight_dominance_proved=true
beta_sieve_main_coefficient_99pct_proved=false
standard_beta_sieve_import_accepted=false
external_short_interval_rough_lower_bound_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 支配命题

```text
For every integer n, with P(z)=prod_{p<z} p, sum_{d|(n,P(z))} lambda_d^- <= 1_{(n,P(z))=1}.
```

## 2. 证明骨架

- Let A be the finite set of primes p<z dividing n.
- The complete descending subset tree has alternating sum sum_{T subset A} (-1)^|T| = 1 if A is empty and 0 otherwise.
- The lower word rule defines a pruned subtree: even-depth words retain every odd child; odd-depth words retain only even children passing the Rosser gate.
- For an even prefix w, every odd child remains admissible because the previous even Rosser gate and B>=2 imply the extended product stays below D.
- Inductively, a retained child subtree is no larger than its complete alternating subtree.
- At odd depth, discarded even child subtrees have complete alternating contribution 0 or +1, hence deleting them can only decrease the total.
- Therefore the pruned lower sum is at most the complete alternating sum, giving the desired pointwise lower-bound dominance.

## 3. 替换

```text
BetaSieveLowerBoundDominanceProof
  =>
BUCHSTAB_TREE_PARITY_PRUNING_DOMINANCE_CLOSED
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DominanceGateActive | `true` | `false` | 上一层最新最窄点是证明显式 lower word rule 对筛剩余指示函数逐点给出下界。 | BetaSieveLowerBoundDominanceProof |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内证明筛权代数恒等式，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ExplicitLowerWordRuleAvailable | `true` | `true` | 上一层已经固定 lambda_d^- 的有限降序 word rule、符号、squarefree 支撑和 d<P。 | 无定义层剩余。 |
| ExactBuchstabTreeIdentity | `true` | `true` | 对任意有限小素因子集合 A，完整降序子集树的交错和等于 1_{A=empty}。 | 无解析估计。 |
| ParityPruningDominanceLemma | `true` | `true` | 偶层完整保留所有奇子节点；奇层只保留通过 Rosser 门的偶子节点。删去的偶子树完整贡献非负，故截断和不超过完整和。 | 无统计输入。 |
| BetaSieveLowerBoundDominanceClosed | `true` | `true` | 因此对每个整数 n，sum_{d\|(n,P(z))} lambda_d^- <= 1_{(n,P(z))=1}。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| BetaSieveMainCoefficientExplicit99PercentPGe100000 | `false` | `false` | 仍需证明该具体 lower word rule 的主系数在 P>=100000 尾段达到 99% 归一目标。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| StandardRosserIwaniecBetaSieveTheoremImportAccepted | `false` | `false` | 若允许标准 Rosser-Iwaniec beta-sieve 定理导入，可替代内部支配与主系数；但本步已经自足关闭支配层。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((BetaSieveMainCoefficientExplicit99PercentPGe100000 OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND ((BetaSieveMainCoefficientExplicit99PercentPGe100000 OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND ((BetaSieveMainCoefficientExplicit99PercentPGe100000 OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

直接攻 `BetaSieveMainCoefficientExplicit99PercentPGe100000`。
