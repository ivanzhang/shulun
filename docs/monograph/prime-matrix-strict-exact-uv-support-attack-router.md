# Prime Matrix 严格自足 ExactUV 支撑主攻路由器

**状态：** `strict_exact_uv_support_reduced_to_new_actual_source_support_theorem_open`

直接硬攻 ExactUV 后，现有内部路线已经把伪出口全部压掉：支撑关联需要 exact 层转移，exact 层转移需要 actual 路径分割，路径分割需要 pre-Cauchy signed 来源恒等式；而该来源恒等式不能由早期零行覆盖图、几何 Phi、canonical 模板或 generic WFD 反推出。因此严格自足数学主攻点被进一步定名为 NewActualNoncanonicalExactUVSupportTheoremInput。当前没有无条件闭合。

```text
strict_exact_uv_attack_boundary_closed=true
support_incidence_reduction_closed=true
path_partition_source_reduction_closed=true
zero_row_seed_extraction_blocked=true
actual_exact_uv_support_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=NewActualNoncanonicalExactUVSupportTheoremInput
```

## 1. 压缩链

```text
ActualNoncanonicalExactUVSupportLowerBound
  -> CleanCoreTerminalSupportIncidenceTheorem
  -> CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn
  -> CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn
  -> CleanCorePreCauchyCoefficientSourceLawAndReturn
  -> IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn
  -> NewActualNoncanonicalExactUVSupportTheoremInput
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictExactUVGateActive` | `true` | `false` | 上一层严格自足过滤后，数学主攻点只剩 ActualNoncanonicalExactUVSupportLowerBound。 | 直接攻击该支撑下界。 |
| `SupportIncidenceReductionImported` | `true` | `true` | ExactUV 支撑下界可由 CleanCoreTerminalSupportIncidenceTheorem 支付。 | 证明 clean-core terminal support incidence。 |
| `ExactLayerTransferReductionImported` | `true` | `true` | 支撑关联已压到 clean-core exact 层承认、非零转移和 thin return。 | CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn。 |
| `PathPartitionReductionImported` | `true` | `true` | 层承认可由 actual clean-core 系数的 polylog 路径分割、同路径非零/无抵消推出。 | CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn。 |
| `PreCauchySourceLawRequired` | `true` | `true` | 路径分割必须建立在 Cauchy/dispersion 前的 actual signed alpha/delta 来源恒等式上。 | CleanCorePreCauchyCoefficientSourceLawAndReturn。 |
| `SourceLoopCutAndZeroRowSeedNoGo` | `true` | `true` | 不能从 downstream payment skeleton、有限投影、早期零行覆盖图或几何 Phi 反向生成 pre-Cauchy 源。 | IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn。 |
| `IndependentIdentityTaxonomyClosed` | `true` | `true` | canonical、generic WFD、AP/external 来源都不能作为严格自足 noncanonical clean-core 来源恒等式。 | actual noncanonical moving-block spread / source theorem。 |
| `MovingBlockReturnLoopDetected` | `true` | `true` | actual moving-block 若有低维签名则回流 PDEC/SAE/ColumnCRT；若无签名则回到早期零行终端包。 | 这不是 ExactUV 的新证明，而是回到终端门/外部谱分支。 |
| `NoExistingInternalProofOfExactUV` | `true` | `false` | 现有内部链已经压完伪出口，但没有产生 actual exact u/v 支撑下界。 | NewActualNoncanonicalExactUVSupportTheoremInput。 |
| `StrictExactUVSupportClosureCurrentCorpusProved` | `true` | `false` | 当前语料库不能证明严格自足 ExactUV 支撑输入。 | 新增并证明 actual noncanonical exact-support 定理，或改变目标为条件外部线。 |

## 3. 新主攻合同

下一数学主攻点：`NewActualNoncanonicalExactUVSupportTheoremInput`。

必须证明：
- 在 Cauchy/dispersion 前给出 actual noncanonical clean-core signed source identity。
- 从该 identity 得到 polylog exact path partition。
- 证明同路径非零/无抵消或给出 sign-refined partition。
- 证明 thin/rejected/path-overbudget block 全部命名回流。
- 推出 S_u*S_v >= L^(2A+4C+E) 的 exact u/v 支撑下界。

不能作为证明使用：
- canonical RIW/Buchstab 来源表跨分支导入。
- formal WFD/Type/Fourier/K4/K6 平坦性。
- 真实样本未见早期零行。
- 从 payment skeleton 或 CRT 覆盖图反推 signed source。
- 外部 FullS-KLS 黑箱。

严格自足数学基更新为：

```text
NewActualNoncanonicalExactUVSupportTheoremInput AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
