# Prime Matrix strict 内置 signed pairing 闭式前沿

**状态：** `builtin_signed_pairing_reduced_to_exact_atomic_joint_branch_trace_open`

本步继续直接攻击 `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`。已闭合的 unsigned skeleton 只给 atomic row 的位置和相位；signed coefficient 是取向/local factor 敏感的奇数据，不能由偶几何、Möbius/奇偶影子或 signed-value 旧链后验生成。旧链会回到 row-level origin table，因此不能作为 atomic 内置闭式。真正非循环前沿压成 `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`：对每条 atomic joint row，在同一 formal unit 和 Cauchy/Phi/payment 前完整列出 branch trace，并同步给出 basis word、signed coefficient、alpha/delta pairing、orientation/local factor、exact UV 和回流。当前语料没有该 trace 公式，行/列命题仍未无条件闭合。

```text
unsigned_joint_row_skeleton_closed=true
old_signed_value_route_circular=true
orientation_branch_trace_reduction_synced=true
branch_trace_conditionally_suffices=true
exact_atomic_joint_branch_trace_signed_coefficient_formula_proved=false
builtin_signed_coefficient_pairing_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 本步压缩引理

| lemma | statement |
| --- | --- |
| `ClosedFormNeedsOddData` | unsigned carry-shell、P列锚、相位轮和 ExactUV 支撑只是不带符号的偶数据；signed coefficient 对 primitive orientation/local factor 反变，因此闭式值必须包含奇数据来源。 |
| `OldSignedValueRouteIsCircular` | 从 pointwise signed value 继续展开会经过 signed weight、primitive expression、origin identity，最终回到 row-level origin table；该路径不能证明 atomic 内置闭式。 |
| `BranchTraceSufficesConditionally` | 若每条 atomic joint row 都有 Cauchy 前完整 branch trace，且 trace 同时给出 word、signed coefficient、orientation/local factor、alpha/delta payload 与 exact UV，则内置 pairing 闭式条件闭合。 |
| `MobiusParityShadowIsNotEnough` | Möbius/奇偶只给局部符号影子；缺 actual source tuple、ordered branch trace、exact UV 和命名回流，不能替代 strict 内部闭式公式。 |

## 2. atomic branch trace 字段

| field | requirement |
| --- | --- |
| `atomic_row_domain` | 输入是已登记 unsigned carry-shell/phase skeleton 的 atomic joint row，而不是 payment 侧纤维。 |
| `same_formal_unit_trace` | source tuple、basis word、signed coefficient、alpha/delta pairing 与 return tag 共享同一 formal unit。 |
| `ordered_branch_operations` | 在 Cauchy/Phi/payment 前给出有限有序 branch trace；不得由 row-level origin table 后验读取。 |
| `signed_coefficient_closed_value` | signed coefficient 是 trace 中 orientation、truncation 和 local factor product 的闭式函数。 |
| `word_coefficient_pairing` | 证明 primitive basis word 与 signed coefficient 是同一 trace 的两面，而不是两条链拼接。 |
| `alpha_delta_payload` | 同一 row 携带 alpha/delta 两侧 payload 和 prepushforward sum identity。 |
| `exact_uv_branch_key` | 同步输出 exact `(u,v)`、branch key、sign/local factor 和非零条件。 |
| `named_return_tags` | 缺 trace、零 local factor、符号冲突、超预算、canonical 泄漏或后验读取必须命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BuiltInPairingTargetActive` | `true` | `false` | 上一层已把 atomic joint rows 公式压成内置 signed coefficient/pairing 闭式。 | BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows |
| `UnsignedSkeletonImported` | `true` | `true` | carry-shell、P列锚、相位轮和 row skeleton 可作为 atomic row 输入域。 | 输入域闭合，不给 signed 值。 |
| `OddSignedDataStillMissing` | `true` | `true` | 已登记的偶几何数据在取向翻转下不变，不能决定 signed coefficient。 | PrimitiveOrientationLocalFactorProductLawBeforePushforward |
| `OldSignedValueRouteCircular` | `true` | `false` | pointwise signed value 旧链会回到 row-level origin table，不能作为 atomic 声明内置闭式。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `SameRowBridgeNeeded` | `true` | `false` | unsigned primitive word 与 signed coefficient 必须在同一 pre-Cauchy row 上同源。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `OrientationReducedToBranchTrace` | `true` | `false` | 取向/local factor 律已压成 actual noncanonical 完整 branch trace 公式或命名回流。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| `MobiusParityNotExactPairingFormula` | `true` | `true` | Möbius 截断和奇偶审计只是符号影子，不含 exact trace、UV、branch key 和回流。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `PointwiseKernelContractDemandsOneTable` | `true` | `true` | 非递归逐点核表要求 rows、weight、UV、local factor、rank 和回流在同一 formal unit 一次性给出。 | atomic trace table。 |
| `BranchTraceWouldCloseBuiltinPairingConditionally` | `true` | `true` | 若 atomic branch trace 正向给出 word/coefficient/pairing/local factor，则 BuiltIn pairing 闭式不再依赖 origin table。 | prove ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `ActualEmitterExactUVStillParallel` | `true` | `false` | branch trace 可输出每行 UV，但 bounded multiplicity incidence 仍是并行守门项。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `ExactAtomicJointBranchTraceCurrentCorpusProved` | `false` | `false` | 当前材料没有提交每条 atomic joint row 的 exact branch trace signed coefficient formula。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `BuiltInSignedCoefficientPairingCurrentCorpusProved` | `false` | `false` | 没有 branch trace 公式，内置 signed coefficient/pairing 闭式仍未证明。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 缺少 atomic trace 闭式、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 作者侧剩余基

```text
ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
```
