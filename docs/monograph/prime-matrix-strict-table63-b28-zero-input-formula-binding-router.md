# Prime Matrix strict Table 6.3 b=28 零点输入绑定审计证书

**状态：** `table63_b28_zero_input_binding_blocked_by_actual_table_formula_declaration`

`Table63B28ZeroInputToExplicitFormulaBinding` 的首缺口不是再登记 Gourdon/Kadiri，而是声明 b=28 表行实际采用的显式公式/表算法。仓库内部粗 Perron 链已经自洽闭合，但它被数值压力排除为 Table 6.3 生成器；外部零点来源虽然可用，仍未绑定到同一核、截断、端点和尾项阈值。因此下一最窄点是 `Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger`。

```text
internal_coarse_explicit_formula_chain_complete=true
internal_coarse_formula_rejected_as_table63_generator=true
external_zero_inputs_available_but_unbound=true
table63_b28_actual_formula_declaration_closed=false
table63_b28_zero_input_binding_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 绑定矩阵

| field | current internal status | binding gap | next gate |
| --- | --- | --- | --- |
| `target_function` | psi_0 exact formula closed | Table 6.3 的 epsilon_psi 行必须声明使用 psi、psi_0 或端点跳变转换。 | `Table63B28PsiVsPsi0EndpointConventionLedger` |
| `kernel_truncation_smoothing` | unsmoothed Perron C=12128 closed for internal coarse route | 内部非平滑核已闭合但过粗；Table 6.3 的实际核/截断/平滑规则未声明。 | `Table63B28KernelTruncationAndSmoothingConventionLedger` |
| `finite_zero_block` | Gourdon external source identified; repository self-contained data/hash open | 需要把零点数量或高度端点转换为表公式实际使用的 H 与零点块。 | `Table63B28FiniteRHHeightEndpointAndZeroBlockLedger` |
| `zero_free_tail` | Kadiri external source identified; table constants/start height open | 需要声明表尾项使用的零点自由常数、起点和适用范围。 | `Table63B28ZeroFreeTailConstantsAndStartHeightLedger` |
| `split_no_gap_no_overlap` | common-variable taxonomy closed only | 需要证明 finite block、zero-free tail 与截断余项覆盖连续且不重复扣费。 | `Table63B28FiniteToTailNoGapNoOverlapLedger` |
| `budget_and_rounding` | cap fixed; component numerical budget/hash open | 需要证明绑定后的各项和被外向舍入到 2.224E-5。 | `Table63B28PsiEpsilonBudgetPartitionLedger AND Table63B28DirectedUpperRoundingAndIntervalPropagationLedger AND Table63B28ReproducibleComputationHashLedger` |

## 2. 数值边界

| field | value |
| --- | ---: |
| `epsilon_psi_28` | `0.00002224` |
| `target_1_over_36260` | `0.000027578599007170435741864313292884721456150027578599` |
| `p51_high_tail_margin` | `0.000005338599007170435741864313292884721456150027578599` |
| `coarse_template_gap_factor_high_tail_b28` | `2779902555195.0005` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只审计假设反例链可调用的 Table 6.3 解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ZeroInputBindingGateActive` | `true` | `true` | 上一证书已把最窄点压到 b=28 的有限零点/零点自由尾项与显式公式绑定。 | Table63B28ZeroInputToExplicitFormulaBindingLedger |
| `InternalCoarseExplicitFormulaChainComplete` | `true` | `true` | 仓库内部 psi_0 身份、非平滑 Perron、零点和粗预算、平凡尾项/素数幂账本已经自洽闭合。 | internal coarse Perron route |
| `InternalCoarseFormulaRejectedAsTable63Generator` | `true` | `true` | 现有内部公式链虽自洽，但以 C=1280,C_Z=65536 口径生成 b=28 表值失败约 10^12 倍。 | gap_factor=2779902555195.0005 |
| `ExternalZeroInputsAvailableButUnbound` | `true` | `false` | Gourdon 有限零点与 Kadiri 零点自由区可作为外部来源，但尚未进入同一 b=28 表公式。 | Table63B28FiniteRHHeightEndpointAndZeroBlockLedger AND Table63B28ZeroFreeTailConstantsAndStartHeightLedger |
| `CommonVariableTaxonomyImported` | `true` | `true` | 六类共同变量已经分类：x 区间、高度端点、尾项阈值、公式核、预算、舍入/hash。 | taxonomy closed, numerical binding open |
| `Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger` | `false` | `false` | 缺少 Table 6.3 b=28 实际表公式/算法工件；没有它，零点输入无法判断应绑定到哪个核、截断和端点约定。 | Table63B28PsiVsPsi0EndpointConventionLedger AND Table63B28KernelTruncationAndSmoothingConventionLedger AND Table63B28FiniteRHHeightEndpointAndZeroBlockLedger AND Table63B28ZeroFreeTailConstantsAndStartHeightLedger |
| `Table63B28ZeroInputToExplicitFormulaBindingLedger` | `false` | `false` | 零点输入绑定不能在公式声明之前闭合；现有内部粗公式不能替代 Table 6.3 表算法。 | Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger AND Table63B28FiniteToTailNoGapNoOverlapLedger |
| `B28GenerationStillOpen` | `false` | `false` | 即使完成绑定，仍需预算分摊、外向舍入、区间传播和可复现 hash 生成 2.224E-5。 | Table63B28PsiEpsilonBudgetPartitionLedger AND Table63B28DirectedUpperRoundingAndIntervalPropagationLedger AND Table63B28ReproducibleComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | Table 6.3 零点输入绑定审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger
```

