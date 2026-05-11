# Prime Matrix strict 联合 declaration/constructor 同步路由器

**状态：** `joint_declaration_line_reduced_to_explicit_joint_constructor_rule_open`

本步把 joint declaration line 与已有 pre-Cauchy declaration/actual constructor 线同步：它不是新的来源类，也不能由 canonical、generic WFD、外部谱、payment 反推或早期零行几何填充。合法闭合必须给出显式 joint alpha/delta primitive constructor rule，并在同一行输出 basis word、signed coefficient、branch key、u/v、sign 与 local factor。该规则当前未证明，行/列命题仍未无条件闭合。

```text
joint_declaration_constructor_sync_router_closed=true
same_source_tuple_container_closed=true
explicit_joint_alpha_delta_constructor_rule_proved=false
pre_cauchy_joint_declaration_line_proved=false
joint_basis_word_coefficient_emitter_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿同步

`PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple` 与已有 broad `PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` 是同一声明行，区别只在 joint payload：同一 actual source tuple 必须同时发射 primitive basis word 与 signed coefficient。因此首个生产性硬点变为 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple`。

## 2. 显式规则字段

| field | role |
| --- | --- |
| `explicit_joint_alpha_delta_rule` | 第一开口；在 pre-Cauchy 层把 source tuple 映到 alpha/delta primitive row。 |
| `same_source_tuple_domain` | 定义域必须正好是当前 actual noncanonical clean-core source tuple，而不是 canonical 或 generic WFD。 |
| `basis_word_and_coefficient_row_emission` | 同一公式行必须同时输出 primitive basis word、signed coefficient、branch key、u/v、sign 和 local factor。 |
| `timestamp_and_no_leak_lock` | 公式发生在 Cauchy/dispersion/payment/Phi 之前，且不读取 canonical/external/后验数据。 |
| `failure_return_tags` | 公式缺失、多值、零 local factor、超预算、thin/rejected/cancelling 时必须命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `JointDeclarationLineTargetActive` | `true` | `false` | 上一层 joint-emitter 字段证书已把第一生产性原子钉为 joint declaration line。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `BroadPreCauchyDeclarationFilterImported` | `true` | `true` | 已有 declaration line 分类已排除 canonical、generic WFD、external、unregistered/mixed 伪声明。 | joint 版继承同一分类，不另开来源类。 |
| `ActualConstructorFormulaLineRouterImported` | `true` | `true` | 已有 actual constructor formula line 证书把 broad 声明行压到显式 alpha/delta primitive constructor rule。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `SameSourceTupleContainerClosed` | `true` | `true` | formal unit/source tuple 容器已闭合；joint 版只是要求同一容器同时发射 word 与 coefficient。 | JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger |
| `FakeSourceFilterStillBlocksShortcuts` | `true` | `true` | canonical、generic WFD、外部谱、未登记来源都不能替代 joint constructor rule。 | NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger |
| `ReverseAndZeroRowStillCannotSupplyJointRule` | `true` | `true` | payment 反推和早期零行 unsigned 几何不能生成 signed word/coefficient 联合规则。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `OriginAdmissionIsNotFormula` | `true` | `false` | 来源准入/构造器分类只能说明合法入口形态，仍没有写出实际 joint alpha/delta 规则。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `JointPayloadRequirementPinned` | `true` | `true` | joint 目标要求显式规则不仅给 alpha/delta 行，还要在同一行输出 basis word 与 signed coefficient。 | JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger |
| `TimestampAndNoLeakStillParallel` | `true` | `false` | pre-Cauchy 时间戳锁和 noncanonical no-leak 纪律仍需与显式规则并行证明。 | SameFormalUnitPreCauchyTimestampLockLedger AND NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger |
| `ExplicitJointConstructorRuleCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出从 actual noncanonical source tuple 到 joint primitive row 的显式 alpha/delta 规则。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `PreCauchyJointDeclarationLineCurrentCorpusProved` | `false` | `false` | 显式规则、同源定义域、行输出、时间戳/no-leak 和回流标签尚未合取闭合。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |

## 4. 下一真正单点

首攻：

```text
ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
```

完整 joint declaration 生产性基：

```text
ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple AND JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger AND JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger AND SameFormalUnitPreCauchyTimestampLockLedger AND NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger AND JointConstructorFormulaFailureReturnTagsLedger
```

保留终端下降并行门后的当前严格自足基：

```text
((ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple AND JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger AND JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger AND SameFormalUnitPreCauchyTimestampLockLedger AND NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger AND JointConstructorFormulaFailureReturnTagsLedger) OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只证明 joint declaration 与 actual constructor 线的精确对接，没有证明显式 joint constructor rule，也没有证明行/列命题无条件闭合。
