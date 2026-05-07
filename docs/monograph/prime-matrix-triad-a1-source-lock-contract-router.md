# Triad-A1 Source Lock Contract 路由审计

**状态：** `source_lock_contract_split_into_canonical_branch_admission_or_external_dibfi`

CanonicalRIWBuchstabSourceLockContract 已被严格二分：canonical 源头分支上，source lock 按定义成立并可接入此前完整内部支撑链；generic well-factorable 分支不能偷用该链，必须走外部 DI/BFI 或回 PDEC/SAE。剩余内部目标只剩证明当前 A1 clean 分支确实属于 canonical RIW/Buchstab source branch。

## 1. 分支锁定二分律

The source-lock contract is resolved as a rigorous branch split. The internal support chain is valid on the canonical RIW/Buchstab source branch, where lambda_c is defined as the decision-tree coefficient before any Cauchy or dispersion operation. It is not valid for a generic well-factorable WFD theorem. The complement is not ignored: a noncanonical source must go to external DI/BFI original dispersion or a PDEC/SAE missing-row return. Thus the only remaining internal obligation is branch admission: prove the A1 clean branch under attack is the canonical source branch.

```text
if lambda_c is the canonical RIW/Buchstab decision-tree coefficient:
  source lock is definitional;
  internal support chain applies;
else:
  generic well-factorable WFD cannot use canonical support;
  route to external DI/BFI or PDEC/SAE missing-row.
```

## 2. 汇总

- `source_identification_input_status=source_identification_reduced_to_canonical_source_lock_contract`。
- `source_identification_input_next_target=CanonicalRIWBuchstabSourceLockContract`。
- `canonical_source_branch_defined=True`。
- `branch_split_preserves_original_target=True`。
- `source_lock_contract_closed_for_canonical_branch=True`。
- `global_internal_a1_closed=False`。
- `next_internal_target=A1CleanBranchCanonicalSourceAdmission`。
- `terminal_gap_after_router=A1CleanBranchCanonicalSourceAdmissionOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `GenericWFDNotEligibleForInternalSupport` | formal WFD source has already been rejected as insufficient | generic well-factorable lambda_c must not enter the canonical support chain | none; this prevents a false closure | generic WFD branch uses external DI/BFI original dispersion | `True` |
| `CanonicalSourceBranchDefinition` | KZ-E spine notes RIW/Buchstab weights may be used as algebraic definition | define the internal branch object with lambda_c := lambda_c^RIW-tree before Cauchy/dispersion | definition must be explicit in the A1 ledger | create a canonical source branch, not a generic WFD theorem | `True` |
| `BranchSplitPreservesOriginalTarget` | two legal routes exist: canonical internal support or generic external DI/BFI | the split must not replace a generic theorem by a narrower one without routing the complement | must record that noncanonical source exits to external DI/BFI/PDEC | prove a dichotomy: canonical source branch or generic WFD branch | `True` |
| `A1CleanBranchCanonicalAdmission` | current ledger wants the actual A1/KZ-E source identified | the clean A1 branch under attack is admitted into the canonical RIW/Buchstab source branch | this is now the only internal branch-admission obligation | show the original row/triad clean construction chooses the canonical source weight | `False` |
| `CanonicalBranchFeedsSupportChain` | all previous routers are conditional on canonical source lock | once admitted, the internal support chain applies without further source ambiguity | conditional implication is direct | canonical branch => decision-tree support => factor support => A1 chain | `True` |
| `NoncanonicalBranchExternalReturn` | external DI/BFI route is already registered | if A1 clean branch is not canonical, no internal support proof is claimed | none after branch split | route to ExternalDIBFIOriginalDispersion or PDEC/SAE missing-row | `True` |

## 4. 结论

新最窄内部目标为：

```text
A1CleanBranchCanonicalSourceAdmission:
  prove the clean A1 branch under attack uses the canonical RIW/Buchstab source weight;
  then the complete internal support chain applies;
  otherwise route to external DI/BFI or PDEC/SAE.
```

这仍不是行命题最终闭合；但 source lock 本身已转化为严格分支准入问题。
