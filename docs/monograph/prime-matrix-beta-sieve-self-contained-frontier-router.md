# Prime Matrix beta-sieve 自足前沿拆分路由器

**状态：** `beta_sieve_frontier_split_to_three_self_contained_atoms_open`

本步把 beta-sieve 双输入拆成三枚可审查原子。参数、支撑与容量乘子已经由上一层账本固定：D=P、z=P^0.43、s=2.325581，且 99% 主系数足以覆盖 90% sawtooth 损失后的 401 目标。真正自足剩余现在是：有限递归 lower weights 构造、lower-bound 支配证明、以及 P>=100000 的 1% 显式主系数误差。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
beta_sieve_frontier_split_closed=true
self_contained_beta_sieve_appendix_proved=false
beta_sieve_main_coefficient_99pct_proved=false
standard_beta_sieve_import_accepted=false
external_short_interval_rough_lower_bound_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 容量账本

| item | value |
| --- | ---: |
| alpha | 0.430000 |
| D | D=P |
| s=logD/logz | 2.325581 |
| linear sieve f(s) | 0.431717689229 |
| model main at P=100000 | 4896.256004 |
| target S | 401 |
| target/main | 0.081899 |
| sawtooth loss budget | 0.900000 main |
| minimum main fraction after 90% loss | 0.981899 |
| conservative main fraction | 0.990000 |
| conservative surplus fraction | 0.008101 |
| conservative surplus count at P=100000 | 39.663040 |
| normalized 1% error target | 0.004317176892 |

## 2. 拆分律

完全自足路线：

```text
(SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000)
  =>
(BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000)
```

允许标准定理导入的 conditional 路线：

```text
(SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000)
  =>
((BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted)
```

## 3. 自足证明合同

构造合同：

- 定义有限递归 lower weights lambda_d^-，并证明 lambda_1^-=1、lambda_d^- in {-1,0,1}。
- 证明 lambda_d^- 只支撑在 squarefree d<=P 且所有素因子 <P^0.43 的 d 上。
- 递归必须完全有限化；不能直接引用标准 beta-sieve 定理作为自足证明。

支配合同：

- 对任意整数 n，按 n 的小素因子集合做有限归纳。
- 证明 lower weights 的 alternating 递归给出筛剩余指示函数的下界。
- 该证明只依赖递归结构，不依赖真实零行缺席或统计实验。

主系数合同：

- 把 W^-(P)=sum lambda_d^-/d 与 V(z)f(s) 比较。
- 在 P>=100000、s=1/0.43 下证明 W^-(P)>=0.99 V(z)f(s)。
- 等价归一误差目标为 <=0.004317176892290826。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BetaSieveFrontierGateActive | `true` | `false` | 最新 canonical 自足输入基正卡在 beta-sieve 自足构造与 99% 主系数双原子。 | SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内整理尾段筛输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| SupportLevelAndSAlreadyPinned | `true` | `true` | 上一层已固定 D=P、z=P^0.43、s=1/0.43，且权重支撑只允许 squarefree d<=P、p\|d=>p<z。 | 无新的参数自由度。 |
| CapacityMultiplierDisciplinePreserved | `true` | `true` | 90% sawtooth 损失预算要求主系数至少保留 0.981899...；99% 目标在 P=100000 仍有正余量。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| SelfContainedAppendixSplitToConstructionAndDominance | `true` | `false` | 自足 beta-sieve 附录不再是单一黑箱；它必须拆成 finite recursive lower weights 与 lower-bound 支配证明。 | BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof |
| MainCoefficientAtomRenormalizedToOnePercent | `true` | `false` | 旧 99% 主系数输入被重写为一个明确的 1% 归一误差账本。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| StandardBetaSieveImportBoundaryMarked | `true` | `false` | 标准 Rosser-Iwaniec beta-sieve 定理可作为 conditional 导入，但不能算作自足闭合。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| BetaSieveLowerWeightRecursiveConstructionLedger | `false` | `false` | 需要逐行给出 beta-sieve lower weights 的有限递归、截断、符号与支撑。 | BetaSieveLowerWeightRecursiveConstructionLedger |
| BetaSieveLowerBoundDominanceProof | `false` | `false` | 需要证明对任意整数 n 有 sum_{d\|(n,P(z))} lambda_d^- <= 1_{(n,P(z))=1}。 | BetaSieveLowerBoundDominanceProof |
| BetaSieveMainCoefficientExplicit99PercentPGe100000 | `false` | `false` | 需要把离散权重主系数与连续 f(1/0.43) 的误差显式压到 1% 以内，且 P>=100000 全尾段有效。 | BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开整个内部 beta-sieve 包。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (((BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

直接攻 `BetaSieveLowerWeightRecursiveConstructionLedger`；随后验收 `BetaSieveLowerBoundDominanceProof` 与 `BetaSieveMainCoefficientExplicit99PercentPGe100000`。
