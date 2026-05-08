# Prime Matrix new-layer PDEC schema 准入路由器

**状态：** `newlayer_pdec_schema_admission_closed_budget_ledger_open`

本步闭合 new-layer PDEC schema 的准入层：同一 formal unit 可显式登记，低秩、二点、列位移、稀疏、cap 不稳定和口径错配全部回流命名出口。剩余不再是 schema 准入，而是准入后的二秩 cap-stable 核预算账本。

```text
newlayer_schema_admission_closed=true
registered_same_formal_unit_omega_tau_weight=true
lowrank_column_sparse_return_closed=true
cap_unstable_return_closed=true
newlayer_ranktwo_budget_ledger_closed=false
row_column_unconditional_closed=false
terminal_gap_before_router=RegisteredNewLayerPDECFormalUnitAndCapStableSchema
terminal_gap_after_router=NewLayerRankTwoCapStablePDECBudgetLedger
```

## 1. Formal Unit 字段

| field | value |
| --- | --- |
| `Omega` | Omega'_A=A x F_r inside the same C_P projection tower |
| `phase_map` | (old phase on W0, new fiber residue b mod r) |
| `weight` | w_A(b)=centered signed fiber mass delta_A(b), or count weight for positive cap |
| `cap` | B subset F_r or cyclic arc preimage selected by FourierToFiberCapSlicer |
| `named_return_if_invalid` | Multiplicity/Stitching, SAE, ColumnCRT, or refined PDEC |

## 2. 替换律

```text
RegisteredNewLayerPDECFormalUnitAndCapStableSchema
  =>
NewLayerRankTwoCapStablePDECBudgetLedger
```

准入层只负责把对象登记成合法证书，或把非法情形回流到命名出口；它不证明最终预算不等式。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NewLayerSchemaInputImported` | `true` | `true` | 上一层已把新增层子口压成 new-layer PDEC schema 准入与 flat admission。 | `本步只处理 schema 准入支。` |
| `SameCPProjectionFormalUnitAvailable` | `true` | `true` | 同一 C_P 投影单调和 Fourier-to-cap 切片已给出确定的新增层 cap 来源。 | `显式登记 Omega、tau、w 与 phase map。` |
| `RegisteredSameFormalUnitOmegaTauWeight` | `true` | `true` | 对每个旧层原子 A 和新增 fiber F_r，登记 Omega'=A x F_r，tau=(old_phase,b mod r)，w=delta_A(b)。 | `若不能保持同一 C_P 或同一权重口径，则回流 Stitching/source duty。` |
| `FormalUnitMismatchNamedReturn` | `true` | `true` | 跨层、重复、权重口径错配不准作为新终端。 | `weighted PDEC / quotient primitive PDEC / ColumnCRT-SAE reuse defect。` |
| `PrimitiveAdmissionBoundaryInherited` | `true` | `true` | 裸持久签名、二点 tautology、ColumnCRT、SAE 和对偶失败不能直接准入。 | `只有 primitive multi-atom same-formal-unit PDEC 可进入预算支。` |
| `LowRankAndColumnCasesNamed` | `true` | `true` | 零秩、一秩、固定壳、列位移和稀疏孤窗全部回流命名出口。 | `rank>=2 primitive kernel only。` |
| `CapUnstableCasesNamed` | `true` | `true` | 若候选不是 cap-stable，方向帽失败回流 SAE/refined PDEC/ColumnCRT/multiplicity，且无同层循环。 | `rank>=2 cap-stable budget ledger only。` |
| `NewLayerSchemaAdmissionClosed` | `true` | `true` | new-layer schema 准入层闭合：每个候选要么命名回流，要么成为二秩 cap-stable 同单位预算核。 | `NewLayerRankTwoCapStablePDECBudgetLedger。` |
| `NewLayerRankTwoCapStablePDECBudgetLedger` | `false` | `false` | 尚未证明准入后的 new-layer 二秩 cap-stable 核满足同单位 U_CRT<L_PDEC。 | `PDECCapBudgetLowerUpperSameUnitLedger for new-layer rank-two kernels。` |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND NewLayerRankTwoCapStablePDECBudgetLedger AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND NewLayerRankTwoCapStablePDECBudgetLedger AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

最窄目标更新为 `NewLayerRankTwoCapStablePDECBudgetLedger`。这一步仍不是行/列无条件闭合；它把 new-layer 集中支的准入问题压成真正的同单位预算账本。
