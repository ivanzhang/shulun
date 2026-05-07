# Triad-A1 Canonical Branch Admission 路由审计

**状态：** `canonical_branch_admission_reduced_to_branch_statement_and_coverage`

A1CleanBranchCanonicalSourceAdmission 已被压成分支陈述与覆盖合同：canonical RIW/Buchstab 源头是合法子分支，且该子分支可接入内部支撑链；但当前 KZ-E 仍是 generic WFD 口径，所以必须明确声明 canonical 内部分支与 generic 外部分支的覆盖关系，不能静默把 generic 分支也标为内部闭合。

## 1. 分支陈述覆盖律

A1 clean branch canonical admission is not a numerical lemma. The current KZ-E/WFD statement is generic in well-factorable lambda_c, while the internal support chain is valid only for the canonical RIW/Buchstab source subcase. Therefore the proof must make an explicit branch statement: canonical-source clean branch is handled internally; generic noncanonical clean branch is handled only by external DI/BFI or returned to PDEC/SAE. This preserves the original target without silently claiming generic closure.

```text
current KZ-E/WFD statement: generic well-factorable lambda_c;
internal support proof: canonical RIW/Buchstab lambda_c only;
therefore:
  canonical source branch => internal support chain;
  generic noncanonical branch => external DI/BFI or PDEC/SAE;
no silent generic internal closure.
```

## 2. 汇总

- `source_lock_input_status=source_lock_contract_split_into_canonical_branch_admission_or_external_dibfi`。
- `source_lock_input_next_target=A1CleanBranchCanonicalSourceAdmission`。
- `current_kze_statement_is_generic_wfd=True`。
- `canonical_source_branch_is_legal_subcase=True`。
- `internal_canonical_branch_closed_conditionally=True`。
- `original_clean_object_covered_by_branch_split=False`。
- `canonical_branch_statement_adopted=False`。
- `next_internal_target=A1CanonicalSourceBranchStatementAndCoverage`。
- `terminal_gap_after_router=A1CanonicalSourceBranchStatementAndCoverageOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `CurrentKZEStatementIsGenericWFD` | KZ-E/WFD-core states lambda_c is well-factorable | recognize this is broader than canonical RIW/Buchstab source | none; current upstream text is generic in lambda_c | do not claim canonical admission from the generic statement | `True` |
| `CanonicalSourceBranchIsLegalSubcase` | RIW/Buchstab weights are valid well-factorable weights | the canonical branch is a legal subcase of KZ-E inputs | none; legality follows from the well-factorable algebra already recorded | restrict internal proof branch to lambda_c^RIW-tree | `True` |
| `InternalCanonicalBranchClosedConditionally` | previous routers close support chain on the canonical source branch | canonical admission feeds the A1 chain | none after canonical branch statement is adopted | canonical source branch => support chain => A1 clean internal branch | `True` |
| `OriginalCleanObjectCoveredByBranchSplit` | generic complement can go to external DI/BFI or PDEC/SAE | the proof statement explicitly covers both canonical and noncanonical clean objects | current ledger still needs a branch-statement update | state: canonical source branch uses internal proof; generic source branch uses external DI/BFI | `False` |
| `CanonicalBranchStatementAdopted` | all ingredients for the branch statement are now present | A1 theorem/ledger states the internal no-black-box branch is canonical-source only | this is a documentation/theorem-contract obligation, not a density estimate | update A1 clean theorem statement before claiming internal closure | `False` |
| `NoSilentGenericClosure` | generic WFD source was already shown insufficient for support | do not mark generic WFD branch internally closed | none after branch statement | generic branch remains ExternalDIBFIOriginalDispersion | `True` |

## 4. 结论

新最窄内部目标为：

```text
A1CanonicalSourceBranchStatementAndCoverage:
  state the canonical RIW/Buchstab clean branch as the internal no-black-box branch;
  state the generic noncanonical WFD branch as external DI/BFI or PDEC/SAE;
  then the canonical internal support chain is eligible for closure.
```

这仍不是行命题最终闭合；但它把分支准入硬点压成了主定理/账本陈述合同。
