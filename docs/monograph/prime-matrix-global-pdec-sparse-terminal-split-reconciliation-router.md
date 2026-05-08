# Prime Matrix 全局 PDEC/sparse 终端拆分调和路由器

**状态：** `global_pdec_sparse_terminal_reconciled_to_pdec_cap_or_internal_kls_open`

本步把 GlobalPDECorSparseTerminalExclusion 与既有全局终端家族边界和拆分路由对齐。当前已物化 PDEC 与 sparse/LocalSurvivor 前沿已经清零，不能继续靠局部样本消元；全局终端门被压成完全自足路线的 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。这仍不是行列无条件闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
global_pdec_sparse_terminal_split_reconciled=true
current_materialized_frontier_exhausted=true
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
exact_model_gap_dprc_compatibility_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=GlobalPDECorSparseTerminalExclusion
terminal_gap_after_router=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

## 1. 拆分律

```text
GlobalPDECorSparseTerminalExclusion
  =>
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

这一步只导入已闭合的边界和拆分结果：当前物化前沿耗尽，但全局 PDEC-CAP 与内部 CleanKLS 大筛仍未证明。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| GlobalPDECorSparseTerminalGateActive | `true` | `false` | 上一层最新最窄点是 GlobalPDECorSparseTerminalExclusion。 | 把它与既有全局终端家族边界对齐。 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 仍只在假设早期零行反例链条中工作，不从真实样本缺席取证。 | 保持 row_column_unconditional_closed=false。 |
| CurrentPDECFrontierBoundaryImported | `true` | `true` | 当前已物化合法非二点 primitive PDEC 候选为零；未来 PDEC 必须提交显式同 formal unit schema。 | 不是全局 PDEC family 无条件排斥。 |
| CurrentSparseFrontierBoundaryImported | `true` | `true` | 当前 sparse/LocalSurvivor 前沿清零，已知入口 extractor 或合同准入均覆盖。 | 未来 sparse 路线仍需完整 extractor schema。 |
| MaterializedTerminalFrontierExhausted | `true` | `true` | 当前物化终端前沿没有可继续局部消元对象。 | 剩余不是样本层对象，而是全局家族证书。 |
| GlobalTerminalFamilySplitImported | `true` | `true` | 全局终端家族拆分已把 LocalSurvivor 与 NC-BLK 独立阻塞删除，连续终端二分送入 PDEC-CAP 或 CleanKLS/DLS。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| GlobalPDECorSparseTerminalReconciledToTerminalSplit | `true` | `true` | GlobalPDECorSparseTerminalExclusion 不再作为宽泛终端黑箱保留。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| PDEC_CAP | `false` | `false` | 尚未证明同一坏窗集合上的全局 U_CRT<L_PDEC 容量证书。 | PDEC_CAP。 |
| INTERNAL_CleanKLS_LargeSieve | `false` | `false` | 尚未证明 diffuse clean residual 的内部大筛吸收；外部 KLS/DI/BFI 只能作为条件分支。 | INTERNAL_CleanKLS_LargeSieve 或显式外部输入。 |
| ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock | `false` | `false` | moving-block 到终端门替换仍需与模型余量/有限 DPRC 账本口径兼容。 | ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | 最终晋级仍需 DStructure/Tail-log4/finite Rankin 独立验收。 | DStructureRankinPromotionPackage。 |

## 3. 最新输入基

条件输入基：

```text
((PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock AND ExplicitModelGapAndFiniteDPRCLedger) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

下一步最窄目标为 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`：在自足路线中二选一突破全局 PDEC-CAP 容量证书或内部 CleanKLS/DLS 大筛吸收；同时保留 moving-block/DPRC 口径兼容与 DStructure/Rankin 独立验收门。
