# Prime Matrix witness obligation domain 规范化路由器

**状态：** `witness_obligation_domain_canonicalized_partition_key_open`

WitnessObligationDomainCanonicalizationLemma 已闭合：任意早期零行 witness 的 O(w) 可规范化为有限 physical filler atoms、phase/carry/cofactor 字段、命名 return records 与 quotient records。下一最窄点是 `FiniteFormalUnitPartitionKeyLemma`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
witness_obligation_domain_canonicalization_closed=true
formal_unit_partition_coverage_lemma_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
WitnessObligationDomainCanonicalizationLemma => WitnessObligationDomainCanonicalizationClosed AND FiniteFormalUnitPartitionKeyLemma.
```

## 2. O(w) 组件

| component | definition |
| --- | --- |
| physical_filler_atoms | 对每个 c in R_x=F_x，取 q_*(c)=min{q: x<q<P, q divides xP+c}，m_*(c)=(xP+c)/q_*(c)。 |
| phase_defect_record | 同一 formal unit 中登记 Omega=R_x、tau(c)=q_*(c)、w(c)=1 与 phase(c,ell)。 |
| carry_cofactor_record | 把 q_*(c)=P-a、m_*(c)=P-b 写入 carry-shell 与 cofactor-depth 字段。 |
| named_return_records | 稳定复现、边界相位、anchor-collar、复合 cofactor、SAE/ColumnCRT/PDEC 均只作为命名回流记录。 |
| quotient_records | 重复物理原子按同坐标 quotient 或 weighted/reuse return 处理，不能重复计数。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| WitnessDomainGateActive | `true` | `false` | 上一层已把最窄点推进到 O(w) 义务域规范化。 | WitnessObligationDomainCanonicalizationLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在任意假设早期零行 witness 下工作，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| PartitionInterfaceImported | `true` | `true` | partition coverage 已要求先构造有限 O(w) 再切分。 | 本步只处理 O(w)。 |
| CanonicalHighPrimeFillerAtomSelectorClosed | `true` | `true` | 对每个 c in R_x=F_x，有限非空高素因子集合有最小元 q_*(c)，因此 tau 可规范化。 | CanonicalHighPrimeFillerAtomSelectorClosed |
| CarryCofactorFieldsImported | `true` | `true` | canonical q_*(c),m_*(c) 可写入 carry-shell 与 cofactor-depth 字段。 | 容量排斥仍不在本步证明。 |
| TerminalReturnObligationDomainSchemaClosed | `true` | `true` | 终端包已被压到命名回流 schema；O(w) 可把它们作为 return records 而非无名出口。 | TerminalReturnObligationDomainSchemaClosed |
| PhysicalAtomQuotientDeduplicationClosed | `true` | `true` | Multiplicity-Stitching 合同给出同坐标 quotient、weighted 或 reuse return 的规范化方式。 | PhysicalAtomQuotientDeduplicationClosed |
| WitnessObligationDomainCanonicalizationClosed | `true` | `true` | O(w) 被规范化为 physical atoms、phase/carry/cofactor 字段、命名回流和 quotient records 的有限对象。 | WitnessObligationDomainCanonicalizationClosed |
| WitnessObligationDomainCanonicalizationLemma | `true` | `true` | 义务域规范化已闭合；下一步才是对每个 obligation 指派有限 formal-unit key。 | FiniteFormalUnitPartitionKeyLemma |

## 4. 下一步

当前唯一最窄点更新为 `FiniteFormalUnitPartitionKeyLemma`。

审稿边界：本步只证明义务域规范化；不证明 formal-unit key 全覆盖，也不关闭行列无条件定理。
