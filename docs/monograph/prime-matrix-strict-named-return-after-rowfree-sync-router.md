# Prime Matrix strict row-free 后命名回流同步路由器

**状态：** `named_return_alphabet_compressed_to_budget_and_terminal_family_open`

`NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` 已完成字母表级压缩：无名缺陷出口被删除，持久命名回流回到 acyclic PDEC/CleanKLS 终端包，非持久回流进入统一预算吸收。因此命名回流不再作为独立宽黑箱；下一步应直接攻 `UnifiedTerminalBudgetStrictInequality`，并行保留持久终端族的 moving atom/PDEC-CAP 排斥与 DStructure。

```text
named_return_alphabet_compression_closed=true
named_return_exclusion_proved=false
unified_terminal_budget_strict_inequality_proved=false
row_column_unconditional_closed=false
```

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `NamedReturnTargetImportedFromRowFree` | `true` | `false` | row-free 抗塌缩预算版闭合后，剩余回流不能静默消失，只能作为命名回流或预算项处理。 | `NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` |
| `NoUnnamedDefectExitClosed` | `true` | `false` | 容量失败、丢标签、相位漂移、端点/TV 缺陷没有第四类无名出口，必须进入命名字母表。 | `NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` |
| `NamedAlphabetCompressionClosed` | `true` | `false` | PDEC/SAE/ColumnCRT/热核心/固定历史等命名出口字母表本身已压成持久终端包与非持久预算。 | `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily OR UnifiedTerminalBudgetStrictInequality` |
| `SameParameterDeductionSchemaClosed` | `true` | `false` | E_named 的同参数扣除表结构闭合；不能凭空填 0，必须通过终端排斥或预算吸收。 | `NamedReturnSameParameterDeductionTable` |
| `PersistentNamedReturnReducedToTerminalFamily` | `true` | `false` | 持久命名回流只有在 acyclic terminal family 被排斥后才能数值归零。 | `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily` |
| `NonpersistentNamedReturnReducedToBudgetAbsorption` | `true` | `false` | 非持久命名回流不需要单独逐项排斥；它必须进入 U_cold/统一预算吸收。 | `UnifiedTerminalBudgetStrictInequality` |
| `NamedReturnAlphabetNoLongerIndependentHardpoint` | `true` | `false` | 命名回流这个宽标签已完成拆解；剩余是终端族排斥与统一预算严格不等式，不是再扩展出口字母表。 | `UnifiedTerminalBudgetStrictInequality AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily` |
| `NamedReturnExclusionCurrentCorpusProved` | `false` | `false` | 当前材料尚未排斥所有持久终端族，也未证明统一预算严格吸收全部非持久回流。 | `UnifiedTerminalBudgetStrictInequality AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭命名回流字母表硬点，不关闭最终反例矛盾。 | `UnifiedTerminalBudgetStrictInequality AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`UnifiedTerminalBudgetStrictInequality`。
- 并行保留：
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DirectAcyclicSameSetPDECCapDualCertificate`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json` | `a1f751511b011c2bd64b4fe717c36436c18d3946c2407fa0d4cdb4b3338cd31c` |
| `docs/monograph/prime-matrix-strict-named-return-exclusion-compression-router.json` | `7e54f4f456a2108e28a8100a147c9491951f9367c633dd51972e908291d127c2` |
| `docs/monograph/prime-matrix-strict-named-return-same-parameter-deduction-router.json` | `2eee9f35708971c2d184bcc194c94c6be162a4f928834f628380ed747a45e1df` |
| `docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json` | `f480a9407780a2cc2a9f8e6fc742d6f2db1fa6875fe3de58f687f585abef12e6` |
| `docs/monograph/prime-matrix-strict-terminal-defect-exhaustion-router.json` | `d7b8551217e0b50d171f2eefc7ce67996eff1da16abaa3eab68c4640595c9658` |
| `experiments/prime_matrix_strict_named_return_after_rowfree_sync_router.py` | `3dbf0a518f4d199c46f930b53a3345bcbd983cf95b6681d17fb2625114790722` |
