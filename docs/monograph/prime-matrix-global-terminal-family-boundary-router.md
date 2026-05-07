# Prime Matrix 全局终端家族边界路由器

**状态：** `materialized_frontier_exhausted_terminal_family_exclusion_open`

当前已物化前沿已经耗尽：PDEC 侧无合法非二点候选，LocalSurvivor 侧无开放包，已知 sparse 入口全部准入，NC-BLK 已与 canonical-source 边界核查对齐。因此下一硬点不再是局部样本或固定常数，而是全局终端家族排斥证书：必须证明所有未来 PDEC/LocalSurvivor/CleanKLS-DLS 终端对象都被证书排除，或明确调用外部/referee 输入。完整行/列无条件定理仍未闭合。

## 1. 边界律

The current materialized ledger has no remaining local terminal instance to eliminate: the non-tautological primitive PDEC candidate count is zero, the materialized LocalSurvivor ledger has no open packet, all known sparse entry routes are admitted, and NC-BLK has been reconciled with the canonical boundary. This proves a boundary statement, not the full row/column theorem: a future counterexample can only survive by producing a genuinely new global terminal family certificate obligation or by using an accepted external/referee input.

```text
current materialized frontier:
  PDEC current non-tautological primitive candidates = 0;
  LocalSurvivor open materialized packets = 0;
  known sparse entry routes admitted = true;
  NC-BLK reconciled with canonical boundary = true;
therefore:
  local materialized frontier is exhausted;
  remaining proof target = global terminal family exclusion certificates.
```

## 2. 汇总

- `materialized_frontier_exhausted=true`。
- `terminal_generation_contract_closed=true`。
- `current_terminal_instances_exhausted=true`。
- `global_terminal_family_exclusion_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=GlobalTerminalFamilyExclusionCertificates`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `CurrentMaterializedFrontierExhausted` | `true` | `false` | name=CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen; subgate=NoCurrentMaterializedNonTautologicalPDECAndNCBLKReconciled | 当前机器总账能触及的 PDEC、LocalSurvivor 与 NC-BLK 局部硬点已耗尽。 |
| `TerminalTriadGenerationContract` | `true` | `false` | PDEC / LocalSurvivor / CleanKLS-DLS; no fourth exit | 在已列上游合同内，任何最小反例必须进入三类终端证书之一。 |
| `CurrentPDECAdmissionEmpty` | `true` | `false` | candidate_count=0; frontier_status=current_materialized_nontautological_pdec_absent_global_family_open | 当前已物化的合法非二点 primitive PDEC 候选为零；未来候选需重新准入。 |
| `CurrentLocalSurvivorAndSparseEntryGuarded` | `true` | `false` | open_materialized=0; missing_extractors=0; missing_admission=0; frontier_status=materialized_packets_closed_global_generation_open | 当前已物化孤窗包清零，已知入口均有 extractor 或合同准入。 |
| `NCBLKBoundaryReconciled` | `true` | `false` | ncblk_reconciled=True; frontier_status=ncblk_reconciled_with_boundary_global_family_open | NC-BLK 已从无名 CleanKLS 出口改写为 canonical 吸收或 generic 外部路线。 |
| `GlobalTerminalFamilyExclusion` | `false` | `true` | PDEC family certificates, LocalSurvivorCert family, CleanKLS/DLS certificates or explicit ExternalKLS input, D-structure/Tail-log4/Rankin/referee-block interfaces | 仍未提交全部 PDEC、LocalSurvivor 与 CleanKLS/DLS 家族证书或外部输入。 |
| `DStructureRankinRefereePromotion` | `false` | `true` | BLOCK-REFEREE | D-structure/Tail-log4/finite Rankin 接口仍需独立逐行审稿接受。 |
| `ClaimStatusNoOverclaim` | `true` | `false` | CANONICAL_SOURCE_BOUNDARY_MERGED_NO_GLOBAL_OVERCLAIM | 状态表继续区分已闭合边界、已反证强化版和未闭合全局命题。 |

## 4. 下一条必须证明的定理

For every minimal counterexample, the emitted terminal object must be certified by a PDEC-family exclusion, a LocalSurvivor witness/deficit certificate, or a CleanKLS/DLS/internal-large-sieve certificate; otherwise the branch must route to an explicitly accepted external/referee input.

这个路由器的结论不是最终无条件证明。它关闭的是“当前已物化前沿还有可继续局部消元的对象”这一可能；剩余是全局终端家族全集的排斥或外部/referee 接口接受。
