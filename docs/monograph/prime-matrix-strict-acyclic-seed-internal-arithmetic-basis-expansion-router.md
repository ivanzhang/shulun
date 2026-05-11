# Prime Matrix strict acyclic seed internal arithmetic basis expansion 路由器

**状态：** `acyclic_seed_internal_arithmetic_basis_expansion_reduced_to_noncanonical_basis_alphabet_open`

本步没有转换命题，只把真正破坏输入继续下钻：内部算术基展开首先缺的是 actual noncanonical pre-Cauchy basis alphabet。没有这张字母表账本，signed coefficient assignment 没有定义域，后续截断/相位层、local factor、Phi 推前前恒等式都不能成为可检验命题。因此当前仍未形成无条件矛盾，下一步应直接攻 basis alphabet 账本。

```text
acyclic_seed_internal_arithmetic_basis_expansion_router_closed=true
noncanonical_precauchy_basis_alphabet_ledger_proved=false
basis_coefficient_assignment_ledger_proved=false
acyclic_seed_internal_arithmetic_basis_expansion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy 的第一不可替代字段是 `AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger`。因为字母表先于 coefficient assignment、截断相位规则和 pre-Cauchy 恒等式；现有 canonical、generic WFD、外部谱、零行/payment 反推、formal-unit/source-tuple 容器和 unsigned skeleton 都不能给出 actual noncanonical seed 的 basis word 集。

## 2. basis alphabet 账本字段

| field | meaning |
| --- | --- |
| `basis_word_set` | seed 内部允许出现的 pre-Cauchy 算术基字母和有限 word 集。 |
| `word_to_source_tuple_map` | 每个 basis word 到 actual noncanonical source tuple 的正向生成映射。 |
| `local_factor_domain` | 每个 word 的 local factor、符号和非零条件所在定义域。 |
| `truncation_phase_compatibility` | 字母表与 carry shell、phase wheel、截断层和 branch key 的兼容规则。 |
| `noncanonical_scope_lock` | 证明这些字母不是 canonical RIW/Buchstab 的跨作用域导入。 |
| `failure_return` | 缺字母、超预算、后验选择或作用域冲突时的命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `InternalArithmeticBasisExpansionTargetActive` | `true` | `false` | 上一层已把 basis weight source formula 压到 seed 内部 pre-Cauchy 算术基展开。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |
| `BasisAlphabetIsFirstDomainGate` | `true` | `true` | 没有 basis alphabet，coefficient assignment、截断层规则和 pre-Cauchy 恒等式都没有定义域。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `CanonicalAlphabetCrossImportBlocked` | `true` | `true` | canonical RIW/Buchstab 字母表只在 canonical branch 内有作用域，不能作为 actual noncanonical seed 的字母表。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `GenericWFDIsNotAlphabet` | `true` | `true` | generic WFD 是性质约束，不是逐 primitive row 的算术基字母表。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `ExternalSpectralDoesNotEmitAlphabet` | `true` | `true` | 外部谱估计接收已给定的系数族；它不生成 seed 内部 basis alphabet。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `ReversePaymentAndZeroRowRecoveryBlocked` | `true` | `true` | 不能从 payment 原像、推前后结构或早期零行 unsigned 覆盖反推出 pre-Cauchy 字母表。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `FormalUnitAndSourceTupleAreContainersOnly` | `true` | `false` | formal unit 与 source tuple 能登记参数、哈希和锚点；它们没有列出可赋权的 basis word 集。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `UnsignedSkeletonHasPhaseAlphabetNotArithmeticAlphabet` | `true` | `false` | unsigned skeleton 的相位/几何字母只能定位 row，不能给 signed arithmetic basis alphabet。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `CanonicalT1ClassifierDoesNotSupplyNoncanonicalAlphabet` | `true` | `false` | canonical T1 分支分类只区分 canonical absorbed 或 mismatch；不提交 noncanonical basis word 集。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `ExplicitAlphaDeltaRuleRequiresAlphabetUpstream` | `true` | `false` | 显式 alpha/delta rule 需要已有 primitive source word 与 local factor 定义，不能反过来定义字母表。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `CompleteEmitterKeyPartitionIsDownstream` | `true` | `false` | complete emitter key partition 是 source table 之后的登记纪律，不是 source basis alphabet 的来源。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `NoncanonicalPreCauchyBasisAlphabetCurrentCorpusProved` | `false` | `false` | 当前材料尚未提交 actual noncanonical seed 的 pre-Cauchy basis alphabet 账本。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `CoefficientAssignmentCurrentCorpusBlockedByMissingAlphabet` | `false` | `false` | 没有字母表定义域，coefficient assignment 只能作为并行依赖保留，不能先行闭合。 | AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger |
| `InternalArithmeticBasisExpansionCurrentCorpusProved` | `false` | `false` | basis alphabet、coefficient assignment、截断相位规则、作用域锁和推前前恒等式未合取证明。 | AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy |

## 4. 下一真正单点

```text
AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger
```

并行依赖：

```text
AcyclicSeedCoefficientAssignmentOnBasisAlphabetLedger
AcyclicSeedTruncationPhaseCompatibilityLedger
AcyclicSeedPreCauchyBasisExpansionIdentityLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
