# Prime Matrix low-overlap multiplicity table 路由器

**状态：** `low_overlap_multiplicity_table_closed_coloring_open`

LowOverlapMultiplicityTableLedger 已闭合：从锚区间端点事件可唯一复算 m(d)，m(d)<=Omega 进入低重叠表，m(d)>Omega 强制回流 `HighOverlapFixedCoreDefect`。下一步可攻 `GreedyIntervalColoringExecutionLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
low_overlap_multiplicity_table_ledger_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
LowOverlapMultiplicityTableLedger => AnchorIntervalEnumeration AND AnchorIntervalCertificateFile AND OmegaDiscipline AND SweepLineEventConservation AND HighOverlapNamedReturn.
```

## 2. 多重度记录族

| record_type | coverage | rule |
| --- | --- | --- |
| endpoint_event | 每个非空 anchor interval 产生 left:+1 与 right:-1 两个事件。 | 事件按 (d,event_type,anchor_id) 规范排序；半开端点先处理 right 再处理 left。 |
| active_anchor_set | 每个核心 d 或最大常值段一条。 | active(d)={a: left_a<=d<right_a 且 phase_rule(d)=true}。 |
| multiplicity_row | 每个 d 或最大常值段记录 m(d)。 | m(d)=\|active(d)\|，active_anchor_hash=H(sorted(active(d)))。 |
| low_overlap_row | m(d)<=Omega 的核心点或段进入低重叠走廊。 | 写 low_overlap_flag=true，并保留 active_anchor_hash。 |
| high_overlap_return | m(d)>Omega 的核心点或段必须命名回流。 | 写 return_type=HighOverlapFixedCoreDefect，不得留在低重叠着色域。 |
| empty_active_row | m(d)=0 的空活动段显式记录或压缩记录。 | 空活动段不是数据缺口，写 empty_active_flag=true。 |

## 3. sweep-line 纪律

| law | formula | meaning |
| --- | --- | --- |
| event_conservation | sum(left_events)-sum(right_events)=0 over each source_tuple file. | 每条锚区间只进入一次、退出一次，不能制造或丢失 active anchor。 |
| half_open_endpoint_order | [left,right) uses right-events before left-events at the same d. | 相接区间不被误判为重叠。 |
| phase_filtered_activity | active(d) additionally requires phase_rule(d)=true. | 相位过滤继承证书文件，不能在多重度表里重选。 |
| omega_split_exact | low(d) iff m(d)<=Omega; high(d) iff m(d)>Omega. | 低/高重叠二分是互斥且穷尽的。 |
| high_overlap_named_return | m(d)>Omega -> HighOverlapFixedCoreDefect(d,active(d)). | 高重叠点不能进入 colored corridor，也不能静默删除。 |
| canonical_table_hash | table_id=H(source_tuple_hash,Omega,sorted(multiplicity_row_hashes)). | 多重度表由锚区间证书和 Omega 唯一决定。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LowOverlapMultiplicityGateActive | `true` | `false` | 上一层已把最窄点推进到 low-overlap multiplicity table。 | LowOverlapMultiplicityTableLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| AnchorIntervalsImported | `true` | `true` | 锚区间枚举账本和证书文件生成律均已闭合，事件域固定。 | 不能重选 J_a。 |
| OmegaDisciplineImported | `true` | `true` | Omega 来自同一 source tuple 的 DCS 高/低重叠二分纪律。 | 不能后验移动阈值。 |
| SweepLineMultiplicityDeterministic | `true` | `true` | 按端点事件前缀和可唯一复算每个 d 的 active anchors 与 m(d)。 | 无多重度选择口。 |
| HighLowSplitExhaustive | `true` | `true` | m(d)<=Omega 进入低重叠表；m(d)>Omega 进入命名 high-overlap return。 | HighOverlapFixedCoreDefect |
| CanonicalMultiplicityHashImported | `true` | `true` | multiplicity row hash 与 table_id 继承 source_tuple_hash。 | 表身份稳定。 |
| LowOverlapMultiplicityTableLedger | `true` | `true` | 低重叠多重度表由锚区间事件和 Omega 确定性生成；高重叠点强制命名回流。 | GreedyIntervalColoringExecutionLedger |

## 5. 下一步

当前回收目标为 `GreedyIntervalColoringExecutionLedger`。

审稿边界：本步只关闭假设链条中的低重叠多重度表生成律；高重叠点保留为命名 return，不关闭行列无条件定理。
