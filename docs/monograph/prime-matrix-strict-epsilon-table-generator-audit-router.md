# Prime Matrix strict epsilon 表生成器审计路由器

**状态：** `epsilon_table_generator_audit_extracted_values_algorithm_zero_input_hash_open`

Schoenfeld/Dusart epsilon 表生成器被进一步拆成五项：表值提取、计算算法、零点/零点自由尾项输入、区间传播规则和可复现 hash。当前只闭合表值提取；没有原始表生成算法和零点输入证书，所以不能把 `eps_psi(28)` 与 `1.00002841` 当作作者侧自足证明。

```text
epsilon_table_statement_extraction_closed=true
epsilon_table_generator_self_contained_closed=false
table_computation_algorithm_closed=false
verified_zero_and_zero_free_tail_input_closed=false
interval_propagation_closed=false
reproducible_table_hash_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 抽取表值

| symbol | value | source role | needed by |
| --- | ---: | --- | --- |
| `eps_psi_28` | `0.000022240000` | high tail x>=e^28 | `PsiEpsilonHighTailB28TableCertificate` |
| `psi_middle_upper` | `1.000028410000` | middle strip 8e11<=x<=e^28 | `PsiUpperMiddle8e11ToE28TableCertificate` |

## 2. 外部边界

- `Dusart arXiv:1002.0442`：https://arxiv.org/abs/1002.0442；source boundary for the extracted table values; not a reproducible computation artifact

## 3. 自足替换

```text
SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger
  =>
DusartTableEpsilonStatementExtractionLedger AND PsiEpsilonTableComputationAlgorithmLedger AND VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger

PsiEpsilonTableComputationAlgorithmLedger
  =>
VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计外部表值生成责任，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `EpsilonTableGeneratorGateActive` | `true` | `true` | 上一证书把下一最窄点设为 Schoenfeld/Dusart epsilon 表生成器形式化。 | SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger |
| `DusartTableEpsilonStatementExtractionLedger` | `true` | `true` | 已把 P5.1 需要的两个 psi 表值抽出为机器可读责任项。 | eps_psi_28=0.00002224; psi_middle_upper=1.00002841 |
| `TableValuesAreNotProof` | `true` | `true` | 表值提取只说明外部论文使用了这些数；作者侧自足证明还需要生成算法、零点输入和可复现工件。 | PsiEpsilonTableComputationAlgorithmLedger AND VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `PsiEpsilonTableComputationAlgorithmLedger` | `false` | `false` | 当前仓库尚无从显式公式、零点验证和零点自由尾项自动生成 eps_psi(b) 表的算法账本。 | VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger` | `false` | `false` | 表生成器需要明确使用哪些有限零点验证、高度阈值、零点自由区和尾项常数。 | Verified zeros plus zero-free/tail constants with citations or internal proof。 |
| `PsiEpsilonIntervalPropagationAndMonotonicityLedger` | `false` | `false` | 需要证明表值如何从离散 b 或有限节点传播到整段 x 区间，包含跳点、端点和单调性规则。 | PsiEpsilonTableComputationAlgorithmLedger |
| `ReproduciblePsiEpsilonTableComputationHashLedger` | `false` | `false` | 需要可复现计算文件、版本、输入数据 hash 和输出表 hash；当前只有路由证书，没有原始计算工件。 | Reproducible source tables and scripts |
| `DusartP51TableRoundingMarginAuditLedger` | `true` | `true` | P5.1 拼接余量审查已完成；这只约束表值舍入方向，不证明表值。 | DusartP51TableRoundingMarginAuditLedger |
| `SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger` | `false` | `false` | epsilon 表生成器尚未自足形式化；当前只关闭了表值提取与责任拆包。 | DusartTableEpsilonStatementExtractionLedger AND PsiEpsilonTableComputationAlgorithmLedger AND VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 表生成器审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger
```
