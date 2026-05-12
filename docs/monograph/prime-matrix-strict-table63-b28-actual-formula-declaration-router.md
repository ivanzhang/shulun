# Prime Matrix strict Table 6.3 b=28 实际表公式/算法工件审计证书

**状态：** `table63_b28_published_row_and_use_site_confirmed_algorithm_artifact_missing`

arXiv 源文件足以确认 Table 6.3 的 b=28 表行和 Proposition 5.1 的使用点，因此外部表行路线可接受；但它没有给出作者侧可复现的表生成算法。实际闭合只剩二选一：取得 `dusart:eps`/等价外部算法工件，或独立重建 Table 6.3 b=28 的显式公式、零点输入、预算、外向舍入和 hash。下一最窄点为独立重建输入基。

```text
table63_b28_published_row_statement_closed=true
table63_b28_p51_use_site_closed=true
table63_b28_actual_formula_declaration_closed=false
table63_b28_external_algorithm_artifact_present=false
table63_b28_independent_regeneration_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 源文件事实

| fact | source | meaning | status |
| --- | --- | --- | --- |
| `intro_dependency` | arXiv:1002.0442 source, introduction | 文章说明 psi/theta 有效估计依赖有限 RH 验证与显式零点自由区。 | source boundary confirmed |
| `gourdon_kadiri_boundary` | arXiv:1002.0442 source, bibliography/introduction | Gourdon 10^13 零点与 Kadiri 零点自由区是外部来源边界。 | external inputs identified |
| `table_eps_b28` | arXiv:1002.0442 source, table labeled Values of epsilon(x) for psi and theta | 表行给出 b=28, epsilon_psi=2.224E-5, epsilon_theta=2.308E-5。 | published row statement confirmed |
| `prop_eta0_use` | arXiv:1002.0442 source, Proposition theta(x)-x < x/36260 proof | 证明使用中段 1.00002841 与 eps_28<=0.00002224 完成高尾拼接。 | use site confirmed |
| `missing_generator` | arXiv:1002.0442 source, bibliography item dusart:eps | 更底层的 psi/theta 大值估计被指向一个 submitted 源，当前 arXiv 源未给出可复现表生成算法。 | algorithm artifact absent from this source |

## 2. 工件需求

| field | needed | why |
| --- | --- | --- |
| `formula_convention` | `Table63B28PsiVsPsi0EndpointConventionLedger AND Table63B28KernelTruncationAndSmoothingConventionLedger` | 必须知道表值使用 psi 还是 psi_0，以及核、截断、平滑、端点规则。 |
| `zero_inputs` | `Table63B28FiniteRHHeightEndpointAndZeroBlockLedger AND Table63B28ZeroFreeTailConstantsAndStartHeightLedger` | 必须知道有限零点块和零点自由尾项如何进入同一个公式。 |
| `budget` | `Table63B28PsiEpsilonBudgetPartitionLedger` | 必须证明所有误差项总和小于 b=28 的 2.224E-5 cap。 |
| `output_discipline` | `Table63B28DirectedUpperRoundingAndIntervalPropagationLedger AND Table63B28ReproducibleComputationHashLedger` | 必须给出外向舍入、区间传播和可复现输出。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只审计假设反例链可调用的 Table 6.3 表算法输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ActualFormulaDeclarationGateActive` | `true` | `true` | 上一证书已证明零点输入绑定必须先取得 b=28 的实际表公式或外部算法工件。 | Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger |
| `Table63B28PublishedRowStatementLedger` | `true` | `false` | b=28 的公开表行陈述已经确认：epsilon_psi=2.224E-5。 | statement only, not generator |
| `Table63B28P51UseSiteLedger` | `true` | `false` | 该表行在 Proposition 5.1 高尾拼接中可用，外部路线可接受。 | external Table 6.3 accepted |
| `Dusart10020442SourceBoundaryForTable63Ledger` | `true` | `true` | arXiv 源文件给出来源边界：有限 RH 验证、零点自由区、表行和 P5.1 使用点都能定位。 | source boundary closed |
| `Table63B28ExternalAlgorithmArtifactMissingLedger` | `true` | `true` | 当前 arXiv 源文件没有给出生成 Table 6.3 的完整显式公式算法、舍入日志或 hash。 | DusartEpsSubmittedTableAlgorithmArtifactLedger OR IndependentTable63B28RegenerationFromExplicitFormulaLedger |
| `Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger` | `false` | `false` | 实际表公式/算法工件尚未闭合：已知的是表行和使用点，不是可复现生成机制。 | DusartEpsSubmittedTableAlgorithmArtifactLedger OR IndependentTable63B28RegenerationFromExplicitFormulaLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | Table 6.3 实际表公式审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
IndependentTable63B28RegenerationFromExplicitFormulaLedger
```

