# Prime Matrix strict no-return Rankin P^0.18 pass/return 同步路由器

**状态：** `no_return_rankin_p018_pass_return_schema_closed_sigma_failure_return_open`

no-return dyadic 块枚举器关闭后，`PrimitiveProductRankinP018InequalityTable` 的缺口不再是 h0/Y 字段来源，而是逐块 pass-or-return：每个枚举块必须给出 sigma 使 Rankin bound 不超过 P^0.18，否则必须附热窗口、共同核、PDEC/SAE、固定历史或 carrier-lcm return 的命名回流包。诊断样表已有失败行，因此不能只靠公式层宣称全部通过。本步关闭 pass/return schema，但不关闭 sigma 选择表、失败回流包或全局行/列命题。

```text
no_return_rankin_p018_pass_or_return_schema_closed=true
all_no_return_rankin_rows_pass_proved=false
per_block_rankin_sigma_selection_table_proved=false
primitive_product_rankin_failure_return_packet_ledger_closed=false
primitive_product_rankin_p018_inequality_table_present=false
row_column_unconditional_closed=false
```

## 1. Pass/Return 规则

| row_type | condition | effect |
| --- | --- | --- |
| rankin_pass | there exists an admitted sigma with rankin_bound(P,h0,Y,kernel,sigma)<=P^0.18 budget | block support is charged to primitive Rankin budget |
| rankin_return | all admitted sigma choices fail the P^0.18 budget, or kernel/profile is not primitive-clean | block must carry a return_packet |
| sigma_missing | block has h0/Y but no sigma selection or finite sigma grid certificate | route to PerBlockRankinSigmaSelectionTable |
| return_packet_missing | rankin_bound exceeds budget and return_packet is absent | route to PrimitiveProductRankinFailureReturnPacketLedger |
| global_return | source-defect or valuation-overflow branch | route to CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NoReturnEnumeratorImported` | `true` | `true` | no-return 分支已有 h0^car 和唯一 dyadic 产品块枚举规则。 | ActualDyadicColdProductBlockEnumeratorForH0 |
| `RankinFormulaAndProjectionImported` | `true` | `true` | 候选 d 的 primitive projection 与局部 Rankin/Euler 权重公式可用。 | PrimitiveProductRankinWeightP018Comparison |
| `P018PassReturnSchemaClosed` | `true` | `true` | 每个 no-return 枚举块必须二分为 pass 或带 return_packet 的失败行。 | NoReturnPrimitiveProductRankinP018PassOrFailureReturnTable |
| `DiagnosticFailRowsRequireReturn` | `true` | `true` | 诊断样表已有失败行，说明失败回流包是必要项。 | PrimitiveProductRankinFailureReturnPacketLedger |
| `AllNoReturnRankinRowsPassProved` | `false` | `false` | 尚未证明所有 no-return 枚举块都存在通过 P^0.18 的 sigma。 | PerBlockRankinSigmaSelectionTable |
| `PrimitiveProductRankinFailureReturnPacketLedgerClosed` | `false` | `false` | 尚未为所有失败块给出热窗口、共同核、PDEC/SAE 或固定历史回流包。 | PrimitiveProductRankinFailureReturnPacketLedger |
| `PrimitiveProductRankinP018InequalityTablePresent` | `false` | `false` | pass/return schema 已闭合，但缺全体块的 sigma/pass/return 实表。 | PerBlockRankinSigmaSelectionTable AND PrimitiveProductRankinFailureReturnPacketLedger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | PrimitiveProductRankinFailureReturnPacketLedger AND CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步

- 主攻：`PrimitiveProductRankinFailureReturnPacketLedger`。
- 并行保留：
  - `PerBlockRankinSigmaSelectionTable`
  - `CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption`
  - `SparseHistoryDemandExceedsNonpersistentSupplyBudget`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/primitive-product-rankin-p018-sample-table.json` | `6ee83fd827a289762f17da0e458cc1fb7fcfbe64b862d7b1fef635133f06e551` |
| `docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json` | `a2d4e9a4d5d5f8d377571fc39d9c94e1ddb97d2afae30ef9e4c9e18296677307` |
| `docs/monograph/prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json` | `3e4a65761bb62c0fff3f6614aedffd25ae31dda55b75295520a2eae1e3ce29ad` |
| `docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json` | `4c85ccfac092bb1ef772079cbf6adaa4c1f64f7b485b8d3ed2a71e2ea67422f9` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-p018-table-router.json` | `01ac5c80037d76d59f0d127041d9105c694a553da6cb5f6466928b73c67985f6` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json` | `2b1fa788ac82421045fe246cf635e7c945c68d6dee6b67a5e418c134120e940f` |
| `experiments/prime_matrix_strict_no_return_rankin_p018_pass_return_sync_router.py` | `87dd44a1a76ccfa8e857f46283fcec3af9c492ac8b0c05fed227c03993806be8` |
