# Prime Matrix greedy interval coloring execution 路由器

**状态：** `greedy_interval_coloring_execution_closed_coverage_equation_open`

GreedyIntervalColoringExecutionLedger 已闭合：低重叠 intervals 按稳定顺序执行贪心着色，每步释放颜色并取最小可用色，color_count<=Omega。下一步可攻 `CoverageEquationCertificateDataLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
greedy_interval_coloring_execution_ledger_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
GreedyIntervalColoringExecutionLedger => LowOverlapMultiplicityTable AND IntervalGraphColoringTheorem AND StableGreedyTranscript AND CanonicalTranscriptHash.
```

## 2. 执行记录族

| record_type | coverage | rule |
| --- | --- | --- |
| ordered_interval_input | 每个低重叠 interval 一条排序输入记录。 | 按 (left_d,right_d_exclusive,source_tuple_hash,anchor_id) 稳定排序。 |
| release_event | 扫描到新区间左端点时释放 right_d_exclusive<=left_d 的旧区间颜色。 | 半开端点保证相接区间可复用同色。 |
| active_set_before_after | 每一步记录 active_before_hash 与 active_after_hash。 | active set 来自 low-overlap multiplicity table，不能重算出不同活动域。 |
| chosen_color | 每个 interval 一条颜色选择记录。 | 取最小可用 color_id；无可用色则开新色，但 color_count 必须 <= Omega。 |
| same_color_disjointness_check | 每个颜色类记录上一右端点。 | 新 interval 的 left_d 必须 >= 同色上一 right_d_exclusive。 |
| color_count_bound_row | 每个 source tuple 记录 max_color_count。 | max_color_count <= max_d m(d) <= Omega。 |

## 3. 贪心纪律

| law | formula | meaning |
| --- | --- | --- |
| stable_interval_order | sort by (left,right,source_tuple_hash,anchor_id). | 执行 transcript 不依赖文件枚举顺序。 |
| release_before_assign | free colors with right<=left before assigning current interval. | 半开区间相接不算重叠。 |
| smallest_available_color | color(I)=min(free_colors) or next_new_color. | 颜色选择是确定性函数。 |
| omega_capacity | simultaneous_active_count<=Omega from low-overlap table. | 贪心所需颜色数不超过 Omega。 |
| per_color_disjointness | same color implies previous_right<=next_left. | 同色走廊两两不交。 |
| transcript_hash | transcript_id=H(source_tuple_hash,sorted(step_hashes)). | 执行记录可复算且稳定。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| GreedyColoringExecutionGateActive | `true` | `false` | 上一层已把最窄点推进到 greedy interval coloring execution。 | GreedyIntervalColoringExecutionLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行链条，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| CoverageComponentSchemaImported | `true` | `true` | coverage 数据已拆成锚区间、多重度、着色执行和覆盖等式四组件。 | 组件口径固定。 |
| LowOverlapMultiplicityImported | `true` | `true` | 低重叠表已给出 m(d)<=Omega 的精确活动域。 | 颜色容量上界固定。 |
| IntervalGraphColoringTheoremImported | `true` | `true` | 整数区间图贪心着色与 color_count<=Omega 已由上层 formal 证书给出。 | 无存在性剩余。 |
| AnchorIntervalInputImported | `true` | `true` | 每个低重叠 interval 的端点可由 anchor interval 证书复算。 | 输入区间稳定。 |
| CanonicalTranscriptHashImported | `true` | `true` | 执行步骤哈希继承 source_tuple_hash。 | transcript 身份稳定。 |
| GreedyIntervalColoringExecutionLedger | `true` | `true` | 贪心着色执行 transcript 由排序、释放颜色和最小可用色规则确定性生成。 | CoverageEquationCertificateDataLedger |

## 5. 下一步

当前回收目标为 `CoverageEquationCertificateDataLedger`。

审稿边界：本步只关闭假设链条中的贪心着色执行 transcript；不提交覆盖等式证书，也不关闭行列无条件定理。
