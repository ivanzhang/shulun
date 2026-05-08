# Prime Matrix 近平方条带终端准入路由器

**状态：** `nearsquare_strip_terminal_admitted_to_global_pdec_sparse_split_open`

本步删除了近平方条带的独立终端地位。上一层已把失败态做成同一 dyadic 条带 formal unit 的 PDEC/SAE 证书；既有全局终端家族边界又说明这类证书不能作为第四出口，必须进入全局 PDEC/sparse 终端拆分。因此当前真正剩余改为 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。这仍不是行列无条件闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
nearsquare_strip_terminal_admission_closed=true
nearsquare_strip_independent_terminal_remaining=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 准入链条

```text
NearSquareStripPDECOrSAEExclusionAlpha043 -> GlobalPDECorSparseTerminalExclusion
GlobalPDECorSparseTerminalExclusion -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

## 2. 替换律

```text
NearSquareStripPDECOrSAEExclusionAlpha043
  =>
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| NearSquareStripTerminalGateActive | `true` | `false` | 最新最窄点是排斥 dyadic 近平方条带产生的 PDEC/SAE 证书。 | NearSquareStripPDECOrSAEExclusionAlpha043 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条中做终端准入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| NearSquareStripSameFormalUnitCertificate | `true` | `true` | 上一层已证明失败态生成同一 dyadic 条带 formal unit，且持久/稀疏二分准入 PDEC/SAE。 | GlobalPDECorSparseTerminalExclusion |
| CurrentMaterializedTerminalFrontierImported | `true` | `true` | 当前已物化终端前沿耗尽；未来证书不能靠样本消元，必须进入全局终端家族。 | GlobalPDECorSparseTerminalExclusion |
| PDECAndSparseBoundaryImported | `true` | `true` | PDEC 显式输入边界与 future sparse packet 边界均已登记；二者本身仍未无条件排斥。 | GlobalPDECorSparseTerminalExclusion |
| GlobalTerminalSplitImported | `true` | `true` | 全局终端家族拆分已把 GlobalPDECorSparseTerminalExclusion 压到 PDEC-CAP 或内部 CleanKLS/DLS。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| NearSquareIndependentTerminalRemoved | `true` | `false` | 近平方条带没有独立第四出口；其终端义务被吸收到全局 PDEC/sparse 终端门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve | `false` | `false` | 仍需证明全局 PDEC-CAP 容量证书，或内部 CleanKLS/DLS 大筛吸收。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| ExternalWellFactorableSawtoothDispersionBoundAlpha043 | `false` | `false` | 外部解析路线仍可直接给 well-factorable sawtooth/条带分散估计。 | ExternalWellFactorableSawtoothDispersionBoundAlpha043 |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 短区间 rough-number 下界仍可绕过内部 sawtooth 与条带分析。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043))) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((((SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000) OR StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR ExternalWellFactorableSawtoothDispersionBoundAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

直接攻 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`；外部备线仍为 `ExternalWellFactorableSawtoothDispersionBoundAlpha043`。
