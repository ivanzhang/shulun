# Prime Matrix strict Table 6.3 b=28 psi/psi0 端点口径转换证书

**状态：** `table63_b28_psi_vs_psi0_endpoint_convention_closed_endpoint_tax_registered`

Table 6.3 的 b=28 表行使用普通 `psi`，仓库内部闭合的是半权端点 `psi_0`。二者差异只可能来自跳点半权，满足 `0<=psi(x)-psi_0(x)<=0.5 log x`；因此在 `x>=e^28` 上相对端点税至多 `14/e^28`。该原子闭合，且端点税远小于高尾拼接余量，但仍必须进入后续表值预算。下一最窄点是 Table 6.3 b=28 的核/截断/平滑规则。

```text
table63_b28_psi_vs_psi0_endpoint_convention_closed=true
endpoint_tax_fits_high_tail_margin=true
independent_table63_b28_regeneration_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 数值边界

| field | value |
| --- | ---: |
| `endpoint_tax_relative_bound_14_over_e28` | `9.6801601497162842131776185222379729796541382148845267987022664063153121069547269E-12` |
| `epsilon_psi_28` | `0.00002224` |
| `p51_high_tail_margin` | `0.000005338599007170435741864313292884721456150027578599007170435741864313292884721456` |
| `endpoint_tax_to_margin_ratio` | `0.0000018132397913225107944814919061727643086920131857803430857751319362002278001079588` |

## 2. 证明步骤

| step | claim | reason |
| --- | --- | --- |
| `table_target` | Table 6.3 b=28 行是普通 Chebyshev 函数 psi 的 epsilon_psi 表值。 | arXiv 源文件定义 psi(x)=sum_{p^alpha<=x} log p，表头写 epsilon_psi。 |
| `internal_formula_target` | 仓库内部精确公式闭合的是 psi_0 半权端点版本。 | internal psi0 Perron 证书声明 psi_0(x)=sum_{n<x} Lambda(n)+1/2 Lambda(x) if x is an integer。 |
| `endpoint_difference` | 对任意 x>1，0 <= psi(x)-psi_0(x) <= (1/2)log x。 | 只有当 x 恰为素数幂跳点时出现半个 Lambda(x)，且 Lambda(x)<=log x。 |
| `high_tail_relative_bound` | 对 x>=e^28，(psi(x)-psi_0(x))/x <= 14/e^28。 | (log x)/(2x) 在 x>e 上递减，故最大点为 x=e^28。 |
| `budget_registration` | 该端点税只关闭口径转换；必须在后续 b=28 预算中显式扣除。 | 端点税远小于高尾拼接余量，但不能凭空消失。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只统一 Table 6.3 重建中的函数端点口径，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `IndependentRegenerationGateActive` | `true` | `true` | 上一证书已把自足路线压到独立重建 Table 6.3 b=28。 | IndependentTable63B28RegenerationFromExplicitFormulaLedger |
| `Table63TargetsOrdinaryPsi` | `true` | `false` | 机器表行与 arXiv 表头均指向普通 psi，而不是 psi_0。 | Table63B28PsiVsPsi0EndpointConventionLedger |
| `InternalPsi0FormulaAvailable` | `true` | `true` | 仓库内部 psi_0 精确显式公式已闭合，可作为重建公式起点。 | InternalPsi0ExactExplicitFormulaClosedAllXGe20000NoTruncationCost |
| `EndpointJumpTaxBoundClosed` | `true` | `true` | psi 与 psi_0 的差只可能是一个跳点的半个 Lambda(x)，故相对税在 x>=e^28 上至多 14/e^28。 | endpoint tax registered |
| `EndpointTaxFitsHighTailMargin` | `true` | `true` | 端点税小于 P5.1 高尾拼接余量，但后续生成 2.224E-5 时仍需登记预算。 | Table63B28PsiEpsilonBudgetPartitionLedger |
| `Table63B28PsiVsPsi0EndpointConventionLedger` | `true` | `true` | Table 6.3 的普通 psi 口径可由内部 psi_0 公式无损转换，代价为显式端点税。 | closed with endpoint tax |
| `IndependentRegenerationStillOpen` | `false` | `false` | 端点口径闭合不等于重建表值；仍缺核/截断、有限零点高度、零点自由尾项、预算、舍入和 hash。 | Table63B28KernelTruncationAndSmoothingConventionLedger AND Table63B28FiniteRHHeightEndpointAndZeroBlockLedger AND Table63B28ZeroFreeTailConstantsAndStartHeightLedger AND Table63B28PsiEpsilonBudgetPartitionLedger AND Table63B28DirectedUpperRoundingAndIntervalPropagationLedger AND Table63B28ReproducibleComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | psi/psi0 端点口径转换不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
Table63B28KernelTruncationAndSmoothingConventionLedger
```

