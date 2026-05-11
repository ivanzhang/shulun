# Prime Matrix strict 统一反例矛盾场矩阵路由器

**状态：** `unified_contradiction_field_matrix_built_coprime_dynamics_integrated_intersection_open`

统一矛盾场已把早期零行的连续合数链、相邻互质/商相邻互质动力系统、prefix 残洞强制负载、容量乘子、类型压缩和命名缺陷回流放进同一矩阵。新增的确定刚性是：若 xP+c=tau_c m_c 与 xP+c+1=tau_{c+1}m_{c+1}，则两侧全部因子支撑互质，并满足 tau_{c+1}m_{c+1}-tau_c m_c=1；若同一素标签命中距离 d 的两列，则该标签必须整除 d。这给出有限素因子供给的局部容量场，但尚未证明强制负载超过该容量。行/列命题仍未无条件闭合。

```text
adjacent_coprime_dynamics_closed=true
quotient_cross_coprime_dynamics_closed=true
short_distance_large_label_reuse_forbidden_closed=true
block_capacity_envelope_closed=true
coprime_dynamics_finite_supply_contradiction_proved=false
unified_contradiction_field_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 动力系统刚性

在早期零行假设下，每个被选中的覆盖原子可写为

```text
xP+c = tau_c m_c.
```

连续列满足

```text
tau_{c+1} m_{c+1} - tau_c m_c = 1.
```

因此相邻两列的标签、商、以及它们的任意因子支撑全互质。更一般地，若同一素数 q 同时命中距离 d 的两列，则 q|d；所以 q>d 的标签不能在该短距离复用。

## 2. 刚性律

| law | formula | status | role |
| --- | --- | --- | --- |
| `adjacent_integer_coprime` | gcd(xP+c, xP+c+1)=1. | `closed` | 相邻列的全部因子支撑不相交。 |
| `quotient_cross_coprime` | If xP+c=tau_c m_c and xP+c+1=tau_{c+1}m_{c+1}, then every factor from the first product is coprime to every factor from the second. | `closed` | 商相邻互质动力系统的基本守恒。 |
| `unimodular_neighbor_equation` | tau_{c+1}m_{c+1}-tau_c m_c=1. | `closed` | 把连续合数链写成相邻乘法坐标的刚性差分系统。 |
| `short_distance_label_reuse` | If a prime q divides both xP+c and xP+c+d, then q divides d; hence q>d cannot be reused at distance d. | `closed` | 大标签在短块内近似一次性消耗。 |
| `block_label_capacity` | For a block of length L, a fixed q can cover at most ceil(L/q) canonical prefix atoms. | `closed` | 有限素因子供给的局部容量上界。 |
| `prefix_mass_lower_route` | \|R_{x,z}\| >= (P-1)W^- - TV(lambda^-), and M#>=\|R_{x,z}\|/ceil(P/z). | `reduced_open` | 给反例链施加强制输入负载。 |
| `no_loss_named_return` | Every failed or drifting obligation remains as PDEC/SAE/ColumnCRT/quotient/reuse return. | `closed_as_accounting` | 防止把矛盾压力静默丢失。 |

## 3. 矛盾场矩阵

| field | counterexample chain | true rigidity chain | closed part | remaining |
| --- | --- | --- | --- | --- |
| `stable_same_label_recurrence` | 类型压缩迫使同 formal unit 同标签短复现。 | 同标签短复现要求 prod(Q)\|Delta；短 Delta<prod(Q) 不可能。 | CRT 短复现矛盾已闭合。 | BoundaryCap/Prefix 有效实例下界与重复 type -> same label。 |
| `prefix_mass_vs_finite_label_supply` | 早期零行迫使每个 prefix 残洞选一个 tau_z(c) in (z,P)。 | 每个 q 在块长 L 中容量 <=ceil(L/q)，总容量是有限素数供给和。 | prefix 加权转移、容量乘子、M# 到粗筛余公式已闭合。 | B3RemainderTotalVariationBudgetForLengthP AND B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND FiniteBoundaryPrefixRoughCountCertificate |
| `adjacent_coprime_quotient_dynamics` | 连续合数链要求每列都有 tau_c m_c 分解并满足 tau_{c+1}m_{c+1}-tau_c m_c=1。 | 相邻列全部因子支撑互质；大标签短距不能复用；商链也相邻互质。 | 相邻互质、商互质、短距复用禁止均为整数恒等式。 | BlockCoprimeDynamicsCapacitySurplus / FinitePrimeSupplyVsCoprimeDynamicsLoad |
| `drift_to_named_defect` | 为避免稳定复现，phase_key、anchor、label skeleton 或 quotient records 必须漂移。 | no-loss 账本要求所有漂移进入 PDEC/SAE/ColumnCRT 命名桶。 | schema 准入与 no-loss accounting 已闭合。 | SignatureDriftToRegisteredPhaseDefectTheorem and terminal exclusion。 |
| `low_prefix_mass_defect` | 若 prefix 粗筛余本身不足，反例避开质量压力。 | 低模端点筛余异常必须登记为 PDEC/SAE/ColumnCRT，而不是自由失败。 | 缺陷路线已定义。 | LowPrefixResidualMassToRegisteredPhaseDefect。 |
| `bottom_pair_curve` | 底部带早期零行要求残洞全部落入 c=a(h-a) 高素对曲线或素数为空。 | 底部精确分解给 \|F_{P-h}\|<=floor(h/2)，残洞质量若超过即矛盾。 | 二次缺口曲线分解已闭合。 | BottomPrimeWindow 或其 PDEC/SAE 回流。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `UnifiedFieldInputActive` | `true` | `false` | 把当前反例链所有压力源统一到同一个矩阵，而不宣称任一开放出口已排斥。 | UnifiedCounterexampleTrueStructureContradictionField |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 所有结论都在假设早期零行下推导；不使用真实零行缺席替代证明。 | 保持 row_column_unconditional_closed=false。 |
| `AdjacentCoprimeDynamicsClosed` | `true` | `true` | 连续整数相邻互质，任意因子分解后的标签与商在相邻列之间全互质。 | AdjacentQuotientCoprimeDynamicsLedger |
| `ShortDistanceLargeLabelReuseForbiddenClosed` | `true` | `true` | 同一素标签若命中距离 d 的两列，则必整除 d；所以大于 d 的标签不能短距复用。 | 可进入 block capacity。 |
| `LocalLabelConflictScanImportedAsDiagnostic` | `true` | `true` | 已有扫描支持相邻标签不交与短距大标签不可复用，但该扫描只作诊断，不作全局证明。 | 正式证明由整数恒等式给出。 |
| `BlockCapacityEnvelopeClosed` | `true` | `true` | 块长 L 内，每个 canonical label q 的容量 <=ceil(L/q)，有限供给容量上界可写成 sum_{z<q<P}ceil(L/q)。 | BlockCoprimeDynamicsCapacitySurplus |
| `PrefixMassInputReduced` | `true` | `false` | 强制负载 \|R_{x,z}\| 已压成 beta 主项减总变差；尚未得到全局正下界。 | B3RemainderTotalVariationBudgetForLengthP AND B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND FiniteBoundaryPrefixRoughCountCertificate |
| `CapacityMultiplierImported` | `true` | `true` | 行内标签复用乘子已精确登记，不能重复计算同一素数供给。 | FormalUnitTypeThresholdLedger |
| `NoLossNamedReturnImported` | `true` | `true` | 漂移、复用、quotient 与终端失败不允许消失，必须回到命名缺陷桶。 | SignatureDriftToRegisteredPhaseDefectTheorem |
| `CoprimeDynamicsSupplyContradictionCurrentCorpusProved` | `false` | `false` | 相邻/商互质刚性本身已闭合，但尚未证明某个块的强制负载超过有限素因子供给容量。 | BlockCoprimeDynamicsCapacitySurplus AND FinitePrimeSupplyVsCoprimeDynamicsLoad |
| `UnifiedContradictionFieldCurrentCorpusClosed` | `false` | `false` | 统一矩阵已建立；明显直接矛盾仍需在某个交点完成严格不等式或终端排斥。 | (B3RemainderTotalVariationBudgetForLengthP AND B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND FiniteBoundaryPrefixRoughCountCertificate AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse) OR BlockCoprimeDynamicsCapacitySurplus OR SignatureDriftToRegisteredPhaseDefectTheorem |

## 5. 下一最窄交点

优先寻找局部块上的负载超过供给：

```text
BlockCoprimeDynamicsCapacitySurplus
```

质量路线仍保留当前主硬点：

```text
B3RemainderTotalVariationBudgetForLengthP
```

并行保留：

```text
B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND FiniteBoundaryPrefixRoughCountCertificate AND FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse AND SignatureDriftToRegisteredPhaseDefectTheorem
```

审稿边界：本步建立统一矛盾场和闭合若干整数刚性律；没有证明某个交点的不等式已经反超容量，因此不能升级为无条件闭合。
