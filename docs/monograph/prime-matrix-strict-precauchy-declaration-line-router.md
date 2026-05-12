# Prime Matrix strict pre-Cauchy declaration line 路由器

**状态：** `strict_precauchy_declaration_line_reduced_to_actual_constructor_formula_line_open`

`PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` 被逐类过滤到同一源表内部的 `ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter`。这不是换命题，而是证明源表第一行时必须写出的实际公式行。当前语料没有该公式行，因此源表、complete key、fixed-pair fiber bound 和最终源熵命题仍未闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
precauchy_declaration_line_router_closed=true
actual_noncanonical_declaration_only_strict_option=true
actual_noncanonical_primitive_constructor_formula_line_proved=false
pre_cauchy_constructor_declaration_line_proved=false
actual_noncanonical_primitive_emitter_source_table_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 分类律

A pre-Cauchy declaration line is legal for this strict source table only if it declares the actual noncanonical primitive constructor before Cauchy/dispersion. Canonical declarations are scoped to the canonical branch, generic WFD is not a constructor, unregistered/mixed declarations return, and external spectral estimates do not emit source rows.

## 2. 源表第一行拆分

拆分前：

```text
PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter
```

拆分后：

```text
ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter AND SameFormalUnitPreCauchyTimestampLockLedger AND NoncanonicalDeclarationNoCanonicalOrExternalLeakLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreCauchyDeclarationLineTargetActive` | `true` | `false` | 上一层源表字段拆分已把第一硬点压成 Cauchy/dispersion 前的 constructor declaration line。 | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter |
| `SourceClassPartitionClosed` | `true` | `true` | 任何 declaration line 必须属于 canonical、generic WFD、unregistered/mixed、external 或 actual noncanonical。 | 逐类过滤，保留 strict 自足合法分支。 |
| `CanonicalDeclarationScopedOut` | `true` | `true` | canonical RIW/Buchstab provenance 只在 pre-Cauchy 声明本来就是 canonical 时闭合，不能作为 noncanonical emitter 声明。 | 不能用 canonical 表填 actual noncanonical declaration line。 |
| `GenericWFDDeclarationRejected` | `true` | `true` | generic WFD 是形式分解约束，不是产生 primitive summand 的 constructor declaration。 | 不能以 WFD 模板作为源表第一行。 |
| `ExternalSpectralDeclarationRejectedForStrict` | `true` | `true` | DI/BFI/Kuznetsov 等外部引理从给定系数后处理，不能生成 strict 自足 pre-Cauchy declaration line。 | 外部谱只能作为条件分支，不填当前自足表。 |
| `UnregisteredMixedDeclarationReturned` | `true` | `true` | 未登记或混合 formal unit 的声明不能留在 clean-core 表内，必须命名回流。 | 保留表必须同 formal unit。 |
| `ActualNoncanonicalDeclarationIsOnlyStrictOption` | `true` | `true` | 四类伪声明过滤后，strict 自足 declaration line 只能是 actual noncanonical primitive constructor formula line。 | ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter。 |
| `SameFormalUnitTimestampRequirementPinned` | `true` | `true` | 声明行必须发生在 Cauchy/dispersion/Type/Fourier/completion 前，并锁定同一 actual formal unit。 | SameFormalUnitPreCauchyTimestampLockLedger。 |
| `ActualConstructorFormulaLineCurrentCorpusProved` | `false` | `false` | 当前材料尚未写出 actual noncanonical primitive constructor formula line。 | ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter。 |
| `PreCauchyDeclarationLineCurrentCorpusProved` | `false` | `false` | actual formula line、时间戳/formal-unit 锁和无泄漏纪律未合取证明。 | ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter AND SameFormalUnitPreCauchyTimestampLockLedger AND NoncanonicalDeclarationNoCanonicalOrExternalLeakLedger |

## 4. 下一主攻点

```text
ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter
```
