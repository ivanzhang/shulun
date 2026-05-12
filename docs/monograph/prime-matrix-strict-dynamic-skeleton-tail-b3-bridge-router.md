# Prime Matrix strict 动态骨架尾段到 B3 粗筛桥接路由器

**状态：** `dynamic_skeleton_tail_b3_bridge_conditional_external_closed_self_contained_mertens_open`

本步把动态骨架尾段 lower-sieve 账本接到已有 B3 粗筛体系：对象接口、lower weights 支配性和 10% 容量代数均已对齐。若接受外部显式 Mertens/Dusart 或标准 beta-sieve 输入，尾段骨架下界可条件关闭；严格自足版仍只剩 Mertens/PNT 尾段内联证明，不能声明行/列无条件闭合。

```text
tail_object_interface_closed=true
lower_weight_construction_and_dominance_imported=true
ten_percent_capacity_algebra_imported=true
tail_ledger_external_or_standard_closed=true
tail_ledger_strict_self_contained_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 同口径接口

动态骨架尾段的目标对象可写成：

```text
S(P)=#{1<=k<P: k avoids one prescribed residue class modulo every prime q<=P^0.43}.
```

对每个 squarefree `d<P`，CRT 给出单余类计数：

```text
A_d(P)=(P-1)/d + r_d, |r_d|<=1.
```

因此该对象与已有 B3 lower-weight 粗筛余账本同口径。

## 2. 容量常数

| item | value |
| --- | ---: |
| tail start | 100000 |
| alpha | 0.430000 |
| f(1/alpha) | 0.431717689229 |
| model main at P=100000 | 4896.256004 |
| 10% main | 489.625600 |
| 10% surplus over 401 | 88.625600 |
| 98% main | 4798.330884 |
| 98% surplus over 401 | 4397.330884 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TailLinearSieveGateActive | `true` | `false` | 前沿下钻后，非循环可攻点正是 P>=100000 的动态骨架尾段 lower-sieve 账本。 | LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger |
| DynamicSkeletonTailObjectMatched | `true` | `true` | 尾段对象是区间 1<=k<P 中避开每个 q<=P^0.43 的一个同余类；对任意 formal unit 与正负侧都只改变同余类名，不改变筛公式。 | 可接入一维 beta-sieve 粗筛余框架。 |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内证明必要筛余输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| LowerWeightConstructionAndDominanceImported | `true` | `true` | B=3 lower weights 的有限递归、支撑、符号和逐点 lower-bound 支配已由内部组合证明关闭。 | 不再把 lower weights 构造当活动硬点。 |
| TenPercentCapacityAlgebraImported | `true` | `true` | P=100000 处 10% 模型主项仍大于 401，且尾段主量随 P/log P 增长。 | 需要主系数与 floor/TV 余项账本匹配。 |
| B3MainCoefficientConditionalExternalClosed | `true` | `false` | 接受外部显式 Mertens/Dusart 尾段时，B=3 主系数 99% 包已在既有证书中闭合。 | 严格自足版仍需内联 Mertens/PNT 尾段。 |
| B3RemainderTVConditionalExternalClosed | `true` | `false` | 接受外部显式 Mertens/Dusart 尾段时，长度 P 的 B3 floor/TV 余项由有符号 Stieltjes 边界预算关闭。 | 严格自足版仍需内联 Mertens/PNT 尾段。 |
| ExternalOrStandardTailLedgerClosed | `true` | `false` | 在允许外部显式 Mertens/Dusart 或标准 beta-sieve 粗数输入时，动态骨架尾段下界可从活动剩余基移除。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR StandardRosserIwaniecBetaSieveTheoremImportAccepted |
| StrictSelfContainedMertensTailStillOpen | `true` | `false` | 严格自足版不能把外部 Mertens/Dusart 尾段当已证；需要内联显式 PNT/Mertens 证明。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| StrictSelfContainedTailLedgerProved | `false` | `false` | 当前仓库尚未给出完全自足的 Mertens/PNT 尾段内联证明，因此 tail lower-sieve 账本不能标成严格自足已证。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| RowColumnUnconditionalClosureReached | `false` | `false` | 该桥接只关闭或压缩高段骨架尾段输入；速率终端门、RatePreservation 与 DStructure 仍未全部完成。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 剩余基

严格自足路线：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

接受外部或标准筛输入的路线：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本证书不把外部 Mertens/Dusart 或标准 beta-sieve 输入冒充为严格自足证明。
