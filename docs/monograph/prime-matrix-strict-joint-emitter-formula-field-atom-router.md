# Prime Matrix strict 联合 word/coefficient 发射公式字段原子路由器

**状态：** `joint_emitter_formula_reduced_to_precauchy_joint_declaration_line_open`

本步把联合发射公式拆到字段级：source tuple 输入已经闭合，后验读取已被 source-loop/no-go 防火墙排除；但能同时生成 primitive basis word 与 signed coefficient 的生产性公式仍不存在。因此当前首缺口不是再找一个后验表，而是在 Cauchy/payment/Phi 推前之前提交同一 actual noncanonical source tuple 的联合 declaration line。没有这条第一行，rows formula、word/coefficient identity、prepushforward identity 与 return ledger 都不能闭合。

```text
joint_emitter_formula_field_atom_router_closed=true
source_tuple_input_closed=true
pre_cauchy_joint_declaration_line_proved=false
joint_basis_word_coefficient_emitter_proved=false
acyclic_terminal_return_well_founded_descent_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy` 内部不能再靠 word-first 或 coefficient-first 顺序拆分闭合。已有 source tuple 只是输入容器；真正第一生产性原子是 Cauchy/payment 前的联合 declaration line，即 `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple`。

## 2. 生产性字段

| field | status | meaning |
| --- | --- | --- |
| `precauchy_joint_declaration_line` | `first_open_atom` | 在 Cauchy、dispersion、payment、Phi 推前之前声明同一 source tuple 的 actual noncanonical 联合发射器。 |
| `joint_rows_formula` | `blocked_until_declaration` | 由 declaration line 正向列出 primitive basis word、branch key、u/v、sign、local factor 与 signed coefficient。 |
| `word_coefficient_identity` | `blocked_until_rows_formula` | 证明 word 与 coefficient 是同一 pre-Cauchy 算术对象的两面，而非两个后验拼接标签。 |
| `prepushforward_sum_identity` | `blocked_until_rows_formula` | 证明联合发射行在 Phi/payment 推前前已经给出目标 alpha/delta 贡献。 |
| `no_downstream_recovery_and_named_return` | `schema_pinned_exact_ledger_open` | 禁止从 payment/零行/终端证书反推；失败、零因子、多值、超预算、thin/rejected/cancelling 必须命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `JointEmitterFormulaTargetActive` | `true` | `false` | 上一层已把 cycle-cut 破环输入压成同一 formal unit 的联合 basis word/coefficient 发射公式。 | AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy |
| `SourceTupleInputAlreadyClosed` | `true` | `true` | formal unit 与 source tuple 的字段、锚参数和哈希纪律已经存在，输入容器不是当前硬点。 | 生产性联合发射公式仍未给出。 |
| `WordFirstRouteStillCannotEmitJointFormula` | `true` | `false` | 单独从 source tuple 先构造 basis word 仍卡在 word coordinate 和 signed slot，不能给出联合发射。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `CoefficientFirstRouteStillReturnsToOriginTable` | `true` | `false` | 单独从 signed slot/assignment 出发仍回到 value map、origin identity 和 row-level 原始表。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `ActualEmitterSourceTableFirstLineMatchesJointDeclaration` | `true` | `false` | actual emitter 源表已有字段律：没有 pre-Cauchy declaration line，rows、identity 和 return ledger 都不能合法开始。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `DownstreamRecoveryFirewallImported` | `true` | `true` | payment、Phi 投影、零行覆盖和来源环均不能反推 signed pre-Cauchy 联合发射器。 | JointEmitterNoDownstreamRecoveryAndNamedReturnLedger |
| `FakeIndependentSourceTaxonomyImported` | `true` | `true` | 独立恒等式分类和 source-class 防火墙已排除 canonical/generic/external/unregistered 伪来源混入 strict 自足线。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `NoDownstreamReturnLedgerExactFormStillOpen` | `true` | `false` | 禁止后验读取的原则已闭合，但 exact return ledger 仍需逐类记录零因子、多值、超预算、thin/rejected/cancelling。 | JointEmitterNoDownstreamRecoveryAndNamedReturnLedger |
| `JointEmitterProductiveFieldsPinned` | `true` | `true` | 联合公式的生产性字段被压成 declaration line、rows formula、word/coefficient identity、prepushforward identity 和 return ledger。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger |
| `PreCauchyJointDeclarationLineCurrentCorpusProved` | `false` | `false` | 当前材料尚未在 Cauchy/payment 前声明 actual noncanonical source tuple 的联合 word/coefficient emitter。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `JointEmitterFormulaCurrentCorpusProved` | `false` | `false` | 缺 declaration line 时，后续 rows、identity 和 return ledger 不能合取闭合。 | AcyclicSeedJointPrimitiveBasisWordCoefficientEmitterFormulaBeforeCauchy |

## 4. 下一真正单点

首攻：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

完整生产性字段基：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger
```

保留终端下降并行门后的当前严格自足基：

```text
((PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger) OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只关闭字段定位和第一原子定位；它没有证明联合 declaration line，也没有证明行/列命题无条件闭合。
