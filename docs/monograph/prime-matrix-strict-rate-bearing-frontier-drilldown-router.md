# Prime Matrix strict 速率型前沿下钻路由器

**状态：** `rate_bearing_frontier_drilled_high_segment_to_tail_sieve_open`

本步完成前沿同步下钻：调和窗口上界已从活动剩余基中删除；动态粗骨架下界只剩 P>=100000 的一维 lower-sieve 尾段账本。速率型 moving-atom 终端排斥仍未证明，PDEC/CleanKLS 速率门、RatePreservation 与 DStructure 验收仍开放。

```text
frontier_drilldown_closed=true
harmonic_window_removed_from_active_basis=true
dynamic_skeleton_tail_linear_sieve_open=true
rate_bearing_moving_atom_packet_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 剩余基更新

旧压缩基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

旧展开基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND (HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

新活动基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

允许外部或标准筛输入时的旁路基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND ExternalShortIntervalRoughNumberLowerBoundForAlpha043_OR_StandardBetaSieveMertensTail AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍同步假设早期零行反例链，不使用真实零行缺席，也不转换命题。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| RateBearingPacketFrontierActive | `true` | `false` | 速率型 moving-atom 终端包已定位，但终端排斥尚未证明。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet |
| HarmonicWindowRemovedFromActiveBasis | `true` | `true` | 调和窗口上界已有 Dusart/有限段证书，不能继续作为活动硬点重复攻击。 | 从高段模型余量中删除该原子。 |
| DynamicSkeletonReducedToTailLinearSieve | `true` | `false` | 动态粗骨架有限段已闭合，P>=100000 被压成一维 lower-sieve 尾段账本。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| HighSegmentModelGapCompressed | `true` | `false` | 高段模型余量不再是调和窗口加骨架双硬点；活动剩余只保留骨架尾段筛下界。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| PDECCleanKLSRatePacketGateStillOpen | `true` | `false` | 速率型终端包的 PDEC/CleanKLS 速率门仍未证明，不能由标签命名本身闭合。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet |
| DirectTerminalExpansionRecurrenceBlocked | `true` | `true` | 裸展开 PDEC/CleanKLS 终端标签会回流到 canonical-lock 或新的独立 source-entropy 输入；这是防火墙，不是证明。 | AcyclicTerminalCanonicalLockSubatoms_OR_NewIndependentSourceEntropyProof |
| RatePreservationLedgerStillOpen | `false` | `false` | 终端排斥还必须保存 moving atom 所需的 log-power 速率字段。 | RatePreservationLedger_FOR_moving_atom_packet |
| DStructureIndependentAcceptanceStillOpen | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍需独立验收或自足替代。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| RowColumnUnconditionalClosureReached | `false` | `false` | 尚未得到足以排除早期零行反例链的终端矛盾。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步

主硬点仍是 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet`；可独立下钻的非循环账本是 `LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger`。

本证书只删除已闭合的调和窗口并同步尾段骨架账本，不声明行/列无条件闭合。
