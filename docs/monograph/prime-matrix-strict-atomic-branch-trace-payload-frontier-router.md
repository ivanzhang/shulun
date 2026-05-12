# Prime Matrix strict atomic branch trace signed payload 前沿

**状态：** `exact_atomic_branch_trace_reduced_to_signed_payload_constructor_open`

本步直接攻击 `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`。已有 branch trace 审查表明：可见坐标 trace 可以沿 anchor、D0/K/Omega、phase 和 word-coordinate 链定位，但 signed payload trace 会经 signed slot、coefficient assignment、value map 和 origin identity 回到 row-level 表。atomic 限制只缩小输入域，不能自动产生 signed coefficient。因此真正最窄字段压成 `AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`：在同一 atomic trace 上正向给出 orientation、signed coefficient、local factor、same-row identity、alpha/delta prepushforward identity、exact UV/key 和命名回流。当前材料没有该 payload constructor，行/列命题仍未无条件闭合。

```text
actual_trace_cycle_imported=true
visible_coordinate_trace_reduced_to_word_coordinate_chain=true
signed_payload_trace_returns_to_row_level_origin_table=true
payload_constructor_conditionally_suffices=true
atomic_signed_payload_constructor_proved=false
exact_atomic_joint_branch_trace_signed_coefficient_formula_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. signed payload 字段

| field | requirement |
| --- | --- |
| `payload_domain` | 同一 atomic joint row 的 visible trace 已给出，payload 必须绑定这条 trace。 |
| `orientation_parity` | 给出 primitive orientation bit，证明它早于 Cauchy/Phi/payment 且不是 payment 反推。 |
| `signed_coefficient_value` | 给出 signed coefficient 的闭式或有限递推值，不能调用 row-level origin table。 |
| `local_factor_product` | 列出筛因子、截断因子、branch local factor 与非零条件。 |
| `word_coefficient_same_row_identity` | 证明 basis word 与 signed coefficient 是同一 trace 的两个字段。 |
| `alpha_delta_prepushforward_identity` | 证明 payload 在 Phi/payment 推前前等于 actual alpha/delta 贡献。 |
| `uv_key_payload` | 同步输出 exact `(u,v)`、branch key、sign 和 local factor 口径。 |
| `payload_return_tags` | 缺 payload、零 local factor、符号冲突、超预算、canonical 泄漏或后验读取必须命名回流。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExactAtomicTraceTargetActive` | `true` | `false` | 上一层已把 BuiltIn pairing 闭式压成 exact atomic joint branch trace。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `ActualTraceCycleImported` | `true` | `true` | actual noncanonical branch trace 的内部展开已被证明不能自证 signed payload。 | atomic specialization inherits this obstruction。 |
| `TraceSplitsIntoCoordinateAndPayload` | `true` | `true` | 完整 trace 分为 visible coordinate trace 与 signed payload trace；只有前者已定位。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `VisibleCoordinateTraceDoesNotEmitPayload` | `true` | `true` | anchor/D0/K/Omega/phase/word-coordinate 只给 row 与 word 的可见坐标，不产生 orientation 或 signed coefficient。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `SignedPayloadAssignmentChainReturnsToOrigin` | `true` | `true` | signed slot -> slot value -> coefficient assignment -> value map -> origin identity 继续回到 row-level 表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `OrientationAndSameRowLawsStillDemandPayload` | `true` | `false` | 取向/local factor 与 same-row word/coefficient 桥接都要求 payload 正向生成。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `AtomicRestrictionDoesNotCreateSignedPayload` | `true` | `true` | 把 actual trace 限制到 atomic joint rows 只缩小输入域；不会凭空产生 signed coefficient 值。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `PayloadConstructorWouldCloseAtomicTraceConditionally` | `true` | `true` | 若 signed payload constructor 给出 orientation、coefficient、local factor、same-row identity 和回流，则 atomic trace 条件闭合。 | prove AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `TraceSelfProofAlreadyRemovedFromGlobalFrontier` | `true` | `true` | 全局前沿已把 branch trace 自证从活动证明路径删除。 | new payload input or nontrace terminal atom。 |
| `ActualEmitterExactUVStillParallel` | `true` | `false` | payload 可登记每行 UV；bounded multiplicity incidence 仍需独立证明。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `AtomicSignedPayloadConstructorCurrentCorpusProved` | `false` | `false` | 当前材料没有给出不经 assignment/origin 环的 atomic signed payload trace constructor。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `ExactAtomicTraceCurrentCorpusProved` | `false` | `false` | 缺少 signed payload constructor，ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn 未证明。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 缺少 atomic signed payload、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 作者侧剩余基

```text
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
```
