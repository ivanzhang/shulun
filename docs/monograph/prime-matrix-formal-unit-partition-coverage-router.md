# Prime Matrix formal unit partition coverage 路由器

**状态：** `formal_unit_partition_coverage_closed_assignment_totality_open`

FormalUnitPartitionCoverageLemma 已闭合：O(w) 已规范化，finite key、no-loss 覆盖等式与不交/边界回流四个子门全部闭合。下一最窄点回到普遍抽取定理的 `SourceFamilyAssignmentTotalityLemma`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
formal_unit_partition_coverage_interface_closed=true
formal_unit_partition_coverage_lemma_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
FormalUnitPartitionCoverageLemma => FormalUnitPartitionCoverageInterfaceClosed AND WitnessObligationDomainCanonicalizationLemma AND FiniteFormalUnitPartitionKeyLemma AND PartitionCoverageNoLossEquationLemma AND PartitionDisjointnessAndBoundaryReturnLemma.
```

## 2. 子门

| atom | meaning |
| --- | --- |
| WitnessObligationDomainCanonicalizationLemma | 把任意早期零行 witness 的全部义务规范化成一个有限集合 O(w)：R_x=F_x 物理原子、边界相位、carry/cofactor、走廊与命名回流。 |
| FiniteFormalUnitPartitionKeyLemma | 给每个 o in O(w) 指派有限 key=(formal_unit_id,family_id,window,D0,K,Omega,phase_key,branch)。 |
| PartitionCoverageNoLossEquationLemma | 证明 O(w) 等于所有 key-fibers 与显式 return records 的不交并；没有义务被丢弃。 |
| PartitionDisjointnessAndBoundaryReturnLemma | 处理边界重叠、quotient 和复用：重复原子只能合并或回流，不能重复计数。 |

## 3. 当前扫描

- FormalUnitPartitionCoverageLemma: `1`
- WitnessObligationDomainCanonicalizationLemma: `1`
- FiniteFormalUnitPartitionKeyLemma: `1`
- PartitionCoverageNoLossEquationLemma: `1`
- PartitionDisjointnessAndBoundaryReturnLemma: `1`

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FormalUnitPartitionGateActive | `true` | `false` | 上一层已把最窄点推进到 formal unit partition coverage。 | FormalUnitPartitionCoverageLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行 witness，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| EarlyZeroObligationSourcesImported | `true` | `true` | CLB 的 R_x/F_x、相位缺陷 formal unit、carry-shell 与 cofactor 深度门均已导入。 | 义务来源口径固定。 |
| FiniteTaxonomyAndEmitterImported | `true` | `true` | 所有坏窗/走廊来源族和记录发射器已固定。 | 无新来源类型剩余。 |
| FormalUnitPartitionCoverageInterfaceClosed | `true` | `true` | partition coverage 的输入、输出、key 字段与 no-loss 义务已固定。 | FormalUnitPartitionCoverageInterfaceClosed |
| WitnessObligationDomainCanonicalizationAvailable | `true` | `true` | O(w) 义务域规范化证明状态。 | WitnessObligationDomainCanonicalizationLemma |
| FiniteFormalUnitPartitionKeyAvailable | `true` | `true` | 有限 formal unit key 切分证明状态。 | FiniteFormalUnitPartitionKeyLemma |
| PartitionCoverageNoLossEquationAvailable | `true` | `true` | 覆盖无漏等式证明状态。 | PartitionCoverageNoLossEquationLemma |
| PartitionDisjointnessBoundaryReturnAvailable | `true` | `true` | 重复、边界与回流处理证明状态。 | PartitionDisjointnessAndBoundaryReturnLemma |
| FormalUnitPartitionCoverageLemma | `true` | `true` | 四个子门已全部闭合，得到 formal unit partition coverage。 | SourceFamilyAssignmentTotalityLemma |

## 5. 下一步

当前唯一最窄点更新为 `SourceFamilyAssignmentTotalityLemma`。

审稿边界：本步关闭的是 partition coverage 账本；不关闭 source-family assignment、普遍抽取总定理或行列无条件定理。
