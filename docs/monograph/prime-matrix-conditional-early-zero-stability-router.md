# Prime Matrix 假设早期零行的稳定性/相位缺陷条件路由器

**状态：** `conditional_stability_dichotomy_closed_defect_schema_open`

在假设反例内，可以证明一个条件稳定性二分：P 行以内零行若存在，要么同一覆盖证书有短移自同构并稳定复现；要么没有短移自同构，那它本身就是同一 R_x/F_x formal unit 上的早期边界相位缺陷。这还不是最终矛盾；剩余是把该缺陷登记成可验收的 PDEC/SAE/ColumnCRT 证书。

```text
conditional_lemma_proved=true
stable_recurrence_forced_unconditionally=false
phase_defect_forced_if_no_stable_recurrence=true
row_column_unconditional_closed=false
```

## 1. 条件引理

**Conditional Early-Zero Stability Dichotomy.**
假设存在 `1<=x<P` 使第 `x` 条边界行 `xP+c, 1<=c<P` 是零行。固定 CLB 低骨架残洞 `R_x` 与高斜线补洞 `F_x`。则：

```text
EarlyZeroRowWithinP
  => StableShortRecurrence
     OR BoundaryPhaseNoncoverageDefectSameFormalUnit.
```

这里 `StableShortRecurrence` 指存在非零短移 `d`，使同一覆盖标签相位保持，因而同一证书在 `x+d` 复现；
`BoundaryPhaseNoncoverageDefectSameFormalUnit` 指没有这种短移时，`R_x=F_x` 本身就是早期小代表元的全补洞相位锁定缺陷。

## 2. 证明骨架

1. 由 CLB 分解，低斜线留下 `R_x`，高斜线只在 `R_x` 内补洞。若第 `x` 行是零行，则 `U_x=R_x\F_x` 为空，所以 `R_x=F_x`。
2. 用 `Omega=R_x`、补洞标签 `tau(c)=q(c)`、权重 `w(c)=1` 固定同一个 formal unit。任何跨口径拼接都不允许作为证明，只能回流 Stitching/quotient/reuse。
3. 若存在短移 `d` 同时保持所有已登记标签相位，即 `dP≡0 mod q(c)` 对全部必要标签成立，则同一覆盖证书在 `x+d` 行复现。
4. 若不存在这种短移，则这个早期零行不是稳定轨道点，而是高素数补洞标签在 `R_x` 上一次性锁定全部残洞的边界相位缺陷。
5. 该缺陷已经落入命名路线：`PDEC/SAE/ColumnCRT` 或首端帽 `BoundaryPhaseNoncoverage`，但还需要正式 schema 准入才能成为矛盾。

## 3. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `EarlyZeroAssumptionFormalized` | `true` | `true` | 假设存在 x<P 使 xP+1,...,xP+P-1 全被 <P 素数覆盖。 | `完整覆盖证书 S_x。` |
| `SameFormalUnitFromCLB` | `true` | `true` | 用已完成低斜线残洞 R_x 与未完成高斜线补洞 F_x 定义同一个 formal unit。 | `早期零行等价于 R_x=F_x，即边界相位非覆盖失败。` |
| `ActivationShadowRemoved` | `true` | `true` | q^2 前的 q 命中不是独立覆盖；零行的最后补洞必须来自已激活的相位锁定标签。 | `排除“未画完斜线”作为独立出口。` |
| `StableRecurrenceBranchDefinition` | `true` | `true` | 若存在非零短移 d 保持证书 S_x 的全部覆盖标签相位，则 x+d 是同 formal unit 稳定复现零行。 | `StableShortRecurrence。` |
| `NoStableRecurrenceImpliesPhaseDefect` | `true` | `true` | 若无这种短移，则早期零行不能由稳定轨道解释，只能是高素数补洞标签在 R_x 上的相位锁定缺陷。 | `BoundaryPhaseNoncoverageFailure / early diagonal phase defect。` |
| `DefectHasNamedReturn` | `true` | `true` | 上一轮已确认该缺陷必须进入 BoundaryPhaseNoncoverage 或稳定复现 PDEC/SAE/ColumnCRT 路线。 | `BoundaryPhaseNoncoverageOrStableRecurrencePDEC` |
| `PDECSchemaAdmissionStillOpen` | `true` | `false` | 要把相位缺陷升级成最终矛盾，仍需正式登记同 formal unit 的 PDEC/SAE/ColumnCRT 证书字段。 | `EarlyZeroPhaseDefectSchemaAdmission。` |
| `UnconditionalClosure` | `false` | `false` | 条件稳定性二分闭合，但相位缺陷终端尚未排斥。 | `row_column_unconditional_closed=false。` |

## 4. 当前剩余

条件稳定性二分不改变当前完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

新的最窄附加输入是：

```text
EarlyZeroPhaseDefectSchemaAdmission
  = RegisteredSameFormalUnitRxFxLedger
    AND StableShortRecurrenceCertificateOrNoStableAutomorphism
    AND BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT.
```

这说明你的思路可以作为反例分支内的稳定性二分使用；但若要变成最终矛盾，下一步必须把 `BoundaryPhaseNoncoverageDefectSameFormalUnit` 的证书字段完全登记并通过 PDEC/SAE/ColumnCRT 准入。
