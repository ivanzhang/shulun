# Prime Matrix strict 非递归逐点 primitive 核表字段合同证书

**状态：** `nonrecursive_pointwise_kernel_table_field_contract_closed_constructor_rule_open`

本步把非递归逐点 primitive 核表从单一标签压成字段合同，并确认字段边界已闭合：合法证明必须在同一 formal unit、Cauchy/dispersion/Phi 推前之前一次性给出 rows、权重、`(u,v)`、Phi atom、local factor、rank 证书和回流栏。当前语料没有这张表；真正第一生产性硬点是 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple`。因此行/列命题仍未无条件自足闭合。

```text
field_contract_boundary_closed=true
nonrecursive_pointwise_table_proved=false
explicit_joint_alpha_delta_constructor_rule_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
rate_preservation_ledger_proved=false
dstructure_independent_gate_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn 不能由 alpha/weight/rank 三腿后验拼装；它要求同一 formal unit 的一张正向 primitive 表。所有活动链条交到同一个第一生产性原子 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple`：没有这条显式 joint constructor rule，primitive row index、signed weight、exact-UV/Phi atom、local factor、rank/multiplicity 和 named return 都没有共同载体。

## 2. 非递归表字段合同

| field | meaning | atom |
| --- | --- | --- |
| `primitive_row_index_set` | 同一 formal unit 内 primitive rows 的有限索引集合。 | AlphaPrimitiveRowIndexSetLedger |
| `source_tuple_to_anchor_phase_row_formula` | 从 actual source tuple 到 anchor/phase row 的显式发射公式。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| `same_row_word_coefficient_payload` | 同一行同时输出 basis word、signed coefficient、branch key、u/v、sign/local factor。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `signed_weight_arithmetic_identity` | 推前前 signed 权重必须来自独立 noncanonical 算术恒等式。 | IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger |
| `exact_uv_phi_atom_output` | 每行同步输出 exact `(u,v)` 与 Phi/payment atom，不能后验补配。 | JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger |
| `local_factor_nonzero_and_sign` | 非零 local factor、符号和 branch refinement 与 row 同步。 | AlphaWeightNonzeroSignLocalFactorLedger |
| `rank_multiplicity_certificate` | 同一张表上证明 exact-UV bounded multiplicity/rank。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `named_return_discipline` | 缺行、零权、跨来源、后验读取、超预算等失败必须命名回流。 | JointConstructorFormulaFailureReturnTagsLedger AND SourceTableNoDownstreamRecoveryAndNamedReturnLedger |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NonrecursivePointwiseTableTargetActive` | `true` | `false` | 上一层三腿回流已把核表缺口压成非递归逐点表。 | NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn |
| `FieldContractBoundaryPinned` | `true` | `true` | 所有合法字段必须在同一 formal unit、Cauchy/dispersion/Phi 推前之前一次性给出。 | 字段边界闭合，不等于表构造已证明。 |
| `SameSourceTupleContainerReady` | `true` | `true` | formal unit/source tuple 容器可承载同一行 word/coefficient/u/v/hash。 | 容器不产生 primitive row。 |
| `ActualJointConstructorRuleMissing` | `true` | `false` | actual noncanonical constructor 必须显式把 source tuple 映到 joint primitive row；当前没有公式。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `AlphaIndexAndEmissionFormulaMissing` | `true` | `false` | alpha row 索引集合、anchor/phase 发射公式、有限排序和无后验选择仍未证明。 | AlphaPrimitiveRowIndexSetLedger AND AlphaRowAnchorPhaseEmissionFormulaLedger AND AlphaRowFiniteMultiplicityOrderingLedger AND AlphaEmissionMapNoDownstreamChoiceLedger AND AlphaEmissionMapNamedReturnLedger |
| `SameRowWordCoefficientOriginMissing` | `true` | `false` | unsigned skeleton 与 signed coefficient 不能分别拼接；必须同一 row 同源。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands -> AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SignedWeightArithmeticIdentityMissing` | `true` | `false` | signed 权重律仍缺独立 pre-Cauchy 算术恒等式、精确权重公式和非零 local factor。 | IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND ExactAlphaSignedWeightFormulaLedger AND AlphaWeightNonzeroSignLocalFactorLedger AND AlphaWeightNoZeroRowGeometryOrPaymentRecoveryLedger AND AlphaWeightLawFailureNamedReturnLedger |
| `ExactUVRankMultiplicityStillOpen` | `true` | `false` | fixed-pair/key 形式门已定位，但 actual bounded multiplicity incidence 未证明。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `NamedReturnDisciplineIncomplete` | `true` | `false` | 缺行、零 local factor、跨来源、超预算或后验读取的回流栏尚未与同一公式行合取。 | JointConstructorFormulaFailureReturnTagsLedger AND SourceTableNoDownstreamRecoveryAndNamedReturnLedger AND AlphaEmissionMapNamedReturnLedger AND AlphaWeightLawFailureNamedReturnLedger |
| `NoTerminalReturnCurrentlyUnproved` | `true` | `false` | 现有内部路线仍会回到 terminal/source 固定点；非递归表必须由正向公式破环。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `NonrecursivePointwiseTableCurrentCorpusProved` | `false` | `false` | 当前语料只闭合字段边界和伪出口排除，没有提交同一张非递归 primitive 核表。 | NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 尚未推出早期零行反例链与真实结构链的终端矛盾。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一真正单点

```text
ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
```

构造器之后仍需并行验收：

```text
ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

当前最小生产性基：

```text
(ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple AND JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger AND JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger AND SameFormalUnitPreCauchyTimestampLockLedger AND NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger AND JointConstructorFormulaFailureReturnTagsLedger AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```
