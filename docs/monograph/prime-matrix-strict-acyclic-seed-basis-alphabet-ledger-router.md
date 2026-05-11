# Prime Matrix strict acyclic seed basis alphabet ledger 路由器

**状态：** `acyclic_seed_basis_alphabet_reduced_to_generated_primitive_basis_word_set_open`

本步继续保持同一个反例链目标，把 basis alphabet 账本压到 primitive basis word set generation rule。也就是说，下一步必须给出从 actual noncanonical seed/source tuple 到 basis word 的正向构造、准入谓词、row anchor、复杂度收费和缺字母回流；否则 signed coefficient assignment 仍无定义域。

```text
acyclic_seed_basis_alphabet_ledger_router_closed=true
primitive_basis_word_set_generation_rule_proved=false
noncanonical_precauchy_basis_alphabet_ledger_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

`AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger` 继续压缩为 `AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment`：basis alphabet 账本的首要内容不是命名一个 alphabet，而是正向生成实际可用的 primitive basis word 集。容器、unsigned phase alphabet、下游 key partition 或 payment/零行反推都不能替代这个生成规则。

## 2. word 生成规则字段

| field | meaning |
| --- | --- |
| `word_constructor` | 从 actual noncanonical seed/source tuple 正向生成 basis word 的规则。 |
| `admissible_word_predicate` | 判断 word 是否属于 pre-Cauchy basis alphabet 的算术条件。 |
| `word_to_row_anchor` | word 到 carry-shell row、phase 和 primitive summand 的锚定。 |
| `scope_and_noncanonical_lock` | 排除 canonical scoped import、post-payment 选择和零行反推。 |
| `finite_complexity_bound` | 字母表复杂度、分支数和截断层数量的可收费上界。 |
| `missing_word_return` | 缺字母、未登记 word 或超预算 word 的命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BasisAlphabetTargetActive` | `true` | `false` | 上一层已证明内部算术基展开首先缺 noncanonical pre-Cauchy basis alphabet。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |
| `AlphabetLedgerRequiresGeneratedWordSet` | `true` | `true` | 字母表不是标签名集合；必须给出 actual seed 在 Cauchy 前正向生成的 basis word 集。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `ContainersDoNotGenerateWords` | `true` | `false` | formal unit/source tuple 只是容器；没有 word_constructor 和 admissible_word_predicate。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `SourceGenerationStillOpen` | `true` | `false` | actual noncanonical primitive source constructor 与原始系数生成账本仍未证明，不能导出 basis word 集。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `UnsignedPhaseAlphabetNotBasisWordSet` | `true` | `false` | unsigned phase wheel/carry-shell 字母是几何相位，不是带 signed local factor 的算术 basis word。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `ExplicitRuleAndKeyAreDownstream` | `true` | `false` | alpha/delta rule 和 complete key partition 都要求已存在 primitive basis words，不能倒置为字母表来源。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `ReverseRecoveryBlocked` | `true` | `true` | payment、推前后投影和早期零行覆盖不能反向选择 basis words，否则会形成后验循环。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `PrimitiveBasisWordSetGenerationRuleCurrentCorpusProved` | `false` | `false` | 当前材料没有给出 word_constructor、admissible predicate、row anchor、复杂度上界和缺字母回流。 | AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment |
| `BasisAlphabetLedgerCurrentCorpusProved` | `false` | `false` | 没有正向生成的 basis word 集，basis alphabet 账本仍未证明。 | AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger |

## 4. 下一真正单点

```text
AcyclicSeedPrimitiveBasisWordSetGenerationRuleBeforeCoefficientAssignment
```

并行依赖：

```text
AcyclicSeedBasisWordAdmissibilityPredicateLedger
AcyclicSeedBasisWordFiniteComplexityBoundLedger
AcyclicSeedMissingBasisWordNamedReturnLedger
```

缺失或失败时的命名回流：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```
