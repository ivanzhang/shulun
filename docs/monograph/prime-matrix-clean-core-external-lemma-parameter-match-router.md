# Prime Matrix clean-core 外部引理参数匹配路由器

**状态：** `external_lemmas_do_not_close_self_contained_constructor_formula`

与外部引理逐项对比后，最新完全自足剩余没有被外部定理消掉：DI/BFI/Kuznetsov 只能处理完成后的谱平均或 AP/well-factorable 分布，不能生成 pre-Cauchy actual noncanonical summand emitter。完全自足剩余仍是 ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn。

```text
external_lemma_parameter_match_boundary_closed=true
external_lemmas_match_constructor_formula=false
external_lemmas_close_self_contained_remainder=false
external_spectral_atom_accepted=false
actual_noncanonical_primitive_constructor_formula_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CurrentSelfContainedAtomPinned` | `true` | `false` | 上一层已把完全自足源侧剩余压成 actual noncanonical constructor formula。 | 核对外部引理是否可替代该公式。 |
| `ExternalPrimarySourcesIdentified` | `true` | `true` | 外部索引已定位 DI Kloosterman 与 BFI well-factorable AP 主来源。 | 这些来源的对象是否匹配当前原子。 |
| `KLSWindowAdaptationAvailable` | `true` | `true` | KLS-window 已有相位、模数、频率、权重和损失适配模板。 | 模板属于 completion 后谱平均，不是 source constructor。 |
| `ExternalLemmasDoNotEmitPreCauchySummands` | `true` | `true` | DI/BFI/Kuznetsov 输入都从已给定系数或完成型权重开始，不能生成 alpha/delta summand emitter。 | 自足 constructor formula 仍需内部证明。 |
| `PrimarySourceSpecializationNoGoRetained` | `true` | `true` | 现有 DI/BFI 主来源不能直接推出 full-S non-AP KLS-ext。 | 若走外部路线，仍需新 Full-S 定理或 APSourceLift。 |
| `CDependentResidueExternalTargetStillOpen` | `true` | `false` | 最接近的外部谱目标仍是 c-dependent residue weight cancellation。 | 证明或接受该外部谱输入。 |
| `ActualNoncanonicalConstructorFormulaStillOpen` | `false` | `false` | 外部引理匹配不能替代 actual noncanonical primitive source constructor formula。 | 证明 ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 2. 对比律

外部 DI/BFI/Kuznetsov 引理与当前自足原子处在不同层级：外部引理处理 completion 之后的 Kloosterman/AP/谱平均，要求系数或 residue 权重已经给定；当前自足原子要求在 Cauchy/dispersion 前写出 actual noncanonical alpha/delta 的 primitive constructor。因此外部引理不能替代该公式，只能作为 external_spectral 分支的候选。

## 3. 外部来源

| source | object | usable for | not usable for | url |
| --- | --- | --- | --- | --- |
| Deshouillers-Iwaniec 1982/83 | Kloosterman sums and Fourier coefficients of cusp forms | 谱 Kloosterman 大筛、Kuznetsov/trace formula 后的平均抵消。 | pre-Cauchy source constructor 或 actual summand emitter。 | https://eudml.org/doc/142975 |
| Bombieri-Friedlander-Iwaniec 1986 | Primes in arithmetic progressions to large moduli, Theorem 10 | well-factorable AP discrepancy / dispersion framework。 | non-AP clean-core primitive constructor formula。 | https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6385-11511_2006_Article_BF02399204.pdf |
| Maynard 2020 | well-factorable AP estimates to larger moduli | 更强 AP/well-factorable 分布背景。 | c-dependent completed residue weights 或 pre-Cauchy source emitter。 | https://arxiv.org/abs/2006.07088 |

## 4. 参数匹配表

| lemma family | structure match | parameter match | constructor match | reason | route |
| --- | --- | --- | --- | --- | --- |
| `DI_Kuznetsov_KLS` | post_completion_inverse_phase_average | partial | `false` | DI/Kuznetsov 处理的是已给定系数向量后的 Kloosterman 模数/频率平均；当前自足原子要求 Cauchy 前生成 alpha/delta summand。 | 只能进入 external_spectral 或 KLS-window 分支。 |
| `BFI1986_Theorem10` | well_factorable_AP_discrepancy | AP_source_only | `false` | BFI Theorem 10 的对象是 AP discrepancy 与 well-factorable 模权；当前对象是 non-AP clean-core primitive source constructor。 | 若能证明 APSourceLift 才可回接；当前 APSourceLift 未证。 |
| `Maynard_WellFactorable_AP` | stronger_AP_level_background | not_c_dependent_completed_weight | `false` | Maynard 扩展 AP/well-factorable 平均范围，但仍不是 actual noncanonical summand emitter，也不处理当前 B_{c,x} 依赖。 | 可作外部谱路线背景，不能替代自足公式。 |
| `KLS_Window_Template` | phase_modulus_frequency_match_after_CRT | matched_for_two_point_or_clean_KLS_template | `false` | 仓库 KLS-window 模板已把相位、模数、频率和 well-factorable 权重对齐到外部 KLS，但它从已给定系数开始，不生成 noncanonical clean-core 系数。 | KuznetsovLSAtomSC9OrExternalCitation |
| `Completed_CDependentResidueSpectral` | closest_external_target | open | `false` | After full-S completion, the remaining obstacle is not the length of the s-window. The residue weights B_{c,x} have an L2 budget, but they are c-dependent and not flat or centered. Pointwise Weil with Cauchy reaches only the natural/root scale and ordinary large sieve lacks the required c,h dispersion structure. Therefore the next honest atom is a spectral cancellation theorem for c-dependent completed residue weights. | CDependentResidueWeightSpectralCancellationInput |
| `Existing_DI_BFI_Primary_Source_Specialization` | rejected_for_full_S_non_AP | blocked_by_scale_or_object | `false` | The final primary-source check is not a missing citation. BFI Theorem 10, correctly located in the 1986 Acta Math paper, closes AP-source discrepancies with positive level slack, but the current remaining branch is non-AP WFD. The DI/Maynard Kloosterman J-scale cannot supply the custom full-S KLS-ext theorem when s=q=1/2, since n+2r+5s+q<=2 already fails before adding n and r. Therefore deriving FullS-KLS-ext from existing DI/BFI primary sources is rejected. | NewFullSTheoremInputOrAPSourceLift |

## 5. 最新输入基

条件输入基：

```text
(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 当前结论

外部引理参数匹配没有推进为完全自足闭合；它只确认外部谱路线的边界位置。
当前自足证明仍必须直接写出 actual noncanonical primitive constructor formula，
并且 DStructure/Rankin 独立验收门仍未完成。
