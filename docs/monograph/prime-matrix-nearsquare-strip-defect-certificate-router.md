# Prime Matrix 近平方条带缺陷证书路由器

**状态：** `signed_nearsquare_strip_bound_reduced_to_pdec_or_sae_exclusion_open`

本步把 signed near-square strip bound 的失败态完全显化。若它失败，必有一个 side/h/t/a dyadic 条带承担强负偏差；该条带是同一 finite formal unit 的测试函数。因此剩余不再是无名非集中，而是排斥这些条带产生的 PDEC 或 SAE 证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
failure_to_dyadic_strip_certificate_proved=true
dyadic_strip_certificate_formal_unit_admission_proved=true
persistent_sparse_pdec_sae_admission_proved=true
signed_strip_bound_compressed=true
nearsquare_strip_pdec_or_sae_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 失败态证书

若

```text
signed near-square strip discrepancy < -0.90 M(P)
```

则按 `side,h,t,a` dyadic 分块，必有一个块承担至少平均强度的负偏差。

| item | value |
| --- | ---: |
| tail start | 100000 |
| ceil(log2 P) | 17 |
| dyadic block count bound | 9826 |
| 90% loss budget at tail start | 4406.630403 |
| pigeonhole threshold at tail start | 0.448466 |

## 2. Formal Unit 字段

| field | value |
| --- | --- |
| `Omega` | prime rows P in the hypothetical counterexample family |
| `tau` | fixed dyadic side/h/t/a strip and the induced residue phase P mod Q_B |
| `weight` | Rosser lower weight restricted to the fixed strip block |
| `test_function` | centered signed near-square strip indicator minus arc-length expectation |
| `persistent_branch` | bad rows of positive density give PDEC/Fourier defect |
| `sparse_branch` | isolated bad rows become SAE/local-survivor packets |

## 3. 压缩律

```text
SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000
  =>
NearSquareStripPDECOrSAEExclusionAlpha043
```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SignedNearSquareStripGateActive | `true` | `false` | 最新真正剩余是有符号 Rosser 质量在近平方条带上的非集中。 | SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条中处理失败态，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| FailureToDyadicStripCertificateClosed | `true` | `true` | 若总条带偏差<-0.90M(P)，按 side,h,t,a dyadic 分块必有一个强负块证书。 | DyadicSignedNearSquareStripDefectCertificateAlpha043 |
| DyadicStripCertificateIsFiniteFormalUnit | `true` | `true` | 固定 dyadic 条带、side 与 Rosser 权重块后，坏相位是同一有限 formal unit 的测试函数。 | 同 formal unit PDEC/SAE 准入。 |
| PersistentSparseAdmissionImported | `true` | `true` | 同一 formal unit 的坏证书若持久则进入 PDEC，若稀疏则进入 SAE/local survivor。 | NearSquareStripPDECOrSAEExclusionAlpha043 |
| SignedStripBoundCompressedToPDECorSAEExclusion | `true` | `false` | 证明原有 signed strip bound 等价压缩为排斥所有 dyadic 条带 PDEC/SAE 证书。 | NearSquareStripPDECOrSAEExclusionAlpha043 |
| NearSquareStripPDECOrSAEExclusionAlpha043 | `false` | `false` | 仍需证明这些新条带 formal unit 的 persistent PDEC 或 sparse SAE 均不能实际存在。 | NearSquareStripPDECOrSAEExclusionAlpha043 |
| ExternalWellFactorableSawtoothDispersionBoundAlpha043 | `false` | `false` | 外部解析路线仍可直接给 well-factorable sawtooth/条带分散估计。 | ExternalWellFactorableSawtoothDispersionBoundAlpha043 |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 短区间 rough-number 下界仍可绕过内部 sawtooth 与条带分析。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) AND NearSquareStripPDECOrSAEExclusionAlpha043) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND (NearSquareStripPDECOrSAEExclusionAlpha043 OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043))) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND (NearSquareStripPDECOrSAEExclusionAlpha043 OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

直接攻 `NearSquareStripPDECOrSAEExclusionAlpha043`，即排斥 dyadic 近平方条带产生的 PDEC/SAE 证书。
