# Prime Matrix strict 反分裂 joint declaration 防火墙

**状态：** `antisplit_joint_formula_reduced_to_atomic_declaration_with_split_firewall_open`

本步继续压缩反分裂 joint 公式。普通 `PreCauchyJointWordCoefficientEmitterDeclarationLine` 已经被既有证书同步到 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRule`，而后者会经 alpha-side、same-row、row-level 回到 signed-source 固定点。因此普通 declaration line 不足以闭合。真正最窄点必须是带 split firewall 的原子声明：`AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing`，声明行本身就要内置 rows formula、basis word/signed coefficient 同源、alpha/delta payload、prepushforward identity，并证明不降解到旧分裂链。当前语料没有该原子声明，行/列命题仍未无条件闭合。

```text
antisplit_formula_target_active=true
ordinary_joint_declaration_route_is_nonproof_cycle=true
atomic_antisplit_declaration_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 防火墙判定

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AntiSplitFormulaTargetActive` | `true` | `false` | 上一层已把新 joint 公式压成反分裂同排公式。 | NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection |
| `JointEmitterFieldsPointToDeclaration` | `true` | `false` | 联合发射公式字段层的第一普通字段是 pre-Cauchy joint declaration line。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `OrdinaryJointDeclarationReturnsToExplicitConstructor` | `true` | `false` | 普通 joint declaration 已同步到 explicit joint constructor rule；这不是反分裂出口。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `ExplicitConstructorRouteIsKnownFixedPoint` | `true` | `false` | explicit constructor 继续展开会经 alpha-side/same-row/row-level 回到 signed-source 固定点。 | cannot count as antisplit proof。 |
| `SeedCoordinateCycleStillBlocksReverseConstruction` | `true` | `true` | 坐标-来源闭环不能被普通 declaration 重命名后当作正向公式。 | AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing |
| `ExactUVParallelGateNotFormula` | `true` | `false` | ExactUV incidence 仍是并行守门项，不给 word/coefficient 原子声明。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `AtomicAntiSplitDeclarationCurrentCorpusProved` | `false` | `false` | 当前语料没有一条 declaration line 同时内置 rows formula、word/coefficient 同源、prepushforward identity 和 split firewall。 | AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 缺少原子反分裂声明、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。 | AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 原子声明字段

| field | requirement |
| --- | --- |
| `actual_source_tuple_domain` | 定义域必须是 actual noncanonical source tuple，不借 canonical、external 或 terminal 回流。 |
| `joint_rows_formula` | 声明行本身正向列出 primitive rows，而不是再调用 explicit joint constructor rule。 |
| `word_coefficient_pairing` | 每条 row 同时给出 basis word、signed coefficient 和二者同源恒等式。 |
| `alpha_delta_payload` | 同一 row 内置 alpha/delta pairing、exact `(u,v)`、branch key、sign/local factor。 |
| `prepushforward_identity` | 在 Cauchy、Phi、payment 推前前证明求和等于 actual emitter 系数。 |
| `split_firewall` | 证明该声明不降解为 explicit joint constructor -> alpha-side -> row-level 来源环。 |

## 3. 作者侧剩余基

```text
AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing
```
