# Prime Matrix clean-core 几何 Phi/预算桥路由器

**状态：** `geometric_phi_budget_bridge_closed_signed_source_and_budget_open`

几何模型提供了可用的 Phi 基底和预算/回流桥，但不能直接闭合 signed source。最新自足剩余分裂为 signed source/Phi identity 与 geometric variation/branch budget 两个未证原子。

```text
geometric_phi_budget_bridge_boundary_closed=true
geometric_payment_base_available=true
geometry_defines_signed_source_measure=false
geometry_proves_phi_pushforward_identity=false
geometry_supplies_budget_return_shape=true
actual_signed_source_measure_phi_compatibility_budget_proved=false
row_column_unconditional_closed=false
```

## 1. 几何桥律

斜线覆盖、圆柱环绕、第P列锚和层叠轮筛共同给出的是 signed source 的几何基底与预算场：它们定义哪些 payment atoms 可以由哪些斜线/锚相位/轮层命中，并说明容量失败、同步尖峰或 branch 爆炸必须回流 PDEC/SAE/ColumnCRT/CleanKLS。但这些几何对象本身不生成 pre-Cauchy signed alpha/delta 源测度，也不自动证明 Phi_*nu 等于目标 payment-side 系数。因此最新输入被拆为源侧 Phi 恒等式和几何预算/回流证书两个原子。

```text
cylindrical lines + P-column anchor + layered wheel
  => geometric Phi base map + variation/support/branch return shape;
not => signed alpha/delta source measure;
not => Phi_*nu coefficient identity.
```

## 2. 模型映射表

| model | closed | provides | does not provide | field |
| --- | --- | --- | --- | --- |
| cylindrical_completed_line | `true` | 低素骨架 R_x、未完成斜线补洞 F_x、最终洞 U_x 的确定性覆盖恒等式。 | signed alpha/delta 源测度或 local factor 符号。 | payment_base_map / absolute support skeleton |
| bottom_pair_deficit | `true` | 底部带补洞点 c=a(h-a) 的二次曲线刚性，可作为支撑/重叠预算证书。 | pre-Cauchy signed summand 生成公式。 | support budget / named return |
| pcolumn_anchor_wheel_field | `true` | 全行骨架 S_W(P,y) 是第一行骨架的圆柱平移，给出统一覆盖-筛除 Phi 基底。 | Phi_*nu 等于 signed alpha/delta payment-side 系数的恒等式。 | geometric Phi base map |
| dynamic_promoted_rough_capacity | `true` | 把低素斜线提升进轮底座后，剩余高素总命中 T_Y 与粗骨架 S_Y 的容量门。 | signed 总变差等于覆盖容量的证明。 | variation/support budget candidate |
| layered_wheel_phase_clamp | `true` | 若高素补洞在层叠轮单位类中同步，则回流 W-unit PDEC/SAE/ColumnCRT；否则进入分散 KLS 形状。 | noncanonical signed source 的 branch key 表。 | branch budget / phase return |
| closure_input_atlas | `true` | 所有几何路线已归入命名输入包，不再允许无名逃逸。 | 三包本身的无条件证明。 | return discipline |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PriorSourcePhiBudgetPinned | `true` | `false` | 上一层已把自足硬点压成 actual signed 源测度、Phi 兼容恒等式和预算。 | 判断几何模型能闭合哪些字段。 |
| GeometricPaymentBaseAvailable | `true` | `true` | 斜线圆柱、P列锚和层叠轮筛给出统一覆盖-筛除 Phi 基底和命名回流场。 | 这仍是 unsigned/geometric payment 基底。 |
| GeometryDoesNotDefineSignedSourceMeasure | `true` | `true` | 几何覆盖只告诉哪些数被哪些斜线命中，不定义 pre-Cauchy signed alpha/delta 源测度。 | 必须提交 actual signed source，或走外部谱输入。 |
| GeometryDoesNotProvePhiPushforwardIdentity | `true` | `true` | 圆柱/轮筛 Phi 与 signed source 的 Phi_*nu 恒等式不是自动的，需要系数级证明。 | 证明 ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn。 |
| GeometrySuppliesBudgetAndReturnShape | `true` | `false` | 现有几何模型给出总变差/支撑/branch 预算的候选证书形状和 PDEC/SAE/ColumnCRT 回流出口。 | 仍需正式预算不等式或命名回流证书全集。 |
| GeometricBridgeSplitsLatestInput | `true` | `true` | 最新输入可分解为 signed source/Phi identity 与 geometric variation/branch budget 两个原子。 | 两个原子当前均未由材料无条件证明。 |
| ActualSignedSourceMeasurePhiCompatibilityBudgetCurrentCorpusProved | `false` | `false` | 当前材料尚未同时证明 signed source、Phi 恒等式与几何预算。 | 证明 ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn 和 GeometricVariationBranchBudgetCertificateOrNamedReturn。 |
| DStructureRankinStillIndependent | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 4. 最新原子

| input | meaning |
| --- | --- |
| `ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn` | 定义 actual noncanonical signed alpha/delta 源测度 nu，并证明它沿几何/first-cover Phi 推前为目标 payment-side 系数。 |
| `GeometricVariationBranchBudgetCertificateOrNamedReturn` | 用圆柱骨架、P列锚、层叠轮和动态容量证明总变差/绝对支撑/branch key 在预算内，或命名回流。 |

## 5. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND GeometricVariationBranchBudgetCertificateOrNamedReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND GeometricVariationBranchBudgetCertificateOrNamedReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 当前结论

本步没有证明 signed source，也没有证明几何预算证书全集。它关闭的是接口层：几何模型已经足以提供
Phi 基底和预算/回流场；剩余必须分别证明 signed source/Phi 恒等式和几何预算证书。
