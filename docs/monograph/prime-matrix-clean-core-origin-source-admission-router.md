# Prime Matrix clean-core 原始来源准入路由器

**状态：** `clean_core_origin_ledger_reduced_to_primitive_source_constructor_admission_open`

最新完全自足剩余继续压缩为 clean-core primitive source constructor 准入：先找到并登记实际来源构造器，才能生成 alpha/delta 原始账本。canonical 构造器已闭合但作用域有限，generic WFD 不是构造器；当前材料尚未证明 noncanonical clean-core 的构造器准入或未登记来源吸收。

```text
clean_core_origin_source_admission_boundary_closed=true
constructor_admission_implies_origin_ledger=true
unregistered_source_return_absorbed=false
clean_core_primitive_source_constructor_admission_proved=false
clean_core_original_coefficient_generation_ledger_proved=false
external_spectral_atom_accepted=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PriorOriginGenerationLedgerPinned` | `true` | `false` | 上一层已把 pre-Cauchy 来源律压到 actual 原始生成账本。 | 继续判断生成账本最小入口是什么。 |
| `OriginLedgerNeedsSourceConstructorAdmission` | `true` | `true` | 一张 summand 表必须先有 pre-Cauchy 原始构造器；否则无法审查其来源。 | 证明 clean-core 候选都有合法构造器，或未登记来源回流。 |
| `ConstructorAdmissionImpliesOriginLedger` | `true` | `true` | 若构造器准入并给出 emitted summand schema，原始生成账本由有限展开得到。 | 该推出不证明 clean-core 构造器存在。 |
| `CanonicalConstructorAlreadyScoped` | `true` | `true` | canonical RIW/Buchstab 构造器已闭合，但只在 canonical-source 分支内有效。 | noncanonical clean-core 不能使用该构造器偷渡。 |
| `GenericWFDNotAConstructor` | `true` | `true` | well-factorable 性质是形式约束，不是生成 summand 的原始构造器。 | 必须提交 actual noncanonical 构造器或外部谱输入。 |
| `ReturnAlphabetCanAbsorbUnregisteredSource` | `true` | `false` | 非 clean-core packet 的回流字母表已闭合，但未登记来源是否总能落入这些出口仍需准入账本标注。 | 把 unregistered source 具体标到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。 |
| `CleanCorePrimitiveSourceConstructorAdmissionCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明 noncanonical clean-core 候选都有 pre-Cauchy primitive source constructor。 | 证明 CleanCorePrimitiveSourceConstructorAdmissionAndReturn。 |
| `ExternalSpectralAtomStillOpen` | `true` | `false` | 外部路线仍是 c-dependent residue weight 谱抵消输入。 | 证明或接受 CDependentResidueWeightSpectralCancellationInput。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 2. 压缩律

原始生成账本的入口不是估计，而是来源准入：必须先证明 actual clean-core alpha/delta 由某个 pre-Cauchy primitive source constructor 生成。构造器准入后，emitted summand schema 可展开为原始生成账本；构造器缺失则必须作为未登记来源回流，不能继续当作 clean-core 终端。

## 3. 构造器准入字段

| field | requirement | why |
| --- | --- | --- |
| `source_constructor` | 在 Cauchy/dispersion 前声明系数由哪个原始构造器生成。 | 没有构造器就没有可审查的 summand 表。 |
| `formal_unit_id` | 构造器输出必须落在同一个 actual formal unit。 | 避免把不同口径的系数拼成一张伪账本。 |
| `branch_admission` | 标明 canonical、noncanonical actual、external spectral 或 named return。 | canonical 账本不能跨分支导入，generic WFD 不能冒充来源。 |
| `emitted_summand_schema` | 给出 summand、branch key、u/v map、符号和 local factor 的生成规则。 | 该 schema 才能展开成原始生成账本。 |
| `failure_return_tag` | 构造器缺失、口径冲突、超预算或 thin block 必须带回流标签。 | 未登记来源不能成为新的隐藏终端。 |

## 4. 最新输入基

条件输入基：

```text
(CleanCorePrimitiveSourceConstructorAdmissionAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
CleanCorePrimitiveSourceConstructorAdmissionAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

`CleanCorePrimitiveSourceConstructorAdmissionAndReturn` 要求：

- 在 Cauchy/dispersion 前给出 actual clean-core `alpha/delta` 的 primitive source constructor；
- 证明该构造器输出落在同一个 actual formal unit；
- 给出 emitted summand schema，使其可展开为原始生成账本；
- 证明该构造器不是 canonical 跨分支导入，也不是 generic WFD 形式冒充；
- 构造器缺失、口径冲突或未登记来源必须回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。

## 5. 当前结论

本步没有证明 primitive source constructor 准入，也没有吸收未登记来源。它只把原始生成账本的
最小入口压成来源构造器准入：没有构造器，就没有合法 clean-core 原始账本。
