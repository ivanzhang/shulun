# Triad-A1 终端汇合路由器

**状态：** `a1_current_branches_confluent_to_terminal_triad_not_closed`

A1 当前所有物化分支已汇合到终端三证书接口，且当前 P×P 早期出口已关闭。这仍不是最终行命题证明；剩余是三终端证书全集，首要是 PDEC 同集容量上界。

## 1. 汇合律

当前 A1 物化链中，ActualPayment 持久性、PDEC DualCap、同集容量前沿、升层删除势、NoDeletion-KL 和 top-prime promotion 均已路由到 PDEC/LocalSurvivor/CleanKLS 三终端。失败只会回流到三终端内部，不生成第四出口。

```text
Persistent actual Gamma => A:PDEC；
Sparse/DualCap sparse   => B:LocalSurvivor or A:PDEC；
FiberDeletion diverges  => B:LocalSurvivor / capacity contradiction；
NoDeletion + KL/MI bias => A:PDEC；
NoDeletion + flat       => C:CleanKLS/DLS。
```

## 2. 总计

- `all_current_pxP_exits_closed=True`。
- `all_materialized_branches_routed_to_terminal_triad=True`。
- `no_fourth_exit_current_a1_chain=True`。
- `triad_counts={'A/B/C': 1, 'A:PDEC': 3, 'A:PDEC-or-C:CleanKLS': 1, 'B:LocalSurvivor-or-A:PDEC': 1, 'B:LocalSurvivor-or-A:PDEC-or-C:CleanKLS': 3, 'C:CleanKLS': 1, 'C:CleanKLS-or-A:PDEC': 1}`。
- `status_counts={'current_layers_all_deleting': 1, 'known_frontiers_routed_dual_open': 1, 'mass_source_and_pxP_exit_closed': 3, 'materialized_gates_pass': 1, 'not_currently_visible': 1, 'positive_current_layer': 1, 'routed': 2, 'routed_before_clean_terminal': 1}`。

## 3. 义务明细

| name | triad | route | status | P×P closed | remaining |
| --- | --- | --- | --- | --- | --- |
| APS persistent actual Gamma | `A:PDEC` | `PersistentGammaFiniteSignatureToMFUPDEC` | `routed` | `True` | 证明持久 actual Gamma 签名的同集 PDEC 容量上界。 |
| APS no persistent actual Gamma | `C:CleanKLS-or-A:PDEC` | `SmallAmbiguousSuccessor` | `routed_before_clean_terminal` | `True` | 删除势继续则升层；NoDeletion 偏斜则 PDEC；NoDeletion 平坦才 CleanKLS。 |
| small ambiguous current successor | `B:LocalSurvivor-or-A:PDEC-or-C:CleanKLS` | `CurrentLayerFiberDeletionOrNoDeletionPhaseResiduePDEC; CleanKLSOnlyAfterFlatNoDeletion` | `routed` | `True` | 当前层由 FiberDeletion 推进；若删除停止，KL/MI 偏斜回流 PDEC，KL/MI 平坦才进入 CleanKLS。 |
| small ambiguous clean visibility | `C:CleanKLS` | `CleanKLSOnlyAfterFlatNoDeletion` | `not_currently_visible` | `True` | 未来 clean 输入必须提交 KLS/DLS admission 与大筛证书。 |
| PDEC SparseCap | `B:LocalSurvivor-or-A:PDEC` | `SparseLocalSurvivorOrFinitePDEC` | `mass_source_and_pxP_exit_closed` | `True` | finite PDEC packet beyond P; no P-row exit in current sparse atoms. |
| PDEC PersistentCap | `A:PDEC` | `BoundarySubsetBTLS` | `mass_source_and_pxP_exit_closed` | `True` | ColumnTail/TailAnchor PDEC or distributed CleanKLS/DLS. |
| PDEC ForcedPersistentByDensityBarrier | `A:PDEC-or-C:CleanKLS` | `BoundarySubsetBTLS plus lift monotonicity` | `mass_source_and_pxP_exit_closed` | `True` | next lift, column-tail rows, PDECEntropy, or CleanKLS. |
| PDEC same-set capacity frontier | `A:PDEC` | `SameSetCapacityFrontierToContinuousDirectionArcDual` | `known_frontiers_routed_dual_open` | `True` | Attachment/零块/DualCap/P×P/终端回流已接线；仍需提交 ContinuousDirectionArcDual 或更窄 column/tail/cofactor DualCap。 |
| new-layer terminal router | `B:LocalSurvivor-or-A:PDEC-or-C:CleanKLS` | `LiftFiberDeletionOrNoDeletionTriad` | `current_layers_all_deleting` | `True` | 删除势发散则 Sparse/LocalSurvivor 或容量矛盾；删除势停止则 PDEC/CleanKLS。 |
| A1 middle no-cycle gates | `A/B/C` | `NoMiddleEscapeNoSameLayerCycle` | `materialized_gates_pass` | `True` | 仍需提交 PDEC、LocalSurvivor、CleanKLS 三终端证书全集。 |
| top-prime promotion deletion potential | `B:LocalSurvivor-or-A:PDEC-or-C:CleanKLS` | `PositiveDeletionPotentialOrNoDeletionKL` | `positive_current_layer` | `True` | 当前晋升层有正删除势；未来若删除势不可发散，则进入 NoDeletion-KL/PDEC/CleanKLS。 |

## 4. 仍未闭合的终端证书

- A:PDEC family same-set capacity upper U_CRT<L_PDEC.
- B:LocalSurvivor witness/blocker-deficit certificates for sparse packets.
- C:CleanKLS/DLS admission plus large-sieve or explicit external input.

## 5. 读法

这一步完成的是当前 A1 链条的汇合与无第四出口接线：不能再把 APS、DualCap、升层删除、
top-prime 晋升或 NoDeletion-KL 当作独立逃逸。下一步应直接提交三终端证书；
其中最窄入口仍是 `A:PDEC same-set capacity upper`。
