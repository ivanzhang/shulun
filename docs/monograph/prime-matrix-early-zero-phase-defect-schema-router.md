# Prime Matrix 早期零行相位缺陷 schema 准入路由器

**状态：** `early_zero_phase_defect_schema_admission_closed_terminal_exclusion_open`

`EarlyZeroPhaseDefectSchemaAdmission` 已作为 schema 准入层闭合：早期零行反例分支不会产生第四类未命名出口。它要么给稳定短复现证书，要么给 no-automorphism 相位缺陷证书；两者都可同口径登记并进入 PDEC、SAE/LocalSurvivor 或 ColumnCRT 吸收路线。该步骤仍不排斥这些终端，所以行列无条件命题仍未闭合。

```text
early_zero_phase_defect_schema_admission_closed=true
registered_same_formal_unit_rxf_ledger=true
stable_short_recurrence_certificate_or_no_stable_automorphism_closed=true
boundary_phase_defect_to_named_families_closed=true
early_zero_branch_unconditional_contradiction=false
row_column_unconditional_closed=false
```

## 1. 准入定理

**Early-Zero Phase-Defect Schema Admission.**
假设存在 `1<=x<P` 的早期零行。固定 CLB 分解的低骨架残洞 `R_x` 与高斜线补洞 `F_x`。则：

```text
EarlyZeroRowWithinP
  => RegisteredStableRecurrencePDEC/SAE/ColumnCRT
     OR RegisteredBoundaryPhaseDefectPDEC/SAE/ColumnCRT.
```

更精确地，上一轮的条件二分中开放的

```text
EarlyZeroPhaseDefectSchemaAdmission
  = RegisteredSameFormalUnitRxFxLedger
    AND StableShortRecurrenceCertificateOrNoStableAutomorphism
    AND BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT
```

三项现在作为证书准入层闭合。闭合的是“能否正规登记并命名回流”，不是“终端已被排斥”。

## 2. 同 formal unit 登记

早期零行给出 `R_x=F_x`。正式登记为：

```text
Omega = R_x
tau(c) = q(c), 其中 x<q(c)<P 且 q(c) | xP+c
w(c) = 1
phase(c,ell) = c+xP mod ell
physical_atom(c) = (c,q(c),m(c)), xP+c=q(c)m(c), m(c)>x
```

这里 `m(c)>x` 来自 `c in R_x`：若 `m(c)<=x`，则 `m(c)` 有不超过 `x` 的素因子，反而会让 `xP+c` 被低骨架删去。
重复物理原子不能重复计数；必须按 Multiplicity-Stitching 合同进入 quotient、weighted PDEC 或复用缺陷。

## 3. 稳定性判定

同一 formal unit 的短移自同构必须保持所有活动标签相位。由于 `P` 与每个 `ell<P` 互素，条件

```text
dP == 0 mod ell
```

等价于 `ell | d`。因此短移集合由活动标签的 `lcm` 完全判定：

```text
Aut_short(S_x) = {0<|d|<P : lcm(active labels) | d}.
```

若集合非空，输出稳定短复现证书；若为空，输出 no-stable-automorphism 证书，并把 `R_x=F_x` 登记为一次性边界相位锁定缺陷。

## 4. 命名回流

- 持久、多原子、同口径、非二点且二秩以上的缺陷进入 `PDEC family`。
- 孤立短窗、端点或有限局部逃逸进入 `SAE/LocalSurvivorCert`。
- 固定列位移或同列复用先进入 `ColumnCRT`，再由位移 PDEC/SAE 吸收。
- 多重、跨层或口径错配不能作为证明，必须 quotient、weighted-dual 或回流复用缺陷。

## 5. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `ConditionalEarlyZeroDichotomyImported` | `true` | `true` | 已在假设反例内证明：早期零行给出稳定短复现，或给出同 formal unit 相位缺陷。 | `只处理 schema 准入，不重证二分。` |
| `RegisteredSameFormalUnitRxFxLedger` | `true` | `true` | 固定 Omega=R_x，tau(c)=q(c)，w(c)=1，phase map 由 c -> -xP mod q(c) 给出。 | `R_x=F_x 是同一 formal unit 的补洞证书，不允许跨口径拼接。` |
| `FillerAtomPhysicalLedger` | `true` | `true` | 若 c in R_x=F_x，则存在 x<q(c)<P 与 m(c)>x 使 xP+c=q(c)m(c)。 | `每个补洞点产生物理原子 (c,q(c),m(c))，重复必须 quotient 或 weighted。` |
| `StableShortRecurrenceCertificateOrNoStableAutomorphism` | `true` | `true` | 同 formal unit 的短移自同构由 dP=0 mod ell 对全部活动 ell 判定；等价于 d 被活动标签 lcm 整除。 | `若存在 0<\|d\|<P 的解则输出 StableShortRecurrence；否则输出 no-stable-automorphism 证书。` |
| `StableBranchNamedReturn` | `true` | `true` | 稳定复现若带固定列位移或端点复用，则不是新出口，按 ColumnCRT/SAE/PDEC 吸收。 | `StableShortRecurrence -> displacement PDEC or SAE/endpoint or PDEC dual row。` |
| `NoAutomorphismPhaseDefectRegistered` | `true` | `true` | 无短移自同构时，R_x=F_x 是一次性相位锁定缺陷，必须作为有限签名进入终端家族。 | `BoundaryPhaseNoncoverageDefectSameFormalUnit is registered。` |
| `BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT` | `true` | `true` | 持久多原子同口径缺陷进 PDEC；孤窗/端点进 SAE/LocalSurvivor；固定列位移先经 ColumnCRT 吸收。 | `早期零行相位缺陷没有第四类未命名出口。` |
| `EarlyZeroPhaseDefectSchemaAdmission` | `true` | `true` | 三项 schema 字段已全部登记：同 formal unit、稳定/无自同构、PDEC/SAE/ColumnCRT 命名回流。 | `schema admission closed; terminal exclusion still open。` |
| `EarlyZeroTerminalExclusion` | `false` | `false` | 准入不是排斥。还需证明准入后的 PDEC 容量不等式，或给出 SAE/LocalSurvivor 排斥。 | `EarlyZeroTerminalExclusionPackage。` |
| `CurrentMainBasisUnchanged` | `true` | `false` | 该早期零行分支是附加 overlay，不替代当前 new-layer/DLS/source/DStructure 输入基。 | `RegisteredNewLayerPDECFormalUnitAndCapStableSchema` |
| `DStructureRankinStillIndependent` | `true` | `false` | 即使早期零行分支完成，DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。` |

## 6. 新剩余

本步把早期零行反例分支的准入层压成一个更具体的终端排斥义务：

```text
EarlyZeroTerminalExclusionPackage
  = EarlyZeroPrimitivePDECBudgetInequality
    AND EarlyZeroLocalSurvivorPacketOrSAEExclusion
    AND StableRecurrenceDisplacementPDECBudgetOrColumnSAEExclusion.
```

当前主输入基不改变：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission AND DLSFlatHighModLargeSieveAbsorption AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

因此本结论是反例分支内的结构闭合推进；`row_column_unconditional_closed=false` 仍必须保留。
