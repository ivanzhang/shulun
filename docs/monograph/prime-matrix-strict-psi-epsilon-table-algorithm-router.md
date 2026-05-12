# Prime Matrix strict psi epsilon 表计算算法路由器

**状态：** `psi_epsilon_table_algorithm_dependency_graph_closed_reproducible_algorithm_open`

psi epsilon 表算法的依赖图已经压清：P5.1 使用 theta<x 到 8e11、中段 psi(x)<1.00002841x、psi-theta 下界和 Table 6.3 的 epsilon_psi(28)。这关闭的是原文依赖图定位，不是作者侧可复现表算法。当前真正最窄点是 `1.00002841` 的来源/生成账本；该常数所在中段只有约 4.46e-11 余量，不能只按外部文字引用粗放通过。

```text
p51_dependency_graph_closed=true
published_source_boundary_identified=true
bridge_common_variables_taxonomized=true
epsilon_psi_28_source_located=true
middle_psi_upper_100002841_source_closed=false
machine_readable_table63_closed=false
theta_table64_to_8e11_source_closed=false
zero_input_binding_to_table_formula_closed=false
psi_epsilon_interval_propagation_closed=false
reproducible_table_hash_closed=false
table_computation_algorithm_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 原文边界

| item | source | location | meaning |
| --- | --- | --- | --- |
| finite RH and zero-free lineage | https://arxiv.org/pdf/1002.0442 | introduction, lines 38-48 in extracted PDF view | psi/theta estimates depend on finite zeta-zero verification and explicit zero-free regions. |
| Proposition 5.1 dependency graph | https://arxiv.org/pdf/1002.0442 | Proposition 5.1 proof, extracted lines 291-303 | theta<x to 8e11, psi-theta lower gap, middle psi upper, and epsilon_28 are all used. |
| Table 6.3 epsilon psi at b=28 | https://arxiv.org/pdf/1002.0442 | Table 6.3, extracted lines 1400-1412 | the published table contains epsilon_psi(28)=2.224E-5. |
| table interval statement | https://arxiv.org/pdf/1002.0442 | Theorem 5.2 proof, extracted lines 324-340 | the paper states table lines are valid between successive b_i for Tables 6.4 and 6.5. |

## 2. P5.1 依赖图

| node | role | status | ledger |
| --- | --- | --- | --- |
| theta(x)<x for x<=8e11 | left finite table input | published Table 6.4 route identified; repository self-contained table-to-8e11 proof open | `ThetaLessThanIdentityTable64To8e11SourceLedger` |
| psi(x)<1.00002841x on 8e11<=x<=e^28 | middle strip psi upper input | constant appears in P5.1 proof; source/generator not yet isolated | `MiddlePsiUpper100002841SourceLedger` |
| psi(x)-theta(x)>0.9999sqrt(x) | middle strip subtraction input | dependency already separated in Dusart analytic-kernel router | `PsiMinusThetaLowerGap09999SqrtSelfContainedLedger` |
| epsilon_psi(28)<=0.00002224 | high tail psi input | published Table 6.3 row b=28 identified; reproducible generator open | `EpsilonPsi28Table63SourceLedger` |

## 3. 自足替换

```text
PsiEpsilonTableComputationAlgorithmLedger
  =>
MiddlePsiUpper100002841SourceLedger AND MachineReadableDusartTable63EpsilonPsiLedger AND ThetaLessThanIdentityTable64To8e11SourceLedger AND VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger

MiddlePsiUpper100002841SourceLedger
  =>
must locate or reproduce the source of 1.00002841 before the middle strip budget can be certified

```

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计假设反例链可调用的 psi epsilon 表算法，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `PsiEpsilonTableComputationAlgorithmGateActive` | `true` | `true` | 同一显式公式口径证书已把下一最窄点压到表计算算法。 | PsiEpsilonTableComputationAlgorithmLedger |
| `DusartP51DependencyGraphForPsiEpsilonLedger` | `true` | `true` | Dusart P5.1 的表输入依赖图已从原文定位：左有限表、中段 psi 上界、psi-theta 下界和高尾 epsilon_28。 | dependency graph closed, computation algorithm still open |
| `PublishedSourceBoundaryIdentified` | `true` | `true` | 原文说明这些改进依赖有限 RH 验证和零点自由区；仓库已抽出 Gourdon/Kadiri 等来源边界。 | VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger |
| `BridgeCommonVariablesAlreadyTaxonomized` | `true` | `true` | 有限零点窗口、零点自由尾项、显式公式、预算和 hash 的共同变量表已关闭分类。 | VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `EpsilonPsi28Table63SourceLedger` | `true` | `false` | Table 6.3 给出 b=28 的 epsilon_psi 数值；这可关闭表值来源定位，但不是可复现算法证明。 | MachineReadableDusartTable63EpsilonPsiLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `MiddlePsiUpper100002841SourceLedger` | `false` | `false` | 1.00002841 是中段最薄余量处的关键常数；当前只在 P5.1 中定位到使用点，未定位其生成公式和核验方式。 | MachineReadableDusartTable63EpsilonPsiLedger OR ThetaLessThanIdentityTable64To8e11SourceLedger OR explicit middle psi computation source |
| `MachineReadableDusartTable63EpsilonPsiLedger` | `false` | `false` | 需要把 Table 6.3 转成机器可读表，并证明每个值的生成规则、舍入方向和适用区间。 | VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `ThetaLessThanIdentityTable64To8e11SourceLedger` | `false` | `false` | 需要 theta<x 到 8e11 的表源、节点覆盖和直接计算证书；仓库现有自足有限桥只到 20000。 | ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger` | `false` | `false` | 需要证明有限零点验证和零点自由尾项按同一表算法进入 Table 6.3，而不是只作为外部背景。 | LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger |
| `PsiEpsilonIntervalPropagationAndMonotonicityLedger` | `false` | `false` | 需要证明表格值如何覆盖连续区间，特别是 8e11 到 e^28 的中段和 x>=e^28 的高尾。 | PsiEpsilonTableComputationAlgorithmLedger |
| `ReproduciblePsiEpsilonTableComputationHashLedger` | `false` | `false` | 需要原始计算工件、版本、输入哈希、输出哈希和外向舍入日志。 | reproducible computation artifact |
| `PsiEpsilonTableComputationAlgorithmLedger` | `false` | `false` | 当前关闭的是 P5.1 依赖图和外部来源边界，不是表计算算法自足闭合。 | MiddlePsiUpper100002841SourceLedger AND MachineReadableDusartTable63EpsilonPsiLedger AND ThetaLessThanIdentityTable64To8e11SourceLedger AND VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger AND PsiEpsilonIntervalPropagationAndMonotonicityLedger AND ReproduciblePsiEpsilonTableComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | psi epsilon 表算法审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
MiddlePsiUpper100002841SourceLedger
```
