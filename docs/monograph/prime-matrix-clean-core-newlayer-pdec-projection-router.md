# Prime Matrix clean-core new-layer PDEC 投影切片路由器

**状态：** `newlayer_projection_slicer_closed_schema_admission_open`

本步把 `ExactNewLayerFiberPDECProjectionMorphism` 中真正的几何/Fourier 部分压下去了：同一 C_P 投影不会新增旧层外支撑，强新增 Fourier 频率必能切出一个相位 cap。剩下的不是外部 KLS，也不是统计问题，而是把该 cap 登记成合法 PDEC schema。

```text
exact_newlayer_projection_morphism_closed=false
row_column_unconditional_closed=false
```

## 1. 结构律

The geometric projection part of the new-layer morphism is closed on the same C_P formal unit: lifting to Q'=rQ cannot create support outside the old projection. The analytic-to-combinatorial part is also deterministic: a large new-layer Fourier coefficient on the r-fiber slices to a phase cap with comparable signed mass discrepancy. What remains is not the projection or Fourier step, but formal PDEC admission: the cap must be registered with the same Omega,tau,w, must be non-tautological and cap-stable, and its lower and upper budgets must be computed in that same unit.

本轮压缩为：

```text
ExactNewLayerFiberPDECProjectionMorphism
  => RegisteredNewLayerPDECFormalUnitAndCapStableSchema.
```

其中已闭合的子引理是：

- `SameCPProjectionMonotonicity`：同一 `C_P` 的升层支撑投影单调。
- `FourierToFiberCapSlicer`：强新增 Fourier 系数可切出相位 cap 质量偏差。
- `FormalUnitMismatchNamedReturn`：口径不一致不再是终端，回流 Stitching/quotient/reuse。

## 2. Fourier-to-cap 确定性切片

设 `W=rW0`，固定旧层原子 `A` 后，新增 fiber 上的中心化质量为 `delta(b)`，且 `sum_b delta(b)=0`。若某个 `r∤h` 的 Fourier 系数满足 `|sum_b delta(b)e(hb/r)|>=eta`，旋转相位后取实部。由于 `cos` 是有界测试函数，层蛋糕分解给出某个循环弧或半平面 cap `B`，使

```text
|delta(B)| >= c * eta
```

其中 `c>0` 是绝对常数。这个步骤只用有限群 Fourier 对偶，不使用概率假设。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SameCPProjectionMonotonicity` | `true` | `true` | 同一全周期完成集合 C_P 下，新层支撑投影必落在旧层支撑中。 | none for LHB M_Q support; outside same C_P returns to stitching/source duty。 |
| `FourierNewLayerFrequencyPinned` | `true` | `true` | 新增层频率就是 W=rW0 中 r 不整除 h 的 Fourier 方向。 | 把强 Fourier 方向切成 PDEC cap。 |
| `FourierToFiberCapSlicer` | `true` | `true` | 有限循环群上，若中心化 fiber 分布存在大小 eta 的非零 Fourier 系数，旋转相位并用层蛋糕分解，可取一个循环弧/半平面 cap 使质量偏差至少 c eta。 | 该 cap 是否可作为正式 PDEC schema 仍需准入。 |
| `TowerEntropyReturnAvailable` | `true` | `false` | 若新增层偏斜沿塔持续，熵/能量账要求它进入 finite/profinite new-layer PDEC 或 CleanKLS。 | 把本层 cap 接到正式 PDEC 准入 schema。 |
| `PDECExplicitSchemaBoundaryKnown` | `true` | `false` | 未来 PDEC 候选必须同 formal unit、非二点、二秩以上、cap-stable。 | 当前 new-layer cap 必须提交这些字段。 |
| `FormalUnitHazardsNamed` | `true` | `true` | 若 cap 跨层、重复或不在同一 formal unit，已有 Stitching/quotient/reuse 回流纪律。 | 对当前 new-layer cap 固定 Omega、tau、w 与 phase map。 |
| `ExactNewLayerProjectionMorphismClosed` | `false` | `false` | 投影单调和 Fourier 切片已闭合，但正式 PDEC 准入字段尚未给出。 | RegisteredNewLayerPDECFormalUnitAndCapStableSchema。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立门。 | 所有 new-layer/DLS/source 输入完成后仍需验收。 |

## 4. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 当前结论

`ExactNewLayerFiberPDECProjectionMorphism` 的核心几何/Fourier 难点已变成可审稿的确定性切片。剩余唯一 schema 口径为 `RegisteredNewLayerPDECFormalUnitAndCapStableSchema`：必须固定同一个 `Omega,tau,w`，证明 cap 不是二点 tautology、不是 ColumnCRT/SAE 复用，并且 PDEC 下界与 CRT 上界按同一单位计量。
