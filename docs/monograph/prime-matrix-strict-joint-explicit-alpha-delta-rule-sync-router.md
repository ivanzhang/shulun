# Prime Matrix strict joint 显式 alpha/delta 规则同步路由器

**状态：** `explicit_joint_alpha_delta_rule_reduced_to_joint_alpha_side_rule_open`

本步把 explicit joint alpha/delta rule 与已有普通 explicit alpha/delta 两侧拆分同步：source tuple 与 unsigned alpha 几何只能提供输入和骨架，不能生成 signed payload。joint 规则必须先给 alpha-side 的 primitive word/coefficient 正向发射规则；没有它，delta-side、Cauchy 前配对、非零/local factor 和回流都无对象。当前仍未闭合行/列命题。

```text
joint_explicit_alpha_delta_rule_sync_router_closed=true
joint_alpha_side_primitive_word_coefficient_rule_proved=false
explicit_joint_alpha_delta_constructor_rule_proved=false
pre_cauchy_joint_declaration_line_proved=false
joint_basis_word_coefficient_emitter_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple` 不是普通 alpha/delta 规则的简单复述；它要求 alpha/delta 两侧每条 primitive row 都携带同一 source tuple 下的 basis word 与 signed coefficient payload。因此第一真正单点压成 `JointAlphaSidePrimitiveWordCoefficientRuleLedger`。

## 2. joint 规则字段

| field | meaning |
| --- | --- |
| `joint_alpha_side_rule` | 从同一 source tuple 正向发射 alpha-side primitive basis word、signed coefficient 与 row payload。 |
| `joint_delta_side_rule` | 从同一 source tuple 正向发射 delta-side primitive basis word、signed coefficient 与 row payload。 |
| `same_word_coefficient_payload` | 每条 primitive row 的 word、coefficient、branch key、u/v、sign 和 local factor 同时产生。 |
| `pre_cauchy_pairing_identity` | alpha/delta 两侧在 Cauchy 前配对为同一个 actual emitter 系数。 |
| `nonzero_and_return_discipline` | 零 local factor、符号冲突、多值、超预算、后验读取或 unmatched pair 必须命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExplicitJointRuleTargetActive` | `true` | `false` | 上一层 joint declaration/constructor 同步已把首个生产性公式压成 explicit joint alpha/delta rule。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `BroadAlphaDeltaTwoSideSplitImported` | `true` | `true` | 已有显式 alpha/delta 规则证书说明普通规则必须拆成 alpha-side、delta-side、pairing 和 nonzero/sign/local factor。 | joint 版继承此两侧结构。 |
| `SourceTupleContainerStillOnlyContainer` | `true` | `true` | formal unit/source tuple 只给输入容器和锚参数，不自动给 primitive row 规则。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `UnsignedAlphaGeometryImportedButNotSignedPayload` | `true` | `true` | carry-shell、anchor/phase、P列锚与层叠轮等 unsigned alpha 几何可登记，但不产生 signed coefficient。 | signed payload 仍需 joint alpha-side 规则。 |
| `AlphaSideGenericRuleStillOpen` | `true` | `false` | 普通 alpha-side primitive rule 和 deterministic alpha row emission map 尚未证明。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `SignedPayloadStillOpen` | `true` | `false` | alpha signed weight law 与逐点 signed weight expression 仍未给出 exact signed coefficient。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `DownstreamRecoveryStillBlocked` | `true` | `true` | payment 反推、零行覆盖和终端证书不能替代 joint alpha/delta 规则。 | JointAlphaDeltaRuleFailureNamedReturnLedger |
| `JointRuleNeedsPayloadStrongerThanBroadRule` | `true` | `true` | joint 规则比普通 alpha/delta 规则更强：每侧发射时必须同时带 basis word 与 signed coefficient payload。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `JointAlphaSidePrimitiveRuleCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出 source tuple 到 alpha-side joint primitive word/coefficient row 的正向规则。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `ExplicitJointAlphaDeltaRuleCurrentCorpusProved` | `false` | `false` | 缺 joint alpha-side 首规则时，delta-side、pairing、nonzero/local factor 和回流不能合取闭合。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |

## 4. 下一真正单点

首攻：

```text
JointAlphaSidePrimitiveWordCoefficientRuleLedger
```

完整 joint explicit alpha/delta 生产性基：

```text
JointAlphaSidePrimitiveWordCoefficientRuleLedger AND JointDeltaSidePrimitiveWordCoefficientRuleLedger AND JointAlphaDeltaPairingCompatibilityBeforeCauchyLedger AND JointPrimitiveWordCoefficientNonzeroSignLocalFactorLedger AND JointAlphaDeltaRuleFailureNamedReturnLedger
```

保留终端下降并行门后的当前严格自足基：

```text
((JointAlphaSidePrimitiveWordCoefficientRuleLedger AND JointDeltaSidePrimitiveWordCoefficientRuleLedger AND JointAlphaDeltaPairingCompatibilityBeforeCauchyLedger AND JointPrimitiveWordCoefficientNonzeroSignLocalFactorLedger AND JointAlphaDeltaRuleFailureNamedReturnLedger) OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只完成 joint 显式规则的两侧同步和首字段定位；没有证明 joint alpha-side 规则，也没有证明行/列命题无条件闭合。
