# Prime Matrix 复合 cofactor 下降命名回流 schema 路由器

**状态：** `composite_cofactor_descent_schema_closed_terminal_exclusion_open`

本步闭合的是复合 cofactor 递归壳的命名回流 schema：由于 m<P 且 x-rough 深度有限，无穷递归循环不可能；持久复合签名必须进 PDEC，孤立复合签名必须进 SAE/LocalSurvivor。因此复合 cofactor 专属 gap 被删除，但 PDEC/SAE 终端排斥本身仍未证明。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
composite_cofactor_descent_schema_closed=true
composite_cofactor_specific_gap_removed=true
pdec_or_sae_terminal_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=CompositeCofactorDepthDescentOrNamedReturn
terminal_gap_after_router=NoCompositeCofactorUnnamedDescentGap_AfterWellFoundedNamedReturn
```

## 1. 替换律

```text
CompositeCofactorDepthDescentOrNamedReturn
  =>
NoCompositeCofactorUnnamedDescentGap_AfterWellFoundedNamedReturn
```

这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CompositeCofactorGateActive` | `true` | `true` | 当前输入基仍包含 CompositeCofactorDepthDescentOrNamedReturn。 | `本步只攻击复合 cofactor 递归壳。` |
| `XRoughDepthBoundImported` | `true` | `true` | 若 xP+c=q m 且 m 复合，则 m<P 且所有素因子 >x，深度 d<log(P)/log(x)。 | `递归深度有限。` |
| `SqrtGateTerminatesPrimePair` | `true` | `true` | 一旦 x>=sqrt(P)，复合 cofactor 不可能存在，只剩真双素/anchor 分支。 | `递归不能跨过 sqrt 门继续无名存在。` |
| `CarryShellSupportInherited` | `true` | `true` | 复合 cofactor 仍来自同一个 carry-shell 高补洞支撑。 | `不能换口径计数。` |
| `WellFoundedDescentMeasure` | `true` | `true` | 每次真正递归都把顶层 P 换成更小 cofactor m<P，或降低 cofactor 乘法深度。 | `不存在无穷递归循环。` |
| `PersistentCompositeCofactorAdmitsPDEC` | `true` | `true` | 若同一复合 cofactor 签名持久复现，它必须提交同 formal unit primitive PDEC schema。 | `PDEC 终端排斥仍未证明。` |
| `IsolatedCompositeCofactorAdmitsSparseSAE` | `true` | `true` | 若复合 cofactor 只孤立出现，它必须提交有限 sparse/SAE packet schema。 | `SAE/sparse 终端排斥仍未证明。` |
| `NoUnnamedCompositeCofactorDescent` | `true` | `true` | 复合 cofactor 只有下降、持久 PDEC 或孤立 SAE 三种命名归宿。 | `NoCompositeCofactorUnnamedDescentGap_AfterWellFoundedNamedReturn` |
| `CompositeCofactorDepthDescentOrNamedReturn` | `true` | `true` | 该硬点作为 well-founded 命名回流 schema 已闭合。 | `终端家族本身仍未无条件排斥。` |
| `GlobalPDECorSparseTerminalExclusion` | `false` | `false` | 若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。 | `FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。` |

## 3. 最新输入基

条件输入基：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSFixedWheelUnitPeakDilutionOrPDECReturn AND EarlyBandLocalSurvivorOrSAEExclusion AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

复合 cofactor 专属 gap 已删除。下一步最窄目标回到 `EarlyBandLocalSurvivorOrSAEExclusion`；若未来实际物化新的 PDEC/SAE packet，则由 `FutureExplicitPrimitivePDECSchema_OR_FutureExplicitSparsePacketExtractorSchema_if_materialized` 接管。
