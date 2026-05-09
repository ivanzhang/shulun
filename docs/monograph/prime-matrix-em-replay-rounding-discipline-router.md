# Prime Matrix Euler-Maclaurin replay 舍入纪律路由器

**状态：** `em_replay_rounding_discipline_closed_center_values_only`

DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger 已闭合：Euler-Maclaurin 中心值 replay 所需的 dyadic、复矩形、log/trig/exp、除法和余项外包均落入已闭合区间核与 trace/hash 账本。严格自足剩余只剩 1024 个中心值下界表。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
em_replay_rounding_discipline_closed=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 运算映射

| operation | covered by | note |
| --- | --- | --- |
| dyadic centers c_j and height 14 | DyadicRationalIntervalArithmeticCoreClosed | 中心点、网格端点、N=32、p=8、Bernoulli 系数均为有理数据。 |
| log n | RationalLogTrigTaylorOracleTemplateClosed | n<=32，atanh-log 模板给向外有理盒。 |
| n^{-s}=exp(-s log n) | RationalExpTaylorRangeReductionTemplateClosed AND RationalLogTrigTaylorOracleTemplateClosed | 拆成 exp(-sigma log n)*(cos(14 log n)-i sin(14 log n))。 |
| rising factorial (s)_m | ComplexRectangularIntervalPropagationClosed | 有限复矩形乘法和加法。 |
| division by s-1 | ComplexRectangularIntervalPropagationClosed | \|s-1\|>=14，除法零排斥有显式下界。 |
| EM remainder interval | integer endpoint inequality plus Bernoulli periodic bound | 使用标准余项上界写成实半径，加入复盒外包。 |
| node ordering and reproducibility | IntervalOperationTraceHashLedgerClosedCanonicalDAGv1 | 每个中心值 replay 是 canonical DAG root hash。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EMRoundingGateActive` | `true` | `true` | 导数门闭合后，并行实现门是 EM 中心值 replay 的舍入纪律。 | DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只规定有限中心值证书的可复放计算纪律，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `CertifiedIntervalKernelImported` | `true` | `true` | dyadic、复矩形、log/trig/exp Taylor 尾阶与 trace/hash 账本均已闭合。 | all arithmetic primitives available. |
| `EulerMaclaurinOperationMapClosed` | `true` | `true` | EM replay 的每种运算都落入已闭合的区间核或整数不等式。 | DyadicComplexIntervalEulerMaclaurinReplayRoundingClosedCanonicalDAGv1 |
| `CenterValuesStillMissing` | `false` | `false` | 舍入纪律不替代 1024 个中心值的实际非零下界表。 | TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1 |
| `DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger` | `true` | `true` | EM replay 舍入纪律已闭合，剩余只是真正的中心值表。 | DyadicComplexIntervalEulerMaclaurinReplayRoundingClosedCanonicalDAGv1 |

## 3. 下一步

严格自足唯一顶边剩余：`TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1`。
顶边完成后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：舍入纪律不是剩余；中心值 replay 表才是剩余。
