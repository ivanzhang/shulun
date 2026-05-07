# Triad-A1 Path Partition / No-Cancellation 路由审计

**状态：** `finite_signature_no_cancellation_reduced_to_exact_decision_tree_or_clean_return`

FiniteSignatureNoCancellation 已被压缩为 exact RIW/Buchstab 决策树公式问题：若签名细化到完整分支轨迹，则路径天然互斥，同一路径系数非零，无抵消随结构闭合。真正剩余是把 canonical 筛权逐项写成该完整决策树，并证明完整路径数仍在 K6 polylog 预算内；失败块必须回到 PDEC/SAE。

## 1. 决策树无抵消律

No-cancellation is not a new analytic estimate after the full path signature is fixed. A Buchstab/RIW expansion can be made into a decision tree: the complete trace records the ordered branch choices, parity and truncation state. Complete traces are disjoint, and a same-trace coefficient is a nonzero product of local branch factors. Therefore the remaining obligation is to write the exact canonical coefficient formula as such a complete decision-tree partition within the polylog signature budget, or to return over-budget/non-disjoint/cancelling blocks to existing clean exits.

```text
refine signature to the complete RIW/Buchstab decision trace;
complete traces are disjoint by deterministic branch history;
same-trace coefficient is a nonzero product of local branch factors;
therefore no-cancellation is structural, not spectral;
remaining issue: exact formula + path-count budget, or clean return.
```

## 2. 汇总

- `selector_input_status=selector_retention_reduced_to_finite_signature_no_cancellation_or_clean_return`。
- `selector_input_next_target=FiniteSignatureNoCancellationOrCleanReturn`。
- `all_path_rows_suffice=True`。
- `conditional_decision_tree_implies_no_cancellation=True`。
- `finite_signature_no_cancellation_closed=False`。
- `next_internal_target=ExactRIWDecisionTreeFormulaOrCleanReturn`。
- `terminal_gap_after_router=ExactRIWDecisionTreeFormulaOrCleanReturnOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `CompleteDecisionTraceSignature` | finite signatures exist as labels in the previous router | signature records the full RIW/Buchstab branch trace: ordered primes, parity, dyadic bin and truncation | current label may be coarser than the exact coefficient path | refine the signature until every coefficient contribution has one complete trace | `False` |
| `DisjointPathPartition` | Buchstab recursion is a deterministic decision tree after a full trace is fixed | each squarefree product lies in at most one selected complete trace | none once CompleteDecisionTraceSignature is fixed | use ordered least-new-prime / branch-state uniqueness | `True` |
| `SamePathNonzeroCoefficient` | a complete trace has a fixed sign/parity and nonzero local factors | no cancellation inside one complete path support | none once coefficients are written as path weights with nonzero local factors | coefficient on a path is a nonzero product of local branch factors | `True` |
| `FullSignatureCountBudget` | K6/tail-label bookkeeping gives a polylog count | the complete trace count remains <= log^J with E+J<=C | coarse labels may hide extra trace states; the full count must be recorded | charge extra trace states to K6; if the budget is exceeded, return to tail-label/PDEC | `False` |
| `NonDecisionTreeCleanReturn` | edge/PDEC/SAE exits exist | failure of complete disjoint path formula exits clean A1 | the contrapositive clean contract is not yet stated | non-disjoint, cancelling or over-budget traces are named clean failures | `False` |
| `PathPartitionImpliesNoCancellation` | disjoint partition + nonzero same-path coefficient | FiniteSignatureNoCancellationOrCleanReturn | conditional implication is direct; exact formula/budget/return remain | combine complete traces with full signature budget | `True` |

## 4. 完整路径预算模型

| k | log y | raw support | full signatures | selected path support | required support | suffices |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 15728.4 | 6.90776 | 2276.92 | 2276.92 | `True` |
| 4 | 9.21034 | 66279.4 | 9.21034 | 7196.19 | 7196.19 | `True` |
| 5 | 11.5129 | 202269 | 11.5129 | 17568.8 | 17568.8 | `True` |
| 6 | 13.8155 | 503309 | 13.8155 | 36430.7 | 36430.7 | `True` |
| 7 | 16.1181 | 1.08785e+06 | 16.1181 | 67492.4 | 67492.4 | `True` |
| 8 | 18.4207 | 2.12094e+06 | 18.4207 | 115139 | 115139 | `True` |
| 9 | 20.7233 | 3.822e+06 | 20.7233 | 184431 | 184431 | `True` |

## 5. 结论

新最窄内部目标为：

```text
ExactRIWDecisionTreeFormulaOrCleanReturn:
  write the canonical RIW/Buchstab coefficients as a complete disjoint decision-tree expansion;
  prove the complete trace count stays within the K6/polylog budget;
  otherwise return over-budget/non-disjoint/cancelling blocks to edge/PDEC/SAE.
```

这仍不是行命题最终闭合；但它把无抵消从解析难题降为 exact 系数公式和 clean 准入合同。
