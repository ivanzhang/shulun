# Prime Matrix clean-core 几何变差/分支预算攻关路由器

**状态：** `geometric_budget_reduced_to_dprc_and_signed_variation_lift`

几何模型已经闭合 payment 支撑字母表和命名回流字母表。预算侧真正剩余不是再找一个固定轮或固定常数，而是两把锁：第一，动态提升轮的正偏差必须满足 DPRC 平方根界，或在某层回流 PDEC/SAE/ColumnCRT/CleanKLS；第二，actual signed source 的总变差和 branch key 复杂度必须被这个几何账本支配，不能在 Phi 纤维内靠正负抵消隐藏出超预算质量。

```text
geometric_budget_attack_boundary_closed=true
geometry_ledger_alphabet_closed=true
dprc_analytic_capacity_bound_proved=false
signed_variation_branch_lift_proved=false
geometric_variation_branch_budget_certificate_proved=false
row_column_unconditional_closed=false
```

## 1. 预算侧核心约化律

几何预算不是一个单纯计数不等式。它由两个不同层次组成：

- payment/geometric 层：支撑集合、覆盖总命中、轮层相位、命名回流出口；
- signed-source 层：pre-Cauchy `alpha/delta` 源测度的总变差、branch key、sign/local factor 和 `Phi` 纤维内绝对质量。

第一层已经由斜线圆柱、P列锚、动态提升轮和层叠轮筛形成统一账本；第二层不能由 unsigned 几何自动推出。

因此预算原子被压成：

```text
GeometricVariationBranchBudgetCertificateOrNamedReturn
  => DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn
     AND SignedGeometricLedgerVariationBranchLiftAndReturn。
```

## 2. 几何账本表

| ledger | available | pays | open |
| --- | --- | --- | --- |
| completed_line_support | `true` | 低素完成骨架、未完成补洞和最终素数洞的支撑分解。 | 不控制 signed source 的绝对变差。 |
| bottom_deficit_pair_curve | `true` | 底部带补洞必须落在二次曲线 c=a(h-a)，给出局部支撑容量上界。 | 只覆盖底部带，不能单独支付全局行。 |
| pcolumn_anchor_phi_skeleton | `true` | 所有行的轮骨架是第一行骨架的圆柱平移，给出统一 payment/Phi 支撑。 | 锚相位不生成 pre-Cauchy signed branch key。 |
| dynamic_promoted_capacity | `true` | 把全覆盖压力降为动态粗骨架正偏差平方根界或命名回流。 | 全局 DPRC 解析不等式仍未证明，只是最窄解析输入。 |
| layered_wheel_return | `true` | 相位同步失败/未稀释峰回流 W-unit PDEC、SAE、ColumnCRT 或 CleanKLS。 | 未证明所有层的分散峰均由大筛吸收。 |
| named_return_discipline | `true` | 预算失败不能成为无名第五出口，必须落入命名输入包。 | 命名输入包本身仍需证明或独立接受。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PreviousBridgeSplitAvailable | `true` | `true` | 上一层已把 signed source/Phi identity 与 geometric variation/branch budget 分开。 | 单独攻击预算侧原子。 |
| GeometryLedgerAlphabetClosed | `true` | `true` | CLB/PAW/DPRC/LayeredWheel/Atlas 已给出支撑、容量、相位和命名回流字母表。 | 这只是 payment/geometric 账本。 |
| UnsignedSupportBudgetShapeClosed | `true` | `true` | 几何层可把覆盖压力写成 S、T、H、正偏差、轮层峰和回流出口。 | 需证明 DPRC 正偏差平方根界或命名回流。 |
| DPRCAnalyticCapacityBoundProved | `false` | `false` | 当前材料尚未给出所有 P 的 T_Y<S_Y 或 max(0,T-HS)<=3sqrt(S) 无条件证明。 | 证明 DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn。 |
| SignedVariationDominatedByGeometryLedger | `false` | `false` | signed alpha/delta 源的总变差可能在 Phi 纤维内因正负抵消而大于 payment 几何账本。 | 证明 SignedGeometricLedgerVariationBranchLiftAndReturn。 |
| BranchKeyMultiplicityBudgetProved | `false` | `false` | 几何标签 q,m,W,phase 可登记，但 actual source branch key 的 polylog/K6 复杂度尚未由几何自动推出。 | 与 signed variation lift 同时证明，或把 branch 爆炸命名回流。 |
| GeometricVariationBranchBudgetCertificateProved | `false` | `false` | 预算侧原子未闭合；它被压成一个几何解析锁和一个 signed 提升锁。 | DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn |
| DStructureRankinStillIndependent | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧和预算侧完成后仍需独立验收。 |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 当前结论

本步关闭的是预算侧的接口误差：几何支撑和回流字母表已经足够清楚，不能再把剩余归因于“斜线/轮筛模型未建好”。真正剩余是 DPRC 正偏差解析界，以及 actual signed source 的变差/branch 提升纪律。当前材料仍未证明这些输入，也没有闭合无条件行/列命题。
