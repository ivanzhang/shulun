# Prime Matrix strict 回流后冷供给数值包同步路由器

**状态：** `cold_supply_numeric_after_return_cycle_reduced_to_core_pdec_tables_open`

`ColdSupplySameParameterNumericEnvelope` 已同步到共同核回流关闭后的前沿。旧的有效剪枝阻塞不再是一个免费循环：终端冷窗口反级联失败、兄弟超收费、collar 宽度爆发、低乘子共同核回流都会进入热核心、固定历史、PDEC/SAE 或统一预算扣减，不能继续算入纯非持久冷供给。因此在非持久预算侧，真正剩余压成两个数值表：`ColdCoreThresholdFunctionNumericTable` 和 `SameParameterPDECThresholdNumericTable`。本步不排斥热/固定/持久出口，也不证明最终数值反超。

```text
cold_numeric_target_imported=true
cold_supply_formula_sync_imported=true
effective_pruning_structural_sync_imported=true
no_free_return_cycle_imported=true
effective_pruning_closed_for_nonpersistent_budget=true
cold_core_threshold_numeric_table_proved=false
same_parameter_pdec_threshold_numeric_table_proved=false
cold_supply_same_parameter_numeric_envelope_proved=false
row_column_unconditional_closed=false
```

## 1. 剪枝失败出口

| failure mode | route | budget effect |
| --- | --- | --- |
| terminal cold-window anti-cascade fails | sibling charging / collar width LCM / low-kernel return | cannot remain in U_np after no-free-return-cycle |
| sibling family overcharges parent cold support | hot core or fixed history | counted as named return, not cold supply |
| collar width explosion | LCM height or common-kernel return | LCM/common-kernel branch is charged, not free |
| all named returns absent | genuinely cold nonpersistent histories only | remaining task is numeric C_core/T_PDEC summation |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ColdNumericTargetImported` | `true` | `true` | 回流后同参数余量已把主攻点指向冷供给数值包。 | ColdSupplySameParameterNumericEnvelope |
| `ColdSupplyFormulaSyncImported` | `true` | `true` | 旧冷供给公式和同参数调参纪律可用。 | ColdSupplySameParameterNumericEnvelope |
| `EffectivePruningStructuralSyncImported` | `true` | `true` | 有效剪枝已通过小素数幂、fan-in、稀疏终端和兄弟收费链同步到最新前沿。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem |
| `NoFreeReturnCycleImported` | `true` | `true` | 共同核/LCM/collar 回流不能作为免费冷供给循环。 | CommonKernelReturnCycleDescentOrPDECLedger |
| `EffectivePruningClosedForNonpersistentBudget` | `true` | `true` | 剪枝失败均进入命名出口或预算扣减；纯非持久 U_np 只剩真正冷历史。 | ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable |
| `ColdCoreThresholdNumericTableProved` | `false` | `false` | 仍缺同参数 C_core(W) 的可求和数值表。 | ColdCoreThresholdFunctionNumericTable |
| `SameParameterPDECThresholdNumericTableProved` | `false` | `false` | 仍缺同参数 T_PDEC(W) 的阈值数值表。 | SameParameterPDECThresholdNumericTable |
| `ColdSupplySameParameterNumericEnvelopeProved` | `false` | `false` | 预算版剪枝关闭后，真正剩余是 C_core/T_PDEC 数值表与并行命名出口排斥。 | ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步最窄点

- 主攻：`ColdCoreThresholdFunctionNumericTable`。
- 并行：`SameParameterPDECThresholdNumericTable`、热核心/固定历史、moving atom 与 DStructure。
- 边界：本步关闭预算版有效剪枝，不提交 C_core/T_PDEC 数值表。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json` | `86ba2fbc9abd9d917a940525fde0a9db0dd4e70ee94f745a56382fee896d8255` |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-effective-pruning-latest-sync-router.json` | `ed70b01806e4ff545cc7ab3d3d051009e33cf6e1e43190141f5278ed9d73c126` |
| `docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json` | `10d6c849cdb719344db932e7cfbf6f7f94ba66f26b28f0f3bb5f73d5d5df778d` |
| `docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json` | `c7265153d74715fc941d430ceb1307996ffff0955769b5d84660464dc7f90faa` |
| `docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json` | `973a1c986598cb27dd132354715b336eae7938103c89d09da451123f2ade08de` |
| `docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json` | `c2ef211342a04f992f35f62a595d3c1647663d1a9fde5d1e78ff57c735bf63d6` |
| `experiments/prime_matrix_strict_cold_supply_numeric_after_return_cycle_router.py` | `951960f340951767524952cda051b0ff23bc1c082482aa909c66f5e3fea04cc6` |
