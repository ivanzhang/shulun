# Prime Matrix coverage equation certificate 路由器

**状态：** `coverage_equation_certificate_closed_coverage_data_ready`

CoverageEquationCertificateDataLedger 已闭合：colored interval multiset 删除 color_id 后，逐 key 等于低重叠走廊 multiset。下一步可回收 `ConcreteColoringCoverageDataLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
coverage_equation_certificate_data_ledger_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
CoverageEquationCertificateDataLedger => LowOverlapDomain AND GreedyColoredDomain AND ProjectionMultiplicityEquality AND CanonicalEquationHash.
```

## 2. 等式记录族

| record_type | coverage | rule |
| --- | --- | --- |
| low_overlap_atom | 每个低重叠原子 (source_tuple_hash,a,d) 一条。 | 来自 multiplicity table 的 low_overlap_row，且 d in J_a。 |
| colored_atom | 每个着色 interval 展开为同一批 (source_tuple_hash,a,d,color_id)。 | 投影 pi(source_tuple_hash,a,d,color_id)=(source_tuple_hash,a,d)。 |
| projection_count_row | 每个 projection key 一条计数比较。 | count_low_overlap(key)=count_colored_projection(key)=1；压缩段按长度计数。 |
| color_partition_row | 每个 color_id 一条同色不交走廊记录。 | 同色 intervals 两两不交，允许交给后续 per-color Rankin。 |
| zero_loss_balance_row | 每个 source_tuple_hash 一条总量平衡记录。 | sum low_overlap atoms = sum colored projected atoms。 |
| mismatch_return | 若计数不等，必须命名为 CoverageEquationMismatchReturn。 | 不允许把漏点、重复点或跨 tuple 错配静默带入 color set。 |

## 3. 等式纪律

| law | formula | meaning |
| --- | --- | --- |
| same_source_tuple_projection | pi(source_tuple_hash,a,d,color_id)=(source_tuple_hash,a,d). | 颜色只是附加标签，不改变原低重叠原子。 |
| low_overlap_domain_exact | domain = {(a,d): d in J_a and m(d)<=Omega}. | 覆盖等式的左边由低重叠表唯一给出。 |
| colored_domain_exact | colored = union_color {(a,d,color): d in colored_interval(a,color)}. | 右边由贪心 transcript 唯一给出。 |
| multiplicity_preservation | for every key, count_left(key)=count_right(pi^-1(key)). | 不漏点、不重复、不跨 source tuple 拼接。 |
| per_color_disjoint_partition | same color intervals are disjoint and colors partition the low-overlap atoms. | 后续 Rankin 只接收同色不交走廊。 |
| canonical_equation_hash | equation_id=H(source_tuple_hash,sorted(projection_count_hashes),transcript_id). | 等式证书可复算且稳定。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CoverageEquationGateActive | `true` | `false` | 上一层已把最窄点推进到 coverage equation certificate。 | CoverageEquationCertificateDataLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| CoverageComponentSchemaImported | `true` | `true` | coverage 数据四组件口径已固定。 | 等式左右边字段固定。 |
| LowOverlapDomainImported | `true` | `true` | 低重叠原子域由 J_a 与 m(d)<=Omega 唯一给出。 | 左边 multiset 固定。 |
| GreedyColoredDomainImported | `true` | `true` | 贪心 transcript 给出每个低重叠 interval 的 color_id 和同色不交性。 | 右边 colored multiset 固定。 |
| ProjectionEqualityDiscipline | `true` | `true` | 投影 pi 删除 color_id 后逐 key 比较计数。 | 无漏点或重复点出口。 |
| CanonicalEquationHashImported | `true` | `true` | equation_id 继承 source_tuple_hash 与 transcript hash。 | 等式身份稳定。 |
| CoverageEquationCertificateDataLedger | `true` | `true` | 有色 interval 多重集投影后与低重叠走廊多重集逐 key 相等。 | ConcreteColoringCoverageDataLedger |

## 5. 下一步

当前回收目标为 `ConcreteColoringCoverageDataLedger`；随后才是 `PerColorRankinCertificateFileLedger`。

审稿边界：本步只关闭假设链条中的 coverage equation 数据证书；不执行 per-color Rankin，也不关闭行列无条件定理。
