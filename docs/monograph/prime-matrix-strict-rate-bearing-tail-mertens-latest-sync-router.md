# Prime Matrix strict 速率尾段 Mertens 最新前沿同步路由器

**状态：** `rate_bearing_tail_mertens_strict_self_contained_tail_closed_terminal_gates_open`

本步把速率尾段中的旧 `SelfContainedDusart...` 粗原子同步到最新解析前沿：直接 theta/PNT 包络与 Meissel-Mertens B1 常数区间都已由严格自足证书关闭，完整 Mertens 尾段解析包移出活动剩余。行/列命题仍未无条件闭合，下一步回到 PDEC/CleanKLS、RatePreservation 与 DStructure 终端门。

```text
old_self_contained_dusart_atom_refined=true
external_mertens_theta_route_closed_to_dstructure=true
strict_self_contained_mertens_tail_proved=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 剩余基

严格自足压缩基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

当前细化主攻基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

接受外部或标准输入后的基：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步只同步尾段筛输入的解析前沿，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| OldSelfContainedDusartAtomIsActiveButOutdated | `true` | `false` | `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372` 是上一桥接层的粗命名，后续语料已将其继续展开。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| MertensTailFrontierCompressed | `true` | `false` | 有限素数倒数跳点、分部求和接口、DVP 符号排斥和初等尾项可复用；剩余进入显式 PNT/Mertens 包。 | closed |
| PostFiniteThetaSyncImported | `true` | `false` | theta@20000 与有限 theta 桥已自足移出；旧内部 theta/PNT contour 主攻点已被后续 P5.1 自足同步吸收。 | absorbed by DirectInternalDusartThetaPNTEnvelopeLedger |
| InternalThetaPNTClosedByP51SelfContainedSync | `true` | `true` | 直接内部 Dusart theta/PNT 包络已由 P5.1 自足同步关闭，显式 theta 包不再是速率尾段活动硬点。 | remove InternalZeroFreeRegionToThetaContourEnvelopeLedger from active basis |
| SelfContainedMeisselMertensB1IntervalImported | `true` | `true` | B1 常数区间已由 Euler-product 区间证书关闭；该证书本身不单独声称完整 Mertens 尾段闭合。 | closed |
| ExternalThetaAndMeisselRouteReady | `true` | `false` | 外部条件路线下，theta 包络、有限桥和 Meissel-Mertens 区间均已严格匹配到 DStructure 门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| OrderedCondensedBasisReady | `true` | `false` | 按序推进证书给出的严格自足替代基为显式零点自由 theta 包加 Meissel-Mertens 常数区间。 | superseded by current theta+B1 self-contained sync |
| StrictSelfContainedMertensTailClosedByThetaAndB1Sync | `true` | `true` | 有限倒数素数跳点、分部求和接口、theta/PNT 包络与 B1 常数区间全部自足导入后，Mertens 尾段解析包从活动剩余中移出。 | closed |
| RowColumnUnconditionalClosureReached | `false` | `false` | 该同步只更新尾段解析前沿；速率 PDEC/CleanKLS、RatePreservation 与 DStructure 仍未全部完成。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步

直接攻 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet`，并行保留 `RatePreservationLedger_FOR_moving_atom_packet`。
