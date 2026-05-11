# Prime Matrix strict 块互质动力容量反超路由器

**状态：** `block_capacity_surplus_criterion_closed_load_surplus_input_open`

本步把早期零行反例链压成一个明确的容量反超判据：对任意块 B 和 cutoff z，若 z-rough 位置数 |R_{B,z}(x)| 大于 高标签容量 C_{B,z}(x)，则这些位置无法全部由 P 以内素因子覆盖，早期零行矛盾。当 z=alpha P 且 alpha>1/2 时，全行容量有简单上界 2(pi(P)-pi(alpha P))。相邻互质与商相邻互质已并入该容量场，但它们本身不提供 |R| 的正下界；当前真正剩余是证明某个 alpha/块的粗洞负载严格超过有限供给容量，或证明负载不足必登记为 PDEC/SAE 缺陷并被排斥。

```text
exact_block_capacity_formula_closed=true
full_row_alpha_half_capacity_closed=true
direct_capacity_surplus_contradiction_criterion_closed=true
adjacent_quotient_dynamics_integrated=true
coprime_dynamics_capacity_surplus_proved=false
finite_supply_vs_load_contradiction_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 精确反超判据

设 `B` 是一段列块，`R_{B,z}(x)` 是块内所有不含 `<=z` 素因子的列。早期零行若成立，则每个这样的列仍必须有某个 `q<P` 因子；因为它没有 `<=z` 因子，所以这个因子必在 `(z,P)` 中。

```text
C_{B,z}(x)=sum_{z<q<P} #{c in B: q divides xP+c}.
|R_{B,z}(x)| <= C_{B,z}(x)    (早期零行的必要条件)
```

所以只要证明 `|R_{B,z}(x)|>C_{B,z}(x)`，就得到直接矛盾。

## 2. 已闭合刚性律

| law | formula | status | meaning |
| --- | --- | --- | --- |
| `block_high_label_capacity` | C_{B,z}(x)=sum_{z<q<P} #{c in B: xP+c == 0 mod q}. | `closed_definition` | 早期零行中，所有 z-rough 位置必须由这个高标签容量覆盖。 |
| `block_capacity_ceiling` | C_{B,z}(x)<=sum_{z<q<P} ceil(\|B\|/q). | `closed` | 同一素标签在短块中只能按同一模 q 余类重复。 |
| `full_row_alpha_half_capacity` | If z=alpha P and alpha>1/2, then C_{[1,P-1],z}(x)<=2(pi(P)-pi(alpha P)). | `closed` | 高标签每个最多命中两列，给出最清晰的有限供给上界。 |
| `rough_load_to_contradiction` | If \|R_{B,z}(x)\|>C_{B,z}(x), then an early zero row at x is impossible. | `closed_implication` | 这是反例链与真实容量链之间的直接矛盾判据。 |
| `adjacent_quotient_coprime_support` | For adjacent rough composites q_c m_c and q_{c+1} m_{c+1}, all prime supports across the two products are disjoint. | `closed` | 商相邻互质已并入容量场，但还需要负载下界才能产生反超。 |
| `semiprime_shell_for_alpha_gt_half` | For alpha>1/2 and n<P^2+P, every alpha P-rough composite has at most two prime factors. | `closed_with_small_P_boundary` | 粗洞在早期零行下进入高标签-商壳层；平方点作为单独缺陷账本登记。 |

## 3. alpha 全行容量诊断

下表不是证明，只用于定位最窄常数目标。若能给出 `|R_{x,alpha P}| >= c_alpha P/log P`，且 `c_alpha` 大于高标签容量常数，就能触发上面的直接矛盾。

| alpha | hit cap | high-label capacity constant | Mertens-scale reference | surplus if available | target beaten |
| --- | ---: | ---: | ---: | ---: | --- |
| 0.550000 | 2 | 0.900000 | 0.561459 | -0.338541 | `false` |
| 0.666667 | 2 | 0.666667 | 0.561459 | -0.105207 | `false` |
| 0.700000 | 2 | 0.600000 | 0.561459 | -0.038541 | `false` |
| 0.750000 | 2 | 0.500000 | 0.561459 | 0.061459 | `true` |
| 0.800000 | 2 | 0.400000 | 0.561459 | 0.161459 | `true` |
| 0.850000 | 2 | 0.300000 | 0.561459 | 0.261459 | `true` |
| 0.900000 | 2 | 0.200000 | 0.561459 | 0.361459 | `true` |
| 0.950000 | 2 | 0.100000 | 0.561459 | 0.461459 | `true` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 所有结论仍在 Assume EarlyZeroRowWithinP 下推导。 | 保持 row_column_unconditional_closed=false。 |
| `ExactBlockCapacityFormulaClosed` | `true` | `true` | 块内高标签供给等于各 q 的单余类命中数之和。 | 无。 |
| `FullRowAlphaHalfCapacityClosed` | `true` | `true` | alpha>1/2 时，全行每个高标签最多命中两列。 | HighLabelPrimeCountingUpperBoundForAlphaSlice |
| `DirectContradictionCriterionClosed` | `true` | `true` | 若 alphaP-rough 负载超过高标签容量，早期零行立刻矛盾。 | AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity |
| `AdjacentQuotientDynamicsIntegrated` | `true` | `true` | 相邻互质和商相邻互质给出支撑不交、短距不可复用和壳层容量约束。 | AdjacentQuotientShellCapacityOrSquareDefectLedger |
| `CoprimeDynamicsCapacitySurplusCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明某个 alpha 或块上 \|R\| 严格大于 C；互质动力本身不自动给负载下界。 | AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity AND HighLabelPrimeCountingUpperBoundForAlphaSlice |
| `UnifiedContradictionFieldPromotedToClosure` | `false` | `false` | 容量反超判据已闭合，但反超输入未闭合，所以统一矛盾场不能升级为无条件闭合。 | B3RemainderTotalVariationBudgetForLengthP OR AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity OR registered PDEC/SAE defect exclusion |

## 5. 最新最窄输入

```text
AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity
```

并行保留：

```text
HighLabelPrimeCountingUpperBoundForAlphaSlice AND AdjacentQuotientShellCapacityOrSquareDefectLedger AND B3RemainderTotalVariationBudgetForLengthP
```

审稿边界：本步闭合的是反例链必须满足的容量不等式，以及违反该不等式时的直接矛盾；尚未证明任何具体 `alpha` 或块真的违反容量上界。
