# Triad-A1 PDEC 同集容量前沿路由器

**状态：** `same_set_capacity_frontier_materialized_terminal_dual_open`

Triad-A1 的 PDEC same-set capacity 已被压到一个明确前沿：当前合法行足以闭合零块子支并输出/路由 DualCap，连续方向弧也已精确物化为 persistent cap，但仍不足以给完整 U_CRT<L_PDEC。下一步必须提交 column/tail/cofactor 同集结构行，或把剩余平坦残差送入 CleanKLS。

## 1. 结构律

同集容量上界只允许作用在同一个 g(t) 上。当前 LHB 分支的 Attachment、零块容量行、DualCap 输出、P×P 出口和终端回流均已接线；box-only 行结构上不足，连续方向弧精确审计已排除离散采样不足这一退路；最终缺口变成 column/tail/cofactor 同集结构行，或 flat residual CleanKLS/DLS。

```text
Same-set capacity upper:
  only rows on the same g(t) are legal；
  box-only rows are insufficient；
  failure must output DualCap or missing row；
  routed DualCap returns to PDEC/LocalSurvivor/CleanKLS。
```

## 2. 汇总

- `all_known_frontiers_routed=True`。
- `terminal_dual_gap=ColumnTailCofactorOrCleanKLSStructureRows`。
- `status_counts={'closed': 1, 'closed_subbranch': 1, 'continuous_dualcap_materialized_not_closed': 1, 'dualcap_materialized': 1, 'no_fourth_exit': 1, 'ready_current_lhb_branch': 1, 'structurally_insufficient': 1}`。
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
remaining gap is column/tail/cofactor same-set structure or CleanKLS。
```

所以下一步唯一值得硬攻的 A1 目标是同集结构行：
把连续弧 persistent cap 与 column/tail/cofactor 非复用约束接起来，或证明其平坦残差进入 CleanKLS。
