# Prime Matrix clean-core pre-Cauchy 来源律原子化路由器

**状态：** `clean_core_precauchy_source_law_reduced_to_origin_generation_ledger_open`

最新真正剩余继续压缩：pre-Cauchy 来源律不是一个新的统计估计，而是 actual clean-core alpha/delta 的原始生成账本问题。canonical 账本只闭合 canonical-source 分支，generic WFD 不给原始来源；当前材料尚未提交 noncanonical clean-core 的完整生成表。

```text
clean_core_precauchy_source_law_atom_boundary_closed=true
origin_generation_ledger_implication_closed=true
clean_core_original_coefficient_generation_ledger_proved=false
clean_core_precauchy_source_law_proved=false
external_spectral_atom_accepted=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PriorPreCauchySourceLawPinned` | `true` | `false` | 上一层已把路径来源防火墙压到 clean-core pre-Cauchy 来源律。 | 判断该来源律还能否继续拆成更小的必要账本。 |
| `SourceLawIsOriginLedgerBundle` | `true` | `false` | pre-Cauchy 来源律的四项内容等价于原始生成账本：公式、路径、非零和回流。 | 提交 actual clean-core alpha/delta 的原始生成账本。 |
| `OriginLedgerImpliesPreCauchySourceLaw` | `true` | `true` | 若同一 formal unit 的原始生成表存在，branch key 给出路径签名，非零/回流由表项纪律推出。 | 该推出只处理逻辑结构，不证明生成表存在。 |
| `CanonicalLedgerClosedButScoped` | `true` | `true` | canonical RIW/Buchstab 原始来源账本已闭合，但只服务 canonical-source 分支。 | 不能把 canonical 账本导入 noncanonical clean-core。 |
| `GenericWFDOriginLedgerRejected` | `true` | `true` | well-factorable/generic WFD 只给形式分解，不给 actual 原始生成表。 | clean-core 必须给出自己的 actual source ledger 或走外部。 |
| `NoncanonicalComplementNeedsOwnActualSource` | `true` | `true` | canonical 分支扣除后，noncanonical 补集只剩实际源定理、强化反原子或外部谱路线。 | 当前 clean-core 来源律必须落到自己的原始生成账本。 |
| `CleanCoreOriginalCoefficientGenerationLedgerCurrentCorpusProved` | `false` | `false` | 当前材料尚未列出 actual clean-core alpha/delta 的完整 pre-Cauchy 原始生成表。 | 证明 CleanCoreOriginalCoefficientGenerationLedgerAndReturn。 |
| `ExternalSpectralAtomStillOpen` | `true` | `false` | 外部 completed KLS 路线仍压在 c-dependent residue weight 谱抵消输入上。 | 证明或接受 CDependentResidueWeightSpectralCancellationInput。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 2. 压缩定理

CleanCorePreCauchyCoefficientSourceLawAndReturn 的真正原子是 CleanCoreOriginalCoefficientGenerationLedgerAndReturn：若在 Cauchy/dispersion 前列出 actual clean-core alpha/delta 的同一 formal unit 原始生成表，则路径签名、polylog 路径预算、同路径非零/无抵消和失败回流都由账本纪律推出；反过来，任何来源律证明都必须至少给出这张表。

## 3. 原始生成账本条款

| clause | ledger requirement | source-law output |
| --- | --- | --- |
| `SameFormalUnitBeforeCauchy` | 所有 actual alpha/delta summand 在 Cauchy、Type/Fourier、completion 前登记到同一 formal unit。 | 来源公式不是后验替换，而是原始系数恒等式。 |
| `PrimitivePathKey` | 每个 summand 记录 source class、branch key、u/v map、dyadic/truncation state、sign 和 local factor。 | branch key 直接给出 exact path signature。 |
| `PolylogPathBudget` | branch alphabet 和 truncation depth 均为 K6/tail-label 已登记的 log^O 成本。 | 路径数预算可用于 selector pigeonhole。 |
| `PrimitiveNonzeroOrSignSplit` | 同一完整 branch key 的 local factors 非零；若同一 key 有相反号，必须先按 sign/refinement 细分。 | 同路径非零、无抵消，或抵消被命名回流。 |
| `NamedReturnDiscipline` | 缺失来源、路径超预算、thin/rejected block、未消除抵消均带 return tag。 | 失败回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。 |

## 4. 最新输入基

条件输入基：

```text
(CleanCoreOriginalCoefficientGenerationLedgerAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

`CleanCoreOriginalCoefficientGenerationLedgerAndReturn` 要求：

- 在 Cauchy、dispersion、Type/Fourier、completion 之前固定同一 actual formal unit；
- 列出 clean-core `alpha/delta` 的所有原始 summand、branch key、u/v map、符号和 local factor；
- 证明 branch key 数为 `log^O(1)`，或把路径超预算回流到 K6/PDEC/SAE；
- 同一完整 key 非零且无抵消；若有抵消，必须进一步细分或输出命名回流；
- 缺失来源、thin/rejected block 或外部谱需求必须带 return tag。

## 5. 当前结论

本步没有证明 clean-core 原始生成账本。它闭合的是逻辑压缩：pre-Cauchy 来源律若要成立，
最小自足证据就是这张 actual 生成表；canonical 表不能跨分支导入，generic WFD 也不能替代它。
