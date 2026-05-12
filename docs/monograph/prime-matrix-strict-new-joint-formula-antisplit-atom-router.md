# Prime Matrix strict 新 joint 公式反分裂原子

**状态：** `new_joint_formula_reduced_to_antisplit_joint_row_formula_open`

本步直接攻 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 的内部形态。若新公式沿旧路线先拆成 explicit alpha/delta、alpha-side、deterministic row map、anchor-phase、signed lift、signed value、origin table，则会回到 row-level/signed-source 坐标来源环，不能算新公式。因此真正最窄原子不是再展开旧 alpha-side 链，而是一个反分裂公式：`NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection`，它必须在同一行同时输出basis word、signed coefficient、alpha/delta pairing、exact `(u,v)`、key、sign/local factor，且证明不经已登记固定点。当前语料没有该工件，命题仍未无条件闭合。

```text
new_formula_target_active=true
old_split_formula_route_synced=true
old_split_formula_route_is_nonproof_cycle=true
antisplit_joint_formula_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 分裂路线同步

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NewFormulaTerminalObligationActive` | `true` | `false` | 上一层已把 strict 内部非循环点压成新显式 joint 公式工件。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `OldFormulaLineSplitsToExplicitAlphaDelta` | `true` | `false` | 旧 actual constructor formula line 先拆成显式 alpha/delta primitive rule。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| `ExplicitAlphaDeltaSplitsToAlphaSide` | `true` | `false` | 显式 alpha/delta 规则又先要求 alpha-side primitive rule；delta/pairing 还没有对象。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger |
| `AlphaSideSplitsToDeterministicRowMap` | `true` | `false` | alpha-side 规则压到确定性 alpha row 发射映射。 | DeterministicAlphaPrimitiveRowEmissionMapLedger |
| `DeterministicRowMapSplitsToAnchorPhase` | `true` | `false` | 确定性发射映射的首缺口是把 A/D0/K/Omega/phase_rule 变成 alpha row。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| `AnchorPhaseHasOnlyUnsignedSkeleton` | `true` | `false` | carry-shell、P列锚、相位轮等只给 unsigned skeleton；signed coefficient 仍开放。 | AlphaFormulaSignedCoefficientLiftLedger |
| `SignedLiftSplitsToPointwiseValueTable` | `true` | `false` | signed lift 等价于逐 skeleton row 的 signed alpha value table。 | PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton |
| `SignedValueRouteReturnsToOriginTable` | `true` | `false` | signed value 继续展开会回到 primitive origin identity 与 row-level 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowLevelReturnsToSeedCoordinateCycle` | `true` | `false` | row-level/signed-emitter 路线回到 signed 坐标-来源依赖环。 | cannot count as new formula。 |
| `ExactUVDoesNotSupplyFormula` | `true` | `false` | ExactUV incidence 是并行守门项；它不生产 basis word/coefficient joint formula。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `AntiSplitFormulaCurrentCorpusProved` | `false` | `false` | 当前材料没有提交不经 alpha-side/row-level/signed-source 分裂路径的 joint primitive row 公式。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 反分裂 joint 公式、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 均未合取闭合。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 反分裂字段

| field | requirement |
| --- | --- |
| `single_row_source_tuple` | 同一 actual noncanonical source tuple 在同一 formal unit 内直接生成 joint primitive row。 |
| `basis_word_and_signed_coefficient_together` | 同一公式同时输出 basis word 与 signed coefficient；不得先走 alpha-side word 再后验补 coefficient。 |
| `alpha_delta_pairing_payload` | 同一行直接携带 alpha/delta 两侧 pairing 数据，而不是由 row-level 表或 signed-source 固定点回推。 |
| `uv_key_sign_local_factor` | 同步输出 exact `(u,v)`、branch key、sign/local factor 和非零条件。 |
| `prepushforward_identity` | 在 Cauchy、Phi、payment 推前前证明该行贡献等于 actual emitter 系数。 |
| `no_split_certificate` | 证明该构造不因分裂为 alpha-side/row-level/signed-source 路径而回到已登记固定点。 |

## 3. 作者侧剩余基

```text
NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection
```
