# Triad-A1 Source Identification 路由审计

**状态：** `source_identification_reduced_to_canonical_source_lock_contract`

ActualKZESourceCoefficientIdentification 已被压成 canonical source lock 合同：必须证明 A1/KZ-E 实际 lambda_c 在进入 Cauchy/dispersion 前就等于 RIW/Buchstab 决策树系数；仅有 well-factorable 性质不够。若没有该锁定，内部支撑证明不可用，必须回 PDEC/SAE 或外部 DI/BFI。

## 1. 源头锁定律

Actual source identification cannot be replaced by the statement that lambda_c is well-factorable. The internal support chain applies only if the A1/KZ-E coefficient is locked to the canonical RIW/Buchstab decision-tree coefficient before dispersion and Cauchy steps. If the source is merely an arbitrary well-factorable coefficient, the earlier sparse formal-factor obstruction returns, so the block must exit to a missing-row/PDEC/SAE contract or use external DI/BFI original dispersion.

```text
well-factorable(lambda_c) is not enough;
internal support route requires:
  lambda_c == canonical RIW/Buchstab decision-tree coefficient
  before Cauchy/dispersion/source transformations;
if not locked:
  return to missing-row/PDEC/SAE or external DI/BFI.
```

## 2. 汇总

- `decision_tree_input_status=decision_tree_formula_reduced_to_source_coefficient_identification`。
- `decision_tree_input_next_target=ActualKZESourceCoefficientIdentificationOrCleanReturn`。
- `formal_wfd_source_rejected=True`。
- `conditional_source_lock_implies_internal_support_chain=True`。
- `source_identification_closed=False`。
- `next_internal_target=CanonicalRIWBuchstabSourceLockContract`。
- `terminal_gap_after_router=CanonicalRIWBuchstabSourceLockContractOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `FormalWFDSourceRejected` | previous routers showed formal WFD/Type/Fourier inputs do not force source entropy | do not identify lambda_c from well-factorability alone | none: this false shortcut has already been blocked | arbitrary well-factorable lambda_c cannot use canonical support proof | `True` |
| `CanonicalRIWBuchstabSourceLock` | decision-tree formula exists algebraically for canonical RIW/Buchstab weights | the actual A1/KZ-E lambda_c is declared and proved equal to that canonical coefficient | current A1 ledger still treats lambda_c as an exact source to be identified, not as a locked formula | add a source-lock contract before invoking the support chain | `False` |
| `SourceLockPreservesUpstreamBlocks` | dyadic/K6 bookkeeping and Type/Fourier wrappers already exist | locking lambda_c to the canonical tree does not change the upstream WFD/KZ-E object | must verify source-lock is not silently replacing the original target | show equality before Cauchy/dispersion, not after changing coefficients | `False` |
| `UnlockedSourceCleanReturn` | external DI/BFI and PDEC/SAE exits exist | if source lock is absent, clean A1 cannot use the internal support proof | the missing source-lock exit must be recorded as a clean failure | unlocked source returns to missing-row/PDEC/SAE or external DI/BFI | `False` |
| `SourceLockImpliesInternalSupportChain` | all downstream reductions from canonical source to support are conditional | source lock + path budget | conditional implication is direct; source lock remains | Canonical source lock feeds the already built decision-tree/support chain | `True` |

## 4. 结论

新最窄内部目标为：

```text
CanonicalRIWBuchstabSourceLockContract:
  prove the A1/KZ-E lambda_c is locked to the canonical RIW/Buchstab decision-tree coefficient;
  prove this lock preserves the original upstream WFD/KZ-E target;
  otherwise route to PDEC/SAE missing-row or external DI/BFI.
```

这仍不是行命题最终闭合；但它把源头识别硬点压成一个明确的合同检查。
