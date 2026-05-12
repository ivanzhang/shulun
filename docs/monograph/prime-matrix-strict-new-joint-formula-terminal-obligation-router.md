# Prime Matrix strict 新显式 joint 公式终端义务

**状态：** `new_joint_formula_terminal_obligation_open_no_current_internal_formula_artifact`

当前 strict 内部路线已压到真正终端公式义务：必须提交一个新的显式 actual joint alpha/delta primitive word/coefficient 构造公式。已有 declaration、alpha-side、same-row、row-level、signed-emitter 材料只能形成固定点，不能生产该公式；terminal descent 替代路线也已是宏循环。因此目标命题作者侧无条件闭合尚未完成，最后数学输入就是 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`，并需同时通过 ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 守门项。

```text
new_joint_formula_is_current_internal_noncycle_target=true
old_joint_constructor_route_returns_to_signed_source_fixed_point=true
new_explicit_joint_constructor_formula_artifact_present=false
explicit_joint_constructor_rule_proved=false
terminal_descent_alternative_is_macrocycle=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CurrentStrictInternalNoncycleTarget` | `true` | `false` | seed-cycle-cut 与 PDEC 作用域分支饱和后，唯一内部非循环主攻点是新显式 joint 公式。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `ExistingDirectAttackImported` | `true` | `false` | 已有 direct attack 证明：继续展开旧 TARGET 会回到 signed-source 固定点。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `DeclarationIsNotFormula` | `true` | `false` | source tuple 容器、字段边界、payload 名称都不是正向 coefficient 公式。 | 需要 actual formula。 |
| `OldJointRuleReducesToAlphaSide` | `true` | `false` | 旧 joint rule 的首字段仍是 alpha-side primitive word/coefficient ledger。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `AlphaSideReducesToSameRow` | `true` | `false` | alpha-side 需要同一 pre-Cauchy row 上 basis word 与 signed coefficient 同源。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `SameRowReducesToRowLevel` | `true` | `false` | same-row 同源恒等式仍要求逐行原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowLevelReturnsToSignedEmitter` | `true` | `false` | row-level 表继续要求 signed row emitter。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SignedEmitterRouteIsFixedPoint` | `true` | `true` | signed row emitter 的内部展开已经登记为 signed-source 固定点。 | 不能用固定点替代新公式。 |
| `TerminalDescentAlternativeIsMacrocycle` | `true` | `false` | 没有新公式时的终端下降替代已是 terminal-source-pair-joint 宏循环。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `PairEnergyDoesNotSupplyFormula` | `true` | `false` | pair-energy 抽象输入不能生产逐行 joint formula；它也回到 source entropy/joint constructor 固定点。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `NewFormulaArtifactPresent` | `false` | `false` | 当前仓库没有提交满足六字段合同的显式新公式工件。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 缺少新公式以及 ExactUV/模型余量/Rate/DStructure 验收门，作者侧无条件闭合尚未完成。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 公式字段合同

| field | requirement |
| --- | --- |
| `actual_noncanonical_source_tuple_domain` | 在 Cauchy、dispersion、terminal extraction、payment 推前前定义；不得由零行或 payment 数据反推。 |
| `joint_row_index_and_formal_unit` | 每个 primitive row 属于同一 formal unit，并给出 alpha/delta 两侧共同索引。 |
| `basis_word_formula` | 从 source tuple 正向输出 primitive basis word 坐标，而非后验选择。 |
| `signed_coefficient_formula` | 同一行同时输出 signed coefficient、sign、local factor 和非零条件。 |
| `uv_phi_pairing` | 同步给出 exact (u,v)、Phi atom，并证明推前前 alpha/delta pairing 恒等式。 |
| `budget_and_failure_return` | 给出总变差、branch key、rank/multiplicity 预算；失败必须落入命名回流。 |

## 3. 作者侧剩余基

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻仍是：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```
