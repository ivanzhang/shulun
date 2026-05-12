# Prime Matrix strict 显式 joint 构造器直接攻坚证书

**状态：** `explicit_joint_constructor_direct_attack_reduced_to_new_formula_or_terminal_descent_open`

本轮直接攻击 ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple：若沿现有 joint declaration / alpha-side / same-row / row-level 表继续展开，路线回到 signed-source 来源固定点，不能形成非循环证明。当前语料没有新的 actual joint alpha/delta 正向公式工件；因此该硬点没有闭合。下一最小可生产输入是 NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact，或者改走非循环替代 AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate。二者之外仍必须保留 ExactUV、RatePreservation 与 DStructure 门。

```text
joint_declaration_sync_imported=true
joint_rule_reduced_to_alpha_side=true
joint_alpha_side_route_returns_to_signed_source_fixed_point=true
new_explicit_joint_constructor_formula_artifact_present=false
explicit_joint_constructor_rule_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
rate_preservation_ledger_proved=false
dstructure_independent_gate_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 当前自回流链

| from | to |
| --- | --- |
| ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| JointAlphaSidePrimitiveWordCoefficientRuleLedger | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward |
| AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward | AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows |
| AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility | AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility |
| AcyclicSeedBasisWordFormulaFromSourceTupleParametersBeforeAdmissibility | AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters |
| AcyclicSeedWordCoordinateFormulaFromAnchorD0KOmegaPhaseParameters | AcyclicSeedSignedWeightCoordinateSlotLedger |
| AcyclicSeedSignedWeightCoordinateSlotLedger | AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords |
| AcyclicSeedSignedWeightSlotValueFormulaOnPrimitiveBasisWords | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| AcyclicSeedBasisWordToSignedCoefficientValueMapFormula | AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| AcyclicSeedBasisWordSignedCoefficientOriginIdentityBeforePushforward | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |

## 2. 新公式工件最低字段

| field | meaning |
| --- | --- |
| `domain` | actual noncanonical source tuple 的精确定义域，不能读取 canonical、terminal 或后验 payment 数据。 |
| `row_index_formula` | 同一 formal unit 内 alpha/delta primitive rows 的正向索引和排序公式。 |
| `basis_word_and_signed_coefficient` | 每一行同时输出 primitive basis word 与 signed coefficient，不能先分别生成再后验配对。 |
| `uv_branch_sign_local_factor` | 同一行同步输出 exact (u,v)、branch key、sign 与非零 local factor。 |
| `pre_cauchy_pairing_identity` | 在 Cauchy/dispersion/Phi 推前前证明 alpha/delta 两侧配成 actual emitter 系数。 |
| `failure_return_tags` | 缺行、零 local factor、跨来源、后验读取、超预算和 unmatched pair 必须落入已登记命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExplicitJointConstructorTargetActive` | `true` | `false` | pair-energy 非循环对齐与逐点核表字段合同都把首个生产性工件钉为显式 joint alpha/delta 构造器。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `JointDeclarationBoundaryImported` | `true` | `true` | 同一 source tuple 容器与 joint payload 字段边界已闭合。 | 字段边界不是构造公式。 |
| `JointConstructorReducedToAlphaSide` | `true` | `false` | 直接展开 TARGET 后，第一实际字段是 alpha-side primitive word/coefficient 规则。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `AlphaSideReducedToSameRow` | `true` | `false` | alpha-side 规则的未闭合处是 unsigned word skeleton 与 signed coefficient 在同一 pre-Cauchy row 上同源。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `SameRowReducedToRowLevelTable` | `true` | `false` | same-row 同源恒等式要求完整逐行 clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowLevelTableReducedToSignedEmitter` | `true` | `false` | 逐行表必须由无环 source seed 自带 signed row emitter 产生。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SignedSourceFixedPointImported` | `true` | `true` | 继续内部展开 signed row emitter 会回到 row-level/signed-source 来源固定点。 | 不能用固定点自证显式构造器。 |
| `JointConstructorCurrentRouteIsFixedPoint` | `true` | `true` | 现有 joint-alpha 路线已经被同步为回到 signed-source 固定点。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `NewExplicitFormulaArtifactPresent` | `false` | `false` | 当前语料没有提交新的 actual joint alpha/delta 正向公式工件。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `TerminalDescentAlternativeSchemaImported` | `true` | `false` | 若不提交新公式，唯一非循环替代是终端回流 well-founded 下降证书及其叶子防火墙。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `ExplicitJointConstructorRuleCurrentCorpusProved` | `false` | `false` | 当前直接攻坚未得到非循环构造公式，只得到固定点判定和精确剩余。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 没有显式新公式、终端下降、ExactUV、RatePreservation 和 DStructure 独立门，不能升级为无条件闭合。 | (NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 当前严格活动基

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件是对显式 joint 构造器的直接攻坚判定。它没有把固定点冒充为证明，也没有声称行/列命题已经无条件闭合。
