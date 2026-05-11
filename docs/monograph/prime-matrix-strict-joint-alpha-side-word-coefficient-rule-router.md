# Prime Matrix strict joint alpha-side word/coefficient 规则路由器

**状态：** `joint_alpha_side_rule_reduced_to_same_row_word_coefficient_origin_identity_open`

本步继续下钻 joint alpha-side 规则：已有材料可登记 carry-shell/anchor/phase 的 unsigned skeleton，也已把 signed expression 压到 origin identity，但二者尚未在同一 primitive row 上桥接。joint 规则必须证明同一 source tuple 同时产生 primitive basis word、signed coefficient、`(u,v)`、branch key、sign/local factor，并在失败时命名回流。该 same-row 桥接当前未证明，行/列命题仍未无条件闭合。

```text
joint_alpha_side_word_coefficient_rule_router_closed=true
unsigned_carry_shell_skeleton_registered=true
signed_expression_reduced_to_origin_identity=true
joint_alpha_same_row_word_coefficient_origin_identity_proved=false
joint_alpha_side_primitive_word_coefficient_rule_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`JointAlphaSidePrimitiveWordCoefficientRuleLedger` 的真正难点不是单独生成 alpha unsigned row，也不是单独命名 signed coefficient；而是证明二者在同一 pre-Cauchy primitive row 上同源。因此下一原子为 `JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward`。

## 2. same-row 桥接字段

| field | meaning |
| --- | --- |
| `same_source_tuple_row_id` | 同一 formal unit/source tuple 下的 alpha primitive row 标识。 |
| `carry_shell_word_binding` | 把 unsigned carry-shell/anchor/phase skeleton 绑定为 primitive basis word。 |
| `signed_coefficient_origin_identity` | 同一行给出 signed coefficient 的 pre-Cauchy 来源恒等式。 |
| `uv_key_sign_local_factor_payload` | 同一行同步输出 exact `(u,v)`、branch key、sign 和 local factor。 |
| `prepushforward_validity` | word 与 coefficient 在 Phi/payment 推前之前已经同源成立。 |
| `named_return` | 缺 word、缺 coefficient、零 local factor、过载、后验读取或跨来源泄漏必须命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `JointAlphaSideTargetActive` | `true` | `false` | 上一层 joint explicit alpha/delta 规则已把首字段压成 joint alpha-side word/coefficient rule。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `BroadAlphaSideRuleImported` | `true` | `true` | 普通 alpha-side primitive rule 已拆成定义域、发射映射、权重公式、row payload 和回流。 | joint 版需要把 word 与 coefficient 同行合并。 |
| `DeterministicAlphaMapStillOpen` | `true` | `false` | 确定性 alpha row map 仍未给出完整 row 发射，但后续 unsigned skeleton 已说明几何骨架可登记。 | JointAlphaCarryShellSkeletonToPrimitiveBasisWordBindingLedger |
| `UnsignedCarryShellSkeletonRegistered` | `true` | `true` | carry-shell、P列锚、anchor-collar 和 layered-wheel 已给出 alpha row 的 unsigned skeleton。 | 只给 word/skeleton 形状，不给 signed coefficient。 |
| `AnchorPhaseFormulaStillNeedsSignedLiftAndReturn` | `true` | `false` | alpha anchor/phase 公式已压到 signed coefficient lift 与 anchor-collar overload return。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward AND AlphaFormulaAnchorCollarOverloadNamedReturnLedger |
| `SignedExpressionReducedToOriginIdentity` | `true` | `false` | 逐 summand signed expression 已被压成 signed coefficient origin identity。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |
| `SignedPayloadStillOpen` | `true` | `false` | signed lift、逐点 signed weight expression 和 origin identity 都未证明。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |
| `SameSourceTupleContainerAvailable` | `true` | `true` | formal unit/source tuple 容器可用于同行绑定 word 与 coefficient。 | 容器不是桥接证明。 |
| `PointwiseKernelNeedsSameRows` | `true` | `false` | 逐点 primitive 核表同样要求行公式、权重恒等式和 rank 证书在同一行上对齐。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `DownstreamReverseRecoveryBlocked` | `true` | `true` | payment、零行覆盖、来源环和有限投影不能反推出 same-row signed payload。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `SameRowBridgeCurrentCorpusProved` | `false` | `false` | 当前材料没有证明 unsigned primitive word skeleton 与 signed coefficient origin identity 是同一 pre-Cauchy row。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `JointAlphaSideRuleCurrentCorpusProved` | `false` | `false` | 没有 same-row 桥接，joint alpha-side primitive word/coefficient rule 仍未证明。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |

## 4. 下一真正单点

首攻：

```text
JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward
```

完整 joint alpha-side 生产性基：

```text
JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward AND JointAlphaCarryShellSkeletonToPrimitiveBasisWordBindingLedger AND PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward AND JointAlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaFormulaAnchorCollarOverloadNamedReturnLedger AND JointAlphaSideRuleFailureNamedReturnLedger
```

保留终端下降并行门后的当前严格自足基：

```text
((JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward AND JointAlphaCarryShellSkeletonToPrimitiveBasisWordBindingLedger AND PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward AND JointAlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaFormulaAnchorCollarOverloadNamedReturnLedger AND JointAlphaSideRuleFailureNamedReturnLedger) OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只证明 joint alpha-side 规则的最窄剩余是 same-row word/coefficient 桥接；它没有证明该桥接，也没有证明行/列命题无条件闭合。
