# Prime Matrix new-layer 二秩预算账本路由器

**状态：** `newlayer_ranktwo_budget_ledger_reduced_to_flat_admission_gate`

本步没有证明所有 new-layer 二秩核的 U_CRT<L_PDEC；它证明更窄的结构事实：若该预算账本失败，则同一 formal unit 内必产生有限字符弧 cap。该 cap 要么回流 SAE/refined PDEC/ColumnCRT/multiplicity，要么在非平坦缺陷剥离后成为 NewLayerNoConcentrationImpliesFlatAdmission 的 flat residual。因此二秩预算账本不再是独立最终输入。

```text
newlayer_ranktwo_budget_ledger_reduced=true
newlayer_ranktwo_budget_independent_input_removed=true
newlayer_pdec_budget_inequality_unconditionally_proved=false
newlayer_no_concentration_flat_admission_proved=false
row_column_unconditional_closed=false
terminal_gap_before_router=NewLayerRankTwoCapStablePDECBudgetLedger
terminal_gap_after_router=NewLayerNoConcentrationImpliesFlatAdmission
```

## 1. 预算失败的强制形状

```text
NewLayerRankTwoCapStablePDECBudgetLedger
  same formal unit Omega'_A=A x F_r;
  if U_CRT >= L_PDEC:
    cap localization gives a finite cyclic arc cap;
    old-axis cap   => old PDEC / ColumnCRT / SAE return;
    new-fiber cap  => new-layer PDEC cap or flat residual;
    mixed-axis cap => transverse split, then named return or flat residual;
  therefore no independent budget-ledger terminal remains.
```

## 2. 方向分裂

| direction class | route |
| --- | --- |
| `old_axis` | projection to old formal unit; old PDEC/ColumnCRT/SAE return |
| `new_fiber_axis` | fiber residue b mod r; new-layer cap or flat admission |
| `mixed_axis` | finite character arc in A x F_r; transverse split then flat admission |

## 3. 替换律

```text
NewLayerRankTwoCapStablePDECBudgetLedger
  =>
absorbed by named cap returns OR NewLayerNoConcentrationImpliesFlatAdmission
```

注意：这里删除的是独立预算账本原子，不是宣称 new-layer flat admission 已经完成。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NewLayerRankTwoBudgetInputActive` | `true` | `true` | 上一层已把合法 new-layer schema 的唯一开放门定位为二秩 cap-stable 预算账本。 | `检查它是否真是独立新原子。` |
| `SameFormalUnitBudgetLedgerRegistered` | `true` | `true` | Omega'_A=A x F_r、phase、weight 与同一 C_P 投影塔已固定，预算比较不换集合不换权重。 | `若换口径则回流 Stitching/Multiplicity，不进入本账本。` |
| `RankTwoCapLocalizationImported` | `true` | `true` | 同 formal unit 二秩 cap-stable 核的预算失败必给方向帽质量下界。 | `U_CRT>=L_PDEC 不能作为无名失败保留，必须输出 cap witness。` |
| `UniformFiniteArcBasisImported` | `true` | `true` | 连续方向帽在有限 formal unit 上等价于有限循环弧 cap 基。 | `只需处理旧轴、新 fiber、混合轴上的有限字符弧。` |
| `ProductCharacterDirectionSplit` | `true` | `true` | Omega'_A=A x F_r 中每个非平凡方向分成 old-axis、new-fiber 或 mixed-axis，均仍是有限字符弧预像。 | `old-axis 回旧层 PDEC/ColumnCRT；new/mixed 进入 new-layer cap/flat 分裂。` |
| `FiniteArcTransverseTrichotomyInherited` | `true` | `true` | 高质量有限弧只有低横向支撑、持久横向偏斜、横向平坦分散三类。 | `前两类回流 SAE/ColumnCRT/refined PDEC；平坦类进入 clean/flat 门。` |
| `TransverseFlatResidualUsesNewLayerFlatGate` | `true` | `false` | 非平坦缺陷剥离后，剩余正是 new-layer 无集中 flat admission 的对象。 | `仍需证明 NewLayerNoConcentrationImpliesFlatAdmission 及后续 flat DLS/KLS 吸收。` |
| `NoCycleAndNamedReturnPreserved` | `true` | `true` | cap 细化不会在同层无限循环；升层只能进入 profinite/new-layer PDEC 或 CleanKLS/DLS。 | `不允许新增第五类终端。` |
| `NewLayerRankTwoBudgetIndependentGateRemoved` | `true` | `true` | 二秩预算账本失败已被强制材料化为有限弧 cap，并被路由到命名回流或 new-layer flat gate。 | `它不再作为独立开放输入保留。` |
| `NewLayerNoConcentrationImpliesFlatAdmission` | `false` | `false` | 当前材料尚未证明删除所有可登记 PDEC cap 后的 residual 自动满足 flat-DLS/KLS 准入。 | `下一步最窄目标。` |

## 5. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

最窄目标更新为 `NewLayerNoConcentrationImpliesFlatAdmission`。必须证明：删除/回流所有可登记 PDEC cap 后，剩余新增层对象确实满足 flat-DLS/KLS 准入；否则必须输出新的命名 PDEC/SAE/ColumnCRT/multiplicity 证书。
