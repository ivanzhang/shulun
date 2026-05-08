# Prime Matrix clean-core 构造器来源分类防火墙路由器

**状态：** `constructor_admission_reduced_to_actual_noncanonical_primitive_formula_open`

最新完全自足剩余继续压缩：构造器准入的来源分类防火墙已闭合，未登记来源不再作为 clean-core 终端保留。唯一自足源侧原子变成 actual noncanonical primitive source constructor 的显式公式。

```text
constructor_source_class_firewall_boundary_closed=true
source_class_partition_closed=true
unregistered_source_return_absorbed=true
actual_noncanonical_primitive_constructor_formula_proved=false
clean_core_primitive_source_constructor_admission_proved=false
external_spectral_atom_accepted=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PriorPrimitiveConstructorAdmissionPinned` | `true` | `false` | 上一层已把原始来源准入压到 primitive source constructor admission。 | 拆分构造器准入的来源类别。 |
| `ConstructorAdmissionSplitsBySourceClass` | `true` | `true` | 任一候选来源必须属于 canonical、generic_wfd、unregistered/mixed、external_spectral 或 actual_noncanonical。 | 逐类路由后只剩 actual noncanonical 公式。 |
| `CanonicalClassClosedScoped` | `true` | `true` | canonical RIW/Buchstab constructor 已闭合，但只在 canonical-source 分支有效。 | 不能导入 noncanonical clean-core。 |
| `GenericWFDClassRejected` | `true` | `true` | generic WFD 只是形式性质，不是 source constructor。 | generic 分支只能走外部谱输入或命名回流。 |
| `UnregisteredOrMixedFormalUnitReturnAbsorbed` | `true` | `true` | 没有同一 formal unit/source registration 的对象不是 clean-core 终端；口径不一致回到 Multiplicity/Stitching 或 K7 失败出口。 | 不再把 unregistered source 当作自足剩余。 |
| `ExternalSpectralClassPinned` | `true` | `false` | 外部谱类已压成 c-dependent completed residue spectral cancellation。 | 证明或接受 CDependentResidueWeightSpectralCancellationInput。 |
| `ActualNoncanonicalPrimitiveConstructorFormulaCurrentCorpusProved` | `false` | `false` | 当前材料尚未写出 actual noncanonical clean-core primitive constructor formula。 | 证明 ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 2. 来源分类防火墙律

primitive constructor admission splits by source class. Canonical constructor is closed only in its own branch; generic WFD is not a constructor; unregistered or mixed formal-unit sources return via Multiplicity/Stitching or K7 formal-unit failure; external spectral class remains external. Therefore the only self-contained source-side atom left is the actual noncanonical primitive constructor formula.

## 3. 来源类别

| source class | route | status | remaining |
| --- | --- | --- | --- |
| `canonical` | canonical RIW/Buchstab constructor | `closed_scoped` | 不能覆盖 noncanonical clean-core。 |
| `generic_wfd` | formal well-factorable template | `rejected_as_constructor` | 形式可分解性不给 summand emitter。 |
| `unregistered_or_mixed_formal_unit` | Multiplicity/Stitching or K7 formal-unit return | `absorbed_as_return` | 不能作为 clean-core 终端保留。 |
| `external_spectral` | c-dependent completed residue spectral input | `open_external` | 需证明或接受外部谱输入。 |
| `actual_noncanonical` | primitive constructor formula | `open_self_contained` | 写出 actual noncanonical constructor formula。 |

## 4. actual noncanonical 公式字段

| field | requirement |
| --- | --- |
| `pre_cauchy_definition` | 在 Cauchy/dispersion 前定义 actual noncanonical clean-core 系数。 |
| `summand_emitter` | 给出产生 alpha/delta summand 的确定性 emitter。 |
| `branch_key_schema` | 每个 summand 带有限 branch key、u/v map、sign、local factor。 |
| `formal_unit_compatibility` | emitter 输出与后续容量、支撑、回流账本使用同一个 formal unit。 |
| `return_tags` | 公式不适用、超预算、thin block 或抵消必须输出命名 return tag。 |

## 5. 最新输入基

条件输入基：

```text
(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

`ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn` 要求：

- 在 Cauchy/dispersion 前写出 actual noncanonical clean-core 系数定义；
- 给出确定性 summand emitter，输出 `alpha/delta`、branch key、`u/v` map、符号和 local factor；
- 证明 emitter 与后续支撑、容量和回流账本处于同一 formal unit；
- 证明 branch key 数为 `log^O(1)`，或把超预算部分命名回流；
- 公式不适用、thin block、抵消或未登记来源必须回流。

## 6. 当前结论

本步没有证明 actual noncanonical primitive constructor formula。它闭合的是来源分类防火墙：
canonical、generic、unregistered 和 external 类都已按边界处理，唯一自足剩余是 actual noncanonical 显式公式。
