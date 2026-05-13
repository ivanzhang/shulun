# Prime Matrix strict 命名回流终端饱和同步路由器

**状态：** `named_return_terminal_saturation_synced_exclusion_open`

`NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` 的最新前沿已同步到终端饱和态：非持久命名回流不再另开扣除项，而是进入同参数显式正余量 `D_prefix-E_named-U_cold>0`；持久命名回流不再是宽黑箱，而是进入 acyclic 终端家族的 nonrecursive 破环、同集 PDEC 作用域匹配或新显式构造公式。本步只关闭同步边界，不证明两条通道排斥，因此行/列命题仍未无条件闭合。

```text
named_return_terminal_saturation_sync_closed=true
nonpersistent_named_return_absorbed_by_positive_margin=false
persistent_named_return_excluded_by_nonrecursive_breaker=false
named_return_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 终端饱和通道

| lane | saturation | current_status | meaning |
| --- | --- | --- | --- |
| `nonpersistent SAE/sparse/hot-core packets` | UnifiedTerminalBudgetStrictInequality -> ExplicitPositiveTerminalBudgetMarginInequality | `synchronized_open` | 非持久命名回流不能另开扣除项；它只能进入同参数预算余量。 |
| `persistent PDEC/ColumnCRT/fixed-history/hot-core` | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily -> (NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) | `saturated_open` | 持久命名回流已回到 acyclic 终端家族；剩余是破环、同集匹配或显式构造。 |
| `carrier-lcm source/valuation return` | SparseHistoryDemandExceedsNonpersistentSupplyBudget OR IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore | `frontier_closed_exclusion_open` | carrier-lcm return 不是新局部整除硬点；它按持久性接入两条主通道。 |
| `finite promotion / referee gate` | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `independent_gate_open` | DStructure/Rankin 是独立验收门，不能由命名回流同步自动关闭。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalDefectNoFreeExitImported` | `true` | `true` | 强 TV/端点缺陷已耗尽到命名出口集合，没有第四类无名出口。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `NamedReturnAlphabetCompressionImported` | `true` | `true` | PDEC/SAE/ColumnCRT/热核心/固定历史字母表已压成持久终端与非持久预算二分。 | UnifiedTerminalBudgetStrictInequality AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `CarrierLCMReturnBranchAligned` | `true` | `true` | carrier-lcm return 分支已按同一命名回流二分登记，不再形成独立局部整除硬点。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `NonpersistentLaneSaturatedToPositiveMargin` | `true` | `false` | 非持久命名回流已同步到统一预算最新前沿，即同参数正余量 D_prefix-E_named-U_cold>0。 | ExplicitPositiveTerminalBudgetMarginInequality |
| `PersistentLaneSaturatedToAcyclicTerminalFamily` | `true` | `false` | 持久命名回流已同步到 acyclic 终端家族饱和态，必须破环或同集匹配。 | NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `DStructureRankinGatePreserved` | `true` | `false` | 独立 DStructure/Rankin 验收门仍保留，不能由本同步证书替代。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `NamedReturnTerminalSaturationSyncClosed` | `true` | `true` | 命名回流的当前终端饱和边界已同步：剩余只在非持久正余量与持久终端破环两侧。 | ExplicitPositiveTerminalBudgetMarginInequality AND (NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) |
| `NonpersistentNamedReturnAbsorbedByPositiveMargin` | `false` | `false` | 还没有同一参数下的显式正终端预算余量数值/符号证书。 | ExplicitPositiveTerminalBudgetMarginInequality |
| `PersistentNamedReturnExcludedByNonrecursiveBreaker` | `false` | `false` | 还没有 nonrecursive actual noncanonical pre-Cauchy/signed-lift 破环包或等价替代证书。 | NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `NamedReturnExclusionProved` | `false` | `false` | 同步压缩不等于排斥；两条终端通道尚未同时关闭。 | ExplicitPositiveTerminalBudgetMarginInequality AND (NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未从早期零行反例链与真实结构链之间得到最终无条件矛盾。 | ExplicitPositiveTerminalBudgetMarginInequality AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 当前最窄硬点

主攻：

```text
ExplicitPositiveTerminalBudgetMarginInequality
```

并行守门：

```text
NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage AND AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完整剩余：

```text
ExplicitPositiveTerminalBudgetMarginInequality AND (NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json` | `ee2c23863dfa524a59dfb34333d45cef28f4e606a258cd4d7a02f2904455277c` |
| `docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json` | `a2d4e9a4d5d5f8d377571fc39d9c94e1ddb97d2afae30ef9e4c9e18296677307` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-named-return-exclusion-compression-router.json` | `7e54f4f456a2108e28a8100a147c9491951f9367c633dd51972e908291d127c2` |
| `docs/monograph/prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json` | `81ec38d8b42838b270454600184d385487f3c5453b7c4758920d3e0c8a5c22fa` |
| `docs/monograph/prime-matrix-strict-terminal-defect-exhaustion-router.json` | `d7b8551217e0b50d171f2eefc7ce67996eff1da16abaa3eab68c4640595c9658` |
| `experiments/prime_matrix_strict_named_return_terminal_saturation_sync_router.py` | `1b28b6d27e5ac648c5e8af4969e4843143569dddcf1db4aa665465e62cba080e` |
