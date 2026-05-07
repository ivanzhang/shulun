# Triad-A1 Branch Statement Coverage 路由审计

**状态：** `canonical_source_branch_statement_adopted_generic_wfd_external_only`

A1CanonicalSourceBranchStatementAndCoverage 已落实为显式二分陈述：canonical RIW/Buchstab source branch 走内部支撑链，generic noncanonical WFD branch 不再假装内部闭合，只保留外部 DI/BFI 或 PDEC/SAE 路由。因此 canonical 源头分支的 source-lock 终端已闭合；剩余外部缺口只属于 broader generic WFD 版本。

## 1. 显式分支陈述

The branch statement is now explicit. The no-black-box internal A1 clean proof is a canonical-source statement: lambda_c must be the canonical RIW/Buchstab decision-tree coefficient. The generic noncanonical well-factorable WFD branch is not silently upgraded; it remains an external DI/BFI original-dispersion branch or returns to PDEC/SAE. Thus the source-lock terminal is closed for the canonical branch, while the broader generic WFD theorem remains external.

```text
canonical branch:
  lambda_c = canonical RIW/Buchstab decision-tree coefficient;
  internal support chain applies;

generic noncanonical WFD branch:
  no internal support closure claimed;
  use external DI/BFI or PDEC/SAE;

there is no silent generic upgrade.
```

## 2. 汇总

- `canonical_branch_input_status=canonical_branch_admission_reduced_to_branch_statement_and_coverage`。
- `canonical_branch_input_next_target=A1CanonicalSourceBranchStatementAndCoverage`。
- `canonical_internal_branch_statement_adopted=True`。
- `generic_complement_statement_adopted=True`。
- `coverage_no_overlap_no_gap=True`。
- `canonical_source_branch_internal_gap_closed=True`。
- `generic_wfd_self_contained_gap_closed=False`。
- `next_internal_target=NoFurtherInternalGapForCanonicalSourceBranch`。
- `terminal_gap_after_router=ExternalDIBFIOriginalDispersionForGenericWFDBranchOnly`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `CanonicalInternalBranchStatement` | canonical source branch is legal and all downstream support routers are conditional | state internal no-black-box branch only for lambda_c^RIW-tree | none after this branch statement is adopted | canonical RIW/Buchstab source branch uses internal support chain | `True` |
| `GenericComplementStatement` | generic WFD source is broader than canonical source | state generic noncanonical branch is not internally closed | none after this branch statement is adopted | generic WFD branch uses ExternalDIBFIOriginalDispersion or PDEC/SAE | `True` |
| `CoverageNoOverlapNoGap` | source is either canonical RIW/Buchstab or noncanonical | the two branches cover the source alternatives | none by source dichotomy | canonical vs noncanonical source dichotomy | `True` |
| `NoSilentGenericUpgrade` | generic WFD source failed the support route | do not claim self-contained closure for generic WFD | none after explicit branch statement | generic closure requires external DI/BFI | `True` |
| `CanonicalBranchInternalGap` | canonical source branch feeds all previous internal routers | no remaining source-lock/selector/support gap on canonical branch | none in the current routed chain | source branch statement closes the source-lock terminal for canonical branch | `True` |
| `GenericSelfContainedGap` | external DI/BFI route is registered | generic WFD self-contained proof if one wants the broader theorem | still external/deep; not solved by canonical branch | ExternalDIBFIOriginalDispersion | `False` |

## 4. 结论

当前 canonical-source 内部分支已经没有 source-lock 链条上的剩余缺口：

```text
NoFurtherInternalGapForCanonicalSourceBranch
```

若仍要求 generic WFD 版本完全自足，剩余只能是：

```text
ExternalDIBFIOriginalDispersionForGenericWFDBranchOnly
```

这不等于宣称全部行命题无条件闭合；它说明本轮 source-lock 终端在 canonical 源头分支上已经闭合，generic WFD 宽口径仍需外部深定理或另行攻关。
