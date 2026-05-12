# Prime Matrix strict primitive 核表三腿回流同步证书

**状态：** `kernel_table_three_leg_return_synced_nonrecursive_table_open`

继续下钻核恒等式后，真正障碍变得更窄：逐点 primitive 核表的三条自然分支不能分开闭合。alpha row 公式与 signed 权重律都已回到 PDEC/CleanKLS 终端门；rank/multiplicity 分支又要求同一张 primitive source table。三腿分攻形成固定点。因此当前唯一非递归自足主攻点是`NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn`；它未被当前语料证明，行/列命题仍未无条件闭合。

```text
kernel_table_three_leg_return_sync_closed=true
alpha_formula_leg_returns_to_terminal=true
weight_identity_leg_returns_to_terminal=true
rank_multiplicity_leg_needs_same_primitive_table=true
three_leg_separate_attack_is_fixed_point=true
nonrecursive_pointwise_table_proved=false
row_column_unconditional_closed=false
```

## 1. 同步后严格基

```text
NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

并行直接终端基：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks) AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PostMertensFrontierImported` | `true` | `false` | 最新 post-Mertens 前沿把主攻点钉为同 formal-unit 核恒等式。 | SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion |
| `KernelIdentityReducedToPointwiseTable` | `true` | `false` | 核恒等式不能由记录守恒或几何 Phi 自动推出；必须先提交逐点 primitive 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `PointwiseTableSplitIntoThreeLegs` | `true` | `false` | 逐点核表被拆成 alpha row 发射公式、独立权重恒等式、同表 rank/multiplicity 证书。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `AlphaFormulaLegReturnsToTerminal` | `true` | `false` | alpha row 局部 unsigned 骨架、signed-lift 和 anchor 回流都已同步到 PDEC/CleanKLS 终端门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `WeightIdentityLegReturnsToTerminal` | `true` | `false` | signed 权重律经独立恒等式分类、moving-block/NC-BLK 回到同一终端门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `RankMultiplicityLegNeedsSamePrimitiveTable` | `true` | `false` | rank/multiplicity 分支需要 source table、complete key 与 fixed-pair fiber；这些又要求同一 primitive rows。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `ThreeLegSeparateAttackIsFixedPoint` | `true` | `true` | 三腿逐项攻击只会在 source table、alpha signed lift、PDEC/CleanKLS 之间循环。 | NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn |
| `NonrecursivePointwiseTableCurrentCorpusProved` | `false` | `false` | 当前语料没有一次性正向构造逐 primitive row 的 source tuple、signed weight、Phi atom、exact-UV rank 证书。 | NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn |
| `DirectTerminalParallelArmsStillOpen` | `true` | `false` | 并行终端路线仍可攻，但 PDEC 作用域匹配与自足 KZ/DLS 都未证明。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks |
| `RatePreservationStillOpen` | `false` | `false` | moving-atom packet 的 log-power 速率保持仍未证明。 | RatePreservationLedger_FOR_moving_atom_packet |
| `DStructureGateStillOpen` | `true` | `false` | DStructure/Tail-log4/finite Rankin 边界已命名但未独立接受。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 当前只证明三腿回流和最窄非递归表目标；尚未推出早期零行反例矛盾。 | NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 非递归表合同

必须在同一 formal unit、Cauchy/dispersion/terminal extraction 之前一次性列出 primitive rows：source tuple、anchor/phase、signed weight、exact `(u,v)`、Phi atom、local factor 非零、rank/multiplicity 证书和命名回流。不能分别从 alpha 局部公式、权重律或 rank 支路后验拼装。

若该非递归逐点表不给出，alpha、weight、rank 三腿分攻都会回到 PDEC/CleanKLS 固定点，不能闭合行/列命题。

## 4. 下一主攻点

```text
NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn
```
