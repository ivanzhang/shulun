# Prime Matrix clean-core 路径来源防火墙路由器

**状态：** `clean_core_path_partition_reduced_to_precauchy_source_law_open`

最新真正剩余继续压缩为 clean-core pre-Cauchy 系数来源律：先写出 actual alpha/delta 的来源公式，才能审查路径分割、无抵消和薄块回流。当前材料尚未证明该来源律。

```text
clean_core_path_source_firewall_boundary_closed=true
clean_core_precauchy_source_law_proved=false
clean_core_path_partition_proved=false
external_spectral_atom_accepted=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PriorPathPartitionPinned` | `true` | `false` | 上一层已把 clean-core 层转移压成 actual 系数路径分割账本。 | 判断该路径账本需要什么最小来源输入。 |
| `PathPartitionNeedsPreCauchySourceLaw` | `true` | `false` | 路径签名、无抵消和路径数预算必须作用在 Cauchy/dispersion 前的 actual 系数公式上。 | 写出 clean-core pre-Cauchy actual coefficient source law。 |
| `CanonicalDecisionTreeAvailableOnlyAsTemplate` | `true` | `true` | canonical RIW/Buchstab 决策树和来源账本已闭合，但作用域只限 canonical-source 分支。 | 不能把该模板导入 noncanonical clean-core。 |
| `WellFactorableTemplateRejected` | `true` | `true` | 仅有 well-factorable/generic WFD 形式不提供路径分割或 source entropy。 | clean-core 必须有 actual 来源公式，而非形式可分解性。 |
| `NoncanonicalComplementFirewallClosed` | `true` | `true` | canonical 分支已扣除，generic WFD 自足模板被 moving-delta 阻断。 | noncanonical clean-core 只能走 actual-source 定理或外部谱输入。 |
| `CleanCorePreCauchySourceLawCurrentCorpusProved` | `false` | `false` | 当前材料没有 clean-core actual alpha/delta 的 pre-Cauchy 来源公式、路径分割和失败回流账本。 | 证明 CleanCorePreCauchyCoefficientSourceLawAndReturn。 |
| `ExternalSpectralAtomPinned` | `true` | `false` | 外部 completed KLS 路线已进一步压成 c-dependent residue weight 谱抵消。 | 证明或引用 CDependentResidueWeightSpectralCancellationInput。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 2. 来源律

路径分割账本必须在 Cauchy/dispersion 前的 actual clean-core alpha/delta 系数上建立：给出 exact 来源公式、polylog 路径签名、同路径非零/无抵消、路径超预算或薄块的命名回流。

## 3. 防火墙律

canonical 决策树可作为模板但不能跨分支导入；generic WFD 形式被 moving-delta 阻断。因此 clean-core noncanonical 残余的自足闭合只能来自自己的 pre-Cauchy coefficient source law，否则走 c-dependent completed residue spectral input 或命名回流。

## 4. 最新输入基

条件输入基：

```text
(CleanCorePreCauchyCoefficientSourceLawAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
CleanCorePreCauchyCoefficientSourceLawAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

`CleanCorePreCauchyCoefficientSourceLawAndReturn` 要求：

- 在 Cauchy、Type/Fourier、completion 之前写出 actual clean-core `alpha/delta` 来源公式；
- 从该公式得到 polylog exact path signatures；
- 证明同路径非零且无抵消，或继续细分直到互斥；
- source-law 失败、路径超预算、thin/rejected block 必须回流到 PDEC/SAE/ColumnCRT/CleanKLS，或进入外部谱输入。

## 5. 当前结论

本步没有证明 clean-core 来源律。它关闭的是两个偷渡方向：canonical 决策树不能导入 noncanonical
clean-core，generic WFD 形式不能替代 actual coefficient source law。
