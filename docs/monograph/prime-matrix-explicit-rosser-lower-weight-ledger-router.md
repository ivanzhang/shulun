# Prime Matrix 显式 Rosser-Iwaniec 下界权重账本路由器

**状态：** `explicit_rosser_weight_ledger_compressed_to_beta_sieve_boundary_open`

本步把显式 Rosser-Iwaniec 下界权重输入继续压窄。参数层已闭合：D=P、z=P^0.43 给 s=1/0.43=2.325581，f(s)=0.431717689229，P=100000 处 10% 模型主项 489.625600>401。真正剩余不是参数选择，而是：若走自足路线，必须证明 beta-sieve lower weights 构造及其主系数误差；若接受标准 Rosser-Iwaniec beta-sieve 定理，则权重账本可外部关闭，下一硬点转为精确加权 floor/sawtooth 余项。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
explicit_rosser_iwaniec_lower_weight_ledger_compressed=true
explicit_rosser_iwaniec_lower_weight_ledger_proved=false
standard_beta_sieve_import_accepted=false
self_contained_beta_sieve_appendix_proved=false
main_coefficient_ten_percent_error_proved=false
exact_residue_weighted_floor_sawtooth_bound_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 参数账本

| item | value |
| --- | ---: |
| alpha | 0.430000 |
| D | D=P |
| z at P=100000 | 141.253754 |
| floor(z) at P=100000 | 141 |
| s=logD/logz | 2.325581 |
| s with floor(z) | 2.326426 |
| linear sieve f(s) | 0.431717689229 |
| model main at P=100000 | 4896.256004 |
| 10% model main | 489.625600 |
| target S | 401 |
| target/main | 0.081899 |
| required coefficient 0.1 f(s) | 0.043171768923 |
| allowed normalized error 0.9 f(s) | 0.388545920306 |

## 2. 权重对象

所需 lower weights 只需满足以下弱接口：

```text
lambda_1^-=1; lambda_d^- in {-1,0,1}
lambda_d^-=0 unless d is squarefree, d<=D=P, and every prime divisor of d is <z=P^0.43
sum_{d|(n,P(z))} lambda_d^- <= 1_{(n,P(z))=1} for every integer n
W^-(P)=sum_{d|P(z)} lambda_d^-/d >= 0.1 V(z) f(1/0.43) for P>=100000
```

这比完整最优线性筛常数弱：这里只要求主系数至少达到标准模型的 10%。

## 3. 拆分律

自足路线：

```text
ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000
  =>
(SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000)
```

允许标准 beta-sieve 定理导入的路线：

```text
ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000
  =>
((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted)
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExplicitWeightGateActive | `true` | `false` | 最新最窄内部点是固定 Rosser-Iwaniec lower weights、level、s 与主项常数。 | ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行反例链条内的尾段筛输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| LevelChoiceDEqualsPAlpha043Closed | `true` | `true` | 取 D=P、z=P^0.43，则 s=logD/logz=1/0.43 位于线性下界筛 2<s<3 区间；floor(z) 后仍有 s>2。 | 无剩余。 |
| TenPercentMainCoefficientAlgebraClosed | `true` | `true` | P=100000 处 10% 线性筛模型主项已超过 401，且 P/logP 在尾段递增。 | 无剩余。 |
| WeightLedgerCompressedToBetaSieveBoundary | `true` | `false` | 显式权重原子被压成：自足 beta-sieve 构造与主系数误差，或接受标准 Rosser-Iwaniec beta-sieve 定理。 | (SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| StandardBetaSieveSourceLocated | `true` | `false` | 标准外部来源可登记为 Friedlander-Iwaniec beta-sieve/Rosser-Iwaniec weights；接受它会关闭权重账本，但不是自足证明。 | StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix | `false` | `false` | 若坚持完全自足，需要逐行给出 lower weights 的构造，并证明其 lower-bound 支配关系。 | SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix |
| BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000 | `false` | `false` | 还需显式证明主系数 normalized error 不超过 0.9 f(s)，等价于 W^->=0.1 V(z)f(s)。 | BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000 |
| ExactResidueWeightedFloorSawtoothTenPercentBound | `false` | `false` | 即使权重包被接受，仍必须证明精确 CRT 残基 floor 余项的加权负损失不会吞掉 10% 主项。 | ExactResidueWeightedFloorSawtoothTenPercentBound |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部短区间 rough-number 下界仍可绕开内部 beta-sieve 权重与 sawtooth 两步。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000) AND ExactResidueWeightedFloorSawtoothTenPercentBound) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND ExactResidueWeightedFloorSawtoothTenPercentBound) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043))) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND ExactResidueWeightedFloorSawtoothTenPercentBound) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 来源边界

- 标准外部来源：Friedlander-Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57，beta-sieve/Rosser-Iwaniec weights。
- 本路由尚未接受该外部输入为自足证明；若接受它，下一步直接转入 `ExactResidueWeightedFloorSawtoothTenPercentBound`。

## 7. 下一步

自足路线先攻 `SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix`，随后攻 `BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000`。若允许标准 beta-sieve 定理导入，则权重账本让位给 `ExactResidueWeightedFloorSawtoothTenPercentBound`。
