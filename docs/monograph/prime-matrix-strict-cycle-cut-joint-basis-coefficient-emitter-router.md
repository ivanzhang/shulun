# Prime Matrix strict cycle-cut 联合 basis/coefficient 发射器路由器

**状态：** `cycle_cut_source_input_reduced_to_joint_basis_word_coefficient_emitter_open`

本步把 cycle-cut 输入进一步压窄：现有 word-first 路线只给 unsigned 坐标域，最终卡在 signed slot；coefficient-first 路线又要求 value map 来源恒等式，并回到逐行原始生成表。因此顺序拆分仍是来源环。要真正破环，必须提交一个同 formal unit、Cauchy/payment 前的联合发射器，同时输出 primitive basis word、signed coefficient、sign/local factor、prepushforward sum identity 和失败回流。该联合发射器当前未证明，行/列命题仍未无条件闭合。

```text
cycle_cut_input_router_closed=true
sequential_word_then_coefficient_split_rejected=true
joint_basis_word_coefficient_emitter_proved=false
acyclic_seed_cycle_cut_source_input_proved=false
acyclic_terminal_return_well_founded_descent_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput` 不能继续拆成“先生成 basis word、再赋 signed coefficient”的顺序链；这两条链已互相回指并回到 row-level origin 表。真正非循环破环输入必须是一条 Cauchy 前联合发射公式，即 `AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy`。

## 2. 联合发射器字段

| field | meaning |
| --- | --- |
| `source_tuple_input` | 只读取同一 formal unit 的 actual noncanonical source tuple 与已闭合锚参数。 |
| `basis_word_output` | 在 Cauchy/payment 前输出 primitive basis word，而不是后验选择 word。 |
| `signed_coefficient_output` | 同一公式同时输出 signed coefficient、sign、local factor 和非零条件。 |
| `word_coefficient_identity` | 证明输出的 word 与 coefficient 是同一个 pre-Cauchy 算术对象的两面。 |
| `prepushforward_sum_identity` | 证明联合发射后的 rows 在 Phi/payment 推前前已经给出目标 alpha/delta 贡献。 |
| `no_downstream_read` | 公式不读取 payment、零行覆盖、origin table、terminal certificate 或外部谱后处理。 |
| `named_return_tags` | 缺 word、零 local factor、符号冲突、多值或超预算时命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CycleCutInputActive` | `true` | `false` | 上一层前沿同步已把非循环新增输入钉为 primitive basis 与 signed coefficient 的前置源输入。 | AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput |
| `ExistingCycleGuardImported` | `true` | `true` | 已登记的 signed 坐标-来源链形成闭合依赖环，不能用环本身证明 signed coefficient。 | AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput |
| `WordFirstRouteStillOpen` | `true` | `false` | 先生成 basis word 的路线最终仍卡在 word coordinate / signed slot，而不是给出完整源输入。 | AcyclicSeedSourceTupleToPrimitiveBasisWordConstructorBeforeAdmissibility |
| `AnchorCoordinatesDoNotCloseSignedSlot` | `true` | `true` | anchor/dyadic/phase 坐标域已闭合，但 signed weight coordinate slot 仍未证明。 | AcyclicSeedSignedWeightCoordinateSlotLedger |
| `CoefficientFirstRouteStillOpen` | `true` | `false` | 先给 coefficient assignment 的路线又要求 basis word value map 与来源恒等式，回到原始行表。 | AcyclicSeedBasisWordToSignedCoefficientValueMapFormula |
| `ValueMapReturnsToOriginLedger` | `true` | `true` | signed coefficient value map 必须是来源恒等式；来源恒等式又要求逐行原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowTableRequiresEmitterImported` | `true` | `true` | 逐行原始表本身要求 seed signed row emitter；这正是被环守卫禁止自证的对象。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity |
| `SequentialSplitRejected` | `true` | `true` | word-first 与 coefficient-first 都回到对方或原始表；cycle-cut 输入必须是联合发射公式。 | AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy |
| `JointEmitterCurrentCorpusProved` | `false` | `false` | 当前材料没有提交同时输出 basis word 与 signed coefficient 的 Cauchy 前联合发射公式。 | AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy |
| `TerminalDescentAlternativeStillOpen` | `false` | `false` | 若不能提交联合发射器，只能走终端回流严格下降证书；该证书也未证明。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |

## 4. 下一最窄点

首攻：

```text
AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy
```

并行守门：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
```

外部 Mertens/theta 高段已接受时的当前活动基：

```text
(AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只证明顺序拆分会回到来源环，并把破环输入压成联合发射公式；它没有证明该联合公式，也没有证明行/列命题无条件闭合。
