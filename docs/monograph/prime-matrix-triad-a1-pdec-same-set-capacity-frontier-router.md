# Triad-A1 PDEC 同集容量前沿路由器

**状态：** `same_set_capacity_frontier_materialized_terminal_dual_open`

Triad-A1 的 PDEC same-set capacity 已被压到一个明确前沿：当前合法行足以闭合零块子支并输出/路由 DualCap，连续方向弧也已精确物化为 persistent cap，连续 cap 已接入 column-tail 暴露账本，且 canonical actual payment measure 已精确构造。终端二分已说明没有第三出口；下一步不再是路由，而是证明 PDEC-CAP 或 KLS-EXT。

## 1. 结构律

同集容量上界只允许作用在同一个 g(t) 上。当前 LHB 分支的 Attachment、零块容量行、DualCap 输出、P×P 出口和终端回流均已接线；box-only 行结构上不足，连续方向弧精确审计已排除离散采样不足这一退路；连续 cap 也已接到 column-tail 暴露账本。actual payment measure 已由 canonical 选择律构造，终端投影塔二分也已闭合。最终缺口只剩 PDEC 容量不等式或 CleanKLS/DLS 大筛估计。

```text
Same-set capacity upper:
  only rows on the same g(t) are legal；
  box-only rows are insufficient；
  failure must output DualCap or missing row；
  continuous cap exposes column-tail payment buckets；
  canonical actual payment measure is constructed；
  actual payment concentration returns to PDEC；
  recursive diffusion returns to CleanKLS/DLS；
  no third terminal route remains after finite-projection dichotomy。
```

## 2. 汇总

- `all_known_frontiers_routed=True`。
- `terminal_dual_gap=PDECCapacityOrKLSLargeSieve`。
- `status_counts={'actual_payment_measure_constructed': 1, 'actual_payment_selection_materialized': 1, 'closed': 1, 'closed_subbranch': 1, 'continuous_dualcap_materialized_not_closed': 1, 'dualcap_materialized': 1, 'no_fourth_exit': 1, 'ready_current_lhb_branch': 1, 'structurally_insufficient': 1, 'terminal_dichotomy_admission_closed_capacity_open': 1}`。
- `lp_summary={'q': 2310, 'p_count': 9, 'all_zero_blocks_ready': True, 'box_only_global_closure': False, 'box_only_obstruction_count': 9, 'row_generators_ready': ['nonnegativity', 'phase_caps_g_le_M', 'WHOLEDEF_zero_block', 'BRIDGED_zero_block']}`。
- `fourier_summary={'q': 2310, 'p_count': 9, 'class_counts': {'EmptyCap': 8267, 'PersistentCap': 192813, 'SparseCap': 48292}, 'has_persistent_cap': True}`。
- `dualcap_summary={'aggregate_class_counts': {'ForcedPersistentByDensityBarrier': 24, 'PersistentCap': 68, 'SparseCap': 16}, 'aggregate_route_counts': {'LiftOrColumnTailOrCleanKLS': 24, 'LocalSurvivorOrExplicitPDEC': 16, 'RefinedPDECOrColumnTailRows': 68}}`。

## 3. 前沿表

| frontier | status | evidence | next action |
| --- | --- | --- | --- |
| `SameSetAttachment` | `ready_current_lhb_branch` | 当前 DualCap 三族都有同一 M_Q 质量来源。 | 新 formal PDEC 分支仍必须先证明 S subset Z_theta。 |
| `ZeroBlockCapacityRows` | `closed_subbranch` | WHOLEDEF/BRIDGED 与 supp(M) 交集为空。 | 真实 PDEC 方向若落在零块并集，该 LHB 分支直接空。 |
| `BoxOnlyCapacity` | `structurally_insufficient` | 9 个 P 都存在单相位 box-only 可行见证。 | 必须补方向、column/tail/cofactor、NoDeletion-KL 或 CleanKLS 行。 |
| `FourierCapDualFailure` | `dualcap_materialized` | class_counts={'ForcedPersistentByDensityBarrier': 24, 'PersistentCap': 68, 'SparseCap': 16}；route_counts={'LiftOrColumnTailOrCleanKLS': 24, 'LocalSurvivorOrExplicitPDEC': 16, 'RefinedPDECOrColumnTailRows': 68}。 | SparseCap 进 LocalSurvivor；Persistent/Forced 进 refined PDEC、升层或 CleanKLS。 |
| `CurrentPXPExit` | `closed` | 当前 DualCap 的 P×P 早期出口由 SparseLocalSurvivor/BTLS/LFTE 接住。 | 剩余不是 P 行出口，而是终端 PDEC/LocalSurvivor/CleanKLS 证书。 |
| `TerminalConfluence` | `no_fourth_exit` | APS、DualCap、升层删除、NoDeletion-KL、promotion 均汇入三终端。 | 直接攻三终端证书；首要为 PDEC same-set U_CRT<L_PDEC。 |
| `ContinuousDirectionArcDual` | `continuous_dualcap_materialized_not_closed` | 连续方向弧精确审计已提交；route_counts={'PersistentContinuousDualCapNeedsColumnTailOrCleanKLS': 8, 'SparseContinuousDualCapToLocalSurvivor': 1}；max U_box/M=0.998391。 | 方向采样退路关闭；下一步补 column/tail/cofactor 同集结构行或转 CleanKLS。 |
| `ContinuousColumnTailBridge` | `actual_payment_selection_materialized` | 连续 cap 已接到 column-tail 暴露账本；route_counts={'ContinuousCapActualPaymentSelectionDichotomy': 8, 'NoTailDemandSparseOrLocalSurvivor': 1}；all_cap_recomputations_match=True。 | 从暴露候选桶提升到真实支付测度：集中给 PDEC，递归扩散给 CleanKLS/DLS。 |
| `ContinuousActualPaymentSelection` | `actual_payment_measure_constructed` | canonical actual payment measure 已构造；route_counts={'ActualPaymentMeasureDichotomySubmitted': 8, 'NoTailDemandSparseOrLocalSurvivor': 1}；all_payment_counts_match_demand=True。 | 终端只剩两引理：positive-limsup finite signature=>PDEC；diffuse=>CleanKLS/DLS。 |
| `ContinuousTerminalDichotomy` | `terminal_dichotomy_admission_closed_capacity_open` | 终端二分已路由；route_counts={'NoTailDemandSparseOrLocalSurvivor': 1, 'PositiveLimsupPDECOrDiffuseCleanKLSDichotomy': 8}；open=['PDEC-CAP: prove the resulting column-tail PDEC capacity inequality U_CRT<L_PDEC', 'KLS-EXT: prove or import the CleanKLS/DLS large-sieve bound for diffuse payment measures']。 | 直接攻 PDEC-CAP 容量不等式，或攻/引用 KLS-EXT 大筛估计。 |

## 4. 当前结论

A1 的同集容量上界已经不再是一个模糊缺口。当前状态是：

```text
Attachment ready for current LHB branch；
zero-block subbranch closed；
box-only structurally insufficient；
DualCap materialized and routed；
P×P exits closed；
no fourth exit in current A1 chain；
continuous direction-arc dual materialized but not closed；
continuous column-tail bridge materialized；
canonical actual payment measure constructed；
terminal finite-projection dichotomy closed；
remaining gap is PDEC-CAP or KLS-EXT。
```

所以下一步唯一值得硬攻的 A1 目标是同集结构行：
直接证明 column-tail PDEC 容量不等式，或证明/接入 diffuse CleanKLS/DLS 大筛估计。
