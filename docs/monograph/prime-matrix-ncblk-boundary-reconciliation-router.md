# Prime Matrix NC-BLK 边界核查路由器

**状态：** `ncblk_reconciled_with_canonical_boundary_global_not_closed`

NC-BLK 不是新的无名 CleanKLS 出口：在 canonical-source A1 分支中，它已经被既有同集容量最终边界吸收；在 generic full-S non-AP 分支中，它仍保持外部/精确源熵路线，不能冒充自足闭合。完整行/列无条件定理仍未闭合。

## 1. 边界核查律

NC-BLK must be read through the theorem boundary. On the canonical RIW/Buchstab source branch, the existing same-set capacity frontier and final boundary review have already absorbed the NC-BLK clean-KLS chain. On the broader full-S non-AP generic WFD branch, NC-BLK is still an external/exact-source-entropy route and must not be imported into the self-contained claim. Therefore this reconciles the NC-BLK label but does not close the full row/column theorem.

```text
canonical source branch:
  NC-BLK clean-KLS chain is absorbed by the existing same-set capacity boundary;
generic full-S non-AP branch:
  NC-BLK remains exact source entropy or external DI/BFI/Kuznetsov;
therefore:
  no unnamed CleanKLS exit remains, but the global row/column theorem is not closed.
```

## 2. 汇总

- `all_reconciliation_gates_passed=true`。
- `canonical_ncblk_absorbed_by_existing_boundary=true`。
- `generic_ncblk_self_contained_not_claimed=true`。
- `row_column_unconditional_closed=false`。
- `row_frontier_before_reconciliation=CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen`。

## 3. 核查表

| gate | closed | evidence | meaning |
| --- | --- | --- | --- |
| `RowFrontierPinsNCBLK` | `true` | frontier=CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen; clean_kls_status=ncblk_reconciled_with_boundary_global_family_open | 总前沿已把 CleanKLS 宽口径压到 NC-BLK，并在升级后记录为已核查边界。 |
| `CanonicalSameSetBoundaryClosed` | `true` | NoFurtherCanonicalSourceSelfContainedGap_GenericUnrestrictedRefuted | canonical RIW/Buchstab source branch 的同集容量/Full-S 终端已闭合。 |
| `BoundaryReviewNoOpenGate` | `true` | self_contained_theorem_boundary_review_passed | 定理边界审查无剩余门。 |
| `GenericUnrestrictedNotImported` | `true` | Unrestricted generic full-S well-factorable WFD self-contained theorem. | generic WFD 自足版保持反证，不能偷渡进 canonical 闭合。 |
| `NCBLKGenericBranchStillExternal` | `true` | ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov | full-S non-AP generic NC-BLK 仍只能走 exact source entropy 或外部定理。 |
| `NoGlobalRowColumnUpgrade` | `true` | PDEC family certificates, LocalSurvivorCert family, CleanKLS/DLS certificates or explicit ExternalKLS input, D-structure/Tail-log4/Rankin/referee-block interfaces | 完整行/列无条件定理仍需独立终端证书，不能由 canonical 边界替代。 |

## 4. 剩余全局义务

- `PDEC family certificates`
- `LocalSurvivorCert family`
- `CleanKLS/DLS certificates or explicit ExternalKLS input`
- `D-structure/Tail-log4/Rankin/referee-block interfaces`
