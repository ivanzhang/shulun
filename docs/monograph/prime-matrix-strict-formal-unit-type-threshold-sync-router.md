# Prime Matrix strict formal-unit 类型阈值同步路由器

**状态：** `formal_unit_type_threshold_reduced_to_rowfree_anticollapse_named_return_open`

`FormalUnitTypeThresholdLedger` 已不能作为独立固定常数继续悬挂：同参数窗口和 row-free type key 已经闭合，容量乘子把 D0/M# 需求侧接入，finite-prefix 的旧 Mertens 粗原子也已移除。真正未闭合的是保标签投影：不同 prefix 标签或标签骨架是否会在 row-free type/quotient 下大量合并。若完整 key 重复，可接同标签短复现；若粗 key 重复，则标签丢失并必须进入 PDEC/SAE/ColumnCRT 等命名回流。因此本步把类型阈值压成 `PrefixLabelSupportToRowFreeTypeAntiCollapse`，并行保留命名回流与 DStructure。

```text
formal_unit_type_threshold_reduction_closed=true
formal_unit_type_threshold_standalone_numeric_proved=false
prefix_label_support_to_row_free_type_anticollapse_proved=false
row_column_unconditional_closed=false
```

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `FormalUnitTypeThresholdTargetImported` | `true` | `false` | 上一层关闭旧 Mertens 粗原子后，把下一主攻点固定为 formal-unit 类型阈值。 | `FormalUnitTypeThresholdLedger` |
| `SameParameterTypeAlphabetClosed` | `true` | `true` | D0、M#、终端预算和 row-free type key 已登记在同一 alpha=0.43/P>=100000 窗口。 | `type key defined; threshold comparison remains separate` |
| `CapacityMultiplierAndMsharpLinkClosed` | `true` | `true` | 容量乘子纪律给出 M#>=\|R\|/ceil(P/z)，同一标签复用不能免费制造类型实例。 | `requires prefix mass and row-free anti-collapse` |
| `PrefixMassSideAvailableUnderCurrentContract` | `true` | `false` | finite-prefix 的 Mertens 尾段已回接，standard/external lower-sieve 合同下 D0/M# 需求侧可用。 | `strict first-principles beta-sieve appendix remains separate` |
| `NormalizedPotentialStillDoesNotDefineTypeCount` | `true` | `true` | 归一化势下界只给标签/质量侧；它本身不给 row-free type alphabet 的有效上界。 | `PrefixLabelSupportToRowFreeTypeAntiCollapse` |
| `BoundaryCapPigeonholeSkeletonImported` | `true` | `true` | 边界帽类型压缩的条件鸽巢骨架已闭合：若有效义务数超过保标签类型数，则可接短复现矛盾。 | `BoundaryCapLabelPreservingQuotientEntropyDeficit OR BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn` |
| `StandaloneNumericTypeThresholdRejected` | `true` | `true` | 不存在可脱离标签保持与命名回流的固定常数 T_formal；粗 key 压缩会丢标签，完整 key 又缺数量亏损。 | `PrefixLabelSupportToRowFreeTypeAntiCollapse AND BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn` |
| `LabelPreservingQuotientRouteAlreadyReduced` | `true` | `false` | 保标签商类型熵亏损已被既有证书压到统一终端预算严格缺口，不应作为新的黑箱常数重复保留。 | `UnifiedTerminalBudgetStrictInequality` |
| `SparseTerminalAntiCollapseNotRowFreeAntiCollapse` | `true` | `true` | 稀疏终端历史的无静默塌缩已闭合，但它只保证投影负载不消失，不等于 row-free type 保标签商熵亏损。 | `PrefixLabelSupportToRowFreeTypeAntiCollapse` |
| `FormalUnitTypeThresholdReducedToRowFreeAntiCollapse` | `true` | `false` | 类型阈值账本的独立内容已压成：prefix 标签支撑不能在 row-free type/quotient 中大量塌缩；若塌缩必须登记为命名回流。 | `PrefixLabelSupportToRowFreeTypeAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步是精确压缩，不是终局矛盾；row-free 抗塌缩、命名回流、moving atom 与 DStructure 仍未全部闭合。 | `PrefixLabelSupportToRowFreeTypeAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`PrefixLabelSupportToRowFreeTypeAntiCollapse`。
- 并行保留：
  - `NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-boundary-cap-type-compression-router.json` | `6af93d615695d4c6fb8ffa9af7458663d2cd3a16e5f961b081d5c108f3987c09` |
| `docs/monograph/prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json` | `7fd3d57383dc86ebf277117fc120cc42b2c43371ddd07612c16a0f0fd7bb1d55` |
| `docs/monograph/prime-matrix-strict-label-preserving-quotient-entropy-deficit-router.json` | `28bda5e210875011eac3c96784b35c95c00890f6bcc8b477903046e1ce7f9c87` |
| `docs/monograph/prime-matrix-strict-normalized-prefix-potential-router.json` | `4f86ea29ee34a43e365527b3c6e030050418f872c893c8ba470d8997ed66d6da` |
| `docs/monograph/prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json` | `10d4d7aab7648367047e86acd7069d1986730a138b8c74e4d8a8269378119e65` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-same-parameter-prefix-window-spec-router.json` | `d80bb554768007ffae5c7b1823173e7c985d85af69f458046ca8aa84f81fcc0b` |
| `experiments/prime_matrix_strict_formal_unit_type_threshold_sync_router.py` | `e7f6da4be3e9cbaef5592318170faf7e99b7a308352e04cf6d8dd1d667387a0f` |
