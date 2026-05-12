# Prime Matrix strict alpha 公式 signed lift 路由器

**状态：** `strict_alpha_formula_signed_lift_reduced_to_source_weight_phi_budget_return_open`

`AlphaFormulaSignedCoefficientLiftLedger` 被压成 actual signed alpha 源测度、pre-Cauchy 算术权重律、Phi 推前兼容、signed 变差/branch 预算和失败命名回流五项。上游早期零行刚性能显著缩小候选 row 形状，但仍不能把 unsigned 覆盖数据变成 signed alpha 系数；当前最窄点为 `AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger`。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
alpha_formula_signed_lift_router_closed=true
alpha_formula_signed_coefficient_lift_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
actual_noncanonical_alpha_side_primitive_rule_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. signed lift 律

The signed lift cannot be obtained by naming carry-shell hits. It must define an actual signed alpha source measure before Cauchy/dispersion, give an arithmetic weight law, prove Phi pushforward compatibility, control absolute variation and branch keys, and return every failed lift by name.

## 2. signed lift 内部拆分

拆分前：

```text
AlphaFormulaSignedCoefficientLiftLedger
```

拆分后：

```text
ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AlphaFormulaSignedLiftTargetActive` | `true` | `false` | 上一层已把当前最窄点固定为 unsigned row 形状到 signed alpha 系数行的提升。 | AlphaFormulaSignedCoefficientLiftLedger |
| `DisintegrationFormalButNeedsSourceImported` | `true` | `true` | 给定 signed source 后逐纤维解积分形式闭合；真正硬点是 actual source 与 Phi 推前恒等式。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaRowsPhiPushforwardCompatibilityLedger。 |
| `GeometricLedgerUnsignedOnlyImported` | `true` | `true` | 斜线、P列锚、carry-shell 和 layered-wheel 给出支撑/相位字母表，但不控制 signed 变差。 | AlphaSignedLiftVariationBranchBudgetLedger。 |
| `PhiBudgetReductionToEmitterImported` | `true` | `true` | actual signed/Phi 兼容预算已被压成 pre-pushforward primitive emitter；但 emitter 尚未证明。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger。 |
| `UnsignedZeroRowCannotSupplySignedSeedImported` | `true` | `true` | 早期零行假设只给 unsigned covering data，不能作为 signed alpha source seed。 | AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger。 |
| `PreCauchyFieldContractImported` | `true` | `true` | pre-Cauchy 来源律和反向来源 no-go 已固定：必须正向给出 signed 行、权重、branch key 和回流。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger |
| `ActualSignedAlphaSourceMeasureCurrentCorpusProved` | `false` | `false` | 当前材料尚未定义同一 formal unit 内 actual noncanonical carry-shell alpha rows 上的 signed 源测度。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger。 |
| `AlphaSignedWeightLawCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出 signed alpha 权重来自独立 pre-Cauchy 算术恒等式的公式。 | AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger。 |
| `AlphaRowsPhiPushforwardCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明 alpha rows 沿 Phi 推前后等于目标 payment-side alpha 系数。 | AlphaRowsPhiPushforwardCompatibilityLedger。 |
| `AlphaSignedLiftVariationBranchBudgetCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明 signed lift 的总变差、绝对支撑和 branch key 复杂度由几何账本支配。 | AlphaSignedLiftVariationBranchBudgetLedger。 |
| `AlphaSignedLiftFailureReturnCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出 signed 源缺失、Phi 不兼容、变差超预算或 branch 爆炸的命名回流。 | AlphaSignedLiftFailureNamedReturnLedger。 |
| `AlphaFormulaSignedCoefficientLiftCurrentCorpusProved` | `false` | `false` | signed 源测度、权重律、Phi 推前、变差预算和失败回流五项尚未合取证明。 | ActualSignedAlphaSourceMeasureForCarryShellRowsLedger AND AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger AND AlphaRowsPhiPushforwardCompatibilityLedger AND AlphaSignedLiftVariationBranchBudgetLedger AND AlphaSignedLiftFailureNamedReturnLedger |

## 4. 下一主攻点

```text
AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger
```
